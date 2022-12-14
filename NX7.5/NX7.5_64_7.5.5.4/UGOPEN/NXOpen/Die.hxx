#ifndef NXOpen_DIE_HXX_INCLUDED
#define NXOpen_DIE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Die.ja
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
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Die
    {
        /** Settings for the profile direction. */
        enum DirectionOption
        {
            DirectionOptionFromEnd = -1/** Profile direction is aligned with the first curve from the end to start. */,
            DirectionOptionFromStart = 1/** Profile direction is aligned with the first curve from the start to end. */
        };

        /** Settings for the build status of the die design sub features. */
        enum DieBuildStatusOption
        {
            DieBuildStatusOptionIndeterminant/** Build status could not be determined since sub feature is not active. */,
            DieBuildStatusOptionUnknown/** Build status is unknown since sub feature has not been built yet. */,
            DieBuildStatusOptionFail/** Sub feature build has failed. */,
            DieBuildStatusOptionValid/** Sub feature has built successfully. */
        };

    }
}
#undef EXPORTLIBRARY
#endif
