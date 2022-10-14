#ifndef NXOpen_ANNOTATIONS_PMIPREFERENCESBUILDER_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_PMIPREFERENCESBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_PmiPreferencesBuilder.ja
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
#include <NXOpen/Annotations_CommonWorkflowBuilder.hxx>
#include <NXOpen/Annotations_DimensionWorkflowBuilder.hxx>
#include <NXOpen/Annotations_PmiGeneralSetupDisplayBuilder.hxx>
#include <NXOpen/Annotations_PmiGeneralSetupEffectivityBuilder.hxx>
#include <NXOpen/Annotations_PmiGeneralSetupGeneralBuilder.hxx>
#include <NXOpen/Annotations_PmiGeneralSetupParallelToScreenBuilder.hxx>
#include <NXOpen/Annotations_PmiSectionViewCuttingPlaneSymbolBuilder.hxx>
#include <NXOpen/Annotations_PmiSectionViewViewBuilder.hxx>
#include <NXOpen/Annotations_PmiSupplementalGeometryRegionBuilder.hxx>
#include <NXOpen/Annotations_RetainedAnnotationsBuilder.hxx>
#include <NXOpen/Annotations_StyleBuilder.hxx>
#include <NXOpen/Annotations_SymbolWorkflowBuilder.hxx>
#include <NXOpen/Annotations_TableCellStyleBuilder.hxx>
#include <NXOpen/Annotations_TableSectionStyleBuilder.hxx>
#include <NXOpen/Annotations_TabularNoteStyleBuilder.hxx>
#include <NXOpen/Builder.hxx>
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
        class PmiPreferencesBuilder;
    }
    namespace Annotations
    {
        class CommonWorkflowBuilder;
    }
    namespace Annotations
    {
        class DimensionWorkflowBuilder;
    }
    namespace Annotations
    {
        class PmiGeneralSetupDisplayBuilder;
    }
    namespace Annotations
    {
        class PmiGeneralSetupEffectivityBuilder;
    }
    namespace Annotations
    {
        class PmiGeneralSetupGeneralBuilder;
    }
    namespace Annotations
    {
        class PmiGeneralSetupParallelToScreenBuilder;
    }
    namespace Annotations
    {
        class PmiSectionViewCuttingPlaneSymbolBuilder;
    }
    namespace Annotations
    {
        class PmiSectionViewViewBuilder;
    }
    namespace Annotations
    {
        class PmiSupplementalGeometryRegionBuilder;
    }
    namespace Annotations
    {
        class RetainedAnnotationsBuilder;
    }
    namespace Annotations
    {
        class StyleBuilder;
    }
    namespace Annotations
    {
        class SymbolWorkflowBuilder;
    }
    namespace Annotations
    {
        class TableCellStyleBuilder;
    }
    namespace Annotations
    {
        class TableSectionStyleBuilder;
    }
    namespace Annotations
    {
        class TabularNoteStyleBuilder;
    }
    class Builder;
    class NXObject;
    namespace Annotations
    {
        class _PmiPreferencesBuilderBuilder;
        class PmiPreferencesBuilderImpl;
        /** Represents a NXOpen.Annotations.PmiPreferencesBuilder builder  <br> To create a new instance of this class, use @link NXOpen::Annotations::PmiSettingsManager::CreatePreferencesBuilder  NXOpen::Annotations::PmiSettingsManager::CreatePreferencesBuilder @endlink  <br> 
         <br>  Created in NX1847.0.0.  <br>  
        */
        class NXOPENCPP_ANNOTATIONSEXPORT  PmiPreferencesBuilder : public NXOpen::Builder
        {
            private: PmiPreferencesBuilderImpl * m_pmipreferencesbuilder_impl;
            private: friend class  _PmiPreferencesBuilderBuilder;
            protected: PmiPreferencesBuilder();
            public: ~PmiPreferencesBuilder();
            /**Returns  the annotation style builder 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::StyleBuilder * AnnotationStyle
            (
            );
            /**Returns  the table section style builder 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::TableSectionStyleBuilder * TableSection
            (
            );
            /**Returns  the symbol workflow builder 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::SymbolWorkflowBuilder * SymbolWorkflow
            (
            );
            /**Returns  the table cell style builder 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::TableCellStyleBuilder * TableCellStyle
            (
            );
            /**Returns  the tabular note style builder 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::TabularNoteStyleBuilder * TabularNoteStyle
            (
            );
            /**Returns  the general retained annotations builder 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::RetainedAnnotationsBuilder * RetainedAnnotations
            (
            );
            /**Returns  the common workflow builder 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::CommonWorkflowBuilder * CommonWorkflow
            (
            );
            /**Returns  the dimension workflow builder 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::DimensionWorkflowBuilder * DimensionWorkflow
            (
            );
            /**Returns  the general settings builder in pmi preferences 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::PmiGeneralSetupGeneralBuilder * PmiGeneralSetupGeneral
            (
            );
            /**Returns  the display settings builder in pmi preferences 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::PmiGeneralSetupDisplayBuilder * PmiGeneralSetupDisplay
            (
            );
            /**Returns  the parallel to screen settings builder in pmi preferences 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::PmiGeneralSetupParallelToScreenBuilder * PmiGeneralSetupParallelToScreen
            (
            );
            /**Returns  the effectivity settings builder in pmi preferences 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::PmiGeneralSetupEffectivityBuilder * PmiGeneralSetupEffectivity
            (
            );
            /**Returns  the region settings builder in pmi preferences 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::PmiSupplementalGeometryRegionBuilder * PmiSupplementalGeometryRegion
            (
            );
            /**Returns  the view settings builder in pmi preferences 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::PmiSectionViewViewBuilder * PmiSectionViewView
            (
            );
            /**Returns  the cutting plane symbol settings builder in pmi preferences 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::PmiSectionViewCuttingPlaneSymbolBuilder * PmiSectionViewCuttingPlaneSymbol
            (
            );
            /** Inherit Settings From Selected Object 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void InheritSettingsFromSelectedObject
            (
                NXOpen::NXObject * selectedObject /** The selected annotation or table instance object. NULL is not allowed. */
            );
            /** Inherit Settings From Customer Default 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void InheritSettingsFromCustomerDefault
            (
            );
            /** Inherit Settings From Preferences 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void InheritSettingsFromPreferences
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