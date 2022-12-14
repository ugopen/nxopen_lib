#ifndef NXOpen_DISPLAY_LIGHTBUILDER_HXX_INCLUDED
#define NXOpen_DISPLAY_LIGHTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Display_LightBuilder.ja
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
#include <NXOpen/Display_LightTypes.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/libnxopencpp_display_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Display
    {
        class LightBuilder;
    }
    class Builder;
    class Point;
    namespace Display
    {
        class _LightBuilderBuilder;
        class LightBuilderImpl;
        /**
            Represents a @link NXOpen::Display::LightBuilder NXOpen::Display::LightBuilder@endlink 
             <br> This class is restricted to being called from a program running during an 
            Interactive NX session.  If run from a non-interactive session it will 
            return NULL. <br> 
             <br> To create a new instance of this class, use @link NXOpen::ViewCollection::CreateLightBuilder  NXOpen::ViewCollection::CreateLightBuilder @endlink  <br> 
         <br>  Created in NX5.0.0.  <br>  
        */
        class NXOPENCPP_DISPLAYEXPORT  LightBuilder : public NXOpen::Builder
        {
            /** shadow types */
            public: enum ShadowType
            {
                ShadowTypeNone/** No shadows will be produced. */,
                ShadowTypeSoftEdged/** Soft-edged,approximated shadows will be generated using a shadow
                                                                                       mapping algorithm. */,
                ShadowTypeHardEdged/** Hard-edged, precise shadows will be generated using a ray-tracing
                                                                                       algorithm. */,
                ShadowTypeTranslucentHard/** Hard-edged, precise shadows will be generated using a ray-tracing
                                                                                       algorithm.  Shadows from translucent objects will also be generated
                                                                                       and their color will be determined by the transparent object's
                                                                                       color. */
            };

            /** light_mode */
            public: enum LightMode
            {
                LightModeFixedToObserver/** fixed to observer */ ,
                LightModeFixedToThePart/** fixed to the part */ 
            };

            private: LightBuilderImpl * m_lightbuilder_impl;
            private: friend class  _LightBuilderBuilder;
            protected: LightBuilder();
            public: ~LightBuilder();
            /**Returns  the light type for a particular light 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::LightType LightType
            (
            );
            /**Sets  the light type for a particular light 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void SetLightType
            (
                NXOpen::LightType lightType /** lighttype */ 
            );
            /**Returns  the brightness intensity for a given light 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: double Intensity
            (
            );
            /**Sets  the brightness intensity for a given light 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void SetIntensity
            (
                double intensity /** intensity */ 
            );
            /**Returns  the flag to indicate whether the given light is to be used with image based lighting in the advanced studio display. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: bool UseWithAdvancedStudioImageBasedLighting
            (
            );
            /**Returns  the use_with_ibl flag for a given light 
             <br>  @deprecated Deprecated in NX10.0.0.  This funcationality is no longer supported. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX10.0.0.  This funcationality is no longer supported.") bool UseWithIbl
            (
            );
            /**Sets  the flag to indicate whether the given light is to be used with image based lighting in the advanced studio display. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void SetUseWithAdvancedStudioImageBasedLighting
            (
                bool useWithAdvancedStudioIBl /** usewithadvancedstudioibl */ 
            );
            /**Sets  the use_with_ibl flag for a given light 
             <br>  @deprecated Deprecated in NX10.0.0.  This funcationality is no longer supported. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX10.0.0.  This funcationality is no longer supported.") void SetUseWithIbl
            (
                bool useWithIBL /** usewithibl */ 
            );
            /**Returns  the flag to indicate whether the given light is to be used with image based lighting in ray traced rendering. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: bool UseWithRayTracedImageBasedLighting
            (
            );
            /**Sets  the flag to indicate whether the given light is to be used with image based lighting in ray traced rendering. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void SetUseWithRayTracedImageBasedLighting
            (
                bool useWithRayTracedIBL /** usewithraytracedibl */ 
            );
            /**Returns  the source position - only applicable to spot and point light types 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Point * SourcePosition
            (
            );
            /**Sets  the source position - only applicable to spot and point light types 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void SetSourcePosition
            (
                NXOpen::Point * sourcePosition /** sourceposition */ 
            );
            /**Returns  the destination position - only applicable to spot light types 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Point * DestinationPosition
            (
            );
            /**Sets  the destination position - only applicable to spot light types 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void SetDestinationPosition
            (
                NXOpen::Point * destinationPosition /** destinationposition */ 
            );
            /**Returns  the cone angle - only applicable to spot light types 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: double ConeAngle
            (
            );
            /**Sets  the cone angle - only applicable to spot light types 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void SetConeAngle
            (
                double coneAngle /** coneangle */ 
            );
            /**Returns  the light shadow type - not applicable to ambient or eye light types 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Display::LightBuilder::ShadowType LightShadowType
            (
            );
            /**Sets  the light shadow type - not applicable to ambient or eye light types 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void SetLightShadowType
            (
                NXOpen::Display::LightBuilder::ShadowType lightShadowType /** lightshadowtype */ 
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
