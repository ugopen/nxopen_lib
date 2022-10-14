#ifndef NXOpen_ANNOTATIONS_DATUMDATA_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_DATUMDATA_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_DatumData.ja
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
        class DatumData;
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
        /** Represents datum data */
        class NXOPENCPPEXPORT DatumData : public TransientObject
        {
            public: explicit DatumData(void *ptr);
            /** Frees the object from memory.  After this method is called,
                    it is illegal to use the object.  In .NET, this method is automatically
                    called when the object is deleted by the garbage collector.   <br> License requirements : None */
            public: virtual ~DatumData();
            /**Returns  the label  <br> License requirements : None */
            public: NXString Label
            (
            );
            /**Sets  the label  <br> License requirements : None */
            public: void SetLabel
            (
                const NXString & label /** Datum label */
            );
            /**Returns  the flag indicating whether to draw X, where the leader terminates  <br> License requirements : None */
            public: bool DrawX
            (
            );
            /**Sets  the flag indicating whether to draw X, where the leader terminates  <br> License requirements : None */
            public: void SetDrawX
            (
                bool drawX /** Flag indicating whether to draw X where leader termiantes */
            );
            /**Returns  the flag indicating whether the datum is always vertical (without the stub)   <br> License requirements : None */
            public: bool AlwaysVertical
            (
            );
            /**Sets  the flag indicating whether the datum is always vertical (without the stub)   <br> License requirements : None */
            public: void SetAlwaysVertical
            (
                bool alwaysVertical /** Flag indicating whether the datum is always vertical */
            );
            /** Returns the SimpleDraftingAidPreferences object  @return  Datum preferences  <br> License requirements : None */
            public: NXOpen::Annotations::SimpleDraftingAidPreferences * GetSimpleDraftingAidPreferences
            (
            );
            /** Sets the SimpleDraftingAidPreferences object  <br> License requirements : None */
            public: void SetSimpleDraftingAidPreferences
            (
                NXOpen::Annotations::SimpleDraftingAidPreferences * preferences /** New datum preferences */
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif