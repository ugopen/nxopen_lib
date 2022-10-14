#ifndef NXOpen_DRAWINGS_DRAWINGVIEWBUILDER_HXX_INCLUDED
#define NXOpen_DRAWINGS_DRAWINGVIEWBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Drawings_DrawingViewBuilder.ja
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
#include <NXOpen/Drawings_MultipleViewPlacementBuilder.hxx>
#include <NXOpen/Drawings_View2dOrientBuilder.hxx>
#include <NXOpen/Drawings_ViewBoundaryBuilder.hxx>
#include <NXOpen/Drawings_ViewCenterCoordinateBuilder.hxx>
#include <NXOpen/Drawings_ViewPlacementBuilder.hxx>
#include <NXOpen/Drawings_ViewScaleBuilder.hxx>
#include <NXOpen/Drawings_ViewStyleBuilder.hxx>
#include <NXOpen/Builder.hxx>
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
        class DrawingViewBuilder;
    }
    class Builder;
    namespace Drawings
    {
        class MultipleViewPlacementBuilder;
    }
    namespace Drawings
    {
        class View2dOrientBuilder;
    }
    namespace Drawings
    {
        class ViewBoundaryBuilder;
    }
    namespace Drawings
    {
        class ViewCenterCoordinateBuilder;
    }
    namespace Drawings
    {
        class ViewPlacementBuilder;
    }
    namespace Drawings
    {
        class ViewScaleBuilder;
    }
    namespace Drawings
    {
        class ViewStyleBuilder;
    }
    namespace Drawings
    {
        class _DrawingViewBuilderBuilder;
        class DrawingViewBuilderImpl;
        /** This builder allows the user to create a Drawing View  <br> To create a new instance of this class, use @link NXOpen::Drawings::DraftingViewCollection::CreateDrawingViewBuilder  NXOpen::Drawings::DraftingViewCollection::CreateDrawingViewBuilder @endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        MultipleViewPlacement.OptionType </td> <td> 
         
        Center </td> </tr> 

        <tr><td> 
         
        MultipleViewPlacement.ViewPlacementCenter.AlignmentMethod </td> <td> 
         
        Infer </td> </tr> 

        <tr><td> 
         
        MultipleViewPlacement.ViewPlacementCenter.AlignmentOption </td> <td> 
         
        ToView </td> </tr> 

        <tr><td> 
         
        Scale.Denominator </td> <td> 
         
        1.0 </td> </tr> 

        <tr><td> 
         
        Scale.Numerator </td> <td> 
         
        1.0 </td> </tr> 

        <tr><td> 
         
        Scale.ScaleType </td> <td> 
         
        Ratio </td> </tr> 

        <tr><td> 
         
        ViewStyle.ViewStyleGeneral.AngleSetting.Angle.Value </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        ViewStyle.ViewStyleGeneral.AngleSetting.Associative </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        ViewStyle.ViewStyleGeneral.AngleSetting.EvaluationPlane </td> <td> 
         
        DrawingSheet </td> </tr> 

        <tr><td> 
         
        ViewStyle.ViewStyleOrientation.HingeLine.ReverseDirection </td> <td> 
         
        false </td> </tr> 

        <tr><td> 
         
        ViewStyle.ViewStyleOrientation.HingeLine.VectorOption </td> <td> 
         
        Inferred </td> </tr> 

        <tr><td> 
         
        ViewStyle.ViewStyleOrientation.Ovt.AssociativeOrientation </td> <td> 
         
        0 </td> </tr> 

        </table>  

         <br>  Created in NX6.0.0.  <br>  
        */
        class NXOPENCPP_DRAWINGSEXPORT  DrawingViewBuilder : public NXOpen::Builder
        {
            private: DrawingViewBuilderImpl * m_drawingviewbuilder_impl;
            private: friend class  _DrawingViewBuilderBuilder;
            protected: DrawingViewBuilder();
            public: ~DrawingViewBuilder();
            /**Returns  the multiple view placement 
             <br>  Created in NX6.0.2.  <br>  
             <br> License requirements : None */
            public: NXOpen::Drawings::MultipleViewPlacementBuilder * MultipleViewPlacement
            (
            );
            /**Returns  the view boundary.
                        It is replace by @link Drawings::DrawingViewBuilder::MultipleViewPlacement Drawings::DrawingViewBuilder::MultipleViewPlacement@endlink  
             <br>  @deprecated Deprecated in NX6.0.2.  Use @link Drawings::DrawingViewBuilder::MultipleViewPlacement Drawings::DrawingViewBuilder::MultipleViewPlacement@endlink  <br>  

             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX6.0.2.  Use Drawings::DrawingViewBuilder::MultipleViewPlacement") NXOpen::Drawings::ViewBoundaryBuilder * ViewBoundary
            (
            );
            /**Returns  the view placement.
                        It is replace by @link Drawings::DrawingViewBuilder::MultipleViewPlacement Drawings::DrawingViewBuilder::MultipleViewPlacement@endlink  
             <br>  @deprecated Deprecated in NX6.0.2.  Use @link Drawings::DrawingViewBuilder::MultipleViewPlacement Drawings::DrawingViewBuilder::MultipleViewPlacement@endlink  <br>  

             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX6.0.2.  Use Drawings::DrawingViewBuilder::MultipleViewPlacement") NXOpen::Drawings::ViewPlacementBuilder * ViewPlacement
            (
            );
            /**Returns  the view scale 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Drawings::ViewScaleBuilder * Scale
            (
            );
            /**Returns  the view orientation in 2D 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Drawings::View2dOrientBuilder * TwodOrientation
            (
            );
            /**Returns  the view style 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Drawings::ViewStyleBuilder * ViewStyle
            (
            );
            /**Returns  the center coordinate 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Drawings::ViewCenterCoordinateBuilder * CenterCoordinate
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