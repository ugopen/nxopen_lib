#ifndef NXOpen_TOOLING_STAMPINGPROCESSINFORMATIONDATA_HXX_INCLUDED
#define NXOpen_TOOLING_STAMPINGPROCESSINFORMATIONDATA_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Tooling_StampingProcessInformationData.ja
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
#include <NXOpen/Tooling_CostDataObject.hxx>
#include <NXOpen/libnxopencpp_tooling_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Tooling
    {
        class StampingProcessInformationData;
    }
    namespace Tooling
    {
        class CostDataObject;
    }
    namespace Tooling
    {
        class _StampingProcessInformationDataBuilder;
        class StampingProcessInformationDataImpl;
        /** Represents the StampingProcessInformationData object. 
              <br> Not support KF.  <br> 
         <br>  Created in NX2007.0.0.  <br>  
        */
        class NXOPENCPP_TOOLINGEXPORT  StampingProcessInformationData : public NXOpen::Tooling::CostDataObject
        {
            private: StampingProcessInformationDataImpl * m_stampingprocessinformationdata_impl;
            private: friend class  _StampingProcessInformationDataBuilder;
            protected: StampingProcessInformationData();
            public: ~StampingProcessInformationData();
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
