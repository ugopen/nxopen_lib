#ifndef NXOpen_ANNOTATIONS_REVISIONBUSINESSMODIFIER_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_REVISIONBUSINESSMODIFIER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_RevisionBusinessModifier.ja
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
#include <NXOpen/Annotations_BusinessModifier.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Annotations
    {
        class RevisionBusinessModifier;
    }
    namespace Annotations
    {
        class BusinessModifier;
    }
    namespace Annotations
    {
        class _RevisionBusinessModifierBuilder;
        class RevisionBusinessModifierImpl;
        /** Represents business modifier that applies a revision (in the string format such as -A1) to 
                a PMI. Plese see ug_revision_busmod.dfa for attribute details. */
        class NXOPENCPPEXPORT  RevisionBusinessModifier : public Annotations::BusinessModifier
        {
            private: RevisionBusinessModifierImpl * m_revisionbusinessmodifier_impl;
            private: friend class  _RevisionBusinessModifierBuilder;
            protected: RevisionBusinessModifier();
            public: ~RevisionBusinessModifier();
        };
    }
}
#undef EXPORTLIBRARY
#endif
