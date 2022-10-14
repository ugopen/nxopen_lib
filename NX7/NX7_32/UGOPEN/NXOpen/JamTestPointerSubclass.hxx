#ifndef NXOpen_JAMTESTPOINTERSUBCLASS_HXX_INCLUDED
#define NXOpen_JAMTESTPOINTERSUBCLASS_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     JamTestPointerSubclass.ja
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
#include <NXOpen/JamTestPointer.hxx>
#include <NXOpen/libnxopenjamtestcpp_exports.hxx>
namespace NXOpen
{
    class JamTestPointerSubclass;
    class JamTestPointer;
    /**
    Represents a JamTestPointerSubclass.  This is for internal testing only.
    */
    class NXOPENJAMTESTCPPEXPORT JamTestPointerSubclass : public JamTestPointer
    {
        public: explicit JamTestPointerSubclass(void *ptr);
        /**  <br> License requirements : None */
        public: virtual ~JamTestPointerSubclass();
    };
}
#undef EXPORTLIBRARY
#endif