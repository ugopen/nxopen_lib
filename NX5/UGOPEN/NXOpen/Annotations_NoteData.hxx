#ifndef NXOpen_ANNOTATIONS_NOTEDATA_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_NOTEDATA_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_NoteData.ja
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
#include <NXOpen/Annotations_SimpleDraftingAidPreferences.hxx>
#include <NXOpen/TransientObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Annotations
    {
        class NoteData;
    }
    namespace Annotations
    {
        class SimpleDraftingAidPreferences;
    }
    namespace Annotations
    {
    }
    namespace Annotations
    {
        /** Represents note data */
        class NXOPENCPPEXPORT NoteData : public TransientObject
        {
            public: explicit NoteData(void *ptr);
            /** Frees the object from memory.  After this method is called,
                    it is illegal to use the object.  In .NET, this method is automatically
                    called when the object is deleted by the garbage collector.   <br> License requirements : None */
            public: virtual ~NoteData();
            /** Returns the text  @return  List of lines  <br> License requirements : None */
            public: std::vector<NXString> GetText
            (
            );
            /** Sets the text  <br> License requirements : None */
            public: void SetText
            (
                std::vector<NXString> & lines /** List of new lines */
            );
            /** Returns the SimpleDraftingAidPreferences object  @return  Note preferences  <br> License requirements : None */
            public: NXOpen::Annotations::SimpleDraftingAidPreferences * GetSimpleDraftingAidPreferences
            (
            );
            /** Sets the SimpleDraftingAidPreferences object  <br> License requirements : None */
            public: void SetSimpleDraftingAidPreferences
            (
                NXOpen::Annotations::SimpleDraftingAidPreferences * preferences /** New note preferences */
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
