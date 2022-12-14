#ifndef NXOpen_PREFERENCES_DRAFTINGPREFERENCEMANAGER_HXX_INCLUDED
#define NXOpen_PREFERENCES_DRAFTINGPREFERENCEMANAGER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Preferences_DraftingPreferenceManager.ja
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
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Preferences
    {
        class DraftingPreferenceManager;
    }
    namespace Preferences
    {
        class PartPreferences;
    }
    namespace Preferences
    {
        class LoadDraftingStandardBuilder;
    }
    namespace Preferences
    {
        class DraftingPreferenceManagerImpl;
        /** Represents a collection of pmi preference builders. <br> To obtain an instance of this class, refer to @link Preferences::PartPreferences Preferences::PartPreferences@endlink  <br> */
        class NXOPENCPPEXPORT  DraftingPreferenceManager
        {
            private: DraftingPreferenceManagerImpl * m_draftingpreferencemanager_impl;
            private: NXOpen::Preferences::PartPreferences* m_owner;
            /** Constructor */
            public: explicit DraftingPreferenceManager(NXOpen::Preferences::PartPreferences *owner);
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~DraftingPreferenceManager();
            /** Creates the load drafting standard builder  @return  the loaddraftingstandard Builder with this identifier  <br> License requirements : None */
            public: NXOpen::Preferences::LoadDraftingStandardBuilder * CreateLoadDraftingStandardBuilder
            (
            );
        }; //lint !e1712 default constructor not defined for class  

    }
}
#undef EXPORTLIBRARY
#endif
