#ifndef NXOpen_ANNOTATIONS_SEARCHCRITERIADIMENSIONBUILDER_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_SEARCHCRITERIADIMENSIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_SearchCriteriaDimensionBuilder.ja
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
#include <NXOpen/Annotations_SearchCriteriaCalloutBuilder.hxx>
#include <NXOpen/Annotations_SearchCriteriaDimensionBuilder.hxx>
#include <NXOpen/Annotations_SearchModelViewBuilder.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/libnxopencpp_annotations_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Annotations
    {
        class SearchCriteriaDimensionBuilder;
    }
    namespace Annotations
    {
        class SearchCriteriaCalloutBuilder;
    }
    class Builder;
    namespace Annotations
    {
        class _SearchCriteriaDimensionBuilderBuilder;
        class SearchCriteriaDimensionBuilderImpl;
        /** Represents SearchCriteriaDimensionBuilder  <br> To create a new instance of this class, use @link NXOpen::Annotations::SearchModelViewCollection::CreateSearchCriteriaDimensionBuilder  NXOpen::Annotations::SearchModelViewCollection::CreateSearchCriteriaDimensionBuilder @endlink  <br> 
         <br>  Created in NX7.5.0.  <br>  
        */
        class NXOPENCPP_ANNOTATIONSEXPORT  SearchCriteriaDimensionBuilder : public NXOpen::Builder
        {
            /** Specifies dimension types*/
            public: enum DimensionTypes
            {
                DimensionTypesLinear/** Linear*/,
                DimensionTypesAngular/** Angular*/,
                DimensionTypesDiameter/** Diameter*/,
                DimensionTypesRadial/** Radial*/,
                DimensionTypesChamfer/** Chamfer*/,
                DimensionTypesThickness/** Thickness*/,
                DimensionTypesArcLength/** ArcLength*/,
                DimensionTypesChain/** Chain*/,
                DimensionTypesOrdinate/** Ordinate*/,
                DimensionTypesBaseline/** Baseline*/
            };

            /** Specifies measurement types*/
            public: enum MeasurementTypes
            {
                MeasurementTypesAll/** Linear ALL*/,
                MeasurementTypesDirected/** Linear Directed*/,
                MeasurementTypesFeatureOfSize/** Linear Feature of Size*/
            };

            /** Specifies radial symbol option*/
            public: enum RadialSymbolOptions
            {
                RadialSymbolOptionsR/** R */,
                RadialSymbolOptionsRad/** RAD */,
                RadialSymbolOptionsSr/** SR */,
                RadialSymbolOptionsCr/** CR */,
                RadialSymbolOptionsUserDefined/** UserDefined*/
            };

            /** Specifies diameter symbol option*/
            public: enum DiameterSymbolOptions
            {
                DiameterSymbolOptionsDiameter/** diameter */ ,
                DiameterSymbolOptionsDia/** dia */ ,
                DiameterSymbolOptionsSphericalDiameter/** spherical diameter */ ,
                DiameterSymbolOptionsUserDefined/** UserDefined*/
            };

            /** Specifies tolerance types*/
            public: enum ToleranceTypes
            {
                ToleranceTypesNoTolerance/** NoTolerance*/,
                ToleranceTypesEqualBilateralTolerance/** qualBilateralTolerance*/,
                ToleranceTypesBilateralTolerance/** BilateralTolerance*/,
                ToleranceTypesUnilateralPlus/** UnilateralPlus*/,
                ToleranceTypesUnilateralMinus/** UnilateralMinus*/,
                ToleranceTypesPlusLimitTwoLines/** PlusLimitTwoLines*/,
                ToleranceTypesMinusLimitTwoLines/** MinusLimitTwoLines*/,
                ToleranceTypesPlusLimitOneLine/** PlusLimitOneLine*/,
                ToleranceTypesMinusLimitOneLine/** MinusLimitOneLine*/,
                ToleranceTypesLimitsAndFits/** LimitsAndFits*/,
                ToleranceTypesBasic/** Basic*/,
                ToleranceTypesReference/** Reference*/,
                ToleranceTypesDiameterReference/** DiameterReference*/,
                ToleranceTypesNotToScale/** NotToScale*/,
                ToleranceTypesBasicDimensionNotToScale/** BasicDimensionNotToScale*/
            };

            private: SearchCriteriaDimensionBuilderImpl * m_searchcriteriadimensionbuilder_impl;
            private: friend class  _SearchCriteriaDimensionBuilderBuilder;
            protected: SearchCriteriaDimensionBuilder();
            public: ~SearchCriteriaDimensionBuilder();
            /**Returns  the dimension type toggle 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: bool ByDimensionType
            (
            );
            /**Sets  the dimension type toggle 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetByDimensionType
            (
                bool dimensionType /** dimensiontype */ 
            );
            /**Returns  the dimension type 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::SearchCriteriaDimensionBuilder::DimensionTypes DimensionType
            (
            );
            /**Sets  the dimension type 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetDimensionType
            (
                NXOpen::Annotations::SearchCriteriaDimensionBuilder::DimensionTypes dimensionType /** dimensiontype */ 
            );
            /**Returns  the radial symbol toggle 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: bool ByRadialSymbol
            (
            );
            /**Sets  the radial symbol toggle 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetByRadialSymbol
            (
                bool radialSymbol /** radialsymbol */ 
            );
            /**Returns  the radial symbol 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::SearchCriteriaDimensionBuilder::RadialSymbolOptions RadialSymbol
            (
            );
            /**Sets  the radial symbol 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetRadialSymbol
            (
                NXOpen::Annotations::SearchCriteriaDimensionBuilder::RadialSymbolOptions radialSymbol /** radialsymbol */ 
            );
            /**Returns  the diameter symbol toggle 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: bool ByDiameterSymbol
            (
            );
            /**Sets  the diameter symbol toggle 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetByDiameterSymbol
            (
                bool diameterSymbol /** diametersymbol */ 
            );
            /**Returns  the diameter symbol 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::SearchCriteriaDimensionBuilder::DiameterSymbolOptions DiameterSymbol
            (
            );
            /**Sets  the diameter symbol 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetDiameterSymbol
            (
                NXOpen::Annotations::SearchCriteriaDimensionBuilder::DiameterSymbolOptions diameterSymbol /** diametersymbol */ 
            );
            /**Returns  the dimension value toggle 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: bool ByDimensionValue
            (
            );
            /**Sets  the dimension value toggle 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetByDimensionValue
            (
                bool dimensionValue /** dimensionvalue */ 
            );
            /**Returns  the dimension value enum 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::SearchModelViewBuilder::ValueComparisionOptions DimensionValueType
            (
            );
            /**Sets  the dimension value enum 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetDimensionValueType
            (
                NXOpen::Annotations::SearchModelViewBuilder::ValueComparisionOptions dimensionValueType /** dimensionvaluetype */ 
            );
            /**Returns  the dimension value 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: double DimensionValue
            (
            );
            /**Sets  the dimension value 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetDimensionValue
            (
                double dimensionValue /** dimensionvalue */ 
            );
            /**Returns  the tolerance type toggle 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: bool ByToleranceType
            (
            );
            /**Sets  the tolerance type toggle 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetByToleranceType
            (
                bool toleranceType /** tolerancetype */ 
            );
            /**Returns  the tolerance type 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::SearchCriteriaDimensionBuilder::ToleranceTypes ToleranceType
            (
            );
            /**Sets  the tolerance type 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetToleranceType
            (
                NXOpen::Annotations::SearchCriteriaDimensionBuilder::ToleranceTypes toleranceType /** tolerancetype */ 
            );
            /**Returns  the upper tolerance toggle 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: bool ByUpperTolerance
            (
            );
            /**Sets  the upper tolerance toggle 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetByUpperTolerance
            (
                bool upperTolerance /** uppertolerance */ 
            );
            /**Returns  the upper tolerance enum 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::SearchModelViewBuilder::ValueComparisionOptions UpperToleranceType
            (
            );
            /**Sets  the upper tolerance enum 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetUpperToleranceType
            (
                NXOpen::Annotations::SearchModelViewBuilder::ValueComparisionOptions upperToleranceType /** uppertolerancetype */ 
            );
            /**Returns  the upper tolerance value 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: double UpperToleranceValue
            (
            );
            /**Sets  the upper tolerance value 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetUpperToleranceValue
            (
                double upperToleranceValue /** uppertolerancevalue */ 
            );
            /**Returns  the lower tolerance toggle 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: bool ByLowerTolerance
            (
            );
            /**Sets  the lower tolerance toggle 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetByLowerTolerance
            (
                bool lowerTolerance /** lowertolerance */ 
            );
            /**Returns  the lower tolerance enum 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::SearchModelViewBuilder::ValueComparisionOptions LowerToleranceType
            (
            );
            /**Sets  the lower tolerance enum 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetLowerToleranceType
            (
                NXOpen::Annotations::SearchModelViewBuilder::ValueComparisionOptions lowerToleranceType /** lowertolerancetype */ 
            );
            /**Returns  the lower tolerance value 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: double LowerToleranceValue
            (
            );
            /**Sets  the lower tolerance value 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetLowerToleranceValue
            (
                double lowerToleranceValue /** lowertolerancevalue */ 
            );
            /**Returns  the deviation toggle 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: bool ByDeviation
            (
            );
            /**Sets  the deviation toggle 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetByDeviation
            (
                bool byDeviation /** bydeviation */ 
            );
            /**Returns  the deviation 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXString Deviation
            (
            );
            /**Sets  the deviation 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetDeviation
            (
                const NXString & deviation /** deviation */ 
            );
            /**Sets  the deviation 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            void SetDeviation
            (
                const char * deviation /** deviation */ 
            );
            /**Returns  the grade toggle 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: bool ByGrade
            (
            );
            /**Sets  the grade toggle 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetByGrade
            (
                bool byGrade /** bygrade */ 
            );
            /**Returns  the grade 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXString Grade
            (
            );
            /**Sets  the grade 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetGrade
            (
                const NXString & grade /** grade */ 
            );
            /**Sets  the grade 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            void SetGrade
            (
                const char * grade /** grade */ 
            );
            /**Returns  the before text toggle 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: bool ByBeforeText
            (
            );
            /**Sets  the before text toggle 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetByBeforeText
            (
                bool beforeText /** beforetext */ 
            );
            /**Returns  the before text enum 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::SearchModelViewBuilder::TextComparisionOptions BeforeTextType
            (
            );
            /**Sets  the before text enum 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetBeforeTextType
            (
                NXOpen::Annotations::SearchModelViewBuilder::TextComparisionOptions beforeTextType /** beforetexttype */ 
            );
            /**Returns  the before text 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXString BeforeText
            (
            );
            /**Sets  the before text 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetBeforeText
            (
                const NXString & beforeText /** beforetext */ 
            );
            /**Sets  the before text 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            void SetBeforeText
            (
                const char * beforeText /** beforetext */ 
            );
            /**Returns  the after text toggle 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: bool ByAfterText
            (
            );
            /**Sets  the after text toggle 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetByAfterText
            (
                bool afterText /** aftertext */ 
            );
            /**Returns  the after text enum 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::SearchModelViewBuilder::TextComparisionOptions AfterTextType
            (
            );
            /**Sets  the after text enum 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetAfterTextType
            (
                NXOpen::Annotations::SearchModelViewBuilder::TextComparisionOptions afterTextType /** aftertexttype */ 
            );
            /**Returns  the after text 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXString AfterText
            (
            );
            /**Sets  the after text 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetAfterText
            (
                const NXString & afterText /** aftertext */ 
            );
            /**Sets  the after text 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            void SetAfterText
            (
                const char * afterText /** aftertext */ 
            );
            /**Returns  the above text toggle 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: bool ByAboveText
            (
            );
            /**Sets  the above text toggle 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetByAboveText
            (
                bool aboveText /** abovetext */ 
            );
            /**Returns  the above text enum 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::SearchModelViewBuilder::TextComparisionOptions AboveTextType
            (
            );
            /**Sets  the above text enum 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetAboveTextType
            (
                NXOpen::Annotations::SearchModelViewBuilder::TextComparisionOptions aboveTextType /** abovetexttype */ 
            );
            /**Returns  the above text 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXString AboveText
            (
            );
            /**Sets  the above text 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetAboveText
            (
                const NXString & aboveText /** abovetext */ 
            );
            /**Sets  the above text 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            void SetAboveText
            (
                const char * aboveText /** abovetext */ 
            );
            /**Returns  the below text toggle 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: bool ByBelowText
            (
            );
            /**Sets  the below text toggle 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetByBelowText
            (
                bool belowText /** belowtext */ 
            );
            /**Returns  the below text enum 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::SearchModelViewBuilder::TextComparisionOptions BelowTextType
            (
            );
            /**Sets  the below text enum 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetBelowTextType
            (
                NXOpen::Annotations::SearchModelViewBuilder::TextComparisionOptions belowTextType /** belowtexttype */ 
            );
            /**Returns  the below text 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXString BelowText
            (
            );
            /**Sets  the below text 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetBelowText
            (
                const NXString & belowText /** belowtext */ 
            );
            /**Sets  the below text 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            void SetBelowText
            (
                const char * belowText /** belowtext */ 
            );
            /**Returns  the callout block 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::SearchCriteriaCalloutBuilder * Callout
            (
            );
            /**Returns  the measurement type 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::SearchCriteriaDimensionBuilder::MeasurementTypes MeasurementType
            (
            );
            /**Sets  the measurement type 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void SetMeasurementType
            (
                NXOpen::Annotations::SearchCriteriaDimensionBuilder::MeasurementTypes measurementType /** measurementtype */ 
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
