#ifndef NXOpen_DRAWINGS_VIEWPROJECTEDARROWSETTINGSBUILDER_HXX_INCLUDED
#define NXOpen_DRAWINGS_VIEWPROJECTEDARROWSETTINGSBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Drawings_ViewProjectedArrowSettingsBuilder.ja
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
#include <NXOpen/LineColorFontWidthBuilder.hxx>
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
        class ViewProjectedArrowSettingsBuilder;
    }
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    class LineColorFontWidthBuilder;
    namespace Drawings
    {
        class _ViewProjectedArrowSettingsBuilderBuilder;
        class ViewProjectedArrowSettingsBuilderImpl;
        /** Represents a @link NXOpen::Drawings::ViewProjectedArrowSettingsBuilder NXOpen::Drawings::ViewProjectedArrowSettingsBuilder@endlink  
         <br>  Created in NX9.0.0.  <br>  
        */
        class NXOPENCPP_DRAWINGSEXPORT  ViewProjectedArrowSettingsBuilder : public NXOpen::TaggedObject, public virtual NXOpen::GeometricUtilities::IComponentBuilder
        {
            /**  Represents arrowhead style
                    */
            public: enum DimensionsStyleType
            {
                DimensionsStyleTypeFilled/** filled */ ,
                DimensionsStyleTypeClosed/** closed */ ,
                DimensionsStyleTypeOpen/** open */ 
            };

            /**  Represents display label type
                    */
            public: enum DispalyLabelType
            {
                DispalyLabelTypeNo/** no */ ,
                DispalyLabelTypeOnReferenceArrow/** on reference arrow */ ,
                DispalyLabelTypeOnReferenceArrowAndView/** on reference arrow and view */ 
            };

            private: ViewProjectedArrowSettingsBuilderImpl * m_viewprojectedarrowsettingsbuilder_impl;
            private: friend class  _ViewProjectedArrowSettingsBuilderBuilder;
            protected: ViewProjectedArrowSettingsBuilder();
            public: ~ViewProjectedArrowSettingsBuilder();
            /**Returns  the display label 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Drawings::ViewProjectedArrowSettingsBuilder::DispalyLabelType DisplayLabel
            (
            );
            /**Sets  the display label 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetDisplayLabel
            (
                NXOpen::Drawings::ViewProjectedArrowSettingsBuilder::DispalyLabelType displayLabel /** displaylabel */ 
            );
            /**Returns  the size factor 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: double SizeFactor
            (
            );
            /**Sets  the size factor 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetSizeFactor
            (
                double sizeFactor /** sizefactor */ 
            );
            /**Returns  the arrow head style 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Drawings::ViewProjectedArrowSettingsBuilder::DimensionsStyleType ArrowHeadStyle
            (
            );
            /**Sets  the arrow head style 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetArrowHeadStyle
            (
                NXOpen::Drawings::ViewProjectedArrowSettingsBuilder::DimensionsStyleType arrowHeadStyle /** arrowheadstyle */ 
            );
            /**Returns  the arrow head length 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: double ArrowHeadLength
            (
            );
            /**Sets  the arrow head length 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetArrowHeadLength
            (
                double arrowHeadLength /** arrowheadlength */ 
            );
            /**Returns  the arrow head angle 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: double ArrowHeadAngle
            (
            );
            /**Sets  the arrow head angle 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetArrowHeadAngle
            (
                double arrowHeadAngle /** arrowheadangle */ 
            );
            /**Returns  the arrow line length 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: double ArrowLineLength
            (
            );
            /**Sets  the arrow line length 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetArrowLineLength
            (
                double arrowLineLength /** arrowlinelength */ 
            );
            /**Returns  the arrow line distance to geometry 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: double ArrowLineDistanceToGeometry
            (
            );
            /**Sets  the arrow line distance to geometry 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetArrowLineDistanceToGeometry
            (
                double arrowLineDistanceToGeometry /** arrowlinedistancetogeometry */ 
            );
            /**Returns  the line color font width0 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::LineColorFontWidthBuilder * LineColorFontWidth
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