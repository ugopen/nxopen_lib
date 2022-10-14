#ifndef NXOpen_APPEARANCE_APPEARANCEMANAGER_HXX_INCLUDED
#define NXOpen_APPEARANCE_APPEARANCEMANAGER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Appearance_AppearanceManager.ja
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
#include <NXOpen/ErrorList.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_appearance_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Appearance
    {
        class AppearanceManager;
    }
    class Part;
    namespace Appearance
    {
        class AppearanceDesignatorBuilder;
    }
    namespace Appearance
    {
        class AppearanceEditTexture;
    }
    namespace Appearance
    {
        class AppearanceSchemeBuilder;
    }
    class ErrorList;
    namespace Appearance
    {
        class AppearanceManagerImpl;
        /** Represents an object that manages Appearance application specific objects.  <br> To obtain an instance of this class, refer to @link NXOpen::Part  NXOpen::Part @endlink  <br> 
         <br>  Created in NX1899.0.0.  <br>  
        */
        class NXOPENCPP_APPEARANCEEXPORT  AppearanceManager
        {
            private: AppearanceManagerImpl * m_appearancemanager_impl;
            private: NXOpen::Part* m_owner;
            /// \cond NX_NO_DOC 
            public: explicit AppearanceManager(NXOpen::Part *owner);


            /// \endcond 
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~AppearanceManager();
            /** Creates a @link NXOpen::Appearance::AppearanceDesignatorBuilder NXOpen::Appearance::AppearanceDesignatorBuilder@endlink  object 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : appearance_mgmt (" AppearanceManagement Author for Native mode") OR appearance_mgmt_mgd (" AppearanceManagement Author for Managed mode") */
            public: NXOpen::Appearance::AppearanceDesignatorBuilder * CreateAppearanceDesignatorBuilder
            (
                const NXString & schemeName /** schemename */ 
            );
            /** Creates a @link NXOpen::Appearance::AppearanceDesignatorBuilder NXOpen::Appearance::AppearanceDesignatorBuilder@endlink  object 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : appearance_mgmt (" AppearanceManagement Author for Native mode") OR appearance_mgmt_mgd (" AppearanceManagement Author for Managed mode") */
            NXOpen::Appearance::AppearanceDesignatorBuilder * CreateAppearanceDesignatorBuilder
            (
                const char * schemeName /** schemename */ 
            );
            /** Creates a @link NXOpen::Appearance::AppearanceEditTexture NXOpen::Appearance::AppearanceEditTexture@endlink  object 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : appearance_mgmt (" AppearanceManagement Author for Native mode") OR appearance_mgmt_mgd (" AppearanceManagement Author for Managed mode") */
            public: NXOpen::Appearance::AppearanceEditTexture * CreateAppearanceEditTextureBuilder
            (
                const NXString & designatorName /** designatorname */ ,
                const NXString & schemeName /** schemename */ 
            );
            /** Creates a @link NXOpen::Appearance::AppearanceEditTexture NXOpen::Appearance::AppearanceEditTexture@endlink  object 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : appearance_mgmt (" AppearanceManagement Author for Native mode") OR appearance_mgmt_mgd (" AppearanceManagement Author for Managed mode") */
            NXOpen::Appearance::AppearanceEditTexture * CreateAppearanceEditTextureBuilder
            (
                const char * designatorName /** designatorname */ ,
                const char * schemeName /** schemename */ 
            );
            /** Creates a @link NXOpen::Appearance::AppearanceSchemeBuilder NXOpen::Appearance::AppearanceSchemeBuilder@endlink  
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : appearance_mgmt (" AppearanceManagement Author for Native mode") OR appearance_mgmt_mgd (" AppearanceManagement Author for Managed mode") */
            public: NXOpen::Appearance::AppearanceSchemeBuilder * CreateAppearanceSchemeBuilder
            (
            );
            /** This function will set the input product assembly which has the appearance data @return  Any errors that occurred. 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : studio_visualize ("STUDIO VISUALIZE") */
            public: NXOpen::ErrorList * SetProductAssembly
            (
                const NXString & productAssembly /** productassembly */ 
            );
            /** This function will set the input product assembly which has the appearance data @return  Any errors that occurred. 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : studio_visualize ("STUDIO VISUALIZE") */
            NXOpen::ErrorList * SetProductAssembly
            (
                const char * productAssembly /** productassembly */ 
            );
            /** This function will do full unload of appearance schemes present in session  @return  Any errors that occurred. 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : studio_visualize ("STUDIO VISUALIZE") */
            public: NXOpen::ErrorList * UnloadAllAppearanceData
            (
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