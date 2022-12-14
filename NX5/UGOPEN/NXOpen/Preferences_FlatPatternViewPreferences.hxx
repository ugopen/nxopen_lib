#ifndef NXOpen_PREFERENCES_FLATPATTERNVIEWPREFERENCES_HXX_INCLUDED
#define NXOpen_PREFERENCES_FLATPATTERNVIEWPREFERENCES_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Preferences_FlatPatternViewPreferences.ja
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
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Preferences
    {
        class FlatPatternViewPreferences;
    }
    namespace Preferences
    {
        class ViewPreferences;
    }
    namespace SheetMetal
    {
        class FlatPatternSettings;
    }
    namespace Preferences
    {
        /** Provides access to object and callout properties for sheet-metal data in
            flat pattern views on drawings.  <br> To obtain an instance of this class, refer to @link Preferences::ViewPreferences Preferences::ViewPreferences@endlink  <br> */
        class NXOPENCPPEXPORT FlatPatternViewPreferences
        {
            private: NXOpen::Preferences::ViewPreferences* m_owner;
            public: explicit FlatPatternViewPreferences(NXOpen::Preferences::ViewPreferences *owner): m_owner(owner)
            {
            }
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            /** Returns the properties object for the part's flat pattern view preferences.  @return  Reference to the object on which to get and set the
                                    preferences for flat pattern drawing member views.  <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
            public: NXOpen::SheetMetal::FlatPatternSettings * GetPropertiesObject
            (
            );
            /** Commits and applies all the settings done with set_callout_type_display
                        and set_object_type_display. It must be called after a sequence of calls
                        to those methods to cause the view to update.  <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
            public: void Commit
            (
            );
            public: virtual void initialize();
        };
    }
}
#undef EXPORTLIBRARY
#endif
