#ifndef NXOpen_CAE_FEELEMFACE_HXX_INCLUDED
#define NXOpen_CAE_FEELEMFACE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_FEElemFace.ja
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
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAE
    {
        class FEElemFace;
    }
    namespace CAE
    {
        class _FEElemFaceBuilder;
        class FEElemFaceImpl;
        /** Represents a Finite Element Face. */
        class NXOPENCPPEXPORT  FEElemFace : public TaggedObject
        {
            private: FEElemFaceImpl * m_feelemface_impl;
            private: friend class  _FEElemFaceBuilder;
            protected: FEElemFace();
            public: ~FEElemFace();
        };
    }
}
#undef EXPORTLIBRARY
#endif