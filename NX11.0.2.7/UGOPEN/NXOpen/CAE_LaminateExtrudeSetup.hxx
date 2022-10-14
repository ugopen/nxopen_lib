#ifndef NXOpen_CAE_LAMINATEEXTRUDESETUP_HXX_INCLUDED
#define NXOpen_CAE_LAMINATEEXTRUDESETUP_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_LaminateExtrudeSetup.ja
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
#include <NXOpen/CAE_LaminateExtrudeSetup.hxx>
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
        class LaminateExtrudeSetup;
    }
    class NXObject;
    namespace CAE
    {
        class _LaminateExtrudeSetupBuilder;
        class LaminateExtrudeSetupImpl;
        /** Extrude Setup  <br> To create or edit an instance of this class, use @link NXOpen::CAE::LaminateExtrudeSetupBuilder  NXOpen::CAE::LaminateExtrudeSetupBuilder @endlink  <br> 
         <br>  Created in NX6.0.4.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  LaminateExtrudeSetup : public NXOpen::NXObject
        {
            private: LaminateExtrudeSetupImpl * m_laminateextrudesetup_impl;
            private: friend class  _LaminateExtrudeSetupBuilder;
            protected: LaminateExtrudeSetup();
            public: ~LaminateExtrudeSetup();
            /** Create groups for each inflated meshes (one group per mesh). 
             <br>  Created in NX8.5.1.  <br>  
             <br> License requirements : nx_lam_comp_adv ("Laminate Composites Advanced") */
            public: void CreateGroups
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