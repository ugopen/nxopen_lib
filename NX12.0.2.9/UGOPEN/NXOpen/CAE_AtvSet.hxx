#ifndef NXOpen_CAE_ATVSET_HXX_INCLUDED
#define NXOpen_CAE_ATVSET_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_AtvSet.ja
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
#include <NXOpen/CAE_AlternateFemRepresentationSource.hxx>
#include <NXOpen/CAE_IPostScenarioDataSource.hxx>
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
        class AtvSet;
    }
    namespace CAE
    {
        class AlternateFemRepresentationSource;
    }
    namespace CAE
    {
        class IPostScenarioDataSource;
    }
    namespace CAE
    {
        class _AtvSetBuilder;
        class AtvSetImpl;
        /**  @brief  This is the class representing a Atv result set.  

           <br> Not support KF.  <br> 
         <br>  Created in NX12.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  AtvSet : public NXOpen::CAE::AlternateFemRepresentationSource, public virtual NXOpen::CAE::IPostScenarioDataSource
        {
            private: AtvSetImpl * m_atvset_impl;
            private: friend class  _AtvSetBuilder;
            protected: AtvSet();
            public: ~AtvSet();
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
