#ifndef NXOpen_CAE_RESPONSESIMULATION_VELOCITYIMPACTEXCITATIONBUILDER_HXX_INCLUDED
#define NXOpen_CAE_RESPONSESIMULATION_VELOCITYIMPACTEXCITATIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_ResponseSimulation_VelocityImpactExcitationBuilder.ja
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
#include <NXOpen/CAE_ResponseSimulation_VelocityImpactDirection.hxx>
#include <NXOpen/CAE_ResponseSimulation_VelocityImpactExcitationBuilder.hxx>
#include <NXOpen/CAE_ResponseSimulation_VelocityImpactParameters.hxx>
#include <NXOpen/CAE_ResponseSimulation_ExcitationBuilder.hxx>
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
            class VelocityImpactExcitationBuilder;
        }
    }
    namespace CAE
    {
        namespace ResponseSimulation
        {
            class ExcitationBuilder;
        }
    }
    namespace CAE
    {
        namespace ResponseSimulation
        {
            class VelocityImpactDirection;
        }
    }
    namespace CAE
    {
        namespace ResponseSimulation
        {
            class VelocityImpactParameters;
        }
    }
    namespace CAE
    {
        namespace ResponseSimulation
        {
            class _VelocityImpactExcitationBuilderBuilder;
            class VelocityImpactExcitationBuilderImpl;
            /**
                Represents a @link CAE::ResponseSimulation::VelocityImpactExcitationBuilder CAE::ResponseSimulation::VelocityImpactExcitationBuilder@endlink 
                 <br> To create a new instance of this class, use @link NXOpen::CAE::ResponseSimulation::ExcitationCollection::CreateVelocityImpactExcitationBuilder  NXOpen::CAE::ResponseSimulation::ExcitationCollection::CreateVelocityImpactExcitationBuilder @endlink  <br> 
            Default values.
            <table border="1"> 
             
            <tr><th> 
            Property</th>  <th> 
            Value</th> </tr>
            <tr><td> 
             
            ImpactDirection.DirectionOption </td> <td> 
             
            NodalComponent </td> </tr> 

            <tr><td> 
             
            ImpactDirection.NodalComponent </td> <td> 
             
            Dof1 </td> </tr> 

            <tr><td> 
             
            ImpactMethod </td> <td> 
             
            ConstantVelocity </td> </tr> 

            <tr><td> 
             
            ImpactParameters.DropHeight.Value </td> <td> 
             
            1.0 (millimeters part), 1.0 (inches part) </td> </tr> 

            <tr><td> 
             
            ImpactParameters.PulseDuration.Value </td> <td> 
             
            1.0 (millimeters part), 1.0 (inches part) </td> </tr> 

            <tr><td> 
             
            ImpactParameters.StartPosition </td> <td> 
             
            AtDrop </td> </tr> 

            <tr><td> 
             
            ImpactParameters.TimeStep.Value </td> <td> 
             
            1.0 (millimeters part), 1.0 (inches part) </td> </tr> 

            <tr><td> 
             
            ImpactParameters.Velocity.Value </td> <td> 
             
            1.0 (millimeters part), 1.0 (inches part) </td> </tr> 

            </table>  

             <br>  Created in NX6.0.0.  <br>  
            */
            class NXOPENCPP_CAEEXPORT  VelocityImpactExcitationBuilder : public NXOpen::CAE::ResponseSimulation::ExcitationBuilder
            {
                /** the impact definiton methods */
                public: enum ImpactMethodType
                {
                    ImpactMethodTypeConstantVelocity/** the users will only be able to specify the velocity for the impact */,
                    ImpactMethodTypeDropImpact/** the users will be able to specify the drop height or the desired velocity at the impact*/
                };

                private: VelocityImpactExcitationBuilderImpl * m_velocityimpactexcitationbuilder_impl;
                private: friend class  _VelocityImpactExcitationBuilderBuilder;
                protected: VelocityImpactExcitationBuilder();
                public: ~VelocityImpactExcitationBuilder();
                /**Returns  the impact method 
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::CAE::ResponseSimulation::VelocityImpactExcitationBuilder::ImpactMethodType ImpactMethod
                (
                );
                /**Sets  the impact method 
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: void SetImpactMethod
                (
                    NXOpen::CAE::ResponseSimulation::VelocityImpactExcitationBuilder::ImpactMethodType impactMethod /** impactmethod */ 
                );
                /**Returns  the impact parameters setting
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::CAE::ResponseSimulation::VelocityImpactParameters * ImpactParameters
                (
                );
                /**Returns  the impact direction setting
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::CAE::ResponseSimulation::VelocityImpactDirection * ImpactDirection
                (
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
