#ifndef NXOpen_CAE_RELATEDELEMFACEMETHODFACEPREF_HXX_INCLUDED
#define NXOpen_CAE_RELATEDELEMFACEMETHODFACEPREF_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_RelatedElemFaceMethodFacePref.ja
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

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace CAE
    {
        /** Specify the radius point type */
        enum FacePref
        {
            FacePrefFirst2dElse3d/** 2D if present else 3D */,
            FacePrefFirst3dElse2d/** 3D if present else 2D */,
            FacePrefOnly2d/** 2D only */,
            FacePrefOnly3d/** 3D only */
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

#endif
