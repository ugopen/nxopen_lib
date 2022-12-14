#ifndef NXOpen_PREFERENCES_ROUTINGELECTRICAL_HXX_INCLUDED
#define NXOpen_PREFERENCES_ROUTINGELECTRICAL_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Preferences_RoutingElectrical.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Preferences
    {
        class RoutingElectrical;
    }
    namespace Preferences
    {
        class RoutingApplicationView;
    }
    namespace Preferences
    {
        /** The RoutingElectrical object stores a set of route electrical
                preferences.  A valid application view file is necessary to get
                values other than defaults for the electrical preferences.  <br> To obtain an instance of this class, refer to @link RoutingApplicationView RoutingApplicationView@endlink  <br> */
        class NXOPENCPPEXPORT RoutingElectrical
        {
            /** How to create terminal segments (if creating terminal segments). */
            public: enum CreateTerminalsType
            {
                CreateTerminalsTypeAll/** Create terminals to all terminals */,
                CreateTerminalsTypeListed/** Create terminals to listed terminals */,
                CreateTerminalsTypeRouted/** Create terminals to routed terminals */
            };

            /** Manual/Auto Assign component uses the component match method to determine
                        which component(s) are candidates for assignment to a component list record.

                        Matching consists of matching the:
                         o the file name of a component
                         o the component name
                         o Part Name field of the component list record to an attribute

                        If attribute name matching is specified, indicate the name of the attribute. */
            public: enum ComponentMatchType
            {
                ComponentMatchTypeFileName/** Match file name during component assignment. */,
                ComponentMatchTypeComponentName/** Match component name during component assignment. */,
                ComponentMatchTypeAttributeName/** Match attribute name during component assignment. */
            };

            private: NXOpen::Preferences::RoutingApplicationView* m_owner;
            public: explicit RoutingElectrical(NXOpen::Preferences::RoutingApplicationView *owner): m_owner(owner)
            {
            }
            public: tag_t Tag() const;
            /**Returns  the create terminals option.   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXOpen::Preferences::RoutingElectrical::CreateTerminalsType CreateTerminalsOption
            (
            );
            /**Sets  the create terminals option.   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void SetCreateTerminalsOption
            (
                NXOpen::Preferences::RoutingElectrical::CreateTerminalsType create_terminals_option /** */
            );
            /**Returns  the terminal segment solid display option  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: bool TerminalSegmentSolidDisplay
            (
            );
            /**Sets  the terminal segment solid display option  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void SetTerminalSegmentSolidDisplay
            (
                bool terminal_segment_solid /** */
            );
            /**Returns  the option to override the harness name on imported electrical data.
                        If the override_harness_name attribute is set to true, then the
                        default harness name replaces empty and non-empty Harness fields in
                        imported connection/component lists.  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: bool OverrideHarnessName
            (
            );
            /**Sets  the option to override the harness name on imported electrical data.
                        If the override_harness_name attribute is set to true, then the
                        default harness name replaces empty and non-empty Harness fields in
                        imported connection/component lists.  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void SetOverrideHarnessName
            (
                bool override_harness_name /** */
            );
            /** Gets the default harness name.  The default harness name replaces
                        the Harness field value of any records in an imported
                        connection/component list that are empty.  A blank string in the
                        Default_Harness_Name element below replaces blank Harness fields
                        with the leaf name of the work part.   @return   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXString GetDefaultHarnessName
            (
            );
            /** Sets the default harness name  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void SetDefaultHarnessName
            (
                const NXString & default_harness_name /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /**Returns  the level at which to automatically route a path.  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: bool AutomaticRouteLevel
            (
            );
            /**Sets  the level at which to automatically route a path.  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void SetAutomaticRouteLevel
            (
                bool is_pin_level_route /** */
            );
            /**Returns  the option to report auto/manual route errors to the listing window.  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: bool ReportRouteErrors
            (
            );
            /**Sets  the option to report auto/manual route errors to the listing window.  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void SetReportRouteErrors
            (
                bool report_route_errors /** */
            );
            /**Returns  the option to highlight a wire in the connection list navigator.  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: bool HighlightWire
            (
            );
            /**Sets  the option to highlight a wire in the connection list navigator.  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void SetHighlightWire
            (
                bool highlight_wire /** */
            );
            /**Returns  the component match option for automatic/manual component assignment.  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXOpen::Preferences::RoutingElectrical::ComponentMatchType ComponentMatchMethod
            (
            );
            /**Sets  the component match option for automatic/manual component assignment.  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void SetComponentMatchMethod
            (
                NXOpen::Preferences::RoutingElectrical::ComponentMatchType component_match_method /** */
            );
            /** Gets the column name of the component list used for component matching
                       if the method is attribute matching.  @return   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXString GetComponentMatchColumnHeading
            (
            );
            /** Sets the column name of the component list used for component matching
                       if the method is attribute matching.  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void SetComponentMatchColumnHeading
            (
                const NXString & column_heading /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Gets the component attribute name used for component matching
                       if the method is attribute matching.  @return   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXString GetComponentMatchComponentAttributeTitle
            (
            );
            /** Sets the component attribute name used for component matching
                       if the method is attribute matching.  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void SetComponentMatchComponentAttributeTitle
            (
                const NXString & component_attribute_title /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /**Returns  the default length of a jumper wire.  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXString DefaultJumperLength
            (
            );
            /**Sets  the default length of a jumper wire.  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void SetDefaultJumperLength
            (
                const NXString & default_jumper_length /** */
            );
            /** Gets the Rlist_Filter_Blanking_Attribute.  @return   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXString GetFilterBlankingAttribute
            (
            );
            /** Sets the Rlist_Filter_Blanking_Attribute.  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void SetFilterBlankingAttribute
            (
                const NXString & attribute_name /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /**Returns  the option to export the XML routelist data with the formats and
                        filters information separately.  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: bool StandaloneFilterFormatFile
            (
            );
            /**Sets  the option to export the XML routelist data with the formats and
                        filters information separately.  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void SetStandaloneFilterFormatFile
            (
                bool standalone_filter_format_file /** */
            );
            /** Gets the file name for the stand alone XML filters and formats file.  @return   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXString GetFilterFormatFileName
            (
            );
            /** Sets the file name for the stand alone XML filters and formats file.  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void SetFilterFormatFileName
            (
                const NXString & filter_format_file_name /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /**Returns  the option to export the format at the top of a legacy routelist file.  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: bool ExportFormatInLegacyFile
            (
            );
            /**Sets  the option to export the format at the top of a legacy routelist file.  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void SetExportFormatInLegacyFile
            (
                bool export_format /** */
            );
            /**Returns  the default segment length tolerance to use for Formboard Synchronization.  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: double FormboardSynchronizationLengthTolerance
            (
            );
            /**Sets  the default segment length tolerance to use for Formboard Synchronization.  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void SetFormboardSynchronizationLengthTolerance
            (
                double segment_length_tolerance /** */
            );
            /** Gets the formboard frame sizes currently specified within the
                        Routing Electrical application.  Formboard frame sizes are character
                        strings are of the form Height x Length (units).

                        Units can be "in" or "mm" (case insensitive).

                        The Height, Length and units fields of the string are separated
                        by one of the following separator characters:

                               "x", "X",  any whitespace, ":" (colon), or a "," (comma)
                       @return   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: std::vector<NXString> GetFormboardFrameSizes
            (
            );
            /** Sets a formboard frame size.  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void SetFormboardFrameSizes
            (
                std::vector<NXString> & frame_sizes /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /**Returns  the default bundle color.  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: int BundleColor
            (
            );
            /**Sets  the default bundle color.  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void SetBundleColor
            (
                int bundle_color /** */
            );
            public: virtual void initialize();
        };
    }
}
#undef EXPORTLIBRARY
#endif
