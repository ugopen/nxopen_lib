#===================================================================================================
#
#   This material contains trade secrets or otherwise confidential information owned by
#   Siemens Industry Software Inc. or its affiliates (collectively, "SISW"), or its licensors.
#   Access to and use of this information is strictly limited as set forth in the Customer's
#   applicable agreements with SISW.
#
#   Unpublished work Copyright 2023 Siemens
#
#===================================================================================================
#
#    NOTE:  NX Development provides programming examples for illustration only.
#    NX Development assumes you are familiar with the programming language
#    demonstrated in these examples, and the tools used to create and debug NX/Open
#    programs. GTAC support professionals can help explain the functionality of
#    a particular procedure, but neither GTAC nor NX Development will modify
#    these examples to provide added functionality or construction procedures.
#
#File description:
#
#    A python script that implements example Routing Spool plugins.
#
#
#===================================================================================================
import NXOpen
import NXOpen.Assemblies
import NXOpen.MechanicalRouting
import NXOpen.RoutingCommon
import NXOpen.Schematic.Mechanical
import NXOpen.UF

from types import NoneType

#---------------------------------------------------------------------------------------------------
# Returns true and the attribute information object of the attribute if the attribute is in the list.
# Returns false if not.
# NOTE: The attribute name comparison is case insensitive.
def getAttributeFromList( attributes, attributeName ):
 
    for attribute in attributes:
        # Watch out for attributes with no title.
        if len( attribute.Title ) == 0:
            continue
 
        # NOTE: This does not look for aliases on the attribute titles.
        if attribute.Title.lower() == attributeName.lower():
            return attribute
 
    return None
 
#---------------------------------------------------------------------------------------------------
# Returns true and the attribute information object of the attribute if the attribute exists.
# Returns false if not.
def getAttributeFromObject( nxObject, attributeName ):
 
    return getAttributeFromList( nxObject.GetUserAttributes(), attributeName )
 
#---------------------------------------------------------------------------------------------------
# Returns the string value of the attribute or None if it does not exist.
def getStringAttributeValueFromObject( nxObject, attributeName ):
 
    attributeInformation = getAttributeFromObject( nxObject, attributeName )
 
    if attributeInformation == None or attributeInformation.Type != NXOpen.NXObject.AttributeType.String:
        return None
 
    return attributeInformation.StringValue

#---------------------------------------------------------------------------------------------------
# Returns the spool part's name as the "Block" to add to the spool name.
def getBlock( spoolPart ):
    if spoolPart is None:
        return ""

    return spoolPart.Name

#---------------------------------------------------------------------------------------------------
# Uses the runs assignment manager to figure out which run this component belongs to.
def getRun( runsManager, component ):

    runs = runsManager.GetAssignedRuns(component)

    for run in runs:
        runId = run.Identifier
        if type(runId) != NoneType and len( runId ) > 0:
            return runId

    return ""

#---------------------------------------------------------------------------------------------------
# Gets the specification and the run from the components selected for the spool.
def getSpecificationAndRun(spoolComponents):

    specification = ""
    runId = ""

    session = NXOpen.Session.GetSession()

    runsManager = NXOpen.MechanicalRouting.RoutingManager.GetRoutingManager(session).RunsAssignmentManager

    for spoolComponent in spoolComponents:

        componentSpecification = getStringAttributeValueFromObject(spoolComponent, "SPECIFICATION")
        if type(componentSpecification) != NoneType and len( componentSpecification ) > 0:
            specification = componentSpecification

        componentRun = getRun(runsManager, spoolComponent)
        if type(componentRun) != NoneType and len( componentRun ) > 0:
            runId = componentRun

        if len( specification ) > 0 and len( runId ) > 0:
            break

    return specification, runId

#---------------------------------------------------------------------------------------------------
# Builds a description of the spool that includes:
# 
#   - Prefix:        The spool Name Prefix defined in the Routed System Designer->Mechanical->Spools customer defaults.
#   - Block:         The Block identifier is simply the name of the work part.
#   - Specification: The specification assigned to the components.
#   - Run ID:        The identifier of the run to which the components belong.
#
def buildSpoolDescription( spoolPart, spoolComponents ):

    session = NXOpen.Session.GetSession()

    prefix    = session.OptionsManager.GetStringValue("RSD_SpoolNamePrefix")
    blockName = getBlock(spoolPart)
    
    specification, runId = getSpecificationAndRun(spoolComponents)
    
    description = ""
    if len( prefix ) > 0:
        description = prefix

    if len( blockName ) > 0:
        description += blockName + " "

    if len( specification ) > 0:
        description += specification + " "

    if len( runId ) > 0:
        description += runId + " "

    return description

