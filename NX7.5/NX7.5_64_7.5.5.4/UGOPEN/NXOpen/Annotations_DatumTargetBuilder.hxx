#ifndef NXOpen_ANNOTATIONS_DATUMTARGETBUILDER_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_DATUMTARGETBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_DatumTargetBuilder.ja
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
#include <NXOpen/Annotations_DatumTargetBuilder.hxx>
#include <NXOpen/Annotations_LeaderBuilder.hxx>
#include <NXOpen/Annotations_OriginBuilder.hxx>
#include <NXOpen/Annotations_StyleBuilder.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/Expression.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Annotations
    {
        class DatumTargetBuilder;
    }
    namespace Annotations
    {
        class LeaderBuilder;
    }
    namespace Annotations
    {
        class OriginBuilder;
    }
    namespace Annotations
    {
        class StyleBuilder;
    }
    class Builder;
    class Expression;
    namespace Annotations
    {
        class _DatumTargetBuilderBuilder;
        class DatumTargetBuilderImpl;
        /** Represents a Datum target Builder  <br> This is an abstract class, and cannot be instantiated. <br> */
        class NXOPENCPPEXPORT  DatumTargetBuilder : public Builder
        {
            /** datum symbol type */
            public: enum Types
            {
                TypesPoint/** point */,
                TypesLine/** point */,
                TypesRectangular/** rectangular */,
                TypesCircular/** circular */,
                TypesAnnular/** annular */,
                TypesCylindrical/** cylindrical */,
                TypesArbitrary/** arbitrary */
            };

            private: DatumTargetBuilderImpl * m_datumtargetbuilder_impl;
            private: friend class  _DatumTargetBuilderBuilder;
            protected: DatumTargetBuilder();
            public: ~DatumTargetBuilder();
            /**Returns  the origin  <br> License requirements : None */
            public: NXOpen::Annotations::OriginBuilder * Origin
            (
            );
            /**Returns  the @link Annotations::LeaderBuilder Annotations::LeaderBuilder@endlink  for the annotation  <br> License requirements : None */
            public: NXOpen::Annotations::LeaderBuilder * Leader
            (
            );
            /**Returns  the label  <br> License requirements : None */
            public: NXString Label
            (
            );
            /**Sets  the label  <br> License requirements : drafting ("DRAFTING") OR geometric_tol ("GDT") */
            public: void SetLabel
            (
                const NXString & label /** label */ 
            );
            /**Returns  the index  <br> License requirements : None */
            public: int Index
            (
            );
            /**Sets  the index  <br> License requirements : drafting ("DRAFTING") OR geometric_tol ("GDT") */
            public: void SetIndex
            (
                int index /** index */ 
            );
            /**Returns  the width  <br> License requirements : None */
            public: NXOpen::Expression * Width
            (
            );
            /**Returns  the height  <br> License requirements : None */
            public: NXOpen::Expression * Height
            (
            );
            /**Returns  the outer diameter  <br> License requirements : None */
            public: NXOpen::Expression * OuterDiameter
            (
            );
            /**Returns  the inner diameter  <br> License requirements : None */
            public: NXOpen::Expression * InnerDiameter
            (
            );
            /**Returns  the area size  <br> License requirements : None */
            public: NXString AreaSize
            (
            );
            /**Sets  the area size  <br> License requirements : drafting ("DRAFTING") OR geometric_tol ("GDT") */
            public: void SetAreaSize
            (
                const NXString & areaSize /** areasize */ 
            );
            /**Returns  the style  <br> License requirements : None */
            public: NXOpen::Annotations::StyleBuilder * Style
            (
            );
            /**Returns  the type  <br> License requirements : None */
            public: NXOpen::Annotations::DatumTargetBuilder::Types Type
            (
            );
            /**Sets  the type  <br> License requirements : drafting ("DRAFTING") OR geometric_tol ("GDT") */
            public: void SetType
            (
                NXOpen::Annotations::DatumTargetBuilder::Types type /** type */ 
            );
            /**Returns  the draw x  <br> License requirements : None */
            public: bool DrawX
            (
            );
            /**Sets  the draw x  <br> License requirements : drafting ("DRAFTING") OR geometric_tol ("GDT") */
            public: void SetDrawX
            (
                bool flag /** flag */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif