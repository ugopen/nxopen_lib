#ifndef NXOpen_FEATURES_COATINGS_COATING_HXX_INCLUDED
#define NXOpen_FEATURES_COATINGS_COATING_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_Coatings_Coating.ja
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
        namespace Coatings
        {
            class Coating;
        }
    }
    namespace Features
    {
        class BodyFeature;
    }
    namespace Features
    {
        namespace Coatings
        {
            class _CoatingBuilder;
            class CoatingImpl;
            /**
                     * Defines a feature that will contain some form of bodies (solid or sheet) created on some
                     * form of user-defined area.
                      <br> To create or edit an instance of this class, use @link NXOpen::Features::Coatings::CoatingBuilder  NXOpen::Features::Coatings::CoatingBuilder @endlink  <br> 
             <br>  Created in NX1926.0.0.  <br>  
            */
            class NXOPENCPP_FEATURESEXPORT  Coating : public NXOpen::Features::BodyFeature
            {
                private: CoatingImpl * m_coating_impl;
                private: friend class  _CoatingBuilder;
                protected: Coating();
                public: ~Coating();
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
