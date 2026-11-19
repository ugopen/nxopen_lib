#===================================================================================================
#
#   This material contains trade secrets or otherwise confidential information owned by
#   Siemens Industry Software Inc. or its affiliates (collectively, "SISW"), or its licensors.
#   Access to and use of this information is strictly limited as set forth in the Customer's
#   applicable agreements with SISW.
#
#   Unpublished work Copyright 2024 Siemens
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
#    A python script that implements example Routing Run plugins.
#
#
#===================================================================================================

import NXOpen
import NXOpen.UF
import NXOpen.MechanicalRouting
import NXOpen.Routing
import NXOpen.RoutingCommon
import NXOpen.Schematic.Mechanical
import collections
  
#---------------------------------------------------------------------------------------------------
# Does a string attribute with the passed in attribute title exist for the passed in object?
#
# \param[in]
#     attirbuteObject
#         The object to see if the string attribute exists
#
# \param[in]
#     attributeTitle
#         The title of the string attribute whose value you want to check exists for the passed in
#         object. For classification based objects, it will be in the format
#         "ClassIdentifier:AttributeIdentifier". This function will also match on the title
#         alias in case the classification format is not known.
#
# \return
#     True if the string attribute exists on the object, False otherwise.
#
def doesObjectHaveStringAttribute( attributeObject, attributeTitle ):
    
    attributeIterator = attributeObject.CreateAttributeIterator()

    attributeIterator.SetIncludeOnlyType(NXOpen.NXObject.AttributeType.String)   
    attributeIterator.SetIncludeAllCategories()        

    stringAttributes = attributeObject.GetUserAttributes(attributeIterator)

    if (not stringAttributes):
        return False
    
    for currentStringAttribute in stringAttributes: 
        if (currentStringAttribute.Title == attributeTitle):
            return True
        elif (currentStringAttribute.TitleAlias == attributeTitle):
            return True

    return False
    
#---------------------------------------------------------------------------------------------------
# Get the value for the string attribute with the passed in attribute title for the passed in
# object.
#
# \param[in]
#     attirbuteObject
#         The object to get the string attribute value for
#
# \param[in]
#     attributeTitle
#         The title of the string attribute whose value you want to retrieve for the passed in
#         object. For classification based objects, it will be in the format
#         "ClassIdentifier:AttributeIdentifier". This function will also match on the title
#         alias in case the classification format is not known.
#
# \return
#     The string value of the string attribute with the passed in attribute title. Empty
#     string if not found.
#
def getObjectStringAttribute( attributeObject, attributeTitle ):
    
    attributeIterator = attributeObject.CreateAttributeIterator()

    attributeIterator.SetIncludeOnlyType(NXOpen.NXObject.AttributeType.String)   
    attributeIterator.SetIncludeAllCategories()        

    stringAttributes = attributeObject.GetUserAttributes(attributeIterator)

    if (not stringAttributes):
        return ""
        
    for currentStringAttribute in stringAttributes:
        if (currentStringAttribute.Title == attributeTitle):
            return currentStringAttribute.StringValue
        elif (currentStringAttribute.TitleAlias == attributeTitle):
            return currentStringAttribute.StringValue
            
    return ""
    
#---------------------------------------------------------------------------------------------------
# Does the values for the attribute with the passed in attribute title match between the passed in
# objects.  Returns False if one or the other object does not have the attribute set on it.
#
# \param[in]
#     object1
#         The first object whose attribute value you want to compare
#
# \param[in]
#     object2
#         The second object whose attribute value you want to compare
#
# \param[in]
#     attributeTitle
#         The title of the attribute whose value you want to compare between the two objects.
#         For classification based objects, it will be in the format
#         "ClassIdentifier:AttributeIdentifier". This function will also match on the title
#         alias in case the classification format is not known.
#
# \return
#     True if the attribute exists on both objects and the value is the same between both objects.
#     False otherwise.
#
def doAttributeStringValuesMatchForObjects( object1, object2, attributeTitle ):
    
    if (not doesObjectHaveStringAttribute(object1, attributeTitle) or
        not doesObjectHaveStringAttribute(object2, attributeTitle)):
        return False
        
    object1StringValue = getObjectStringAttribute(object1, attributeTitle)
    object2StringValue = getObjectStringAttribute(object2, attributeTitle)
    
    if (object1StringValue == object2StringValue):
        return True
     
    return False

