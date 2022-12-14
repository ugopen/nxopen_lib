#ifndef NXOpen_JOIN_FACEJOIN_HXX_INCLUDED
#define NXOpen_JOIN_FACEJOIN_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Join_FaceJoin.ja
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
        class FaceJoin;
    }
    namespace Features
    {
        class BodyFeature;
    }
    namespace Join
    {
        class _FaceJoinBuilder;
        class FaceJoinImpl;

        /// \cond NX_NO_DOC 
        /** Represents a face based join feature  <br> To create or edit an instance of this class, use @link NXOpen::Join::FaceJoinBuilder  NXOpen::Join::FaceJoinBuilder @endlink  <br> 
         <br>  Created in NX1926.0.0.  <br>  
        */
        class JOINOPENCPPEXPORT  FaceJoin : public NXOpen::Features::BodyFeature
        {
            private: FaceJoinImpl * m_facejoin_impl;
            private: friend class  _FaceJoinBuilder;
            protected: FaceJoin();
            public: ~FaceJoin();
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
