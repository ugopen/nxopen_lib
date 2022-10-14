#ifndef NXOpen_CAM_MILLUSERDEFINED_HXX_INCLUDED
#define NXOpen_CAM_MILLUSERDEFINED_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_MillUserDefined.ja
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
#include <NXOpen/CAM_UserDefinedOpr.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAM
    {
        class MillUserDefined;
    }
    namespace CAM
    {
        class UserDefinedOpr;
    }
    namespace CAM
    {
        class _MillUserDefinedBuilder;
        class MillUserDefinedImpl;
        /** Represents a Mill User Defined operation */
        class NXOPENCPPEXPORT  MillUserDefined : public CAM::UserDefinedOpr
        {
            private: MillUserDefinedImpl * m_milluserdefined_impl;
            private: friend class  _MillUserDefinedBuilder;
            protected: MillUserDefined();
            public: ~MillUserDefined();
        };
    }
}
#undef EXPORTLIBRARY
#endif