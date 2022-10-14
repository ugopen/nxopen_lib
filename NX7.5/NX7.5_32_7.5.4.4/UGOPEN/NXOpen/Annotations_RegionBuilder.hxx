#ifndef NXOpen_ANNOTATIONS_REGIONBUILDER_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_REGIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_RegionBuilder.ja
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
#include <NXOpen/Annotations_PlaneBuilder.hxx>
#include <NXOpen/Annotations_RegionBuilder.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/Expression.hxx>
#include <NXOpen/ObjectList.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Annotations
    {
        class RegionBuilder;
    }
    namespace Annotations
    {
        class ArbitraryAreaSeedBuilderList;
    }
    namespace Annotations
    {
        class PlaneBuilder;
    }
    class Builder;
    class Expression;
    class NXColor;
    class Point;
    class SelectDisplayableObjectList;
    namespace Annotations
    {
        class _RegionBuilderBuilder;
        class RegionBuilderImpl;
        /** Represents a @link Annotations::RegionBuilder Annotations::RegionBuilder@endlink  builder  <br> To create a new instance of this class, use @link Annotations::PmiRegionCollection::CreateRegionBuilder Annotations::PmiRegionCollection::CreateRegionBuilder@endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        ConformToSurface </td> <td> 
         
        0 </td> </tr> 

        </table>  
        */
        class NXOPENCPPEXPORT  RegionBuilder : public Builder
        {
            /** Specifies the region type */
            public: enum Types
            {
                TypesRectangularRegion/** rectangular */,
                TypesCircularRegion/** circular */,
                TypesAnnularRegion/** annular */,
                TypesCylindricalRegion/** cylindrical */,
                TypesArbitraryRegion/** arbitrary */
            };

            /** Specifies the anchor location of the region */
            public: enum AlignmentPosition
            {
                AlignmentPositionTopLeft/** top left */,
                AlignmentPositionTopCenter/** top center */,
                AlignmentPositionTopRight/** top right */,
                AlignmentPositionMiddleLeft/** middle left */,
                AlignmentPositionMiddleCenter/** middle center */,
                AlignmentPositionMiddleRight/** middle right */,
                AlignmentPositionBottomLeft/** bottom left */,
                AlignmentPositionBottomCenter/** bottom center */,
                AlignmentPositionBottomRight/** bottom right */
            };

            /** Specifies the crosshatch pattern */
            public: enum CrosshatchPatterns
            {
                CrosshatchPatternsNone/** none */,
                CrosshatchPatternsGeneralUse/** general use */
            };

            private: RegionBuilderImpl * m_regionbuilder_impl;
            private: friend class  _RegionBuilderBuilder;
            protected: RegionBuilder();
            public: ~RegionBuilder();
            /**Returns  the origin
                        Only available when region type is
                        @link Annotations::RegionBuilder::TypesRectangularRegion Annotations::RegionBuilder::TypesRectangularRegion@endlink ,
                        @link Annotations::RegionBuilder::TypesCircularRegion Annotations::RegionBuilder::TypesCircularRegion@endlink ,
                        @link Annotations::RegionBuilder::TypesAnnularRegion Annotations::RegionBuilder::TypesAnnularRegion@endlink   <br> License requirements : None */
            public: NXOpen::Point * Origin
            (
            );
            /**Sets  the origin
                        Only available when region type is
                        @link Annotations::RegionBuilder::TypesRectangularRegion Annotations::RegionBuilder::TypesRectangularRegion@endlink ,
                        @link Annotations::RegionBuilder::TypesCircularRegion Annotations::RegionBuilder::TypesCircularRegion@endlink ,
                        @link Annotations::RegionBuilder::TypesAnnularRegion Annotations::RegionBuilder::TypesAnnularRegion@endlink   <br> License requirements : geometric_tol ("GDT") */
            public: void SetOrigin
            (
                NXOpen::Point * origin /** origin */ 
            );
            /**Returns  the anchor
                        Only available when region type is
                        @link Annotations::RegionBuilder::TypesRectangularRegion Annotations::RegionBuilder::TypesRectangularRegion@endlink ,
                        @link Annotations::RegionBuilder::TypesCircularRegion Annotations::RegionBuilder::TypesCircularRegion@endlink ,
                        @link Annotations::RegionBuilder::TypesAnnularRegion Annotations::RegionBuilder::TypesAnnularRegion@endlink   <br> License requirements : None */
            public: NXOpen::Annotations::RegionBuilder::AlignmentPosition Anchor
            (
            );
            /**Sets  the anchor
                        Only available when region type is
                        @link Annotations::RegionBuilder::TypesRectangularRegion Annotations::RegionBuilder::TypesRectangularRegion@endlink ,
                        @link Annotations::RegionBuilder::TypesCircularRegion Annotations::RegionBuilder::TypesCircularRegion@endlink ,
                        @link Annotations::RegionBuilder::TypesAnnularRegion Annotations::RegionBuilder::TypesAnnularRegion@endlink   <br> License requirements : geometric_tol ("GDT") */
            public: void SetAnchor
            (
                NXOpen::Annotations::RegionBuilder::AlignmentPosition anchor /** anchor */ 
            );
            /**Returns  the plane  <br> License requirements : None */
            public: NXOpen::Annotations::PlaneBuilder * Plane
            (
            );
            /**Returns  the conform to surface toggle 
                        Only available when region type is
                        @link Annotations::RegionBuilder::TypesRectangularRegion Annotations::RegionBuilder::TypesRectangularRegion@endlink ,
                        @link Annotations::RegionBuilder::TypesCircularRegion Annotations::RegionBuilder::TypesCircularRegion@endlink ,
                        @link Annotations::RegionBuilder::TypesAnnularRegion Annotations::RegionBuilder::TypesAnnularRegion@endlink   <br> License requirements : None */
            public: bool ConformToSurface
            (
            );
            /**Sets  the conform to surface toggle 
                        Only available when region type is
                        @link Annotations::RegionBuilder::TypesRectangularRegion Annotations::RegionBuilder::TypesRectangularRegion@endlink ,
                        @link Annotations::RegionBuilder::TypesCircularRegion Annotations::RegionBuilder::TypesCircularRegion@endlink ,
                        @link Annotations::RegionBuilder::TypesAnnularRegion Annotations::RegionBuilder::TypesAnnularRegion@endlink   <br> License requirements : geometric_tol ("GDT") */
            public: void SetConformToSurface
            (
                bool conformToSurfaceToggle /** conformtosurfacetoggle */ 
            );
            /**Returns  the select face 
                        Only available when region type is
                        @link Annotations::RegionBuilder::TypesRectangularRegion Annotations::RegionBuilder::TypesRectangularRegion@endlink ,
                        @link Annotations::RegionBuilder::TypesCircularRegion Annotations::RegionBuilder::TypesCircularRegion@endlink ,
                        @link Annotations::RegionBuilder::TypesAnnularRegion Annotations::RegionBuilder::TypesAnnularRegion@endlink   <br> License requirements : None */
            public: NXOpen::SelectDisplayableObjectList * SelectFace
            (
            );
            /**Returns  the select cylindrical face 
                        Only available when region type is
                        @link Annotations::RegionBuilder::TypesCylindricalRegion Annotations::RegionBuilder::TypesCylindricalRegion@endlink   <br> License requirements : None */
            public: NXOpen::SelectDisplayableObjectList * SelectCylindricalFace
            (
            );
            /**Returns  the outer diameter
                        Only available when region type is
                        @link Annotations::RegionBuilder::TypesCircularRegion Annotations::RegionBuilder::TypesCircularRegion@endlink ,
                        @link Annotations::RegionBuilder::TypesAnnularRegion Annotations::RegionBuilder::TypesAnnularRegion@endlink   <br> License requirements : None */
            public: NXOpen::Expression * OuterDiameter
            (
            );
            /**Returns  the inner diameter
                        Only available when region type is
                        @link Annotations::RegionBuilder::TypesAnnularRegion Annotations::RegionBuilder::TypesAnnularRegion@endlink   <br> License requirements : None */
            public: NXOpen::Expression * InnerDiameter
            (
            );
            /**Returns  the width
                        Only available when region type is
                        @link Annotations::RegionBuilder::TypesRectangularRegion Annotations::RegionBuilder::TypesRectangularRegion@endlink   <br> License requirements : None */
            public: NXOpen::Expression * Width
            (
            );
            /**Returns  the height
                        Only available when region type is
                        @link Annotations::RegionBuilder::TypesRectangularRegion Annotations::RegionBuilder::TypesRectangularRegion@endlink   <br> License requirements : None */
            public: NXOpen::Expression * Height
            (
            );
            /**Returns  the start point
                        Only available when the region type is
                        @link Annotations::RegionBuilder::TypesCylindricalRegion Annotations::RegionBuilder::TypesCylindricalRegion@endlink   <br> License requirements : None */
            public: NXOpen::Point * StartPoint
            (
            );
            /**Sets  the start point
                        Only available when the region type is
                        @link Annotations::RegionBuilder::TypesCylindricalRegion Annotations::RegionBuilder::TypesCylindricalRegion@endlink   <br> License requirements : geometric_tol ("GDT") */
            public: void SetStartPoint
            (
                NXOpen::Point * startPoint /** startpoint */ 
            );
            /**Returns  the end point
                        Only available when the region type is
                        @link Annotations::RegionBuilder::TypesCylindricalRegion Annotations::RegionBuilder::TypesCylindricalRegion@endlink   <br> License requirements : None */
            public: NXOpen::Point * EndPoint
            (
            );
            /**Sets  the end point
                        Only available when the region type is
                        @link Annotations::RegionBuilder::TypesCylindricalRegion Annotations::RegionBuilder::TypesCylindricalRegion@endlink   <br> License requirements : geometric_tol ("GDT") */
            public: void SetEndPoint
            (
                NXOpen::Point * endPoint /** endpoint */ 
            );
            /**Returns  the arbitrary area list
                        Only available when the region type is
                        @link Annotations::RegionBuilder::TypesArbitraryRegion Annotations::RegionBuilder::TypesArbitraryRegion@endlink   <br> License requirements : None */
            public: NXOpen::Annotations::ArbitraryAreaSeedBuilderList * ArbitraryAreaList
            (
            );
            /**Returns  the crosshatch distance  <br> License requirements : None */
            public: NXOpen::Expression * CrosshatchDistance
            (
            );
            /**Returns  the crosshatch angle  <br> License requirements : None */
            public: NXOpen::Expression * CrosshatchAngle
            (
            );
            /**Returns  the crosshatch pattern enum  <br> License requirements : None */
            public: NXOpen::Annotations::RegionBuilder::CrosshatchPatterns CrosshatchPattern
            (
            );
            /**Sets  the crosshatch pattern enum  <br> License requirements : geometric_tol ("GDT") */
            public: void SetCrosshatchPattern
            (
                NXOpen::Annotations::RegionBuilder::CrosshatchPatterns crosshatchPattern /** crosshatchpattern */ 
            );
            /**Returns  the crosshatch color  <br> License requirements : None */
            public: NXOpen::NXColor * CrosshatchColor
            (
            );
            /**Sets  the crosshatch color  <br> License requirements : geometric_tol ("GDT") */
            public: void SetCrosshatchColor
            (
                NXOpen::NXColor * crosshatchColor /** crosshatchcolor */ 
            );
            /**Returns  the type  <br> License requirements : None */
            public: NXOpen::Annotations::RegionBuilder::Types Type
            (
            );
            /**Sets  the type  <br> License requirements : geometric_tol ("GDT") */
            public: void SetType
            (
                NXOpen::Annotations::RegionBuilder::Types type /** type */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif