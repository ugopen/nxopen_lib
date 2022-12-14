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
        /** Represents a Note  <br> To create or edit an instance of this class, use @link NXOpen::Annotations::DraftingNoteBuilder  NXOpen::Annotations::DraftingNoteBuilder @endlink  <br> 
         <br>  Created in NX3.0.0.  <br>  
        */
        class NXOPENCPP_ANNOTATIONSEXPORT  Note : public NXOpen::Annotations::BaseNote
        {
            private: NoteImpl * m_note_impl;
            private: friend class  _NoteBuilder;
            protected: Note();
            public: ~Note();
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
