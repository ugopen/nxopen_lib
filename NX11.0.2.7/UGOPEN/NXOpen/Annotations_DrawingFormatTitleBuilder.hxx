#ifndef NXOpen_ANNOTATIONS_DRAWINGFORMATTITLEBUILDER_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_DRAWINGFORMATTITLEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_DrawingFormatTitleBuilder.ja
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
#include <NXOpen/Annotations_DrawingFormatTitleBuilder.hxx>
#include <NXOpen/GeometricUtilities_IComponentBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_annotations_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Annotations
    {
        class DrawingFormatTitleBuilder;
    }
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    namespace Annotations
    {
        class _DrawingFormatTitleBuilderBuilder;
        class DrawingFormatTitleBuilderImpl;
        /** Represents a @link NXOpen::Annotations::DrawingFormatTitleBuilder NXOpen::Annotations::DrawingFormatTitleBuilder@endlink 
         <br>  Created in NX9.0.0.  <br>  
        */
        class NXOPENCPP_ANNOTATIONSEXPORT  DrawingFormatTitleBuilder : public NXOpen::TaggedObject, public virtual NXOpen::GeometricUtilities::IComponentBuilder
        {
            /** Represent the option of TitleBlockPosition that specifies Type display */
            public: enum TitleBlockPositionType
            {
                TitleBlockPositionTypeTopLeft/** top left */ ,
                TitleBlockPositionTypeTopRight/** top right */ ,
                TitleBlockPositionTypeBottomLeft/** bottom left */ ,
                TitleBlockPositionTypeBottomRight/** bottom right */ 
            };

            private: DrawingFormatTitleBuilderImpl * m_drawingformattitlebuilder_impl;
            private: friend class  _DrawingFormatTitleBuilderBuilder;
            protected: DrawingFormatTitleBuilder();
            public: ~DrawingFormatTitleBuilder();
            /**Returns  the option that specifies how the title block aligns relative to the cursor during placement 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::DrawingFormatTitleBuilder::TitleBlockPositionType TitleBlockAlignmentPosition
            (
            );
            /**Sets  the option that specifies how the title block aligns relative to the cursor during placement 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetTitleBlockAlignmentPosition
            (
                NXOpen::Annotations::DrawingFormatTitleBuilder::TitleBlockPositionType titleBlockAlignmentPosition /** titleblockalignmentposition */ 
            );
            /**Returns  the flag that determines whether or not the title block updates automatically whenever a change occurs to a referenced object in the model 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: bool Automatic
            (
            );
            /**Sets  the flag that determines whether or not the title block updates automatically whenever a change occurs to a referenced object in the model 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetAutomatic
            (
                bool automatic /** automatic */ 
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