#---------------------------------------------------------------------------------------------------
# Evaluates the Schematic.Mechanical.Port object and logs any mapping status messages corresponding
# to conditions detected for the port. In this case, this example function implements two checks:
#
#    - If the port names match between 2D and 3D based on a custom mapping. If they match based on
#      this custom mapping, it removes out of the box message corresponding to the condition
#      indicating this mismatch.
#      
#    - If the 2D port's equipment has the same value for its PART_NUMBER attribute as the 3D
#      port assigned to it, it removes the out of the box message corresponding to the condition
#      indiciating this mismatch.
#
# \param[in]
#     portObject
#         The port object to evaluate.
#
# \param[in/out]
#     messageList
#         The message list to update with messages based on the evaluation of the passed in port
#         object. The passed in message list initially contains the messages corresponding to the
#         conditions for the port object detected by the out of the box evaluation done by NX for
#         the port object. See the possible values for the messages defined by
#         MechanicalRouting.RunsAssignmentManager.MappingStatusMessage. The plug-in can clear this
#         list, add individual messages to this list, or remove individual messages from this list
#         based on the evaluation of the port object.
#
# \return
#     True if you want to override the messages logged by NX gainst the passed in port object. False
#     if you want to use the out of the box messages. If True, it will use the messages returned in
#     the message list argument for final evaluation of the port object.
#
def evaluatePortRunObject( portObject, messageList ):
    
    theSession  = NXOpen.Session.GetSession()

    theRoutingManager = NXOpen.MechanicalRouting.RoutingManager.GetRoutingManager(theSession)
    
    theRunsAssignmentManager = theRoutingManager.RunsAssignmentManager
    
    assignedPorts, assignedComponents = theRunsAssignmentManager.GetPositionsLogicalPortAssignedToInSession(portObject)
    
    if (not assignedPorts):
        return False

    # If the out of the box NX evaluation fails because the 2D logical port names do not match the 3D
    # assigned port names, see if one of the following mappings apply:
    # 
    #     2D Port Name | 3D Port Name
    #     ---------------------------
    #     P1           | IN
    #     P2           | OUT
    #     IN           | P1
    #     OUT          | P2    
    #     
    # If one of the above mappings apply, then remove the message that indicates that the port
    # identifiers do not match between 2D and 3D.
    if (messageList.ContainsMessage(theRunsAssignmentManager.MappingStatusMessage.PortIdentifierDoesNotMatchLogicalPortIdentifier)):

        if (assignedPorts):

            # 2D port name to expected 3D port name mapping
            portNameMap = {
                    "P1": "IN",
                    "P2": "OUT",
                    "IN": "P1",
                    "OUT": "P2"
                }
        
            for assignedPort in assignedPorts:
                if (portObject.Identifier in portNameMap.values()):
                    
                    expectedPortName = portNameMap.get(portObject.Identifier)
                    
                    if (expectedPortName == assignedPort.Name):
                        messageList.RemoveMessage(theRunsAssignmentManager.MappingStatusMessage.PortIdentifierDoesNotMatchLogicalPortIdentifier)

    # If the out of the box NX evaluation fails matching the 2D logical equipment to the placed 3D
    # equipment, compare the values of the PART_NUMBER attributes on the 2D logical equipment and
    # the assigned 3D component. If they match, remove the the message about the 3D assigned
    # equipment not matching the 2D logical equipment.
    if (messageList.ContainsMessage(theRunsAssignmentManager.MappingStatusMessage.AssignedEquipmentDoesNotMatchLogicalEquipment)):
        
        portOwningJunction = portObject.GetOwningJunction()
        
        junctionAttributeOwner = portOwningJunction.GetClassificationAttributeOwner()

        # For WAVE linked ports, the PART_NUMBER will be inherited from the WAVE linked component so check for it on the assigned port object
        for assignedPort in assignedPorts:
            if (doAttributeStringValuesMatchForObjects(junctionAttributeOwner, assignedPort, "PART_NUMBER")):
                messageList.RemoveMessage(theRunsAssignmentManager.MappingStatusMessage.AssignedEquipmentDoesNotMatchLogicalEquipment)
                        
        # Check the PART_NUMBER on the assigned component object
        for assignedComponent in assignedComponents:
            if (doAttributeStringValuesMatchForObjects(junctionAttributeOwner, assignedComponent, "PART_NUMBER")):
                messageList.RemoveMessage(theRunsAssignmentManager.MappingStatusMessage.AssignedEquipmentDoesNotMatchLogicalEquipment)

    # IMPORTANT NOTE: Other messages that were logged against the port object will be left untouched in the message list.

    # Returning True indicates it overrides the out of the box NX evaluation
    return True
   
