#ifndef NXOpen_CAE_SIMLOAD_HXX_INCLUDED
#define NXOpen_CAE_SIMLOAD_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_SimLoad.ja
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
#include <NXOpen/CAE_SimBC.hxx>
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
        class SimLoad;
    }
    namespace CAE
    {
        class SimBC;
    }
    namespace CAE
    {
        class _SimLoadBuilder;
        class SimLoadImpl;
        /**  @brief  Represents a load  

           <br> To create a new instance of this class, use @link NXOpen::CAE::SimLoadCollection::CreateLoad  NXOpen::CAE::SimLoadCollection::CreateLoad @endlink  <br> 
         <br>  Created in NX4.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  SimLoad : public NXOpen::CAE::SimBC
        {
            private: SimLoadImpl * m_simload_impl;
            private: friend class  _SimLoadBuilder;
            protected: SimLoad();
            public: ~SimLoad();
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
