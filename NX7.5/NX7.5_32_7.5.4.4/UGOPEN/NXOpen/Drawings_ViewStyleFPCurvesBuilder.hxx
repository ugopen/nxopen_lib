#ifndef NXOpen_DRAWINGS_VIEWSTYLEFPCURVESBUILDER_HXX_INCLUDED
#define NXOpen_DRAWINGS_VIEWSTYLEFPCURVESBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Drawings_ViewStyleFPCurvesBuilder.ja
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
#include <NXOpen/Drawings_ViewStyleFPCurvesBuilder.hxx>
#include <NXOpen/GeometricUtilities_IComponentBuilder.hxx>
#include <NXOpen/Preferences_ViewStylePreferencesData.hxx>
#include <NXOpen/SheetMetal_FlatPatternSettings.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Drawings
    {
        class ViewStyleFPCurvesBuilder;
    }
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    class NXColor;
    namespace Drawings
    {
        class _ViewStyleFPCurvesBuilderBuilder;
        class ViewStyleFPCurvesBuilderImpl;
        /** Represents the Curve section of the Flat Pattern tab on the View Style Dialog (Drawings.ViewStyleFPCurvesBuilder)
            */
        class NXOPENCPPEXPORT  ViewStyleFPCurvesBuilder : public TaggedObject, public virtual GeometricUtilities::IComponentBuilder
        {
            private: ViewStyleFPCurvesBuilderImpl * m_viewstylefpcurvesbuilder_impl;
            private: friend class  _ViewStyleFPCurvesBuilderBuilder;
            protected: ViewStyleFPCurvesBuilder();
            public: ~ViewStyleFPCurvesBuilder();
            /**Returns  the type of Flat Pattern Curve  <br> License requirements : None */
            public: NXOpen::SheetMetal::FlatPatternSettings::FlatPatternObjectType Type
            (
            );
            /**Returns  the state toggle on the Curve section of the Flat Pattern tab of the View Style Dialog  <br> License requirements : None */
            public: bool State
            (
            );
            /**Sets  the state toggle on the Curve section of the Flat Pattern tab of the View Style Dialog  <br> License requirements : drafting ("DRAFTING") */
            public: void SetState
            (
                bool stateToggle /** Sets a new state toggle value on the curve section of the flat pattern sub-builder */
            );
            /**Returns  the color on the Curve section of the Flat Pattern tab of the View Style Dialog  <br> License requirements : None */
            public: NXOpen::NXColor * Color
            (
            );
            /**Sets  the color on the Curve section of the Flat Pattern tab of the View Style Dialog  <br> License requirements : drafting ("DRAFTING") */
            public: void SetColor
            (
                NXOpen::NXColor * color /** Sets a new color on the curve section of the flat pattern sub-builder */
            );
            /**Returns  the font on the Curve section of the Flat Pattern tab of the View Style Dialog  <br> License requirements : None */
            public: NXOpen::Preferences::Font Font
            (
            );
            /**Sets  the font on the Curve section of the Flat Pattern tab of the View Style Dialog  <br> License requirements : drafting ("DRAFTING") */
            public: void SetFont
            (
                NXOpen::Preferences::Font font /** Sets a new font on the curve section of the flat pattern sub-builder */
            );
            /**Returns  the width on the Curve section of the Flat Pattern tab of the View Style Dialog  <br> License requirements : None */
            public: NXOpen::Preferences::Width Width
            (
            );
            /**Sets  the width on the Curve section of the Flat Pattern tab of the View Style Dialog  <br> License requirements : drafting ("DRAFTING") */
            public: void SetWidth
            (
                NXOpen::Preferences::Width width /** Sets a new width on the curve section of the flat pattern sub-builder */
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