#---------------------------------------------------------------------------------------------------
# Evaluates the Schematic.Mechanical.Connection object and logs any mapping status messages
# corresponding to conditions detected for the port. In this case, this example function implements
# one check:
#      
#    - If the 2D connection has the same value for its PART_NUMBER attribute as the 3D stock
#      components assigned to it, it removes the out of the box message corresponding to the
#      condition indiciating this mismatch.
#
# \param[in]
#     connectionObject
#         The connection object to evaluate.
#
# \param[in/out]
#     messageList
#         The message list to update with messages based on the evaluation of the passed in
#         connection object. The passed in message list initially contains the messages corresponding
#         to the conditions for the connection object detected by the out of the box evaluation done
#         by NX for the connection object. See the possible values for the messages defined by
#         MechanicalRouting.RunsAssignmentManager.MappingStatusMessage. The plug-in can clear this
#         list, add individual messages to this list, or remove individual messages from this list
#         based on the evaluation of the port object.
#
# \return
#     True if you want to override the messages logged by NX gainst the passed in connection object.
#     False if you want to use the out of the box messages. If True, it will use the messages
#     returned in the message list argument for final evaluation of the connection object.
#
def evaluateConnectionRunObject( connectionObject, messageList ):
    
    theSession  = NXOpen.Session.GetSession()

    theRoutingManager = NXOpen.MechanicalRouting.RoutingManager.GetRoutingManager(theSession)
    
    theRoutingCommonRoutingManager = NXOpen.RoutingCommon.RoutingManager.GetRoutingManager(theSession)
    
    theRunsAssignmentManager = theRoutingManager.RunsAssignmentManager
    
    # If the out of the box NX evaluation fails matching the 2D logical connection to the placed 3D
    # stock components, compare the values of the PART_NUMBER attributes on the 2D logical
    # connection and the assigned 3D stock components. If they match, remove the the message about
    # the 3D assigned stock components not matching the 2D logical connection.
    if (messageList.ContainsMessage(theRunsAssignmentManager.MappingStatusMessage.AssignedStockDoesNotMatchLogicalStock)):

        assignedComponents = theRunsAssignmentManager.GetComponentsLogicalConnectionAssignedToInSession(connectionObject)

        if (assignedComponents):

            connectionAttributeOwner = connectionObject.GetStockAttributeOwner()

            workPart = theSession.Parts.Work

            foundMismatch = False

            for assignedComponent in assignedComponents:
                if (theRoutingCommonRoutingManager.IsStockComponentPart(assignedComponent.Prototype)):
                    if (not doAttributeStringValuesMatchForObjects(assignedComponent, connectionAttributeOwner, "PART_NUMBER")):
                        foundMismatch = True

            # If there is no mismatch based on the PART_NUMBER with ALL the assigned 3D stock components, we can remove the message
            if (not foundMismatch):
                messageList.RemoveMessage(theRunsAssignmentManager.MappingStatusMessage.AssignedStockDoesNotMatchLogicalStock)
    
    # IMPORTANT NOTE: Other messages that were logged against the connection object will be left untouched in the message list.

    # Returning True indicates it overrides the out of the box NX evaluation
    return True
   
#---------------------------------------------------------------------------------------------------
# Evaluates the Schematic.Mechanical.Branch object and logs any mapping status messages
# corresponding to conditions detected for the branch. In this case, this function does nothing
# except return False to indicate that the out of the box mapping status messages logged by NX
# against the branch should be used.
#
# \param[in]
#     branchObject
#         The branch object to evaluate.
#
# \param[in/out]
#     messageList
#         The message list to update with messages based on the evaluation of the passed in branch
#         object. The passed in message list initially contains the messages corresponding to the
#         conditions for the branch object detected by the out of the box evaluation done by NX for
#         the branch object. See the possible values for the messages defined by
#         MechanicalRouting.RunsAssignmentManager.MappingStatusMessage. The plug-in can clear this
#         list, add individual messages to this list, or remove individual messages from this list
#         based on the evaluation of the branch object.
#
# \return
#     True if you want to override the messages logged by NX gainst the passed in branch object.
#     False if you want to use the out of the box messages. If True, it will use the messages
#     returned in the message list argument for final evaluation of the branch object.
#
def evaluateBranchRunObject( branchObject, messageList ):
    
    # Returning False indicates it does not override the out of the box NX evaluation
    return False
   
