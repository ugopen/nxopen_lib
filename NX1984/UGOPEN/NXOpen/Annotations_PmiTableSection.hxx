#ifndef NXOpen_ANNOTATIONS_PMITABLESECTION_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_PMITABLESECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_PmiTableSection.ja
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
#include <NXOpen/Annotations_TableSection.hxx>
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
        class PmiTableSection;
    }
    namespace Annotations
    {
        class TableSection;
    }
    namespace Annotations
    {
        class _PmiTableSectionBuilder;
        class PmiTableSectionImpl;
        /** Represents a PMI table section  <br> To create or edit an instance of this class, use @link NXOpen::Annotations::PmiTableBuilder  NXOpen::Annotations::PmiTableBuilder @endlink  <br> 
         <br>  Created in NX12.0.0.  <br>  
        */
        class NXOPENCPP_ANNOTATIONSEXPORT  PmiTableSection : public NXOpen::Annotations::TableSection
        {
            private: PmiTableSectionImpl * m_pmitablesection_impl;
            private: friend class  _PmiTableSectionBuilder;
            protected: PmiTableSection();
            public: ~PmiTableSection();
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