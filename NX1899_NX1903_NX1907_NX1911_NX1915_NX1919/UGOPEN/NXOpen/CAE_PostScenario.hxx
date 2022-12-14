#ifndef NXOpen_CAE_POSTSCENARIO_HXX_INCLUDED
#define NXOpen_CAE_POSTSCENARIO_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_PostScenario.ja
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
#include <NXOpen/CAE_PostScenarioAction.hxx>
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
        class PostScenario;
    }
    namespace CAE
    {
        class PostScenarioAction;
    }
    namespace CAE
    {
        class PostScenarioPlotHandleCollection;
    }
    class NXObject;
    namespace CAE
    {
        class _PostScenarioBuilder;
        class PostScenarioImpl;
        /**  @brief  This class represents a @link NXOpen::CAE::PostScenario NXOpen::CAE::PostScenario@endlink . The lifetime of this object is managed internally, so you should not delete this type of object. 

           <br> No support for KF.  <br> 
         <br>  Created in NX12.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  PostScenario : public NXOpen::NXObject
        {
            private: PostScenarioImpl * m_postscenario_impl;
            private: friend class  _PostScenarioBuilder;
            protected: PostScenario();
            public: ~PostScenario();
            /** Get a list of available workflow actions that can be invoked on this scenario. These can be invoked with @link NXOpen::CAE::PostScenarioAction::Invoke NXOpen::CAE::PostScenarioAction::Invoke@endlink 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXOpen::CAE::PostScenarioAction *> GetAvailableActions
            (
            );
            /** Get a workflow action by name that can be invoked on this scenario. These can be invoked with @link NXOpen::CAE::PostScenarioAction::Invoke NXOpen::CAE::PostScenarioAction::Invoke@endlink 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::PostScenarioAction * GetActionByName
            (
                const NXString & subvisualization /** subvisualization */ ,
                const NXString & name /** name */ 
            );
            /** Get a workflow action by name that can be invoked on this scenario. These can be invoked with @link NXOpen::CAE::PostScenarioAction::Invoke NXOpen::CAE::PostScenarioAction::Invoke@endlink 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            NXOpen::CAE::PostScenarioAction * GetActionByName
            (
                const char * subvisualization /** subvisualization */ ,
                const char * name /** name */ 
            );


            /** The collection of Plots this scenario is attached to. 

                        
                            Access is provided via @link NXOpen::CAE::PostScenarioPlotHandle NXOpen::CAE::PostScenarioPlotHandle@endlink  instances.

                            The Plots are determined by the selected @link CAE::PostScenarioBuilder::Visualization CAE::PostScenarioBuilder::Visualization @endlink and @link CAE::PostScenarioBuilder::SetVisualization CAE::PostScenarioBuilder::SetVisualization @endlink .

                            If multiple scenarios are overlaid, the resulting visualization can change.
                         
             <br>  Created in NX1899.0.0.  <br>  
            */
            public: NXOpen::CAE::PostScenarioPlotHandleCollection *Plots();
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
