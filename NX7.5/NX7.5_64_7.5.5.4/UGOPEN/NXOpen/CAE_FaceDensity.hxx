#ifndef NXOpen_CAE_FACEDENSITY_HXX_INCLUDED
#define NXOpen_CAE_FACEDENSITY_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_FaceDensity.ja
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
#include <NXOpen/CAE_MeshControl.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAE
    {
        class FaceDensity;
    }
    namespace CAE
    {
        class MeshControl;
    }
    namespace CAE
    {
        class _FaceDensityBuilder;
        class FaceDensityImpl;
        /**  @brief  Represents a CAE face density  

          */
        class NXOPENCPPEXPORT  FaceDensity : public CAE::MeshControl
        {
            private: FaceDensityImpl * m_facedensity_impl;
            private: friend class  _FaceDensityBuilder;
            protected: FaceDensity();
            public: ~FaceDensity();
        };
    }
}
#undef EXPORTLIBRARY
#endif
