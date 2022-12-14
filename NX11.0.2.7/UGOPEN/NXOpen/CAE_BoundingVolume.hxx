#ifndef NXOpen_CAE_BOUNDINGVOLUME_HXX_INCLUDED
#define NXOpen_CAE_BOUNDINGVOLUME_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_BoundingVolume.ja
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
#include <NXOpen/DisplayableObject.hxx>
#include <NXOpen/libnxopencpp_cae_exports.hxx>

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
        class BoundingVolume;
    }
    class DisplayableObject;
    namespace CAE
    {
        class _BoundingVolumeBuilder;
        class BoundingVolumeImpl;
        /** Represents a @link NXOpen::CAE::BoundingVolume NXOpen::CAE::BoundingVolume@endlink .  <br> To create or edit an instance of this class, use @link NXOpen::CAE::BoundingVolumeBuilder  NXOpen::CAE::BoundingVolumeBuilder @endlink  <br> 
         <br>  Created in NX11.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  BoundingVolume : public NXOpen::DisplayableObject
        {
            private: BoundingVolumeImpl * m_boundingvolume_impl;
            private: friend class  _BoundingVolumeBuilder;
            protected: BoundingVolume();
            public: ~BoundingVolume();
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
