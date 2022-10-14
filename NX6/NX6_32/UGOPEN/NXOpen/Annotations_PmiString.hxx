#ifndef NXOpen_ANNOTATIONS_PMISTRING_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_PMISTRING_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_PmiString.ja
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
#include <NXOpen/Annotations_PmiAttribute.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Annotations
    {
        class PmiString;
    }
    namespace Annotations
    {
        class PmiAttribute;
    }
    namespace Annotations
    {
        class _PmiStringBuilder;
        /** Represents a Pmi String */
        class NXOPENCPPEXPORT PmiString : public Annotations::PmiAttribute
        {
            private: friend class  _PmiStringBuilder;
            protected: PmiString();
        };
    }
}
#undef EXPORTLIBRARY
#endif