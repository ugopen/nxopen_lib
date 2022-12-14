#ifndef NXOpen_WINDOWHANDLE_HXX_INCLUDED
#define NXOpen_WINDOWHANDLE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     WindowHandle.ja
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
#include <NXOpen/libnxopenuicpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    class WindowHandle;
    class WindowHandleImpl;
    /** Represent a window handle.
        For the resource bar, it represents the docking window handle. 

     <br>  Created in NX10.0.0.  <br>  
    */
    class NXOPENUICPPEXPORT  WindowHandle : public NXOpen::TransientObject
    {
        private: WindowHandleImpl * m_windowhandle_impl;
        /// \cond NX_NO_DOC 
        public: explicit WindowHandle(void *ptr);
        /// \endcond 
        /** Free resources associated with the instance. After this method
                is called, it is illegal to use the object.  In .NET or Java, this 
                method is automatically called when the object is deleted by the 
                garbage collector. 
         <br>  Created in NX10.0.0.  <br>  
         <br> License requirements : None */
        public: virtual ~WindowHandle();
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
