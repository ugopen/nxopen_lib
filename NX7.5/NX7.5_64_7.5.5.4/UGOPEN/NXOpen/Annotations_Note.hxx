#ifndef NXOpen_ANNOTATIONS_NOTE_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_NOTE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_Note.ja
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
#include <NXOpen/Annotations_BaseNote.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Annotations
    {
        class Note;
    }
    namespace Annotations
    {
        class BaseNote;
    }
    namespace Annotations
    {
        class _NoteBuilder;
        class NoteImpl;
        /** Represents a Note */
        class NXOPENCPPEXPORT  Note : public Annotations::BaseNote
        {
            private: NoteImpl * m_note_impl;
            private: friend class  _NoteBuilder;
            protected: Note();
            public: ~Note();
        };
    }
}
#undef EXPORTLIBRARY
#endif