#---------------------------------------------------------------------------------------------------
# Returns the name of the spool that owns the given components.
# 
# This assumes all components belong to the same spool and only belong to one spool.
# 
def getSpoolName( spoolComponents ):
    if len( spoolComponents ) == 0:
        return ""

    session         = NXOpen.Session.GetSession()
    workPart        = session.Parts.Work
    spoolCollection = workPart.MechanicalRoutingCollectionsManager.Spools

    spool = spoolCollection.GetSpoolFromComponent( spoolComponents[0] )
    if spool == None:
        return ""
    
    return spool.Name

#---------------------------------------------------------------------------------------------------
# Called by the Spool dialog to create a name for the new spool.
# 
# The name this plugin generates is a combination of:
# 
#   - Prefix:        The spool Name Prefix defined in the Routed System Designer->Mechanical->Spools customer defaults.
#   - Block:         The Block identifier is simply the name of the work part.
#   - Specification: The specification assigned to the components.
#   - Run ID:        The identifier of the run to which the components belong.
#   - Index:         An index one greater than the number of existing spools in the part.
#
# \param[in]
#      spoolPart
#          The part in which the new spool is created.
#
# \param[in]
#      spoolComponents
#          The connected components that will make up the new spool.
#
# \return
#      The name the Routing application will use for the new spool.
def generateSpoolName( spoolPart, spoolComponents ):

    generatedName = buildSpoolDescription( spoolPart, spoolComponents )

    spools = spoolPart.MechanicalRoutingCollectionsManager.Spools
    nSpools = 0
    for spool in spools:
        nSpools += 1

    generatedName += "{:02d}".format(nSpools)

    message = generatedName
    message += " was created."

    listingWindow = NXOpen.Session.GetSession().ListingWindow
    listingWindow.Open()
    listingWindow.WriteFullline(message)

    return generatedName

#---------------------------------------------------------------------------------------------------
# Called by the Publish Spool Assemblies command to create a name for the new spool assembly part.
#
# The spool assembly name plugin is given a data object that needs to be filled out
# completely, either for a native file or a Teamcenter item.
#
# \param[in]
#      spoolComponents
#          The components of the spool that are to go in the new spool assembly.
# 
# \param[out]
#      dataObject
#          The data object that is to be filled out by the plugin.
def generateSpoolAssemblyName( spoolComponents, dataObject ):

    try:
        if not hasattr(generateSpoolAssemblyName, "spoolAssemblyCounter"):
            generateSpoolAssemblyName.spoolAssemblyCounter = 0  # it doesn't exist yet, so initialize it

        generateSpoolAssemblyName.spoolAssemblyCounter += 1

        assemblyName = "SpoolAssembly_" + str( generateSpoolAssemblyName.spoolAssemblyCounter )
        homeFolder = ""

        session = NXOpen.Session.GetSession()

        if session.PdmSession is None:
            dataObject.NativeFileName = assemblyName
            dataObject.NativePath     = "" # An empty path means the current directory.
            return

        ugmgr = NXOpen.UF.UFSession.GetUFSession().Ugmgr

        rootFolderTag = ugmgr.AskRootFolder()
        homeFolder    = ugmgr.AskFolderName( rootFolderTag )

        dataObject.ManagedModeFolderName      = homeFolder + ":SpoolAssemblies"
        dataObject.ManagedModeItemName        = "" # Return an empty item name to get the next available item ID.
        dataObject.ManagedModeItemRevision    = "A"
        dataObject.ManagedModeItemType        = "Item"
        dataObject.ManagedModeItemDescription = getSpoolName( spoolComponents )

    except Exception as ex:
        NXOpen.UI.GetUI().NXMessageBox.Show( "Python", NXOpen.NXMessageBox.DialogType.Error, str( ex ) )
        raise ex

#---------------------------------------------------------------------------------------------------
def startup( argc, args ):

    NXOpen.Session.GetSession().CreateRoutingSession()

    customManager = NXOpen.Session.GetSession().RoutingCustomManager

    customManager.SetSpoolNamePlugin( generateSpoolName )
    customManager.SetSpoolAssemblyNamePlugin( generateSpoolAssemblyName )
    
    NXOpen.Session.GetSession().LicenseManager.ReleaseAll( None )

    return 0 # No errors.

