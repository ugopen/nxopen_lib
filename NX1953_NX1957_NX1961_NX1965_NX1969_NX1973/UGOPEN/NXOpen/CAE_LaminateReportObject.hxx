#ifndef NXOpen_CAE_LAMINATEREPORTOBJECT_HXX_INCLUDED
#define NXOpen_CAE_LAMINATEREPORTOBJECT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_LaminateReportObject.ja
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
        class LaminateReportObject;
    }
    class NXObject;
    namespace CAE
    {
        class _LaminateReportObjectBuilder;
        class LaminateReportObjectImpl;
        /**  @brief  laminate report object  

           <br> To create or edit an instance of this class, use @link NXOpen::CAE::LaminateReportObjectBuilder  NXOpen::CAE::LaminateReportObjectBuilder @endlink  <br> 
         <br>  Created in NX1847.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  LaminateReportObject : public NXOpen::NXObject
        {
            private: LaminateReportObjectImpl * m_laminatereportobject_impl;
            private: friend class  _LaminateReportObjectBuilder;
            protected: LaminateReportObject();
            public: ~LaminateReportObject();
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