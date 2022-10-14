#ifndef NXOpen_ANNOTATIONS_URLBUSINESSMODIFIER_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_URLBUSINESSMODIFIER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_UrlBusinessModifier.ja
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
#include <NXOpen/Annotations_BusinessModifier.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Annotations
    {
        class UrlBusinessModifier;
    }
    namespace Annotations
    {
        class BusinessModifier;
    }
    namespace Annotations
    {
        class _UrlBusinessModifierBuilder;
        /** Represents business modifier that applies an URL to a PMI. Please see ug_url_busmod.dfa for attribute details. */
        class NXOPENCPPEXPORT UrlBusinessModifier : public Annotations::BusinessModifier
        {
            private: friend class  _UrlBusinessModifierBuilder;
            protected: UrlBusinessModifier();
        };
    }
}
#undef EXPORTLIBRARY
#endif