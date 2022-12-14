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
        class Breakpoint;
    }
    namespace SIM
    {
        class _NcProgramBuilder;
        class NcProgramImpl;
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
             <br>  @deprecated Deprecated in NX12.0.0.  Use @link SIM::NcProgram::InsertBreakpoint SIM::NcProgram::InsertBreakpoint@endlink  instead which returns the added Breakpoint. <br>  

             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") */
            public: NX_DEPRECATED("Deprecated in NX12.0.0.  Use SIM::NcProgram::InsertBreakpoint instead which returns the added Breakpoint.") void AddBreakpoint
            (
                int line /** The line number of the breakpoint (zero based). */
            );
            /** Add a breakpoint. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") */
            public: NXOpen::SIM::Breakpoint * InsertBreakpoint
            (
                int line /** The line number of the breakpoint (zero based). */
            );
            /** Export program to file. 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") */
            public: void Export
            (
                const NXString & file /** The file to be exported to */
            );
            /** Export program to file. 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") */
            void Export
            (
                const char * file /** The file to be exported to */
            );
            /** Get the line content of a specific line number.  @return  The content of the specific line 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") */
            public: NXString GetLine
            (
                int line /** the line number of the program (zero based) */
            );

            /// \cond NX_NO_DOC 
            /** Postprocess all lines of this program. 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") */
            public: void PostAllLines
            (
            );

            /// \endcond 
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
