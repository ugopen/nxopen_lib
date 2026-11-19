/*==================================================================================================
               Copyright 2017 Siemens Product Lifecycle Management Software Inc.
====================================================================================================

    NOTE:  NX Development provides programming examples for illustration only.
    NX Development assumes you are familiar with the programming language
    demonstrated in these examples, and the tools used to create and debug NX/Open
    programs. GTAC support professionals can help explain the functionality of
    a particular procedure, but neither GTAC nor NX Development will modify
    these examples to provide added functionality or construction procedures.

File description:

    A C# class that implements example Routing Design Rules.


==================================================================================================*/
using System;
using NXOpen;
using NXOpen.Preferences;
using NXOpen.Routing;
using NXOpen.Routing.Electrical;
using System.Collections.Generic;

namespace Routing
{
    public class DesignRules
    {
        // Static class members
        static Session theSession = null;
        static ListingWindow listingWindow = null;
        static CustomManager customManager = null;
        static int createPathRuleId = 0;
        static int subdivideSegmentRuleId = 0;

        //------------------------------------------------------------------------------------------
        // Called when NX starts up to register the Design Rules.
        public static int Startup()
        {
            if (theSession == null)
                theSession = Session.GetSession();

            if (listingWindow == null)
                listingWindow = theSession.ListingWindow;

            if (customManager == null)
                customManager = theSession.RouteCustomManager;

            RegisterDesignRules();

            return 0;
        }

        //------------------------------------------------------------------------------------------
        // Called from File->Execute->NX Open. Useful for testing.
        public static void Main()
        {
            if (theSession == null)
                theSession = Session.GetSession();

            if (listingWindow == null)
                listingWindow = theSession.ListingWindow;

            if (customManager == null)
                customManager = theSession.RouteCustomManager;

            RegisterDesignRules();
        }

        //------------------------------------------------------------------------------------------
        // Called by both Main and Startup to register the Design Rules.
        private static void RegisterDesignRules()
        {
            string createPathName = "Create Path";
            string subdivideSegmentName = "Subdivide Segment";
            string createPathDescription = "The Create Path design rule makes sure each segment on the path is not too long.";
            string subdivideSegmentDescription = "The Subdivide Segment design rule makes sure each new segment is not too short.";

            createPathRuleId = customManager.AddDesignRule(CustomManager.DesignRuleReason.CreatePath, createPathName, createPathDescription, CreatePathDesignRule);
            subdivideSegmentRuleId = customManager.AddDesignRule(CustomManager.DesignRuleReason.SubdivideSegment, subdivideSegmentName, subdivideSegmentDescription, SubdivideSegmentDesignRule);
        }

        //------------------------------------------------------------------------------------------
        static void CreatePathDesignRule
        (
            CustomManager.DesignRuleReason reason,
            NXObject[] nxObjects
        )
        {
            string createPathName = "Create Path";

            double maximumLength = 1000.0;

            if (reason == CustomManager.DesignRuleReason.Interactive)
            {
                // For interactive checks, check all the segments in the work part.
                SegmentManager segmentManager = theSession.Parts.Work.SegmentManager;
                ISegmentCollection segmentCollection = segmentManager.Segments;

                foreach (ISegment segment in segmentCollection)
                    checkForLongSegments(createPathName, maximumLength, segment);

                return;
            }

            // Otherwise, check the segments in the given list of objects.
            foreach (NXObject nxObject in nxObjects)
            {
                if (nxObject.GetType() == typeof(SplineSegment))
                    checkForLongSegments(createPathName, maximumLength, (ISegment)nxObject);
            }
        }

        //------------------------------------------------------------------------------------------
        // Checks the length of the given segment against the maximum allowed length.
        //
        // Creates a violation for the given reason if the segment is too long.
        //
        // \param[in]
        //      maximumLength
        //          The longest length allowed.
        //
        // \param[in]
        //      segment
        //          The segment to check.
        static void checkForLongSegments
        (
            string designRuleName,
            double maximumLength,
            ISegment segment
        )
        {
            if (segment.Length < maximumLength)
                return;

            List<NXObject> objects = new List<NXObject>();
            objects.Add((Curve)segment);

            customManager.CreateViolationForReason(designRuleName,
                                                   CustomManager.DesignRuleReason.CreatePath,
                                                   "This path is too long.",
                                                   "Long paths need to be broken up and supported by clamps.",
                                                   objects.ToArray());
        }

        //------------------------------------------------------------------------------------------
        static void SubdivideSegmentDesignRule
        (
            CustomManager.DesignRuleReason reason,
            NXObject[] nxObjects
        )
        {
            string subdivideSegmentName = "Subdivide Segment";

            RoutingUserPreferences userPreferences = theSession.Preferences.RoutingApplicationView.RoutingUserPreferences;

            double minimumLength = 0.0;
            if (!userPreferences.GetDoublePreference("ROUTE_ELEC_MIN_STRAIGHT_LENGTH_COEFF", out minimumLength))
                minimumLength = 10.0;

            if (reason == CustomManager.DesignRuleReason.Interactive)
            {
                // For interactive checks, check all the segments in the work part.
                SegmentManager segmentManager = theSession.Parts.Work.SegmentManager;
                ISegmentCollection segmentCollection = segmentManager.Segments;

                foreach (ISegment segment in segmentCollection)
                    checkForShortSegments(subdivideSegmentName, minimumLength, segment);

                return;
            }

            // Otherwise, check the segments in the given list of objects.
            foreach (NXObject nxObject in nxObjects)
            {
                if (nxObject.GetType() == typeof(SplineSegment))
                    checkForShortSegments(subdivideSegmentName, minimumLength, (ISegment)nxObject);
            }
        }

        //------------------------------------------------------------------------------------------
        // Checks the length of the given segment against the minimum allowed length.
        //
        // Creates a violation for the given reason if the segment is too short.
        //
        // \param[in]
        //      minimumLength
        //          The shortest length allowed.
        //
        // \param[in]
        //      segment
        //          The segment to check.
        static void checkForShortSegments
        (
            string designRuleName,
            double minimumLength,
            ISegment segment
        )
        {
            if (segment.Length > minimumLength)
                return;

            List<NXObject> objects = new List<NXObject>();
            objects.Add((Curve)segment);

            customManager.CreateViolationForReason(designRuleName,
                                                   CustomManager.DesignRuleReason.SubdivideSegment,
                                                   "This segment is too short.",
                                                   "Short segments violate our design standards.",
                                                   objects.ToArray());
        }

        //------------------------------------------------------------------------------------------
        // Tells NX when to unload your application.
        // For Routing callbacks, plugins, and Design Rules, this MUST return AtTermination.
        public static int GetUnloadOption(string arg)
        {
            return System.Convert.ToInt32(Session.LibraryUnloadOption.AtTermination);
        }
    }
}
