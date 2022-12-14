#ifndef NXOpen_MFG_AM_SUPPORTLIBRARY_HXX_INCLUDED
#define NXOpen_MFG_AM_SUPPORTLIBRARY_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Mfg_AM_SupportLibrary.ja
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
#include <NXOpen/Mfg_AM_Library.hxx>
#include <NXOpen/libmfgamopencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Mfg
    {
        namespace AM
        {
            class SupportLibrary;
        }
    }
    namespace Mfg
    {
        namespace AM
        {
            class Library;
        }
    }
    namespace Mfg
    {
        namespace AM
        {
            class ProfileSupport;
        }
    }
    namespace Mfg
    {
        namespace AM
        {
            class _SupportLibraryBuilder;
            class SupportLibraryImpl;
            /** Interface for Services Support Library objects  <br> To obtain an instance of this class use @link NXOpen::Mfg::AM::SupportLibrary NXOpen::Mfg::AM::SupportLibrary@endlink .  <br> 
             <br>  @deprecated Deprecated in NX1953.0.0.  Use @link SupportProfile SupportProfile@endlink  instead. <br>  

             <br>  Created in NX1847.0.0.  <br>  
            */
            class NX_DEPRECATED("Deprecated in NX1953.0.0.  Use SupportProfile instead.") MFGAMOPENCPPEXPORT  SupportLibrary : public NXOpen::Mfg::AM::Library
            {
                private: SupportLibraryImpl * m_supportlibrary_impl;
                private: friend class  _SupportLibraryBuilder;
                protected: SupportLibrary();
                public: ~SupportLibrary();
                /** Adds a support profile  @return  the new support profile 
                 <br>  @deprecated Deprecated in NX1953.0.0.  Use @link SupportProfile SupportProfile@endlink  instead. <br>  

                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : None */
                public: NX_DEPRECATED("Deprecated in NX1953.0.0.  Use SupportProfile instead.") NXOpen::Mfg::AM::ProfileSupport * AddSupportProfile
                (
                );
            };
        }
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
