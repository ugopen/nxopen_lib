#ifndef NXOpen_CAE_CONNECTIONS_TYPES_HXX_INCLUDED
#define NXOpen_CAE_CONNECTIONS_TYPES_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_Connections_Types.ja
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
        namespace Connections
        {
            /** Material definition types */
            enum MaterialType
            {
                MaterialTypeUser/** User defined material */,
                MaterialTypeFromSupport/** Material defined from support */,
                MaterialTypeNone/** No material required */
            };

            /** Diameter definition types */
            enum DiameterType
            {
                DiameterTypeUser/** User defined diameter */,
                DiameterTypeFormula/** Formula defined diameter */,
                DiameterTypeTableFile/** Table defined diameter */,
                DiameterTypeFlangeHoleDetection/** Flange hole defined diameter */
            };

            /** Types of height definitions */
            enum HeightType
            {
                HeightTypeUndefined/** Undefined height type, used for connections that don't use this parameter */ = -1,
                HeightTypeUser/** User defined thickness */,
                HeightTypeMeanOfFlangesThickness/** Mean of flanges thickness */,
                HeightTypeDistanceBetweenFlanges/** Distance between flanges */,
                HeightTypeDistanceBetweenFlangesMeanOfFlangesThickness/** Distance between flanges - Mean of flanges thickness */,
                HeightTypeDistanceBetweenFlangesMaxOfFlangesThickness/** Distance between flanges - Max of flanges thickness */,
                HeightTypeDistanceBetweenFlangesAndMeanOfFlangesThickness/** Distance between flanges + Mean of the Flange Thickness */
            };

            /** Location type */
            enum LocationType
            {
                LocationTypeCoordinates/** Coordinates */,
                LocationTypePoint/** Point */,
                LocationTypeNode/** Node */,
                LocationTypeSeriesOfNodes/** Series Of Nodes */,
                LocationTypeSeriesOfCoordinates/** Series Of Coordinates*/,
                LocationTypeCurve/** Curve */,
                LocationTypeFeEdgeGroup/** Group Of Element Edges */,
                LocationTypeSeriesOfPoints/** Series Of Points */,
                LocationTypeLocationWithDirection/** Location with direction */,
                LocationTypeSelectionRecipe/** Selection Recipe */,
                LocationTypeMeshPoint/** Mesh Point */
            };

            /** Csys types */
            enum CsysType
            {
                CsysTypeExisting/** Existing CSYS */,
                CsysTypePredefined/** Predefined CSYS */,
                CsysTypeAbsolute/** Absolute CSYS */,
                CsysTypeLocalCartesian/** Local Cartesian CSYS */,
                CsysTypeLocalCylindrical/** Local Cylindrical CSYS */,
                CsysTypeLocalSpherical/** Local Spherical CSYS */
            };

            /** Element status */
            enum ElementStatusType
            {
                ElementStatusTypeInvalid/** Invalid */,
                ElementStatusTypeNotUpdated/** Not updated */,
                ElementStatusTypeUpdated/** Updated */
            };

            /** Modelization PPTRefTargetType */
            enum ModelizationPPTRefTargetType
            {
                ModelizationPPTRefTargetTypeNone/** None */,
                ModelizationPPTRefTargetTypeEc/** Element collector */,
                ModelizationPPTRefTargetTypeEcc/** Element collector container */,
                ModelizationPPTRefTargetTypeEad/** Element Associated Data */
            };

            /** Modelization result type */
            enum ModelizationResultType
            {
                ModelizationResultTypeNone/** None */,
                ModelizationResultTypeMaterial/** Material */,
                ModelizationResultTypeWeights/** Interpolation element weights */,
                ModelizationResultTypeSection/** Section */,
                ModelizationResultTypeCsys/** Csys */,
                ModelizationResultTypeStiffness/** Stiffness */,
                ModelizationResultTypeViscousDamping/** ViscousDamping */,
                ModelizationResultTypeStructuralDamping/** StructuralDamping */,
                ModelizationResultTypeDofs/** Dofs */,
                ModelizationResultTypeDynamicStiffness/** Dynamic Stiffness */,
                ModelizationResultTypeDynamicViscousDamping/** Dynamic ViscousDamping */,
                ModelizationResultTypeDynamicStructuralDamping/** Dynamic StructuralDamping */,
                ModelizationResultTypeFriction/** Friction */
            };

            /** Shank length discretization definition types */
            enum ShankLengthDiscretizationType
            {
                ShankLengthDiscretizationTypeNone/** No shank discretization for shank length */,
                ShankLengthDiscretizationTypeUserDefined/** User defined length for shank discretization */,
                ShankLengthDiscretizationTypePercentLength/** Percentage of length for shank discretization */,
                ShankLengthDiscretizationTypePercentCurve/** Percentage of curve length for shank discretization */
            };

            /** Shank segment discretization definition types */
            enum ShankSegmentDiscretizationType
            {
                ShankSegmentDiscretizationTypeNone/** No shank discretization for shank segments */,
                ShankSegmentDiscretizationTypeSegmentLength/** Segment length for shank segment discretization */,
                ShankSegmentDiscretizationTypeNumSegments/** Number of segments for shank segment discretization */
            };

            /** Head diameter definition types */
            enum HeadDiameterType
            {
                HeadDiameterTypeUser/** User defined diameter */,
                HeadDiameterTypeFactorOfDiameter/** User defined relationship with bolt diameter */
            };

            /** Location and Direction type */
            enum LocationDirectionType
            {
                LocationDirectionTypePoint/** Two Points/Nodes */,
                LocationDirectionTypeVector/** Points/Node and Vector */,
                LocationDirectionTypeCurve/** Curves */,
                LocationDirectionTypeSelectionRecipes/** Selection Recipes */
            };

            /** Seam Weld xMCF Type (describes the weld topology) */
            enum SeamWeldMcfType
            {
                SeamWeldMcfTypeOther/** Unspecified */,
                SeamWeldMcfTypeYJoint/** Y-Joint */,
                SeamWeldMcfTypeOverlapWeld/** Overlap Weld */,
                SeamWeldMcfTypeCornerWeld/** Corner Weld */,
                SeamWeldMcfTypeButtJoint/** Butt Joint */,
                SeamWeldMcfTypeEdgeWeld/** Edge Weld */,
                SeamWeldMcfTypeDoubleCornerWeld/** Corner Weld (Double) */,
                SeamWeldMcfTypeCruciformJoint/** Cruciform Joint */,
                SeamWeldMcfTypeKJoint/** K-Joint */,
                SeamWeldMcfTypeIWeld/** I-Weld */,
                SeamWeldMcfTypeSplitIWeld/** Split I-Weld */
            };

            /** Seam Weld Type */
            enum SeamWeldType
            {
                SeamWeldTypeWithMaterial/** Seam weld done with material */,
                SeamWeldTypeWithLaser/** Seam weld done by laser */,
                SeamWeldTypeResistance/** Seam weld done by resistance welding */,
                SeamWeldTypeFriction/** Seam weld done by friction welding */,
                SeamWeldTypeBrazing/** Seam weld done by braze welding */
            };

            /** Seam Weld Material type */
            enum SeamWeldMaterialType
            {
                SeamWeldMaterialTypeAngle/** Seam weld angle material type */,
                SeamWeldMaterialTypeOverlap/** Seam weld overlap material type */,
                SeamWeldMaterialTypeDouble/** Seam weld double material type */
            };

            /** Seam Weld Section type */
            enum SeamWeldSectionType
            {
                SeamWeldSectionTypeI/** i */ ,
                SeamWeldSectionTypeV/** v */ ,
                SeamWeldSectionTypeU/** u */ ,
                SeamWeldSectionTypeX/** x */ ,
                SeamWeldSectionTypeY/** y */ ,
                SeamWeldSectionTypeHv/** hv */ ,
                SeamWeldSectionTypeHy/** hy */ ,
                SeamWeldSectionTypeFillet/** fillet */ ,
                SeamWeldSectionTypeRadius/** radius */ 
            };

            /** Seam Weld Shape type */
            enum SeamWeldShapeType
            {
                SeamWeldShapeTypeStraight/** straight */ ,
                SeamWeldShapeTypeConvex/** convex */ ,
                SeamWeldShapeTypeConcave/** concave */ 
            };

            /** Seam Weld Location type */
            enum SeamWeldLocationType
            {
                SeamWeldLocationTypeVector/** vector */ ,
                SeamWeldLocationTypeFlange1Side1/** flange1side1 */ ,
                SeamWeldLocationTypeFlange1Side2/** flange1side2 */ ,
                SeamWeldLocationTypeFlange2Side1/** flange2side1 */ ,
                SeamWeldLocationTypeFlange2Side2/** flange2side2 */ 
            };

            /** Seam Weld Node Selection Method */
            enum SeamWeldNodeSelectionMethod
            {
                SeamWeldNodeSelectionMethodConnectionNodes/** Use the node locations in the USWC(s) */,
                SeamWeldNodeSelectionMethodSpecify/** Explicitly specify nodes or a node group */
            };

            /** Degrees Of Freedom types */
            enum DofType
            {
                DofTypeFree/** The DOF is not constrained */,
                DofTypeFixed/** The DOF is fixed */
            };

            /** Degrees Of Freedom Combination types */
            enum DofCombination
            {
                DofCombinationUserDefined/** User defined combination for all DOFs */,
                DofCombinationFixed/** DOF1 fixed, DOF2 fixed, DOF3 fixed, DOF4 fixed, DOF5 fixed, DOF6 fixed */,
                DofCombinationSpherical/** DOF1 fixed, DOF2 fixed, DOF3 fixed, DOF4 free,  DOF5 free,  DOF6 free */,
                DofCombinationInplane/** DOF1 fixed, DOF2 free,  DOF3 free,  DOF4 free,  DOF5 free,  DOF6 free */,
                DofCombinationSlider/** DOF1 free,  DOF2 fixed, DOF3 fixed, DOF4 fixed, DOF5 fixed, DOF6 fixed */,
                DofCombinationRevolute/** DOF1 fixed, DOF2 fixed, DOF3 fixed, DOF4 free,  DOF5 fixed, DOF6 fixed */,
                DofCombinationCylindrical/** DOF1 free,  DOF2 fixed, DOF3 fixed, DOF4 free,  DOF5 fixed, DOF6 fixed */,
                DofCombinationUniversal/** DOF1 fixed, DOF2 fixed, DOF3 fixed, DOF4 free,  DOF5 fixed, DOF6 free */,
                DofCombinationSliderUniversal/** DOF1 free,  DOF2 fixed, DOF3 fixed, DOF4 free,  DOF5 fixed, DOF6 free */,
                DofCombinationInline/** DOF1 free,  DOF2 fixed, DOF3 fixed, DOF4 free,  DOF5 free, DOF6 free */
            };

            /** Nodal Target types */
            enum NodalTargetType
            {
                NodalTargetTypeSinglePoint/** Single Point */,
                NodalTargetTypeSetOfPoints/** Set of Points */,
                NodalTargetTypeSpider/** Spider */,
                NodalTargetTypeNone/** None */,
                NodalTargetTypeLocalSpider/** Local Spider */
            };

            /** Degrees of freedom definition */
            enum Dof
            {
                DofX/** X Translation degree of freedom */,
                DofY/** Y Translation degree of freedom */,
                DofZ/** Z Translation degree of freedom */,
                DofRx/** X Rotation degree of freedom */,
                DofRy/** Y Rotation degree of freedom */,
                DofRz/** Z Rotation degree of freedom */
            };

            /** Nodal pairing method */
            enum NodalPairingMethod
            {
                NodalPairingMethodProximity/** Proximity */,
                NodalPairingMethodOrientatedSearch/** Oriented Search */,
                NodalPairingMethodSelectionOrder/** Selection Order */
            };

            /** Nodal target dependency type */
            enum TargetDependencyType
            {
                TargetDependencyTypeNone/** No dependency */,
                TargetDependencyTypeDependent/** Dependent target */,
                TargetDependencyTypeIndependent/** Independent target */
            };

            /** connection DB item stiffness type */
            enum ConnectionDBItemStiffnessType
            {
                ConnectionDBItemStiffnessTypeNone/** None */,
                ConnectionDBItemStiffnessTypeRectangular/** Rectangular */,
                ConnectionDBItemStiffnessTypeSpherical/** Spherical */,
                ConnectionDBItemStiffnessTypeCylindrical/** Cylindrical */
            };

            /** lumped mass type */
            enum MassType
            {
                MassTypeOnNodes/** Mass applied on selected nodes */,
                MassTypeWithSpiders/** Mass with defined spider */
            };

            /** lumped mass distribution type */
            enum MassDistributionType
            {
                MassDistributionTypeDistributed/** Mass is distributed on selected nodes */,
                MassDistributionTypeRepeated/** Mass is applied at the defined value on each node  */
            };

            /** mass connectivity type */
            enum MassConnectivityType
            {
                MassConnectivityTypeNearestNodes/** nearest nodes on defined panels */,
                MassConnectivityTypeLocalSpiders/** locally created spiders */
            };

            /** nodal ring search type */
            enum RingSearchType
            {
                RingSearchTypeOneRing/** One Ring */,
                RingSearchTypeTwoRings/** Two Rings */,
                RingSearchTypeExpansionRadius/** Search by exansion radius */,
                RingSearchTypeExpansionRadiusFactor/** Search by exansion radius factor */
            };

            /** panels search type */
            enum PanelSearchType
            {
                PanelSearchTypeNearestSelectedPanel/** Apply on the closest panel */,
                PanelSearchTypeAllSelectedPanels/** Apply on all selected panels */
            };

            /** line locations discretization method */
            enum DiscretizationMethod
            {
                DiscretizationMethodStepLength/** Discretize the line using step length */,
                DiscretizationMethodNumberOfPoints/** Discretize the line using the total number of points */
            };

            /** Seam Weld Side */
            enum SeamWeldSide
            {
                SeamWeldSideOnLargerSheetAngle/** Weld on Side of the Larger Sheet Angle */,
                SeamWeldSideOnSmallerSheetAngle/** Weld on Side of the Smaller Sheet Angle */,
                SeamWeldSideOnBothSheetSides/** Weld on Both Sides */
            };

            /** Stiffness type */
            enum StiffnessType
            {
                StiffnessTypePerElement/** Stiffness value will be specified per element */,
                StiffnessTypePerUnitLength/** Stiffness value will be specified per unit length */
            };

            /** Nodal Target Center Types */
            enum NodalTargetCenterType
            {
                NodalTargetCenterTypeManual/** CoG is picked by selection */,
                NodalTargetCenterTypeFromSpiderDefinition/** Use the spider definition to get the CoG */,
                NodalTargetCenterTypeCoincident/** The CoG is coincident with the other target CoG */
            };

            /** Universal Connection Status */
            enum UniversalConnectionState
            {
                UniversalConnectionStateUnknown/** Connection state cannot be determined */,
                UniversalConnectionStateMeshed/** The Connection is meshed */,
                UniversalConnectionStateNotMeshed/** The Connection is not meshed */,
                UniversalConnectionStateInvalid/** The Connection is not valid */
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
