#ifndef NXOpen_TOOLING_LAYOUTBUILDER_HXX_INCLUDED
#define NXOpen_TOOLING_LAYOUTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Tooling_LayoutBuilder.ja
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
#include <NXOpen/Expression.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/Tooling_LayoutBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Tooling
    {
        class LayoutBuilder;
    }
    class Builder;
    class Direction;
    class Expression;
    class Point;
    class SelectBodyList;
    namespace Tooling
    {
        class _LayoutBuilderBuilder;
        /** Represents a Tooling::LayoutBuilder builder  <br> To create a new instance of this class, use @link Tooling::MWLayoutCollection::CreateLayoutBuilder Tooling::MWLayoutCollection::CreateLayoutBuilder@endlink  <br> 
        Default values:
        CirCavityNumber: 2
        CirRadius: 0
        CirRotateAngle: 360
        CirStartAngle: 0
        DimBalFirst.RightHandSide: 0 (millimeters part), 0 (inches part)
        LinXnumber: 2
        LinYnumber: 1
        */
        class NXOPENCPPEXPORT LayoutBuilder : public Builder
        {
            /** The JA_LAYOUT_BUILDER_layout_type is an index to the type of layout. */
            public: enum LayoutType
            {
                LayoutTypeRectangle/** Rectangle layout */,
                LayoutTypeCircular/** Circle layout */
            };

            /** The JA_LAYOUT_BUILDER_layout_sub_type is an index to the sub type of layout. */
            public: enum LayoutSubType
            {
                LayoutSubTypeBalance/** Balance type */,
                LayoutSubTypeLinear/** Linear type */,
                LayoutSubTypeRadial/** Radial circular type */,
                LayoutSubTypeConstant/** Constanct circular type */
            };

            /** The JA_LAYOUT_BUILDER_bal_number is an index to the number of balance cavity. */
            public: enum BalNumber
            {
                BalNumberTwo/** Two balance cavities */,
                BalNumberFour/** Four balance cavities */
            };

            /** The JA_LAYOUT_BUILDER_xref_num is an index to the type of x move refer. */
            public: enum XrefNum
            {
                XrefNumBlock/** Block type */,
                XrefNumMove/** Move type */
            };

            /** The JA_LAYOUT_BUILDER_yref_num is an index to the type of y move refer. */
            public: enum YrefNum
            {
                YrefNumBlock/** Block type */,
                YrefNumMove/** Move type */
            };

            private: friend class  _LayoutBuilderBuilder;
            protected: LayoutBuilder();
            /**Returns  the select cavity  <br> License requirements : None */
            public: NXOpen::SelectBodyList * SelectCavity
            (
            );
            /**Returns  the layout pattern type  <br> License requirements : None */
            public: NXOpen::Tooling::LayoutBuilder::LayoutType MwLayoutType
            (
            );
            /**Sets  the layout pattern type  <br> License requirements : None */
            public: void SetMwLayoutType
            (
                NXOpen::Tooling::LayoutBuilder::LayoutType enumLayoutType /** enumlayouttype */ 
            );
            /**Returns  the layout transform type  <br> License requirements : None */
            public: NXOpen::Tooling::LayoutBuilder::LayoutSubType SubType
            (
            );
            /**Sets  the layout transform type  <br> License requirements : None */
            public: void SetSubType
            (
                NXOpen::Tooling::LayoutBuilder::LayoutSubType enumSubType /** enumsubtype */ 
            );
            /**Returns  the rotate point  <br> License requirements : None */
            public: NXOpen::Point * RotatePoint
            (
            );
            /**Sets  the rotate point  <br> License requirements : None */
            public: void SetRotatePoint
            (
                NXOpen::Point * rotatePoint /** rotatepoint */ 
            );
            /**Returns  the rotate vector  <br> License requirements : None */
            public: NXOpen::Direction * LayoutVector
            (
            );
            /**Sets  the rotate vector  <br> License requirements : None */
            public: void SetLayoutVector
            (
                NXOpen::Direction * layoutVector /** layoutvector */ 
            );
            /**Returns  the balance cavity number  <br> License requirements : None */
            public: NXOpen::Tooling::LayoutBuilder::BalNumber BalCavityNumber
            (
            );
            /**Sets  the balance cavity number  <br> License requirements : None */
            public: void SetBalCavityNumber
            (
                NXOpen::Tooling::LayoutBuilder::BalNumber enumBalCavityNumber /** enumbalcavitynumber */ 
            );
            /**Returns  the first dimension for balance transform  <br> License requirements : None */
            public: NXOpen::Expression * DimBalFirst
            (
            );
            /**Returns  the second dimension for balance transform  <br> License requirements : None */
            public: NXOpen::Expression * DimBalSecond
            (
            );
            /**Returns  the copy number for linear transform in X-axis  <br> License requirements : None */
            public: int LinXnumber
            (
            );
            /**Sets  the copy number for linear transform in X-axis  <br> License requirements : None */
            public: void SetLinXnumber
            (
                int linXNumber /** linxnumber */ 
            );
            /**Returns  the layout cavity number in X-axis  <br> License requirements : None */
            public: NXOpen::Tooling::LayoutBuilder::XrefNum Xref
            (
            );
            /**Sets  the layout cavity number in X-axis  <br> License requirements : None */
            public: void SetXref
            (
                NXOpen::Tooling::LayoutBuilder::XrefNum enumXRef /** enumxref */ 
            );
            /**Returns  the cavity distance dimension in X-axis  <br> License requirements : None */
            public: NXOpen::Expression * DimXdist
            (
            );
            /**Returns  the copy number for linear transform in Y-axis  <br> License requirements : None */
            public: int LinYnumber
            (
            );
            /**Sets  the copy number for linear transform in Y-axis  <br> License requirements : None */
            public: void SetLinYnumber
            (
                int linYNumber /** linynumber */ 
            );
            /**Returns  the layout cavity number in Y-axis  <br> License requirements : None */
            public: NXOpen::Tooling::LayoutBuilder::YrefNum Yref
            (
            );
            /**Sets  the layout cavity number in Y-axis  <br> License requirements : None */
            public: void SetYref
            (
                NXOpen::Tooling::LayoutBuilder::YrefNum enumYRef /** enumyref */ 
            );
            /**Returns  the cavity distance dimension in Y-axis  <br> License requirements : None */
            public: NXOpen::Expression * DimYdist
            (
            );
            /**Returns  the copy number for circular transform  <br> License requirements : None */
            public: int CirCavityNumber
            (
            );
            /**Sets  the copy number for circular transform  <br> License requirements : None */
            public: void SetCirCavityNumber
            (
                int cirCavityNumber /** circavitynumber */ 
            );
            /**Returns  the start angle  <br> License requirements : None */
            public: double CirStartAngle
            (
            );
            /**Sets  the start angle  <br> License requirements : None */
            public: void SetCirStartAngle
            (
                double cirStartAngle /** cirstartangle */ 
            );
            /**Returns  the rotate angle  <br> License requirements : None */
            public: double CirRotateAngle
            (
            );
            /**Sets  the rotate angle  <br> License requirements : None */
            public: void SetCirRotateAngle
            (
                double cirRotateAngle /** cirrotateangle */ 
            );
            /**Returns  the radius value  <br> License requirements : None */
            public: double CirRadius
            (
            );
            /**Sets  the radius value  <br> License requirements : None */
            public: void SetCirRadius
            (
                double cirRadius /** cirradius */ 
            );
            /** Perform cavity layout  <br> License requirements : None */
            public: void Layout
            (
            );
            /** Insert pocket  <br> License requirements : None */
            public: void Insertpocket
            (
            );
            /** Reposition cavity  <br> License requirements : None */
            public: void Transform
            (
            );
            /** Remove cavity  <br> License requirements : None */
            public: void Remove
            (
            );
            /** Make center of cavity  <br> License requirements : None */
            public: void Autocenter
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif