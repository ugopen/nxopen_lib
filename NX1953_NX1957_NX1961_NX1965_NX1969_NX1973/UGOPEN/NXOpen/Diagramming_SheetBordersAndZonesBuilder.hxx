#ifndef NXOpen_DIAGRAMMING_SHEETBORDERSANDZONESBUILDER_HXX_INCLUDED
#define NXOpen_DIAGRAMMING_SHEETBORDERSANDZONESBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Diagramming_SheetBordersAndZonesBuilder.ja
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
#include <NXOpen/Diagramming_Sheet.hxx>
#include <NXOpen/Diagramming_SheetBorderSettingsBuilder.hxx>
#include <NXOpen/Diagramming_SheetMarginSettingsBuilder.hxx>
#include <NXOpen/Diagramming_SheetZoneSettingsBuilder.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/libnxopencpp_diagramming_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Diagramming
    {
        class SheetBordersAndZonesBuilder;
    }
    class Builder;
    namespace Diagramming
    {
        class Sheet;
    }
    namespace Diagramming
    {
        class SheetBorderSettingsBuilder;
    }
    namespace Diagramming
    {
        class SheetMarginSettingsBuilder;
    }
    namespace Diagramming
    {
        class SheetZoneSettingsBuilder;
    }
    namespace Diagramming
    {
        class _SheetBordersAndZonesBuilderBuilder;
        class SheetBordersAndZonesBuilderImpl;
        /** The SheetBordersAndZones builder  <br> To create a new instance of this class, use @link NXOpen::Diagramming::SheetBordersAndZonesCollection::CreateSheetBordersAndZonesBuilder  NXOpen::Diagramming::SheetBordersAndZonesCollection::CreateSheetBordersAndZonesBuilder @endlink  <br> 
         <br>  Created in NX10.0.0.  <br>  
        */
        class NXOPENCPP_DIAGRAMMINGEXPORT  SheetBordersAndZonesBuilder : public NXOpen::Builder
        {
            /** Represents the horizontal centering mark type. */
            public: enum HorizontalCenteringMarkType
            {
                HorizontalCenteringMarkTypeNone/** None */,
                HorizontalCenteringMarkTypeLeftArrow/** Left Arrow */,
                HorizontalCenteringMarkTypeRightArrow/**  Right Arrow */,
                HorizontalCenteringMarkTypeLeftandRightArrow/** Left and Right Arrow */,
                HorizontalCenteringMarkTypeLeftandRightLine/** leftand right line */ 
            };

            /** Represents the vertical centering mark type. */
            public: enum VerticalCenteringMarkType
            {
                VerticalCenteringMarkTypeNone/** None */,
                VerticalCenteringMarkTypeBottomArrow/** Bottom Arrow */,
                VerticalCenteringMarkTypeTopArrow/** Top Arrow */,
                VerticalCenteringMarkTypeBottomandTopArrow/** Bottom and Top Arrow */,
                VerticalCenteringMarkTypeBottomandTopLine/** bottomand top line */ 
            };

            /** Represents the zone method. */
            public: enum ZoneMethod
            {
                ZoneMethodNone/** None */,
                ZoneMethodStandard/** Standard */,
                ZoneMethodCustom/** custom */ 
            };

            /** Represents the zone origin. */
            public: enum ZoneOrigin
            {
                ZoneOriginBottomRight/** Bottom Right */,
                ZoneOriginTopLeft/** Top Left */,
                ZoneOriginTopRight/** Top Right */,
                ZoneOriginBottomLeft/** bottom left */ 
            };

            /** Represents the arrow style type */
            public: enum ArrowStyleType
            {
                ArrowStyleTypeFilled/** Filled */,
                ArrowStyleTypeClosed/** Closed */,
                ArrowStyleTypeClosedSolid/** Close Solid */,
                ArrowStyleTypeOpen/** open */ 
            };

            /** Represents the arrow direction type */
            public: enum ArrowDirectionType
            {
                ArrowDirectionTypeOutofSheet/** Out of Sheet */,
                ArrowDirectionTypeIntoSheet/** into sheet */ 
            };

            /** Represents the trimming mark style type */
            public: enum TrimmingMarkStyleType
            {
                TrimmingMarkStyleTypeTriangle/** Triangle */,
                TrimmingMarkStyleTypeCorner/** corner */ 
            };

            private: SheetBordersAndZonesBuilderImpl * m_sheetbordersandzonesbuilder_impl;
            private: friend class  _SheetBordersAndZonesBuilderBuilder;
            protected: SheetBordersAndZonesBuilder();
            public: ~SheetBordersAndZonesBuilder();
            /**Returns  the flag that indicates if borders are created. 
             <br>  @deprecated Deprecated in NX12.0.1.  Use <ja_property_get >NXOpen.Diagramming.SheetBorderSettingsBuilder.CreateBorders</ja_property_get > instead. <br>  

             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX12.0.1.  Use <ja_property_get >NXOpen.Diagramming.SheetBorderSettingsBuilder.CreateBorders</ja_property_get > instead.") bool CreateBorders
            (
            );
            /**Sets  the flag that indicates if borders are created. 
             <br>  @deprecated Deprecated in NX12.0.1.  Use <ja_property_set >NXOpen.Diagramming.SheetBorderSettingsBuilder.CreateBorders</ja_property_set > instead. <br>  

             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX12.0.1.  Use <ja_property_set >NXOpen.Diagramming.SheetBorderSettingsBuilder.CreateBorders</ja_property_set > instead.") void SetCreateBorders
            (
                bool createBorders /** createborders */ 
            );
            /**Returns  the width of border. It should be greater than zero. 
             <br>  @deprecated Deprecated in NX12.0.1.  Use <ja_property_get >NXOpen.Diagramming.SheetBorderSettingsBuilder.BorderLineWidth</ja_property_get > instead. <br>  

             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX12.0.1.  Use <ja_property_get >NXOpen.Diagramming.SheetBorderSettingsBuilder.BorderLineWidth</ja_property_get > instead.") double Width
            (
            );
            /**Sets  the width of border. It should be greater than zero. 
             <br>  @deprecated Deprecated in NX12.0.1.  Use <ja_property_set >NXOpen.Diagramming.SheetBorderSettingsBuilder.BorderLineWidth</ja_property_set > instead. <br>  

             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX12.0.1.  Use <ja_property_set >NXOpen.Diagramming.SheetBorderSettingsBuilder.BorderLineWidth</ja_property_set > instead.") void SetWidth
            (
                double width /** width */ 
            );
            /**Returns  the horizontal centering mark used to show the type of centering mark like LeftArrow/RightArrow. 
             <br>  @deprecated Deprecated in NX12.0.1.  Use <ja_property_get >NXOpen.Diagramming.SheetBorderSettingsBuilder.CenteringMarksHorizontal</ja_property_get > instead. <br>  

             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX12.0.1.  Use <ja_property_get >NXOpen.Diagramming.SheetBorderSettingsBuilder.CenteringMarksHorizontal</ja_property_get > instead.") NXOpen::Diagramming::SheetBordersAndZonesBuilder::HorizontalCenteringMarkType HorizontalCenteringMark
            (
            );
            /**Sets  the horizontal centering mark used to show the type of centering mark like LeftArrow/RightArrow. 
             <br>  @deprecated Deprecated in NX12.0.1.  Use <ja_property_set >NXOpen.Diagramming.SheetBorderSettingsBuilder.CenteringMarksHorizontal</ja_property_set > instead. <br>  

             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX12.0.1.  Use <ja_property_set >NXOpen.Diagramming.SheetBorderSettingsBuilder.CenteringMarksHorizontal</ja_property_set > instead.") void SetHorizontalCenteringMark
            (
                NXOpen::Diagramming::SheetBordersAndZonesBuilder::HorizontalCenteringMarkType horizontalCenteringMarkType /** horizontalcenteringmarktype */ 
            );
            /**Returns  the vertical centering mark  used to show the type of centering mark like TopArrow/BottomArrow. 
             <br>  @deprecated Deprecated in NX12.0.1.  Use <ja_property_get >NXOpen.Diagramming.SheetBorderSettingsBuilder.CenteringMarksVertical</ja_property_get > instead. <br>  

             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX12.0.1.  Use <ja_property_get >NXOpen.Diagramming.SheetBorderSettingsBuilder.CenteringMarksVertical</ja_property_get > instead.") NXOpen::Diagramming::SheetBordersAndZonesBuilder::VerticalCenteringMarkType VerticalCenteringMark
            (
            );
            /**Sets  the vertical centering mark  used to show the type of centering mark like TopArrow/BottomArrow. 
             <br>  @deprecated Deprecated in NX12.0.1.  Use <ja_property_set >NXOpen.Diagramming.SheetBorderSettingsBuilder.CenteringMarksVertical</ja_property_set > instead. <br>  

             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX12.0.1.  Use <ja_property_set >NXOpen.Diagramming.SheetBorderSettingsBuilder.CenteringMarksVertical</ja_property_set > instead.") void SetVerticalCenteringMark
            (
                NXOpen::Diagramming::SheetBordersAndZonesBuilder::VerticalCenteringMarkType verticalCenteringMark /** verticalcenteringmark */ 
            );
            /**Returns  the length of centering marks extension from inner border 
             <br>  @deprecated Deprecated in NX12.0.1.  Use <ja_property_get >NXOpen.Diagramming.SheetBorderSettingsBuilder.CenteringMarksExtension</ja_property_get > instead. <br>  

             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX12.0.1.  Use <ja_property_get >NXOpen.Diagramming.SheetBorderSettingsBuilder.CenteringMarksExtension</ja_property_get > instead.") double CenteringMarkExtension
            (
            );
            /**Sets  the length of centering marks extension from inner border 
             <br>  @deprecated Deprecated in NX12.0.1.  Use <ja_property_set >NXOpen.Diagramming.SheetBorderSettingsBuilder.CenteringMarksExtension</ja_property_set > instead. <br>  

             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX12.0.1.  Use <ja_property_set >NXOpen.Diagramming.SheetBorderSettingsBuilder.CenteringMarksExtension</ja_property_set > instead.") void SetCenteringMarkExtension
            (
                double centeringMarkExtension /** centeringmarkextension */ 
            );
            /**Returns  the flag that indicate if trimming marks are created. 
             <br>  @deprecated Deprecated in NX12.0.1.  Use <ja_property_get >NXOpen.Diagramming.SheetBorderSettingsBuilder.CreateTrimmingMarks</ja_property_get > instead. <br>  

             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX12.0.1.  Use <ja_property_get >NXOpen.Diagramming.SheetBorderSettingsBuilder.CreateTrimmingMarks</ja_property_get > instead.") bool CreateTrimmingMarks
            (
            );
            /**Sets  the flag that indicate if trimming marks are created. 
             <br>  @deprecated Deprecated in NX12.0.1.  Use <ja_property_set >NXOpen.Diagramming.SheetBorderSettingsBuilder.CreateTrimmingMarks</ja_property_set > instead. <br>  

             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX12.0.1.  Use <ja_property_set >NXOpen.Diagramming.SheetBorderSettingsBuilder.CreateTrimmingMarks</ja_property_set > instead.") void SetCreateTrimmingMarks
            (
                bool createTrimmingMarks /** createtrimmingmarks */ 
            );
            /**Returns  the length of trimming mark. It should be greater than zero. 
             <br>  @deprecated Deprecated in NX12.0.1.  Use <ja_property_get >NXOpen.Diagramming.SheetBorderSettingsBuilder.TrimmingMarkLength</ja_property_get > instead. <br>  

             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX12.0.1.  Use <ja_property_get >NXOpen.Diagramming.SheetBorderSettingsBuilder.TrimmingMarkLength</ja_property_get > instead.") double TrimmingMarkLength
            (
            );
            /**Sets  the length of trimming mark. It should be greater than zero. 
             <br>  @deprecated Deprecated in NX12.0.1.  Use <ja_property_set >NXOpen.Diagramming.SheetBorderSettingsBuilder.TrimmingMarkLength</ja_property_set > instead. <br>  

             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX12.0.1.  Use <ja_property_set >NXOpen.Diagramming.SheetBorderSettingsBuilder.TrimmingMarkLength</ja_property_set > instead.") void SetTrimmingMarkLength
            (
                double trimmingMarkLength /** trimmingmarklength */ 
            );
            /**Returns  the width of trimming mark. It should be greater than zero. 
             <br>  @deprecated Deprecated in NX12.0.1.  Use <ja_property_get >NXOpen.Diagramming.SheetBorderSettingsBuilder.TrimmingMarkWidth</ja_property_get > instead. <br>  

             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX12.0.1.  Use <ja_property_get >NXOpen.Diagramming.SheetBorderSettingsBuilder.TrimmingMarkWidth</ja_property_get > instead.") double TrimmingMarkThickness
            (
            );
            /**Sets  the width of trimming mark. It should be greater than zero. 
             <br>  @deprecated Deprecated in NX12.0.1.  Use <ja_property_set >NXOpen.Diagramming.SheetBorderSettingsBuilder.TrimmingMarkWidth</ja_property_set > instead. <br>  

             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX12.0.1.  Use <ja_property_set >NXOpen.Diagramming.SheetBorderSettingsBuilder.TrimmingMarkWidth</ja_property_set > instead.") void SetTrimmingMarkThickness
            (
                double trimmingMarkThickness /** trimmingmarkthickness */ 
            );
            /**Returns  the type of methods to create the zones. 
             <br>  @deprecated Deprecated in NX12.0.1.  Use <ja_property_get >NXOpen.Diagramming.SheetBorderSettingsBuilder.Method</ja_property_get > instead. <br>  

             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX12.0.1.  Use <ja_property_get >NXOpen.Diagramming.SheetBorderSettingsBuilder.Method</ja_property_get > instead.") NXOpen::Diagramming::SheetBordersAndZonesBuilder::ZoneMethod Method
            (
            );
            /**Sets  the type of methods to create the zones. 
             <br>  @deprecated Deprecated in NX12.0.1.  Use <ja_property_set >NXOpen.Diagramming.SheetBorderSettingsBuilder.Method</ja_property_set > instead. <br>  

             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX12.0.1.  Use <ja_property_set >NXOpen.Diagramming.SheetBorderSettingsBuilder.Method</ja_property_set > instead.") void SetMethod
            (
                NXOpen::Diagramming::SheetBordersAndZonesBuilder::ZoneMethod method /** method */ 
            );
            /**Returns  the size of horizontal zones. It should be greater than zero. 
             <br>  @deprecated Deprecated in NX12.0.1.  Use <ja_property_get >NXOpen.Diagramming.SheetZoneSettingsBuilder.HorizontalSize</ja_property_get > instead. <br>  

             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX12.0.1.  Use <ja_property_get >NXOpen.Diagramming.SheetZoneSettingsBuilder.HorizontalSize</ja_property_get > instead.") double HorizontalSize
            (
            );
            /**Sets  the size of horizontal zones. It should be greater than zero. 
             <br>  @deprecated Deprecated in NX12.0.1.  Use <ja_property_set >NXOpen.Diagramming.SheetZoneSettingsBuilder.HorizontalSize</ja_property_set > instead. <br>  

             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX12.0.1.  Use <ja_property_set >NXOpen.Diagramming.SheetZoneSettingsBuilder.HorizontalSize</ja_property_set > instead.") void SetHorizontalSize
            (
                double horizontalSize /** horizontalsize */ 
            );
            /**Returns  the size of vertical zones. It should be greater than zero. 
             <br>  @deprecated Deprecated in NX12.0.1.  Use <ja_property_get >NXOpen.Diagramming.SheetZoneSettingsBuilder.VerticalSize</ja_property_get > instead. <br>  

             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX12.0.1.  Use <ja_property_get >NXOpen.Diagramming.SheetZoneSettingsBuilder.VerticalSize</ja_property_get > instead.") double VerticalSize
            (
            );
            /**Sets  the size of vertical zones. It should be greater than zero. 
             <br>  @deprecated Deprecated in NX12.0.1.  Use <ja_property_set >NXOpen.Diagramming.SheetZoneSettingsBuilder.VerticalSize</ja_property_set > instead. <br>  

             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX12.0.1.  Use <ja_property_set >NXOpen.Diagramming.SheetZoneSettingsBuilder.VerticalSize</ja_property_set > instead.") void SetVerticalSize
            (
                double verticalSize /** verticalsize */ 
            );
            /**Returns  the type of zone origin like TopLeft/BottomRight. 
             <br>  @deprecated Deprecated in NX12.0.1.  Use <ja_property_get >NXOpen.Diagramming.SheetZoneSettingsBuilder.Origin</ja_property_get > instead. <br>  

             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX12.0.1.  Use <ja_property_get >NXOpen.Diagramming.SheetZoneSettingsBuilder.Origin</ja_property_get > instead.") NXOpen::Diagramming::SheetBordersAndZonesBuilder::ZoneOrigin Origin
            (
            );
            /**Sets  the type of zone origin like TopLeft/BottomRight. 
             <br>  @deprecated Deprecated in NX12.0.1.  Use <ja_property_set >NXOpen.Diagramming.SheetZoneSettingsBuilder.Origin</ja_property_set > instead. <br>  

             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX12.0.1.  Use <ja_property_set >NXOpen.Diagramming.SheetZoneSettingsBuilder.Origin</ja_property_set > instead.") void SetOrigin
            (
                NXOpen::Diagramming::SheetBordersAndZonesBuilder::ZoneOrigin origin /** origin */ 
            );
            /**Returns  the flag that indicates if zone marking is create. 
             <br>  @deprecated Deprecated in NX12.0.1.  Use <ja_property_get >NXOpen.Diagramming.SheetZoneSettingsBuilder.CreateZoneMarkings</ja_property_get > instead. <br>  

             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX12.0.1.  Use <ja_property_get >NXOpen.Diagramming.SheetZoneSettingsBuilder.CreateZoneMarkings</ja_property_get > instead.") bool CreateZoneMarking
            (
            );
            /**Sets  the flag that indicates if zone marking is create. 
             <br>  @deprecated Deprecated in NX12.0.1.  Use <ja_property_set >NXOpen.Diagramming.SheetZoneSettingsBuilder.CreateZoneMarkings</ja_property_set > instead. <br>  

             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX12.0.1.  Use <ja_property_set >NXOpen.Diagramming.SheetZoneSettingsBuilder.CreateZoneMarkings</ja_property_set > instead.") void SetCreateZoneMarking
            (
                bool createZoneMarking /** createzonemarking */ 
            );
            /**Returns  the height of marking. It should be greater than zero. 
             <br>  @deprecated Deprecated in NX12.0.1.  Use <ja_property_get >NXOpen.Diagramming.SheetZoneSettingsBuilder.MarkingHeight</ja_property_get > instead. <br>  

             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX12.0.1.  Use <ja_property_get >NXOpen.Diagramming.SheetZoneSettingsBuilder.MarkingHeight</ja_property_get > instead.") double MarkingHeight
            (
            );
            /**Sets  the height of marking. It should be greater than zero. 
             <br>  @deprecated Deprecated in NX12.0.1.  Use <ja_property_set >NXOpen.Diagramming.SheetZoneSettingsBuilder.MarkingHeight</ja_property_set > instead. <br>  

             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX12.0.1.  Use <ja_property_set >NXOpen.Diagramming.SheetZoneSettingsBuilder.MarkingHeight</ja_property_set > instead.") void SetMarkingHeight
            (
                double markingHeight /** markingheight */ 
            );
            /**Returns  the flag that indicates if zone labels are created. 
             <br>  @deprecated Deprecated in NX12.0.1.  Use <ja_property_get >NXOpen.Diagramming.SheetZoneSettingsBuilder.CreateZoneLabels</ja_property_get > instead. <br>  

             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX12.0.1.  Use <ja_property_get >NXOpen.Diagramming.SheetZoneSettingsBuilder.CreateZoneLabels</ja_property_get > instead.") bool CreateZoneLabels
            (
            );
            /**Sets  the flag that indicates if zone labels are created. 
             <br>  @deprecated Deprecated in NX12.0.1.  Use <ja_property_set >NXOpen.Diagramming.SheetZoneSettingsBuilder.CreateZoneLabels</ja_property_set > instead. <br>  

             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX12.0.1.  Use <ja_property_set >NXOpen.Diagramming.SheetZoneSettingsBuilder.CreateZoneLabels</ja_property_set > instead.") void SetCreateZoneLabels
            (
                bool createZoneLabels /** createzonelabels */ 
            );
            /**Returns  the height of the label(text). It should be greater than zero. 
             <br>  @deprecated Deprecated in NX12.0.1.  Use <ja_property_get >NXOpen.Diagramming.SheetZoneSettingsBuilder.LabelHeight</ja_property_get > instead. <br>  

             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX12.0.1.  Use <ja_property_get >NXOpen.Diagramming.SheetZoneSettingsBuilder.LabelHeight</ja_property_get > instead.") double LabelHeight
            (
            );
            /**Sets  the height of the label(text). It should be greater than zero. 
             <br>  @deprecated Deprecated in NX12.0.1.  Use <ja_property_set >NXOpen.Diagramming.SheetZoneSettingsBuilder.LabelHeight</ja_property_set > instead. <br>  

             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX12.0.1.  Use <ja_property_set >NXOpen.Diagramming.SheetZoneSettingsBuilder.LabelHeight</ja_property_set > instead.") void SetLabelHeight
            (
                double labelHeight /** labelheight */ 
            );
            /**Returns  the font of the label(text). 
             <br>  @deprecated Deprecated in NX12.0.1.  Use <ja_property_get >NXOpen.Diagramming.SheetZoneSettingsBuilder.LabelFont</ja_property_get > instead. <br>  

             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX12.0.1.  Use <ja_property_get >NXOpen.Diagramming.SheetZoneSettingsBuilder.LabelFont</ja_property_get > instead.") int LabelFont
            (
            );
            /**Sets  the font of the label(text). 
             <br>  @deprecated Deprecated in NX12.0.1.  Use <ja_property_set >NXOpen.Diagramming.SheetZoneSettingsBuilder.LabelFont</ja_property_set > instead. <br>  

             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX12.0.1.  Use <ja_property_set >NXOpen.Diagramming.SheetZoneSettingsBuilder.LabelFont</ja_property_set > instead.") void SetLabelFont
            (
                int labelFont /** labelfont */ 
            );
            /**Returns  the value of the margin in top border.
             <br>  @deprecated Deprecated in NX12.0.1.  Use <ja_property_get >NXOpen.Diagramming.SheetMarginSettingsBuilder.TopTrimmedMargin</ja_property_get > instead. <br>  

             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX12.0.1.  Use <ja_property_get >NXOpen.Diagramming.SheetMarginSettingsBuilder.TopTrimmedMargin</ja_property_get > instead.") double TopMargin
            (
            );
            /**Sets  the value of the margin in top border.
             <br>  @deprecated Deprecated in NX12.0.1.  Use <ja_property_set >NXOpen.Diagramming.SheetMarginSettingsBuilder.TopTrimmedMargin</ja_property_set > instead. <br>  

             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX12.0.1.  Use <ja_property_set >NXOpen.Diagramming.SheetMarginSettingsBuilder.TopTrimmedMargin</ja_property_set > instead.") void SetTopMargin
            (
                double topMargin /** topmargin */ 
            );
            /**Returns  the value of the margin in bottom border.
             <br>  @deprecated Deprecated in NX12.0.1.  Use <ja_property_get >NXOpen.Diagramming.SheetMarginSettingsBuilder.BottomTrimmedMargin</ja_property_get > instead. <br>  

             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX12.0.1.  Use <ja_property_get >NXOpen.Diagramming.SheetMarginSettingsBuilder.BottomTrimmedMargin</ja_property_get > instead.") double BottomMargin
            (
            );
            /**Sets  the value of the margin in bottom border.
             <br>  @deprecated Deprecated in NX12.0.1.  Use <ja_property_set >NXOpen.Diagramming.SheetMarginSettingsBuilder.BottomTrimmedMargin</ja_property_set > instead. <br>  

             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX12.0.1.  Use <ja_property_set >NXOpen.Diagramming.SheetMarginSettingsBuilder.BottomTrimmedMargin</ja_property_set > instead.") void SetBottomMargin
            (
                double bottomMargin /** bottommargin */ 
            );
            /**Returns  the value of the margin in left border.
             <br>  @deprecated Deprecated in NX12.0.1.  Use <ja_property_get >NXOpen.Diagramming.SheetMarginSettingsBuilder.LeftTrimmedMargin</ja_property_get > instead. <br>  

             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX12.0.1.  Use <ja_property_get >NXOpen.Diagramming.SheetMarginSettingsBuilder.LeftTrimmedMargin</ja_property_get > instead.") double LeftMargin
            (
            );
            /**Sets  the value of the margin in left border.
             <br>  @deprecated Deprecated in NX12.0.1.  Use <ja_property_set >NXOpen.Diagramming.SheetMarginSettingsBuilder.LeftTrimmedMargin</ja_property_set > instead. <br>  

             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX12.0.1.  Use <ja_property_set >NXOpen.Diagramming.SheetMarginSettingsBuilder.LeftTrimmedMargin</ja_property_set > instead.") void SetLeftMargin
            (
                double leftMargin /** leftmargin */ 
            );
            /**Returns  the value of the margin in right border.
             <br>  @deprecated Deprecated in NX12.0.1.  Use <ja_property_get >NXOpen.Diagramming.SheetMarginSettingsBuilder.RightTrimmedMargin</ja_property_get > instead. <br>  

             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX12.0.1.  Use <ja_property_get >NXOpen.Diagramming.SheetMarginSettingsBuilder.RightTrimmedMargin</ja_property_get > instead.") double RightMargin
            (
            );
            /**Sets  the value of the margin in right border.
             <br>  @deprecated Deprecated in NX12.0.1.  Use <ja_property_set >NXOpen.Diagramming.SheetMarginSettingsBuilder.RightTrimmedMargin</ja_property_set > instead. <br>  

             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX12.0.1.  Use <ja_property_set >NXOpen.Diagramming.SheetMarginSettingsBuilder.RightTrimmedMargin</ja_property_set > instead.") void SetRightMargin
            (
                double rightMargin /** rightmargin */ 
            );
            /** Set the owning sheet when the sheet element is created.
                    It is not allowed to change the owning sheet when editing the borders and zones. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void SetOwningSheet
            (
                NXOpen::Diagramming::Sheet * owningSheet /** owningsheet */ 
            );
            /**Returns  the sheet border settings builder used to get the values related to borders
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : None */
            public: NXOpen::Diagramming::SheetBorderSettingsBuilder * SheetBorderSettings
            (
            );
            /**Returns  the sheet margin settings builder used to get the values related to margins
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : None */
            public: NXOpen::Diagramming::SheetMarginSettingsBuilder * SheetMarginSettings
            (
            );
            /**Returns  the sheet zone settings builder used to get the values related to zones
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : None */
            public: NXOpen::Diagramming::SheetZoneSettingsBuilder * SheetZoneSettings
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