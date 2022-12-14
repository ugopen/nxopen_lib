#ifndef NXOpen_ANNOTATIONS_DRAFTINGARBITRARYTARGET_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_DRAFTINGARBITRARYTARGET_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_DraftingArbitraryTarget.ja
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
#include <NXOpen/Annotations_IArbitraryTarget.hxx>
#include <NXOpen/Annotations_DraftingDatumTarget.hxx>
#include <NXOpen/INXObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Annotations
    {
        class DraftingArbitraryTarget;
    }
    namespace Annotations
    {
        class DraftingDatumTarget;
    }
    namespace Annotations
    {
        class IArbitraryTarget;
    }
    namespace Assemblies
    {
        class Component;
    }
    class BasePart;
    class INXObject;
    namespace Annotations
    {
        class _DraftingArbitraryTargetBuilder;
        class DraftingArbitraryTargetImpl;
        /** Represents a drafting arbitrary datum target. */
        class NXOPENCPPEXPORT  DraftingArbitraryTarget : public Annotations::DraftingDatumTarget, public virtual Annotations::IArbitraryTarget
        {
            private: DraftingArbitraryTargetImpl * m_draftingarbitrarytarget_impl;
            private: friend class  _DraftingArbitraryTargetBuilder;
            protected: DraftingArbitraryTarget();
            public: ~DraftingArbitraryTarget();
            /**Returns  the target upper text  <br> License requirements : None */
            public: virtual NXString UpperText
            (
            );
            /**Sets  the target upper text  <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: virtual void SetUpperText
            (
                const NXString & upperText /** Upper text */
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
