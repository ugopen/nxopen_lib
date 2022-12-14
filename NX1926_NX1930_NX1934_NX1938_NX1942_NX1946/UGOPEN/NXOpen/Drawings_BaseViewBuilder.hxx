#ifndef NXOpen_DRAWINGS_BASEVIEWBUILDER_HXX_INCLUDED
#define NXOpen_DRAWINGS_BASEVIEWBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Drawings_BaseViewBuilder.ja
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
#include <NXOpen/Drawings_DraftingComponentSelectionBuilder.hxx>
#include <NXOpen/Drawings_HiddenObjectsBuilder.hxx>
#include <NXOpen/Drawings_SelectModelViewBuilder.hxx>
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
        class BaseViewBuilder;
    }
    class Builder;
    namespace Drawings
    {
        class DraftingComponentSelectionBuilder;
    }
    namespace Drawings
    {
        class HiddenObjectsBuilder;
    }
    namespace Drawings
    {
        class SelectModelViewBuilder;
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
        class _BaseViewBuilderBuilder;
        class BaseViewBuilderImpl;
        /** Represents a @link NXOpen::Drawings::BaseView NXOpen::Drawings::BaseView@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::Drawings::DraftingViewCollection::CreateBaseViewBuilder  NXOpen::Drawings::DraftingViewCollection::CreateBaseViewBuilder @endlink  <br> 
        Default values.
        <list type="table"> 
         
        <listheader><term> 
        Property</term>  <description> 
        Value</description> </listheader>
        <item><term> 
         
        Placement.AlignmentMethod </term> <description> 
         
        Infer </description> </item> 

        <item><term> 
         
        Placement.AlignmentOption </term> <description> 
         
        ToView </description> </item> 

        <item><term> 
         
        Scale.Denominator </term> <description> 
         
        1.0 </description> </item> 

        <item><term> 
         
        Scale.Numerator </term> <description> 
         
        1.0 </description> </item> 

        <item><term> 
         
        Scale.ScaleType </term> <description> 
         
        Ratio </description> </item> 

        <item><term> 
         
        SecondaryComponents.ObjectType </term> <description> 
         
        PrimaryGeometry </description> </item> 

        <item><term> 
         
        Style.ViewStyleGeneral.AngleSetting.Angle.Value </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        Style.ViewStyleGeneral.AngleSetting.Associative </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        Style.ViewStyleGeneral.AngleSetting.EvaluationPlane </term> <description> 
         
        DrawingSheet </description> </item> 

        <item><term> 
         
        Style.ViewStyleOrientation.HingeLine.ReverseDirection </term> <description> 
         
        false </description> </item> 

        <item><term> 
         
        Style.ViewStyleOrientation.HingeLine.VectorOption </term> <description> 
         
        Inferred </description> </item> 

        <item><term> 
         
        Style.ViewStyleOrientation.Ovt.AssociativeOrientation </term> <description> 
         
        0 </description> </item> 

        </list> 

         <br>  Created in NX6.0.0.  <br>  
        */
        class NXOPENCPP_DRAWINGSEXPORT  BaseViewBuilder : public NXOpen::Builder
        {
            private: BaseViewBuilderImpl * m_baseviewbuilder_impl;
            private: friend class  _BaseViewBuilderBuilder;
            protected: BaseViewBuilder();
            public: ~BaseViewBuilder();
            /**Returns  the view placement 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Drawings::ViewPlacementBuilder * Placement
            (
            );
            /**Returns  the model view 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Drawings::SelectModelViewBuilder * SelectModelView
            (
            );
            /**Returns  the view scale 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Drawings::ViewScaleBuilder * Scale
            (
            );
            /**Returns  the view style 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Drawings::ViewStyleBuilder * Style
            (
            );
            /**Returns  the list of objects to not show in the view 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Drawings::HiddenObjectsBuilder * HiddenObjects
            (
            );
            /**Returns  the list of objects to not section in the view 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Drawings::HiddenObjectsBuilder * NonSectionedObjects
            (
            );
            /**Returns  the list of secondary objects in the view 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Drawings::DraftingComponentSelectionBuilder * SecondaryComponents
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
