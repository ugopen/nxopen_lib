#ifndef NXOpen_CAE_OVERRIDE_HXX_INCLUDED
#define NXOpen_CAE_OVERRIDE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_Override.ja
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
        class Override;
    }
    namespace CAE
    {
        class _OverrideBuilder;
        class OverrideImpl;
        /**  @brief This class represents an override. 

           <br> An instance of this class can not be created  <br> 
         <br>  Created in NX1847.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  Override : public NXOpen::TaggedObject
        {
            private: OverrideImpl * m_override_impl;
            private: friend class  _OverrideBuilder;
            protected: Override();
            public: ~Override();
            /** Prints information for a @link NXOpen::CAE::Override NXOpen::CAE::Override@endlink  
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void Information
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