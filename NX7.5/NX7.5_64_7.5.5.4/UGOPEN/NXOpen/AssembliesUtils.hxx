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
namespace NXOpen
{
    class AssembliesUtils;
    class Session;
    namespace Assemblies
    {
        class WaveQuery;
    }
    class AssembliesUtilsImpl;
    /** Contains various assembly utility methods  <br> To obtain an instance of this class, refer to @link Session Session@endlink  <br> */
    class NXOPENCPPEXPORT  AssembliesUtils
    {
        private: AssembliesUtilsImpl * m_assembliesutils_impl;
        private: NXOpen::Session* m_owner;
        /** Constructor */
        public: explicit AssembliesUtils(NXOpen::Session *owner);
        public: 
        /**Returns the tag of this object.  */
        tag_t Tag() const; 
        public: ~AssembliesUtils();
        /** Returns a query utility class  @return  Class to use for wave queries.  <br> License requirements : None */
        public: NXOpen::Assemblies::WaveQuery * NewWaveQuery
        (
        );
    }; //lint !e1712 default constructor not defined for class  

}
#undef EXPORTLIBRARY
#endif
