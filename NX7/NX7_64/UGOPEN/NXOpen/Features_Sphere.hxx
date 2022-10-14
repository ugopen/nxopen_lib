#ifndef NXOpen_FEATURES_SPHERE_HXX_INCLUDED
#define NXOpen_FEATURES_SPHERE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_Sphere.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/Features_BodyFeature.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Features
    {
        class Sphere;
    }
    namespace Features
    {
        class BodyFeature;
    }
    namespace Features
    {
        class _SphereBuilder;
        /** Represents a sphere feature */
        class NXOPENCPPEXPORT Sphere : public Features::BodyFeature
        {
            private: friend class  _SphereBuilder;
            protected: Sphere();
        };
    }
}
#undef EXPORTLIBRARY
#endif