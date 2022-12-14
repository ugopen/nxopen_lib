#ifndef NXOpen_CAE_RESPONSESIMULATION_HXX_INCLUDED
#define NXOpen_CAE_RESPONSESIMULATION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_ResponseSimulation.ja
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
            /** This enum defines interpolation method */
            enum InterpolationMethod
            {
                InterpolationMethodLogLog/** log log */ ,
                InterpolationMethodLinearLinear/** linear linear */ ,
                InterpolationMethodLinearLog/** linear log */ ,
                InterpolationMethodLogLinear/** log linear */ 
            };

            /** Specifies the evaluation result type */
            enum EvaluationResultType
            {
                EvaluationResultTypeReceptance/** receptance */ ,
                EvaluationResultTypeMobility/** mobility */ ,
                EvaluationResultTypeInertance/** inertance */ ,
                EvaluationResultTypeDisplacement/** displacement */ ,
                EvaluationResultTypeVelocity/** velocity */ ,
                EvaluationResultTypeAcceleration/** acceleration */ ,
                EvaluationResultTypeStress/** stress */ ,
                EvaluationResultTypeStrain/** strain */ ,
                EvaluationResultTypeStrainEnergy/** strain energy */ ,
                EvaluationResultTypeShellResultant/** shell resultant */ ,
                EvaluationResultTypeElementForce/** element force */ ,
                EvaluationResultTypeBeamElementForce/** beam element force */ ,
                EvaluationResultTypeShellStressResultant/** shell stress resultant */ ,
                EvaluationResultTypeReactionForce/** reaction force */ 
            };

            /** Specifies the coordinate system */
            enum CoordinateSystem
            {
                CoordinateSystemNodal/** nodal */ ,
                CoordinateSystemGlobal/** global */ ,
                CoordinateSystemElemental/** elemental */ ,
                CoordinateSystemMaterial/** material */ 
            };

            /** Specifies the direction data components */
            enum DirectionDataComponent
            {
                DirectionDataComponentX/** x */ ,
                DirectionDataComponentY/** y */ ,
                DirectionDataComponentZ/** z */ ,
                DirectionDataComponentRx/** rx */ ,
                DirectionDataComponentRy/** ry */ ,
                DirectionDataComponentRz/** rz */ ,
                DirectionDataComponentXx/** xx */ ,
                DirectionDataComponentYy/** yy */ ,
                DirectionDataComponentZz/** zz */ ,
                DirectionDataComponentXy/** xy */ ,
                DirectionDataComponentXz/** xz */ ,
                DirectionDataComponentYz/** yz */ ,
                DirectionDataComponentAx/** ax */ ,
                DirectionDataComponentSy/** sy */ ,
                DirectionDataComponentSz/** sz */ ,
                DirectionDataComponentTx/** tx */ ,
                DirectionDataComponentByy/** byy */ ,
                DirectionDataComponentBz/** bz */ ,
                DirectionDataComponentFxx/** fxx */ ,
                DirectionDataComponentFyy/** fyy */ ,
                DirectionDataComponentFzz/** fzz */ ,
                DirectionDataComponentFxy/** fxy */ ,
                DirectionDataComponentMx/** mx */ ,
                DirectionDataComponentMy/** my */ ,
                DirectionDataComponentMz/** mz */ ,
                DirectionDataComponentMxy/** mxy */ ,
                DirectionDataComponentMxz/** mxz */ ,
                DirectionDataComponentMyz/** myz */ ,
                DirectionDataComponentVx/** vx */ ,
                DirectionDataComponentVy/** vy */ ,
                DirectionDataComponentTranslationalMagnitude/** translational magnitude */ ,
                DirectionDataComponentVonmises/** vonmises */ ,
                DirectionDataComponentMaxPrincipal/** max principal */ ,
                DirectionDataComponentMinPrincipal/** min principal */ ,
                DirectionDataComponentMaxShear/** max shear */ ,
                DirectionDataComponentAllNormals/** all normals */ ,
                DirectionDataComponentAllTranslational/** all translational */ ,
                DirectionDataComponentAllForces/** all forces */ ,
                DirectionDataComponentAllDirections/** all directions */ ,
                DirectionDataComponentAllDataComponents/** all data components */ ,
                DirectionDataComponentAll/** all */ ,
                DirectionDataComponentAllXyPlane/** all xy plane */ ,
                DirectionDataComponentLeg1/** leg1 */ ,
                DirectionDataComponentLeg2/** leg2 */ ,
                DirectionDataComponentLeg3/** leg3 */ ,
                DirectionDataComponentAllLegs/** all legs */ 
            };

            /** Specifies response request for nodal function evaluation */
            enum NodalFunctionEvalRequest
            {
                NodalFunctionEvalRequestUserDefinedDirection/** user defined direction */ ,
                NodalFunctionEvalRequestDataComponent/** data component */ 
            };

            /** Specifies beam element evaluation locations for nodal function evaluation */
            enum NodalFunctionEvalBeamLocation
            {
                NodalFunctionEvalBeamLocationC/** Stress Recovery point C on a beam cross section */,
                NodalFunctionEvalBeamLocationD/** Stress Recovery point D on a beam cross section */,
                NodalFunctionEvalBeamLocationE/** Stress Recovery point E on a beam cross section */,
                NodalFunctionEvalBeamLocationF/** Stress Recovery point F on a beam cross section */,
                NodalFunctionEvalBeamLocationAll/** All four Stress Recovery points on a beam cross section */
            };

            /** Specifies shell element evaluation locations for nodal function evaluation */
            enum NodalFunctionEvalShellLocation
            {
                NodalFunctionEvalShellLocationTop/** Top layer */,
                NodalFunctionEvalShellLocationMiddle/** Middle layer */,
                NodalFunctionEvalShellLocationBottom/** Bottom layer */,
                NodalFunctionEvalShellLocationAll/** All three layers */
            };

            /** Specifies beam element evaluation locations */
            enum ElementalFunctionEvalBeamLocation
            {
                ElementalFunctionEvalBeamLocationC/** c */ ,
                ElementalFunctionEvalBeamLocationD/** d */ ,
                ElementalFunctionEvalBeamLocationE/** e */ ,
                ElementalFunctionEvalBeamLocationF/** f */ 
            };

            /** Specifies shell element evaluation locations */
            enum ShellElementEvaluationLocation
            {
                ShellElementEvaluationLocationTop/** top */ ,
                ShellElementEvaluationLocationMiddle/** middle */ ,
                ShellElementEvaluationLocationBottom/** bottom */ 
            };

            /** Specifies element locations */
            enum ElementLocation
            {
                ElementLocationBoth/** both */ ,
                ElementLocationCentroid/** centroid */ ,
                ElementLocationCorners/** corners */ 
            };

            /** Specifies response result evaluation options*/
            enum ResponseDomainDefinitionMethod
            {
                ResponseDomainDefinitionMethodStartEndPoint/** start end point */ ,
                ResponseDomainDefinitionMethodKeyIn/** key in */ ,
                ResponseDomainDefinitionMethodNaturalFrequency/** natural frequency */ 
            };

            /** Specifies nodal averaging options */
            enum NodalAveragingOption
            {
                NodalAveragingOptionShells/** shells */ ,
                NodalAveragingOptionSolids/** solids */ 
            };

            /** Specifies strength stress criteria */
            enum StrengthStressCriteria
            {
                StrengthStressCriteriaVonMises/** von mises */ ,
                StrengthStressCriteriaMaxPrinciple/** max principle */ ,
                StrengthStressCriteriaMinPrinciple/** min principle */ 
            };

            /** The options of stress */
            enum StrengthStressOption
            {
                StrengthStressOptionElementMaximum/** element maximum */ ,
                StrengthStressOptionNodeOnElement/** node on element */ 
            };

            /** Specifies the definition method for material */
            enum StrengthStressMaterialDefinitionMethod
            {
                StrengthStressMaterialDefinitionMethodUltimateSafety/** ultimate safety */ ,
                StrengthStressMaterialDefinitionMethodYieldSafety/** yield safety */ 
            };

            /** Specifies the type of Sensor */
            enum SensorType
            {
                SensorTypeComponent/** component */ ,
                SensorTypeDirection/** direction */ ,
                SensorTypeNormal/** normal */ 
            };

            /** Specifies the result type of Sensor */
            enum SensorResultType
            {
                SensorResultTypeDisplacement/** displacement */ ,
                SensorResultTypeVelocity/** velocity */ ,
                SensorResultTypeAcceleration/** acceleration */ ,
                SensorResultTypeReactionForce/** reaction force */ 
            };

            /** Specifies the coordinate type of Sensor */
            enum SensorCoordinateType
            {
                SensorCoordinateTypeNodalCs/** nodal cs */ ,
                SensorCoordinateTypeGlobalCs/** global cs */ 
            };

            /** Specifies the type of Strain Gage */
            enum StrainGageType
            {
                StrainGageTypeUniAxial/** uni axial */ ,
                StrainGageTypeBiAxial/** bi axial */ ,
                StrainGageTypeRosette45DegreeIncrement/** Rosette 0-45-90 */,
                StrainGageTypeRosette60DegreeIncrement/** Rosette 0-60-120 */
            };

            /** Specifies the result type of Strain Gage */
            enum StrainGageResult
            {
                StrainGageResultStrain/** strain */ ,
                StrainGageResultStress/** stress */ 
            };

            /** Specifies the placement type of Strain Gage */
            enum StrainGagePlacementType
            {
                StrainGagePlacementTypeNode/** node */ ,
                StrainGagePlacementTypeElementFaceCenter/** element face center */ 
            };

            /** Specifies the shell element location type of Strain Gage */
            enum StrainGageShellElementFaceType
            {
                StrainGageShellElementFaceTypeTop/** top */ ,
                StrainGageShellElementFaceTypeBotton/** botton */ 
            };

            /** Specifies the orientation plane type of Strain Gage */
            enum StrainGageOrientationPlane
            {
                StrainGageOrientationPlaneFacePlane/** face plane */ ,
                StrainGageOrientationPlaneCsys/** csys */ 
            };

            /** Specifies the evaluation method for RMS or LCR calculation */
            enum RmsLcrEvaluationMethod
            {
                RmsLcrEvaluationMethodSmallNumberItems/** Small number of evaluation items */,
                RmsLcrEvaluationMethodLargeNumberItems/** Large number of evaluation items */,
                RmsLcrEvaluationMethodAutomaticSelection/** Automatic selection */
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

#endif
