#ifndef NXOpen_DRAWINGS_VIEWSTYLETRACELINESBUILDER_HXX_INCLUDED
#define NXOpen_DRAWINGS_VIEWSTYLETRACELINESBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Drawings_ViewStyleTraceLinesBuilder.ja
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
        class ViewStyleTraceLinesBuilder;
    }
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    class NXColor;
    namespace Drawings
    {
        class _ViewStyleTraceLinesBuilderBuilder;
        class ViewStyleTraceLinesBuilderImpl;
        /** Represents the TRACE LINES tab on the View Style Dialog (Drawings.ViewStyleTraceLinesBuilder)
            
         <br>  Created in NX6.0.0.  <br>  
        */
        class NXOPENCPP_DRAWINGSEXPORT  ViewStyleTraceLinesBuilder : public NXOpen::TaggedObject, public virtual NXOpen::GeometricUtilities::IComponentBuilder
        {
            private: ViewStyleTraceLinesBuilderImpl * m_viewstyletracelinesbuilder_impl;
            private: friend class  _ViewStyleTraceLinesBuilderBuilder;
            protected: ViewStyleTraceLinesBuilder();
            public: ~ViewStyleTraceLinesBuilder();
            /**Returns  the visible color on the TRACE LINES tab of the View Style Dialog 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::NXColor * VisibleColor
            (
            );
            /**Sets  the visible color on the TRACE LINES tab of the View Style Dialog 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetVisibleColor
            (
                NXOpen::NXColor * visibleColor /** Sets a new visible color on the trace lines sub-builder */
            );
            /**Returns  the visible font on the TRACE LINES tab of the View Style Dialog 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Preferences::Font VisibleFont
            (
            );
            /**Sets  the visible font on the TRACE LINES tab of the View Style Dialog 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetVisibleFont
            (
                NXOpen::Preferences::Font font /** Sets a new visible font on the trace lines sub-builder */
            );
            /**Returns  the visible width on the TRACE LINES tab of the View Style Dialog 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Preferences::Width VisibleWidth
            (
            );
            /**Sets  the visible width on the TRACE LINES tab of the View Style Dialog 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetVisibleWidth
            (
                NXOpen::Preferences::Width width /** Sets a new visible width on the trace lines sub-builder */
            );
            /**Returns  the hidden color on the TRACE LINES tab of the View Style Dialog 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::NXColor * HiddenColor
            (
            );
            /**Sets  the hidden color on the TRACE LINES tab of the View Style Dialog 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetHiddenColor
            (
                NXOpen::NXColor * hiddenColor /** Sets a new hidden color on the trace lines sub-builder */
            );
            /**Returns  the hidden font on the TRACE LINES tab of the View Style Dialog 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Preferences::Font HiddenFont
            (
            );
            /**Sets  the hidden font on the TRACE LINES tab of the View Style Dialog 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetHiddenFont
            (
                NXOpen::Preferences::Font hiddenFont /** Sets a new hidden font on the trace lines sub-builder */
            );
            /**Returns  the hidden width on the TRACE LINES tab of the View Style Dialog 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Preferences::Width HiddenWidth
            (
            );
            /**Sets  the hidden width on the TRACE LINES tab of the View Style Dialog 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetHiddenWidth
            (
                NXOpen::Preferences::Width hiddenWidth /** Sets a new hidden width on the trace lines sub-builder */
            );
            /**Returns  the create gaps toggle on the TRACE LINES tab of the View Style Dialog 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: bool CreateGaps
            (
            );
            /**Sets  the create gaps toggle on the TRACE LINES tab of the View Style Dialog 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetCreateGaps
            (
                bool createGapsToggle /** Sets a new create gaps toggle value on the trace lines sub-builder */
            );
            /**Returns  the gap size on the TRACE LINES tab of the View Style Dialog 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: double GapSize
            (
            );
            /**Sets  the gap size on the TRACE LINES tab of the View Style Dialog 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetGapSize
            (
                double gapSize /** Sets a new gap size on the trace lines sub-builder */
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
