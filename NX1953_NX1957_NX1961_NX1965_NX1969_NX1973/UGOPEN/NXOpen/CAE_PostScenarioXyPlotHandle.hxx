#ifndef NXOpen_CAE_POSTSCENARIOXYPLOTHANDLE_HXX_INCLUDED
#define NXOpen_CAE_POSTSCENARIOXYPLOTHANDLE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_PostScenarioXyPlotHandle.ja
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
#include <NXOpen/CAE_Xyplot_Plot.hxx>
#include <NXOpen/CAE_Xyplot_ResultAccessor.hxx>
#include <NXOpen/CAE_PostScenarioPlotHandle.hxx>
#include <NXOpen/libnxopencpp_cae_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace CAE
    {
        class PostScenarioXyPlotHandle;
    }
    namespace CAE
    {
        class PostScenarioPlotHandle;
    }
    namespace CAE
    {
        namespace Xyplot
        {
            class Plot;
        }
    }
    namespace CAE
    {
        namespace Xyplot
        {
            class ResultAccessor;
        }
    }
    namespace CAE
    {
        class _PostScenarioXyPlotHandleBuilder;
        class PostScenarioXyPlotHandleImpl;
        /**  @brief  Handle to an XY Plot created as visualization for a @link NXOpen::CAE::PostScenario NXOpen::CAE::PostScenario@endlink .  

           <br> Use @link NXOpen::CAE::PostScenario::Plots NXOpen::CAE::PostScenario::Plots@endlink  to access instances of this class.  <br> 
         <br>  Created in NX1899.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  PostScenarioXyPlotHandle : public NXOpen::CAE::PostScenarioPlotHandle
        {
            private: PostScenarioXyPlotHandleImpl * m_postscenarioxyplothandle_impl;
            private: friend class  _PostScenarioXyPlotHandleBuilder;
            protected: PostScenarioXyPlotHandle();
            public: ~PostScenarioXyPlotHandle();
            /**Returns  the @link CAE::Xyplot::Plot CAE::Xyplot::Plot@endlink .
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::Xyplot::Plot * XyPlot
            (
            );
            /**Returns  the index of the Canvas within the plot. 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: int CanvasIndex
            (
            );
            /** Shortcut to create a @link CAE::Xyplot::ResultAccessor CAE::Xyplot::ResultAccessor@endlink  directly on this plot. 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::Xyplot::ResultAccessor * CreateResultAccessor
            (
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