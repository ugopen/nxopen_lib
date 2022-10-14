#ifndef NXOpen_DIE_CASTRELIEF_HXX_INCLUDED
#define NXOpen_DIE_CASTRELIEF_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Die_CastRelief.ja
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
#include <NXOpen/Features_BodyFeature.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Die
    {
        class CastRelief;
    }
    namespace Features
    {
        class BodyFeature;
    }
    namespace Die
    {
        class _CastReliefBuilder;
        class CastReliefImpl;
        /** Represents a cast relief feature */
        class NXOPENCPPEXPORT  CastRelief : public Features::BodyFeature
        {
            private: CastReliefImpl * m_castrelief_impl;
            private: friend class  _CastReliefBuilder;
            protected: CastRelief();
            public: ~CastRelief();
        };
    }
}
#undef EXPORTLIBRARY
#endif