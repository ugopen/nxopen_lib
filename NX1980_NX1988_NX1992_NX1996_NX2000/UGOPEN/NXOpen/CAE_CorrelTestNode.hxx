#ifndef NXOpen_CAE_CORRELTESTNODE_HXX_INCLUDED
#define NXOpen_CAE_CORRELTESTNODE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_CorrelTestNode.ja
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
#include <NXOpen/NXObject.hxx>
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
        class CorrelTestNode;
    }
    class NXObject;
    namespace CAE
    {
        class _CorrelTestNodeBuilder;
        class CorrelTestNodeImpl;
        /** Represents a Correl Test Node. 
         <br>  Created in NX1980.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  CorrelTestNode : public NXOpen::NXObject
        {
            private: CorrelTestNodeImpl * m_correltestnode_impl;
            private: friend class  _CorrelTestNodeBuilder;
            protected: CorrelTestNode();
            public: ~CorrelTestNode();
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
