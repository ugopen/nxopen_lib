#ifndef NXOpen_DIAGRAMMING_TABLES_TABLE_HXX_INCLUDED
#define NXOpen_DIAGRAMMING_TABLES_TABLE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Diagramming_Tables_Table.ja
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
#include <NXOpen/Diagramming_TitleBlock.hxx>
#include <NXOpen/Diagramming_Annotation.hxx>
#include <NXOpen/libnxopencpp_diagramming_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Diagramming
    {
        namespace Tables
        {
            class Table;
        }
    }
    namespace Diagramming
    {
        class Annotation;
    }
    namespace Diagramming
    {
        class TitleBlock;
    }
    namespace Diagramming
    {
        namespace Tables
        {
            class _TableBuilder;
            class TableImpl;
            /** Represents the Table class.  <br> To create or edit an instance of this class, use @link NXOpen::Diagramming::Tables::TableBuilder  NXOpen::Diagramming::Tables::TableBuilder @endlink  <br> 
             <br>  Created in NX10.0.0.  <br>  
            */
            class NXOPENCPP_DIAGRAMMINGEXPORT  Table : public NXOpen::Diagramming::Annotation
            {
                private: TableImpl * m_table_impl;
                private: friend class  _TableBuilder;
                protected: Table();
                public: ~Table();
                /** Get the title block attached to the table. @return  
                 <br>  Created in NX11.0.1.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Diagramming::TitleBlock * GetTitleBlock
                (
                );
                /** Remove the title block attached to the table.
                 <br>  Created in NX11.0.1.  <br>  
                 <br> License requirements : None */
                public: void RemoveTitleBlock
                (
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