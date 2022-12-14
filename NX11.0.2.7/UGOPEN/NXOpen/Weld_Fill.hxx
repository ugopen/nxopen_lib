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
#include <NXOpen/INXObject.hxx>
#include <NXOpen/Weld_IFeature.hxx>
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
    namespace Assemblies
    {
        class Component;
    }
    class BasePart;
    namespace Features
    {
        class BodyFeature;
    }
    class INXObject;
    namespace Weld
    {
        class IFeature;
    }
    namespace Weld
    {
        class _FillBuilder;
        class FillImpl;
        /** Represents a Weld Fill feature  <br> To create or edit an instance of this class, use @link NXOpen::Weld::WeldFillBuilder  NXOpen::Weld::WeldFillBuilder @endlink  <br> 
         <br>  Created in NX7.5.0.  <br>  
        */
        class NXOPENCPP_WELDEXPORT  Fill : public NXOpen::Features::BodyFeature, public virtual NXOpen::Weld::IFeature
        {
            private: FillImpl * m_fill_impl;
            private: friend class  _FillBuilder;
            protected: Fill();
            public: ~Fill();
            /** Returns the feature diagnostic information, warning, or error codes. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: virtual void GetFeatureDiagnostics
            (
                std::vector<int> & diagnosticCodes /** the information, warning, or error codes for this feature. */
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
