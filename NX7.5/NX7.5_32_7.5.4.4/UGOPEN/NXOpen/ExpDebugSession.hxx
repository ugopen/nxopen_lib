#ifndef NXOpen_EXPDEBUGSESSION_HXX_INCLUDED
#define NXOpen_EXPDEBUGSESSION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     ExpDebugSession.ja
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
namespace NXOpen
{
    class ExpDebugSession;
    class DebugSession;
    class ExpDebugSessionImpl;
    /** Represents a class that is used for NX testing.  This class should not
    be made available to customers  <br> To obtain an instance of this class, refer to @link DebugSession DebugSession@endlink  <br> */
    class NXOPENDEBUGSESSIONCPPEXPORT  ExpDebugSession
    {
        private: ExpDebugSessionImpl * m_expdebugsession_impl;
        private: NXOpen::DebugSession* m_owner;
        /** Constructor */
        public: explicit ExpDebugSession(NXOpen::DebugSession *owner);
        public: 
        /**Returns the tag of this object.  */
        tag_t Tag() const; 
        public: ~ExpDebugSession();
        /** Print all expressions in session  <br> License requirements : None */
        public: void PrintAllExpsInSession
        (
        );
    }; //lint !e1712 default constructor not defined for class  

}
#undef EXPORTLIBRARY
#endif
