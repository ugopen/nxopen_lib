#===================================================================================================
#               Copyright 2017 Siemens Product Lifecycle Management Software Inc.
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
#    A python script that implements Maximum Height Violation Routing Design Rule.
#
#
#===================================================================================================
import NXOpen
import NXOpen.Routing

#---------------------------------------------------------------------------------------------------
# Get the the double value from attribute
#
# \param[in]
#      attributeInfo
#         Attribute information from which double needs to be queried
#
# \return
#      Value of attribute as Double
#
def convertToReal( attribute ):

    if attribute.Type == NXOpen.NXObject.AttributeType.Real:
        return attribute.RealValue

    if attribute.Type == NXOpen.NXObject.AttributeType.Integer:
        return float( attribute.IntegerValue )

    if attribute.Type == NXOpen.NXObject.AttributeType.String:
        return float( attribute.StringValue )

    raise ValueError( 'Unexpected attribute type.' )

#---------------------------------------------------------------------------------------------------
# Gets the real value of the attribute on the given object, if any.
#
# \param[in]
#      object
#          The object to check for the attribute.
#
# \param[in]
#      attributeName
#          The name (a.k.a. title) of the attribute for which to look.
#
# \return
#          The value of the attribute, if found.
def getAttributeValue( nxObjectTag, attributeNameString ):

    nxObject = NXOpen.TaggedObjectManager.GetTaggedObject( nxObjectTag )

    attrInfoVector = nxObject.GetUserAttributes()

    for attribute in attrInfoVector:

        if attribute == None:
            continue

        if attribute.Title == attributeNameString:
            return convertToReal( attribute )

    return 0.0

#---------------------------------------------------------------------------------------------------
# Queries the list of stock devices routing through the segment
#
# \param[in]
#      segment
#          Segment through which stock devices are routed.
#
# \param[in]
#      routeManager
#          RouteManager from the current work part
#
# \return
#          List of stock stock devices referencing the segment
#
def getStockDevicesRoutedThroughSegment( segmentTag, routeManager ):
    
    stockDevicesOnSegment = []

    stockDeviceCollection = routeManager.ElectricalStockDevice

    for stockDevice in stockDeviceCollection:
        wire = stockDevice.NxEquivalent
        if wire == None:
            continue

        for singleSegment in wire.GetSegments():
            if singleSegment.Tag == segmentTag:
                stockDevicesOnSegment.append( stockDevice )

    # Use a temporary set to remove duplicate stock devices, if any.
    tempSet = set( stockDevicesOnSegment )
    stockDevicesOnSegment = list( tempSet )

    return stockDevicesOnSegment
#------------------------------------------------------------------------------------------------
# This method gives diameter of maximum size connection amongst the stock devices routing through the segment
#
# \param[in]
#      segment
#          Segment through which connections are routed
# \param[in]
#      stockDevicesOnSegment
#          List of stock devices routed through the segment
# \return
#          Maximum size diameter 
def getValueToCheckMaxHeightViolationForStockDevice( segmentTag, stockDevicesOnSegment ):

    valueToCompare = 0.0

    for stockDevice in stockDevicesOnSegment:
        maxValue = 0.0

        cableDefinition = stockDevice.FindTopmostCableDefinition()

        stockDef = None

        if cableDefinition == None:
            stockDef = stockDevice.StockDefinition
        else:
            cableDevice = cableDefinition.GetReferencingDevice()
            stockDef    = cableDevice.StockDefinition

        maxValue = stockDef.OuterDiameter
        
        if maxValue > valueToCompare:
            valueToCompare = maxValue

    return valueToCompare

#------------------------------------------------------------------------------------------------
# Queries the overstock referencing the segment
#
# \param[in]
#      segment
#         Segment from which referencing overstock needs to be queried.
# \param[in]
#      routeManager
#          RouteManager from the current work part
# \return
#          Set of overstocks referencing the segment
def getOverstocksPresentOnTheSegment( segmentTag, routeManager ):
    
    overstockOnSegment = []

    for overstockApplication in routeManager.OverstockApplications:
        
        segmentsOfOverstockApplication = overstockApplication.GetSegments()

        for currentSegment in segmentsOfOverstockApplication:

            if singleSegment.Tag == segmentTag:
                overstocks = overstockApplication.GetOverstocks()
                overstockOnSegment.append( overstocks[0] )

    return overstockOnSegment;

