#ifndef NXOpen_FEATURES_SHIPDESIGN_INTERACTIVEANNOTATIONBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_SHIPDESIGN_INTERACTIVEANNOTATIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_ShipDesign_InteractiveAnnotationBuilder.ja
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
#include <NXOpen/Annotations_LeaderBuilder.hxx>
#include <NXOpen/Annotations_OriginBuilder.hxx>
#include <NXOpen/Annotations_StyleBuilder.hxx>
#include <NXOpen/Drawings_DraftingBody.hxx>
#include <NXOpen/Expression.hxx>
#include <NXOpen/Features_ShipDesign_InteractiveAnnotationTableBuilder.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/libnxopencpp_features_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Features
    {
        namespace ShipDesign
        {
            class InteractiveAnnotationBuilder;
        }
    }
    namespace Annotations
    {
        class BaseCustomSymbol;
    }
    namespace Annotations
    {
        class LeaderBuilder;
    }
    namespace Annotations
    {
        class OriginBuilder;
    }
    namespace Annotations
    {
        class StyleBuilder;
    }
    namespace Annotations
    {
        class Table;
    }
    namespace Assemblies
    {
        class Component;
    }
    class Builder;
    class DisplayableObject;
    namespace Drawings
    {
        class DraftingBody;
    }
    namespace Drawings
    {
        class DraftingCurve;
    }
    namespace Drawings
    {
        class DraftingView;
    }
    class Expression;
    namespace Features
    {
        namespace ShipDesign
        {
            class InteractiveAnnotationTableBuilder;
        }
    }
    class Line;
    class NXObject;
    class Point;
    namespace Features
    {
        namespace ShipDesign
        {
            class _InteractiveAnnotationBuilderBuilder;
            class InteractiveAnnotationBuilderImpl;
            /** Represents a @link NXOpen::Features::ShipDesign::InteractiveAnnotationBuilder NXOpen::Features::ShipDesign::InteractiveAnnotationBuilder@endlink  builder . This builder returns NULL.  <br> To create a new instance of this class, use @link NXOpen::Features::ShipCollection::CreateInteractiveAnnotationBuilder  NXOpen::Features::ShipCollection::CreateInteractiveAnnotationBuilder @endlink  <br> 
             <br>  Created in NX11.0.0.  <br>  
            */
            class NXOPENCPP_FEATURESEXPORT  InteractiveAnnotationBuilder : public NXOpen::Builder
            {
                private: InteractiveAnnotationBuilderImpl * m_interactiveannotationbuilder_impl;
                private: friend class  _InteractiveAnnotationBuilderBuilder;
                protected: InteractiveAnnotationBuilder();
                public: ~InteractiveAnnotationBuilder();
                /** Add annotations of sturcture ID And scantling.  
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : nx_ship_gen_arrange ("Ship General Arrangement") OR nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") OR nx_ship_mfg_prep ("Ship Manufacturing") */
                public: void AddAnnotationOfStructureIdAndScantling
                (
                    bool createIDAnnotation /** Create ID annotation or not */,
                    bool createScantlingAnnotation /** Create Scantling annotation or not */,
                    NXOpen::Drawings::DraftingBody * draftingBody /** draftingbody */ 
                );
                /** Add annotation of end cuts. 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : nx_ship_gen_arrange ("Ship General Arrangement") OR nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") OR nx_ship_mfg_prep ("Ship Manufacturing") */
                public: void AddAnnotationOfEndCuts
                (
                    bool createEndCutsSymbol /** Create End Cuts symbols or not*/,
                    NXOpen::Drawings::DraftingBody * draftingBody /** draftingbody */ 
                );
                /** Add annotation of opening filling line 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : nx_ship_gen_arrange ("Ship General Arrangement") OR nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") OR nx_ship_mfg_prep ("Ship Manufacturing") */
                public: void AddAnnotationOfOpeningFillingLine
                (
                    bool createOpeningFillingLine /** createopeningfillingline */ ,
                    NXOpen::Drawings::DraftingBody * draftingbody /** draftingbody */ 
                );
                /** Add annotation of bracket 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : nx_ship_gen_arrange ("Ship General Arrangement") OR nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") OR nx_ship_mfg_prep ("Ship Manufacturing") */
                public: void AddAnnotationOfBracket
                (
                    bool createBracketSymbol /** createbracketsymbol */ ,
                    NXOpen::Drawings::DraftingBody * draftingbody /** draftingbody */ 
                );
                /** Add annotation of seam symbol for detail design 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : nx_ship_gen_arrange ("Ship General Arrangement") OR nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") OR nx_ship_mfg_prep ("Ship Manufacturing") */
                public: void AddAnnotationOfSeamForDetailDesign
                (
                    bool createSeamSymbol /** createseamsymbol */ ,
                    NXOpen::Drawings::DraftingView * tgView /** tgview */ ,
                    const std::vector<NXOpen::Drawings::DraftingBody *> & objects /** objects */ ,
                    NXOpen::Drawings::DraftingBody * selectedObjecty /** selectedobjecty */ 
                );
                /** Add annotation of seam symbol for non-sectioned plate for basic design 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : nx_ship_gen_arrange ("Ship General Arrangement") OR nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") OR nx_ship_mfg_prep ("Ship Manufacturing") */
                public: void HandleSeamForNonSectionedPlateForBasicDesign
                (
                    bool createSeamSymbol /** createseamsymbol */ ,
                    NXOpen::Drawings::DraftingCurve * draftingVDCurve /** Ship drafting curve*/,
                    NXOpen::NXObject * tgCurve /** tgcurve */ 
                );
                /** Add annotation of seam symbol for sectioned plate for basic design 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : nx_ship_gen_arrange ("Ship General Arrangement") OR nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") OR nx_ship_mfg_prep ("Ship Manufacturing") */
                public: void HandleSeamForSectionedPlateForBasicDesign
                (
                    bool createSeamSymbol /** createseamsymbol */ ,
                    NXOpen::Drawings::DraftingBody * tgDraftingBody /** tgdraftingbody */ ,
                    const std::vector<NXOpen::Drawings::DraftingCurve *> & objects /** objects */ ,
                    NXOpen::Drawings::DraftingCurve * selectedObject /** selectedobject */ 
                );
                /** Add annotation of structure ID and scantling on Ship Expansion View
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : nx_ship_gen_arrange ("Ship General Arrangement") OR nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") OR nx_ship_mfg_prep ("Ship Manufacturing") */
                public: void AddAnnotationOfExpansionStiffenerSturctureIdAndScantling
                (
                    NXOpen::Drawings::DraftingView * tgView /** The Ship Expansion View*/,
                    NXOpen::NXObject * shipStructure /** The Ship Structure on that the annotation will create. */,
                    bool createIDAnnotation /** Create ID annotation or not*/,
                    bool createScantlingAnnotation /** Create Scantling Annotation or not*/
                );
                /** Add annotation of expansion stiffener endcuts
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : nx_ship_gen_arrange ("Ship General Arrangement") OR nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") OR nx_ship_mfg_prep ("Ship Manufacturing") */
                public: void AddAnnotationOfExpansionStiffenerEndCuts
                (
                    NXOpen::Drawings::DraftingView * tgView /** The Ship Expansion View*/,
                    NXOpen::NXObject * shipStructure /** The Ship Structure on that the annotation will create. */,
                    bool createEndCutsSymbol /** Create End Cuts Symbol or not*/
                );
                /** Add annotation of expansion plate
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : nx_ship_gen_arrange ("Ship General Arrangement") OR nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") OR nx_ship_mfg_prep ("Ship Manufacturing") */
                public: void AddAnnotationOfExpansionPlate
                (
                    NXOpen::Drawings::DraftingView * tgView /** The Ship Expansion View*/,
                    NXOpen::NXObject * shipStructure /** The Ship Structure on that the annotation will create. */,
                    bool createScantlingAnnotation /** Create Scantling Annotation or not*/
                );
                /** Creates ship annotations for basic design structures.  @return  The ship entity annotation, entity type can be @link NXOpen::Body NXOpen::Body@endlink  or @link NXOpen::Face NXOpen::Face@endlink 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : nx_ship_gen_arrange ("Ship General Arrangement") OR nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") OR nx_ship_mfg_prep ("Ship Manufacturing") */
                public: NXOpen::NXObject * HandleAnnotationForBasicDesign
                (
                    bool createIDAnnotation /** Create Structure ID Annotation or not*/,
                    bool createScantlingAnnotation /** Create Scantling Annotation or not*/,
                    bool createEndCutsAnnotation /** Create EndCuts Annotation or not*/,
                    NXOpen::Drawings::DraftingCurve * draftingVDCurve /** Ship drafting curve*/,
                    NXOpen::NXObject * shipEntity /** The ship entity, entity type can be @link NXOpen::Body NXOpen::Body@endlink  or @link NXOpen::Face NXOpen::Face@endlink */,
                    NXOpen::Drawings::DraftingView * view /** Ship drafting section view*/
                );
                /** Adds opening filling lines by curve chain method. 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : nx_ship_gen_arrange ("Ship General Arrangement") OR nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") OR nx_ship_mfg_prep ("Ship Manufacturing") */
                public: void AddFillingLineByChain
                (
                    const std::vector<NXOpen::Drawings::DraftingCurve *> & curves /** Ship drafting curves*/,
                    bool createChainAnnotation /** Create Chain Annotation or not*/
                );
                /**  Adds opening filling lines by points method.  @return  Create line by points
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : nx_ship_gen_arrange ("Ship General Arrangement") OR nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") OR nx_ship_mfg_prep ("Ship Manufacturing") */
                public: NXOpen::Line * AddFillingLineByPoints
                (
                    NXOpen::Point * spiderPoint /** spider point*/,
                    NXOpen::Point * strikingPoint /** striking point*/
                );
                /** Modifies the position of opening filling line, which is created by points method. 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : nx_ship_gen_arrange ("Ship General Arrangement") OR nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") OR nx_ship_mfg_prep ("Ship Manufacturing") */
                public: void ModifyFillingLineByPoints
                (
                    NXOpen::Point * spiderPoint /** spider point*/,
                    NXOpen::Point * strikingPoint /** striking point*/,
                    NXOpen::Line * line /** line which created by point */
                );
                /** Deletes the existing annotations excluding the opening filling lines. 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : nx_ship_gen_arrange ("Ship General Arrangement") OR nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") OR nx_ship_mfg_prep ("Ship Manufacturing") */
                public: void DeleteExistingAnnotations
                (
                );
                /** Deletes the specific opening filling line.  
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : nx_ship_gen_arrange ("Ship General Arrangement") OR nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") OR nx_ship_mfg_prep ("Ship Manufacturing") */
                public: void DeleteOpeningFillingLine
                (
                    NXOpen::Line * line /** line */ 
                );
                /** Sets the table index 
                 <br>  @deprecated Deprecated in NX1872.0.0.  Use @link Features::ShipDesign::InteractiveAnnotationTableBuilder Features::ShipDesign::InteractiveAnnotationTableBuilder@endlink .SetTableIndex() instead. <br>  

                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : nx_ship_gen_arrange ("Ship General Arrangement") OR nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") OR nx_ship_mfg_prep ("Ship Manufacturing") */
                public: NX_DEPRECATED("Deprecated in NX1872.0.0.  Use Features::ShipDesign::InteractiveAnnotationTableBuilder.SetTableIndex() instead.") void SetTableIndex
                (
                    int inx /** inx */ 
                );
                /**  Sets the table position 
                 <br>  @deprecated Deprecated in NX1872.0.0.  Use @link Features::ShipDesign::InteractiveAnnotationTableBuilder Features::ShipDesign::InteractiveAnnotationTableBuilder@endlink .SetSelectPoint() instead. <br>  

                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : nx_ship_gen_arrange ("Ship General Arrangement") OR nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") OR nx_ship_mfg_prep ("Ship Manufacturing") */
                public: NX_DEPRECATED("Deprecated in NX1872.0.0.  Use Features::ShipDesign::InteractiveAnnotationTableBuilder.SetSelectPoint() instead.") void SetPosition
                (
                    const std::vector<double> & pos /** position */
                );
                /**  Creates the Table.  @return  table note
                 <br>  @deprecated Deprecated in NX1872.0.0.  Use @link Features::ShipDesign::InteractiveAnnotationBuilder::TableDefinition Features::ShipDesign::InteractiveAnnotationBuilder::TableDefinition@endlink .CreateTable() instead. <br>  

                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : nx_ship_gen_arrange ("Ship General Arrangement") OR nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") OR nx_ship_mfg_prep ("Ship Manufacturing") */
                public: NX_DEPRECATED("Deprecated in NX1872.0.0.  Use Features::ShipDesign::InteractiveAnnotationBuilder::TableDefinition.CreateTable() instead.") NXOpen::Annotations::Table * CreateTable
                (
                );
                /**  Creates the Table by the view plan.  @return  table note
                 <br>  @deprecated Deprecated in NX1872.0.0.  Use @link Features::ShipDesign::InteractiveAnnotationBuilder::TableDefinition Features::ShipDesign::InteractiveAnnotationBuilder::TableDefinition@endlink .CreateTable() instead. <br>  

                 <br>  Created in NX12.0.2.  <br>  
                 <br> License requirements : nx_ship_gen_arrange ("Ship General Arrangement") OR nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") OR nx_ship_mfg_prep ("Ship Manufacturing") */
                public: NX_DEPRECATED("Deprecated in NX1872.0.0.  Use Features::ShipDesign::InteractiveAnnotationBuilder::TableDefinition.CreateTable() instead.") NXOpen::Annotations::Table * CreateTableByViewPlan
                (
                    const NXString & viewPlan /** viewplan */ 
                );
                /**  Creates the Table by the view plan.  @return  table note
                 <br>  @deprecated Deprecated in NX1872.0.0.  Use @link Features::ShipDesign::InteractiveAnnotationBuilder::TableDefinition Features::ShipDesign::InteractiveAnnotationBuilder::TableDefinition@endlink .CreateTable() instead. <br>  

                 <br>  Created in NX12.0.2.  <br>  
                 <br> License requirements : nx_ship_gen_arrange ("Ship General Arrangement") OR nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") OR nx_ship_mfg_prep ("Ship Manufacturing") */
                NXOpen::Annotations::Table * CreateTableByViewPlan
                (
                    const char * viewPlan /** viewplan */ 
                );
                /** Gets the table index 
                 <br>  @deprecated Deprecated in NX1872.0.0.  Use @link Features::ShipDesign::InteractiveAnnotationBuilder::TableDefinition Features::ShipDesign::InteractiveAnnotationBuilder::TableDefinition@endlink .GetTableIndex() instead. <br>  

                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : nx_ship_gen_arrange ("Ship General Arrangement") OR nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") OR nx_ship_mfg_prep ("Ship Manufacturing") */
                public: NX_DEPRECATED("Deprecated in NX1872.0.0.  Use Features::ShipDesign::InteractiveAnnotationBuilder::TableDefinition.GetTableIndex() instead.") int GetTableIndex
                (
                );
                /**Returns  the @link NXOpen::Features::ShipDesign::InteractiveAnnotationTableBuilder NXOpen::Features::ShipDesign::InteractiveAnnotationTableBuilder@endlink  builder of the  
                        @link NXOpen::Features::ShipDesign::InteractiveAnnotationBuilder NXOpen::Features::ShipDesign::InteractiveAnnotationBuilder@endlink  builder. 
                 <br>  Created in NX1872.0.0.  <br>  
                 <br> License requirements : nx_ship_gen_arrange ("Ship General Arrangement") OR nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") OR nx_ship_mfg_prep ("Ship Manufacturing") */
                public: NXOpen::Features::ShipDesign::InteractiveAnnotationTableBuilder * TableDefinition
                (
                );
                /** Deletes opening filling lines 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : nx_ship_gen_arrange ("Ship General Arrangement") OR nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") OR nx_ship_mfg_prep ("Ship Manufacturing") */
                public: void DeleteLines
                (
                    const std::vector<NXOpen::Drawings::DraftingCurve *> & curves /** curves */ 
                );
                /** Adds opening filling lines by model body.  @return  Create Annotation or not
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : nx_ship_gen_arrange ("Ship General Arrangement") OR nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") OR nx_ship_mfg_prep ("Ship Manufacturing") */
                public: bool AddFillingLinesByModelBody
                (
                    NXOpen::Drawings::DraftingBody * draftingbody /** draftingbody */ ,
                    const std::vector<NXOpen::Drawings::DraftingCurve *> & curves /** Ship drafting curves*/
                );
                /**Returns  the annotation origin builder 
                 <br>  Created in NX12.0.2.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Annotations::OriginBuilder * Origin
                (
                );
                /**Returns  the annotation origin builder 
                 <br>  Created in NX12.0.2.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Annotations::StyleBuilder * Style
                (
                );
                /**Returns  the annotation leader builder 
                 <br>  Created in NX12.0.2.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Annotations::LeaderBuilder * Leader
                (
                );
                /**Returns  the ship type 
                 <br>  Created in NX12.0.2.  <br>  
                 <br> License requirements : None */
                public: int ShipType
                (
                );
                /**Sets  the ship type 
                 <br>  Created in NX12.0.2.  <br>  
                 <br> License requirements : nx_ship_gen_arrange ("Ship General Arrangement") OR nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") OR nx_ship_mfg_prep ("Ship Manufacturing") */
                public: void SetShipType
                (
                    int shipType /** shiptype */ 
                );
                /**Returns  the fire and safety method 
                 <br>  Created in NX12.0.2.  <br>  
                 <br> License requirements : None */
                public: int FireAndSafetyPlanMethod
                (
                );
                /**Sets  the fire and safety method 
                 <br>  Created in NX12.0.2.  <br>  
                 <br> License requirements : nx_ship_gen_arrange ("Ship General Arrangement") OR nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") OR nx_ship_mfg_prep ("Ship Manufacturing") */
                public: void SetFireAndSafetyPlanMethod
                (
                    int fireAndSafetyMethod /** fireandsafetymethod */ 
                );
                /**Returns  the symbol type 
                 <br>  Created in NX12.0.2.  <br>  
                 <br> License requirements : None */
                public: int SymbolType
                (
                );
                /**Sets  the symbol type 
                 <br>  Created in NX12.0.2.  <br>  
                 <br> License requirements : nx_ship_gen_arrange ("Ship General Arrangement") OR nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") OR nx_ship_mfg_prep ("Ship Manufacturing") */
                public: void SetSymbolType
                (
                    int symbolType /** symboltype */ 
                );
                /**Returns  the scale 
                 <br>  Created in NX12.0.2.  <br>  
                 <br> License requirements : nx_ship_gen_arrange ("Ship General Arrangement") OR nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") OR nx_ship_mfg_prep ("Ship Manufacturing") */
                public: NXOpen::Expression * Scale
                (
                );
                /** Add annotation of fire and safety 
                 <br>  Created in NX12.0.2.  <br>  
                 <br> License requirements : nx_ship_gen_arrange ("Ship General Arrangement") OR nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") OR nx_ship_mfg_prep ("Ship Manufacturing") */
                public: void AddAnnotationOfFireAndSafetyPlan
                (
                    bool bCreate /** bcreate */ ,
                    NXOpen::Drawings::DraftingView * tgView /** tgview */ ,
                    NXOpen::Assemblies::Component * tgComponent /** tgcomponent */ 
                );
                /** Update the fire and safety symbol part. 
                 <br>  Created in NX12.0.2.  <br>  
                 <br> License requirements : nx_ship_gen_arrange ("Ship General Arrangement") OR nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") OR nx_ship_mfg_prep ("Ship Manufacturing") */
                public: NXOpen::Annotations::BaseCustomSymbol * UpdateSymbolPart
                (
                );
                /** Add annotation of weld seam symbol for detail design 
                 <br>  Created in NX12.0.2.  <br>  
                 <br> License requirements : nx_ship_gen_arrange ("Ship General Arrangement") OR nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") OR nx_ship_mfg_prep ("Ship Manufacturing") */
                public: void AddAnnotationOfWeldSeamForDetailDesign
                (
                    bool createSeamSymbol /** createseamsymbol */ ,
                    NXOpen::Drawings::DraftingCurve * draftingVDCurve /** Ship drafting curve*/,
                    NXOpen::NXObject * tgCurve /** tgcurve */ 
                );
                /** Whether display position symbol of the ship tic 
                 <br>  Created in NX1899.0.0.  <br>  
                 <br> License requirements : nx_ship_gen_arrange ("Ship General Arrangement") OR nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") OR nx_ship_mfg_prep ("Ship Manufacturing") */
                public: void DisplayShipTicPositionSymbol
                (
                    bool bShow /** bshow */ ,
                    NXOpen::DisplayableObject * tgShipTic /** Ship Tic*/
                );
                /** Whether display thickness symbol of the ship tic 
                 <br>  Created in NX1899.0.0.  <br>  
                 <br> License requirements : nx_ship_gen_arrange ("Ship General Arrangement") OR nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") OR nx_ship_mfg_prep ("Ship Manufacturing") */
                public: void DisplayShipTicThicknessSymbol
                (
                    bool bShow /** bshow */ ,
                    NXOpen::DisplayableObject * tgShipTic /** Ship Tic*/
                );
                /** Update manufacturing view state
                 <br>  Created in NX1899.0.0.  <br>  
                 <br> License requirements : nx_ship_gen_arrange ("Ship General Arrangement") OR nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") OR nx_ship_mfg_prep ("Ship Manufacturing") */
                public: void UpdateMFGViewState
                (
                    NXOpen::Drawings::DraftingView * tgView /** tgview */ 
                );
                /** Add annotation of collar plate 
                 <br>  Created in NX1892.0.0.  <br>  
                 <br> License requirements : nx_ship_gen_arrange ("Ship General Arrangement") OR nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") OR nx_ship_mfg_prep ("Ship Manufacturing") */
                public: void AddAnnotationOfCollarPlate
                (
                    bool createCollarPlateSymbol /** createcollarplatesymbol */ ,
                    NXOpen::Drawings::DraftingBody * draftingbody /** draftingbody */ 
                );
            };
        }
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