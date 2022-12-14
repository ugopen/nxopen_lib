#ifndef NXOpen_CAE_FEELEMEDGE_HXX_INCLUDED
#define NXOpen_CAE_FEELEMEDGE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_FEElemEdge.ja
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
        class FEElemEdge;
    }
    namespace CAE
    {
        class _FEElemEdgeBuilder;
        class FEElemEdgeImpl;
        /** Represents a Finite Element Edge. */
        class NXOPENCPPEXPORT  FEElemEdge : public TaggedObject
        {
            private: FEElemEdgeImpl * m_feelemedge_impl;
            private: friend class  _FEElemEdgeBuilder;
            protected: FEElemEdge();
            public: ~FEElemEdge();
        };
    }
}
#undef EXPORTLIBRARY
#endif
