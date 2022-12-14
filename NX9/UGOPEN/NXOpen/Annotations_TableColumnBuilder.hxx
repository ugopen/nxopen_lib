#ifndef NXOpen_ANNOTATIONS_TABLECOLUMNBUILDER_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_TABLECOLUMNBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_TableColumnBuilder.ja
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
#include <NXOpen/Annotations_TableColumnBuilder.hxx>
#include <NXOpen/GeometricUtilities_IComponentBuilder.hxx>
#include <NXOpen/SelectObject.hxx>
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
        class TableColumnBuilder;
    }
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    class SelectDisplayableObject;
    namespace Annotations
    {
        class _TableColumnBuilderBuilder;
        class TableColumnBuilderImpl;
        /** 
             Represents a @link Annotations::TableColumnBuilder Annotations::TableColumnBuilder@endlink .
             This class queries and sets settings specific to parts list  column when creating or
             editing parts list settings.
            
         <br>  Created in NX9.0.0.  <br>  
        */
        class NXOPENCPP_ANNOTATIONSEXPORT  TableColumnBuilder : public TaggedObject, public virtual GeometricUtilities::IComponentBuilder
        {
            /**The options specify the type of column.*/
            public: enum CategoryType
            {
                CategoryTypeGeneral/** general */ ,
                CategoryTypeCallout/** callout */ ,
                CategoryTypeQuantity/** quantity */ 
            };

            /**The options determine whether to apply settings to all cells or only to cells of new rows.*/
            public: enum ScopeType
            {
                ScopeTypeCellsinNewRows/** cellsin new rows */ ,
                ScopeTypeAllCellsinColumn/** all cellsin column */ 
            };

            private: TableColumnBuilderImpl * m_tablecolumnbuilder_impl;
            private: friend class  _TableColumnBuilderBuilder;
            protected: TableColumnBuilder();
            public: ~TableColumnBuilder();
            /**Returns  the category specifies the type of column. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::TableColumnBuilder::CategoryType Category
            (
            );
            /**Sets  the category specifies the type of column. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetCategory
            (
                NXOpen::Annotations::TableColumnBuilder::CategoryType category /** category */ 
            );
            /**Returns  the attribute name specifies the attribute name for cells in column. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXString AttributeName
            (
            );
            /**Sets  the attribute name specifies the attribute name for cells in column. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetAttributeName
            (
                const NXString & attributeName /** attributename */ 
            );
            /**Sets  the attribute name specifies the attribute name for cells in column. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            void SetAttributeName
            (
                const char * attributeName /** attributename */ 
            );
            /**Returns  the default text specifies the default text set for the column cells. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXString DefaultText
            (
            );
            /**Sets  the default text specifies the default text set for the column cells. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetDefaultText
            (
                const NXString & defaultText /** defaulttext */ 
            );
            /**Sets  the default text specifies the default text set for the column cells. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            void SetDefaultText
            (
                const char * defaultText /** defaulttext */ 
            );
            /**Returns  the include nested assy specified the nested assy setting. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: bool IncludeNestedAssemblies
            (
            );
            /**Sets  the include nested assy specified the nested assy setting. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetIncludeNestedAssemblies
            (
                bool includeNestedAssemblies /** includenestedassemblies */ 
            );
            /**Returns  the select parent component. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectDisplayableObject * SelectParentComponent
            (
            );
            /**Returns  the scope enum specifies whether settings are to be applied to all 
                    cells of column or only cells of new rows in column. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::TableColumnBuilder::ScopeType Scope
            (
            );
            /**Sets  the scope enum specifies whether settings are to be applied to all 
                    cells of column or only cells of new rows in column. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetScope
            (
                NXOpen::Annotations::TableColumnBuilder::ScopeType scope /** scope */ 
            );
            /**Returns  the key field specifies whether column is key column. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: bool KeyField
            (
            );
            /**Sets  the key field specifies whether column is key column. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetKeyField
            (
                bool keyField /** keyfield */ 
            );
            /**Returns  the protect cells specifies whether cells of column are protected. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: bool ProtectCells
            (
            );
            /**Sets  the protect cells specifies whether cells of column are protected. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetProtectCells
            (
                bool protectCells /** protectcells */ 
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
