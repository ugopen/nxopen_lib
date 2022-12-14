#ifndef NXOpen_ANNOTATIONS_PMITABLEBUILDER_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_PMITABLEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_PmiTableBuilder.ja
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
#include <NXOpen/Annotations_AssociatedObjectsBuilder.hxx>
#include <NXOpen/Annotations_TableSectionBuilder.hxx>
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
        class PmiTableBuilder;
    }
    namespace Annotations
    {
        class AssociatedObjectsBuilder;
    }
    namespace Annotations
    {
        class TableSectionBuilder;
    }
    namespace Annotations
    {
        class _PmiTableBuilderBuilder;
        class PmiTableBuilderImpl;
        /** Represents a @link NXOpen::Annotations::PmiTableSection NXOpen::Annotations::PmiTableSection@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::Annotations::PmiTableSectionCollection::CreatePmiTableBuilder  NXOpen::Annotations::PmiTableSectionCollection::CreatePmiTableBuilder @endlink  <br> 
        Default values.
        <list type="table"> 
         
        <listheader><term> 
        Property</term>  <description> 
        Value</description> </listheader>
        <item><term> 
         
        ColumnWidth </term> <description> 
         
        50 (millimeters part), 2 (inches part) </description> </item> 

        <item><term> 
         
        NumberOfColumns </term> <description> 
         
        5 </description> </item> 

        <item><term> 
         
        NumberOfRows </term> <description> 
         
        5 </description> </item> 

        <item><term> 
         
        RowHeight </term> <description> 
         
        8 (millimeters part), 0.25 (inches part) </description> </item> 

        </list> 

         <br>  Created in NX12.0.0.  <br>  
        */
        class NXOPENCPP_ANNOTATIONSEXPORT  PmiTableBuilder : public NXOpen::Annotations::TableSectionBuilder
        {
            private: PmiTableBuilderImpl * m_pmitablebuilder_impl;
            private: friend class  _PmiTableBuilderBuilder;
            protected: PmiTableBuilder();
            public: ~PmiTableBuilder();
            /**Returns  the @link NXOpen::Annotations::AssociatedObjectsBuilder NXOpen::Annotations::AssociatedObjectsBuilder@endlink  for PMI Table  
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::AssociatedObjectsBuilder * AssociatedObjects
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
