#ifndef NXOpen_SELECTIONHANDLE_HXX_INCLUDED
#define NXOpen_SELECTIONHANDLE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     SelectionHandle.ja
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
#include <NXOpen/libnxopenuicpp_exports.hxx>
namespace NXOpen
{
    class SelectionHandle;
    /** Represents a SelectionHandle for UI Styler */
    class NXOPENUICPPEXPORT SelectionHandle : public TransientObject
    {
        public: explicit SelectionHandle(void *ptr);
        /** Free resources associated with the instance. After this method
            is called, it is illegal to use the object.  In .NET or Java, this 
            method is automatically called when the object is deleted by the 
            garbage collector.  <br> License requirements : None */
        public: virtual ~SelectionHandle();
    };
}
#undef EXPORTLIBRARY
#endif
