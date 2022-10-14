#ifndef NXOpen_CAE_XYPLOT_DATAEXPORTPARAMETERS_HXX_INCLUDED
#define NXOpen_CAE_XYPLOT_DATAEXPORTPARAMETERS_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_Xyplot_DataExportParameters.ja
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
#include <NXOpen/TransientObject.hxx>
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
            class DataExportParameters;
        }
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
        }
    }
    namespace CAE
    {
        namespace Xyplot
        {
            class DataExportParametersImpl;
            /** Represents the parameters passed to export the data of a plot.  <br> This is an abstract class  <br> 
             <br>  Created in NX1847.0.0.  <br>  
            */
            class NXOPENCPP_CAEEXPORT  DataExportParameters : public NXOpen::TransientObject
            {
                private: DataExportParametersImpl * m_dataexportparameters_impl;
                /// \cond NX_NO_DOC 
                public: explicit DataExportParameters(void *ptr);
                /// \endcond 
                /**Returns  the plot which is being exported. Uses this method when all exported data are in same plot,
                            otherwise uses method @link CAE::Xyplot::DataExportParameters::GetPlots CAE::Xyplot::DataExportParameters::GetPlots@endlink  
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::CAE::Xyplot::Plot * Plot
                (
                );
                /**Sets  the plot which is being exported. Uses this method when all exported data are in same plot,
                            otherwise uses method @link CAE::Xyplot::DataExportParameters::GetPlots CAE::Xyplot::DataExportParameters::GetPlots@endlink  
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : None */
                public: void SetPlot
                (
                    NXOpen::CAE::Xyplot::Plot * plot /** plot */ 
                );
                /** Gets the plots which data is to be exported 
                 <br>  Created in NX1899.0.0.  <br>  
                 <br> License requirements : None */
                public: void GetPlots
                (
                    std::vector<NXOpen::CAE::Xyplot::Plot *> & plots /** plots */ 
                );
                /** Sets the plots which data is to be exported 
                 <br>  Created in NX1899.0.0.  <br>  
                 <br> License requirements : None */
                public: void SetPlots
                (
                    const std::vector<NXOpen::CAE::Xyplot::Plot *> & plots /** plots */ 
                );
                /** Gets the data index vector of the plot. 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : None */
                public: std::vector<int> GetRecordIndices
                (
                );
                /** Sets the plot data index vector 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : None */
                public: void SetRecordIndices
                (
                    const std::vector<int> & plotDataIndices /** plotdataindices */ 
                );
                /** Destroys the object 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : None */
                public: virtual ~DataExportParameters();
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