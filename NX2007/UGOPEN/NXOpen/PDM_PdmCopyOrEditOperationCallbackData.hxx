#ifndef NXOpen_PDM_PDMCOPYOREDITOPERATIONCALLBACKDATA_HXX_INCLUDED
#define NXOpen_PDM_PDMCOPYOREDITOPERATIONCALLBACKDATA_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     PDM_PdmCopyOrEditOperationCallbackData.ja
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
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/PDM_PdmCopyOrEditOperationBuilder.hxx>
#include <NXOpen/libnxopencpp_pdm_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace PDM
    {
        class PdmCopyOrEditOperationCallbackData;
    }
    namespace PDM
    {
        class PdmCopyOrEditOperationBuilder;
    }
    namespace PDM
    {
        class _PdmCopyOrEditOperationCallbackDataBuilder;
        class PdmCopyOrEditOperationCallbackDataImpl;
        /** JA interface for PdmCopyOrEditOperationCallbackData object  <br> This cannot be created  <br> 
         <br>  Created in NX1980.0.0.  <br>  
        */
        class NXOPENCPP_PDMEXPORT  PdmCopyOrEditOperationCallbackData : public NXOpen::TaggedObject
        {
            private: PdmCopyOrEditOperationCallbackDataImpl * m_pdmcopyoreditoperationcallbackdata_impl;
            private: friend class  _PdmCopyOrEditOperationCallbackDataBuilder;
            protected: PdmCopyOrEditOperationCallbackData();
            public: ~PdmCopyOrEditOperationCallbackData();
            /** The @link NXOpen::PDM::PdmCopyOrEditOperationBuilder NXOpen::PDM::PdmCopyOrEditOperationBuilder@endlink  Builder used in this operation 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::PDM::PdmCopyOrEditOperationBuilder * GetBuilder
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