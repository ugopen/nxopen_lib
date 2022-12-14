#ifndef NXOpen_ANNOTATIONS_SIMPLEDRAFTINGAID_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_SIMPLEDRAFTINGAID_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_SimpleDraftingAid.ja
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
#include <NXOpen/Annotations_UserSymbolPreferences.hxx>
#include <NXOpen/Annotations_DraftingAid.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Annotations
    {
        class SimpleDraftingAid;
    }
    namespace Annotations
    {
        class DraftingAid;
    }
    namespace Annotations
    {
        class UserSymbolPreferences;
    }
    namespace Annotations
    {
        class _SimpleDraftingAidBuilder;
        /** Represents a simple drafting aid.
            In all edit methods, the changes are not applied to the system until
            an update is performed.  An update can be performed by calling @link Update::DoUpdate Update::DoUpdate@endlink .
             <br> This is an abstract class. <br> */
        class NXOPENCPPEXPORT SimpleDraftingAid : public Annotations::DraftingAid
        {
            private: friend class  _SimpleDraftingAidBuilder;
            protected: SimpleDraftingAid();
            /** Sets the drafting aid's text  <br> License requirements : drafting ("DRAFTING") */
            public: void SetText
            (
                std::vector<NXString> & lines /** the new text */
            );
            /** Returns the drafting aid's text  @return   <br> License requirements : None */
            public: std::vector<NXString> GetText
            (
            );
            /** Sets the user symbol preferences  <br> License requirements : drafting ("DRAFTING") */
            public: void SetUserSymbolPreferences
            (
                NXOpen::Annotations::UserSymbolPreferences * usym_prefs /** usym prefs */ 
            );
            /** Sets the user symbol size  <br> License requirements : drafting ("DRAFTING") */
            public: void SetUserSymbolSize
            (
                NXOpen::Annotations::UserSymbolPreferences::SizeType size_type /** Whether to use length and height or scale and aspect ratio */,
                double length_or_scale /** length or scale */ ,
                double height_or_aspect_ratio /** height or aspect ratio */ 
            );
            /** Gets the user symbol size  <br> License requirements : None */
            public: void GetUserSymbolSize
            (
                NXOpen::Annotations::UserSymbolPreferences::SizeType* size_type /** Whether the length and height or scale and aspect ratio is used */,
                double* length_or_scale /** length or scale */ ,
                double* height_or_aspect_ratio /** height or aspect ratio */ 
            );
            /** Returns the user symbol preferences  @return   <br> License requirements : None */
            public: NXOpen::Annotations::UserSymbolPreferences * GetUserSymbolPreferences
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
