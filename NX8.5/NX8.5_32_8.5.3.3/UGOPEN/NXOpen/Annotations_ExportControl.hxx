#ifndef NXOpen_ANNOTATIONS_EXPORTCONTROL_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_EXPORTCONTROL_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_ExportControl.ja
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
#include <NXOpen/Annotations_PmiAttribute.hxx>
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
        class ExportControl;
    }
    namespace Annotations
    {
        class PmiAttribute;
    }
    namespace Annotations
    {
        class _ExportControlBuilder;
        class ExportControlImpl;
        /** Represents a Export Control  <br> To create or edit an instance of this class, use @link Annotations::ExportControlBuilder  Annotations::ExportControlBuilder @endlink  <br> 
         <br>  Created in NX6.0.0.  <br>  
        */
        class NXOPENCPP_ANNOTATIONSEXPORT  ExportControl : public Annotations::PmiAttribute
        {
            private: ExportControlImpl * m_exportcontrol_impl;
            private: friend class  _ExportControlBuilder;
            protected: ExportControl();
            public: ~ExportControl();
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
