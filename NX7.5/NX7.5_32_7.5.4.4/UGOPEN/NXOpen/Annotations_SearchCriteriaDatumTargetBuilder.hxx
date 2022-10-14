#ifndef NXOpen_ANNOTATIONS_SEARCHCRITERIADATUMTARGETBUILDER_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_SEARCHCRITERIADATUMTARGETBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_SearchCriteriaDatumTargetBuilder.ja
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
#include <NXOpen/Annotations_SearchCriteriaDatumTargetBuilder.hxx>
#include <NXOpen/Annotations_SearchModelViewBuilder.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Annotations
    {
        class SearchCriteriaDatumTargetBuilder;
    }
    class Builder;
    namespace Annotations
    {
        class _SearchCriteriaDatumTargetBuilderBuilder;
        class SearchCriteriaDatumTargetBuilderImpl;
        /** Represents SearchCriteriaDatumTargetBuilder  <br> To create a new instance of this class, use @link Annotations::SearchModelViewCollection::CreateSearchCriteriaDatumTargetBuilder Annotations::SearchModelViewCollection::CreateSearchCriteriaDatumTargetBuilder@endlink  <br> */
        class NXOPENCPPEXPORT  SearchCriteriaDatumTargetBuilder : public Builder
        {
            /** Lists the search pmi datum target type*/
            public: enum DatumTargetTypes
            {
                DatumTargetTypesPoint/** point type*/,
                DatumTargetTypesLine/** line type*/,
                DatumTargetTypesRectangular/** rectangular type*/,
                DatumTargetTypesCircular/** circular type*/,
                DatumTargetTypesAnnular/** annular type*/,
                DatumTargetTypesCylindrical/** cylindrical type*/,
                DatumTargetTypesArbitrary/** arbitray type*/
            };

            private: SearchCriteriaDatumTargetBuilderImpl * m_searchcriteriadatumtargetbuilder_impl;
            private: friend class  _SearchCriteriaDatumTargetBuilderBuilder;
            protected: SearchCriteriaDatumTargetBuilder();
            public: ~SearchCriteriaDatumTargetBuilder();
            /**Returns  the datum target label toggle  <br> License requirements : None */
            public: bool ByDatumTargetLabel
            (
            );
            /**Sets  the datum target label toggle  <br> License requirements : None */
            public: void SetByDatumTargetLabel
            (
                bool datumTargetLabel /** datumtargetlabel */ 
            );
            /**Returns  the datum target label text  <br> License requirements : None */
            public: NXString DatumTargetLabelText
            (
            );
            /**Sets  the datum target label text  <br> License requirements : None */
            public: void SetDatumTargetLabelText
            (
                const NXString & datumTargetLabelText /** datumtargetlabeltext */ 
            );
            /**Returns  the datum target type toggle  <br> License requirements : None */
            public: bool ByDatumTargetType
            (
            );
            /**Sets  the datum target type toggle  <br> License requirements : None */
            public: void SetByDatumTargetType
            (
                bool datumTargetType /** datumtargettype */ 
            );
            /**Returns  the datum target type enum  <br> License requirements : None */
            public: NXOpen::Annotations::SearchCriteriaDatumTargetBuilder::DatumTargetTypes DatumTargetType
            (
            );
            /**Sets  the datum target type enum  <br> License requirements : None */
            public: void SetDatumTargetType
            (
                NXOpen::Annotations::SearchCriteriaDatumTargetBuilder::DatumTargetTypes datumTargetType /** datumtargettype */ 
            );
            /**Returns  the width toggle  <br> License requirements : None */
            public: bool ByWidth
            (
            );
            /**Sets  the width toggle  <br> License requirements : None */
            public: void SetByWidth
            (
                bool width /** width */ 
            );
            /**Returns  the width enum  <br> License requirements : None */
            public: NXOpen::Annotations::SearchModelViewBuilder::ValueComparisionOptions WidthType
            (
            );
            /**Sets  the width enum  <br> License requirements : None */
            public: void SetWidthType
            (
                NXOpen::Annotations::SearchModelViewBuilder::ValueComparisionOptions widthType /** widthtype */ 
            );
            /**Returns  the width value  <br> License requirements : None */
            public: double WidthValue
            (
            );
            /**Sets  the width value  <br> License requirements : None */
            public: void SetWidthValue
            (
                double widthValue /** widthvalue */ 
            );
            /**Returns  the height toggle  <br> License requirements : None */
            public: bool ByHeight
            (
            );
            /**Sets  the height toggle  <br> License requirements : None */
            public: void SetByHeight
            (
                bool height /** height */ 
            );
            /**Returns  the height enum  <br> License requirements : None */
            public: NXOpen::Annotations::SearchModelViewBuilder::ValueComparisionOptions HeightType
            (
            );
            /**Sets  the height enum  <br> License requirements : None */
            public: void SetHeightType
            (
                NXOpen::Annotations::SearchModelViewBuilder::ValueComparisionOptions heightType /** heighttype */ 
            );
            /**Returns  the height value  <br> License requirements : None */
            public: double HeightValue
            (
            );
            /**Sets  the height value  <br> License requirements : None */
            public: void SetHeightValue
            (
                double heightValue /** heightvalue */ 
            );
            /**Returns  the outer diameter toggle  <br> License requirements : None */
            public: bool ByOuterDiameter
            (
            );
            /**Sets  the outer diameter toggle  <br> License requirements : None */
            public: void SetByOuterDiameter
            (
                bool outerDiameter /** outerdiameter */ 
            );
            /**Returns  the outer diameter enum  <br> License requirements : None */
            public: NXOpen::Annotations::SearchModelViewBuilder::ValueComparisionOptions OuterDiameterType
            (
            );
            /**Sets  the outer diameter enum  <br> License requirements : None */
            public: void SetOuterDiameterType
            (
                NXOpen::Annotations::SearchModelViewBuilder::ValueComparisionOptions outerDiameterType /** outerdiametertype */ 
            );
            /**Returns  the outer diameter value  <br> License requirements : None */
            public: double OuterDiameterValue
            (
            );
            /**Sets  the outer diameter value  <br> License requirements : None */
            public: void SetOuterDiameterValue
            (
                double outerDiameterValue /** outerdiametervalue */ 
            );
            /**Returns  the inner diameter toggle  <br> License requirements : None */
            public: bool ByInnerDiameter
            (
            );
            /**Sets  the inner diameter toggle  <br> License requirements : None */
            public: void SetByInnerDiameter
            (
                bool innerDiameter /** innerdiameter */ 
            );
            /**Returns  the inner diameter enum  <br> License requirements : None */
            public: NXOpen::Annotations::SearchModelViewBuilder::ValueComparisionOptions InnerDiameterType
            (
            );
            /**Sets  the inner diameter enum  <br> License requirements : None */
            public: void SetInnerDiameterType
            (
                NXOpen::Annotations::SearchModelViewBuilder::ValueComparisionOptions innerDiameterType /** innerdiametertype */ 
            );
            /**Returns  the inner diameter value  <br> License requirements : None */
            public: double InnerDiameterValue
            (
            );
            /**Sets  the inner diameter value  <br> License requirements : None */
            public: void SetInnerDiameterValue
            (
                double innerDiameterValue /** innerdiametervalue */ 
            );
            /**Returns  the text toggle  <br> License requirements : None */
            public: bool ByText
            (
            );
            /**Sets  the text toggle  <br> License requirements : None */
            public: void SetByText
            (
                bool text /** text */ 
            );
            /**Returns  the text enum  <br> License requirements : None */
            public: NXOpen::Annotations::SearchModelViewBuilder::TextComparisionOptions TextType
            (
            );
            /**Sets  the text enum  <br> License requirements : None */
            public: void SetTextType
            (
                NXOpen::Annotations::SearchModelViewBuilder::TextComparisionOptions textType /** texttype */ 
            );
            /**Returns  the text  <br> License requirements : None */
            public: NXString Text
            (
            );
            /**Sets  the text  <br> License requirements : None */
            public: void SetText
            (
                const NXString & text /** text */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif