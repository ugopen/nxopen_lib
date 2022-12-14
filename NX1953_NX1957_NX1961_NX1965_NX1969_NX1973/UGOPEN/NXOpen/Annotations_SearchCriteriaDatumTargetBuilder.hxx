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
        class SearchCriteriaDatumTargetBuilder;
    }
    class Builder;
    namespace Annotations
    {
        class _SearchCriteriaDatumTargetBuilderBuilder;
        class SearchCriteriaDatumTargetBuilderImpl;
        /** Represents SearchCriteriaDatumTargetBuilder  <br> To create a new instance of this class, use @link NXOpen::Annotations::SearchModelViewCollection::CreateSearchCriteriaDatumTargetBuilder  NXOpen::Annotations::SearchModelViewCollection::CreateSearchCriteriaDatumTargetBuilder @endlink  <br> 
         <br>  Created in NX7.5.0.  <br>  
        */
        class NXOPENCPP_ANNOTATIONSEXPORT  SearchCriteriaDatumTargetBuilder : public NXOpen::Builder
        {
            /** Lists the search pmi datum target type*/
            public: enum DatumTargetTypes
            {
                DatumTargetTypesPoint/** point type*/,
                DatumTargetTypesLine/** line type*/,
                DatumTargetTypesRectangular/** rectangular type*/,
                DatumTargetTypesCircular/** circular type*/,
                DatumTargetTypesAnnular/** annular type*/,
                DatumTargetTypesSpherical/** spherical type*/,
                DatumTargetTypesCylindrical/** cylindrical type*/,
                DatumTargetTypesArbitrary/** arbitray type*/
            };

            /** Represents the search pmi movable datum target type*/
            public: enum DatumTargetMovableOptions
            {
                DatumTargetMovableOptionsNo/** Datum Target*/,
                DatumTargetMovableOptionsYes/** Movable Datum Target*/
            };

            private: SearchCriteriaDatumTargetBuilderImpl * m_searchcriteriadatumtargetbuilder_impl;
            private: friend class  _SearchCriteriaDatumTargetBuilderBuilder;
            protected: SearchCriteriaDatumTargetBuilder();
            public: ~SearchCriteriaDatumTargetBuilder();
            /**Returns  the datum target label toggle 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: bool ByDatumTargetLabel
            (
            );
            /**Sets  the datum target label toggle 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetByDatumTargetLabel
            (
                bool datumTargetLabel /** datumtargetlabel */ 
            );
            /**Returns  the datum target label text 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXString DatumTargetLabelText
            (
            );
            /**Sets  the datum target label text 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetDatumTargetLabelText
            (
                const NXString & datumTargetLabelText /** datumtargetlabeltext */ 
            );
            /**Sets  the datum target label text 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            void SetDatumTargetLabelText
            (
                const char * datumTargetLabelText /** datumtargetlabeltext */ 
            );
            /**Returns  the datum target type toggle 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: bool ByDatumTargetType
            (
            );
            /**Sets  the datum target type toggle 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetByDatumTargetType
            (
                bool datumTargetType /** datumtargettype */ 
            );
            /**Returns  the datum target type enum 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::SearchCriteriaDatumTargetBuilder::DatumTargetTypes DatumTargetType
            (
            );
            /**Sets  the datum target type enum 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetDatumTargetType
            (
                NXOpen::Annotations::SearchCriteriaDatumTargetBuilder::DatumTargetTypes datumTargetType /** datumtargettype */ 
            );
            /**Returns  the width toggle 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: bool ByWidth
            (
            );
            /**Sets  the width toggle 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetByWidth
            (
                bool width /** width */ 
            );
            /**Returns  the width enum 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::SearchModelViewBuilder::ValueComparisionOptions WidthType
            (
            );
            /**Sets  the width enum 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetWidthType
            (
                NXOpen::Annotations::SearchModelViewBuilder::ValueComparisionOptions widthType /** widthtype */ 
            );
            /**Returns  the width value 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: double WidthValue
            (
            );
            /**Sets  the width value 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetWidthValue
            (
                double widthValue /** widthvalue */ 
            );
            /**Returns  the height toggle 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: bool ByHeight
            (
            );
            /**Sets  the height toggle 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetByHeight
            (
                bool height /** height */ 
            );
            /**Returns  the height enum 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::SearchModelViewBuilder::ValueComparisionOptions HeightType
            (
            );
            /**Sets  the height enum 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetHeightType
            (
                NXOpen::Annotations::SearchModelViewBuilder::ValueComparisionOptions heightType /** heighttype */ 
            );
            /**Returns  the height value 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: double HeightValue
            (
            );
            /**Sets  the height value 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetHeightValue
            (
                double heightValue /** heightvalue */ 
            );
            /**Returns  the outer diameter toggle 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: bool ByOuterDiameter
            (
            );
            /**Sets  the outer diameter toggle 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetByOuterDiameter
            (
                bool outerDiameter /** outerdiameter */ 
            );
            /**Returns  the outer diameter enum 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::SearchModelViewBuilder::ValueComparisionOptions OuterDiameterType
            (
            );
            /**Sets  the outer diameter enum 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetOuterDiameterType
            (
                NXOpen::Annotations::SearchModelViewBuilder::ValueComparisionOptions outerDiameterType /** outerdiametertype */ 
            );
            /**Returns  the outer diameter value 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: double OuterDiameterValue
            (
            );
            /**Sets  the outer diameter value 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetOuterDiameterValue
            (
                double outerDiameterValue /** outerdiametervalue */ 
            );
            /**Returns  the inner diameter toggle 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: bool ByInnerDiameter
            (
            );
            /**Sets  the inner diameter toggle 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetByInnerDiameter
            (
                bool innerDiameter /** innerdiameter */ 
            );
            /**Returns  the inner diameter enum 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::SearchModelViewBuilder::ValueComparisionOptions InnerDiameterType
            (
            );
            /**Sets  the inner diameter enum 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetInnerDiameterType
            (
                NXOpen::Annotations::SearchModelViewBuilder::ValueComparisionOptions innerDiameterType /** innerdiametertype */ 
            );
            /**Returns  the inner diameter value 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: double InnerDiameterValue
            (
            );
            /**Sets  the inner diameter value 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetInnerDiameterValue
            (
                double innerDiameterValue /** innerdiametervalue */ 
            );
            /**Returns  the text toggle 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: bool ByText
            (
            );
            /**Sets  the text toggle 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetByText
            (
                bool text /** text */ 
            );
            /**Returns  the text enum 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::SearchModelViewBuilder::TextComparisionOptions TextType
            (
            );
            /**Sets  the text enum 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetTextType
            (
                NXOpen::Annotations::SearchModelViewBuilder::TextComparisionOptions textType /** texttype */ 
            );
            /**Returns  the text 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXString Text
            (
            );
            /**Sets  the text 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetText
            (
                const NXString & text /** text */ 
            );
            /**Sets  the text 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            void SetText
            (
                const char * text /** text */ 
            );
            /**Returns  the movable datum target option 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: bool ByDatumMovable
            (
            );
            /**Sets  the movable datum target option 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void SetByDatumMovable
            (
                bool datumMovable /** datummovable */ 
            );
            /**Returns  the movable datum target type 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::SearchCriteriaDatumTargetBuilder::DatumTargetMovableOptions DatumMovable
            (
            );
            /**Sets  the movable datum target type 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void SetDatumMovable
            (
                NXOpen::Annotations::SearchCriteriaDatumTargetBuilder::DatumTargetMovableOptions datumTargetMovable /** datumtargetmovable */ 
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
