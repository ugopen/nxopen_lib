#ifndef NXOpen_CAE_XYPLOT_I3DDATAPLOT_HXX_INCLUDED
#define NXOpen_CAE_XYPLOT_I3DDATAPLOT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_Xyplot_I3DDataPlot.ja
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
#include <NXOpen/CAE_FTK_BaseRecord.hxx>
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
            class I3DDataPlot;
        }
    }
    namespace CAE
    {
        namespace FTK
        {
            class BaseRecord;
        }
    }
    namespace CAE
    {
        namespace Xyplot
        {
            /**  @brief  Represents a plot interface which input is 3D data 

             
                    
                    3D plot data can consist of multiple @link CAE::FTK::ArrayRecord2D CAE::FTK::ArrayRecord2D@endlink  or a @link CAE::FTK::SectionBasedMatrixRecord CAE::FTK::SectionBasedMatrixRecord@endlink 
                    To the plot class which implements this interface, all input records will be represented as a whole data.
                    
                    
             <br>  Created in NX12.0.0.  <br>  
            */
            class NXOPENCPP_CAEEXPORT  I3DDataPlot
            {
                virtual void EnsureVtableExists() {}
                public: virtual ~I3DDataPlot() {}
                /**  @brief Edits records of plot.  

                 
                            
                             <br> 
                            <b> Procedure of editing records of plot fully:</b>
                            <ol>
                            <li>Call this method to edit record data</li>
                            <li>Call @link CAE::Xyplot::Plot::CommitRecordsChange CAE::Xyplot::Plot::CommitRecordsChange@endlink  to precess record data change and update data model</li>
                            <li>Call @link CAE::Xyplot::IDisplayableModel::UpdateDisplay CAE::Xyplot::IDisplayableModel::UpdateDisplay@endlink  to regenerate display to reflect data change</li>
                            <li>Optionally call @link CAE::Xyplot::Plot::FitView CAE::Xyplot::Plot::FitView@endlink  to make display fit the view;it is only required when the plot display boundary is changed</li>
                            </ol>
                             <br> 
                            
                            
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: virtual void EditRecords
                (
                    const std::vector<NXOpen::CAE::FTK::BaseRecord *> & records /** records */ 
                ) = 0;
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
