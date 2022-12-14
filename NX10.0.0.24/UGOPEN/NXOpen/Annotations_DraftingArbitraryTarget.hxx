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
#include <NXOpen/Annotations_DraftingDatumTarget.hxx>
#include <NXOpen/Annotations_IArbitraryTarget.hxx>
#include <NXOpen/INXObject.hxx>
#include <NXOpen/libnxopencpp_annotations_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

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
        /** Represents a drafting arbitrary datum target.  <br> To create or edit an instance of this class, use @link NXOpen::Annotations::DraftingDatumTargetBuilder  NXOpen::Annotations::DraftingDatumTargetBuilder @endlink  <br> 
         <br>  Created in NX4.0.0.  <br>  
        */
        class NXOPENCPP_ANNOTATIONSEXPORT  DraftingArbitraryTarget : public NXOpen::Annotations::DraftingDatumTarget, public virtual NXOpen::Annotations::IArbitraryTarget
        {
            private: DraftingArbitraryTargetImpl * m_draftingarbitrarytarget_impl;
            private: friend class  _DraftingArbitraryTargetBuilder;
            protected: DraftingArbitraryTarget();
            public: ~DraftingArbitraryTarget();
            /**Returns  the target upper text.

                    NOTE: The set method should not be used to edit a read-only object such as a Mirrored PMI object.
                          If it is, the changes will be overridden when the part is updated. 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: virtual NXString UpperText
            (
            );
            /**Sets  the target upper text.

                    NOTE: The set method should not be used to edit a read-only object such as a Mirrored PMI object.
                          If it is, the changes will be overridden when the part is updated. 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: virtual void SetUpperText
            (
                const NXString & upperText /** Upper text */
            );
            /**Sets  the target upper text.

                    NOTE: The set method should not be used to edit a read-only object such as a Mirrored PMI object.
                          If it is, the changes will be overridden when the part is updated. 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            virtual void SetUpperText
            (
                const char * upperText /** Upper text */
            );
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
