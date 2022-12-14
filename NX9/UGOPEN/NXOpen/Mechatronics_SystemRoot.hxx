#ifndef NXOpen_MECHATRONICS_SYSTEMROOT_HXX_INCLUDED
#define NXOpen_MECHATRONICS_SYSTEMROOT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Mechatronics_SystemRoot.ja
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
#include <NXOpen/Mechatronics_SystemObject.hxx>
#include <NXOpen/libnxopencpp_mechatronics_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Mechatronics
    {
        class SystemRoot;
    }
    namespace Mechatronics
    {
        class SystemObject;
    }
    namespace Mechatronics
    {
        class _SystemRootBuilder;
        class SystemRootImpl;
        /** Represents the System Root class. System Root is the root object of system tree. <br> Not support KF.  <br> 
         <br>  Created in NX9.0.0.  <br>  
        */
        class NXOPENCPP_MECHATRONICSEXPORT  SystemRoot : public Mechatronics::SystemObject
        {
            /** the system root types. */
            public: enum Type
            {
                TypeFunction/** Function    */,
                TypeLogical/** Logical     */,
                TypeRequirement/** Requirement */
            };

            private: SystemRootImpl * m_systemroot_impl;
            private: friend class  _SystemRootBuilder;
            protected: SystemRoot();
            public: ~SystemRoot();
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
