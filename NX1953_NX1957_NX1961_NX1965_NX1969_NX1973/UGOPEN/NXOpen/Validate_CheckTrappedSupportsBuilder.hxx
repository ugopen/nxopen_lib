#ifndef NXOpen_VALIDATE_CHECKTRAPPEDSUPPORTSBUILDER_HXX_INCLUDED
#define NXOpen_VALIDATE_CHECKTRAPPEDSUPPORTSBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Validate_CheckTrappedSupportsBuilder.ja
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
#include <NXOpen/GeometricUtilities_DisplayResolutionBuilder.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/Validate_SelectionAndPlacementBuilder.hxx>
#include <NXOpen/libnxopencpp_validate_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Validate
    {
        class CheckTrappedSupportsBuilder;
    }
    class Builder;
    namespace GeometricUtilities
    {
        class DisplayResolutionBuilder;
    }
    class NXColor;
    namespace Validate
    {
        class SelectionAndPlacementBuilder;
    }
    namespace Validate
    {
        class _CheckTrappedSupportsBuilderBuilder;
        class CheckTrappedSupportsBuilderImpl;
        /** Represents a Check Trapped Supports Builder  <br> To create a new instance of this class, use @link NXOpen::Validate::AnalysisResultCollection::CreateCheckTrappedSupportsBuilder  NXOpen::Validate::AnalysisResultCollection::CreateCheckTrappedSupportsBuilder @endlink  <br> 
        Default values.
        <list type="table"> 
         
        <listheader><term> 
        Property</term>  <description> 
        Value</description> </listheader>
        <item><term> 
         
        Angle </term> <description> 
         
        45 </description> </item> 

        <item><term> 
         
        AutomaticUpdate </term> <description> 
         
        1 </description> </item> 

        <item><term> 
         
        DisplayResolutionBuilder.AngleTolerance </term> <description> 
         
        15.0 </description> </item> 

        <item><term> 
         
        DisplayResolutionBuilder.EdgeTolerance </term> <description> 
         
        0.005 </description> </item> 

        <item><term> 
         
        DisplayResolutionBuilder.FaceTolerance </term> <description> 
         
        0.005 </description> </item> 

        <item><term> 
         
        DisplayResolutionBuilder.Resolution </term> <description> 
         
        Standard </description> </item> 

        <item><term> 
         
        DisplayResolutionBuilder.WidthTolerance </term> <description> 
         
        0.3 </description> </item> 

        <item><term> 
         
        NonTrappedSupportAreasColor </term> <description> 
         
        36 </description> </item> 

        <item><term> 
         
        PreviewState </term> <description> 
         
        1 </description> </item> 

        <item><term> 
         
        ShowOnlyFailArea </term> <description> 
         
        1 </description> </item> 

        <item><term> 
         
        TrappedSupportAreasColor </term> <description> 
         
        186 </description> </item> 

        </list> 

         <br>  Created in NX1899.0.0.  <br>  
        */
        class NXOPENCPP_VALIDATEEXPORT  CheckTrappedSupportsBuilder : public NXOpen::Builder
        {
            private: CheckTrappedSupportsBuilderImpl * m_checktrappedsupportsbuilder_impl;
            private: friend class  _CheckTrappedSupportsBuilderBuilder;
            protected: CheckTrappedSupportsBuilder();
            public: ~CheckTrappedSupportsBuilder();
            /**Returns  the selection and placement builder
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Validate::SelectionAndPlacementBuilder * SelectionAndPlacement
            (
            );
            /**Returns  the Maximum Overhang Angle 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: double Angle
            (
            );
            /**Sets  the Maximum Overhang Angle 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: void SetAngle
            (
                double angle /** angle */ 
            );
            /**Returns  the show only trapped aupport areas 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: bool ShowOnlyFailArea
            (
            );
            /**Sets  the show only trapped aupport areas 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: void SetShowOnlyFailArea
            (
                bool showOnlyFailArea /** showonlyfailarea */ 
            );
            /**Returns  the non-Trapped Supports Areas Color 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::NXColor * NonTrappedSupportAreasColor
            (
            );
            /**Sets  the non-Trapped Supports Areas Color 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: void SetNonTrappedSupportAreasColor
            (
                NXOpen::NXColor * nonTrappedSupportAreasColor /** nontrappedsupportareascolor */ 
            );
            /**Returns  the Trapped Supports Areas Color 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::NXColor * TrappedSupportAreasColor
            (
            );
            /**Sets  the Trapped Supports Areas Color 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: void SetTrappedSupportAreasColor
            (
                NXOpen::NXColor * trappedSupportAreasColor /** trappedsupportareascolor */ 
            );
            /**Returns  the automatic update toggle 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: bool AutomaticUpdate
            (
            );
            /**Sets  the automatic update toggle 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: void SetAutomaticUpdate
            (
                bool automaticUpdate /** automaticupdate */ 
            );
            /**Returns  the preview toggle 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: bool PreviewState
            (
            );
            /**Sets  the preview toggle 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: void SetPreviewState
            (
                bool previewState /** previewstate */ 
            );
            /**Returns  the trapped area 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: double TrappedArea
            (
            );
            /**Returns  the display resolution 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricUtilities::DisplayResolutionBuilder * DisplayResolutionBuilder
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
