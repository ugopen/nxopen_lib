#ifndef NXOpen_WELD_POINTMARKPOINT_HXX_INCLUDED
#define NXOpen_WELD_POINTMARKPOINT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Weld_PointMarkPoint.ja
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
#include <NXOpen/Features_Feature.hxx>
#include <NXOpen/libnxopencpp_weld_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Weld
    {
        class PointMarkPoint;
    }
    namespace Features
    {
        class Feature;
    }
    namespace Weld
    {
        class _PointMarkPointBuilder;
        class PointMarkPointImpl;
        /** Represents a Weld.PointMarkPoint Feature.  <br> To create or edit an instance of this class, use @link NXOpen::Weld::PointMarkBuilder  NXOpen::Weld::PointMarkBuilder @endlink  <br> 
         <br>  Created in NX10.0.0.  <br>  
        */
        class NXOPENCPP_WELDEXPORT  PointMarkPoint : public NXOpen::Features::Feature
        {
            private: PointMarkPointImpl * m_pointmarkpoint_impl;
            private: friend class  _PointMarkPointBuilder;
            protected: PointMarkPoint();
            public: ~PointMarkPoint();
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
