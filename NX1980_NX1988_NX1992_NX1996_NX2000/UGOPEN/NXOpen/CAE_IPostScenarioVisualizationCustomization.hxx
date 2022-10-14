#ifndef NXOpen_CAE_IPOSTSCENARIOVISUALIZATIONCUSTOMIZATION_HXX_INCLUDED
#define NXOpen_CAE_IPOSTSCENARIOVISUALIZATIONCUSTOMIZATION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_IPostScenarioVisualizationCustomization.ja
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
        class IPostScenarioVisualizationCustomization;
    }
    namespace CAE
    {
        /**  @brief  Visualization specific customization data.  

          
         <br>  Created in NX1847.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  IPostScenarioVisualizationCustomization
        {
            virtual void EnsureVtableExists() {}
            public: virtual ~IPostScenarioVisualizationCustomization() {}
            /** 
                        Returns the subviewport id of the visualization.
                    
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: virtual int GetSubviewportIndex
            (
            ) = 0;
            /** 
                        Returns the name of the visualization.
                    
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: virtual NXString GetName
            (
            ) = 0;
            /** 
                        This commits the changes done to the visualization.
                    
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: virtual void Update
            (
            ) = 0;
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