#ifndef NXOpen_VALIDATE_CHECKMAXIMUMOVERHANGANGLEBUILDER_HXX_INCLUDED
#define NXOpen_VALIDATE_CHECKMAXIMUMOVERHANGANGLEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Validate_CheckMaximumOverhangAngleBuilder.ja
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
#include <NXOpen/ugmath.hxx>
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
        class CheckMaximumOverhangAngleBuilder;
    }
    class Body;
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
        class _CheckMaximumOverhangAngleBuilderBuilder;
        class CheckMaximumOverhangAngleBuilderImpl;
        /** Represents a Check Maximum Overhang Angle builder  <br> To create a new instance of this class, use @link NXOpen::Validate::AnalysisResultCollection::CreateCheckMaximumOverhangAngleBuilder  NXOpen::Validate::AnalysisResultCollection::CreateCheckMaximumOverhangAngleBuilder @endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        Angle </td> <td> 
         
        45 </td> </tr> 

        <tr><td> 
         
        AutomaticUpdate </td> <td> 
         
        1 </td> </tr> 

        <tr><td> 
         
        DisplayResolutionBuilder.AngleTolerance </td> <td> 
         
        15.0 </td> </tr> 

        <tr><td> 
         
        DisplayResolutionBuilder.EdgeTolerance </td> <td> 
         
        0.005 </td> </tr> 

        <tr><td> 
         
        DisplayResolutionBuilder.FaceTolerance </td> <td> 
         
        0.005 </td> </tr> 

        <tr><td> 
         
        DisplayResolutionBuilder.Resolution </td> <td> 
         
        Standard </td> </tr> 

        <tr><td> 
         
        DisplayResolutionBuilder.WidthTolerance </td> <td> 
         
        0.3 </td> </tr> 

        <tr><td> 
         
        ExceedExtendToleranceColor </td> <td> 
         
        186 </td> </tr> 

        <tr><td> 
         
        ExtendedAngularTolerance </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        LessThanMaxAngleColor </td> <td> 
         
        36 </td> </tr> 

        <tr><td> 
         
        MoreThanMaxAngleColor </td> <td> 
         
        6 </td> </tr> 

        <tr><td> 
         
        PreviewState </td> <td> 
         
        1 </td> </tr> 

        <tr><td> 
         
        ShowOnlyExceedingOverhangAngles (deprecated) </td> <td> 
         
        1 </td> </tr> 

        <tr><td> 
         
        ShowOnlyFailArea </td> <td> 
         
        1 </td> </tr> 

        </table>  

         <br>  Created in NX1872.0.0.  <br>  
        */
        class NXOPENCPP_VALIDATEEXPORT  CheckMaximumOverhangAngleBuilder : public NXOpen::Builder
        {
            private: CheckMaximumOverhangAngleBuilderImpl * m_checkmaximumoverhanganglebuilder_impl;
            private: friend class  _CheckMaximumOverhangAngleBuilderBuilder;
            protected: CheckMaximumOverhangAngleBuilder();
            public: ~CheckMaximumOverhangAngleBuilder();
            /**Returns  the selection and placement builder
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Validate::SelectionAndPlacementBuilder * SelectionAndPlacement
            (
            );
            /** Returns the selected Bodies or Parts @return  
             <br>  @deprecated Deprecated in NX1899.0.0.  Use @link  NXOpen::Validate::SelectionAndPlacementBuilder::GetTargets   NXOpen::Validate::SelectionAndPlacementBuilder::GetTargets @endlink  <br>  

             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX1899.0.0.  Use  NXOpen::Validate::SelectionAndPlacementBuilder::GetTargets ") std::vector<NXOpen::Body *> GetTargets
            (
            );
            /** Set the Bodies or Parts 
             <br>  @deprecated Deprecated in NX1899.0.0.  Use @link  NXOpen::Validate::SelectionAndPlacementBuilder::SetTargets   NXOpen::Validate::SelectionAndPlacementBuilder::SetTargets @endlink  <br>  

             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX1899.0.0.  Use  NXOpen::Validate::SelectionAndPlacementBuilder::SetTargets ") void SetTargets
            (
                const std::vector<NXOpen::Body *> & targets /** The objects to apply the attributes to. */
            );
            /**Returns  the draw origin 
             <br>  @deprecated Deprecated in NX1899.0.0.  Use @link  NXOpen::Validate::SelectionAndPlacementBuilder::DrawOrigin   NXOpen::Validate::SelectionAndPlacementBuilder::DrawOrigin @endlink  <br>  

             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX1899.0.0.  Use  NXOpen::Validate::SelectionAndPlacementBuilder::DrawOrigin ") NXOpen::Point3d DrawOrigin
            (
            );
            /**Sets  the draw origin 
             <br>  @deprecated Deprecated in NX1899.0.0.  Use @link  NXOpen::Validate::SelectionAndPlacementBuilder::DrawOrigin   NXOpen::Validate::SelectionAndPlacementBuilder::DrawOrigin @endlink  <br>  

             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX1899.0.0.  Use  NXOpen::Validate::SelectionAndPlacementBuilder::DrawOrigin ") void SetDrawOrigin
            (
                const NXOpen::Point3d & drawOrigin /** draworigin */ 
            );
            /**Returns  the draw orientation 
             <br>  @deprecated Deprecated in NX1899.0.0.  Use @link  NXOpen::Validate::SelectionAndPlacementBuilder::DrawOrientation   NXOpen::Validate::SelectionAndPlacementBuilder::DrawOrientation @endlink  <br>  

             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX1899.0.0.  Use  NXOpen::Validate::SelectionAndPlacementBuilder::DrawOrientation ") NXOpen::Matrix3x3 DrawOrientation
            (
            );
            /**Sets  the draw orientation 
             <br>  @deprecated Deprecated in NX1899.0.0.  Use @link  NXOpen::Validate::SelectionAndPlacementBuilder::DrawOrientation   NXOpen::Validate::SelectionAndPlacementBuilder::DrawOrientation @endlink  <br>  

             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX1899.0.0.  Use  NXOpen::Validate::SelectionAndPlacementBuilder::DrawOrientation ") void SetDrawOrientation
            (
                const NXOpen::Matrix3x3 & drawOrientation /** draworientation */ 
            );
            /**Returns  the Maximum Angle  
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: double Angle
            (
            );
            /**Sets  the Maximum Angle  
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: void SetAngle
            (
                double angle /** angle */ 
            );
            /**Returns  the Extended Angular Tol  
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: double ExtendedAngularTolerance
            (
            );
            /**Sets  the Extended Angular Tol  
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: void SetExtendedAngularTolerance
            (
                double extendedAngularTol /** extendedangulartol */ 
            );
            /**Returns  the Less Than Max Angle Color 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::NXColor * LessThanMaxAngleColor
            (
            );
            /**Sets  the Less Than Max Angle Color 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: void SetLessThanMaxAngleColor
            (
                NXOpen::NXColor * lessThanMaxAngleColor /** lessthanmaxanglecolor */ 
            );
            /**Returns  the More Than Max Angle Color 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::NXColor * MoreThanMaxAngleColor
            (
            );
            /**Sets  the More Than Max Angle Color 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: void SetMoreThanMaxAngleColor
            (
                NXOpen::NXColor * moreThanMaxAngleColor /** morethanmaxanglecolor */ 
            );
            /**Returns  the Exceed Extend Tol color 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::NXColor * ExceedExtendToleranceColor
            (
            );
            /**Sets  the Exceed Extend Tol color 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: void SetExceedExtendToleranceColor
            (
                NXOpen::NXColor * exceedExtendTolColor /** exceedextendtolcolor */ 
            );
            /**Returns  the property will be deprecated. use JA_VALIDATE_CHECK_MAXIMUM_OVERHANG_ANGLE_BUILDER_get_OnlyShowFailArea instead. 
             <br>  @deprecated Deprecated in NX1899.0.0.  JA_VALIDATE_CHECK_MAXIMUM_OVERHANG_ANGLE_BUILDER_get_OnlyShowFailArea. <br>  

             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX1899.0.0.  JA_VALIDATE_CHECK_MAXIMUM_OVERHANG_ANGLE_BUILDER_get_OnlyShowFailArea.") bool ShowOnlyExceedingOverhangAngles
            (
            );
            /**Sets  the property will be deprecated. use JA_VALIDATE_CHECK_MAXIMUM_OVERHANG_ANGLE_BUILDER_get_OnlyShowFailArea instead. 
             <br>  @deprecated Deprecated in NX1899.0.0.  JA_VALIDATE_CHECK_MAXIMUM_OVERHANG_ANGLE_BUILDER_set_OnlyShowFailArea. <br>  

             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX1899.0.0.  JA_VALIDATE_CHECK_MAXIMUM_OVERHANG_ANGLE_BUILDER_set_OnlyShowFailArea.") void SetShowOnlyExceedingOverhangAngles
            (
                bool showOnlyExceed /** showonlyexceed */ 
            );
            /**Returns  the toggle that show only Exceeding Overhang Angles 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: bool ShowOnlyFailArea
            (
            );
            /**Sets  the toggle that show only Exceeding Overhang Angles 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: void SetShowOnlyFailArea
            (
                bool showOnlyFailArea /** showonlyfailarea */ 
            );
            /**Returns  the area that need to support 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: double OverhangArea
            (
            );
            /**Returns  the toggle that automatic update 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: bool AutomaticUpdate
            (
            );
            /**Sets  the toggle that automatic update 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: void SetAutomaticUpdate
            (
                bool automaticUpdate /** automaticupdate */ 
            );
            /**Returns  the toggle that preview block 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: bool PreviewState
            (
            );
            /**Sets  the toggle that preview block 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: void SetPreviewState
            (
                bool previewState /** previewstate */ 
            );
            /**Returns  the display resolution 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricUtilities::DisplayResolutionBuilder * DisplayResolutionBuilder
            (
            );
            /** Update the checker 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: void Update
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