#---------------------------------------------------------------------------------------------------
# Evaluates the Schematic.Mechanical.Run object and logs any mapping status messages corresponding
# to conditions detected for the run. In this case, this function does nothing except return False
# to indicate that the out of the box mapping status messages logged by NX against the run should be
# used.
#
# \param[in]
#     runObject
#         The run object to evaluate.
#
# \param[in/out]
#     messageList
#         The message list to update with messages based on the evaluation of the passed in run
#         object. The passed in message list initially contains the messages corresponding to the
#         conditions for the run object detected by the out of the box evaluation done by NX for the
#         run object. See the possible values for the messages defined by
#         MechanicalRouting.RunsAssignmentManager.MappingStatusMessage. The plug-in can clear this
#         list, add individual messages to this list, or remove individual messages from this list
#         based on the evaluation of the run object.
#
# \return
#     True if you want to override the messages logged by NX gainst the passed in run object. False
#     if you want to use the out of the box messages. If True, it will use the messages returned in
#     the message list argument for final evaluation of the run object.
#
def evaluateRunObject( runObject, messageList ):
        
    # Returning False indicates it does not override the out of the box NX evaluation
    return False

#---------------------------------------------------------------------------------------------------
# Called by the run evaluation code to evaluate the pieces of the run in regards to their
# fulfillment in the Routed System Designer assembly. This plug-in can clear, add, or remove any
# messages corresponding to conditions detected for the run object during the evaluation.  Based on
# the final list of messages logged againt a single run object, the final evaluation of the run
# object is determined. The final evaluation of a single run object is determined by message with
# the most severe evalutation, ultimately determining the run object's status of passing, warning,
# or failure.
# 
# IMPORTANT NOTE: You can override the severity of each mapping status message from the out of the
#                 box NX evaluation by implementing the mapping status message evaluation plug-in.
#
# \param[in]
#     runObject
#         The run object to be evaluated.  The run object will be one of the following types:
#
#             Scehmatic.Mechanical.Port
#             Scehmatic.Mechanical.Connection
#             Schematic.Mechanical.Branch
#             Schematic.Mechanical.Run
#
# \param[in/out]
#     messageList
#         The message list to update with messages based on the evaluation of the passed in run
#         object. The passed in message list initially contains the messages corresponding to the
#         conditions for the run object detected by the out of the box evaluation done by NX for the
#         run object. See the possible values for the messages defined by
#         MechanicalRouting.RunsAssignmentManager.MappingStatusMessage. The plug-in can clear this
#         list, add individual messages to this list, or remove individual messages from this list
#         based on the evaluation of the run object.
#
# \return
#     True if you want to override the messages logged by NX gainst the passed in run object. False
#     if you want to use the out of the box messages. If True, it will use the messages returned in
#     the message list argument for final evaluation of the run object.
#
def runObjectEvaluationPlugin( runObject, messageList ):
  
    try:

        # Based on the type of run object, call the specific function to evaluate it
        if (isinstance(runObject, NXOpen.Schematic.Mechanical.Port)):
            return evaluatePortRunObject(runObject, messageList)
        elif (isinstance(runObject, NXOpen.Schematic.Mechanical.Connection)):
            return evaluateConnectionRunObject(runObject, messageList)
        elif (isinstance(runObject, NXOpen.Schematic.Mechanical.Branch)):
            return evaluateBranchRunObject(runObject, messageList)
        elif (isinstance(runObject, NXOpen.Schematic.Mechanical.Run)):
            return evaluateRunObject(runObject, messageList)            

    except Exception as ex:
        NXOpen.UI.GetUI().NXMessageBox.Show( "Python", NXOpen.NXMessageBox.DialogType.Error, str( ex ) )
        raise ex

    # Returning False indicates it does not override out of the box NX evaluation
    return False 

