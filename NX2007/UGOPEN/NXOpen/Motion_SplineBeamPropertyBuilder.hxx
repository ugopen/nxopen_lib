#ifndef NXOpen_MOTION_SPLINEBEAMPROPERTYBUILDER_HXX_INCLUDED
#define NXOpen_MOTION_SPLINEBEAMPROPERTYBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Motion_SplineBeamPropertyBuilder.ja
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
#include <NXOpen/Motion_CustomizedMaterialBuilder.hxx>
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
        class SplineBeamPropertyBuilder;
    }
    class Expression;
    namespace Motion
    {
        class CustomizedMaterialBuilder;
    }
    namespace Motion
    {
        class MotionBuilder;
    }
    namespace Motion
    {
        class _SplineBeamPropertyBuilderBuilder;
        class SplineBeamPropertyBuilderImpl;
        /** Represents a @link Motion::SplineBeamPropertyBuilder Motion::SplineBeamPropertyBuilder@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::Motion::SplineBeamPropertyCollection::CreateSplineBeamPropertyBuilder  NXOpen::Motion::SplineBeamPropertyCollection::CreateSplineBeamPropertyBuilder @endlink  <br> 
        Default values.
        <list type="table"> 
         
        <listheader><term> 
        Property</term>  <description> 
        Value</description> </listheader>
        <item><term> 
         
        AsyTimoshenkoCorrection.Value </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        AszTimoshenkoCorrection.Value </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        CustomizedMaterial.Density.Value </term> <description> 
         
        7.8e-6 (millimeters part), 7.3e-4 (inches part) </description> </item> 

        <item><term> 
         
        CustomizedMaterial.PoissonRatio.Value </term> <description> 
         
        0.3 </description> </item> 

        <item><term> 
         
        CustomizedMaterial.YoungModulus.Value </term> <description> 
         
        2e+8 (millimeters part), 2.9e+7 (inches part) </description> </item> 

        <item><term> 
         
        DampingRatio.Value </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        DampingType </term> <description> 
         
        Viscous </description> </item> 

        </list> 

         <br>  Created in NX12.0.0.  <br>  
        */
        class NXOPENCPP_MOTIONEXPORT  SplineBeamPropertyBuilder : public NXOpen::Motion::MotionBuilder
        {
            /** the damping type*/
            public: enum DampingTypes
            {
                DampingTypesViscous/** Viscous */,
                DampingTypesStructural/** Structural */
            };

            private: SplineBeamPropertyBuilderImpl * m_splinebeampropertybuilder_impl;
            private: friend class  _SplineBeamPropertyBuilderBuilder;
            protected: SplineBeamPropertyBuilder();
            public: ~SplineBeamPropertyBuilder();
            /**Returns  the name of the spline beam object 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: NXString Name
            (
            );
            /**Sets  the name of the spline beam object 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetName
            (
                const NXString & name /** name */ 
            );
            /**Sets  the name of the spline beam object 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            void SetName
            (
                const char * name /** name */ 
            );
            /**Returns  the customized material 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: NXOpen::Motion::CustomizedMaterialBuilder * CustomizedMaterial
            (
            );
            /**Returns  the ASY Timoshenko correction 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: NXOpen::Expression * AsyTimoshenkoCorrection
            (
            );
            /**Returns  the ASZ Timoshenko correction 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: NXOpen::Expression * AszTimoshenkoCorrection
            (
            );
            /**Returns  the damping method 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: NXOpen::Motion::SplineBeamPropertyBuilder::DampingTypes DampingType
            (
            );
            /**Sets  the damping method 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetDampingType
            (
                NXOpen::Motion::SplineBeamPropertyBuilder::DampingTypes type /** type */ 
            );
            /**Returns  the damping ratio 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: NXOpen::Expression * DampingRatio
            (
            );
            /**Returns  the beam cross damping flag 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: bool IsBeamCrossDamping
            (
            );
            /**Sets  the beam cross damping flag 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetBeamCrossDamping
            (
                bool type /** type */ 
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