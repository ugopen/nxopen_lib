#ifndef NXOpen_TDP_TEMPLATEAUTOMATICTABLEBUILDER_HXX_INCLUDED
#define NXOpen_TDP_TEMPLATEAUTOMATICTABLEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     TDP_TemplateAutomaticTableBuilder.ja
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
#include <NXOpen/TDP_TemplateBaseRectangleBuilder.hxx>
#include <NXOpen/TDP_TemplateAutomaticTablePMIFilterBuilder.hxx>
#include <NXOpen/TextColorFontWidthBuilder.hxx>
#include <NXOpen/libtdpopencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace TDP
    {
        class TemplateAutomaticTableBuilder;
    }
    class LineColorFontWidthBuilder;
    namespace TDP
    {
        class TemplateAutomaticTablePMIFilterBuilder;
    }
    namespace TDP
    {
        class TemplateBaseRectangleBuilder;
    }
    class TextColorFontWidthBuilder;
    namespace TDP
    {
        class _TemplateAutomaticTableBuilderBuilder;
        class TemplateAutomaticTableBuilderImpl;
        /** Represents a Template Automatic Table Builder  <br> To create a new instance of this class, use @link NXOpen::TDP::Manager::CreateTemplateAutomaticTableBuilder  NXOpen::TDP::Manager::CreateTemplateAutomaticTableBuilder @endlink  <br> 
         <br>  Created in NX1847.0.0.  <br>  
        */
        class TDPOPENCPPEXPORT  TemplateAutomaticTableBuilder : public NXOpen::TDP::TemplateBaseRectangleBuilder
        {
            /** represents the automatic table contents */
            public: enum ContentType
            {
                ContentTypeBom/** Bill Of Materials Table */,
                ContentTypePmi/** PMI Table */,
                ContentTypeView/** view */ ,
                ContentTypeIcd/** ICD Table */,
                ContentTypePad/** PAD Table */,
                ContentTypeKpi/** KPI Table */
            };

            /** represents BOM column types for automatic table editor */
            public: enum JaTdpTemplateAutomaticTableBomColumnType
            {
                JaTdpTemplateAutomaticTableBomColumnTypeIndex/** index */ ,
                JaTdpTemplateAutomaticTableBomColumnTypePartName/** part name */ ,
                JaTdpTemplateAutomaticTableBomColumnTypeQuantity/** quantity */ ,
                JaTdpTemplateAutomaticTableBomColumnTypeAttribute/** attribute */ 
            };

            /** represents PMI column types for automatic table editor */
            public: enum JaTdpTemplateAutomaticTablePmiColumnType
            {
                JaTdpTemplateAutomaticTablePmiColumnTypeIndex/** index */ ,
                JaTdpTemplateAutomaticTablePmiColumnTypePmiName/** pmi name */ ,
                JaTdpTemplateAutomaticTablePmiColumnTypeValue/** value */ ,
                JaTdpTemplateAutomaticTablePmiColumnTypeAttribute/** attribute */ ,
                JaTdpTemplateAutomaticTablePmiColumnTypePmiType/** pmi type */ ,
                JaTdpTemplateAutomaticTablePmiColumnTypePmiId/** pmi id */ 
            };

            /** represents PAD column types for automatic table editor */
            public: enum JaTdpTemplateAutomaticTablePadColumnType
            {
                JaTdpTemplateAutomaticTablePadColumnTypeIndex/** index */ ,
                JaTdpTemplateAutomaticTablePadColumnTypeComponents/** components */ ,
                JaTdpTemplateAutomaticTablePadColumnTypeAssemblyConstraints/** assembly constraints */ ,
                JaTdpTemplateAutomaticTablePadColumnTypeElectricalRouting/** electrical routing */ ,
                JaTdpTemplateAutomaticTablePadColumnTypeInterPartExpressions/** inter part expressions */ ,
                JaTdpTemplateAutomaticTablePadColumnTypeInterPartMeasurements/** inter part measurements */ ,
                JaTdpTemplateAutomaticTablePadColumnTypeJoin/** join */ ,
                JaTdpTemplateAutomaticTablePadColumnTypeMechanicalRouting/** mechanical routing */ ,
                JaTdpTemplateAutomaticTablePadColumnTypeWaveLinks/** wave links */ ,
                JaTdpTemplateAutomaticTablePadColumnTypeWelds/** welds */ ,
                JaTdpTemplateAutomaticTablePadColumnTypeAttribute/** attribute */ 
            };

            /** represents ICD column types for automatic table editor */
            public: enum JaTdpTemplateAutomaticTableIcdColumnType
            {
                JaTdpTemplateAutomaticTableIcdColumnTypeIndex/** index */ ,
                JaTdpTemplateAutomaticTableIcdColumnTypeComponents/** components */ ,
                JaTdpTemplateAutomaticTableIcdColumnTypeAssemblyConstraints/** assembly constraints */ ,
                JaTdpTemplateAutomaticTableIcdColumnTypeElectricalRouting/** electrical routing */ ,
                JaTdpTemplateAutomaticTableIcdColumnTypeInterPartExpressions/** inter part expressions */ ,
                JaTdpTemplateAutomaticTableIcdColumnTypeInterPartMeasurements/** inter part measurements */ ,
                JaTdpTemplateAutomaticTableIcdColumnTypeJoin/** join */ ,
                JaTdpTemplateAutomaticTableIcdColumnTypeMechanicalRouting/** mechanical routing */ ,
                JaTdpTemplateAutomaticTableIcdColumnTypeWaveLinks/** wave links */ ,
                JaTdpTemplateAutomaticTableIcdColumnTypeWelds/** welds */ ,
                JaTdpTemplateAutomaticTableIcdColumnTypeAttribute/** attribute */ 
            };

            /** represents KPI column types for automatic table editor */
            public: enum JaTdpTemplateAutomaticTableKpiColumnType
            {
                JaTdpTemplateAutomaticTableKpiColumnTypeName/** name */ ,
                JaTdpTemplateAutomaticTableKpiColumnTypeValue/** value */ ,
                JaTdpTemplateAutomaticTableKpiColumnTypeFormula/** formula */ ,
                JaTdpTemplateAutomaticTableKpiColumnTypeType/** type */ ,
                JaTdpTemplateAutomaticTableKpiColumnTypeDescription/** description */ ,
                JaTdpTemplateAutomaticTableKpiColumnTypeSource/** source */ ,
                JaTdpTemplateAutomaticTableKpiColumnTypeSourceDetails/** source details */ ,
                JaTdpTemplateAutomaticTableKpiColumnTypeResult/** result */ ,
                JaTdpTemplateAutomaticTableKpiColumnTypeValueType/** value type */ ,
                JaTdpTemplateAutomaticTableKpiColumnTypePartName/** part name */ ,
                JaTdpTemplateAutomaticTableKpiColumnTypeAttribute/** attribute */ 
            };

            /** represents the position in 3D PDF */
            public: enum PositionType
            {
                PositionTypeNone/** Not placed in 3D PDF */,
                PositionTypeAbove/** Placed above the PMI table in 3D PDF */,
                PositionTypeBelow/** Placed below the PMI table in 3D PDF */
            };

            /** represents the BOM Scope level in 3D PDF */
            public: enum ScopeType
            {
                ScopeTypeAllLevels/** Assemblies and Sub Assemblies placed in 3D PDF */,
                ScopeTypeTopLevelOnly/** Placed Top Level Assembly in 3D PDF */,
                ScopeTypeComponentsOnly/** Placed Leaf level component in 3D PDF */
            };

            /** represents the Kpi Filter level in 3D PDF */
            public: enum KpiFilterLevel
            {
                KpiFilterLevelPart/** part */ ,
                KpiFilterLevelProductInterface/** product interface */ ,
                KpiFilterLevelExpression/** expression */ ,
                KpiFilterLevelCheck/** check */ ,
                KpiFilterLevelPartOccurence/** part occurence */ ,
                KpiFilterLevelCombinedView/** combined view */ 
            };

            private: TemplateAutomaticTableBuilderImpl * m_templateautomatictablebuilder_impl;
            private: friend class  _TemplateAutomaticTableBuilderBuilder;
            protected: TemplateAutomaticTableBuilder();
            public: ~TemplateAutomaticTableBuilder();
            /**Returns  the content 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::TDP::TemplateAutomaticTableBuilder::ContentType Contents
            (
            );
            /**Sets  the content 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: void SetContents
            (
                NXOpen::TDP::TemplateAutomaticTableBuilder::ContentType content /** content */ 
            );
            /**Returns  the show border toggle 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: bool ShowBorder
            (
            );
            /**Sets  the show border toggle 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: void SetShowBorder
            (
                bool showBorder /** showborder */ 
            );
            /**Returns  the color and width 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::LineColorFontWidthBuilder * ColorWidth
            (
            );
            /** To swap the columns in the table
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: bool SwapColumns
            (
                int index1 /** location of the first item */,
                int index2 /** location of the second item */,
                int length /** number of rows selected for swapping */
            );
            /** To add the row in the table
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: bool AddColumn
            (
            );
            /** To delete the row in the table
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: bool DeleteColumn
            (
                int index /** index of the column to be deleted */
            );
            /** To modify the Bom column type in the table
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: bool UpdateBomColumn
            (
                int rowIndex /** index of the column to be updated */,
                NXOpen::TDP::TemplateAutomaticTableBuilder::JaTdpTemplateAutomaticTableBomColumnType colType /** column type to be updated */
            );
            /** To modify the Pmi column type in the table
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: bool UpdatePmiColumn
            (
                int rowIndex /** index of the column to be updated */,
                NXOpen::TDP::TemplateAutomaticTableBuilder::JaTdpTemplateAutomaticTablePmiColumnType colType /** column type to be updated */
            );
            /** To modify the header column in table
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: bool UpdateHeader
            (
                int rowIndex /** index of the column to be updated */,
                const NXString & value /** Value to be updated */
            );
            /** To modify the header column in table
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            bool UpdateHeader
            (
                int rowIndex /** index of the column to be updated */,
                const char * value /** Value to be updated */
            );
            /** To modify the Attribute name in the table
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: bool UpdateAttribute
            (
                int rowIndex /** index of the column to be updated */,
                const NXString & value /** Value to be updated */
            );
            /** To modify the Attribute name in the table
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            bool UpdateAttribute
            (
                int rowIndex /** index of the column to be updated */,
                const char * value /** Value to be updated */
            );
            /** To modify the Width value in the table
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: bool UpdateWidth
            (
                int rowIndex /** index of the column to be updated */,
                double value /** Value to be updated */
            );
            /**Returns  the pmi Filter position 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::TDP::TemplateAutomaticTableBuilder::PositionType PmiFilterPos
            (
            );
            /**Sets  the pmi Filter position 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: void SetPmiFilterPos
            (
                NXOpen::TDP::TemplateAutomaticTableBuilder::PositionType position /** position */ 
            );
            /**Returns  the Zoom To PMI position 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::TDP::TemplateAutomaticTableBuilder::PositionType ZoomToPmiPos
            (
            );
            /**Sets  the Zoom To PMI position 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: void SetZoomToPmiPos
            (
                NXOpen::TDP::TemplateAutomaticTableBuilder::PositionType position /** position */ 
            );
            /**Returns  the bom scope type 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::TDP::TemplateAutomaticTableBuilder::ScopeType BomScope
            (
            );
            /**Sets  the bom scope type 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: void SetBomScope
            (
                NXOpen::TDP::TemplateAutomaticTableBuilder::ScopeType scope /** scope */ 
            );
            /**Returns  the PMI Filter 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::TDP::TemplateAutomaticTablePMIFilterBuilder * PmiFilter
            (
            );
            /**Returns  the font, and width of Automatic table text 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::TextColorFontWidthBuilder * TextCfw
            (
            );
            /**Returns  the maintain bom assembly order toggle 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: bool MaintainBomAssemOrder
            (
            );
            /**Sets  the maintain bom assembly order toggle 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: void SetMaintainBomAssemOrder
            (
                bool maintainBomAssemOrder /** maintainbomassemorder */ 
            );
            /** To modify the PAD column type in the table
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: bool SetPADColumnType
            (
                int rowIndex /** index of the column to be updated */,
                NXOpen::TDP::TemplateAutomaticTableBuilder::JaTdpTemplateAutomaticTablePadColumnType colType /** column type to be updated */
            );
            /** To modify the ICD column type in the table
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: bool SetICDColumnType
            (
                int rowIndex /** index of the column to be updated */,
                NXOpen::TDP::TemplateAutomaticTableBuilder::JaTdpTemplateAutomaticTableIcdColumnType colType /** column type to be updated */
            );
            /** To modify the KPI column type in the table
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: bool SetKPIColumnType
            (
                int rowIndex /** index of the column to be updated */,
                NXOpen::TDP::TemplateAutomaticTableBuilder::JaTdpTemplateAutomaticTableKpiColumnType colType /** column type to be updated */
            );
            /**Returns  the filter level type 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::TDP::TemplateAutomaticTableBuilder::KpiFilterLevel FilterLevel
            (
            );
            /**Sets  the filter level type 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: void SetFilterLevel
            (
                NXOpen::TDP::TemplateAutomaticTableBuilder::KpiFilterLevel filterLevel /** filterlevel */ 
            );
            /**Returns  the show passed result toggle 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: bool ShowPassed
            (
            );
            /**Sets  the show passed result toggle 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: void SetShowPassed
            (
                bool showPassed /** showpassed */ 
            );
            /**Returns  the show passed with information result toggle 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: bool ShowPassedWithInfo
            (
            );
            /**Sets  the show passed with information result toggle 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: void SetShowPassedWithInfo
            (
                bool showPassedWithInfo /** showpassedwithinfo */ 
            );
            /**Returns  the show passed with warning result toggle 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: bool ShowPassedWithWarning
            (
            );
            /**Sets  the show passed with warning result toggle 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: void SetShowPassedWithWarning
            (
                bool showPassedWithWarning /** showpassedwithwarning */ 
            );
            /**Returns  the show failed result toggle 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: bool ShowFailed
            (
            );
            /**Sets  the show failed result toggle 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: void SetShowFailed
            (
                bool showFailed /** showfailed */ 
            );
            /**Returns  the show suppressed result toggle 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: bool ShowSuppressed
            (
            );
            /**Sets  the show suppressed result toggle 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: void SetShowSuppressed
            (
                bool showSuppressed /** showsuppressed */ 
            );
            /**Returns  the show work part only result toggle 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: bool ShowWorkPartOnly
            (
            );
            /**Sets  the show work part only result toggle 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: void SetShowWorkPartOnly
            (
                bool showWorkPartOnly /** showworkpartonly */ 
            );
            /**Returns  the show physical parameters result toggle 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: bool ShowPhysicalParameter
            (
            );
            /**Sets  the show physical parameters result toggle 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: void SetShowPhysicalParameter
            (
                bool showPhysicalParameters /** showphysicalparameters */ 
            );
            /**Returns  the show unused expression check folder result toggle 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: bool ShowUnusedExpCheckFolder
            (
            );
            /**Sets  the show unused expression check folder result toggle 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: void SetShowUnusedExpCheckFolder
            (
                bool showUnusedExpCheckFolder /** showunusedexpcheckfolder */ 
            );
            /**Returns  the show unvalidated requirements folder result toggle 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: bool ShowUnvalidatedReqFolder
            (
            );
            /**Sets  the show unvalidated requirements folder result toggle 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: void SetShowUnvalidatedReqFolder
            (
                bool showUnvalidatedReqFolder /** showunvalidatedreqfolder */ 
            );
            /**Returns  the show physical parameters folder result toggle 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: bool ShowPhysicalParametersFolder
            (
            );
            /**Sets  the show physical parameters folder result toggle 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: void SetShowPhysicalParametersFolder
            (
                bool showPhysicalParametersFolder /** showphysicalparametersfolder */ 
            );
            /**Returns  the show checked only result toggle 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: bool ShowCheckedOnly
            (
            );
            /**Sets  the show checked only result toggle 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: void SetShowCheckedOnly
            (
                bool showCheckedOnly /** showcheckedonly */ 
            );
            /**Returns  the show product interface toggle 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: bool ShowProductInterfaces
            (
            );
            /**Sets  the show product interface toggle 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: void SetShowProductInterfaces
            (
                bool showProductInterfaces /** showproductinterfaces */ 
            );
            /**Returns  the show unused check expression toggle 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: bool ShowUnusedCheckedExps
            (
            );
            /**Sets  the show unused check expression toggle 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: void SetShowUnusedCheckedExps
            (
                bool showUnusedCheckedExps /** showunusedcheckedexps */ 
            );
            /**Returns  the show unvalidated requirements toggle 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: bool ShowUnvalidatedReqs
            (
            );
            /**Sets  the show unvalidated requirements toggle 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: void SetShowUnvalidatedReqs
            (
                bool showUnvalidatedReqs /** showunvalidatedreqs */ 
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
