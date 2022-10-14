#ifndef NXOpen_FTTESTDEBUGSESSIONELEMENT_HXX_INCLUDED
#define NXOpen_FTTESTDEBUGSESSIONELEMENT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     FTTestDebugSessionElement.ja
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
#include <NXOpen/libnxopendebugsessioncpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    class FTTestDebugSessionElement;
    class FTTestDebugSession;
    class FTTestDebugSessionElementImpl;

    /// \cond NX_NO_DOC 
    /** Represents a class that is used for Feature Toggle Autotest.  This class should not
    be made available to customers  <br> To obtain an instance of this class, refer to @link NXOpen::FTTestDebugSession  NXOpen::FTTestDebugSession @endlink  <br> 
     <br>  Created in NX1847.0.0.  <br>  
    */
    class NXOPENDEBUGSESSIONCPPEXPORT  FTTestDebugSessionElement
    {
        private: FTTestDebugSessionElementImpl * m_fttestdebugsessionelement_impl;
        private: NXOpen::FTTestDebugSession* m_owner;
        /// \cond NX_NO_DOC 
        public: explicit FTTestDebugSessionElement(NXOpen::FTTestDebugSession *owner);


        /// \endcond 
        public: 
        /**Returns the tag of this object.  */
        tag_t Tag() const; 
        public: ~FTTestDebugSessionElement();

        /// \cond NX_NO_DOC 
        /** Test API  @return <O> true if file this API is executed
         <br>  Created in NX1847.0.0.  <br>  
         <br> License requirements : None */
        public: bool ExecuteFtProtectedClassApi
        (
        );

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