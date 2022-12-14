#ifndef NXOpen_DIE_RIBPARENTBUILDER_HXX_INCLUDED
#define NXOpen_DIE_RIBPARENTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Die_RibParentBuilder.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/Die.hxx>
#include <NXOpen/Features_FeatureBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Die
    {
        class RibParentBuilder;
    }
    namespace Die
    {
        class RibChildBuilder;
    }
    namespace Features
    {
        class FeatureBuilder;
    }
    namespace Die
    {
        class _RibParentBuilderBuilder;
        /** Represents a Die Rib Parent sub feature.  <br> This sub feature is created via the main feature builder. <br> */
        class NXOPENCPPEXPORT RibParentBuilder : public Features::FeatureBuilder
        {
            private: friend class  _RibParentBuilderBuilder;
            protected: RibParentBuilder();
            /**Sets  the centerline xy offset of die ribs.  <br> License requirements : ug_die_design ("Die Design") */
            public: void SetCenterlineXyOffset
            (
                double centerline_xy_offset /** centerline xy offset */ 
            );
            /**Returns  the centerline xy offset of die ribs.  <br> License requirements : ug_die_design ("Die Design") */
            public: double CenterlineXyOffset
            (
            );
            /**Sets  the top limit offset of die ribs.  <br> License requirements : ug_die_design ("Die Design") */
            public: void SetTopLimitOffset
            (
                double top_limit_offset /** top limit offset */ 
            );
            /**Returns  the top limit offset of die ribs.  <br> License requirements : ug_die_design ("Die Design") */
            public: double TopLimitOffset
            (
            );
            /**Sets  the bottom limit offset of die ribs.  <br> License requirements : ug_die_design ("Die Design") */
            public: void SetBottomLimitOffset
            (
                double bottom_limit_offset /** bottom limit offset */ 
            );
            /**Returns  the bottom limit offset of die ribs.  <br> License requirements : ug_die_design ("Die Design") */
            public: double BottomLimitOffset
            (
            );
            /**Sets  the top horizontal offset of die ribs.  <br> License requirements : ug_die_design ("Die Design") */
            public: void SetTopHorizontalOffset
            (
                double top_horizontal_offset /** top horizontal offset */ 
            );
            /**Returns  the top horizontal offset of die ribs.  <br> License requirements : ug_die_design ("Die Design") */
            public: double TopHorizontalOffset
            (
            );
            /**Sets  the top vertical offset of die ribs.  <br> License requirements : ug_die_design ("Die Design") */
            public: void SetTopVerticalOffset
            (
                double top_vertical_offset /** top vertical offset */ 
            );
            /**Returns  the top vertical offset of die ribs.  <br> License requirements : ug_die_design ("Die Design") */
            public: double TopVerticalOffset
            (
            );
            /**Sets  the bottom horizontal offset of die ribs.  <br> License requirements : ug_die_design ("Die Design") */
            public: void SetBottomHorizontalOffset
            (
                double bottom_horizontal_offset /** bottom horizontal offset */ 
            );
            /**Returns  the bottom horizontal offset of die ribs.  <br> License requirements : ug_die_design ("Die Design") */
            public: double BottomHorizontalOffset
            (
            );
            /**Sets  the bottom vertical offset of die ribs.  <br> License requirements : ug_die_design ("Die Design") */
            public: void SetBottomVerticalOffset
            (
                double bottom_vertical_offset /** bottom vertical offset */ 
            );
            /**Returns  the bottom vertical offset of die ribs.  <br> License requirements : ug_die_design ("Die Design") */
            public: double BottomVerticalOffset
            (
            );
            /**Sets  the lightening core clearance of die ribs.  <br> License requirements : ug_die_design ("Die Design") */
            public: void SetLighteningCoreClearance
            (
                double lightening_core_clearance /** lightening core clearance */ 
            );
            /**Returns  the lightening core clearance of die ribs.  <br> License requirements : ug_die_design ("Die Design") */
            public: double LighteningCoreClearance
            (
            );
            /**Sets  the lightening core mininum width of die ribs.  <br> License requirements : ug_die_design ("Die Design") */
            public: void SetLccMinWidth
            (
                double lcc_min_width /** lcc min width */ 
            );
            /**Returns  the lightening core mininum width of die ribs.  <br> License requirements : ug_die_design ("Die Design") */
            public: double LccMinWidth
            (
            );
            /**Sets  the thickness of die ribs.  <br> License requirements : ug_die_design ("Die Design") */
            public: void SetThickness
            (
                double thickness /** thickness */ 
            );
            /**Returns  the thickness of die ribs.  <br> License requirements : ug_die_design ("Die Design") */
            public: double Thickness
            (
            );
            /**Sets  the adjusted thickness of die ribs.  <br> License requirements : ug_die_design ("Die Design") */
            public: void SetAdjustedThickness
            (
                double adjusted_thickness /** adjusted thickness */ 
            );
            /**Returns  the adjusted thickness of die ribs.  <br> License requirements : ug_die_design ("Die Design") */
            public: double AdjustedThickness
            (
            );
            /**Sets  the height of die ribs.  <br> License requirements : ug_die_design ("Die Design") */
            public: void SetHeight
            (
                double height /** height */ 
            );
            /**Returns  the height of die ribs.  <br> License requirements : ug_die_design ("Die Design") */
            public: double Height
            (
            );
            /**Sets  the angle of die ribs.  <br> License requirements : ug_die_design ("Die Design") */
            public: void SetAngle
            (
                double angle /** angle */ 
            );
            /**Returns  the angle of die ribs.  <br> License requirements : ug_die_design ("Die Design") */
            public: double Angle
            (
            );
            /**Sets  the x offset of die ribs.  <br> License requirements : ug_die_design ("Die Design") */
            public: void SetXOffset
            (
                double x_offset /** x offset */ 
            );
            /**Returns  the x offset of die ribs.  <br> License requirements : ug_die_design ("Die Design") */
            public: double XOffset
            (
            );
            /**Sets  the y offset of die ribs.  <br> License requirements : ug_die_design ("Die Design") */
            public: void SetYOffset
            (
                double y_offset /** y offset */ 
            );
            /**Returns  the y offset of die ribs.  <br> License requirements : ug_die_design ("Die Design") */
            public: double YOffset
            (
            );
            /**Sets  the x distance of die ribs.  <br> License requirements : ug_die_design ("Die Design") */
            public: void SetXDistance
            (
                double x_distance /** x distance */ 
            );
            /**Returns  the x distance of die ribs.  <br> License requirements : ug_die_design ("Die Design") */
            public: double XDistance
            (
            );
            /**Sets  the y distance of die ribs.  <br> License requirements : ug_die_design ("Die Design") */
            public: void SetYDistance
            (
                double y_distance /** y distance */ 
            );
            /**Returns  the y distance of die ribs.  <br> License requirements : ug_die_design ("Die Design") */
            public: double YDistance
            (
            );
            /**Returns  the lightening core switch of die ribs, if true the lightening core will be built into the rib, if false it will not.  <br> License requirements : ug_die_design ("Die Design") */
            public: bool LighteningCore
            (
            );
            /**Sets  the lightening core switch of die ribs, if true the lightening core will be built into the rib, if false it will not.  <br> License requirements : ug_die_design ("Die Design") */
            public: void SetLighteningCore
            (
                bool lightening_core /** lightening core */ 
            );
            /**Returns  the rectangular switch of die ribs, if true the lightening cores will be rectangular, 
                    if false they will follow the shape of the rib.  <br> License requirements : ug_die_design ("Die Design") */
            public: bool Rectangular
            (
            );
            /**Sets  the rectangular switch of die ribs, if true the lightening cores will be rectangular, 
                    if false they will follow the shape of the rib.  <br> License requirements : ug_die_design ("Die Design") */
            public: void SetRectangular
            (
                bool rectangular /** rectangular */ 
            );
            /**Sets  the design status of die ribs, if true the ribs will be built into the model, if false they will not.  <br> License requirements : ug_die_design ("Die Design") */
            public: void SetDesignStatus
            (
                bool design_status /** design status */ 
            );
            /**Returns  the design status of die ribs, if true the ribs will be built into the model, if false they will not.  <br> License requirements : ug_die_design ("Die Design") */
            public: bool DesignStatus
            (
            );
            /**Returns  the build status of die ribs.  <br> License requirements : ug_die_design ("Die Design") */
            public: NXOpen::Die::DieBuildStatusOption BuildStatus
            (
            );
            /**Sets  the display status of die ribs, if true input data to the ribs will be displayed, 
                    if false the input data will not be displayed.  <br> License requirements : ug_die_design ("Die Design") */
            public: void SetDisplayStatus
            (
                bool display_status /** display status */ 
            );
            /**Returns  the display status of die ribs, if true input data to the ribs will be displayed, 
                    if false the input data will not be displayed.  <br> License requirements : ug_die_design ("Die Design") */
            public: bool DisplayStatus
            (
            );
            /** Creates a child rib.  @return   <br> License requirements : ug_die_design ("Die Design") */
            public: NXOpen::Die::RibChildBuilder * CreateChild
            (
            );
            /** Deletes a child rib.  <br> License requirements : ug_die_design ("Die Design") */
            public: void DeleteChild
            (
                NXOpen::Die::RibChildBuilder * dieribchild /** dieribchild */ 
            );
            /** Outputs the child ribs.  @return  The child ribs.  <br> License requirements : ug_die_design ("Die Design") */
            public: std::vector<NXOpen::Die::RibChildBuilder *> GetChildren
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