#---------------------------------------------------------------------------------------------------
# Called by the run evaluation code to evaluate individual messages logged against a run object
# during its evaluation to determine if the message corresponds to a condition that is passing,
# a warning, a failure or it cannot be evaluated. This allows you to override the out of the box
# NX evaluation for each of these messages. This evaluation shows up in the status column in the
# Run Navigator in the Routed System Designer Mechanical application and is reflected in the
# evaluation status returned from MechanicalRouting.RunsAssignmentManager for a given run object. 
#
# \param[in]
#     message
#         The message corresponding to the condition that run objects are checked for, for which
#         you want to override the evaluation for. See the possible values for the messages defined
#         by MechanicalRouting.RunsAssignmentManager.MappingStatusMessage.
#
# \return
#     Evaluation of the passed in message. The evaluation will be one of the following values:
#
#         MechanicalRouting.RunsAssignmentManager.MappingStatus.Unknown
#         MechanicalRouting.RunsAssignmentManager.MappingStatus.Pass
#         MechanicalRouting.RunsAssignmentManager.MappingStatus.Warning
#         MechanicalRouting.RunsAssignmentManager.MappingStatus.Error
#         MechanicalRouting.RunsAssignmentManager.MappingStatus.CannotBeEvaluated
#
#     If you desire to use the default out of the box NX evaluation, the value
#     MechanicalRouting.RunsAssignmentManager.MappingStatus.Unknown should be returned.
#
def runMappingStatusMessageEvaluationPlugin( message ):
  
    theSession  = NXOpen.Session.GetSession()

    theRoutingManager = NXOpen.MechanicalRouting.RoutingManager.GetRoutingManager(theSession)

    runsAssignmentManager = theRoutingManager.RunsAssignmentManager
        
    try:

        # Evaluate these messages as errors overriding out of the box evaluation as warnings
        if (message == runsAssignmentManager.MappingStatusMessage.AssignedStockDoesNotMatchLogicalStock):
            return theRoutingManager.RunsAssignmentManager.MappingStatus.Error
        elif (message == runsAssignmentManager.MappingStatusMessage.AssignedEquipmentDoesNotMatchLogicalEquipment):
            return theRoutingManager.RunsAssignmentManager.MappingStatus.Error
        elif (message == runsAssignmentManager.MappingStatusMessage.PortIdentifierDoesNotMatchLogicalPortIdentifier):
            return theRoutingManager.RunsAssignmentManager.MappingStatus.Error

    except Exception as ex:
        NXOpen.UI.GetUI().NXMessageBox.Show( "Python", NXOpen.NXMessageBox.DialogType.Error, str( ex ) )
        raise ex

    # Returning Unknown will cause it to use the NX default out of the box standard mapping status message evaluation
    return theRoutingManager.RunsAssignmentManager.MappingStatus.Unknown
    
#---------------------------------------------------------------------------------------------------
# Called by the Run Navigator in the Routed System Designer Mechanical application as well as
# the MechanicalRouting.RunsAssignmentManager to return the user facing string for an individual
# mapping status message logged against a run object during its evaluation. This user string is
# diplayed in the alert column in the Run Navigator.
#
# \param[in]
#     message
#         The mapping status message corresponding to the condition that run objects are checked
#         for, for which you want provide a user facing string for. See the possible values
#         defined by MechanicalRouting.RunsAssignmentManager.MappingStatusMessage. 
#
# \return
#     User facing string for the passed in message. If you desire to use the default out of the box
#     NX user facing, an empty string should be returned.
#
def runMappingStatusMessageUserStringPlugin( message ):
  
    theSession  = NXOpen.Session.GetSession()

    theRoutingManager = NXOpen.MechanicalRouting.RoutingManager.GetRoutingManager(theSession)
    
    runsAssignmentManager = theRoutingManager.RunsAssignmentManager
        
    try:
        
        # Override of the out of the box user facing strings for these messages
        if (message == runsAssignmentManager.MappingStatusMessage.AssignedStockDoesNotMatchLogicalStock):
            return "The 2D logical connection PART_NUMBER attribute did not match the PART_NUMBER attribute of the assigned 3D stock components"
        elif (message == runsAssignmentManager.MappingStatusMessage.AssignedEquipmentDoesNotMatchLogicalEquipment):
            return "The 2D logical equipment PART_NUMBER attribute did not match the PART_NUMBER attribute of the assigned 3D port"

    except Exception as ex:
        NXOpen.UI.GetUI().NXMessageBox.Show( "Python", NXOpen.NXMessageBox.DialogType.Error, str( ex ) )
        raise ex

    # Returning an empty string will cause it to use the default NX out of the box user facing string for this message
    return ""

#---------------------------------------------------------------------------------------------------
def startup( argc, args ):

    NXOpen.Session.GetSession().CreateMechanicalRoutingSession()
  
    customManager = NXOpen.Session.GetSession().MechanicalRoutingCustomManager

    customManager.RemoveAllPlugins()
   
    customManager.SetRunFulfillmentEvaluationPlugin( runObjectEvaluationPlugin )
    customManager.SetRunMappingStatusMessageEvaluationPlugin( runMappingStatusMessageEvaluationPlugin )
    customManager.SetRunMappingStatusMessageStringPlugin( runMappingStatusMessageUserStringPlugin )

    return 0 # No errors.
