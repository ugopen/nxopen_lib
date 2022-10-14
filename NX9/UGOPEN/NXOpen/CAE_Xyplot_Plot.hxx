#ifndef NXOpen_CAE_XYPLOT_PLOT_HXX_INCLUDED
#define NXOpen_CAE_XYPLOT_PLOT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_Xyplot_Plot.ja
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
#include <NXOpen/CAE_Xyplot_BaseTemplate.hxx>
#include <NXOpen/CAE_Xyplot_Plot.hxx>
#include <NXOpen/NXObject.hxx>
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
            class Plot;
        }
    }
    namespace CAE
    {
        namespace Xyplot
        {
            class BaseTemplate;
        }
    }
    class NXObject;
    namespace CAE
    {
        namespace Xyplot
        {
            class _PlotBuilder;
            class PlotImpl;
            /** Manages the plot template  <br> Not support KF.  <br> 
             <br>  Created in NX7.5.0.  <br>  
            */
            class NXOPENCPP_CAEEXPORT  Plot : public NXObject
            {
                private: PlotImpl * m_plot_impl;
                private: friend class  _PlotBuilder;
                protected: Plot();
                public: ~Plot();
                /**Returns  the plot template 
                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : nx_ftk ("NX Advanced Graphing") */
                public: NXOpen::CAE::Xyplot::BaseTemplate * Template
                (
                );
                /** Returns the count of plotted records on the plot graph.  @return  Record count 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: int GetRecordCount
                (
                );
                /** Saves a plotted record on the plot graph to an afu file.
                                Use @link CAE::AfuManager::CreateRecord CAE::AfuManager::CreateRecord@endlink  to create the record. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_ftk ("NX Advanced Graphing") */
                public: void SaveRecord
                (
                    int recordIndex /** the index of record to be saved */,
                    const NXString & afuFileName /** Afu file name   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                    const NXString & recordName /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
                );
                /** Saves a plotted record on the plot graph to an afu file.
                                Use @link CAE::AfuManager::CreateRecord CAE::AfuManager::CreateRecord@endlink  to create the record. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_ftk ("NX Advanced Graphing") */
                void SaveRecord
                (
                    int recordIndex /** the index of record to be saved */,
                    const char * afuFileName /** Afu file name   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                    const char * recordName /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
                );
                /** Gets the window device and view index of the plot graph.  @return  the device of window 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_ftk ("NX Advanced Graphing") */
                public: int GetDeviceAndViewIndex
                (
                    int* viewIndex /** the index of view */
                );
            };
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