#---------------------------------------------------------------------------------------------------
# Check the maximum diameter of connection routing through given segment against the maximum allowed height.
#
# Creates a violation for the given reason if connection diameter exceeds specified Maximum Height value.
#
# \param[in]
#      routeManager
#          RouteManager from current work part
#
# \param[in]
#      customManager
#          CustomManager to create design Rule violation.
#
# \param[in]
#      segment
#          Routing Segment to be check for Maximum Height violation
#
# \param[in]
#      reason
#          Design Rule reason for which Maximum Height Violation needs to be checked.
def checkForMaximumHeightViolation( routeManager, customManager, segment, reason ):
    
    maxHeightAttributeName = "CABLETRAY_MAXHEIGHT"
    
    # Get value of allowed Maximum Height or Specified Maximum Height
    specifiedMaxHeightValue = getAttributeValue( segment.Tag, "CABLETRAY_MAXHEIGHT" )
    if specifiedMaxHeightValue <= 0.0:
        return

    stockDevices = getStockDevicesRoutedThroughSegment( segment.Tag, routeManager )
    if len( stockDevices ) == 0:
        return

    # Get max value diameter of connection routing through the segment
    valueToCompare = getValueToCheckMaxHeightViolationForStockDevice( segment.Tag, stockDevices )            
    
    # Get Overstocks referencing the segment
    overstocksReferencingTheSegment = getOverstocksPresentOnTheSegment( segment.Tag, routeManager )
    
    # If Overstocks are present on segment, get maximum value of diameter including overstock
    if len( overstocksReferencingTheSegment ) > 0:
    
        totalOverstockThickness = 0.0;
        for overstock in overstocksReferencingTheSegment:
            totalOverstockThickness += overstock.GetThickness().Value
        
        valueToCompare += (2 * totalOverstockThickness)

    # If current value of diameter is greater than specified maximum height value then raise violation.
    if valueToCompare > specifiedMaxHeightValue:
    
        description = "The stock exceeds the maximum height allowed for this segment. The current height is " + str( valueToCompare ) + ".The allowed height is " + str( specifiedMaxHeightValue ) + "."

        objects = [segment]
        customManager.CreateViolationForReason( "Maximum Height Violation", reason, "The segment violates Maximum Height Rule", description, objects);

#---------------------------------------------------------------------------------------------------
def createMaximumHeightDesignRule( reason, objects ):
    try:

        session        = NXOpen.Session.GetSession()
        routeManager   = session.Parts.Work.RouteManager
        customManager  = session.RouteCustomManager

        # For interactive checks, check all the segments in the work part.
        if reason == NXOpen.Routing.CustomManager.DesignRuleReason.Interactive:
            
            segmentCollection = session.Parts.Work.SegmentManager.Segments

            for segment in segmentCollection:
                checkForMaximumHeightViolation( routeManager, customManager, segment, reason )

            return
        
        # Otherwise, check the segments in the given list of objects.
        for object in objects:
            if type( object ) is NXOpen.Routing.ArcSegment or \
               type( object ) is NXOpen.Routing.LineSegment or \
               type( object ) is NXOpen.Routing.SplineSegment:
                checkForMaximumHeightViolation( routeManager, customManager, object, reason )

    except Exception as ex:
        NXOpen.UI.GetUI().NXMessageBox.Show( "Python", NXOpen.NXMessageBox.DialogType.Error, str( ex ) )
        raise ex

#---------------------------------------------------------------------------------------------------
def registerMaxHeightDesignRules():

    maxHeightViolationTitle       = "Maximum Height Violation"
    maxHeightViolationDescription = "The Maximum Height design rule makes sure the diameter of each individual connection is within the permissible limit of value specified by attribute CABLETRAY_MAXHEIGHT."
        
    customManager = NXOpen.Session.GetSession().RouteCustomManager
        
    customManager.AddDesignRule(NXOpen.Routing.CustomManager.DesignRuleReason.CreatePath,                maxHeightViolationTitle, maxHeightViolationDescription, createMaximumHeightDesignRule )
    customManager.AddDesignRule(NXOpen.Routing.CustomManager.DesignRuleReason.HealPath,                  maxHeightViolationTitle, maxHeightViolationDescription, createMaximumHeightDesignRule )
    customManager.AddDesignRule(NXOpen.Routing.CustomManager.DesignRuleReason.AssignCorner,              maxHeightViolationTitle, maxHeightViolationDescription, createMaximumHeightDesignRule )
    customManager.AddDesignRule(NXOpen.Routing.CustomManager.DesignRuleReason.AssignStock,               maxHeightViolationTitle, maxHeightViolationDescription, createMaximumHeightDesignRule )
    customManager.AddDesignRule(NXOpen.Routing.CustomManager.DesignRuleReason.RemovePart,                maxHeightViolationTitle, maxHeightViolationDescription, createMaximumHeightDesignRule )
    customManager.AddDesignRule(NXOpen.Routing.CustomManager.DesignRuleReason.AutoRoutePinLevel,         maxHeightViolationTitle, maxHeightViolationDescription, createMaximumHeightDesignRule )
    customManager.AddDesignRule(NXOpen.Routing.CustomManager.DesignRuleReason.ManualRoutePinLevel,       maxHeightViolationTitle, maxHeightViolationDescription, createMaximumHeightDesignRule )
    customManager.AddDesignRule(NXOpen.Routing.CustomManager.DesignRuleReason.AutoRouteComponentLevel,   maxHeightViolationTitle, maxHeightViolationDescription, createMaximumHeightDesignRule )
    customManager.AddDesignRule(NXOpen.Routing.CustomManager.DesignRuleReason.ManualRouteComponentLevel, maxHeightViolationTitle, maxHeightViolationDescription, createMaximumHeightDesignRule )
    customManager.AddDesignRule(NXOpen.Routing.CustomManager.DesignRuleReason.TransformPath,             maxHeightViolationTitle, maxHeightViolationDescription, createMaximumHeightDesignRule )
    customManager.AddDesignRule(NXOpen.Routing.CustomManager.DesignRuleReason.EditCharacteristic,        maxHeightViolationTitle, maxHeightViolationDescription, createMaximumHeightDesignRule )

#---------------------------------------------------------------------------------------------------
def startup( argc, args ):
    try:

        registerMaxHeightDesignRules()

    except Exception as ex:
        NXOpen.UI.GetUI().NXMessageBox.Show( "Python", NXOpen.NXMessageBox.DialogType.Error, str( ex ) )
        raise ex

