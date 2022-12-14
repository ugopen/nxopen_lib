#ifndef NXOpen_MOTION_TEXTBASEDELEMENTBUILDER_HXX_INCLUDED
#define NXOpen_MOTION_TEXTBASEDELEMENTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Motion_TextBasedElementBuilder.ja
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
        class TextBasedElementBuilder;
    }
    namespace Motion
    {
        class MotionBuilder;
    }
    namespace Motion
    {
        class _TextBasedElementBuilderBuilder;
        class TextBasedElementBuilderImpl;
        /** Represents a @link NXOpen::Motion::TextBasedElementBuilder NXOpen::Motion::TextBasedElementBuilder@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::Motion::TextBasedElementCollection::CreateTextBasedElementBuilder  NXOpen::Motion::TextBasedElementCollection::CreateTextBasedElementBuilder @endlink  <br> 
         <br>  Created in NX12.0.0.  <br>  
        */
        class NXOPENCPP_MOTIONEXPORT  TextBasedElementBuilder : public NXOpen::Motion::MotionBuilder
        {
            /** the text based element type - multiple values*/
            public: enum TypeChoices
            {
                TypeChoicesThreePointForce/** three point force */ ,
                TypeChoicesThreePointTorque/** three point torque */ ,
                TypeChoicesKinematicSensor/** kinematic sensor */ ,
                TypeChoicesAllForceDirectionSensor/** all force direction sensor */ ,
                TypeChoicesAeroAeroForce/** aero aero force */ ,
                TypeChoicesAeroHydroForce/** aero hydro force */ ,
                TypeChoicesAeroVehicleForce/** aero vehicle force */ ,
                TypeChoicesCustomizedSolver/** customized solver */ ,
                TypeChoicesStiTire/** sti tire */ ,
                TypeChoicesStiTireProperty/** sti tire property */ ,
                TypeChoicesBumpStopContact/** bump stop contact */ ,
                TypeChoicesSphereToGroundContact/** sphere to ground contact */ ,
                TypeChoicesGearContact/** gear contact */ ,
                TypeChoicesThreeLinkSuspension/** three link suspension */ ,
                TypeChoicesFourLinkSuspension/** four link suspension */ ,
                TypeChoicesFiveLinkSuspension/** five link suspension */ ,
                TypeChoicesRollIaxSuspension/** roll iax suspension */ ,
                TypeChoicesSteerIaxSuspension/** steer iax suspension */ ,
                TypeChoicesHotchKissSuspension/** hotch kiss suspension */ ,
                TypeChoicesMcPhersonSuspension/** mc pherson suspension */ ,
                TypeChoicesDoubleAArmSuspension/** double aarm suspension */ ,
                TypeChoicesPivotBeamSuspension/** pivot beam suspension */ ,
                TypeChoicesVehicle/** vehicle */ ,
                TypeChoicesSpeedSweep/** speed sweep */ ,
                TypeChoicesSystemProperty/** system property */ ,
                TypeChoicesDynamicProperty/** dynamic property */ ,
                TypeChoicesKinematicProperty/** kinematic property */ ,
                TypeChoicesStaticProperty/** static property */ ,
                TypeChoicesPreloadProperty/** preload property */ ,
                TypeChoicesInverseProperty/** inverse property */ ,
                TypeChoicesLinearizationProperty/** linearization property */ ,
                TypeChoicesRestartProperty/** restart property */ ,
                TypeChoicesAdvancedSolution/** advanced solution */ ,
                TypeChoicesGear/** gear */ ,
                TypeChoicesGeneric/** generic */ ,
                TypeChoicesFmi/** fmi */ ,
                TypeChoicesPointToPointConstraint/** point to point constraint */ ,
                TypeChoicesOrientationConstraint/** orientation constraint */ ,
                TypeChoicesFunctioncurveControlInput/** functioncurve control input */ ,
                TypeChoicesPathFollowerControlInput/** path follower control input */ ,
                TypeChoicesUserDefinedControlInput/** user defined control input */ ,
                TypeChoicesSpecialControlInput/** special control input */ ,
                TypeChoicesLinearControlOutput/** linear control output */ ,
                TypeChoicesMassPropertyControlOutput/** mass property control output */ ,
                TypeChoicesLinkInitialCondition/** link initial condition */ ,
                TypeChoicesScrewJointOrSpringInitialCondition/** screw joint or spring initial condition */ ,
                TypeChoicesFlexibleLinkInitialCondition/** flexible link initial condition */ ,
                TypeChoicesTireInitialCondition/** tire initial condition */ ,
                TypeChoicesStaticVehicleAlignment/** static vehicle alignment */ ,
                TypeChoicesSprungMass/** sprung mass */ ,
                TypeChoicesUserDefinedForce/** user defined force */ ,
                TypeChoicesGlobalDirectionsLinkDriver/** global directions link driver */ ,
                TypeChoicesDotOneLinkDriver/** dot one link driver */ ,
                TypeChoicesDotTwoLinkDriver/** dot two link driver */ ,
                TypeChoicesCurveOnCurveConstraintDriver/** curve on curve constraint driver */ ,
                TypeChoicesFixedJointDriver/** fixed joint driver */ ,
                TypeChoicesLinkCouplerDriver/** link coupler driver */ ,
                TypeChoicesLinkDriver/** link driver */ ,
                TypeChoicesJointDriver/** joint driver */ ,
                TypeChoicesLinkControlOutput/** link control output */ ,
                TypeChoicesJointOrConstraintControlOutput/** joint or constraint control output */ ,
                TypeChoicesAmesim/** amesim */ ,
                TypeChoicesMatlab/** matlab */ ,
                TypeChoicesAmplifierControlOperations/** amplifier control operations */ ,
                TypeChoicesControlFunctionControlOperations/** control function control operations */ ,
                TypeChoicesMultiplierControlOperations/** multiplier control operations */ ,
                TypeChoicesSummerControlOperations/** summer control operations */ ,
                TypeChoicesUserAlgebraicControlOperations/** user algebraic control operations */ ,
                TypeChoicesProfile/** profile */ ,
                TypeChoicesCCodeProperty/** ccode property */ ,
                TypeChoicesConstraintOptimization/** constraint optimization */ ,
                TypeChoicesParallelSolution/** parallel solution */ ,
                TypeChoicesCCodeParameter/** ccode parameter */ ,
                TypeChoicesSphericalSphericalJoint/** spherical spherical joint */ ,
                TypeChoicesIntegratorControlOperations/** integrator control operations */ ,
                TypeChoicesLimitControlOperations/** limit control operations */ ,
                TypeChoicesSurfaceLookupControlOperations/** surface lookup control operations */ ,
                TypeChoicesDeadZoneControlOperations/** dead zone control operations */ ,
                TypeChoicesFirstOrderControlOperations/** first order control operations */ ,
                TypeChoicesHysteresisControlOperations/** hysteresis control operations */ ,
                TypeChoicesDelayControlOperations/** delay control operations */ ,
                TypeChoicesSecondOrderControlOperations/** second order control operations */ ,
                TypeChoicesStop/** stop */ ,
                TypeChoicesCylindricalFriction/** cylindrical friction */ ,
                TypeChoicesPlanarFriction/** planar friction */ ,
                TypeChoicesRevoluteFriction/** revolute friction */ ,
                TypeChoicesScrewFriction/** screw friction */ ,
                TypeChoicesSliderFriction/** slider friction */ ,
                TypeChoicesSphericalFriction/** spherical friction */ ,
                TypeChoicesUniversalFriction/** universal friction */ ,
                TypeChoicesVehicleCornerAnalysisControlInput/** vehicle corner analysis control input */ ,
                TypeChoicesSVCIterate/** svciterate */ ,
                TypeChoicesPointCurveFriction/** point curve friction */ ,
                TypeChoicesPointSurfaceFriction/** point surface friction */ ,
                TypeChoicesSlideCurveFriction/** slide curve friction */ ,
                TypeChoicesNForce/** nforce */ ,
                TypeChoicesBushingLink/** bushing link */ ,
                TypeChoicesDifferentialEquation/** differential equation */ ,
                TypeChoicesHydraulicLashAdjuster/** hydraulic lash adjuster */ ,
                TypeChoicesCamContact/** cam contact */ ,
                TypeChoicesCamGenerator/** cam generator */ ,
                TypeChoicesBearing/** bearing */ ,
                TypeChoicesHydrodynamicBearing/** hydrodynamic bearing */ ,
                TypeChoicesCombustion/** combustion */ ,
                TypeChoicesTachometer/** tachometer */ ,
                TypeChoicesLoadTimeSeriesOutput/** load time series output */ ,
                TypeChoicesKinematicTimeSeriesOutput/** kinematic time series output */ ,
                TypeChoicesModeTimeSeriesOutput/** mode time series output */ ,
                TypeChoicesMathFunctionTimeSeriesOutput/** math function time series output */ ,
                TypeChoicesSwitchControlOperations/** switch control operations */ ,
                TypeChoicesSteadyStateControlOperations/** steady state control operations */ ,
                TypeChoicesMechatronicsExport/** mechatronics export */ 
            };

            private: TextBasedElementBuilderImpl * m_textbasedelementbuilder_impl;
            private: friend class  _TextBasedElementBuilderBuilder;
            protected: TextBasedElementBuilder();
            public: ~TextBasedElementBuilder();
            /**Returns  the text based element type - multiple possible values
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: NXOpen::Motion::TextBasedElementBuilder::TypeChoices Type
            (
            );
            /**Sets  the text based element type - multiple possible values
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetType
            (
                NXOpen::Motion::TextBasedElementBuilder::TypeChoices elementType /** elementtype */ 
            );
            /**Returns  the definition of text based element - MDF definition 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: NXString Definition
            (
            );
            /**Sets  the definition of text based element - MDF definition 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetDefinition
            (
                const NXString & definition /** definition */ 
            );
            /**Sets  the definition of text based element - MDF definition 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            void SetDefinition
            (
                const char * definition /** definition */ 
            );
            /**Returns  the name of text based element - MDF definition 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: NXString Name
            (
            );
            /**Sets  the name of text based element - MDF definition 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetName
            (
                const NXString & name /** name */ 
            );
            /**Sets  the name of text based element - MDF definition 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            void SetName
            (
                const char * name /** name */ 
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
