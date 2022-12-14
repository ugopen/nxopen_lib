#ifndef NXOpen_MOTION_RECURDYNSOLVERPROPERTY_HXX_INCLUDED
#define NXOpen_MOTION_RECURDYNSOLVERPROPERTY_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Motion_RecurdynSolverProperty.ja
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
#include <NXOpen/Motion_RecurdynSolverProperty.hxx>
#include <NXOpen/TaggedObject.hxx>
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
        class RecurdynSolverProperty;
    }
    class Expression;
    namespace Motion
    {
        class _RecurdynSolverPropertyBuilder;
        class RecurdynSolverPropertyImpl;
        /** Represents a @link NXOpen::Motion::RecurdynSolverProperty NXOpen::Motion::RecurdynSolverProperty@endlink  
         <br>  Created in NX5.0.0.  <br>  
        */
        class NXOPENCPP_MOTIONEXPORT  RecurdynSolverProperty : public NXOpen::TaggedObject
        {
            /** Integrator type */
            public: enum StaticIntegratorTypes
            {
                StaticIntegratorTypesNewtonRapson/** Newton rapson */,
                StaticIntegratorTypesRobustNewtonRapson/** Robust newton rapson */
            };

            private: RecurdynSolverPropertyImpl * m_recurdynsolverproperty_impl;
            private: friend class  _RecurdynSolverPropertyBuilder;
            protected: RecurdynSolverProperty();
            public: ~RecurdynSolverProperty();
            /**Returns  the dynamic initial step size 
             <br>  @deprecated Deprecated in NX8.5.0.  Obtion the expression using @link NXOpen::Motion::RecurdynSolverProperty::DynamicInitialStepSizeExpression NXOpen::Motion::RecurdynSolverProperty::DynamicInitialStepSizeExpression@endlink  to query or edit it. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX8.5.0.  Obtion the expression using NXOpen::Motion::RecurdynSolverProperty::DynamicInitialStepSizeExpression to query or edit it.") double DynamicInitialStepSize
            (
            );
            /**Sets  the dynamic initial step size 
             <br>  @deprecated Deprecated in NX8.5.0.  Obtion the expression using @link NXOpen::Motion::RecurdynSolverProperty::DynamicInitialStepSizeExpression NXOpen::Motion::RecurdynSolverProperty::DynamicInitialStepSizeExpression@endlink  to query or edit it. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public:  NX_DEPRECATED("Deprecated in NX8.5.0.  Obtion the expression using NXOpen::Motion::RecurdynSolverProperty::DynamicInitialStepSizeExpression to query or edit it.") void SetDynamicInitialStepSize
            (
                double dynamicInitialStepSize /** dynamicinitialstepsize */ 
            );
            /**Returns  the dynamic error tolerance 
             <br>  @deprecated Deprecated in NX8.5.0.  Obtion the expression using @link NXOpen::Motion::RecurdynSolverProperty::DynamicErrorToleranceExpression NXOpen::Motion::RecurdynSolverProperty::DynamicErrorToleranceExpression@endlink  to query or edit it. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX8.5.0.  Obtion the expression using NXOpen::Motion::RecurdynSolverProperty::DynamicErrorToleranceExpression to query or edit it.") double DynamicErrorTolerance
            (
            );
            /**Sets  the dynamic error tolerance 
             <br>  @deprecated Deprecated in NX8.5.0.  Obtion the expression using @link NXOpen::Motion::RecurdynSolverProperty::DynamicErrorToleranceExpression NXOpen::Motion::RecurdynSolverProperty::DynamicErrorToleranceExpression@endlink  to query or edit it. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public:  NX_DEPRECATED("Deprecated in NX8.5.0.  Obtion the expression using NXOpen::Motion::RecurdynSolverProperty::DynamicErrorToleranceExpression to query or edit it.") void SetDynamicErrorTolerance
            (
                double dynamicErrorTolerance /** dynamicerrortolerance */ 
            );
            /**Returns  the dynamic max step size 
             <br>  @deprecated Deprecated in NX8.5.0.  Obtion the expression using @link NXOpen::Motion::RecurdynSolverProperty::DynamicMaxStepSizeExpression NXOpen::Motion::RecurdynSolverProperty::DynamicMaxStepSizeExpression@endlink  to query or edit it. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX8.5.0.  Obtion the expression using NXOpen::Motion::RecurdynSolverProperty::DynamicMaxStepSizeExpression to query or edit it.") double DynamicMaxStepSize
            (
            );
            /**Sets  the dynamic max step size 
             <br>  @deprecated Deprecated in NX8.5.0.  Obtion the expression using @link NXOpen::Motion::RecurdynSolverProperty::DynamicMaxStepSizeExpression NXOpen::Motion::RecurdynSolverProperty::DynamicMaxStepSizeExpression@endlink  to query or edit it. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public:  NX_DEPRECATED("Deprecated in NX8.5.0.  Obtion the expression using NXOpen::Motion::RecurdynSolverProperty::DynamicMaxStepSizeExpression to query or edit it.") void SetDynamicMaxStepSize
            (
                double dynamicMaxStepSize /** dynamicmaxstepsize */ 
            );
            /**Returns  the dynamic numerical damping 
             <br>  @deprecated Deprecated in NX8.5.0.  Obtion the expression using @link NXOpen::Motion::RecurdynSolverProperty::DynamicNumericalDampingExpression NXOpen::Motion::RecurdynSolverProperty::DynamicNumericalDampingExpression@endlink  to query or edit it. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX8.5.0.  Obtion the expression using NXOpen::Motion::RecurdynSolverProperty::DynamicNumericalDampingExpression to query or edit it.") double DynamicNumericalDamping
            (
            );
            /**Sets  the dynamic numerical damping 
             <br>  @deprecated Deprecated in NX8.5.0.  Obtion the expression using @link NXOpen::Motion::RecurdynSolverProperty::DynamicNumericalDampingExpression NXOpen::Motion::RecurdynSolverProperty::DynamicNumericalDampingExpression@endlink  to query or edit it. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public:  NX_DEPRECATED("Deprecated in NX8.5.0.  Obtion the expression using NXOpen::Motion::RecurdynSolverProperty::DynamicNumericalDampingExpression to query or edit it.") void SetDynamicNumericalDamping
            (
                double dynamicNumericalDamping /** dynamicnumericaldamping */ 
            );
            /**Returns  the Maximum kinematic iteration 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: int DynamicMaxKinIteration
            (
            );
            /**Sets  the Maximum kinematic iteration 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetDynamicMaxKinIteration
            (
                int dynamicMaxKinIteration /** dynamicmaxkiniteration */ 
            );
            /**Returns  the integrator type 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Motion::RecurdynSolverProperty::StaticIntegratorTypes StaticIntegratorType
            (
            );
            /**Sets  the integrator type 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetStaticIntegratorType
            (
                NXOpen::Motion::RecurdynSolverProperty::StaticIntegratorTypes integratorType /** integratortype */ 
            );
            /**Returns  the static error tolerance 
             <br>  @deprecated Deprecated in NX8.5.0.  Obtion the expression using @link NXOpen::Motion::RecurdynSolverProperty::DynamicNumericalDampingExpression NXOpen::Motion::RecurdynSolverProperty::DynamicNumericalDampingExpression@endlink  to query or edit it. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX8.5.0.  Obtion the expression using NXOpen::Motion::RecurdynSolverProperty::DynamicNumericalDampingExpression to query or edit it.") double StaticErrorTolerance
            (
            );
            /**Sets  the static error tolerance 
             <br>  @deprecated Deprecated in NX8.5.0.  Obtion the expression using @link NXOpen::Motion::RecurdynSolverProperty::DynamicNumericalDampingExpression NXOpen::Motion::RecurdynSolverProperty::DynamicNumericalDampingExpression@endlink  to query or edit it. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public:  NX_DEPRECATED("Deprecated in NX8.5.0.  Obtion the expression using NXOpen::Motion::RecurdynSolverProperty::DynamicNumericalDampingExpression to query or edit it.") void SetStaticErrorTolerance
            (
                double staticErrorTolerance /** staticerrortolerance */ 
            );
            /**Returns  the static max iteration 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: int StaticMaxIteration
            (
            );
            /**Sets  the static max iteration 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetStaticMaxIteration
            (
                int staticMaxIteration /** staticmaxiteration */ 
            );
            /**Returns  the static stability 
             <br>  @deprecated Deprecated in NX8.5.0.  Obtion the expression using @link NXOpen::Motion::RecurdynSolverProperty::StaticStabilityExpression NXOpen::Motion::RecurdynSolverProperty::StaticStabilityExpression@endlink  to query or edit it. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX8.5.0.  Obtion the expression using NXOpen::Motion::RecurdynSolverProperty::StaticStabilityExpression to query or edit it.") double StaticStability
            (
            );
            /**Sets  the static stability 
             <br>  @deprecated Deprecated in NX8.5.0.  Obtion the expression using @link NXOpen::Motion::RecurdynSolverProperty::StaticStabilityExpression NXOpen::Motion::RecurdynSolverProperty::StaticStabilityExpression@endlink  to query or edit it. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public:  NX_DEPRECATED("Deprecated in NX8.5.0.  Obtion the expression using NXOpen::Motion::RecurdynSolverProperty::StaticStabilityExpression to query or edit it.") void SetStaticStability
            (
                double staticStability /** staticstability */ 
            );
            /**Returns  the static initial step size 
             <br>  @deprecated Deprecated in NX8.5.0.  Obtion the expression using @link NXOpen::Motion::RecurdynSolverProperty::StaticInitialStepSizeExpression NXOpen::Motion::RecurdynSolverProperty::StaticInitialStepSizeExpression@endlink  to query or edit it. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX8.5.0.  Obtion the expression using NXOpen::Motion::RecurdynSolverProperty::StaticInitialStepSizeExpression to query or edit it.") double StaticInitialStepSize
            (
            );
            /**Sets  the static initial step size 
             <br>  @deprecated Deprecated in NX8.5.0.  Obtion the expression using @link NXOpen::Motion::RecurdynSolverProperty::StaticInitialStepSizeExpression NXOpen::Motion::RecurdynSolverProperty::StaticInitialStepSizeExpression@endlink  to query or edit it. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public:  NX_DEPRECATED("Deprecated in NX8.5.0.  Obtion the expression using NXOpen::Motion::RecurdynSolverProperty::StaticInitialStepSizeExpression to query or edit it.") void SetStaticInitialStepSize
            (
                double staticInitialStepSize /** staticinitialstepsize */ 
            );
            /**Returns  the static max step size 
             <br>  @deprecated Deprecated in NX8.5.0.  Obtion the expression using @link NXOpen::Motion::RecurdynSolverProperty::StaticMaxStepSizeExpression NXOpen::Motion::RecurdynSolverProperty::StaticMaxStepSizeExpression@endlink  to query or edit it. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX8.5.0.  Obtion the expression using NXOpen::Motion::RecurdynSolverProperty::StaticMaxStepSizeExpression to query or edit it.") double StaticMaxStepSize
            (
            );
            /**Sets  the static max step size 
             <br>  @deprecated Deprecated in NX8.5.0.  Obtion the expression using @link NXOpen::Motion::RecurdynSolverProperty::StaticMaxStepSizeExpression NXOpen::Motion::RecurdynSolverProperty::StaticMaxStepSizeExpression@endlink  to query or edit it. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public:  NX_DEPRECATED("Deprecated in NX8.5.0.  Obtion the expression using NXOpen::Motion::RecurdynSolverProperty::StaticMaxStepSizeExpression to query or edit it.") void SetStaticMaxStepSize
            (
                double staticMaxStepSize /** staticmaxstepsize */ 
            );
            /**Returns   the sampling time for co-simulation
             <br>  @deprecated Deprecated in NX8.5.0.  Obtion the expression using @link NXOpen::Motion::RecurdynSolverProperty::CosimSampleTimeExpression NXOpen::Motion::RecurdynSolverProperty::CosimSampleTimeExpression@endlink  to query or edit it. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX8.5.0.  Obtion the expression using NXOpen::Motion::RecurdynSolverProperty::CosimSampleTimeExpression to query or edit it.") double CosimSampleTime
            (
            );
            /**Sets   the sampling time for co-simulation
             <br>  @deprecated Deprecated in NX8.5.0.  Obtion the expression using @link NXOpen::Motion::RecurdynSolverProperty::CosimSampleTimeExpression NXOpen::Motion::RecurdynSolverProperty::CosimSampleTimeExpression@endlink  to query or edit it. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public:  NX_DEPRECATED("Deprecated in NX8.5.0.  Obtion the expression using NXOpen::Motion::RecurdynSolverProperty::CosimSampleTimeExpression to query or edit it.") void SetCosimSampleTime
            (
                double cosimSampleTime /** cosimsampletime */ 
            );
            /**Returns   the simulink model for co-simulation
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXString CosimSimModel
            (
            );
            /**Sets   the simulink model for co-simulation
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetCosimSimModel
            (
                const NXString & cosimSimModel /** cosimsimmodel */ 
            );
            /**Sets   the simulink model for co-simulation
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            void SetCosimSimModel
            (
                const char * cosimSimModel /** cosimsimmodel */ 
            );
            /**Returns  the dynamic initial step size expression
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * DynamicInitialStepSizeExpression
            (
            );
            /**Returns  the dynamic error tolerance expression
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * DynamicErrorToleranceExpression
            (
            );
            /**Returns  the dynamic max step size expression 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * DynamicMaxStepSizeExpression
            (
            );
            /**Returns  the dynamic numerical damping expression
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * DynamicNumericalDampingExpression
            (
            );
            /**Returns  the static error tolerance expression
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * StaticErrorToleranceExpression
            (
            );
            /**Returns  the static stability expression
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * StaticStabilityExpression
            (
            );
            /**Returns  the static initial step size expression
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * StaticInitialStepSizeExpression
            (
            );
            /**Returns  the static max step size expression
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * StaticMaxStepSizeExpression
            (
            );
            /**Returns  the redundant violation tolerance expression for length
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * RedundantViolationToleranceForLengthExpression
            (
            );
            /**Returns  the redundant violation tolerance expression for angle
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * RedundantViolationToleranceForAngleExpression
            (
            );
            /**Returns   the sampling time for co-simulation expression
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * CosimSampleTimeExpression
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
