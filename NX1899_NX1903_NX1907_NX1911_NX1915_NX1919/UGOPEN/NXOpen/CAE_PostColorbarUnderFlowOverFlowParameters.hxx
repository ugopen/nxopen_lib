#ifndef NXOpen_CAE_POSTCOLORBARUNDERFLOWOVERFLOWPARAMETERS_HXX_INCLUDED
#define NXOpen_CAE_POSTCOLORBARUNDERFLOWOVERFLOWPARAMETERS_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_PostColorbarUnderFlowOverFlowParameters.ja
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
        class PostColorbarUnderFlowOverFlowParameters;
    }
    class NXColor;
    namespace CAE
    {
        class PostColorbarUnderFlowOverFlowParametersImpl;
        /**  @brief  This class has the information related to post colorbar underflow overflow values.
             

          <br> An instance of this class can not be created. To obtain the object use @link NXOpen::CAE::PostColorbar::GetUnderFlowOverFlowParameters NXOpen::CAE::PostColorbar::GetUnderFlowOverFlowParameters@endlink  method.  <br> 
         <br>  Created in NX1847.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  PostColorbarUnderFlowOverFlowParameters : public NXOpen::TransientObject
        {
            /** Colorbar drawing methods for overflow and under flor values */
            public: enum LimitDisplay
            {
                LimitDisplayNone/** none */ ,
                LimitDisplayShaded/** shaded */ ,
                LimitDisplayTranslucent/** translucent */ ,
                LimitDisplayClipped/** clipped */ 
            };

            private: PostColorbarUnderFlowOverFlowParametersImpl * m_postcolorbarunderflowoverflowparameters_impl;
            /// \cond NX_NO_DOC 
            public: explicit PostColorbarUnderFlowOverFlowParameters(void *ptr);
            /// \endcond 
            /** Gets the overflow above color value for the colorbar.
                    This denotes the color id to draw the result values above the maximum value in the colorbar range. @return  
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: NXOpen::NXColor * GetOverflowAboveColor
            (
            );
            /** Sets the overflow above color value for the colorbar.
                    This denotes the color id to draw the result values above the maximum value in the colorbar range. 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: void SetOverflowAboveColor
            (
                NXOpen::NXColor * colorId /** color id */ 
            );
            /** Gets the underflow below color value for the colorbar.
                    This denotes the color id to draw the result values below the minimum value in the colorbar range. @return  
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: NXOpen::NXColor * GetUnderflowBelowColor
            (
            );
            /** Sets the underflow below color value for the colorbar.
                    This denotes the color id to draw the result values below the minimum value in the colorbar range.
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: void SetUnderflowBelowColor
            (
                NXOpen::NXColor * colorId /** color id */ 
            );
            /** Gets the overflow limit display style for the colorbar  @return  
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: NXOpen::CAE::PostColorbarUnderFlowOverFlowParameters::LimitDisplay GetOverflowDisplayStyle
            (
            );
            /** Sets the overflow limit display style for the colorbar 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: void SetOverflowDisplayStyle
            (
                NXOpen::CAE::PostColorbarUnderFlowOverFlowParameters::LimitDisplay overflow /** overflow */ 
            );
            /** Gets the underflow limit display style for the colorbar  @return  
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: NXOpen::CAE::PostColorbarUnderFlowOverFlowParameters::LimitDisplay GetUnderflowDisplayStyle
            (
            );
            /** Sets the underflow limit display style for the colorbar 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: void SetUnderflowDisplayStyle
            (
                NXOpen::CAE::PostColorbarUnderFlowOverFlowParameters::LimitDisplay underflow /** underflow */ 
            );
            /** Gets the overflow limit display visibility state for the colorbar and postview @return  
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: bool GetOverflowAboveVisibility
            (
            );
            /** Sets the overflow limit display visibility state for the colorbar and postview 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: void SetOverflowAboveVisibility
            (
                bool showoverflowabove /** showoverflowabove */ 
            );
            /** Gets the underflow limit display visibility state for the colorbar and postview  @return  
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: bool GetUnderflowBelowVisibility
            (
            );
            /** Sets the underflow limit display visibility state for the colorbar and postview 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: void SetUnderflowBelowVisibility
            (
                bool showunderflowbelow /** showunderflowbelow */ 
            );
            /** Destroys the object 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: virtual ~PostColorbarUnderFlowOverFlowParameters();
        }; //lint !e1712 default constructor not defined for class  

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