#ifndef NXOpen_MOTION_CONTROLINPUTPORTBUILDER_HXX_INCLUDED
#define NXOpen_MOTION_CONTROLINPUTPORTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Motion_ControlInputPortBuilder.ja
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
#include <NXOpen/Expression.hxx>
#include <NXOpen/Motion_MotionBuilder.hxx>
#include <NXOpen/libnxopencpp_motion_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Motion
    {
        class ControlInputPortBuilder;
    }
    class Expression;
    namespace Motion
    {
        class MotionBuilder;
    }
    namespace Motion
    {
        class _ControlInputPortBuilderBuilder;
        class ControlInputPortBuilderImpl;
        /** Represents a @link Motion::ControlPort Motion::ControlPort@endlink  builder specific to control input element.  <br> To create a new instance of this class, use @link NXOpen::Motion::ControlInputBuilder::CreateControlInputPortBuilder  NXOpen::Motion::ControlInputBuilder::CreateControlInputPortBuilder @endlink  <br> 
         <br>  Created in NX11.0.0.  <br>  
        */
        class NXOPENCPP_MOTIONEXPORT  ControlInputPortBuilder : public NXOpen::Motion::MotionBuilder
        {
            /** the types of components that can be measured by the control input element for the selected variable. */
            public: enum MeasuredComponent
            {
                MeasuredComponentUnused/** Unused */ = -1,
                MeasuredComponentLinearMagnitude/** Linear Magnitude */,
                MeasuredComponentX/** X */,
                MeasuredComponentY/** Y */,
                MeasuredComponentZ/** Z */,
                MeasuredComponentAngularMagnitude/** Angular Magnitude */,
                MeasuredComponentRx/** RX */,
                MeasuredComponentRy/** RY */,
                MeasuredComponentRz/** RZ */,
                MeasuredComponentRadial/** Radial */
            };

            /** the types of variables that can be measured by the control input element.*/
            public: enum MeasuredVariable
            {
                MeasuredVariableUnused/** Unused */ = -1,
                MeasuredVariableDisplacement/** Displacement */,
                MeasuredVariableVelocity/** Velocity */,
                MeasuredVariableAcceleration/** Acceleration*/,
                MeasuredVariableGravityExcludedAcceleration/** Gravity Excluded Acceleration*/,
                MeasuredVariableTraveledDistance/** Traveled Distance */
            };

            /** the types of digital options tha can be chosen by control input element.*/
            public: enum DigitalType
            {
                DigitalTypeNo/** Do not use Digital */,
                DigitalTypeYes/** Use Digital */
            };

            private: ControlInputPortBuilderImpl * m_controlinputportbuilder_impl;
            private: friend class  _ControlInputPortBuilderBuilder;
            protected: ControlInputPortBuilder();
            public: ~ControlInputPortBuilder();
            /**Returns  the control input port name. Must be unique across all motion elements. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: NXString Name
            (
            );
            /**Sets  the control input port name. Must be unique across all motion elements. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetName
            (
                const NXString & name /** name */ 
            );
            /**Sets  the control input port name. Must be unique across all motion elements. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            void SetName
            (
                const char * name /** name */ 
            );
            /**Returns  the component that is measured by the control input element for the selected variable. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: NXOpen::Motion::ControlInputPortBuilder::MeasuredComponent Component
            (
            );
            /**Sets  the component that is measured by the control input element for the selected variable. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetComponent
            (
                NXOpen::Motion::ControlInputPortBuilder::MeasuredComponent component /** component */ 
            );
            /**Returns  the variable that is measured by the control input element.
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: NXOpen::Motion::ControlInputPortBuilder::MeasuredVariable Variable
            (
            );
            /**Sets  the variable that is measured by the control input element.
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetVariable
            (
                NXOpen::Motion::ControlInputPortBuilder::MeasuredVariable variable /** variable */ 
            );
            /**Returns  an option to specify whether the element is sampled or not.
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: NXOpen::Motion::ControlInputPortBuilder::DigitalType DigitalOption
            (
            );
            /**Sets  an option to specify whether the element is sampled or not.
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetDigitalOption
            (
                NXOpen::Motion::ControlInputPortBuilder::DigitalType digitalOption /** digitaloption */ 
            );
            /**Returns  a logical flag to specify whether the element is digital (sampled) or analog.
                        If TRUE, the element will be considered digital and will require a sample rate. 
             <br>  @deprecated Deprecated in NX1899.0.0.  Use @link NXOpen::Motion::ControlInputPortBuilder::DigitalOption NXOpen::Motion::ControlInputPortBuilder::DigitalOption@endlink  <br>  

             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: NX_DEPRECATED("Deprecated in NX1899.0.0.  Use NXOpen::Motion::ControlInputPortBuilder::DigitalOption") bool Digital
            (
            );
            /**Sets  a logical flag to specify whether the element is digital (sampled) or analog.
                        If TRUE, the element will be considered digital and will require a sample rate. 
             <br>  @deprecated Deprecated in NX1899.0.0.  Use @link NXOpen::Motion::ControlInputPortBuilder::SetDigitalOption NXOpen::Motion::ControlInputPortBuilder::SetDigitalOption@endlink  <br>  

             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: NX_DEPRECATED("Deprecated in NX1899.0.0.  Use NXOpen::Motion::ControlInputPortBuilder::SetDigitalOption") void SetDigital
            (
                bool digital /** digital */ 
            );
            /**Returns  the Sample Rate specifies the sampling frequency in samples per second for this element.
                        A value is required if Digital flag is set to TRUE. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: NXOpen::Expression * SampleRate
            (
            );
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