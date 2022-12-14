#ifndef NXOpen_DIAGRAMMING_DEFINETITLEBLOCKBUILDER_HXX_INCLUDED
#define NXOpen_DIAGRAMMING_DEFINETITLEBLOCKBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Diagramming_DefineTitleBlockBuilder.ja
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
#include <NXOpen/Diagramming_DefineTitleBlockBuilder.hxx>
#include <NXOpen/Diagramming_Tables_Table.hxx>
#include <NXOpen/Diagramming_TitleBlockCellBuilder.hxx>
#include <NXOpen/Builder.hxx>
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
        class DefineTitleBlockBuilder;
    }
    class Builder;
    namespace Diagramming
    {
        namespace Tables
        {
            class Table;
        }
    }
    namespace Diagramming
    {
        class TitleBlockCellBuilder;
    }
    namespace Diagramming
    {
        class _DefineTitleBlockBuilderBuilder;
        class DefineTitleBlockBuilderImpl;
        /** Represents a @link NXOpen::Diagramming::DefineTitleBlockBuilder NXOpen::Diagramming::DefineTitleBlockBuilder@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::Diagramming::TitleBlockCollection::CreateDefineTitleBlockBuilder  NXOpen::Diagramming::TitleBlockCollection::CreateDefineTitleBlockBuilder @endlink  <br> 
         <br>  Created in NX11.0.1.  <br>  
        */
        class NXOPENCPP_DIAGRAMMINGEXPORT  DefineTitleBlockBuilder : public NXOpen::Builder
        {
            private: DefineTitleBlockBuilderImpl * m_definetitleblockbuilder_impl;
            private: friend class  _DefineTitleBlockBuilderBuilder;
            protected: DefineTitleBlockBuilder();
            public: ~DefineTitleBlockBuilder();
            /** Get tables. 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : None */
            public: void GetTables
            (
                std::vector<NXOpen::Diagramming::Tables::Table *> & tables /** tables */ 
            );
            /** Set tables. 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : None */
            public: void SetTables
            (
                const std::vector<NXOpen::Diagramming::Tables::Table *> & tables /** tables */ 
            );
            /** Get the cell builder.  @return  
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : None */
            public: NXOpen::Diagramming::TitleBlockCellBuilder * GetCell
            (
                NXOpen::Diagramming::Tables::Table * table /** table */ ,
                int rowIndex /** rowindex */ ,
                int columnIndex /** columnindex */ 
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
