#ifndef NXOpen_DRAWINGS_VIEWSTYLESECONDARYCOMPONENTSBUILDER_HXX_INCLUDED
#define NXOpen_DRAWINGS_VIEWSTYLESECONDARYCOMPONENTSBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Drawings_ViewStyleSecondaryComponentsBuilder.ja
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
#include <NXOpen/Drawings_ViewStyleSecondaryComponentsBuilder.hxx>
#include <NXOpen/Drawings_VisibleAndHiddenLinesColorFontWidthBuilder.hxx>
#include <NXOpen/GeometricUtilities_IComponentBuilder.hxx>
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
        class ViewStyleSecondaryComponentsBuilder;
    }
    namespace Drawings
    {
        class VisibleAndHiddenLinesColorFontWidthBuilder;
    }
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    namespace Drawings
    {
        class _ViewStyleSecondaryComponentsBuilderBuilder;
        class ViewStyleSecondaryComponentsBuilderImpl;
        /** Represents the Secondary Geometry tab on the View Style Dialog (Drawings.ViewStyleHiddenLinesBuilder)
            
         <br>  Created in NX11.0.0.  <br>  
        */
        class NXOPENCPP_DRAWINGSEXPORT  ViewStyleSecondaryComponentsBuilder : public NXOpen::TaggedObject, public virtual NXOpen::GeometricUtilities::IComponentBuilder
        {
            private: ViewStyleSecondaryComponentsBuilderImpl * m_viewstylesecondarycomponentsbuilder_impl;
            private: friend class  _ViewStyleSecondaryComponentsBuilderBuilder;
            protected: ViewStyleSecondaryComponentsBuilder();
            public: ~ViewStyleSecondaryComponentsBuilder();
            /**Returns  the Secondary Geometry toggle on Secondary Geometry tab of View Style Dialog. 
                    If true, the secondary geometry display properties are processed separately from the primary geometry.
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: bool ProcessSecondaryComponents
            (
            );
            /**Sets  the Secondary Geometry toggle on Secondary Geometry tab of View Style Dialog. 
                    If true, the secondary geometry display properties are processed separately from the primary geometry.
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetProcessSecondaryComponents
            (
                bool processSecondaryComponents /** processsecondarycomponents */ 
            );
            /**Returns  the Secondary Geometry Hidden by Primary Geometry toggle on Secondary Geometry tab of View Style Dialog. 
                    If true, the secondary geometry display properties are processed with respect to the primary geometry.
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: bool ProcessSecondaryHiddenByPrimary
            (
            );
            /**Sets  the Secondary Geometry Hidden by Primary Geometry toggle on Secondary Geometry tab of View Style Dialog. 
                    If true, the secondary geometry display properties are processed with respect to the primary geometry.
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetProcessSecondaryHiddenByPrimary
            (
                bool processSecondaryHiddenByPrimary /** processsecondaryhiddenbyprimary */ 
            );
            /**Returns  the Primary Geometry Hidden by Secondary Geometry toggle on Secondary Geometry tab of View Style Dialog. 
                    If true, the primary geometry display properties are processed with respect to the secondary geometry.
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: bool ProcessPrimaryHiddenBySecondary
            (
            );
            /**Sets  the Primary Geometry Hidden by Secondary Geometry toggle on Secondary Geometry tab of View Style Dialog. 
                    If true, the primary geometry display properties are processed with respect to the secondary geometry.
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetProcessPrimaryHiddenBySecondary
            (
                bool processPrimaryHiddenBySecondary /** processprimaryhiddenbysecondary */ 
            );
            /**Returns  the Show Smooth Edges toggle on Secondary Geometry tab of View Style Dialog. 
                    If true, the smooth edges are displayed for secondary geometry.
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: bool ShowSmoothEdges
            (
            );
            /**Sets  the Show Smooth Edges toggle on Secondary Geometry tab of View Style Dialog. 
                    If true, the smooth edges are displayed for secondary geometry.
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetShowSmoothEdges
            (
                bool showSmoothEdges /** showsmoothedges */ 
            );
            /**Returns  the Show Virtual Intersections toggle on Secondary Geometry tab of View Style Dialog.
                    If true, the virtual intersection lines are displayed for secondary geometry.
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: bool ShowVirtualIntersections
            (
            );
            /**Sets  the Show Virtual Intersections toggle on Secondary Geometry tab of View Style Dialog.
                    If true, the virtual intersection lines are displayed for secondary geometry.
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetShowVirtualIntersections
            (
                bool showVirtualIntersections /** showvirtualintersections */ 
            );
            /**Returns  the visible and hidden lines color, font, and width of secondary geometry.
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Drawings::VisibleAndHiddenLinesColorFontWidthBuilder * SecondaryComponentsCFW
            (
            );
            /**Returns  the visible and hidden lines color, font, and width of secondary geometry that is hidden by primary geometry. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Drawings::VisibleAndHiddenLinesColorFontWidthBuilder * SecondaryHiddenByPrimaryCFW
            (
            );
            /**Returns  the visible and hidden lines color, font, and width of primary geometry that is hidden by secondary geometry. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Drawings::VisibleAndHiddenLinesColorFontWidthBuilder * PrimaryHiddenBySecondaryCFW
            (
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