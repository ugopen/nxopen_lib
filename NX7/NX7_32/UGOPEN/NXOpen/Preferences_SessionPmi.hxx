#ifndef NXOpen_PREFERENCES_SESSIONPMI_HXX_INCLUDED
#define NXOpen_PREFERENCES_SESSIONPMI_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Preferences_SessionPmi.ja
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
        class SessionPmi;
    }
    namespace Preferences
    {
        class SessionPreferences;
    }
    namespace Preferences
    {
        /** Represents the set of PMI preferences applicable to entire session <br> To obtain an instance of this class, refer to @link Preferences::SessionPreferences Preferences::SessionPreferences@endlink  <br> */
        class NXOPENCPPEXPORT SessionPmi
        {
            private: NXOpen::Preferences::SessionPreferences* m_owner;
            public: explicit SessionPmi(NXOpen::Preferences::SessionPreferences *owner): m_owner(owner)
            {
            }
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            /**Returns  the associated highlight color  <br> License requirements : None */
            public: int AssocHighlightColor
            (
            );
            /**Sets  the associated highlight color  <br> License requirements : None */
            public: void SetAssocHighlightColor
            (
                int assocHighlightColor /** assoc highlight color */ 
            );
            /**Returns  the reading direction preference  <br> License requirements : None */
            public: bool ReadingDirection
            (
            );
            /**Sets  the reading direction preference  <br> License requirements : None */
            public: void SetReadingDirection
            (
                bool readingDirection /** reading direction */ 
            );
            public: virtual void initialize();
        };
    }
}
#undef EXPORTLIBRARY
#endif