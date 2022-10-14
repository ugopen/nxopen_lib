#ifndef NXOpen_WELD_FILL_HXX_INCLUDED
#define NXOpen_WELD_FILL_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Weld_Fill.ja
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
#include <NXOpen/Features_BodyFeature.hxx>
#include <NXOpen/libnxopencpp_weld_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Weld
    {
        class Fill;
    }
    namespace Features
    {
        class BodyFeature;
    }
    namespace Weld
    {
        class _FillBuilder;
        class FillImpl;
        /** Represents a Weld Fill feature  <br> To create or edit an instance of this class, use @link Weld::WeldFillBuilder  Weld::WeldFillBuilder @endlink  <br> 
         <br>  Created in NX7.5.0.  <br>  
        */
        class NXOPENCPP_WELDEXPORT  Fill : public Features::BodyFeature
        {
            private: FillImpl * m_fill_impl;
            private: friend class  _FillBuilder;
            protected: Fill();
            public: ~Fill();
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