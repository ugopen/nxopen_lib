#ifndef NXOpen_FEATURES_TOPOLOGYOPTIMIZATION_OPTIMIZATIONCONSTRAINTBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_TOPOLOGYOPTIMIZATION_OPTIMIZATIONCONSTRAINTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_TopologyOptimization_OptimizationConstraintBuilder.ja
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
#include <NXOpen/Features_TopologyOptimization_DesignSpace.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/ScCollector.hxx>
#include <NXOpen/libnxopencpp_features_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Features
    {
        namespace TopologyOptimization
        {
            class OptimizationConstraintBuilder;
        }
    }
    class Builder;
    class Direction;
    class Expression;
    namespace Features
    {
        namespace TopologyOptimization
        {
            class DesignSpace;
        }
    }
    class Point;
    class ScCollector;
    namespace Features
    {
        namespace TopologyOptimization
        {
            class _OptimizationConstraintBuilderBuilder;
            class OptimizationConstraintBuilderImpl;
            /** Represents a @link Features::TopologyOptimization::OptimizationConstraint Features::TopologyOptimization::OptimizationConstraint@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::Features::TopologyOptimization::Study::CreateOptimizationConstraintBuilder  NXOpen::Features::TopologyOptimization::Study::CreateOptimizationConstraintBuilder @endlink  <br> 
            Default values.
            <list type="table"> 
             
            <listheader><term> 
            Property</term>  <description> 
            Value</description> </listheader>
            <item><term> 
             
            Type </term> <description> 
             
            MaximumMassLimit </description> </item> 

            </list> 

             <br>  Created in NX1953.0.0.  <br>  
            */
            class NXOPENCPP_FEATURESEXPORT  OptimizationConstraintBuilder : public NXOpen::Builder
            {
                /** define optimization constraint type */
                public: enum ConstraintType
                {
                    ConstraintTypeMassTarget/** mass target */ ,
                    ConstraintTypeMinimumMassLimit/** minimum mass limit */ ,
                    ConstraintTypeMaximumMassLimit/** maximum mass limit */ ,
                    ConstraintTypeMaximumStressLimit/** maximum stress limit */ ,
                    ConstraintTypeMaximumDisplacementLimit/** maximum displacement limit */ ,
                    ConstraintTypeFirstFlexibleModeTarget/** first flexible mode target */ ,
                    ConstraintTypeMinimumFirstFlexibleModeLimit/** minimum first flexible mode limit */ ,
                    ConstraintTypeMaximumFirstFlexibleModeLimit/** maximum first flexible mode limit */ 
                };

                /** define maximum stress enum */
                public: enum MaximumStressOption
                {
                    MaximumStressOptionUltimateTensileStrength/** ultimate tensile strength */ ,
                    MaximumStressOptionYield/** yield */ 
                };

                /** define displacement enum */
                public: enum DisplacementOption
                {
                    DisplacementOptionAbsoluteMagnitude/** absolute magnitude */ ,
                    DisplacementOptionX/** x */ ,
                    DisplacementOptionY/** y */ ,
                    DisplacementOptionZ/** z */ ,
                    DisplacementOptionAlongVector/** along vector */ 
                };

                private: OptimizationConstraintBuilderImpl * m_optimizationconstraintbuilder_impl;
                private: friend class  _OptimizationConstraintBuilderBuilder;
                protected: OptimizationConstraintBuilder();
                public: ~OptimizationConstraintBuilder();
                /**Returns  the optimization constraint name 
                 <br>  Created in NX1953.0.0.  <br>  
                 <br> License requirements : None */
                public: NXString Name
                (
                );
                /**Sets  the optimization constraint name 
                 <br>  Created in NX1953.0.0.  <br>  
                 <br> License requirements : des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") */
                public: void SetName
                (
                    const NXString & optimizationConstraintName /** optimizationconstraintname */ 
                );
                /**Sets  the optimization constraint name 
                 <br>  Created in NX1953.0.0.  <br>  
                 <br> License requirements : des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") */
                void SetName
                (
                    const char * optimizationConstraintName /** optimizationconstraintname */ 
                );
                /**Returns  the mass expression 
                 <br>  Created in NX1953.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * Mass
                (
                );
                /**Returns  the minimum mass expression 
                 <br>  Created in NX1953.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * MinimumMass
                (
                );
                /**Returns  the maximum mass expression 
                 <br>  Created in NX1953.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * MaximumMass
                (
                );
                /**Returns  the maximum stress type 
                 <br>  Created in NX1953.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::TopologyOptimization::OptimizationConstraintBuilder::MaximumStressOption MaximumStressType
                (
                );
                /**Sets  the maximum stress type 
                 <br>  Created in NX1953.0.0.  <br>  
                 <br> License requirements : des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") */
                public: void SetMaximumStressType
                (
                    NXOpen::Features::TopologyOptimization::OptimizationConstraintBuilder::MaximumStressOption maxStressType /** maxstresstype */ 
                );
                /**Returns  the max percent of stress expression 
                 <br>  Created in NX1953.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * MaxPercentOfStress
                (
                );
                /**Returns  the select face 
                 <br>  Created in NX1953.0.0.  <br>  
                 <br> License requirements : des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") */
                public: NXOpen::ScCollector * SelectFace
                (
                );
                /**Returns  the defined location for displacement limit 
                 <br>  Created in NX1953.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Point * DisplacementLocation
                (
                );
                /**Sets  the defined location for displacement limit 
                 <br>  Created in NX1953.0.0.  <br>  
                 <br> License requirements : des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") */
                public: void SetDisplacementLocation
                (
                    NXOpen::Point * location /** location */ 
                );
                /**Returns  the displacement type 
                 <br>  Created in NX1953.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::TopologyOptimization::OptimizationConstraintBuilder::DisplacementOption DisplacementType
                (
                );
                /**Sets  the displacement type 
                 <br>  Created in NX1953.0.0.  <br>  
                 <br> License requirements : des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") */
                public: void SetDisplacementType
                (
                    NXOpen::Features::TopologyOptimization::OptimizationConstraintBuilder::DisplacementOption displacementType /** displacementtype */ 
                );
                /**Returns  the displacement vector 
                 <br>  Created in NX1953.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Direction * DisplacementVector
                (
                );
                /**Sets  the displacement vector 
                 <br>  Created in NX1953.0.0.  <br>  
                 <br> License requirements : des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") */
                public: void SetDisplacementVector
                (
                    NXOpen::Direction * displacementVector /** displacementvector */ 
                );
                /**Returns  the max displacement expression 
                 <br>  Created in NX1953.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * MaxDisplacement
                (
                );
                /**Returns  the first flexible frequency expression 
                 <br>  Created in NX1953.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * FirstFlexibleFrequency
                (
                );
                /**Returns  the min first flex frequency expression 
                 <br>  Created in NX1953.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * MinFirstFlexFrequency
                (
                );
                /**Returns  the max first flex frequency expression 
                 <br>  Created in NX1953.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * MaxFirstFlexFrequency
                (
                );
                /**Returns  the type 
                 <br>  Created in NX1953.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::TopologyOptimization::OptimizationConstraintBuilder::ConstraintType Type
                (
                );
                /**Sets  the type 
                 <br>  Created in NX1953.0.0.  <br>  
                 <br> License requirements : des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") */
                public: void SetType
                (
                    NXOpen::Features::TopologyOptimization::OptimizationConstraintBuilder::ConstraintType type /** type */ 
                );
                /**Returns  the design space 
                 <br>  Created in NX1953.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::TopologyOptimization::DesignSpace * DesignSpace
                (
                );
                /**Sets  the design space 
                 <br>  Created in NX1953.0.0.  <br>  
                 <br> License requirements : des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") */
                public: void SetDesignSpace
                (
                    NXOpen::Features::TopologyOptimization::DesignSpace * designSpace /** designspace */ 
                );
                /**Returns  the flag indicating whether the object uses an user-defined name 
                 <br>  Created in NX1953.0.0.  <br>  
                 <br> License requirements : None */
                public: bool UserSetName
                (
                );
                /**Sets  the flag indicating whether the object uses an user-defined name 
                 <br>  Created in NX1953.0.0.  <br>  
                 <br> License requirements : des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") */
                public: void SetUserSetName
                (
                    bool userSetName /** usersetname */ 
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
