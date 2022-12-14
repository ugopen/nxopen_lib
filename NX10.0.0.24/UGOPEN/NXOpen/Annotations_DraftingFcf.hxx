#ifndef NXOpen_ANNOTATIONS_DRAFTINGFCF_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_DRAFTINGFCF_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_DraftingFcf.ja
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
#include <NXOpen/Annotations_BaseFcf.hxx>
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
        class DraftingFcf;
    }
    namespace Annotations
    {
        class BaseFcf;
    }
    namespace Annotations
    {
        class _DraftingFcfBuilder;
        class DraftingFcfImpl;
        /** Represents an FCF  <br> To create or edit an instance of this class, use @link NXOpen::Annotations::DraftingFeatureControlFrameBuilder  NXOpen::Annotations::DraftingFeatureControlFrameBuilder @endlink  <br> 
         <br>  Created in NX4.0.0.  <br>  
        */
        class NXOPENCPP_ANNOTATIONSEXPORT  DraftingFcf : public NXOpen::Annotations::BaseFcf
        {
            private: DraftingFcfImpl * m_draftingfcf_impl;
            private: friend class  _DraftingFcfBuilder;
            protected: DraftingFcf();
            public: ~DraftingFcf();
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
