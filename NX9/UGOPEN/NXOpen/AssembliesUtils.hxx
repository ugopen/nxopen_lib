#ifndef NXOpen_ASSEMBLIESUTILS_HXX_INCLUDED
#define NXOpen_ASSEMBLIESUTILS_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     AssembliesUtils.ja
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
#include <NXOpen/Assemblies_WaveQuery.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    class AssembliesUtils;
    class Session;
    namespace Assemblies
    {
        class WaveQuery;
    }
    class AssembliesUtilsImpl;
    /** Contains various assembly utility methods  <br> To obtain an instance of this class, refer to @link Session  Session @endlink  <br> 
     <br>  Created in NX6.0.0.  <br>  
    */
    class NXOPENCPPEXPORT  AssembliesUtils
    {
        private: AssembliesUtilsImpl * m_assembliesutils_impl;
        private: NXOpen::Session* m_owner;
        /// \cond NX_NO_DOC 
        public: explicit AssembliesUtils(NXOpen::Session *owner);


        /// \endcond 
        public: 
        /**Returns the tag of this object.  */
        tag_t Tag() const; 
        public: ~AssembliesUtils();
        /** Returns a query utility class  @return  Class to use for wave queries. 
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::Assemblies::WaveQuery * NewWaveQuery
        (
        );
    }; //lint !e1712 default constructor not defined for class  

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