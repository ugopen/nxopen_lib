#ifndef NXOpen_PREFERENCES_SESSIONPDM_HXX_INCLUDED
#define NXOpen_PREFERENCES_SESSIONPDM_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Preferences_SessionPdm.ja
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
        class SessionPdm;
    }
    namespace Preferences
    {
        class SessionPreferences;
    }
    namespace Preferences
    {
        /** Represents the NX Manager preferences for the entire session  <br> To obtain an instance of this class, refer to @link Preferences::SessionPreferences Preferences::SessionPreferences@endlink  <br> */
        class NXOPENCPPEXPORT SessionPdm
        {
            /** Options for the kind of synchronisation with the PDM system performed
                        when a part is loaded. */
            public: enum SynchroniseOnLoadType
            {
                SynchroniseOnLoadTypeComplete/** complete */ ,
                SynchroniseOnLoadTypeAddWithTransforms/** add with transforms */ ,
                SynchroniseOnLoadTypeNone/** none */ 
            };

            /** Options for the kind of synchronisation with the PDM system performed
                        when a part is saved. */
            public: enum SynchroniseOnSaveType
            {
                SynchroniseOnSaveTypeComplete/** complete */ ,
                SynchroniseOnSaveTypeNone/** none */ 
            };

            /** Options for when to add NX datasets upon loading an unpopulated part in the PDM system */
            public: enum UnpopulatedBehaviourType
            {
                UnpopulatedBehaviourTypeOnSave/** on save */ ,
                UnpopulatedBehaviourTypeModifiedPrompt/** modified prompt */ ,
                UnpopulatedBehaviourTypeModifiedNoPrompt/** modified no prompt */ ,
                UnpopulatedBehaviourTypeNever/** never */ ,
                UnpopulatedBehaviourTypePreNx4/** pre nx4 */ 
            };

            private: NXOpen::Preferences::SessionPreferences* m_owner;
            public: explicit SessionPdm(NXOpen::Preferences::SessionPreferences *owner): m_owner(owner)
            {
            }
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            /**Returns  the kind of synchronisation performed when a part is loaded  <br> License requirements : None */
            public: NXOpen::Preferences::SessionPdm::SynchroniseOnLoadType SynchroniseOnLoad
            (
            );
            /**Sets  the kind of synchronisation performed when a part is loaded  <br> License requirements : None */
            public: void SetSynchroniseOnLoad
            (
                NXOpen::Preferences::SessionPdm::SynchroniseOnLoadType sync /** sync */ 
            );
            /**Returns  the kind of synchronisation performed when a part is saved  <br> License requirements : None */
            public: NXOpen::Preferences::SessionPdm::SynchroniseOnSaveType SynchroniseOnSave
            (
            );
            /**Sets  the kind of synchronisation performed when a part is saved  <br> License requirements : None */
            public: void SetSynchroniseOnSave
            (
                NXOpen::Preferences::SessionPdm::SynchroniseOnSaveType sync /** sync */ 
            );
            /**Returns  the behaviour when an unpopulated part is loaded  <br> License requirements : None */
            public: NXOpen::Preferences::SessionPdm::UnpopulatedBehaviourType UnpopulatedBehaviour
            (
            );
            /**Sets  the behaviour when an unpopulated part is loaded  <br> License requirements : None */
            public: void SetUnpopulatedBehaviour
            (
                NXOpen::Preferences::SessionPdm::UnpopulatedBehaviourType behaviour /** behaviour */ 
            );
            public: virtual void initialize();
        };
    }
}
#undef EXPORTLIBRARY
#endif
