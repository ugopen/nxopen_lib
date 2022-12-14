#ifndef NXOpen_CAE_OPTIMIZATION_TBSRESTRICTAREA_HXX_INCLUDED
#define NXOpen_CAE_OPTIMIZATION_TBSRESTRICTAREA_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_Optimization_TBSRestrictArea.ja
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
        namespace Optimization
        {
            class TBSRestrictArea;
        }
    }
    class NXObject;
    namespace CAE
    {
        namespace Optimization
        {
            class _TBSRestrictAreaBuilder;
            class TBSRestrictAreaImpl;
            /** Represents the restrictions for the design variable in an optimization  <br> To create or edit an instance of this class, use @link NXOpen::CAE::Optimization::TBSRestrictAreaBuilder  NXOpen::CAE::Optimization::TBSRestrictAreaBuilder @endlink  <br> 
             <br>  Created in NX8.0.0.  <br>  
            */
            class NXOPENCPP_CAEEXPORT  TBSRestrictArea : public NXOpen::NXObject
            {
                private: TBSRestrictAreaImpl * m_tbsrestrictarea_impl;
                private: friend class  _TBSRestrictAreaBuilder;
                protected: TBSRestrictArea();
                public: ~TBSRestrictArea();
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
