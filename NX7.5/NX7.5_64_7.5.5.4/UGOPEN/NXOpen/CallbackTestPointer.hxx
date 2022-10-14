#ifndef NXOpen_CALLBACKTESTPOINTER_HXX_INCLUDED
#define NXOpen_CALLBACKTESTPOINTER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CallbackTestPointer.ja
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
#include <NXOpen/TransientObject.hxx>
#include <NXOpen/libnxopendebugsessioncpp_exports.hxx>
namespace NXOpen
{
    class CallbackTestPointer;
    class CallbackTestPointerImpl;
    /**
    Represents a CallbackTestPointer.  This is for internal testing only.
    */
    class NXOPENDEBUGSESSIONCPPEXPORT  CallbackTestPointer : public TransientObject
    {
        private: CallbackTestPointerImpl * m_callbacktestpointer_impl;
        public: explicit CallbackTestPointer(void *ptr);
        /**Returns   <br> License requirements : None */
        public: NXString Name
        (
        );
        /**  <br> License requirements : None */
        public: virtual ~CallbackTestPointer();
    }; //lint !e1712 default constructor not defined for class  

}
#undef EXPORTLIBRARY
#endif