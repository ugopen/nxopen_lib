#ifndef NXOpen_JAMTESTNAMESPACE_NOTATAGGEDOBJECT_HXX_INCLUDED
#define NXOpen_JAMTESTNAMESPACE_NOTATAGGEDOBJECT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     JamTestNamespace_NotATaggedObject.ja
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
#include <NXOpen/libnxopenjamtestcpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace JamTestNamespace
    {
        class NotATaggedObject;
    }
    namespace JamTestNamespace
    {
        class _NotATaggedObjectBuilder;
        class NotATaggedObjectImpl;
        /**
             This is for internal testing only.
             <br> TEST CLASS  <br> 
         <br>  Created in NX2007.0.0.  <br>  
        */
        class NXOPENJAMTESTCPPEXPORT  NotATaggedObject : public NXOpen::TaggedObject
        {
            private: NotATaggedObjectImpl * m_notataggedobject_impl;
            private: friend class  _NotATaggedObjectBuilder;
            protected: NotATaggedObject();
            public: ~NotATaggedObject();
            /**Returns  the something something darkside 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: bool Status
            (
            );
        };
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