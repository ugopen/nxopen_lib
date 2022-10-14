#ifndef NXOpen_CAE_XYPLOT_PLOTPARAMETERS_HXX_INCLUDED
#define NXOpen_CAE_XYPLOT_PLOTPARAMETERS_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_Xyplot_PlotParameters.ja
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
#include <NXOpen/CAE_XyplotDataTypes.hxx>
#include <NXOpen/CAE_Xyplot_BaseTemplate.hxx>
#include <NXOpen/CAE_Xyplot_PlotGraphTemplate.hxx>
#include <NXOpen/CAE_Xyplot_BasePlotParameters.hxx>
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
        namespace Xyplot
        {
            class PlotParameters;
        }
    }
    namespace CAE
    {
        namespace Xyplot
        {
            class BasePlotParameters;
        }
    }
    namespace CAE
    {
        namespace Xyplot
        {
            class BaseTemplate;
        }
    }
    namespace CAE
    {
        namespace Xyplot
        {
            class PlotGraphTemplate;
        }
    }
    namespace CAE
    {
        namespace Xyplot
        {
        }
    }
    namespace CAE
    {
        namespace Xyplot
        {
            class PlotParametersImpl;
            /** Represents the parameters passed to create a plot.  <br> To create a new instance of this class, use @link NXOpen::CAE::Xyplot::XYPlotManager::NewPlotParameters  NXOpen::CAE::Xyplot::XYPlotManager::NewPlotParameters @endlink  <br> 
             <br>  Created in NX9.0.0.  <br>  
            */
            class NXOPENCPP_CAEEXPORT  PlotParameters : public NXOpen::CAE::Xyplot::BasePlotParameters
            {
                private: PlotParametersImpl * m_plotparameters_impl;
                /// \cond NX_NO_DOC 
                public: explicit PlotParameters(void *ptr);
                /// \endcond 
                /**Returns  the graph template to be used by the plot 
                 <br>  @deprecated Deprecated in NX10.0.0.  Use @link CAE::Xyplot::PlotParameters::PlotTemplate CAE::Xyplot::PlotParameters::PlotTemplate@endlink  instead. <br>  

                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public:  NX_DEPRECATED("Deprecated in NX10.0.0.  Use CAE::Xyplot::PlotParameters::PlotTemplate instead.") NXOpen::CAE::Xyplot::BaseTemplate * GraphTemplate
                (
                );
                /**Returns  the plot template to be used by the plot 
                 <br>  Created in NX10.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::CAE::Xyplot::PlotGraphTemplate * PlotTemplate
                (
                );
                /**Returns  the value indicates whether to create a 2D plot 
                 <br>  @deprecated Deprecated in NX10.0.0.  Use @link CAE::Xyplot::PlotParameters::PlotType CAE::Xyplot::PlotParameters::PlotType@endlink  instead. <br>  

                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public:  NX_DEPRECATED("Deprecated in NX10.0.0.  Use CAE::Xyplot::PlotParameters::PlotType instead.") bool Is2DPlot
                (
                );
                /**Sets  the value indicates whether to create a 2D plot 
                 <br>  @deprecated Deprecated in NX10.0.0.  Use @link CAE::Xyplot::PlotParameters::SetPlotType CAE::Xyplot::PlotParameters::SetPlotType@endlink  instead. <br>  

                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public:  NX_DEPRECATED("Deprecated in NX10.0.0.  Use CAE::Xyplot::PlotParameters::SetPlotType instead.") void SetIs2DPlot
                (
                    bool is2DPlot /** is2dplot */ 
                );
                /**Returns  the plot type 
                 <br>  Created in NX10.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::CAE::Xyplot::PlotType PlotType
                (
                );
                /**Sets  the plot type 
                 <br>  Created in NX10.0.0.  <br>  
                 <br> License requirements : None */
                public: void SetPlotType
                (
                    NXOpen::CAE::Xyplot::PlotType plotType /** plottype */ 
                );
            }; //lint !e1712 default constructor not defined for class  

        }
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