#ifndef NXOpen_CAE_QUALITYAUDIT_CONNECTEDCOMPONENTSGROUPRESULT_HXX_INCLUDED
#define NXOpen_CAE_QUALITYAUDIT_CONNECTEDCOMPONENTSGROUPRESULT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_QualityAudit_ConnectedComponentsGroupResult.ja
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
#include <NXOpen/CAE_QualityAudit_IConnectedComponents.hxx>
#include <NXOpen/CAE_QualityAudit_Result.hxx>
#include <NXOpen/INXObject.hxx>
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
        namespace QualityAudit
        {
            class ConnectedComponentsGroupResult;
        }
    }
    namespace Assemblies
    {
        class Component;
    }
    class BasePart;
    namespace CAE
    {
        namespace QualityAudit
        {
            class IConnectedComponents;
        }
    }
    namespace CAE
    {
        namespace QualityAudit
        {
            class Result;
        }
    }
    class INXObject;
    namespace CAE
    {
        namespace QualityAudit
        {
            class _ConnectedComponentsGroupResultBuilder;
            class ConnectedComponentsGroupResultImpl;
            /**  @brief  This result a group of connected components. 

               <br> To obtain this result see @link CAE::QualityAudit::ComponentConnectivity CAE::QualityAudit::ComponentConnectivity@endlink .  <br> 
             <br>  Created in NX1847.0.0.  <br>  
            */
            class NXOPENCPP_CAEEXPORT  ConnectedComponentsGroupResult : public NXOpen::CAE::QualityAudit::Result, public virtual NXOpen::CAE::QualityAudit::IConnectedComponents
            {
                private: ConnectedComponentsGroupResultImpl * m_connectedcomponentsgroupresult_impl;
                private: friend class  _ConnectedComponentsGroupResultBuilder;
                protected: ConnectedComponentsGroupResult();
                public: ~ConnectedComponentsGroupResult();
                /** Gets the connected components from a result 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : None */
                public: virtual std::vector<NXOpen::Assemblies::Component *> GetComponents
                (
                );
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
