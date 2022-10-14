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
#include <NXOpen/Diagramming_SheetBordersAndZonesBuilder.hxx>
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
        class _SheetBordersAndZonesBuilderBuilder;
        class SheetBordersAndZonesBuilderImpl;

        /// \cond NX_NO_DOC 
        /** Represents Sheet Borders and Zones builder. It creates and redefines borders and zones.  <br> To create a new instance of this class, use @link NXOpen::Diagramming::SheetBordersAndZonesCollection::CreateSheetBordersAndZonesBuilder  NXOpen::Diagramming::SheetBordersAndZonesCollection::CreateSheetBordersAndZonesBuilder @endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        BottomMargin </td> <td> 
         
        0 (millimeters part), 0 (inches part) </td> </tr> 

        <tr><td> 
         
        CenteringMarkExtension </td> <td> 
         
        5 (millimeters part), 0.25 (inches part) </td> </tr> 

        <tr><td> 
         
        CreateBorders </td> <td> 
         
        1 </td> </tr> 

        <tr><td> 
         
        CreateTrimmingMarks </td> <td> 
         
        1 </td> </tr> 

        <tr><td> 
         
        CreateZoneLabels </td> <td> 
         
        1 </td> </tr> 

        <tr><td> 
         
        CreateZoneMarking </td> <td> 
         
        1 </td> </tr> 

        <tr><td> 
         
        HorizontalCenteringMark </td> <td> 
         
        None </td> </tr> 

        <tr><td> 
         
        HorizontalSize </td> <td> 
         
        50 (millimeters part), 2.5 (inches part) </td> </tr> 

        <tr><td> 
         
        LabelFont </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        LabelHeight </td> <td> 
         
        3.5 (millimeters part), 0.125 (inches part) </td> </tr> 

        <tr><td> 
         
        LeftMargin </td> <td> 
         
        0 (millimeters part), 0 (inches part) </td> </tr> 

        <tr><td> 
         
        MarkingHeight </td> <td> 
         
        10 (millimeters part), 0.375 (inches part) </td> </tr> 

        <tr><td> 
         
        Method </td> <td> 
         
        Standard </td> </tr> 

        <tr><td> 
         
        Origin </td> <td> 
         
        TopLeft </td> </tr> 

        <tr><td> 
         
        RightMargin </td> <td> 
         
        0 (millimeters part), 0 (inches part) </td> </tr> 

        <tr><td> 
         
        TopMargin </td> <td> 
         
        0 (millimeters part), 0 (inches part) </td> </tr> 

        <tr><td> 
         
        TrimmingMarkLength </td> <td> 
         
        10 (millimeters part), 0.5 (inches part) </td> </tr> 

        <tr><td> 
         
        TrimmingMarkThickness </td> <td> 
         
        5 (millimeters part), 0.25 (inches part) </td> </tr> 

        <tr><td> 
         
        VerticalCenteringMark </td> <td> 
         
        None </td> </tr> 

        <tr><td> 
         
        VerticalSize </td> <td> 
         
        50 (millimeters part), 2.5 (inches part) </td> </tr> 

        <tr><td> 
         
        Width </td> <td> 
         
        10 (millimeters part), 0.375 (inches part) </td> </tr> 

        </table>  

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

            private: SheetBordersAndZonesBuilderImpl * m_sheetbordersandzonesbuilder_impl;
            private: friend class  _SheetBordersAndZonesBuilderBuilder;
            protected: SheetBordersAndZonesBuilder();
            public: ~SheetBordersAndZonesBuilder();
            /**Returns  the flag that indicates if borders are created. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: bool CreateBorders
            (
            );
            /**Sets  the flag that indicates if borders are created. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void SetCreateBorders
            (
                bool createBorders /** createborders */ 
            );
            /**Returns  the width of border. It should be non-negative. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: double Width
            (
            );
            /**Sets  the width of border. It should be non-negative. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void SetWidth
            (
                double width /** width */ 
            );
            /**Returns  the horizontal centering mark type. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Diagramming::SheetBordersAndZonesBuilder::HorizontalCenteringMarkType HorizontalCenteringMark
            (
            );
            /**Sets  the horizontal centering mark type. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void SetHorizontalCenteringMark
            (
                NXOpen::Diagramming::SheetBordersAndZonesBuilder::HorizontalCenteringMarkType horizontalCenteringMarkType /** horizontalcenteringmarktype */ 
            );
            /**Returns  the vertical centering mark type. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Diagramming::SheetBordersAndZonesBuilder::VerticalCenteringMarkType VerticalCenteringMark
            (
            );
            /**Sets  the vertical centering mark type. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void SetVerticalCenteringMark
            (
                NXOpen::Diagramming::SheetBordersAndZonesBuilder::VerticalCenteringMarkType verticalCenteringMark /** verticalcenteringmark */ 
            );
            /**Returns  the centering mark extension. It should be non-negative. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: double CenteringMarkExtension
            (
            );
            /**Sets  the centering mark extension. It should be non-negative. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void SetCenteringMarkExtension
            (
                double centeringMarkExtension /** centeringmarkextension */ 
            );
            /**Returns  the flag that indicate if trimming marks are created. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: bool CreateTrimmingMarks
            (
            );
            /**Sets  the flag that indicate if trimming marks are created. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void SetCreateTrimmingMarks
            (
                bool createTrimmingMarks /** createtrimmingmarks */ 
            );
            /**Returns  the trimming mark length. It should be non-negative. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: double TrimmingMarkLength
            (
            );
            /**Sets  the trimming mark length. It should be non-negative. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void SetTrimmingMarkLength
            (
                double trimmingMarkLength /** trimmingmarklength */ 
            );
            /**Returns  the trimming mark thickness. It should be non-negative. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: double TrimmingMarkThickness
            (
            );
            /**Sets  the trimming mark thickness. It should be non-negative. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void SetTrimmingMarkThickness
            (
                double trimmingMarkThickness /** trimmingmarkthickness */ 
            );
            /**Returns  the zones creation method. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Diagramming::SheetBordersAndZonesBuilder::ZoneMethod Method
            (
            );
            /**Sets  the zones creation method. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void SetMethod
            (
                NXOpen::Diagramming::SheetBordersAndZonesBuilder::ZoneMethod method /** method */ 
            );
            /**Returns  the horizontal size of zones. It should be greater than zero. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: double HorizontalSize
            (
            );
            /**Sets  the horizontal size of zones. It should be greater than zero. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void SetHorizontalSize
            (
                double horizontalSize /** horizontalsize */ 
            );
            /**Returns  the vertical size of zones. It should be greater than zero. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: double VerticalSize
            (
            );
            /**Sets  the vertical size of zones. It should be greater than zero. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void SetVerticalSize
            (
                double verticalSize /** verticalsize */ 
            );
            /**Returns  the zone origin. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Diagramming::SheetBordersAndZonesBuilder::ZoneOrigin Origin
            (
            );
            /**Sets  the zone origin. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void SetOrigin
            (
                NXOpen::Diagramming::SheetBordersAndZonesBuilder::ZoneOrigin origin /** origin */ 
            );
            /**Returns  the flag that indicates if zone marking is create. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: bool CreateZoneMarking
            (
            );
            /**Sets  the flag that indicates if zone marking is create. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void SetCreateZoneMarking
            (
                bool createZoneMarking /** createzonemarking */ 
            );
            /**Returns  the marking height. It should be non-negative. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: double MarkingHeight
            (
            );
            /**Sets  the marking height. It should be non-negative. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void SetMarkingHeight
            (
                double markingHeight /** markingheight */ 
            );
            /**Returns  the flag that indicates if zone labels are created. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: bool CreateZoneLabels
            (
            );
            /**Sets  the flag that indicates if zone labels are created. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void SetCreateZoneLabels
            (
                bool createZoneLabels /** createzonelabels */ 
            );
            /**Returns  the label height. It should be greater than zero. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: double LabelHeight
            (
            );
            /**Sets  the label height. It should be greater than zero. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void SetLabelHeight
            (
                double labelHeight /** labelheight */ 
            );
            /**Returns  the label font. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: int LabelFont
            (
            );
            /**Sets  the label font. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void SetLabelFont
            (
                int labelFont /** labelfont */ 
            );
            /**Returns  the top margin. It should be non-negative. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: double TopMargin
            (
            );
            /**Sets  the top margin. It should be non-negative. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void SetTopMargin
            (
                double topMargin /** topmargin */ 
            );
            /**Returns  the bottom margin. It should be non-negative. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: double BottomMargin
            (
            );
            /**Sets  the bottom margin. It should be non-negative. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void SetBottomMargin
            (
                double bottomMargin /** bottommargin */ 
            );
            /**Returns  the left margin. It should be non-negative. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: double LeftMargin
            (
            );
            /**Sets  the left margin. It should be non-negative. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void SetLeftMargin
            (
                double leftMargin /** leftmargin */ 
            );
            /**Returns  the right margin. It should be non-negative. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: double RightMargin
            (
            );
            /**Sets  the right margin. It should be non-negative. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void SetRightMargin
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
        };

        /// \endcond 
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