#ifndef NXOpen_CAE_RESPONSESIMULATION_ELEMENTALFUNCTIONEVALUATIONSETTINGBUILDER_HXX_INCLUDED
#define NXOpen_CAE_RESPONSESIMULATION_ELEMENTALFUNCTIONEVALUATIONSETTINGBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_ResponseSimulation_ElementalFunctionEvaluationSettingBuilder.ja
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
#include <NXOpen/CAE_ResponseSimulation.hxx>
#include <NXOpen/CAE_ResponseSimulation_FunctionEvaluationSettingBuilder.hxx>
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
        namespace ResponseSimulation
        {
            class ElementalFunctionEvaluationSettingBuilder;
        }
    }
    namespace CAE
    {
        class FEElement;
    }
    namespace CAE
    {
        namespace ResponseSimulation
        {
            class FunctionEvaluationSettingBuilder;
        }
    }
    namespace CAE
    {
        namespace ResponseSimulation
        {
            class _ElementalFunctionEvaluationSettingBuilderBuilder;
            class ElementalFunctionEvaluationSettingBuilderImpl;
            /** This is a manager to the @link NXOpen::CAE::ResponseSimulation::ElementalFunctionEvaluationSetting NXOpen::CAE::ResponseSimulation::ElementalFunctionEvaluationSetting@endlink  class. 
                Object of type @link NXOpen::CAE::ResponseSimulation::ElementalFunctionEvaluationSetting NXOpen::CAE::ResponseSimulation::ElementalFunctionEvaluationSetting@endlink  can be 
                created and edited only through this class
                  <br> To create a new instance of this class, use @link NXOpen::CAE::ResponseSimulation::EvaluationSettingManager::CreateElementalFunctionEvaluationSettingBuilder  NXOpen::CAE::ResponseSimulation::EvaluationSettingManager::CreateElementalFunctionEvaluationSettingBuilder @endlink  <br> 
             <br>  Created in NX5.0.0.  <br>  
            */
            class NXOPENCPP_CAEEXPORT  ElementalFunctionEvaluationSettingBuilder : public NXOpen::CAE::ResponseSimulation::FunctionEvaluationSettingBuilder
            {
                private: ElementalFunctionEvaluationSettingBuilderImpl * m_elementalfunctionevaluationsettingbuilder_impl;
                private: friend class  _ElementalFunctionEvaluationSettingBuilderBuilder;
                protected: ElementalFunctionEvaluationSettingBuilder();
                public: ~ElementalFunctionEvaluationSettingBuilder();
                /** Returns the destination elements  @return  
                 <br>  Created in NX5.0.0.  <br>  
                 <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: std::vector<NXOpen::CAE::FEElement *> GetDestinationElements
                (
                );
                /** Sets the destination elements 
                 <br>  Created in NX5.0.0.  <br>  
                 <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: void SetDestinationElements
                (
                    const std::vector<NXOpen::CAE::FEElement *> & destinationElement /** destination element */ 
                );
                /**Returns  the coordinate system 
                 <br>  Created in NX5.0.0.  <br>  
                 <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: NXOpen::CAE::ResponseSimulation::CoordinateSystem CoordinateSystem
                (
                );
                /**Sets  the coordinate system 
                 <br>  Created in NX5.0.0.  <br>  
                 <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: void SetCoordinateSystem
                (
                    NXOpen::CAE::ResponseSimulation::CoordinateSystem coordinateSystem /** coordinate system */ 
                );
                /**Returns  the data component of direction 
                 <br>  Created in NX5.0.0.  <br>  
                 <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: NXOpen::CAE::ResponseSimulation::DirectionDataComponent DataComponent
                (
                );
                /**Sets  the data component of direction 
                 <br>  Created in NX5.0.0.  <br>  
                 <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: void SetDataComponent
                (
                    NXOpen::CAE::ResponseSimulation::DirectionDataComponent dataComponent /** data component */ 
                );
                /**Returns  the data location of beam element. For more information about beam data location,
                        see the Response Simulatin section of the Gateway help 
                 <br>  Created in NX5.0.0.  <br>  
                 <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: NXOpen::CAE::ResponseSimulation::ElementalFunctionEvalBeamLocation BeamDataLocation
                (
                );
                /**Sets  the data location of beam element. For more information about beam data location,
                        see the Response Simulatin section of the Gateway help 
                 <br>  Created in NX5.0.0.  <br>  
                 <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: void SetBeamDataLocation
                (
                    NXOpen::CAE::ResponseSimulation::ElementalFunctionEvalBeamLocation beamLocation /** beam location */ 
                );
                /**Returns  the evaluation location of shell element. 
                 <br>  Created in NX5.0.0.  <br>  
                 <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: NXOpen::CAE::ResponseSimulation::ShellElementEvaluationLocation ShellEvaluationLocation
                (
                );
                /**Sets  the evaluation location of shell element. 
                 <br>  Created in NX5.0.0.  <br>  
                 <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: void SetShellEvaluationLocation
                (
                    NXOpen::CAE::ResponseSimulation::ShellElementEvaluationLocation shellLocation /** shell location */ 
                );
                /**Returns  the evaluation location of element. 
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: NXOpen::CAE::ResponseSimulation::ElementLocation ElementLocation
                (
                );
                /**Sets  the evaluation location of element. 
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: void SetElementLocation
                (
                    NXOpen::CAE::ResponseSimulation::ElementLocation elementLocation /** element location */ 
                );
                /**Returns  the spring force evaluation From displacement flag. 
                 <br>  Created in NX1953.0.0.  <br>  
                 <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: bool SpringForceEvaluationFromDisplacement
                (
                );
                /**Sets  the spring force evaluation From displacement flag. 
                 <br>  Created in NX1953.0.0.  <br>  
                 <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: void SetSpringForceEvaluationFromDisplacement
                (
                    bool springForceEvaluationFromDisplacement /** spring force evaluation from displacement */ 
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
