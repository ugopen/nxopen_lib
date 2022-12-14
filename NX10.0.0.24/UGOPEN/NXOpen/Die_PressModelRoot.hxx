#ifndef NXOpen_DIE_PRESSMODELROOT_HXX_INCLUDED
#define NXOpen_DIE_PRESSMODELROOT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Die_PressModelRoot.ja
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
#include <NXOpen/libnxopencpp_die_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Die
    {
        class PressModelRoot;
    }
    namespace Die
    {
        class _PressModelRootBuilder;
        class PressModelRootImpl;
        /** Represents a Die Simulation - Press Model Root.  <br> This class never built directly by the customer.  <br> 
         <br>  Created in NX6.0.0.  <br>  
        */
        class NXOPENCPP_DIEEXPORT  PressModelRoot : public NXOpen::TaggedObject
        {
            private: PressModelRootImpl * m_pressmodelroot_impl;
            private: friend class  _PressModelRootBuilder;
            protected: PressModelRoot();
            public: ~PressModelRoot();
            /** Is the press model active  @return  
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: bool IsActive
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
