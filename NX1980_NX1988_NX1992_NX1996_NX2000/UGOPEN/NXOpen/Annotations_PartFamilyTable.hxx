#ifndef NXOpen_ANNOTATIONS_PARTFAMILYTABLE_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_PARTFAMILYTABLE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_PartFamilyTable.ja
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
#include <NXOpen/Annotations_Table.hxx>
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
        class PartFamilyTable;
    }
    namespace Annotations
    {
        class Table;
    }
    class DisplayableObject;
    namespace Annotations
    {
        class _PartFamilyTableBuilder;
        class PartFamilyTableImpl;
        /**
            Represents a @link NXOpen::Annotations::PartFamilyTable NXOpen::Annotations::PartFamilyTable@endlink .
            This class represents a part family table.
             <br> To create or edit an instance of this class, use @link NXOpen::Annotations::PartFamilyTableBuilder  NXOpen::Annotations::PartFamilyTableBuilder @endlink  <br> 
         <br>  Created in NX1980.0.0.  <br>  
        */
        class NXOPENCPP_ANNOTATIONSEXPORT  PartFamilyTable : public NXOpen::Annotations::Table
        {
            private: PartFamilyTableImpl * m_partfamilytable_impl;
            private: friend class  _PartFamilyTableBuilder;
            protected: PartFamilyTable();
            public: ~PartFamilyTable();
            /** Update part family table 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: void Update
            (
            );
            /** Hide part family table column 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: void HideColumns
            (
                const std::vector<NXOpen::DisplayableObject *> & columns /** The columns to hide. */
            );
            /** Hide part family table row 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: void HideRows
            (
                const std::vector<NXOpen::DisplayableObject *> & rows /** The rows to hide. */
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
