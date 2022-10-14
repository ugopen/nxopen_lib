#ifndef NXOpen_JAMTESTPOINTER_HXX_INCLUDED
#define NXOpen_JAMTESTPOINTER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     JamTestPointer.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/TransientObject.hxx>
#include <NXOpen/libnxopenjamtestcpp_exports.hxx>
namespace NXOpen
{
    class JamTestPointer;
    /**
    Represents a JamTestPointer.  This is for internal testing only.
    */
    class NXOPENJAMTESTCPPEXPORT JamTestPointer : public TransientObject
    {
        public: explicit JamTestPointer(void *ptr);
        /**Returns   <br> License requirements : None */
        public: NXString Name
        (
        );
        /** <b>Deprecated</b>:<br>
        &nbsp;&nbsp;&nbsp;Use @link Name() Name@endlink instead.
        @deprecated
        */
        public: NXString GetName
        (
        ) { return this->Name(); }
        /**  <br> License requirements : None */
        public: virtual ~JamTestPointer();
    };
}
#undef EXPORTLIBRARY
#endif