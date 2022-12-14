#ifndef NXOpen_DRAWINGS_VIEWSTYLE_HXX_INCLUDED
#define NXOpen_DRAWINGS_VIEWSTYLE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Drawings_ViewStyle.ja
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
#include <NXOpen/TaggedObject.hxx>
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
        class ViewStyle;
    }
    namespace Drawings
    {
        class DraftingView;
    }
    namespace Drawings
    {
        class BaseViewStyle;
    }
    namespace Drawings
    {
        class FlatPatternViewStyle;
    }
    namespace Drawings
    {
        class GeneralViewStyle;
    }
    namespace Drawings
    {
        class HiddenLinesViewStyle;
    }
    namespace Drawings
    {
        class InheritPmiViewStyle;
    }
    namespace Drawings
    {
        class OrientationViewStyle;
    }
    namespace Drawings
    {
        class PerspectiveViewStyle;
    }
    namespace Drawings
    {
        class ProjectedViewStyle;
    }
    namespace Drawings
    {
        class SectionViewStyle;
    }
    namespace Drawings
    {
        class ShadingViewStyle;
    }
    namespace Drawings
    {
        class ShipDraftingViewLinesViewStyle;
    }
    namespace Drawings
    {
        class ShipGeneralArrangementViewLinesViewStyle;
    }
    namespace Drawings
    {
        class ShipbuildingLinesViewStyle;
    }
    namespace Drawings
    {
        class SmoothEdgesViewStyle;
    }
    namespace Drawings
    {
        class ThreadsViewStyle;
    }
    namespace Drawings
    {
        class TraceLinesViewStyle;
    }
    namespace Drawings
    {
        class VirtualIntersectionsViewStyle;
    }
    namespace Drawings
    {
        class VisibleLinesViewStyle;
    }
    namespace Drawings
    {
        class ViewStyleImpl;
        /** Represents set of style applicable to drafting views.  <br> To obtain an instance of this class, refer to @link NXOpen::Drawings::DraftingView  NXOpen::Drawings::DraftingView @endlink  <br> 
         <br>  Created in NX5.0.0.  <br>  
        */
        class NXOPENCPP_DRAWINGSEXPORT  ViewStyle
        {
            private: ViewStyleImpl * m_viewstyle_impl;
            private: NXOpen::Drawings::DraftingView* m_owner;
            /// \cond NX_NO_DOC 
            public: explicit ViewStyle(NXOpen::Drawings::DraftingView *owner);


            /// \endcond 
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~ViewStyle();


            /** Returns object for doing View style settings applicable to General 
             <br>  Created in NX3.0.0.  <br>  
            */
            public: NXOpen::Drawings::GeneralViewStyle *General();
            /** Returns object for doing View style settings applicable to Basedata 
             <br>  Created in NX3.0.0.  <br>  
            */
            public: NXOpen::Drawings::BaseViewStyle *BaseView();
            /** Returns object for doing View style settings applicable to Projected 
             <br>  Created in NX3.0.0.  <br>  
            */
            public: NXOpen::Drawings::ProjectedViewStyle *Projected();
            /** Returns object for doing View style settings applicable to InheritPmi 
             <br>  Created in NX3.0.0.  <br>  
            */
            public: NXOpen::Drawings::InheritPmiViewStyle *InheritPmi();
            /** Returns object for doing View style settings applicable to Section 
             <br>  Created in NX3.0.0.  <br>  
            */
            public: NXOpen::Drawings::SectionViewStyle *Section();
            /** Returns object for doing View style settings applicable to VirtualIntersections 
             <br>  Created in NX3.0.0.  <br>  
            */
            public: NXOpen::Drawings::VirtualIntersectionsViewStyle *VirtualIntersections();
            /** Returns object for doing View style settings applicable to SmoothEdges 
             <br>  Created in NX3.0.0.  <br>  
            */
            public: NXOpen::Drawings::SmoothEdgesViewStyle *SmoothEdges();
            /** Returns object for doing View style settings applicable to Perspective 
             <br>  Created in NX3.0.0.  <br>  
            */
            public: NXOpen::Drawings::PerspectiveViewStyle *Perspective();
            /** Returns object for doing View style settings applicable to Orientation 
             <br>  Created in NX3.0.0.  <br>  
            */
            public: NXOpen::Drawings::OrientationViewStyle *Orientation();
            /** Returns object for doing View style settings applicable to VisibleLines 
             <br>  Created in NX3.0.0.  <br>  
            */
            public: NXOpen::Drawings::VisibleLinesViewStyle *VisibleLines();
            /** Returns object for doing View style settings applicable to Threads 
             <br>  Created in NX3.0.0.  <br>  
            */
            public: NXOpen::Drawings::ThreadsViewStyle *Threads();
            /** Returns object for doing View style settings applicable to TraceLines 
             <br>  Created in NX3.0.0.  <br>  
            */
            public: NXOpen::Drawings::TraceLinesViewStyle *TraceLines();
            /** Returns object for doing View style settings applicable to HiddenLines 
             <br>  Created in NX3.0.0.  <br>  
            */
            public: NXOpen::Drawings::HiddenLinesViewStyle *HiddenLines();
            /** Returns object for doing View style settings applicable to Shading 
             <br>  Created in NX3.0.0.  <br>  
            */
            public: NXOpen::Drawings::ShadingViewStyle *Shading();
            /** Returns object for doing View style settings applicable to Flat Pattern Views. 
             <br>  Created in NX3.0.0.  <br>  
            */
            public: NXOpen::Drawings::FlatPatternViewStyle *FlatPattern();
            /** Returns object for doing View style settings applicable to Ship Lines. 
             <br>  Created in NX8.0.0.  <br>  
            */
            public: NXOpen::Drawings::ShipbuildingLinesViewStyle *ShipbuildingLines();
            /** Returns object for doing View style settings applicable to Ship Drafting View Lines. 
             <br>  Created in NX10.0.0.  <br>  
            */
            public: NXOpen::Drawings::ShipDraftingViewLinesViewStyle *ShipDraftingViewLines();
            /** Returns object for doing View style settings applicable to Ship General Arrangement View Lines. 
             <br>  Created in NX1926.0.0.  <br>  
            */
            public: NXOpen::Drawings::ShipGeneralArrangementViewLinesViewStyle *ShipGeneralArrangementViewLines();
        }; //lint !e1712 default constructor not defined for class  

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
