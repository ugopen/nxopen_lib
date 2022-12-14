#ifndef NXOpen_CAEOBJVALIDATIONBUILDER_HXX_INCLUDED
#define NXOpen_CAEOBJVALIDATIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CaeObjValidationBuilder.ja
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
#include <NXOpen/libnxopendebugsessioncpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    class CaeObjValidationBuilder;
    class Builder;
    namespace CAE
    {
        class CAEBody;
    }
    namespace CAE
    {
        class Mesh;
    }
    namespace CAE
    {
        class SimSolution;
    }
    namespace CAE
    {
        class SimSolutionStep;
    }
    class Expression;
    class _CaeObjValidationBuilderBuilder;
    class CaeObjValidationBuilderImpl;

    /// \cond NX_NO_DOC 
    /** Represents a @link CaeObjValidationBuilder CaeObjValidationBuilder@endlink  builder which can be used to validate Cae Objects
          as within Autotests.  <br> An instance of this class can be obtained through  @link CAE::CaeAutotest CAE::CaeAutotest@endlink    <br> 
     <br>  Created in NX7.5.0.  <br>  
    */
    class NXOPENDEBUGSESSIONCPPEXPORT  CaeObjValidationBuilder : public NXOpen::Builder
    {
        /** represents the type of CAE objects that can be validated */

        /// \cond NX_NO_DOC 
        public: enum ValidationType
        {
            ValidationTypeConstraintSet/** Constraint Sets */,
            ValidationTypeConstraints/** Constraints */,
            ValidationTypeDataSource/** DataSources */,
            ValidationTypeExpressions/** Expressions */,
            ValidationTypeFemDataSet/** FemDataSet */,
            ValidationTypeFields/** Fields */,
            ValidationTypeFieldFolder/** Field Folders */,
            ValidationTypeGeometryOptimizations/** Geometry Optimizations */,
            ValidationTypeGroups/** Groups */,
            ValidationTypeLoadRecipe/** Load Recipes */,
            ValidationTypeLoadSet/** Load Sets */,
            ValidationTypeLoads/** Loads */,
            ValidationTypeFolder/** LBC Folders */,
            ValidationTypeMad/** Meshes - prop table only */,
            ValidationTypeMainObjects/** Main Objects */,
            ValidationTypeMeshBoundingBox/** Meshes - Bounding Box */,
            ValidationTypeMeshCollectors/** Mesh Collectors */,
            ValidationTypeMeshNodePositions/** Meshes - All Node Positions */,
            ValidationTypeMeshes/** Meshes - all data */,
            ValidationTypeMetaSolutions/** MetaSolutions */,
            ValidationTypeMetaSolutionSteps/** MetaSolutions steps */,
            ValidationTypePhysicalProperties/** Physical Properties */,
            ValidationTypePolygonBodies/** Polygon Bodies */,
            ValidationTypeRegions/** Regions */,
            ValidationTypeSSMOs/** SSMOs */,
            ValidationTypeSSSOs/** SSSOs */,
            ValidationTypeSections/** Sections */,
            ValidationTypeSelectionRecipe/** Selection Recipes */,
            ValidationTypeSolutionSteps/** Solution Steps */,
            ValidationTypeSolutions/** Solutions */,
            ValidationTypeDurSpecialistEvents/** Durability Specialist Event*/,
            ValidationTypeDurSpecialistWeldSets/** Durability Specialist Weld Sets*/,
            ValidationTypeStressLinearizations/** Stress Linearizations*/
        };


        /// \endcond 
        private: CaeObjValidationBuilderImpl * m_caeobjvalidationbuilder_impl;
        private: friend class  _CaeObjValidationBuilderBuilder;
        protected: CaeObjValidationBuilder();
        public: ~CaeObjValidationBuilder();

        /// \cond NX_NO_DOC 
        /**Returns  the type to validate 
         <br>  Created in NX7.5.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::CaeObjValidationBuilder::ValidationType TypeToValidate
        (
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /**Sets  the type to validate 
         <br>  Created in NX7.5.0.  <br>  
         <br> License requirements : None */
        public: void SetTypeToValidate
        (
            NXOpen::CaeObjValidationBuilder::ValidationType typeToValidate /** typetovalidate */ 
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /**Returns  the include occs 
         <br>  Created in NX7.5.0.  <br>  
         <br> License requirements : None */
        public: bool IncludeOccs
        (
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /**Sets  the include occs 
         <br>  Created in NX7.5.0.  <br>  
         <br> License requirements : None */
        public: void SetIncludeOccs
        (
            bool includeOccs /** includeoccs */ 
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /**Returns  the output solution props flag 
         <br>  Created in NX12.0.0.  <br>  
         <br> License requirements : None */
        public: bool OutputSolProps
        (
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /**Sets  the output solution props flag 
         <br>  Created in NX12.0.0.  <br>  
         <br> License requirements : None */
        public: void SetOutputSolProps
        (
            bool outputSolProps /** outputsolprops */ 
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /**Returns  the output solution solver params flag 
         <br>  Created in NX12.0.0.  <br>  
         <br> License requirements : None */
        public: bool OutputSolSolverParams
        (
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /**Sets  the output solution solver params flag 
         <br>  Created in NX12.0.0.  <br>  
         <br> License requirements : None */
        public: void SetOutputSolSolverParams
        (
            bool outputSolSolverParams /** outputsolsolverparams */ 
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /**Returns  the output solution steps flag 
         <br>  Created in NX12.0.0.  <br>  
         <br> License requirements : None */
        public: bool OutputSolSteps
        (
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /**Sets  the output solution steps flag 
         <br>  Created in NX12.0.0.  <br>  
         <br> License requirements : None */
        public: void SetOutputSolSteps
        (
            bool outputSolSteps /** outputsolsteps */ 
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /**Returns  the output solution groups flag 
         <br>  Created in NX12.0.0.  <br>  
         <br> License requirements : None */
        public: bool OutputSolGroups
        (
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /**Sets  the output solution groups flag 
         <br>  Created in NX12.0.0.  <br>  
         <br> License requirements : None */
        public: void SetOutputSolGroups
        (
            bool outputSolGroups /** outputsolgroups */ 
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /**Returns  the output conflicts flag 
         <br>  Created in NX1847.0.0.  <br>  
         <br> License requirements : None */
        public: bool OutputConflicts
        (
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /**Sets  the output conflicts flag 
         <br>  Created in NX1847.0.0.  <br>  
         <br> License requirements : None */
        public: void SetOutputConflicts
        (
            bool outputConflicts /** outputconflicts */ 
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /**Returns  the output solution step props flag 
         <br>  Created in NX12.0.0.  <br>  
         <br> License requirements : None */
        public: bool OutputSolStepProps
        (
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /**Sets  the output solution step props flag 
         <br>  Created in NX12.0.0.  <br>  
         <br> License requirements : None */
        public: void SetOutputSolStepProps
        (
            bool outputSolStepProps /** outputsolstepprops */ 
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /**Returns  the output solution step groups flag 
         <br>  Created in NX12.0.0.  <br>  
         <br> License requirements : None */
        public: bool OutputSolStepGroups
        (
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /**Sets  the output solution step groups flag 
         <br>  Created in NX12.0.0.  <br>  
         <br> License requirements : None */
        public: void SetOutputSolStepGroups
        (
            bool outputSolStepGroups /** outputsolstepgroups */ 
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /** Print Mesh Associated Data 
         <br>  Created in NX7.5.2.  <br>  
         <br> License requirements : None */
        public: void PrintMad
        (
            NXOpen::CAE::Mesh * meshTag /**Mesh*/
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /** Print Mesh Associated Data With Start and End Tag 
         <br>  Created in NX1980.0.0.  <br>  
         <br> License requirements : None */
        public: void PrintMadWithStartAndEndTag
        (
            NXOpen::CAE::Mesh * meshTag /**Mesh*/
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /** Print mesh basic position information: its bounding box. 
         <br>  Created in NX11.0.0.  <br>  
         <br> License requirements : None */
        public: void PrintMeshBoundingBox
        (
            NXOpen::CAE::Mesh * meshTag /**Mesh*/
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /** Print mesh detailed position information: detailed list of node coordinates 
         <br>  Created in NX11.0.0.  <br>  
         <br> License requirements : None */
        public: void PrintMeshNodePositions
        (
            NXOpen::CAE::Mesh * meshTag /**Mesh*/
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /** Print Mesh Associated Data 
         <br>  Created in NX8.0.0.  <br>  
         <br> License requirements : None */
        public: void ValidateAll
        (
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /** Validate Polygon Body 
         <br>  Created in NX9.0.0.  <br>  
         <br> License requirements : None */
        public: void ValidatePolygonBody
        (
            NXOpen::CAE::CAEBody * bodyTag /**Polygon Body*/
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /** Validate Expression 
         <br>  Created in NX9.0.0.  <br>  
         <br> License requirements : None */
        public: void ValidateExpression
        (
            NXOpen::Expression * bodyTag /**Expression*/
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /** Validate Solution 
         <br>  Created in NX12.0.0.  <br>  
         <br> License requirements : None */
        public: void ValidateSolution
        (
            NXOpen::CAE::SimSolution * solTag /**Solution*/
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /** Validate Solution Step 
         <br>  Created in NX12.0.0.  <br>  
         <br> License requirements : None */
        public: void ValidateSolutionStep
        (
            NXOpen::CAE::SimSolutionStep * solStepTag /**Solution Step*/
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /** Cleanup preforms all necessary functions prior after all validation and print calls.
                    For example if needed this will do an Update if objects we added to update list during validation. 
         <br>  Created in NX1847.0.0.  <br>  
         <br> License requirements : None */
        public: void Cleanup
        (
        );

        /// \endcond 
    };

    /// \endcond 
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
