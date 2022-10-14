#ifndef NXOpen_SELECTIONINTENTRULE_HXX_INCLUDED
#define NXOpen_SELECTIONINTENTRULE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     SelectionIntentRule.ja
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
#include <NXOpen/TransientObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    class SelectionIntentRule;
    /** Selection Intent method to use with follow fillet rule. */
    enum FollowFilletRuleType
    {
        FollowFilletRuleTypeConnected/** Connected Curves */,
        FollowFilletRuleTypeTangent/** Tangent Curves */
    };

    /** Selection Intent method to use with apparent chaining.
    */
    enum ApparentChainingRuleType
    {
        ApparentChainingRuleTypeConnected/** Connected Curves */,
        ApparentChainingRuleTypeTangent/** Tangent Curves */,
        ApparentChainingRuleTypeDumb/** Dumb Curves */
    };

    /** Selection Intent filter method to use with apparent chaining.
    */
    enum ApparentChainingRuleSelection
    {
        ApparentChainingRuleSelectionAllowAllTypes/** allow all types */ ,
        ApparentChainingRuleSelectionAllowCurve/** allow curve */ ,
        ApparentChainingRuleSelectionAllowEdge/** allow edge */ 
    };

    class SelectionIntentRuleImpl;
    /** Represents a @link  NXOpen::SelectionIntentRule   NXOpen::SelectionIntentRule @endlink  which essentially provides capabilities to collect 
    curves, edges, faces and bodies. The intent of the collection is remembered as a rule in the corresponding 
    @link  NXOpen::Section   NXOpen::Section @endlink  or @link  NXOpen::ScCollector   NXOpen::ScCollector @endlink .

     <br>  Created in NX3.0.0.  <br>  
    */
    class NXOPENCPPEXPORT  SelectionIntentRule : public NXOpen::TransientObject
    {
        /** This enum represents the type of selection intent rules as specified by @link  NXOpen::SelectionIntentRule   NXOpen::SelectionIntentRule @endlink */
        public: enum RuleType
        {
            RuleTypeEdgeDumb/** See documentation for  @link  NXOpen::EdgeDumbRule   NXOpen::EdgeDumbRule @endlink  for more details*/,
            RuleTypeEdgeChain/** See documentation for  @link  NXOpen::EdgeChainRule   NXOpen::EdgeChainRule @endlink  for more details*/,
            RuleTypeEdgeTangent/** See documentation for  @link  NXOpen::EdgeTangentRule   NXOpen::EdgeTangentRule @endlink  for more details*/,
            RuleTypeEdgeFace/** See documentation for  @link  NXOpen::EdgeFaceRule   NXOpen::EdgeFaceRule @endlink  for more details*/,
            RuleTypeEdgeBody/** See documentation for  @link  NXOpen::EdgeBodyRule   NXOpen::EdgeBodyRule @endlink  for more details*/,
            RuleTypeEdgeFeature/** See documentation for  @link  NXOpen::EdgeFeatureRule   NXOpen::EdgeFeatureRule @endlink  for more details*/,
            RuleTypeEdgeSheetBoundary/** See documentation for  @link  NXOpen::EdgeSheetBoundaryRule   NXOpen::EdgeSheetBoundaryRule @endlink  for more details*/,
            RuleTypeEdgeBoundary/** See documentation for  @link  NXOpen::EdgeBoundaryRule   NXOpen::EdgeBoundaryRule @endlink  for more details*/,
            RuleTypeEdgeIntersect/** See documentation for  @link  NXOpen::EdgeIntersectRule   NXOpen::EdgeIntersectRule @endlink  for more details*/,
            RuleTypeEdgeMultipleSeedTangent/** See documentation for  @link  NXOpen::EdgeMultipleSeedTangentRule   NXOpen::EdgeMultipleSeedTangentRule @endlink  for more details*/,
            RuleTypeEdgeVertex/** See documentation for  @link  NXOpen::EdgeVertexRule   NXOpen::EdgeVertexRule @endlink  for more details*/,
            RuleTypeEdgeVertexTangent/** See documentation for  @link  NXOpen::EdgeVertexTangentRule   NXOpen::EdgeVertexTangentRule @endlink  for more details*/,
            RuleTypeCurveDumb/** See documentation for  @link  NXOpen::CurveDumbRule   NXOpen::CurveDumbRule @endlink  for more details*/,
            RuleTypeCurveFeature/** See documentation for  @link  NXOpen::CurveFeatureRule   NXOpen::CurveFeatureRule @endlink  for more details*/,
            RuleTypeCurveFeatureChain/** See documentation for  @link  NXOpen::CurveFeatureChainRule   NXOpen::CurveFeatureChainRule @endlink  for more details*/,
            RuleTypeCurveFeatureTangent/** See documentation for  @link  NXOpen::CurveFeatureTangentRule   NXOpen::CurveFeatureTangentRule @endlink  for more details*/,
            RuleTypeFollowFillet/** See documentation for  @link  NXOpen::FollowFilletRule   NXOpen::FollowFilletRule @endlink  for more details*/,
            RuleTypeFeaturePoints/** See documentation for  @link  NXOpen::FeaturePointsRule   NXOpen::FeaturePointsRule @endlink  for more details*/,
            RuleTypeRegionBoundary/** See documentation for  @link  NXOpen::RegionBoundaryRule   NXOpen::RegionBoundaryRule @endlink  for more details*/,
            RuleTypeFaceDumb/** See documentation for  @link  NXOpen::FaceDumbRule   NXOpen::FaceDumbRule @endlink  for more details*/,
            RuleTypeFaceTangent/** See documentation for  @link  NXOpen::FaceTangentRule   NXOpen::FaceTangentRule @endlink  for more details*/,
            RuleTypeFaceAdjacent/** See documentation for  @link  NXOpen::FaceAdjacentRule   NXOpen::FaceAdjacentRule @endlink  for more details*/,
            RuleTypeFaceBody/** See documentation for  @link  NXOpen::FaceBodyRule   NXOpen::FaceBodyRule @endlink  for more details*/,
            RuleTypeFaceRegion/** See documentation for  @link  NXOpen::FaceRegionRule   NXOpen::FaceRegionRule @endlink  for more details*/,
            RuleTypeFaceFeature/** See documentation for  @link  NXOpen::FaceFeatureRule   NXOpen::FaceFeatureRule @endlink  for more details*/,
            RuleTypeFaceConnectedBlend/** See documentation for  @link  NXOpen::FaceConnectedBlendRule   NXOpen::FaceConnectedBlendRule @endlink  for more details*/,
            RuleTypeFaceAllBlend/** See documentation for  @link  NXOpen::FaceAllBlendRule   NXOpen::FaceAllBlendRule @endlink  for more details*/,
            RuleTypeFaceRib/** See documentation for  @link  NXOpen::FaceRibFacesRule   NXOpen::FaceRibFacesRule @endlink  for more details*/,
            RuleTypeFaceMergedRib/** See documentation for  @link  NXOpen::FaceMergedRibFacesRule   NXOpen::FaceMergedRibFacesRule @endlink  for more details*/,
            RuleTypeFaceSlot/** See documentation for  @link  NXOpen::FaceSlotFacesRule   NXOpen::FaceSlotFacesRule @endlink  for more details*/,
            RuleTypeFaceBossPocket/** See documentation for  @link  NXOpen::FaceBossPocketFacesRule   NXOpen::FaceBossPocketFacesRule @endlink  for more details*/,
            RuleTypeFaceRegionBoundary/** See documentation for  @link  NXOpen::FaceRegionBoundaryRule   NXOpen::FaceRegionBoundaryRule @endlink  for more details*/,
            RuleTypeFaceAndAdjacentFaces/** See documentation for  @link  NXOpen::FaceAndAdjacentFacesRule   NXOpen::FaceAndAdjacentFacesRule @endlink  for more details*/,
            RuleTypeCurveGroup/** See documentation for  @link  NXOpen::CurveGroupRule   NXOpen::CurveGroupRule @endlink  for more details*/,
            RuleTypeBodyDumb/** See documentation for  @link  NXOpen::BodyDumbRule   NXOpen::BodyDumbRule @endlink  for more details*/,
            RuleTypeBodyFeature/** See documentation for  @link  NXOpen::BodyFeatureRule   NXOpen::BodyFeatureRule @endlink  for more details*/,
            RuleTypeBodyGroup/** See documentation for  @link  NXOpen::BodyGroupRule   NXOpen::BodyGroupRule @endlink  for more details*/,
            RuleTypeApparentChaining/** See documentation for  @link  NXOpen::ApparentChainingRule   NXOpen::ApparentChainingRule @endlink  for more details*/,
            RuleTypeOuterFaceEdges/** See documentation for  @link  NXOpen::OuterEdgesOfFacesRule   NXOpen::OuterEdgesOfFacesRule @endlink  for more details*/,
            RuleTypeRibTopFaceEdges/** See documentation for  @link  NXOpen::RibTopFaceEdgesRule   NXOpen::RibTopFaceEdgesRule @endlink  for more details*/,
            RuleTypeFeatureIntersectionEdges/** See documentation for  @link  NXOpen::FeatureIntersectionEdgesRule   NXOpen::FeatureIntersectionEdgesRule @endlink  for more details*/,
            RuleTypeInvalidType/** Invlaid selection intent rule type. */
        };

        private: SelectionIntentRuleImpl * m_selectionintentrule_impl;
        /// \cond NX_NO_DOC 
        public: explicit SelectionIntentRule(void *ptr);
        /// \endcond 
        /** Free resources associated with the instance. After this method
            is called, it is illegal to use the object.  In .NET, this method
            is automatically called when the object is deleted by the garbage
            collector. 
         <br>  Created in NX3.0.0.  <br>  
         <br> License requirements : None */
        public: virtual ~SelectionIntentRule();
        /**Returns  the get the type of selection intent rule: @link  NXOpen::SelectionIntentRule   NXOpen::SelectionIntentRule @endlink  
         <br>  Created in NX3.0.0.  <br>  
         <br> License requirements : gateway ("UG GATEWAY") */
        public: NXOpen::SelectionIntentRule::RuleType Type
        (
        );
    }; //lint !e1712 default constructor not defined for class  

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