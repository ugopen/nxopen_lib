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
#    A python script that implements example Routing Design Rules.
#
#
#===================================================================================================
import NXOpen
import NXOpen.Routing

#-----------------------------------------------------------------------------------------------
def echo( message ):
    try:
        syslog = NXOpen.Session.GetSession().LogFile
        syslog.WriteLine( message )

        listingWindow = NXOpen.Session.GetSession().ListingWindow
        listingWindow.Open()
        listingWindow.WriteLine( message )

    except Exception as ex:
        NXOpen.UI.GetUI().NXMessageBox.Show( "Python", NXOpen.NXMessageBox.DialogType.Error, str( ex ) )
        raise ex

 
#-----------------------------------------------------------------------------------------------
def checkForLongSegments( designRuleName, maximumLength, segment ):
    try:    
        if segment.Length < maximumLength:
            return

        customManager = NXOpen.Session.GetSession().RouteCustomManager

        segmentList = [segment]

        customManager.CreateViolationForReason( designRuleName,
                                                NXOpen.Routing.CustomManager.DesignRuleReason.CreatePath,
                                                "This path is too long.",
                                                "Long paths need to be broken up and supported by clamps.",
                                                segmentList )

    except Exception as ex:
        NXOpen.UI.GetUI().NXMessageBox.Show( "Python", NXOpen.NXMessageBox.DialogType.Error, str( ex ) )
        raise ex

 
#-----------------------------------------------------------------------------------------------
def createPathDesignRule( reason, objects ):
    try:
        createPathName = "Create Path"
        maximumLength = 1000.0

        if reason == NXOpen.Routing.CustomManager.DesignRuleReason.Interactive:
            # For interactive checks, check all the segments in the work part.
            segmentManager    = NXOpen.Session.GetSession().Parts.Work.SegmentManager
            segmentCollection = segmentManager.Segments

            for segment in segmentCollection:
                checkForLongSegments( createPathName, maximumLength, segment )

            return

        # Otherwise, check the segments in the given list of objects.
        for object in objects:
            if type( object ) is NXOpen.Routing.SplineSegment:
               checkForLongSegments( createPathName, maximumLength, object )

    except Exception as ex:
        NXOpen.UI.GetUI().NXMessageBox.Show( "Python", NXOpen.NXMessageBox.DialogType.Error, str( ex ) )
        raise ex
 

#-----------------------------------------------------------------------------------------------
def checkForShortSegments( designRuleName, minimumLength, segment ):
    try:    
        if segment.Length > minimumLength:
            return

        customManager = NXOpen.Session.GetSession().RouteCustomManager

        segmentList = [segment]

        customManager.CreateViolationForReason( designRuleName,
                                                NXOpen.Routing.CustomManager.DesignRuleReason.SubdivideSegment,
                                                "This path is too short.",
                                                "Short segments violate our design standards.",
                                                segmentList )

    except Exception as ex:
        NXOpen.UI.GetUI().NXMessageBox.Show( "Python", NXOpen.NXMessageBox.DialogType.Error, str( ex ) )
        raise ex


#-----------------------------------------------------------------------------------------------
def subdivideSegmentDesignRule( reason, objects ):
    try:
        subdivideSegmentName = "Subdivide Segment"
        userPreferences = NXOpen.Session.GetSession().Preferences.RoutingApplicationView.RoutingUserPreferences

        tuple = userPreferences.GetDoublePreference( "ROUTE_ELEC_MIN_STRAIGHT_LENGTH_COEFF" )

        minimumLength = tuple[1]
        if not tuple[0]:
            minimumLength = 10.0 # Use a default value in case the preferences wasn't defined.

        if reason == NXOpen.Routing.CustomManager.DesignRuleReason.Interactive:
            # For interactive checks, check all the segments in the work part.
            segmentManager    = NXOpen.Session.GetSession().Parts.Work.SegmentManager
            segmentCollection = segmentManager.Segments

            for segment in segmentCollection:
                checkForShortSegments( subdivideSegmentName, minimumLength, segment )

            return

        # Otherwise, check the segments in the given list of objects.
        for object in objects:
            if type( object ) is NXOpen.Routing.SplineSegment:
               checkForShortSegments( subdivideSegmentName, minimumLength, object )

    except Exception as ex:
        NXOpen.UI.GetUI().NXMessageBox.Show( "Python", NXOpen.NXMessageBox.DialogType.Error, str( ex ) )
        raise ex

  
#-----------------------------------------------------------------------------------------------
def startup( argc, args ):
    try:
        customManager = NXOpen.Session.GetSession().RouteCustomManager

        createPathName = "Create Path"
        subdivideSegmentName = "Subdivide Segment"
        createPathDescription = "The Create Path design rule makes sure each segment on the path is not too long."
        subdivideSegmentDescription = "The Subdivide Segment design rule makes sure each new segment is not too short."

        createPathRuleId       = customManager.AddDesignRule(NXOpen.Routing.CustomManager.DesignRuleReason.CreatePath, createPathName, createPathDescription, createPathDesignRule)
        subdivideSegmentRuleId = customManager.AddDesignRule(NXOpen.Routing.CustomManager.DesignRuleReason.SubdivideSegment, subdivideSegmentName, subdivideSegmentDescription, subdivideSegmentDesignRule)


    except Exception as ex:
        NXOpen.UI.GetUI().NXMessageBox.Show( "Python", NXOpen.NXMessageBox.DialogType.Error, str( ex ) )
        raise ex

    return 0 # No errors.


