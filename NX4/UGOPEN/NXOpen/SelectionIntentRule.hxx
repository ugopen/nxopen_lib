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
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/TransientObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    class SelectionIntentRule;
    /** Selection Intent method to use with follow fillet rule.
    */
    enum FollowFilletRuleType
    {
        FollowFilletRuleTypeConnected/** Connected Curves */,
        FollowFilletRuleTypeTangent/** Tangent Curves */
    };

    /** Represents selection intent rule.
    */
    class NXOPENCPPEXPORT SelectionIntentRule : public TransientObject
    {
        /** This enum represents selection intent rules */
        public: enum RuleType
        {
            RuleTypeEdgeDumb/** See documentation for  @link  EdgeDumbRule   EdgeDumbRule @endlink  for more details*/,
            RuleTypeEdgeChain/** See documentation for  @link  EdgeChainRule   EdgeChainRule @endlink  for more details*/,
            RuleTypeEdgeTangent/** See documentation for  @link  EdgeTangentRule   EdgeTangentRule @endlink  for more details*/,
            RuleTypeEdgeFace/** See documentation for  @link  EdgeFaceRule   EdgeFaceRule @endlink  for more details*/,
            RuleTypeEdgeBody/** See documentation for  @link  EdgeBodyRule   EdgeBodyRule @endlink  for more details*/,
            RuleTypeEdgeFeature/** See documentation for  @link  EdgeFeatureRule   EdgeFeatureRule @endlink  for more details*/,
            RuleTypeEdgeSheetBoundary/** See documentation for  @link  EdgeSheetBoundaryRule   EdgeSheetBoundaryRule @endlink  for more details*/,
            RuleTypeEdgeBoundary/** See documentation for  @link  EdgeBoundaryRule   EdgeBoundaryRule @endlink  for more details*/,
            RuleTypeEdgeIntersect/** See documentation for  @link  EdgeIntersectRule   EdgeIntersectRule @endlink  for more details*/,
            RuleTypeEdgeMultipleSeedTangent/** See documentation for  @link  EdgeMultipleSeedTangentRule   EdgeMultipleSeedTangentRule @endlink  for more details*/,
            RuleTypeEdgeVertex/** See documentation for  @link  EdgeVertexRule   EdgeVertexRule @endlink  for more details*/,
            RuleTypeEdgeVertexTangent/** See documentation for  @link  EdgeVertexTangentRule   EdgeVertexTangentRule @endlink  for more details*/,
            RuleTypeCurveDumb/** See documentation for  @link  CurveDumbRule   CurveDumbRule @endlink  for more details*/,
            RuleTypeCurveFeature/** See documentation for  @link  CurveFeatureRule   CurveFeatureRule @endlink  for more details*/,
            RuleTypeCurveFeatureChain/** See documentation for  @link  CurveFeatureChainRule   CurveFeatureChainRule @endlink  for more details*/,
            RuleTypeCurveFeatureTangent/** See documentation for  @link  CurveFeatureTangentRule   CurveFeatureTangentRule @endlink  for more details*/,
            RuleTypeFollowFillet/** See documentation for  @link  FollowFilletRule   FollowFilletRule @endlink  for more details*/,
            RuleTypeFaceDumb/** See documentation for  @link  FaceDumbRule   FaceDumbRule @endlink  for more details*/,
            RuleTypeFaceTangent/** See documentation for  @link  FaceTangentRule   FaceTangentRule @endlink  for more details*/,
            RuleTypeFaceAdjacent/** See documentation for  @link  FaceAdjacentRule   FaceAdjacentRule @endlink  for more details*/,
            RuleTypeFaceBody/** See documentation for  @link  FaceBodyRule   FaceBodyRule @endlink  for more details*/,
            RuleTypeFaceRegion/** See documentation for  @link  FaceRegionRule   FaceRegionRule @endlink  for more details*/,
            RuleTypeFaceFeature/** See documentation for  @link  FaceFeatureRule   FaceFeatureRule @endlink  for more details*/,
            RuleTypeInvalidType/** Invlaid selection intent rule type. */
        };

        public: explicit SelectionIntentRule(void *ptr);
        /** Free resources associated with the instance. After this method
            is called, it is illegal to use the object.  In .NET, this method
            is automatically called when the object is deleted by the garbage
            collector.  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: virtual ~SelectionIntentRule();
        /**Returns  the selection intent rule type  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: NXOpen::SelectionIntentRule::RuleType Type
        (
        );
        /** <b>Deprecated</b>:<br>
        &nbsp;&nbsp;&nbsp;Use @link Type() Type@endlink instead.
        @deprecated
        */
        public: NXOpen::SelectionIntentRule::RuleType GetType
        (
        ) { return this->Type(); }
    };
}
#undef EXPORTLIBRARY
#endif