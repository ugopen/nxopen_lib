#ifndef NXOpen_FEATURES_SUBDIVISION_SUBDIVISIONBODY_HXX_INCLUDED
#define NXOpen_FEATURES_SUBDIVISION_SUBDIVISIONBODY_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_Subdivision_SubdivisionBody.ja
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
        namespace Subdivision
        {
            class SubdivisionBody;
        }
    }
    namespace Features
    {
        class BodyFeature;
    }
    namespace Features
    {
        namespace Subdivision
        {
            class _SubdivisionBodyBuilder;
            class SubdivisionBodyImpl;
            /** Represents a subdivision body feature.  <br> An instance of this class can be obtained from @link SubdivisionTaskEnvironment::ActiveSubdivisionBodyFeature SubdivisionTaskEnvironment::ActiveSubdivisionBodyFeature@endlink   <br> 
             <br>  Created in NX9.0.0.  <br>  
            */
            class NXOPENCPP_FEATURESEXPORT  SubdivisionBody : public Features::BodyFeature
            {
                private: SubdivisionBodyImpl * m_subdivisionbody_impl;
                private: friend class  _SubdivisionBodyBuilder;
                protected: SubdivisionBody();
                public: ~SubdivisionBody();
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