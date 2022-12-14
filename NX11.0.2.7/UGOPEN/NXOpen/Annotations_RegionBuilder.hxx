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
#include <NXOpen/Annotations_HatchFillSettingsBuilder.hxx>
#include <NXOpen/Annotations_PlaneBuilder.hxx>
#include <NXOpen/Annotations_RegionBuilder.hxx>
#include <NXOpen/Expression.hxx>
#include <NXOpen/LineColorFontWidthBuilder.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/ObjectList.hxx>
#include <NXOpen/SelectObjectList.hxx>
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
        class RegionBuilder;
    }
    namespace Annotations
    {
        class ArbitraryAreaSeedBuilderList;
    }
    namespace Annotations
    {
        class HatchFillSettingsBuilder;
    }
    namespace Annotations
    {
        class PlaneBuilder;
    }
    class Builder;
    class Expression;
    class LineColorFontWidthBuilder;
    class NXColor;
    class Point;
    class SelectDisplayableObjectList;
    namespace Annotations
    {
        class _RegionBuilderBuilder;
        class RegionBuilderImpl;
        /** Represents a @link NXOpen::Annotations::RegionBuilder NXOpen::Annotations::RegionBuilder@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::Annotations::PmiRegionCollection::CreateRegionBuilder  NXOpen::Annotations::PmiRegionCollection::CreateRegionBuilder @endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        ConformToSurface </td> <td> 
         
        0 </td> </tr> 

        </table>  

         <br>  Created in NX6.0.0.  <br>  
        */
        class NXOPENCPP_ANNOTATIONSEXPORT  RegionBuilder : public NXOpen::Builder
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
                        @link NXOpen::Annotations::RegionBuilder::TypesRectangularRegion NXOpen::Annotations::RegionBuilder::TypesRectangularRegion@endlink ,
                        @link NXOpen::Annotations::RegionBuilder::TypesCircularRegion NXOpen::Annotations::RegionBuilder::TypesCircularRegion@endlink ,
                        @link NXOpen::Annotations::RegionBuilder::TypesAnnularRegion NXOpen::Annotations::RegionBuilder::TypesAnnularRegion@endlink  
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Point * Origin
            (
            );
            /**Sets  the origin
                        Only available when region type is
                        @link NXOpen::Annotations::RegionBuilder::TypesRectangularRegion NXOpen::Annotations::RegionBuilder::TypesRectangularRegion@endlink ,
                        @link NXOpen::Annotations::RegionBuilder::TypesCircularRegion NXOpen::Annotations::RegionBuilder::TypesCircularRegion@endlink ,
                        @link NXOpen::Annotations::RegionBuilder::TypesAnnularRegion NXOpen::Annotations::RegionBuilder::TypesAnnularRegion@endlink  
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: void SetOrigin
            (
                NXOpen::Point * origin /** origin */ 
            );
            /**Returns  the anchor
                        Only available when region type is
                        @link NXOpen::Annotations::RegionBuilder::TypesRectangularRegion NXOpen::Annotations::RegionBuilder::TypesRectangularRegion@endlink ,
                        @link NXOpen::Annotations::RegionBuilder::TypesCircularRegion NXOpen::Annotations::RegionBuilder::TypesCircularRegion@endlink ,
                        @link NXOpen::Annotations::RegionBuilder::TypesAnnularRegion NXOpen::Annotations::RegionBuilder::TypesAnnularRegion@endlink  
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::RegionBuilder::AlignmentPosition Anchor
            (
            );
            /**Sets  the anchor
                        Only available when region type is
                        @link NXOpen::Annotations::RegionBuilder::TypesRectangularRegion NXOpen::Annotations::RegionBuilder::TypesRectangularRegion@endlink ,
                        @link NXOpen::Annotations::RegionBuilder::TypesCircularRegion NXOpen::Annotations::RegionBuilder::TypesCircularRegion@endlink ,
                        @link NXOpen::Annotations::RegionBuilder::TypesAnnularRegion NXOpen::Annotations::RegionBuilder::TypesAnnularRegion@endlink  
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: void SetAnchor
            (
                NXOpen::Annotations::RegionBuilder::AlignmentPosition anchor /** anchor */ 
            );
            /**Returns  the plane 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::PlaneBuilder * Plane
            (
            );
            /**Returns  the conform to surface toggle 
                        Only available when region type is
                        @link NXOpen::Annotations::RegionBuilder::TypesRectangularRegion NXOpen::Annotations::RegionBuilder::TypesRectangularRegion@endlink ,
                        @link NXOpen::Annotations::RegionBuilder::TypesCircularRegion NXOpen::Annotations::RegionBuilder::TypesCircularRegion@endlink ,
                        @link NXOpen::Annotations::RegionBuilder::TypesAnnularRegion NXOpen::Annotations::RegionBuilder::TypesAnnularRegion@endlink  
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: bool ConformToSurface
            (
            );
            /**Sets  the conform to surface toggle 
                        Only available when region type is
                        @link NXOpen::Annotations::RegionBuilder::TypesRectangularRegion NXOpen::Annotations::RegionBuilder::TypesRectangularRegion@endlink ,
                        @link NXOpen::Annotations::RegionBuilder::TypesCircularRegion NXOpen::Annotations::RegionBuilder::TypesCircularRegion@endlink ,
                        @link NXOpen::Annotations::RegionBuilder::TypesAnnularRegion NXOpen::Annotations::RegionBuilder::TypesAnnularRegion@endlink  
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: void SetConformToSurface
            (
                bool conformToSurfaceToggle /** conformtosurfacetoggle */ 
            );
            /**Returns  the select face 
                        Only available when region type is
                        @link NXOpen::Annotations::RegionBuilder::TypesRectangularRegion NXOpen::Annotations::RegionBuilder::TypesRectangularRegion@endlink ,
                        @link NXOpen::Annotations::RegionBuilder::TypesCircularRegion NXOpen::Annotations::RegionBuilder::TypesCircularRegion@endlink ,
                        @link NXOpen::Annotations::RegionBuilder::TypesAnnularRegion NXOpen::Annotations::RegionBuilder::TypesAnnularRegion@endlink  
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectDisplayableObjectList * SelectFace
            (
            );
            /**Returns  the select cylindrical face 
                        Only available when region type is
                        @link NXOpen::Annotations::RegionBuilder::TypesCylindricalRegion NXOpen::Annotations::RegionBuilder::TypesCylindricalRegion@endlink  
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectDisplayableObjectList * SelectCylindricalFace
            (
            );
            /**Returns  the outer diameter
                        Only available when region type is
                        @link NXOpen::Annotations::RegionBuilder::TypesCircularRegion NXOpen::Annotations::RegionBuilder::TypesCircularRegion@endlink ,
                        @link NXOpen::Annotations::RegionBuilder::TypesAnnularRegion NXOpen::Annotations::RegionBuilder::TypesAnnularRegion@endlink  
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * OuterDiameter
            (
            );
            /**Returns  the inner diameter
                        Only available when region type is
                        @link NXOpen::Annotations::RegionBuilder::TypesAnnularRegion NXOpen::Annotations::RegionBuilder::TypesAnnularRegion@endlink  
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * InnerDiameter
            (
            );
            /**Returns  the width
                        Only available when region type is
                        @link NXOpen::Annotations::RegionBuilder::TypesRectangularRegion NXOpen::Annotations::RegionBuilder::TypesRectangularRegion@endlink  
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * Width
            (
            );
            /**Returns  the height
                        Only available when region type is
                        @link NXOpen::Annotations::RegionBuilder::TypesRectangularRegion NXOpen::Annotations::RegionBuilder::TypesRectangularRegion@endlink  
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * Height
            (
            );
            /**Returns  the start point
                        Only available when the region type is
                        @link NXOpen::Annotations::RegionBuilder::TypesCylindricalRegion NXOpen::Annotations::RegionBuilder::TypesCylindricalRegion@endlink  
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Point * StartPoint
            (
            );
            /**Sets  the start point
                        Only available when the region type is
                        @link NXOpen::Annotations::RegionBuilder::TypesCylindricalRegion NXOpen::Annotations::RegionBuilder::TypesCylindricalRegion@endlink  
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: void SetStartPoint
            (
                NXOpen::Point * startPoint /** startpoint */ 
            );
            /**Returns  the end point
                        Only available when the region type is
                        @link NXOpen::Annotations::RegionBuilder::TypesCylindricalRegion NXOpen::Annotations::RegionBuilder::TypesCylindricalRegion@endlink  
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Point * EndPoint
            (
            );
            /**Sets  the end point
                        Only available when the region type is
                        @link NXOpen::Annotations::RegionBuilder::TypesCylindricalRegion NXOpen::Annotations::RegionBuilder::TypesCylindricalRegion@endlink  
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: void SetEndPoint
            (
                NXOpen::Point * endPoint /** endpoint */ 
            );
            /**Returns  the arbitrary area list
                        Only available when the region type is
                        @link NXOpen::Annotations::RegionBuilder::TypesArbitraryRegion NXOpen::Annotations::RegionBuilder::TypesArbitraryRegion@endlink  
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::ArbitraryAreaSeedBuilderList * ArbitraryAreaList
            (
            );
            /**Returns  the crosshatch distance. Use @link NXOpen::Annotations::RegionBuilder::CrosshatchSettings NXOpen::Annotations::RegionBuilder::CrosshatchSettings@endlink  instead. 
             <br>  @deprecated Deprecated in NX8.5.0.  Use @link NXOpen::Annotations::RegionBuilder::CrosshatchSettings NXOpen::Annotations::RegionBuilder::CrosshatchSettings@endlink  instead. <br>  

             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX8.5.0.  Use NXOpen::Annotations::RegionBuilder::CrosshatchSettings instead.") NXOpen::Expression * CrosshatchDistance
            (
            );
            /**Returns  the crosshatch angle. Use @link NXOpen::Annotations::RegionBuilder::CrosshatchSettings NXOpen::Annotations::RegionBuilder::CrosshatchSettings@endlink  instead. 
             <br>  @deprecated Deprecated in NX8.5.0.  Use @link NXOpen::Annotations::RegionBuilder::CrosshatchSettings NXOpen::Annotations::RegionBuilder::CrosshatchSettings@endlink  instead. <br>  

             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX8.5.0.  Use NXOpen::Annotations::RegionBuilder::CrosshatchSettings instead.") NXOpen::Expression * CrosshatchAngle
            (
            );
            /**Returns  the crosshatch pattern enum. Use @link NXOpen::Annotations::RegionBuilder::CrosshatchSettings NXOpen::Annotations::RegionBuilder::CrosshatchSettings@endlink  instead. 
             <br>  @deprecated Deprecated in NX8.5.0.  Use @link NXOpen::Annotations::RegionBuilder::CrosshatchSettings NXOpen::Annotations::RegionBuilder::CrosshatchSettings@endlink  instead. <br>  

             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX8.5.0.  Use NXOpen::Annotations::RegionBuilder::CrosshatchSettings instead.") NXOpen::Annotations::RegionBuilder::CrosshatchPatterns CrosshatchPattern
            (
            );
            /**Sets  the crosshatch pattern enum. Use @link NXOpen::Annotations::RegionBuilder::CrosshatchSettings NXOpen::Annotations::RegionBuilder::CrosshatchSettings@endlink  instead. 
             <br>  @deprecated Deprecated in NX8.5.0.  Use the sublock of  @link NXOpen::Annotations::RegionBuilder::CrosshatchSettings NXOpen::Annotations::RegionBuilder::CrosshatchSettings@endlink  called Pattern instead. <br>  

             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public:  NX_DEPRECATED("Deprecated in NX8.5.0.  Use the sublock of  NXOpen::Annotations::RegionBuilder::CrosshatchSettings called Pattern instead.") void SetCrosshatchPattern
            (
                NXOpen::Annotations::RegionBuilder::CrosshatchPatterns crosshatchPattern /** crosshatchpattern */ 
            );
            /**Returns  the crosshatch color 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::NXColor * CrosshatchColor
            (
            );
            /**Sets  the crosshatch color 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: void SetCrosshatchColor
            (
                NXOpen::NXColor * crosshatchColor /** crosshatchcolor */ 
            );
            /**Returns  the type 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::RegionBuilder::Types Type
            (
            );
            /**Sets  the type 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: void SetType
            (
                NXOpen::Annotations::RegionBuilder::Types type /** type */ 
            );
            /**Returns  the display crosshatch toggle 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: bool DisplayCrosshatch
            (
            );
            /**Sets  the display crosshatch toggle 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: void SetDisplayCrosshatch
            (
                bool displayCrosshatch /** displaycrosshatch */ 
            );
            /**Returns  the crosshatch settings block 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::HatchFillSettingsBuilder * CrosshatchSettings
            (
            );
            /**Returns  the boundary curve settings block 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::LineColorFontWidthBuilder * BoundaryColorFontWidth
            (
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
