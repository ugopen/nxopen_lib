#ifndef NXOpen_DRAWINGS_SECTIONVIEWBUILDER_HXX_INCLUDED
#define NXOpen_DRAWINGS_SECTIONVIEWBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Drawings_SectionViewBuilder.ja
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
#include <NXOpen/Drawings_ParentViewBuilder.hxx>
#include <NXOpen/Drawings_SectionLineSegmentsBuilder.hxx>
#include <NXOpen/Drawings_SpecifySectionLineBuilder.hxx>
#include <NXOpen/Drawings_SvtBuilder.hxx>
#include <NXOpen/Drawings_ViewOrientationBuilder.hxx>
#include <NXOpen/Drawings_ViewPlacementBuilder.hxx>
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
        class SectionViewBuilder;
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
        class ParentViewBuilder;
    }
    namespace Drawings
    {
        class SectionLineSegmentsBuilder;
    }
    namespace Drawings
    {
        class SpecifySectionLineBuilder;
    }
    namespace Drawings
    {
        class SvtBuilder;
    }
    namespace Drawings
    {
        class ViewOrientationBuilder;
    }
    namespace Drawings
    {
        class ViewPlacementBuilder;
    }
    namespace Drawings
    {
        class ViewStyleBuilder;
    }
    namespace Drawings
    {
        class _SectionViewBuilderBuilder;
        class SectionViewBuilderImpl;
        /** Represents a @link NXOpen::Drawings::SectionView NXOpen::Drawings::SectionView@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::Drawings::DraftingViewCollection::CreateSectionViewBuilder  NXOpen::Drawings::DraftingViewCollection::CreateSectionViewBuilder @endlink  <br> 
        Default values.
        <list type="table"> 
         
        <listheader><term> 
        Property</term>  <description> 
        Value</description> </listheader>
        <item><term> 
         
        CreateFolded </term> <description> 
         
        1 </description> </item> 

        <item><term> 
         
        SecondaryComponents.ObjectType </term> <description> 
         
        PrimaryGeometry </description> </item> 

        <item><term> 
         
        SectionViewTool.Orientation </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        ViewPlacement.AlignmentMethod </term> <description> 
         
        Infer </description> </item> 

        <item><term> 
         
        ViewPlacement.AlignmentOption </term> <description> 
         
        ToView </description> </item> 

        <item><term> 
         
        ViewStyle.ViewStyleGeneral.AngleSetting.Angle.Value </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        ViewStyle.ViewStyleGeneral.AngleSetting.Associative </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        ViewStyle.ViewStyleGeneral.AngleSetting.EvaluationPlane </term> <description> 
         
        DrawingSheet </description> </item> 

        <item><term> 
         
        ViewStyle.ViewStyleGeneral.Scale.Denominator </term> <description> 
         
        1.0 </description> </item> 

        <item><term> 
         
        ViewStyle.ViewStyleGeneral.Scale.Numerator </term> <description> 
         
        1.0 </description> </item> 

        <item><term> 
         
        ViewStyle.ViewStyleGeneral.Scale.ScaleType </term> <description> 
         
        Ratio </description> </item> 

        <item><term> 
         
        ViewStyle.ViewStyleOrientation.HingeLine.ReverseDirection </term> <description> 
         
        false </description> </item> 

        <item><term> 
         
        ViewStyle.ViewStyleOrientation.HingeLine.VectorOption </term> <description> 
         
        Inferred </description> </item> 

        <item><term> 
         
        ViewStyle.ViewStyleOrientation.Ovt.AssociativeOrientation </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        ViewUnfolded (deprecated) </term> <description> 
         
        1 </description> </item> 

        </list> 

         <br>  Created in NX6.0.0.  <br>  
        */
        class NXOPENCPP_DRAWINGSEXPORT  SectionViewBuilder : public NXOpen::Builder
        {
            /**  Section Line Mode */
            public: enum SectionViewModeType
            {
                SectionViewModeTypeDynamic/** dynamic */ ,
                SectionViewModeTypeStandAlone/** stand alone */ 
            };

            /**  Section Line type */
            public: enum SectionLineType
            {
                SectionLineTypeSimpleStepped/** simple stepped */ ,
                SectionLineTypeHalf/** half */ ,
                SectionLineTypeRevolved/** revolved */ ,
                SectionLineTypePointToPoint/** point to point */ ,
                SectionLineTypePointAndAngle/** point and angle */ 
            };

            /**  Section Line Cut type */
            public: enum SectionCutType
            {
                SectionCutTypeFullPart/** full part */ ,
                SectionCutTypeSectionedPart/** sectioned part */ 
            };

            private: SectionViewBuilderImpl * m_sectionviewbuilder_impl;
            private: friend class  _SectionViewBuilderBuilder;
            protected: SectionViewBuilder();
            public: ~SectionViewBuilder();
            /**Returns  the section line mode 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Drawings::SectionViewBuilder::SectionViewModeType SectionViewMode
            (
            );
            /**Sets  the section line mode 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void SetSectionViewMode
            (
                NXOpen::Drawings::SectionViewBuilder::SectionViewModeType sectionViewMode /** sectionviewmode */ 
            );
            /**Returns  the section line type 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Drawings::SectionViewBuilder::SectionLineType SectionViewType
            (
            );
            /**Sets  the section line type 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void SetSectionViewType
            (
                NXOpen::Drawings::SectionViewBuilder::SectionLineType sectionLineType /** sectionlinetype */ 
            );
            /**Returns  the selected parent view 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Drawings::ParentViewBuilder * ParentView
            (
            );
            /**Returns  the section line segment builder 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Drawings::SectionLineSegmentsBuilder * SectionLineSegments
            (
            );
            /**Returns  the section Line 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Drawings::SpecifySectionLineBuilder * SectionLine
            (
            );
            /**Returns  the view orientation 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Drawings::ViewOrientationBuilder * ViewOrientation
            (
            );
            /**Returns  the view placement 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Drawings::ViewPlacementBuilder * ViewPlacement
            (
            );
            /**Returns  the section view tool 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Drawings::SvtBuilder * SectionViewTool
            (
            );
            /**Returns  the view style 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Drawings::ViewStyleBuilder * ViewStyle
            (
            );
            /**Returns  the view unfolded toggle 
             <br>  @deprecated Deprecated in NX10.0.0.  Use @link NXOpen::Drawings::SectionViewBuilder::CreateFolded NXOpen::Drawings::SectionViewBuilder::CreateFolded@endlink  <br>  

             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX10.0.0.  Use NXOpen::Drawings::SectionViewBuilder::CreateFolded") bool ViewUnfolded
            (
            );
            /**Sets  the view unfolded toggle 
             <br>  @deprecated Deprecated in NX10.0.0.  Use @link NXOpen::Drawings::SectionViewBuilder::SetCreateFolded NXOpen::Drawings::SectionViewBuilder::SetCreateFolded@endlink  <br>  

             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: NX_DEPRECATED("Deprecated in NX10.0.0.  Use NXOpen::Drawings::SectionViewBuilder::SetCreateFolded") void SetViewUnfolded
            (
                bool viewUnfolded /** viewunfolded */ 
            );
            /**Returns  the create folded 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: bool CreateFolded
            (
            );
            /**Sets  the create folded 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetCreateFolded
            (
                bool viewUnfolded /** viewunfolded */ 
            );
            /**Returns  the hidden objects 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Drawings::HiddenObjectsBuilder * HiddenObjects
            (
            );
            /**Returns  the non sectioned objects 
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