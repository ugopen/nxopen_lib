#ifndef NXOpen_DIE_RIBCHILDBUILDER_HXX_INCLUDED
#define NXOpen_DIE_RIBCHILDBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Die_RibChildBuilder.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#ifdef _MSC_VER
#pragma once
#endif

#include <NXOpen/NXDeprecation.hxx>
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/Die.hxx>
#include <NXOpen/Features_FeatureBuilder.hxx>
#include <NXOpen/libnxopencpp_die_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Die
    {
        class RibChildBuilder;
    }
    namespace Features
    {
        class FeatureBuilder;
    }
    class IOrientation;
    class IProfile;
    namespace Die
    {
        class _RibChildBuilderBuilder;
        class RibChildBuilderImpl;
        /** Represents a Die Rib Child sub feature.  <br> This sub feature is created via the main feature builder.  <br> 
         <br>  Created in NX4.0.0.  <br>  
        */
        class NXOPENCPP_DIEEXPORT  RibChildBuilder : public Features::FeatureBuilder
        {
            private: RibChildBuilderImpl * m_ribchildbuilder_impl;
            private: friend class  _RibChildBuilderBuilder;
            protected: RibChildBuilder();
            public: ~RibChildBuilder();
            /** Sets the centerline of the rib. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetCenterline
            (
                NXOpen::Die::DirectionOption direction /** Profile direction. */,
                const std::vector<NXOpen::IProfile *> & profileEntries /** The profile entries, can be curves, edges, faces, sketches or curve features. */
            );
            /** Gets the centerline of the rib.  @return  The profile entries, will be curves, edges, faces, sketches or curve features. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: std::vector<NXOpen::IProfile *> GetCenterline
            (
                NXOpen::Die::DirectionOption* direction /** Profile direction. */
            );
            /**Sets  the top limit geometry of the die rib. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetTop
            (
                NXOpen::IOrientation * top /** top */ 
            );
            /**Returns  the top limit geometry of the die rib. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: NXOpen::IOrientation * Top
            (
            );
            /**Sets  the bottom limit geometry of the die rib. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetBottom
            (
                NXOpen::IOrientation * bottom /** bottom */ 
            );
            /**Returns  the bottom limit geometry of the die rib. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: NXOpen::IOrientation * Bottom
            (
            );
            /**Sets  the start limit geometry of the die rib. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetStart
            (
                NXOpen::IOrientation * start /** start */ 
            );
            /**Returns  the start limit geometry of the die rib. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: NXOpen::IOrientation * Start
            (
            );
            /** Sets the start limit geometry of the die rib using a profile. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetStart
            (
                NXOpen::Die::DirectionOption direction /** Profile direction. */,
                const std::vector<NXOpen::IProfile *> & profileEntries /** The the profile entries, can be curves, edges, faces, sketches or curve features. */
            );
            /** Gets the start limit geometry of the die rib as a profile.  @return  The profile entries, will be curves, edges, faces, sketches or curve features. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: std::vector<NXOpen::IProfile *> GetStart
            (
                NXOpen::Die::DirectionOption* direction /** Profile direction. */
            );
            /**Sets  the top end limit geometry of the die rib. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetTopEnd
            (
                NXOpen::IOrientation * topEnd /** top end */ 
            );
            /**Returns  the top end limit geometry of the die rib. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: NXOpen::IOrientation * TopEnd
            (
            );
            /** Sets the top end limit geometry of the die rib using a profile. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetTopEnd
            (
                NXOpen::Die::DirectionOption direction /** Profile direction. */,
                const std::vector<NXOpen::IProfile *> & profileEntries /** The profile entries, can be curves, edges, faces, sketches or curve features. */
            );
            /** Gets the top end limit geometry of the die rib as a profile.  @return  The profile entries, will be curves, edges, faces, sketches or curve features. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: std::vector<NXOpen::IProfile *> GetTopEnd
            (
                NXOpen::Die::DirectionOption* direction /** Profile direction. */
            );
            /**Sets  the bottom end limit geometry of the die rib. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetBottomEnd
            (
                NXOpen::IOrientation * bottomEnd /** bottom end */ 
            );
            /**Returns  the bottom end limit geometry of the die rib. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: NXOpen::IOrientation * BottomEnd
            (
            );
            /** Sets the bottom end limit geometry of the die rib using a profile. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetBottomEnd
            (
                NXOpen::Die::DirectionOption direction /** Profile direction. */,
                const std::vector<NXOpen::IProfile *> & profileEntries /** The profile entries, can be curves, edges, faces, sketches or curve features. */
            );
            /** Gets the bottom end limit geometry of the die rib as a profile.  @return  The profile entries, will be curves, edges, faces, sketches or curve features. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: std::vector<NXOpen::IProfile *> GetBottomEnd
            (
                NXOpen::Die::DirectionOption* direction /** Profile direction. */
            );
            /**Sets  the centerline xy offset of the die rib. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetCenterlineXyOffset
            (
                double centerlineXyOffset /** centerline xy offset */ 
            );
            /**Returns  the centerline xy offset of the die rib. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: double CenterlineXyOffset
            (
            );
            /**Sets  the top limit offset of the die rib. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetTopLimitOffset
            (
                double topLimitOffset /** top limit offset */ 
            );
            /**Returns  the top limit offset of the die rib. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: double TopLimitOffset
            (
            );
            /**Sets  the bottom limit offset of the die rib. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetBottomLimitOffset
            (
                double bottomLimitOffset /** bottom limit offset */ 
            );
            /**Returns  the bottom limit offset of the die rib. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: double BottomLimitOffset
            (
            );
            /**Sets  the top horizontal offset of the die rib. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetTopHorizontalOffset
            (
                double topHorizontalOffset /** top horizontal offset */ 
            );
            /**Returns  the top horizontal offset of the die rib. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: double TopHorizontalOffset
            (
            );
            /**Sets  the top vertical offset of the die rib. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetTopVerticalOffset
            (
                double topVerticalOffset /** top vertical offset */ 
            );
            /**Returns  the top vertical offset of the die rib. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: double TopVerticalOffset
            (
            );
            /**Sets  the bottom horizontal offset of the die rib. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetBottomHorizontalOffset
            (
                double bottomHorizontalOffset /** bottom horizontal offset */ 
            );
            /**Returns  the bottom horizontal offset of the die rib. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: double BottomHorizontalOffset
            (
            );
            /**Sets  the bottom vertical offset of the die rib. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetBottomVerticalOffset
            (
                double bottomVerticalOffset /** bottom vertical offset */ 
            );
            /**Returns  the bottom vertical offset of the die rib. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: double BottomVerticalOffset
            (
            );
            /**Sets  the lightening core clearance of the die rib. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetLighteningCoreClearance
            (
                double lighteningCoreClearance /** lightening core clearance */ 
            );
            /**Returns  the lightening core clearance of the die rib. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: double LighteningCoreClearance
            (
            );
            /**Sets  the lightening core mininum width of the die rib. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetLccMinWidth
            (
                double lccMinWidth /** lcc min width */ 
            );
            /**Returns  the lightening core mininum width of the die rib. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: double LccMinWidth
            (
            );
            /**Sets  the thickness of the die rib. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetThickness
            (
                double thickness /** thickness */ 
            );
            /**Returns  the thickness of the die rib. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: double Thickness
            (
            );
            /**Sets  the adjusted thickness of the die rib. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetAdjustedThickness
            (
                double adjustedThickness /** adjusted thickness */ 
            );
            /**Returns  the adjusted thickness of the die rib. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: double AdjustedThickness
            (
            );
            /**Sets  the height of the die rib. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetHeight
            (
                double height /** height */ 
            );
            /**Returns  the height of the die rib. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: double Height
            (
            );
            /**Sets  the angle of the die rib. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetAngle
            (
                double angle /** angle */ 
            );
            /**Returns  the angle of the die rib. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: double Angle
            (
            );
            /**Returns  the lightening core switch of the die rib, if true the lightening core will be built into the rib, if false it will not. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: bool LighteningCore
            (
            );
            /**Sets  the lightening core switch of the die rib, if true the lightening core will be built into the rib, if false it will not. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetLighteningCore
            (
                bool lighteningCore /** lightening core */ 
            );
            /**Returns  the rectangular switch of the die rib, if true the lightening core will be rectangular, 
                    if false it will follow the shape of the rib. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: bool Rectangular
            (
            );
            /**Sets  the rectangular switch of the die rib, if true the lightening core will be rectangular, 
                    if false it will follow the shape of the rib. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetRectangular
            (
                bool rectangular /** rectangular */ 
            );
            /**Sets  the design status of the die rib, if true the rib will be built into the model, if false it will not. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetDesignStatus
            (
                bool designStatus /** design status */ 
            );
            /**Returns  the design status of the die rib, if true the rib will be built into the model, if false it will not. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: bool DesignStatus
            (
            );
            /**Returns  the build status of the die rib. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: NXOpen::Die::DieBuildStatusOption BuildStatus
            (
            );
            /**Sets  the display status of the die rib, if true input data to the rib will be displayed, 
                    if false the input data will not be displayed. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetDisplayStatus
            (
                bool displayStatus /** display status */ 
            );
            /**Returns  the display status of the die rib, if true input data to the rib will be displayed, 
                    if false the input data will not be displayed. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: bool DisplayStatus
            (
            );
        };
    }
}

#ifdef _MSC_VER
#pragma warning(pop)
#endif
#ifdef __GNUC__
#ifndef NX_NO_GCC_DEPRECATION_WARNINGS
#pragma GCC diagnostic warning "-Wdeprecated-declarations"
#endif
#endif

#undef EXPORTLIBRARY
#endif