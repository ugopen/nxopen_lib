#ifndef NXOpen_PDM_ORDEREDELEMENTGROUP_HXX_INCLUDED
#define NXOpen_PDM_ORDEREDELEMENTGROUP_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     PDM_OrderedElementGroup.ja
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
        class OrderedElementGroup;
    }
    class NXObject;
    namespace PDM
    {
        class _OrderedElementGroupBuilder;
        class OrderedElementGroupImpl;
        /** 
                Represents a base class that provides common methods for ordered elements group in a @link NXOpen::PDM::ElementGroup NXOpen::PDM::ElementGroup@endlink .
             <br> Instance of this can not directly created.  <br> 
         <br>  Created in NX11.0.0.  <br>  
        */
        class NXOPENCPP_PDMEXPORT  OrderedElementGroup : public NXOpen::NXObject
        {
            private: OrderedElementGroupImpl * m_orderedelementgroup_impl;
            private: friend class  _OrderedElementGroupBuilder;
            protected: OrderedElementGroup();
            public: ~OrderedElementGroup();
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
