#ifndef NXOpen_TDP_TEMPLATEAUTOMATICTABLE_HXX_INCLUDED
#define NXOpen_TDP_TEMPLATEAUTOMATICTABLE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     TDP_TemplateAutomaticTable.ja
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
#include <NXOpen/DisplayableObject.hxx>
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
        class TemplateAutomaticTable;
    }
    class DisplayableObject;
    namespace TDP
    {
        class _TemplateAutomaticTableBuilder;
        class TemplateAutomaticTableImpl;
        /**  Represents the @link NXOpen::TDP::TemplateAutomaticTable NXOpen::TDP::TemplateAutomaticTable@endlink  object.
             <br> To create or edit an instance of this class, use @link NXOpen::TDP::TemplateAutomaticTableBuilder  NXOpen::TDP::TemplateAutomaticTableBuilder @endlink  <br> 
         <br>  Created in NX1847.0.0.  <br>  
        */
        class TDPOPENCPPEXPORT  TemplateAutomaticTable : public NXOpen::DisplayableObject
        {
            private: TemplateAutomaticTableImpl * m_templateautomatictable_impl;
            private: friend class  _TemplateAutomaticTableBuilder;
            protected: TemplateAutomaticTable();
            public: ~TemplateAutomaticTable();
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