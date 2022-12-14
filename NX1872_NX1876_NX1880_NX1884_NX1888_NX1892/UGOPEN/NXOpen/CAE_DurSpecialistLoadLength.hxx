#ifndef NXOpen_CAE_DURSPECIALISTLOADLENGTH_HXX_INCLUDED
#define NXOpen_CAE_DURSPECIALISTLOADLENGTH_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_DurSpecialistLoadLength.ja
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
        class DurSpecialistLoadLength;
    }
    namespace CAE
    {
        class _DurSpecialistLoadLengthBuilder;
        class DurSpecialistLoadLengthImpl;
        /**  @brief  TODO: Add documentation  

          
         <br>  Created in NX12.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  DurSpecialistLoadLength : public NXOpen::TaggedObject
        {
            private: DurSpecialistLoadLengthImpl * m_durspecialistloadlength_impl;
            private: friend class  _DurSpecialistLoadLengthBuilder;
            protected: DurSpecialistLoadLength();
            public: ~DurSpecialistLoadLength();
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
