#ifndef NXOpen_FEATURES_SHIPDESIGN_CORNERCUT_HXX_INCLUDED
#define NXOpen_FEATURES_SHIPDESIGN_CORNERCUT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_ShipDesign_CornerCut.ja
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
        namespace ShipDesign
        {
            class CornerCut;
        }
    }
    namespace Features
    {
        class BodyFeature;
    }
    namespace Features
    {
        namespace ShipDesign
        {
            class _CornerCutBuilder;
            class CornerCutImpl;
            /** Represents a corner cut feature  <br> To create or edit an instance of this class, use @link NXOpen::Features::ShipDesign::CornerCutBuilder  NXOpen::Features::ShipDesign::CornerCutBuilder @endlink  <br> 
             <br>  Created in NX8.5.0.  <br>  
            */
            class NXOPENCPP_FEATURESEXPORT  CornerCut : public NXOpen::Features::BodyFeature
            {
                private: CornerCutImpl * m_cornercut_impl;
                private: friend class  _CornerCutBuilder;
                protected: CornerCut();
                public: ~CornerCut();
            };
        }
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
