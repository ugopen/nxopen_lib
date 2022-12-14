#ifndef NXOpen_ANNOTATIONS_PMIURLNOTE_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_PMIURLNOTE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_PmiUrlNote.ja
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
        class PmiUrlNote;
    }
    namespace Annotations
    {
        class PmiAttribute;
    }
    namespace Annotations
    {
        class _PmiUrlNoteBuilder;
        /** Represents a Pmi url Note */
        class NXOPENCPPEXPORT PmiUrlNote : public Annotations::PmiAttribute
        {
            private: friend class  _PmiUrlNoteBuilder;
            protected: PmiUrlNote();
        };
    }
}
#undef EXPORTLIBRARY
#endif
