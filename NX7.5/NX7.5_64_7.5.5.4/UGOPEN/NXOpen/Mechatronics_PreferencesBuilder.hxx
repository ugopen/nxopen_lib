#ifndef NXOpen_MECHATRONICS_PREFERENCESBUILDER_HXX_INCLUDED
#define NXOpen_MECHATRONICS_PREFERENCESBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Mechatronics_PreferencesBuilder.ja
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
#include <NXOpen/Builder.hxx>
#include <NXOpen/Expression.hxx>
#include <NXOpen/Mechatronics_PreferencesBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Mechatronics
    {
        class PreferencesBuilder;
    }
    class Builder;
    class Expression;
    namespace Mechatronics
    {
        class _PreferencesBuilderBuilder;
        class PreferencesBuilderImpl;
        /** Represents a @link Mechatronics::PreferencesBuilder Mechatronics::PreferencesBuilder@endlink  builder.  <br> To create a new instance of this class, use @link Mechatronics::PhysicsManager::CreatePreferenceBuilder Mechatronics::PhysicsManager::CreatePreferenceBuilder@endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        CollisionPrecision </td> <td> 
         
        0.1 </td> </tr> 

        <tr><td> 
         
        DynamicFriction </td> <td> 
         
        0.7 </td> </tr> 

        <tr><td> 
         
        ErrorReduction </td> <td> 
         
        50 </td> </tr> 

        <tr><td> 
         
        Gx.Value </td> <td> 
         
        0 (millimeters part), 0 (inches part) </td> </tr> 

        <tr><td> 
         
        Gy.Value </td> <td> 
         
        0 (millimeters part), 0 (inches part) </td> </tr> 

        <tr><td> 
         
        Gz.Value </td> <td> 
         
        -9806.65 (millimeters part), -386.09 (inches part) </td> </tr> 

        <tr><td> 
         
        MaxIteration </td> <td> 
         
        100 </td> </tr> 

        <tr><td> 
         
        Restitution </td> <td> 
         
        0.01 </td> </tr> 

        <tr><td> 
         
        SpringForceMultiplier </td> <td> 
         
        100 </td> </tr> 

        <tr><td> 
         
        StaticFriction </td> <td> 
         
        0.7 </td> </tr> 

        <tr><td> 
         
        StepTime </td> <td> 
         
        0.001 </td> </tr> 

        <tr><td> 
         
        Tolerance </td> <td> 
         
        0.1 </td> </tr> 

        </table>  
        */
        class NXOPENCPPEXPORT  PreferencesBuilder : public Builder
        {
            private: PreferencesBuilderImpl * m_preferencesbuilder_impl;
            private: friend class  _PreferencesBuilderBuilder;
            protected: PreferencesBuilder();
            public: ~PreferencesBuilder();
            /**Returns  the gx.  <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            public: NXOpen::Expression * Gx
            (
            );
            /**Returns  the gy.  <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            public: NXOpen::Expression * Gy
            (
            );
            /**Returns  the gz.  <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            public: NXOpen::Expression * Gz
            (
            );
            /**Returns  the dynamic friction.  <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            public: double DynamicFriction
            (
            );
            /**Sets  the dynamic friction.  <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            public: void SetDynamicFriction
            (
                double dynamicFriction /** dynamicfriction */ 
            );
            /**Returns  the static friction.  <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            public: double StaticFriction
            (
            );
            /**Sets  the static friction.  <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            public: void SetStaticFriction
            (
                double staticFriction /** staticfriction */ 
            );
            /**Returns  the restitution.  <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            public: double Restitution
            (
            );
            /**Sets  the restitution.  <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            public: void SetRestitution
            (
                double restitution /** restitution */ 
            );
            /**Returns  the collision precision.  <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            public: double CollisionPrecision
            (
            );
            /**Sets  the collision precision.  <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            public: void SetCollisionPrecision
            (
                double collisionPrecision /** collisionprecision */ 
            );
            /**Returns  the step time.  <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            public: double StepTime
            (
            );
            /**Sets  the step time.  <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            public: void SetStepTime
            (
                double stepTime /** steptime */ 
            );
            /**Returns  the spring force multiplier.  <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            public: double SpringForceMultiplier
            (
            );
            /**Sets  the spring force multiplier.  <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            public: void SetSpringForceMultiplier
            (
                double springForceMultiplier /** springforcemultiplier */ 
            );
            /**Returns  the tolerance.  <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            public: double Tolerance
            (
            );
            /**Sets  the tolerance.  <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            public: void SetTolerance
            (
                double tolerance /** tolerance */ 
            );
            /**Returns  the error reduction.  <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            public: double ErrorReduction
            (
            );
            /**Sets  the error reduction.  <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            public: void SetErrorReduction
            (
                double errorReduction /** errorreduction */ 
            );
            /**Returns  the max iteration.  <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            public: int MaxIteration
            (
            );
            /**Sets  the max iteration.  <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            public: void SetMaxIteration
            (
                int maxIter /** maxiter */ 
            );
            /**Returns  the inspector refresh precision.
                     This option specifies the refresh precision to be used by the inspector to determine whether to update property values in UI or not.  <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            public: double RefreshPrecision
            (
            );
            /**Sets  the inspector refresh precision.
                     This option specifies the refresh precision to be used by the inspector to determine whether to update property values in UI or not.  <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            public: void SetRefreshPrecision
            (
                double refreshPrecision /** refreshprecision */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif