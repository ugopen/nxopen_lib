#ifndef NXOpen_TOOLING_BOMLISTBUILDER_HXX_INCLUDED
#define NXOpen_TOOLING_BOMLISTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Tooling_BomListBuilder.ja
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
#include <NXOpen/Builder.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/Tooling_BomListDataProvider.hxx>
#include <NXOpen/ugmath.hxx>
#include <NXOpen/libnxopencpp_tooling_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Tooling
    {
        class BomListBuilder;
    }
    namespace Assemblies
    {
        class Component;
    }
    namespace Assemblies
    {
        class SelectComponentList;
    }
    class Builder;
    class DisplayableObject;
    namespace Tooling
    {
        class BomListDataProvider;
    }
    namespace Tooling
    {
        class _BomListBuilderBuilder;
        class BomListBuilderImpl;
        /** 
            Represents a @link NXOpen::Tooling::BomListBuilder NXOpen::Tooling::BomListBuilder@endlink  builder.
             <br> To create a new instance of this class, use @link NXOpen::Tooling::MoldwizardManager::CreateBomListBuilder  NXOpen::Tooling::MoldwizardManager::CreateBomListBuilder @endlink  <br> 
        Default values.
        <list type="table"> 
         
        <listheader><term> 
        Property</term>  <description> 
        Value</description> </listheader>
        <item><term> 
         
        BomListType </term> <description> 
         
        BomList </description> </item> 

        </list> 

         <br>  Created in NX10.0.0.  <br>  
        */
        class NXOPENCPP_TOOLINGEXPORT  BomListBuilder : public NXOpen::Builder
        {
            /** Represents an index to components list type. */
            public: enum BomListTypes
            {
                BomListTypesBomList/** A list includes components in BOM */,
                BomListTypesHideList/** A list includes hidden components */
            };

            /** Represents an enumeration indicating whether the sorting needs to be performed in ascending or descending order. */
            public: enum BomListSortOption
            {
                BomListSortOptionUnsorted/** Unsorted */,
                BomListSortOptionAscending/** Ascending */,
                BomListSortOptionDescending/** Descending */
            };

            /** Represents the format for decimal delimiter. */
            public: enum BomListDecimalDelimiter
            {
                BomListDecimalDelimiterDot/** Dot as the decimal delimiter */,
                BomListDecimalDelimiterComma/** Comma as the decimal delimiter */
            };

            private: BomListBuilderImpl * m_bomlistbuilder_impl;
            private: friend class  _BomListBuilderBuilder;
            protected: BomListBuilder();
            public: ~BomListBuilder();
            /**Returns  the template file of bom
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXString BomTemplate
            (
            );
            /**Sets  the template file of bom
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR nx_electrode_wizard ("NX Electrode Wizard") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetBomTemplate
            (
                const NXString & bomTemplate /** bomtemplate */ 
            );
            /**Sets  the template file of bom
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR nx_electrode_wizard ("NX Electrode Wizard") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            void SetBomTemplate
            (
                const char * bomTemplate /** bomtemplate */ 
            );
            /**Returns  the sorting method of bom - sort exported and non-exported separately
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: bool SortingMethod
            (
            );
            /**Sets  the sorting method of bom - sort exported and non-exported separately
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR nx_electrode_wizard ("NX Electrode Wizard") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetSortingMethod
            (
                bool isSeparate /** isseparate */ 
            );
            /**Returns  the sorting method of bom - sort modified and unmodified separately
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: bool SortingBasedOnModify
            (
            );
            /**Sets  the sorting method of bom - sort modified and unmodified separately
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR nx_electrode_wizard ("NX Electrode Wizard") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetSortingBasedOnModify
            (
                bool isSeparate /** isseparate */ 
            );
            /**Returns  the select component needed to get stocksize
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Assemblies::SelectComponentList * SelectComponents
            (
            );
            /**Returns  the tree list shows which kind of components should be included in 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Tooling::BomListBuilder::BomListTypes BomListType
            (
            );
            /**Sets  the tree list shows which kind of components should be included in 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR nx_electrode_wizard ("NX Electrode Wizard") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetBomListType
            (
                NXOpen::Tooling::BomListBuilder::BomListTypes bomListType /** bomlisttype */ 
            );
            /** Gets the last used template name
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: NXString GetLastTemplateName
            (
            );
            /** Sets the last used template name
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR nx_electrode_wizard ("NX Electrode Wizard") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetLastTemplateName
            (
                const NXString & lastTemplateName /** lasttemplatename */ 
            );
            /** Sets the last used template name
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR nx_electrode_wizard ("NX Electrode Wizard") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            void SetLastTemplateName
            (
                const char * lastTemplateName /** lasttemplatename */ 
            );
            /**Returns  the data provider of BOM 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Tooling::BomListDataProvider * BomListDataProvider
            (
            );
            /** Updates the blank attributes of electrodes in Electrode Design Application. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR nx_electrode_wizard ("NX Electrode Wizard") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void UpdateEwBlankAttributes
            (
            );
            /** Parses the current BOM template. Use this function to populate data in data provider of BOM. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR nx_electrode_wizard ("NX Electrode Wizard") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void ParseBomTemplate
            (
            );
            /** Populates BOM list data according to current template. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR nx_electrode_wizard ("NX Electrode Wizard") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void PopulateBomListData
            (
            );
            /** Adds a new record into BOM list. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR nx_electrode_wizard ("NX Electrode Wizard") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void AddBomData
            (
                const std::vector<NXOpen::Assemblies::Component *> & partOccs /** The part occurrences to add into BOM. Sets NULL to add the current display part into BOM list.*/,
                std::vector<NXString> & dataStrings /** The BOM data. */
            );
            /** Shows the corresponding components of given row in the BOM List so that the components can be exported to spreadsheet. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR nx_electrode_wizard ("NX Electrode Wizard") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void ShowComponents
            (
                int rowID /** rowid */ ,
                const std::vector<NXOpen::Assemblies::Component *> & partOccs /** The part occurrences to be shown in BOM List. Sets NULL show all part occurrences in given row in BOM List. */
            );
            /** Shows the given rows in the BOM List so that all the components of the rows can be exported to spreadsheet.
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR nx_electrode_wizard ("NX Electrode Wizard") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void ShowRows
            (
                const std::vector<int> & rowIDs /** rowids */ 
            );
            /** Ignores the corresponding components of given row in the Hide List so that the components can not be exported to spreadsheet.
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR nx_electrode_wizard ("NX Electrode Wizard") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void IgnoreComponents
            (
                int rowID /** rowid */ ,
                const std::vector<NXOpen::Assemblies::Component *> & partOccs /** The part occurrences to be ignored in Hide List. Sets NULL to ignore all part occurrences in given row in Hide List. */
            );
            /** Ignores the given rows in the Hide List so that all the components of the rows can not be exported to spreadsheet.
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR nx_electrode_wizard ("NX Electrode Wizard") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void IgnoreRows
            (
                const std::vector<int> & rowIDs /** rowids */ 
            );
            /** Sorts the given column. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR nx_electrode_wizard ("NX Electrode Wizard") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SortColumn
            (
                int columnID /** columnid */ ,
                NXOpen::Tooling::BomListBuilder::BomListSortOption order /** order */ 
            );
            /** Creates parts list for the assembly.  @return  The created parts list. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR nx_electrode_wizard ("NX Electrode Wizard") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: NXOpen::DisplayableObject * CreatePartsList
            (
                const std::vector<int> & columnWidths /** The widths of each column. */,
                const NXOpen::Point3d & point /** The position of parts list. */
            );
            /** Gets the column label.  @return  Column Label 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: NXString GetColumnLabel
            (
                int columnID /** Column index */
            );
            /** Gets the corresponding attribute name of given column.  @return  Column attribute 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: NXString GetColumnAttribute
            (
                int columnID /** Column index */
            );
            /** Gets the corresponding part occurrences of given row.  @return  The corresponding part occurrences of given row. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXOpen::Assemblies::Component *> GetPartOccs
            (
                int rowID /** rowid */ 
            );
            /** Gets all the row numbers in the given List @return  All row numbers in the given list 
             <br>  @deprecated Deprecated in NX11.0.0.  Use @link Tooling::BomListDataProvider::RowCount Tooling::BomListDataProvider::RowCount@endlink  instead. <br>  

             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX11.0.0.  Use Tooling::BomListDataProvider::RowCount instead.") std::vector<int> GetRows
            (
                NXOpen::Tooling::BomListBuilder::BomListTypes bomListType /** bomlisttype */ 
            );
            /** Gets all the attributes listed in the current template @return  Attribute strings. 
             <br>  @deprecated Deprecated in NX11.0.0.  Use @link Tooling::BomListBuilder::GetColumnAttribute Tooling::BomListBuilder::GetColumnAttribute@endlink  instead. <br>  

             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX11.0.0.  Use Tooling::BomListBuilder::GetColumnAttribute instead.") std::vector<NXString> GetAttributeStrings
            (
            );
            /** Gets column number of given attribute
             <br>  @deprecated Deprecated in NX11.0.0.  Use @link Tooling::BomListBuilder::GetColumnAttribute Tooling::BomListBuilder::GetColumnAttribute@endlink  instead. <br>  

             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX11.0.0.  Use Tooling::BomListBuilder::GetColumnAttribute instead.") void GetColumn
            (
                const NXString & attrString /** attrstring */ 
            );
            /** Gets column number of given attribute
             <br>  @deprecated Deprecated in NX11.0.0.  Use @link Tooling::BomListBuilder::GetColumnAttribute Tooling::BomListBuilder::GetColumnAttribute@endlink  instead. <br>  

             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            void GetColumn
            (
                const char * attrString /** attrstring */ 
            );
            /** Modifies BOM data
             <br>  @deprecated Deprecated in NX11.0.0.  Use @link Tooling::BomListDataProvider::SetString Tooling::BomListDataProvider::SetString@endlink  instead. <br>  

             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX11.0.0.  Use Tooling::BomListDataProvider::SetString instead.") void ModifyBomData
            (
                int rowNumber /** rownumber */ ,
                int columnNumber /** columnnumber */ ,
                const NXString & userString /** userstring */ 
            );
            /** Modifies BOM data
             <br>  @deprecated Deprecated in NX11.0.0.  Use @link Tooling::BomListDataProvider::SetString Tooling::BomListDataProvider::SetString@endlink  instead. <br>  

             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            void ModifyBomData
            (
                int rowNumber /** rownumber */ ,
                int columnNumber /** columnnumber */ ,
                const char * userString /** userstring */ 
            );
            /** Stores bom list data.
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: void StoreBomListData
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
