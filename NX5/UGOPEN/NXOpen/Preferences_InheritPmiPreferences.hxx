#ifndef NXOpen_PREFERENCES_INHERITPMIPREFERENCES_HXX_INCLUDED
#define NXOpen_PREFERENCES_INHERITPMIPREFERENCES_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Preferences_InheritPmiPreferences.ja
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
#include <NXOpen/Preferences_ViewStylePreferencesData.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Preferences
    {
        class InheritPmiPreferences;
    }
    namespace Preferences
    {
        class ViewPreferences;
    }
    namespace Preferences
    {
        /** Represents set of InheritPmiPreferences applicable to drafting views.  <br> To obtain an instance of this class, refer to @link Preferences::ViewPreferences Preferences::ViewPreferences@endlink  <br> */
        class NXOPENCPPEXPORT InheritPmiPreferences
        {
            private: NXOpen::Preferences::ViewPreferences* m_owner;
            public: explicit InheritPmiPreferences(NXOpen::Preferences::ViewPreferences *owner): m_owner(owner)
            {
            }
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            /**Returns  the Status of inherit pmi mode.  <br> License requirements : None */
            public: NXOpen::Preferences::PmiOption InheritPmiMode
            (
            );
            /**Returns  the Status of pmi inherited to drawing.  <br> License requirements : None */
            public: bool InheritPmiToDrawing
            (
            );
            /**Returns  the Inherit GD and T option  <br> License requirements : None */
            public: NXOpen::Preferences::GdtOption InheritGdt
            (
            );
            /**Sets  the Status of inherit pmi mode.  <br> License requirements : drafting ("DRAFTING") */
            public: void SetInheritPmiMode
            (
                NXOpen::Preferences::PmiOption pmi_option /** pmi option */ 
            );
            /**Sets  the Status of pmi inherited to drawing.  <br> License requirements : drafting ("DRAFTING") */
            public: void SetInheritPmiToDrawing
            (
                bool pmi_option /** pmi option */ 
            );
            /**Sets  the Inherit GD and T option  <br> License requirements : drafting ("DRAFTING") */
            public: void SetInheritGdt
            (
                NXOpen::Preferences::GdtOption gdt_option /** gdt option */ 
            );
            public: virtual void initialize();
        };
    }
}
#undef EXPORTLIBRARY
#endif
