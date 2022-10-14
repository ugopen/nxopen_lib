#ifndef NXOpen_TOOLING_HOLEREPORTBUILDER_HXX_INCLUDED
#define NXOpen_TOOLING_HOLEREPORTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Tooling_HoleReportBuilder.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/Tooling_HoleReportBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Tooling
    {
        class HoleReportBuilder;
    }
    class Builder;
    namespace Drawings
    {
        class SelectDraftingViewList;
    }
    class Point;
    class SelectEdgeList;
    class SelectPointList;
    namespace Tooling
    {
        class _HoleReportBuilderBuilder;
        /**
             Represents a @link Tooling::HoleReportBuilder Tooling::HoleReportBuilder@endlink 
             This class is for Hole Report Design UI
             <br> To create a new instance of this class, use @link Tooling::HoleReportCollection::CreateHoleReportBuilder Tooling::HoleReportCollection::CreateHoleReportBuilder@endlink  <br> 
        Default values:
        QuadrantType: PositiveQuadrantI
        SelectionType: ViewSelection
        */
        class NXOPENCPPEXPORT HoleReportBuilder : public Builder
        {
            /** Specifies the option of selection type to create hole table */
            public: enum EnumSelectionType
            {
                EnumSelectionTypeViewSelection/** Selects view to create hole table */,
                EnumSelectionTypeWindowSelection/** Selects holes in window to create hole table */
            };

            /** Specifies the option of which quadrant is positive */
            public: enum EnumQuadrantType
            {
                EnumQuadrantTypePositiveQuadrantI/** First quadrant is positive */,
                EnumQuadrantTypePositiveQuadrantIi/** Second quadrant is positive */,
                EnumQuadrantTypePositiveQuadrantIii/** Third quadrant is positive */,
                EnumQuadrantTypePositiveQuadrantIv/** Forth quadrant is positive */,
                EnumQuadrantTypePositiveQuadrantAll/** All quadrant is positive */
            };

            private: friend class  _HoleReportBuilderBuilder;
            protected: HoleReportBuilder();
            /**Returns  the ordinate origin to get the coords in given ordinate  <br> License requirements : None */
            public: NXOpen::SelectPointList * OrdinateOrigin
            (
            );
            /**Returns  the selection type to choose select view or holes in window to create hole report  <br> License requirements : None */
            public: NXOpen::Tooling::HoleReportBuilder::EnumSelectionType SelectionType
            (
            );
            /**Sets  the selection type to choose select view or holes in window to create hole report  <br> License requirements : None */
            public: void SetSelectionType
            (
                NXOpen::Tooling::HoleReportBuilder::EnumSelectionType selectionType /** Sets the selection type value */
            );
            /**Returns  the view to create hole report  <br> License requirements : None */
            public: NXOpen::Drawings::SelectDraftingViewList * TableView
            (
            );
            /**Returns  the holes in window to create hole report  <br> License requirements : None */
            public: NXOpen::SelectEdgeList * TableHole
            (
            );
            /**Returns  the table origin  <br> License requirements : None */
            public: NXOpen::Point * TableOrigin
            (
            );
            /**Sets  the table origin  <br> License requirements : None */
            public: void SetTableOrigin
            (
                NXOpen::Point * tableOrigin /** Sets the table origin to create hole table */
            );
            /** Create hole table  <br> License requirements : None */
            public: void CreateTable
            (
            );
            /**Returns  the hole table to edit  <br> License requirements : None */
            public: NXOpen::SelectEdgeList * HoleTable
            (
            );
            /**Returns  the holes to add to the table  <br> License requirements : None */
            public: NXOpen::SelectEdgeList * TableAddHole
            (
            );
            /** Edit hole table  <br> License requirements : None */
            public: void EditTable
            (
            );
            /**Returns  the positive quadrant type  <br> License requirements : None */
            public: NXOpen::Tooling::HoleReportBuilder::EnumQuadrantType QuadrantType
            (
            );
            /**Sets  the positive quadrant type  <br> License requirements : None */
            public: void SetQuadrantType
            (
                NXOpen::Tooling::HoleReportBuilder::EnumQuadrantType quadrantType /** Sets the positive quadrant type */
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif