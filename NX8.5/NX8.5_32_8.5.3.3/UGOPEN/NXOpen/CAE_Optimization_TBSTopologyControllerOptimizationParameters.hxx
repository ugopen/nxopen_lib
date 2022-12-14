#ifndef NXOpen_CAE_OPTIMIZATION_TBSTOPOLOGYCONTROLLEROPTIMIZATIONPARAMETERS_HXX_INCLUDED
#define NXOpen_CAE_OPTIMIZATION_TBSTOPOLOGYCONTROLLEROPTIMIZATIONPARAMETERS_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_Optimization_TBSTopologyControllerOptimizationParameters.ja
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
#include <NXOpen/CAE_Optimization_TBSOptimizationParameters.hxx>
#include <NXOpen/CAE_Optimization_TBSTopologyControllerOptimizationParameters.hxx>
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
        namespace Optimization
        {
            class TBSTopologyControllerOptimizationParameters;
        }
    }
    namespace CAE
    {
        namespace Optimization
        {
            class TBSOptimizationParameters;
        }
    }
    namespace CAE
    {
        namespace Optimization
        {
            class _TBSTopologyControllerOptimizationParametersBuilder;
            class TBSTopologyControllerOptimizationParametersImpl;
            /** Represents the parameters to control an optimization in controller strategy 
             <br>  Created in NX8.0.0.  <br>  
            */
            class NXOPENCPP_CAEEXPORT  TBSTopologyControllerOptimizationParameters : public CAE::Optimization::TBSOptimizationParameters
            {
                /** Specifies the step size of increment */
                public: enum Speed
                {
                    SpeedVerySlow/** Very small stepsize */,
                    SpeedSlow/** Small stepsize */,
                    SpeedModerate/** Moderate stepsize */,
                    SpeedMedium/** Medium stepsize */,
                    SpeedFast/** Fast large step size */,
                    SpeedIteration/** Step size is modified dynamically so the optimization end after the given number of iterations */
                };

                /** Represents the definition of volume that can be removed immediatedly in the first design cycle */
                public: enum VolumeDefinitionMethod
                {
                    VolumeDefinitionMethodPercent/** Specifying the volume in percentage */,
                    VolumeDefinitionMethodAbsolute/** Specifying the absolute volume*/
                };

                /** Defines the automatic fromzen strategy */
                public: enum AutoFrozen
                {
                    AutoFrozenLoad/** All loaded elements and nodes are excluded from the optimization*/,
                    AutoFrozenOff/** Loaded elements are optimizable */,
                    AutoFrozenSpc/** Elements with boundary conditions are excluded from the optimization */,
                    AutoFrozenBoth/** All loaded elements, elements with load nodes with boundary conditions are excluded from the optimization*/
                };

                private: TBSTopologyControllerOptimizationParametersImpl * m_tbstopologycontrolleroptimizationparameters_impl;
                private: friend class  _TBSTopologyControllerOptimizationParametersBuilder;
                protected: TBSTopologyControllerOptimizationParameters();
                public: ~TBSTopologyControllerOptimizationParameters();
                /**Returns  the speed size of increment 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::CAE::Optimization::TBSTopologyControllerOptimizationParameters::Speed SpeedOption
                (
                );
                /**Sets  the speed size of increment 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : cae_opt_topo ("NX Topology Optimization") OR cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization") */
                public: void SetSpeedOption
                (
                    NXOpen::CAE::Optimization::TBSTopologyControllerOptimizationParameters::Speed speedOption /** speedoption */ 
                );
                /**Returns  the number of iterations. Only available when @link CAE::Optimization::TBSTopologyControllerOptimizationParameters::SpeedOption CAE::Optimization::TBSTopologyControllerOptimizationParameters::SpeedOption@endlink  is
                        @link CAE::Optimization::TBSTopologyControllerOptimizationParameters::SpeedIteration CAE::Optimization::TBSTopologyControllerOptimizationParameters::SpeedIteration@endlink  
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: int IterationNumbers
                (
                );
                /**Sets  the number of iterations. Only available when @link CAE::Optimization::TBSTopologyControllerOptimizationParameters::SpeedOption CAE::Optimization::TBSTopologyControllerOptimizationParameters::SpeedOption@endlink  is
                        @link CAE::Optimization::TBSTopologyControllerOptimizationParameters::SpeedIteration CAE::Optimization::TBSTopologyControllerOptimizationParameters::SpeedIteration@endlink  
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : cae_opt_topo ("NX Topology Optimization") OR cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization") */
                public: void SetIterationNumbers
                (
                    int numIterations /** numiterations */ 
                );
                /**Returns  the volume definition option 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::CAE::Optimization::TBSTopologyControllerOptimizationParameters::VolumeDefinitionMethod VolumeDefinitionOption
                (
                );
                /**Sets  the volume definition option 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : cae_opt_topo ("NX Topology Optimization") OR cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization") */
                public: void SetVolumeDefinitionOption
                (
                    NXOpen::CAE::Optimization::TBSTopologyControllerOptimizationParameters::VolumeDefinitionMethod volumeDefinitionOption /** volumedefinitionoption */ 
                );
                /**Returns  the volume that is deleted in the first design cycle 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: double StartDeleteVolume
                (
                );
                /**Sets  the volume that is deleted in the first design cycle 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : cae_opt_topo ("NX Topology Optimization") OR cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization") */
                public: void SetStartDeleteVolume
                (
                    double startDeleteVolume /** startdeletevolume */ 
                );
                /**Returns  the automatic frozen option 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::CAE::Optimization::TBSTopologyControllerOptimizationParameters::AutoFrozen AutomaticFrozenOption
                (
                );
                /**Sets  the automatic frozen option 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : cae_opt_topo ("NX Topology Optimization") OR cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization") */
                public: void SetAutomaticFrozenOption
                (
                    NXOpen::CAE::Optimization::TBSTopologyControllerOptimizationParameters::AutoFrozen autoFrozen /** autofrozen */ 
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
