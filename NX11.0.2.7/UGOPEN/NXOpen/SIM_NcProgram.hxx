#ifndef NXOpen_SIM_NCPROGRAM_HXX_INCLUDED
#define NXOpen_SIM_NCPROGRAM_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     SIM_NcProgram.ja
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
        class NcProgram;
    }
    class NXObject;
    namespace SIM
    {
        class _NcProgramBuilder;
        class NcProgramImpl;

        /// \cond NX_NO_DOC 
        /**  @brief  Represents the NcProgram class object  

            <br> Use the @link NXOpen::SIM::NcProgramManagerBuilder NXOpen::SIM::NcProgramManagerBuilder@endlink  class to create a NcProgram object.  <br> 
         <br>  Created in NX11.0.0.  <br>  
        */
        class NXOPENCPP_SIMEXPORT  NcProgram : public NXOpen::NXObject
        {
            private: NcProgramImpl * m_ncprogram_impl;
            private: friend class  _NcProgramBuilder;
            protected: NcProgram();
            public: ~NcProgram();
            /** Add a breakpoint. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") */
            public: void AddBreakpoint
            (
                int line /** The line number of the breakpoint (zero based). */
            );
        };

        /// \endcond 
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
