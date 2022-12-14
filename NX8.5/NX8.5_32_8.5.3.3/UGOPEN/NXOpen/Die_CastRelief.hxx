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
        /** Represents a cast relief feature  <br> To create or edit an instance of this class, use @link Die::CastReliefBuilder  Die::CastReliefBuilder @endlink  <br> 
         <br>  Created in NX6.0.0.  <br>  
        */
        class NXOPENCPP_DIEEXPORT  CastRelief : public Features::BodyFeature
        {
            private: CastReliefImpl * m_castrelief_impl;
            private: friend class  _CastReliefBuilder;
            protected: CastRelief();
            public: ~CastRelief();
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
