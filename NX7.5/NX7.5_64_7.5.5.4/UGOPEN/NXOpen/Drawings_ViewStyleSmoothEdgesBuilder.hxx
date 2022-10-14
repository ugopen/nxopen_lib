#ifndef NXOpen_DRAWINGS_VIEWSTYLESMOOTHEDGESBUILDER_HXX_INCLUDED
#define NXOpen_DRAWINGS_VIEWSTYLESMOOTHEDGESBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Drawings_ViewStyleSmoothEdgesBuilder.ja
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
#include <NXOpen/Drawings_ViewStyleSmoothEdgesBuilder.hxx>
#include <NXOpen/GeometricUtilities_IComponentBuilder.hxx>
#include <NXOpen/Preferences_ViewStylePreferencesData.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Drawings
    {
        class ViewStyleSmoothEdgesBuilder;
    }
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    class NXColor;
    namespace Drawings
    {
        class _ViewStyleSmoothEdgesBuilderBuilder;
        class ViewStyleSmoothEdgesBuilderImpl;
        /** Represents the SMOOTH EDGES tab on the View Style Dialog (Drawings.ViewStyleSmoothEdgesBuilder)
            */
        class NXOPENCPPEXPORT  ViewStyleSmoothEdgesBuilder : public TaggedObject, public virtual GeometricUtilities::IComponentBuilder
        {
            private: ViewStyleSmoothEdgesBuilderImpl * m_viewstylesmoothedgesbuilder_impl;
            private: friend class  _ViewStyleSmoothEdgesBuilderBuilder;
            protected: ViewStyleSmoothEdgesBuilder();
            public: ~ViewStyleSmoothEdgesBuilder();
            /**Returns  the smooth edge toggle on the SMOOTH EDGES tab of the View Style Dialog  <br> License requirements : None */
            public: bool SmoothEdge
            (
            );
            /**Sets  the smooth edge toggle on the SMOOTH EDGES tab of the View Style Dialog  <br> License requirements : drafting ("DRAFTING") */
            public: void SetSmoothEdge
            (
                bool smoothEdgesToggle /** Sets a new smooth edge toggle value on the smooth edge sub-builder */
            );
            /**Returns  the color on the SMOOTH EDGES tab of the View Style Dialog  <br> License requirements : None */
            public: NXOpen::NXColor * Color
            (
            );
            /**Sets  the color on the SMOOTH EDGES tab of the View Style Dialog  <br> License requirements : drafting ("DRAFTING") */
            public: void SetColor
            (
                NXOpen::NXColor * color /** Sets a new color on the smooth edge sub-builder */
            );
            /**Returns  the font on the SMOOTH EDGES tab of the View Style Dialog  <br> License requirements : None */
            public: NXOpen::Preferences::Font Font
            (
            );
            /**Sets  the font on the SMOOTH EDGES tab of the View Style Dialog  <br> License requirements : drafting ("DRAFTING") */
            public: void SetFont
            (
                NXOpen::Preferences::Font font /** Sets a new font on the smooth edge sub-builder */
            );
            /**Returns  the width on the SMOOTH EDGES tab of the View Style Dialog  <br> License requirements : None */
            public: NXOpen::Preferences::Width Width
            (
            );
            /**Sets  the width on the SMOOTH EDGES tab of the View Style Dialog  <br> License requirements : drafting ("DRAFTING") */
            public: void SetWidth
            (
                NXOpen::Preferences::Width width /** Sets a new width on the smooth edge sub-builder */
            );
            /**Returns  the end gaps toggle on the SMOOTH EDGES tab of the View Style Dialog  <br> License requirements : None */
            public: bool EndGaps
            (
            );
            /**Sets  the end gaps toggle on the SMOOTH EDGES tab of the View Style Dialog  <br> License requirements : drafting ("DRAFTING") */
            public: void SetEndGaps
            (
                bool endGapsToggle /** Sets a new end gaps toggle value on the smooth edge sub-builder */
            );
            /**Returns  the end gaps data on the SMOOTH EDGES tab of the View Style Dialog  <br> License requirements : None */
            public: double EndGapsDistance
            (
            );
            /**Sets  the end gaps data on the SMOOTH EDGES tab of the View Style Dialog  <br> License requirements : drafting ("DRAFTING") */
            public: void SetEndGapsDistance
            (
                double endGapsData /** Sets new end gaps data on the smooth edge sub-builder */
            );
            /** Returns true if the inputs to the component are sufficient for 
                        commit to be called.  For example, if the component requires
                        you to set some property, this method will return false if
                        you haven't set it.  This method throws a not-yet-implemented
                        NXException for some components.
                     @return  Was self validation successful  <br> License requirements : None */
            public: virtual bool Validate
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif