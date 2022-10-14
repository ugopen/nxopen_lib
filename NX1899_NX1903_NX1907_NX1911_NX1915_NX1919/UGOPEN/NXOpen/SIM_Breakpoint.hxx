#ifndef NXOpen_SIM_BREAKPOINT_HXX_INCLUDED
#define NXOpen_SIM_BREAKPOINT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     SIM_Breakpoint.ja
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
#include <NXOpen/NXObject.hxx>
#include <NXOpen/libnxopencpp_sim_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace SIM
    {
        class Breakpoint;
    }
    class NXObject;
    namespace SIM
    {
        class _BreakpointBuilder;
        class BreakpointImpl;
        /**  @brief  Represents the Breakpoint class object  

            <br> Use the @link NXOpen::SIM::NcProgramManagerBuilder NXOpen::SIM::NcProgramManagerBuilder@endlink  class to create a Breakpoint object.  <br> 
         <br>  Created in NX11.0.0.  <br>  
        */
        class NXOPENCPP_SIMEXPORT  Breakpoint : public NXOpen::NXObject
        {
            private: BreakpointImpl * m_breakpoint_impl;
            private: friend class  _BreakpointBuilder;
            protected: Breakpoint();
            public: ~Breakpoint();
            /** Activate the breakpoint. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") */
            public: void Activate
            (
            );
            /** Deactivate the breakpoint. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") */
            public: void Deactivate
            (
            );
            /** Delete the breakpoint. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") */
            public: void Delete
            (
            );
            /**Returns  the condition for a breakpoint. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: NXString Condition
            (
            );
            /**Sets  the condition for a breakpoint. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") */
            public: void SetCondition
            (
                const NXString & condition /** The condition of the breakpoint. */
            );
            /**Sets  the condition for a breakpoint. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") */
            void SetCondition
            (
                const char * condition /** The condition of the breakpoint. */
            );
        };
    }
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