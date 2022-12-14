#ifndef NXOpen_CAE_AEROSTRUCTURES_MATERIALSOURCE_HXX_INCLUDED
#define NXOpen_CAE_AEROSTRUCTURES_MATERIALSOURCE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_AeroStructures_MaterialSource.ja
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
#include <NXOpen/CAE_AeroStructures_BaseExtractionSource.hxx>
#include <NXOpen/libnxopencpp_cae_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace CAE
    {
        namespace AeroStructures
        {
            class MaterialSource;
        }
    }
    namespace CAE
    {
        namespace AeroStructures
        {
            class BaseExtractionSource;
        }
    }
    namespace CAE
    {
        namespace AeroStructures
        {
            class _MaterialSourceBuilder;
            class MaterialSourceImpl;
            /** Material source class.  <br> To create a new instance of this class, use @link NXOpen::CAE::AeroStructures::ExtractionSourceSet::CreateMaterialSource  NXOpen::CAE::AeroStructures::ExtractionSourceSet::CreateMaterialSource @endlink  <br> 
             <br>  Created in NX1926.0.0.  <br>  
            */
            class NXOPENCPP_CAEEXPORT  MaterialSource : public NXOpen::CAE::AeroStructures::BaseExtractionSource
            {
                private: MaterialSourceImpl * m_materialsource_impl;
                private: friend class  _MaterialSourceBuilder;
                protected: MaterialSource();
                public: ~MaterialSource();
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
