#ifndef NXOpen_FIELDS_IAPPLICATION_HXX_INCLUDED
#define NXOpen_FIELDS_IAPPLICATION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Fields_IApplication.ja
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
#include <NXOpen/libnxopencpp_fields_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Fields
    {
        class IApplication;
    }
    namespace Fields
    {
        class _IApplicationBuilder;
        class IApplicationImpl;
        /**  @brief Interface for all applications registered with the Field subsystem. Each application
            type should only be registered once with the Field subsystem. Each application class is identified
            by its name. 

          <br> This is an abstract class, and cannot be created.  <br> 
         <br>  Created in NX12.0.0.  <br>  
        */
        class NXOPENCPP_FIELDSEXPORT  IApplication : public NXOpen::TaggedObject
        {
            private: IApplicationImpl * m_iapplication_impl;
            private: friend class  _IApplicationBuilder;
            protected: IApplication();
            public: ~IApplication();
            /**Returns  the name of the application. This name should be unique for each application class.
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXString Name
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