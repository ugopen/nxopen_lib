#ifndef NXOpen_IOMNAME_HXX_INCLUDED
#define NXOpen_IOMNAME_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     IOMName.ja
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
    class IOMName;

    /// \cond NX_NO_DOC 
    /**
    Test interface for interfaces

     <br>  Created in NX3.0.0.  <br>  
    */
    class NXOPENJAMTESTCPPEXPORT  IOMName
    {
        virtual void EnsureVtableExists() {}
        public: virtual ~IOMName() {}

        /// \cond NX_NO_DOC 
        /** Returns the object name  @return  
         <br>  Created in NX3.0.0.  <br>  
         <br> License requirements : None */
        public: virtual NXString GetObjectName
        (
        ) = 0;

        /// \endcond 

        /// \cond NX_NO_DOC 
        /** Compare with  @return  
         <br>  Created in NX3.0.0.  <br>  
         <br> License requirements : None */
        public: virtual bool CompareWith
        (
            NXOpen::IOMName * other /** other */ 
        ) = 0;

        /// \endcond 
    }; //lint !e1712 default constructor not defined for class  


    /// \endcond 
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