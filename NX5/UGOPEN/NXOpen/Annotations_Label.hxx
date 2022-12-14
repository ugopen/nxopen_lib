#ifndef NXOpen_ANNOTATIONS_LABEL_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_LABEL_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_Label.ja
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
#include <NXOpen/Annotations_NoteBase.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Annotations
    {
        class Label;
    }
    namespace Annotations
    {
        class NoteBase;
    }
    namespace Annotations
    {
        class _LabelBuilder;
        /** Represents a label  <br> To create an instance of this class @link Annotations::AnnotationManager Annotations::AnnotationManager@endlink  <br> */
        class NXOPENCPPEXPORT Label : public Annotations::NoteBase
        {
            private: friend class  _LabelBuilder;
            protected: Label();
        };
    }
}
#undef EXPORTLIBRARY
#endif
