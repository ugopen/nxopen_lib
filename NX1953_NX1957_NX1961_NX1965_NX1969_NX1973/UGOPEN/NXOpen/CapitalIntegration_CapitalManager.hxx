#ifndef NXOpen_CAPITALINTEGRATION_CAPITALMANAGER_HXX_INCLUDED
#define NXOpen_CAPITALINTEGRATION_CAPITALMANAGER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CapitalIntegration_CapitalManager.ja
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
#include <NXOpen/libnxopencpp_capitalintegration_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace CapitalIntegration
    {
        class CapitalManager;
    }
    class Session;
    namespace CapitalIntegration
    {
        class CapitalQueryObserver;
    }
    namespace CapitalIntegration
    {
        class CapitalManagerImpl;
        /** Represents a manager of capitalintegration objects  <br> To obtain an instance of this class, refer to @link NXOpen::Session  NXOpen::Session @endlink  <br> 
         <br>  Created in NX1872.0.0.  <br>  
        */
        class NXOPENCPP_CAPITALINTEGRATIONEXPORT  CapitalManager
        {
            private: CapitalManagerImpl * m_capitalmanager_impl;
            private: NXOpen::Session* m_owner;
            /// \cond NX_NO_DOC 
            public: explicit CapitalManager(NXOpen::Session *owner);


            /// \endcond 
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            private: static CapitalManager* theCapitalManager;
            /** Returns the CapitalManager object for the running session which serves as the 'gateway' class for the application API.  
                References to all other objects in this API are obtained either directly or indirectly via methods and properties on this class.  
                Platform Session should be initialized using 'GetSession' method from NXOpen API prior to this call.  
            */
            public: static CapitalManager* GetCapitalManager(NXOpen::Session *owner);
            public: ~CapitalManager();


            /** Returns the @link NXOpen::CapitalIntegration::CapitalQueryObserver NXOpen::CapitalIntegration::CapitalQueryObserver@endlink  belonging to this session 
             <br>  Created in NX1872.0.0.  <br>  
            */
            public: NXOpen::CapitalIntegration::CapitalQueryObserver *OnQueryObserver();
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
