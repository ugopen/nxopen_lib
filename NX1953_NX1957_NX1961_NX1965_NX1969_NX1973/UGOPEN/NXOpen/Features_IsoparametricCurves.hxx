#ifndef NXOpen_FEATURES_ISOPARAMETRICCURVES_HXX_INCLUDED
#define NXOpen_FEATURES_ISOPARAMETRICCURVES_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_IsoparametricCurves.ja
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
#include <NXOpen/Features_CurveFeature.hxx>
#include <NXOpen/libnxopencpp_features_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Features
    {
        class IsoparametricCurves;
    }
    namespace Features
    {
        class CurveFeature;
    }
    namespace Features
    {
        class _IsoparametricCurvesBuilder;
        class IsoparametricCurvesImpl;
        /** Represents a isoparametric curves feature  <br> To create or edit an instance of this class, use @link NXOpen::Features::IsoparametricCurvesBuilder  NXOpen::Features::IsoparametricCurvesBuilder @endlink  <br> 
         <br>  Created in NX8.0.0.  <br>  
        */
        class NXOPENCPP_FEATURESEXPORT  IsoparametricCurves : public NXOpen::Features::CurveFeature
        {
            private: IsoparametricCurvesImpl * m_isoparametriccurves_impl;
            private: friend class  _IsoparametricCurvesBuilder;
            protected: IsoparametricCurves();
            public: ~IsoparametricCurves();
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
