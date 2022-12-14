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
#include <NXOpen/NXObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
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
        /** Extrude Setup */
        class NXOPENCPPEXPORT  LaminateExtrudeSetup : public NXObject
        {
            private: LaminateExtrudeSetupImpl * m_laminateextrudesetup_impl;
            private: friend class  _LaminateExtrudeSetupBuilder;
            protected: LaminateExtrudeSetup();
            public: ~LaminateExtrudeSetup();
        };
    }
}
#undef EXPORTLIBRARY
#endif
