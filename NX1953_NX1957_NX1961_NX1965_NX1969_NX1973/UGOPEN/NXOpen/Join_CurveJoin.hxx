#ifndef NXOpen_JOIN_CURVEJOIN_HXX_INCLUDED
#define NXOpen_JOIN_CURVEJOIN_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Join_CurveJoin.ja
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
#include <NXOpen/libjoinopencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Join
    {
        class CurveJoin;
    }
    namespace Features
    {
        class BodyFeature;
    }
    namespace Join
    {
        class _CurveJoinBuilder;
        class CurveJoinImpl;

        /// \cond NX_NO_DOC 
        /** Represents a curve based join feature  <br> To create or edit an instance of this class, use @link NXOpen::Join::CurveJoinBuilder  NXOpen::Join::CurveJoinBuilder @endlink  <br> 
         <br>  Created in NX1926.0.0.  <br>  
        */
        class JOINOPENCPPEXPORT  CurveJoin : public NXOpen::Features::BodyFeature
        {
            private: CurveJoinImpl * m_curvejoin_impl;
            private: friend class  _CurveJoinBuilder;
            protected: CurveJoin();
            public: ~CurveJoin();
        };

        /// \endcond 
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
