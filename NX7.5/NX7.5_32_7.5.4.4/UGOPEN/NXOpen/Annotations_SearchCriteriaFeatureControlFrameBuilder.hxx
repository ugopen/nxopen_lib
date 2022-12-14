#ifndef NXOpen_ANNOTATIONS_SEARCHCRITERIAFEATURECONTROLFRAMEBUILDER_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_SEARCHCRITERIAFEATURECONTROLFRAMEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_SearchCriteriaFeatureControlFrameBuilder.ja
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
#include <NXOpen/Annotations_SearchCriteriaFeatureControlFrameBuilder.hxx>
#include <NXOpen/Annotations_SearchModelViewBuilder.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Annotations
    {
        class SearchCriteriaFeatureControlFrameBuilder;
    }
    class Builder;
    namespace Annotations
    {
        class _SearchCriteriaFeatureControlFrameBuilderBuilder;
        class SearchCriteriaFeatureControlFrameBuilderImpl;
        /** Represents SearchCriteriaFeatureControlFrameBuilder  <br> To create a new instance of this class, use @link Annotations::SearchModelViewCollection::CreateSearchCriteriaFeatureControlFrameBuilder Annotations::SearchModelViewCollection::CreateSearchCriteriaFeatureControlFrameBuilder@endlink  <br> */
        class NXOPENCPPEXPORT  SearchCriteriaFeatureControlFrameBuilder : public Builder
        {
            /** Lists the search pmi feature control frame style*/
            public: enum FrameStyleOptions
            {
                FrameStyleOptionsSingleFrame/** single frame*/,
                FrameStyleOptionsCompositeFrame/** composite frame*/
            };

            /** Lists the search pmi feature control frame type*/
            public: enum CharacteristicOptions
            {
                CharacteristicOptionsStraightness/** strainhtness*/,
                CharacteristicOptionsFlatness/** flatness*/,
                CharacteristicOptionsCircularity/** circularity*/,
                CharacteristicOptionsCylindricity/** cylindricity*/,
                CharacteristicOptionsProfileOfALine/** Profile Of A Line*/,
                CharacteristicOptionsProfileOfASurface/** profile Of A Surface*/,
                CharacteristicOptionsAngularity/** angularity*/,
                CharacteristicOptionsPerpendicularity/** perpendicularity*/,
                CharacteristicOptionsParallelism/** parallelism*/,
                CharacteristicOptionsPosition/** position*/,
                CharacteristicOptionsConcentricity/** concentricity*/,
                CharacteristicOptionsSymmetry/** symmetry*/,
                CharacteristicOptionsCircularRunout/** circular runout*/,
                CharacteristicOptionsTotalRunout/** total runout*/
            };

            /** Lists the type of pmi feature control frame tolerance MCM*/
            public: enum ToleranceMCMOptions
            {
                ToleranceMCMOptionsNone/** none*/,
                ToleranceMCMOptionsLeastMaterialCondition/** least material condition*/,
                ToleranceMCMOptionsMaximumMaterialCondition/** maximum material condition*/,
                ToleranceMCMOptionsRegardlessofFeatureSize/** regardless of feature size*/
            };

            /** Lists the type of pmi feature control frame zone shape*/
            public: enum ZoneShapeOptions
            {
                ZoneShapeOptionsNone/** none*/,
                ZoneShapeOptionsDiameter/** diameter*/,
                ZoneShapeOptionsSphericalDiameter/** spherical diameter*/,
                ZoneShapeOptionsSquare/** square*/
            };

            /** Lists the status of pmi feature control frame statistical*/
            public: enum StatisticalOptions
            {
                StatisticalOptionsYes/** have statistical*/,
                StatisticalOptionsNo/** have no statistical*/
            };

            /** Lists the status of pmi feature control frame tangent plane*/
            public: enum TangentPlaneOptions
            {
                TangentPlaneOptionsYes/** have tangent plane*/,
                TangentPlaneOptionsNo/** have no tangent plane*/
            };

            /** Lists the status of pmi feature control frame free state*/
            public: enum FreeStateOptions
            {
                FreeStateOptionsYes/** have free state*/,
                FreeStateOptionsNo/** have no free state*/
            };

            /** Lists the status of pmi feature control frame circleU*/
            public: enum CircleUOptions
            {
                CircleUOptionsYes/** have circle U*/,
                CircleUOptionsNo/** have no circle U*/
            };

            /** Lists the status of pmi feature control frame projected*/
            public: enum ProjectedOptions
            {
                ProjectedOptionsYes/** have projected*/,
                ProjectedOptionsNo/** have no projected*/
            };

            /** Lists the type of pmi feature control frame primary datum MCM*/
            public: enum PrimaryDatumMCMOptions
            {
                PrimaryDatumMCMOptionsNone/** none*/,
                PrimaryDatumMCMOptionsLeastMaterialCondition/** least material condition*/,
                PrimaryDatumMCMOptionsMaximumMaterialCondition/** maximum material condition*/,
                PrimaryDatumMCMOptionsRegardlessofFeatureSize/** regardless of feature size*/
            };

            /** Lists the type of pmi feature control frame primary datum dual MCM*/
            public: enum PrimaryDatumDualMCMOptions
            {
                PrimaryDatumDualMCMOptionsNone/** none*/,
                PrimaryDatumDualMCMOptionsLeastMaterialCondition/** least material condition*/,
                PrimaryDatumDualMCMOptionsMaximumMaterialCondition/** maximum material condition*/,
                PrimaryDatumDualMCMOptionsRegardlessofFeatureSize/** regardless of feature size*/
            };

            /** Lists the type of pmi feature control frame secondary datum MCM*/
            public: enum SecondaryDatumMCMOptions
            {
                SecondaryDatumMCMOptionsNone/** none*/,
                SecondaryDatumMCMOptionsLeastMaterialCondition/** least material condition*/,
                SecondaryDatumMCMOptionsMaximumMaterialCondition/** maximum material condition*/,
                SecondaryDatumMCMOptionsRegardlessofFeatureSize/** regardless of feature size*/
            };

            /** Lists the type of pmi feature control frame secondary datum dual MCM*/
            public: enum SecondaryDatumDualMCMOptions
            {
                SecondaryDatumDualMCMOptionsNone/** none*/,
                SecondaryDatumDualMCMOptionsLeastMaterialCondition/** least material condition*/,
                SecondaryDatumDualMCMOptionsMaximumMaterialCondition/** maximum material condition*/,
                SecondaryDatumDualMCMOptionsRegardlessofFeatureSize/** regardless of feature size*/
            };

            /** Lists the type of pmi feature control frame tertiary datum MCM*/
            public: enum TertiaryDatumMCMOptions
            {
                TertiaryDatumMCMOptionsNone/** none*/,
                TertiaryDatumMCMOptionsLeastMaterialCondition/** least material condition*/,
                TertiaryDatumMCMOptionsMaximumMaterialCondition/** maximum material condition*/,
                TertiaryDatumMCMOptionsRegardlessofFeatureSize/** regardless of feature size*/
            };

            /** Lists the type of pmi feature control frame tertiary datum dual MCM*/
            public: enum TertiaryDatumDualMCMOptions
            {
                TertiaryDatumDualMCMOptionsNone/** none*/,
                TertiaryDatumDualMCMOptionsLeastMaterialCondition/** least material condition*/,
                TertiaryDatumDualMCMOptionsMaximumMaterialCondition/** maximum material condition*/,
                TertiaryDatumDualMCMOptionsRegardlessofFeatureSize/** regardless of feature size*/
            };

            private: SearchCriteriaFeatureControlFrameBuilderImpl * m_searchcriteriafeaturecontrolframebuilder_impl;
            private: friend class  _SearchCriteriaFeatureControlFrameBuilderBuilder;
            protected: SearchCriteriaFeatureControlFrameBuilder();
            public: ~SearchCriteriaFeatureControlFrameBuilder();
            /**Returns  the frame style enum  <br> License requirements : None */
            public: NXOpen::Annotations::SearchCriteriaFeatureControlFrameBuilder::FrameStyleOptions FrameStyleType
            (
            );
            /**Sets  the frame style enum  <br> License requirements : None */
            public: void SetFrameStyleType
            (
                NXOpen::Annotations::SearchCriteriaFeatureControlFrameBuilder::FrameStyleOptions frameStyleType /** framestyletype */ 
            );
            /**Returns  the characteristic toggle  <br> License requirements : None */
            public: bool ByCharacteristic
            (
            );
            /**Sets  the characteristic toggle  <br> License requirements : None */
            public: void SetByCharacteristic
            (
                bool characteristic /** characteristic */ 
            );
            /**Returns  the characteristic enum  <br> License requirements : None */
            public: NXOpen::Annotations::SearchCriteriaFeatureControlFrameBuilder::CharacteristicOptions CharacteristicType
            (
            );
            /**Sets  the characteristic enum  <br> License requirements : None */
            public: void SetCharacteristicType
            (
                NXOpen::Annotations::SearchCriteriaFeatureControlFrameBuilder::CharacteristicOptions characteristicType /** characteristictype */ 
            );
            /**Returns  the tolerance toggle  <br> License requirements : None */
            public: bool ByTolerance
            (
            );
            /**Sets  the tolerance toggle  <br> License requirements : None */
            public: void SetByTolerance
            (
                bool tolerance /** tolerance */ 
            );
            /**Returns  the tolerance text enum  <br> License requirements : None */
            public: NXOpen::Annotations::SearchModelViewBuilder::TextComparisionOptions ToleranceTextType
            (
            );
            /**Sets  the tolerance text enum  <br> License requirements : None */
            public: void SetToleranceTextType
            (
                NXOpen::Annotations::SearchModelViewBuilder::TextComparisionOptions toleranceTextType /** tolerancetexttype */ 
            );
            /**Returns  the tolerance text  <br> License requirements : None */
            public: NXString ToleranceText
            (
            );
            /**Sets  the tolerance text  <br> License requirements : None */
            public: void SetToleranceText
            (
                const NXString & toleranceText /** tolerancetext */ 
            );
            /**Returns  the tolerance mcmtoggle  <br> License requirements : None */
            public: bool ByToleranceMCM
            (
            );
            /**Sets  the tolerance mcmtoggle  <br> License requirements : None */
            public: void SetByToleranceMCM
            (
                bool toleranceMCM /** tolerancemcm */ 
            );
            /**Returns  the tolerance mcmenum  <br> License requirements : None */
            public: NXOpen::Annotations::SearchCriteriaFeatureControlFrameBuilder::ToleranceMCMOptions ToleranceMCMType
            (
            );
            /**Sets  the tolerance mcmenum  <br> License requirements : None */
            public: void SetToleranceMCMType
            (
                NXOpen::Annotations::SearchCriteriaFeatureControlFrameBuilder::ToleranceMCMOptions toleranceMCMType /** tolerancemcmtype */ 
            );
            /**Returns  the zone shape toggle  <br> License requirements : None */
            public: bool ByZoneShape
            (
            );
            /**Sets  the zone shape toggle  <br> License requirements : None */
            public: void SetByZoneShape
            (
                bool zoneShape /** zoneshape */ 
            );
            /**Returns  the zone shape enum  <br> License requirements : None */
            public: NXOpen::Annotations::SearchCriteriaFeatureControlFrameBuilder::ZoneShapeOptions ZoneShapeType
            (
            );
            /**Sets  the zone shape enum  <br> License requirements : None */
            public: void SetZoneShapeType
            (
                NXOpen::Annotations::SearchCriteriaFeatureControlFrameBuilder::ZoneShapeOptions zoneShapeType /** zoneshapetype */ 
            );
            /**Returns  the statistical toggle  <br> License requirements : None */
            public: bool ByStatistical
            (
            );
            /**Sets  the statistical toggle  <br> License requirements : None */
            public: void SetByStatistical
            (
                bool statistical /** statistical */ 
            );
            /**Returns  the statistical enum  <br> License requirements : None */
            public: NXOpen::Annotations::SearchCriteriaFeatureControlFrameBuilder::StatisticalOptions StatisticalType
            (
            );
            /**Sets  the statistical enum  <br> License requirements : None */
            public: void SetStatisticalType
            (
                NXOpen::Annotations::SearchCriteriaFeatureControlFrameBuilder::StatisticalOptions statisticalType /** statisticaltype */ 
            );
            /**Returns  the tangent plane toggle  <br> License requirements : None */
            public: bool ByTangentPlane
            (
            );
            /**Sets  the tangent plane toggle  <br> License requirements : None */
            public: void SetByTangentPlane
            (
                bool tangentPlane /** tangentplane */ 
            );
            /**Returns  the tangent plane enum  <br> License requirements : None */
            public: NXOpen::Annotations::SearchCriteriaFeatureControlFrameBuilder::TangentPlaneOptions TangentPlaneType
            (
            );
            /**Sets  the tangent plane enum  <br> License requirements : None */
            public: void SetTangentPlaneType
            (
                NXOpen::Annotations::SearchCriteriaFeatureControlFrameBuilder::TangentPlaneOptions tangentPlaneType /** tangentplanetype */ 
            );
            /**Returns  the free state toggle  <br> License requirements : None */
            public: bool ByFreeState
            (
            );
            /**Sets  the free state toggle  <br> License requirements : None */
            public: void SetByFreeState
            (
                bool freeState /** freestate */ 
            );
            /**Returns  the free state enum  <br> License requirements : None */
            public: NXOpen::Annotations::SearchCriteriaFeatureControlFrameBuilder::FreeStateOptions FreeStateType
            (
            );
            /**Sets  the free state enum  <br> License requirements : None */
            public: void SetFreeStateType
            (
                NXOpen::Annotations::SearchCriteriaFeatureControlFrameBuilder::FreeStateOptions freeStateType /** freestatetype */ 
            );
            /**Returns  the circle utoggle  <br> License requirements : None */
            public: bool ByCircleU
            (
            );
            /**Sets  the circle utoggle  <br> License requirements : None */
            public: void SetByCircleU
            (
                bool circleU /** circleu */ 
            );
            /**Returns  the circle uenum  <br> License requirements : None */
            public: NXOpen::Annotations::SearchCriteriaFeatureControlFrameBuilder::CircleUOptions CircleUType
            (
            );
            /**Sets  the circle uenum  <br> License requirements : None */
            public: void SetCircleUType
            (
                NXOpen::Annotations::SearchCriteriaFeatureControlFrameBuilder::CircleUOptions circleUType /** circleutype */ 
            );
            /**Returns  the circle uvalue toggle  <br> License requirements : None */
            public: bool ByCircleUValue
            (
            );
            /**Sets  the circle uvalue toggle  <br> License requirements : None */
            public: void SetByCircleUValue
            (
                bool circleUValue /** circleuvalue */ 
            );
            /**Returns  the circle uvalue enum  <br> License requirements : None */
            public: NXOpen::Annotations::SearchModelViewBuilder::ValueComparisionOptions CircleUValueType
            (
            );
            /**Sets  the circle uvalue enum  <br> License requirements : None */
            public: void SetCircleUValueType
            (
                NXOpen::Annotations::SearchModelViewBuilder::ValueComparisionOptions circleUValueType /** circleuvaluetype */ 
            );
            /**Returns  the circle uvalue  <br> License requirements : None */
            public: double CircleUValue
            (
            );
            /**Sets  the circle uvalue  <br> License requirements : None */
            public: void SetCircleUValue
            (
                double circleUValue /** circleuvalue */ 
            );
            /**Returns  the projected toggle  <br> License requirements : None */
            public: bool ByProjected
            (
            );
            /**Sets  the projected toggle  <br> License requirements : None */
            public: void SetByProjected
            (
                bool projected /** projected */ 
            );
            /**Returns  the projected enum  <br> License requirements : None */
            public: NXOpen::Annotations::SearchCriteriaFeatureControlFrameBuilder::ProjectedOptions ProjectedType
            (
            );
            /**Sets  the projected enum  <br> License requirements : None */
            public: void SetProjectedType
            (
                NXOpen::Annotations::SearchCriteriaFeatureControlFrameBuilder::ProjectedOptions projectedType /** projectedtype */ 
            );
            /**Returns  the projected value toggle  <br> License requirements : None */
            public: bool ByProjectedValue
            (
            );
            /**Sets  the projected value toggle  <br> License requirements : None */
            public: void SetByProjectedValue
            (
                bool projectedValue /** projectedvalue */ 
            );
            /**Returns  the projected value enum  <br> License requirements : None */
            public: NXOpen::Annotations::SearchModelViewBuilder::ValueComparisionOptions ProjectedValueType
            (
            );
            /**Sets  the projected value enum  <br> License requirements : None */
            public: void SetProjectedValueType
            (
                NXOpen::Annotations::SearchModelViewBuilder::ValueComparisionOptions projectedValueType /** projectedvaluetype */ 
            );
            /**Returns  the projected value  <br> License requirements : None */
            public: double ProjectedValue
            (
            );
            /**Sets  the projected value  <br> License requirements : None */
            public: void SetProjectedValue
            (
                double projectedValue /** projectedvalue */ 
            );
            /**Returns  the maximum toggle  <br> License requirements : None */
            public: bool ByMaximum
            (
            );
            /**Sets  the maximum toggle  <br> License requirements : None */
            public: void SetByMaximum
            (
                bool maximum /** maximum */ 
            );
            /**Returns  the maximum text enum  <br> License requirements : None */
            public: NXOpen::Annotations::SearchModelViewBuilder::TextComparisionOptions MaximumTextType
            (
            );
            /**Sets  the maximum text enum  <br> License requirements : None */
            public: void SetMaximumTextType
            (
                NXOpen::Annotations::SearchModelViewBuilder::TextComparisionOptions maximumTextType /** maximumtexttype */ 
            );
            /**Returns  the maximum value  <br> License requirements : None */
            public: NXString MaximumText
            (
            );
            /**Sets  the maximum value  <br> License requirements : None */
            public: void SetMaximumText
            (
                const NXString & maximumText /** maximumtext */ 
            );
            /**Returns  the primary datum toggle  <br> License requirements : None */
            public: bool ByPrimaryDatum
            (
            );
            /**Sets  the primary datum toggle  <br> License requirements : None */
            public: void SetByPrimaryDatum
            (
                bool primaryDatum /** primarydatum */ 
            );
            /**Returns  the primary datum text  <br> License requirements : None */
            public: NXString PrimaryDatumText
            (
            );
            /**Sets  the primary datum text  <br> License requirements : None */
            public: void SetPrimaryDatumText
            (
                const NXString & primaryDatumText /** primarydatumtext */ 
            );
            /**Returns  the primary datum mcmtoggle  <br> License requirements : None */
            public: bool ByPrimaryDatumMCM
            (
            );
            /**Sets  the primary datum mcmtoggle  <br> License requirements : None */
            public: void SetByPrimaryDatumMCM
            (
                bool primaryDatumMCM /** primarydatummcm */ 
            );
            /**Returns  the primary datum mcmenum  <br> License requirements : None */
            public: NXOpen::Annotations::SearchCriteriaFeatureControlFrameBuilder::PrimaryDatumMCMOptions PrimaryDatumMCMType
            (
            );
            /**Sets  the primary datum mcmenum  <br> License requirements : None */
            public: void SetPrimaryDatumMCMType
            (
                NXOpen::Annotations::SearchCriteriaFeatureControlFrameBuilder::PrimaryDatumMCMOptions primaryDatumMCMType /** primarydatummcmtype */ 
            );
            /**Returns  the primary datum dual toggle  <br> License requirements : None */
            public: bool ByPrimaryDatumDual
            (
            );
            /**Sets  the primary datum dual toggle  <br> License requirements : None */
            public: void SetByPrimaryDatumDual
            (
                bool primaryDatumDual /** primarydatumdual */ 
            );
            /**Returns  the primary datum dual text  <br> License requirements : None */
            public: NXString PrimaryDatumDualText
            (
            );
            /**Sets  the primary datum dual text  <br> License requirements : None */
            public: void SetPrimaryDatumDualText
            (
                const NXString & primaryDatumDualText /** primarydatumdualtext */ 
            );
            /**Returns  the primary datum dual mcmtoggle  <br> License requirements : None */
            public: bool ByPrimaryDatumDualMCM
            (
            );
            /**Sets  the primary datum dual mcmtoggle  <br> License requirements : None */
            public: void SetByPrimaryDatumDualMCM
            (
                bool primaryDatumDualMCM /** primarydatumdualmcm */ 
            );
            /**Returns  the primary datum dual mcmenum  <br> License requirements : None */
            public: NXOpen::Annotations::SearchCriteriaFeatureControlFrameBuilder::PrimaryDatumDualMCMOptions PrimaryDatumDualMCMType
            (
            );
            /**Sets  the primary datum dual mcmenum  <br> License requirements : None */
            public: void SetPrimaryDatumDualMCMType
            (
                NXOpen::Annotations::SearchCriteriaFeatureControlFrameBuilder::PrimaryDatumDualMCMOptions primaryDatumDualMCMType /** primarydatumdualmcmtype */ 
            );
            /**Returns  the secondary datum toggle  <br> License requirements : None */
            public: bool BySecondaryDatum
            (
            );
            /**Sets  the secondary datum toggle  <br> License requirements : None */
            public: void SetBySecondaryDatum
            (
                bool secondaryDatum /** secondarydatum */ 
            );
            /**Returns  the secondary datum text  <br> License requirements : None */
            public: NXString SecondaryDatumText
            (
            );
            /**Sets  the secondary datum text  <br> License requirements : None */
            public: void SetSecondaryDatumText
            (
                const NXString & secondaryDatumText /** secondarydatumtext */ 
            );
            /**Returns  the secondary datum mcmtoggle  <br> License requirements : None */
            public: bool BySecondaryDatumMCM
            (
            );
            /**Sets  the secondary datum mcmtoggle  <br> License requirements : None */
            public: void SetBySecondaryDatumMCM
            (
                bool secondaryDatumMCM /** secondarydatummcm */ 
            );
            /**Returns  the secondary datum mcmenum  <br> License requirements : None */
            public: NXOpen::Annotations::SearchCriteriaFeatureControlFrameBuilder::SecondaryDatumMCMOptions SecondaryDatumMCMType
            (
            );
            /**Sets  the secondary datum mcmenum  <br> License requirements : None */
            public: void SetSecondaryDatumMCMType
            (
                NXOpen::Annotations::SearchCriteriaFeatureControlFrameBuilder::SecondaryDatumMCMOptions secondaryDatumMCMType /** secondarydatummcmtype */ 
            );
            /**Returns  the secondary datum dual toggle  <br> License requirements : None */
            public: bool BySecondaryDatumDual
            (
            );
            /**Sets  the secondary datum dual toggle  <br> License requirements : None */
            public: void SetBySecondaryDatumDual
            (
                bool secondaryDatumDual /** secondarydatumdual */ 
            );
            /**Returns  the secondary datum dual text  <br> License requirements : None */
            public: NXString SecondaryDatumDualText
            (
            );
            /**Sets  the secondary datum dual text  <br> License requirements : None */
            public: void SetSecondaryDatumDualText
            (
                const NXString & secondaryDatumDualText /** secondarydatumdualtext */ 
            );
            /**Returns  the secondary datum dual mcmtoggle  <br> License requirements : None */
            public: bool BySecondaryDatumDualMCM
            (
            );
            /**Sets  the secondary datum dual mcmtoggle  <br> License requirements : None */
            public: void SetBySecondaryDatumDualMCM
            (
                bool secondaryDatumDualMCM /** secondarydatumdualmcm */ 
            );
            /**Returns  the secondary datum dual mcmenum  <br> License requirements : None */
            public: NXOpen::Annotations::SearchCriteriaFeatureControlFrameBuilder::SecondaryDatumDualMCMOptions SecondaryDatumDualMCMType
            (
            );
            /**Sets  the secondary datum dual mcmenum  <br> License requirements : None */
            public: void SetSecondaryDatumDualMCMType
            (
                NXOpen::Annotations::SearchCriteriaFeatureControlFrameBuilder::SecondaryDatumDualMCMOptions secondaryDatumDualMCMType /** secondarydatumdualmcmtype */ 
            );
            /**Returns  the tertiary datum toggle  <br> License requirements : None */
            public: bool ByTertiaryDatum
            (
            );
            /**Sets  the tertiary datum toggle  <br> License requirements : None */
            public: void SetByTertiaryDatum
            (
                bool tertiaryDatum /** tertiarydatum */ 
            );
            /**Returns  the tertiary datum text  <br> License requirements : None */
            public: NXString TertiaryDatumText
            (
            );
            /**Sets  the tertiary datum text  <br> License requirements : None */
            public: void SetTertiaryDatumText
            (
                const NXString & tertiaryDatumText /** tertiarydatumtext */ 
            );
            /**Returns  the tertiary datum mcmtoggle  <br> License requirements : None */
            public: bool ByTertiaryDatumMCM
            (
            );
            /**Sets  the tertiary datum mcmtoggle  <br> License requirements : None */
            public: void SetByTertiaryDatumMCM
            (
                bool tertiaryDatumMCM /** tertiarydatummcm */ 
            );
            /**Returns  the tertiary datum mcmenum  <br> License requirements : None */
            public: NXOpen::Annotations::SearchCriteriaFeatureControlFrameBuilder::TertiaryDatumMCMOptions TertiaryDatumMCMType
            (
            );
            /**Sets  the tertiary datum mcmenum  <br> License requirements : None */
            public: void SetTertiaryDatumMCMType
            (
                NXOpen::Annotations::SearchCriteriaFeatureControlFrameBuilder::TertiaryDatumMCMOptions tertiaryDatumMCMType /** tertiarydatummcmtype */ 
            );
            /**Returns  the tertiary datum dual toggle  <br> License requirements : None */
            public: bool ByTertiaryDatumDual
            (
            );
            /**Sets  the tertiary datum dual toggle  <br> License requirements : None */
            public: void SetByTertiaryDatumDual
            (
                bool tertiaryDatumDual /** tertiarydatumdual */ 
            );
            /**Returns  the tertiary datum dual text  <br> License requirements : None */
            public: NXString TertiaryDatumDualText
            (
            );
            /**Sets  the tertiary datum dual text  <br> License requirements : None */
            public: void SetTertiaryDatumDualText
            (
                const NXString & tertiaryDatumDualText /** tertiarydatumdualtext */ 
            );
            /**Returns  the tertiary datum dual mcmtoggle  <br> License requirements : None */
            public: bool ByTertiaryDatumDualMCM
            (
            );
            /**Sets  the tertiary datum dual mcmtoggle  <br> License requirements : None */
            public: void SetByTertiaryDatumDualMCM
            (
                bool tertiaryDatumDualMCM /** tertiarydatumdualmcm */ 
            );
            /**Returns  the tertiary datum dual mcmenum  <br> License requirements : None */
            public: NXOpen::Annotations::SearchCriteriaFeatureControlFrameBuilder::TertiaryDatumDualMCMOptions TertiaryDatumDualMCMType
            (
            );
            /**Sets  the tertiary datum dual mcmenum  <br> License requirements : None */
            public: void SetTertiaryDatumDualMCMType
            (
                NXOpen::Annotations::SearchCriteriaFeatureControlFrameBuilder::TertiaryDatumDualMCMOptions tertiaryDatumDualMCMType /** tertiarydatumdualmcmtype */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
