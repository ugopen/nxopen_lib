#ifndef NXOpen_PREFERENCES_PARTAPPEARANCEMGRPREFERENCE_HXX_INCLUDED
#define NXOpen_PREFERENCES_PARTAPPEARANCEMGRPREFERENCE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Preferences_PartAppearanceMgrPreference.ja
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
#include <NXOpen/libnxopencpp_preferences_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Preferences
    {
        class PartAppearanceMgrPreference;
    }
    namespace Preferences
    {
        class PartPreferences;
    }
    namespace Preferences
    {
        class PartAppearanceMgrPreferenceImpl;
        /**
            Represents preferences for AppearanceManagement that are applicable
                to the entire part.  <br> To obtain an instance of this class, refer to @link NXOpen::Preferences::PartPreferences  NXOpen::Preferences::PartPreferences @endlink  <br> 
         <br>  Created in NX1899.0.0.  <br>  
        */
        class NXOPENCPP_PREFERENCESEXPORT  PartAppearanceMgrPreference
        {
            /** Represents the source type of designator library*/
            public: enum DesignatorSourceType
            {
                DesignatorSourceTypeProductStructure/** from part file related .dlf */,
                DesignatorSourceTypeFile/** from an seperate .dlf file specified by user */
            };

            private: PartAppearanceMgrPreferenceImpl * m_partappearancemgrpreference_impl;
            private: NXOpen::Preferences::PartPreferences* m_owner;
            /// \cond NX_NO_DOC 
            public: explicit PartAppearanceMgrPreference(NXOpen::Preferences::PartPreferences *owner);


            /// \endcond 
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~PartAppearanceMgrPreference();
            /**Returns  the source of designator library 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Preferences::PartAppearanceMgrPreference::DesignatorSourceType DesignatorLibSource
            (
            );
            /**Sets  the source of designator library 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : studio_render ("UG STUDIO RENDER") */
            public: void SetDesignatorLibSource
            (
                NXOpen::Preferences::PartAppearanceMgrPreference::DesignatorSourceType designatorSourceType /** designator source type */ 
            );
            /** Get the seperate .dlf file of designator library 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: NXString GetDesignatorLibraryFile
            (
            );
            /** Set the seperate .dlf file of designator library 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : studio_render ("UG STUDIO RENDER") */
            public: void SetDesignatorLibraryFile
            (
                const NXString & designatorFile /** designator file */ 
            );
            /** Set the seperate .dlf file of designator library 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : studio_render ("UG STUDIO RENDER") */
            void SetDesignatorLibraryFile
            (
                const char * designatorFile /** designator file */ 
            );
            /**Returns  the appearance areas name automatic generating
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: NXString PrefixAppearanceAreas
            (
            );
            /**Sets  the appearance areas name automatic generating
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : studio_render ("UG STUDIO RENDER") */
            public: void SetPrefixAppearanceAreas
            (
                const NXString & designatorPrefix /** designator prefix */ 
            );
            /**Sets  the appearance areas name automatic generating
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : studio_render ("UG STUDIO RENDER") */
            void SetPrefixAppearanceAreas
            (
                const char * designatorPrefix /** designator prefix */ 
            );
            /**Returns  the appearance schemes automatic generating
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: NXString PrefixAppearanceSchemes
            (
            );
            /**Sets  the appearance schemes automatic generating
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : studio_render ("UG STUDIO RENDER") */
            public: void SetPrefixAppearanceSchemes
            (
                const NXString & designatorPrefix /** designator prefix */ 
            );
            /**Sets  the appearance schemes automatic generating
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : studio_render ("UG STUDIO RENDER") */
            void SetPrefixAppearanceSchemes
            (
                const char * designatorPrefix /** designator prefix */ 
            );
            /**Returns  the appearance designators name automatic generating
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: NXString PrefixAppearanceDesignators
            (
            );
            /**Sets  the appearance designators name automatic generating
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : studio_render ("UG STUDIO RENDER") */
            public: void SetPrefixAppearanceDesignators
            (
                const NXString & designatorPrefix /** designator prefix */ 
            );
            /**Sets  the appearance designators name automatic generating
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : studio_render ("UG STUDIO RENDER") */
            void SetPrefixAppearanceDesignators
            (
                const char * designatorPrefix /** designator prefix */ 
            );
        }; //lint !e1712 default constructor not defined for class  

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