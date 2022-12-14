#ifndef NXOpen_DRAWINGS_VIEWSTYLESHADINGBUILDER_HXX_INCLUDED
#define NXOpen_DRAWINGS_VIEWSTYLESHADINGBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Drawings_ViewStyleShadingBuilder.ja
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
#include <NXOpen/GeometricUtilities_IComponentBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/Preferences_ViewStylePreferencesData.hxx>
#include <NXOpen/libnxopencpp_drawings_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Drawings
    {
        class ViewStyleShadingBuilder;
    }
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    class NXColor;
    namespace Drawings
    {
        class _ViewStyleShadingBuilderBuilder;
        class ViewStyleShadingBuilderImpl;
        /** Represents the SHADING tab on the View Style Dialog (Drawings.ViewStyleShadingBuilder)
            
         <br>  Created in NX6.0.0.  <br>  
        */
        class NXOPENCPP_DRAWINGSEXPORT  ViewStyleShadingBuilder : public NXOpen::TaggedObject, public virtual NXOpen::GeometricUtilities::IComponentBuilder
        {
            private: ViewStyleShadingBuilderImpl * m_viewstyleshadingbuilder_impl;
            private: friend class  _ViewStyleShadingBuilderBuilder;
            protected: ViewStyleShadingBuilder();
            public: ~ViewStyleShadingBuilder();
            /**Returns  the rendering style option on the SHADING tab of the View Style Dialog 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Preferences::ShadingRenderingStyleOption RenderingStyle
            (
            );
            /**Sets  the rendering style option on the SHADING tab of the View Style Dialog 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetRenderingStyle
            (
                NXOpen::Preferences::ShadingRenderingStyleOption renderingStyleOption /** Sets a new rendering style option on the shading sub-builder */
            );
            /**Returns  the cut face color on the SHADING tab of the View Style Dialog 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::NXColor * CutFaceColor
            (
            );
            /**Sets  the cut face color on the SHADING tab of the View Style Dialog 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetCutFaceColor
            (
                NXOpen::NXColor * cutFaceColor /** Sets a new cut face color on the shading sub-builder */
            );
            /**Returns  the visible wireframe color on the SHADING tab of the View Style Dialog 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::NXColor * VisibleWireframeColor
            (
            );
            /**Sets  the visible wireframe color on the SHADING tab of the View Style Dialog 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetVisibleWireframeColor
            (
                NXOpen::NXColor * visibleWireframeColor /** Sets a new visible wireframe color on the shading sub-builder */
            );
            /**Returns  the hidden wireframe color on the SHADING tab of the View Style Dialog 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::NXColor * HiddenWireframeColor
            (
            );
            /**Sets  the hidden wireframe color on the SHADING tab of the View Style Dialog 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetHiddenWireframeColor
            (
                NXOpen::NXColor * hiddenWireframeColor /** Sets a new hidden wireframe color on the shading sub-builder */
            );
            /**Returns  the shade tolerance option on the SHADING tab of the View Style Dialog 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Preferences::ShadingToleranceOption ShadeTolerance
            (
            );
            /**Sets  the shade tolerance option on the SHADING tab of the View Style Dialog 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetShadeTolerance
            (
                NXOpen::Preferences::ShadingToleranceOption shadeToleranceOption /** Sets a new shade tolerance option on the shading sub-builder */
            );
            /**Returns  the edge tolerance data on the SHADING tab of the View Style Dialog 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: double EdgeTolerance
            (
            );
            /**Sets  the edge tolerance data on the SHADING tab of the View Style Dialog 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetEdgeTolerance
            (
                double edgeToleranceData /** Sets a new edge tolerance on the shading sub-builder */
            );
            /**Returns  the face tolerance data on the SHADING tab of the View Style Dialog 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: double FaceTolerance
            (
            );
            /**Sets  the face tolerance data on the SHADING tab of the View Style Dialog 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetFaceTolerance
            (
                double faceToleranceData /** Sets a new face tolerance on the shading sub-builder */
            );
            /**Returns  the angle tolerance data on the SHADING tab of the View Style Dialog 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: double AngleTolerance
            (
            );
            /**Sets  the angle tolerance data on the SHADING tab of the View Style Dialog 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetAngleTolerance
            (
                double angleToleranceData /** Sets a new angle tolerance on the shading sub-builder */
            );
            /**Returns  the shininess scale data on the SHADING tab of the View Style Dialog 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: double ShininessScale
            (
            );
            /**Sets  the shininess scale data on the SHADING tab of the View Style Dialog 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetShininessScale
            (
                double shininessScaleData /** Sets a new shininess scale on the shading sub-builder */
            );
            /**Returns  the two sided light toggle on the SHADING tab of the View Style Dialog 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: bool TwoSidedLight
            (
            );
            /**Sets  the two sided light toggle on the SHADING tab of the View Style Dialog 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetTwoSidedLight
            (
                bool twoSidedLightToggle /** Sets a new two sided light toggle value on the shading sub-builder */
            );
            /** Validate whether the inputs to the component are sufficient for 
                        commit to be called.  If the component is not in a state to commit
                        then an exception is thrown.  For example, if the component requires
                        you to set some property, this method will throw an exception if
                        you haven't set it.  This method throws a not-yet-implemented
                        NXException for some components.
                     @return  Was self validation successful 
             <br>  Created in NX3.0.1.  <br>  
             <br> License requirements : None */
            public: virtual bool Validate
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
