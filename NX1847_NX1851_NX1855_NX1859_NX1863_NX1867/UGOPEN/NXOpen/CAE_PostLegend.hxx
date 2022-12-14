#ifndef NXOpen_CAE_POSTLEGEND_HXX_INCLUDED
#define NXOpen_CAE_POSTLEGEND_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_PostLegend.ja
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
#include <NXOpen/CAE_PostColorbar.hxx>
#include <NXOpen/CAE_PostHeader.hxx>
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
        class PostLegend;
    }
    namespace CAE
    {
        class PostColorbar;
    }
    namespace CAE
    {
        class PostHeader;
    }
    namespace CAE
    {
        class PostLegendImpl;
        /**  @brief  This class has the information related to post legend.
            This is a placeholder of the whole legend which includes header and colorbar.
             

          <br> An instance of this class can not be created. To obtain the object use @link NXOpen::CAE::Post::PostviewGetLegend NXOpen::CAE::Post::PostviewGetLegend@endlink  method.  <br> 
         <br>  Created in NX1847.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  PostLegend : public NXOpen::TransientObject
        {
            private: PostLegendImpl * m_postlegend_impl;
            /// \cond NX_NO_DOC 
            public: explicit PostLegend(void *ptr);
            /// \endcond 
            /** Gets the colorbar visibility state  @return  
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: bool GetColorbarVisibility
            (
            );
            /** Sets the colorbar visibility state 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: void SetColorbarVisibility
            (
                bool status /** status */ 
            );
            /** Gets the header visibility state  @return  
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: bool GetHeaderVisibility
            (
            );
            /** Sets the header visibility state 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: void SetHeaderVisibility
            (
                bool status /** status */ 
            );
            /** Gets the colorbar object  @return  
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: NXOpen::CAE::PostColorbar * GetColorbar
            (
            );
            /** Sets the colorbar object 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: void SetColorbar
            (
                NXOpen::CAE::PostColorbar * colorbar /** colorbar */ 
            );
            /** Gets the header object  @return  
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: NXOpen::CAE::PostHeader * GetHeader
            (
            );
            /** Sets the header object 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: void SetHeader
            (
                NXOpen::CAE::PostHeader * header /** header */ 
            );
            /** Destroys the Legend object 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: virtual ~PostLegend();
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
