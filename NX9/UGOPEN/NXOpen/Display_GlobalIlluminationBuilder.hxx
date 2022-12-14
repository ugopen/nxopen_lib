#ifndef NXOpen_DISPLAY_GLOBALILLUMINATIONBUILDER_HXX_INCLUDED
#define NXOpen_DISPLAY_GLOBALILLUMINATIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Display_GlobalIlluminationBuilder.ja
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
#include <NXOpen/Builder.hxx>
#include <NXOpen/Display_GlobalIlluminationBuilder.hxx>
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
        class GlobalIlluminationBuilder;
    }
    class Builder;
    namespace Display
    {
        class _GlobalIlluminationBuilderBuilder;
        class GlobalIlluminationBuilderImpl;
        /**
            Represents a @link Display::GlobalIlluminationBuilder Display::GlobalIlluminationBuilder@endlink .
            Global Illumination provides simulation of real-world lighting using 
            image-based lighting.  Image-Based Lighting replaces the Lights in a 
            view with lighting effects derived from a given image.  Global
            Illumination Final Gather settings affect the Ray Traced Studio 
            photo-realistic display of the work view.
             <br> This class is restricted to being called from a program running during an 
            Interactive NX session.  If run from a non-interactive session it will 
            return NULL. <br> 
             <br> To create a new instance of this class, use @link ViewCollection::CreateGlobalIlluminationBuilder  ViewCollection::CreateGlobalIlluminationBuilder @endlink  <br> 
         <br>  Created in NX9.0.0.  <br>  
        */
        class NXOPENCPP_DISPLAYEXPORT  GlobalIlluminationBuilder : public Builder
        {
            private: GlobalIlluminationBuilderImpl * m_globalilluminationbuilder_impl;
            private: friend class  _GlobalIlluminationBuilderBuilder;
            protected: GlobalIlluminationBuilder();
            public: ~GlobalIlluminationBuilder();
            /**Returns  the intensity control affects the brightness of the Ray Traced Studio lighting and depends on the global illumination image used 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: double IntensityDouble
            (
            );
            /**Sets  the intensity control affects the brightness of the Ray Traced Studio lighting and depends on the global illumination image used 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: void SetIntensityDouble
            (
                double intensityDouble /** intensitydouble */ 
            );
            /**Returns  the stationary final gather quality affects Ray Traced Studio rendering when dynamic operations stop 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: double StationaryFinalGatherQuality
            (
            );
            /**Sets  the stationary final gather quality affects Ray Traced Studio rendering when dynamic operations stop 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: void SetStationaryFinalGatherQuality
            (
                double stationaryFinalGatherQuality /** stationaryfinalgatherquality */ 
            );
            /**Returns  the static final gather quality affects Ray Traced Studio static (still) image rendering 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: double StaticFinalGatherQuality
            (
            );
            /**Sets  the static final gather quality affects Ray Traced Studio static (still) image rendering 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: void SetStaticFinalGatherQuality
            (
                double staticFinalGatherQuality /** staticfinalgatherquality */ 
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
