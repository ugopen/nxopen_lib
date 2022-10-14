#ifndef NXOpen_CAE_XYPLOTDATATYPES_HXX_INCLUDED
#define NXOpen_CAE_XYPLOTDATATYPES_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_XyplotDataTypes.ja
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

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace CAE
    {
        namespace Xyplot
        {
            /** Represents the plot graph style */
            enum GraphStyle
            {
                GraphStyleLine/** Option to display plot in curve style */,
                GraphStyleBar/** Option to display plot in bar style  */,
                GraphStylePlate/** Option to display plot in plate style */,
                GraphStyleSurface/** Option to display plot in surface style */,
                GraphStyleScatter/** Option to display plot in scatter style */
            };

            /** Represents the 2D plot complex option */
            enum ComplexOption2D
            {
                ComplexOption2DMagnitude/** Magnitude of the complex data for 2D plot */,
                ComplexOption2DMagnitudePhase/** Magnitude and phase angle of complex data for 2D plot */,
                ComplexOption2DPhase/** Only the phase of the complex data for 2D plot */,
                ComplexOption2DReal/** Only the real part of the complex data for 2D plot */,
                ComplexOption2DRealImaginary/** Real and imaginary of the complex data for 2D plot */,
                ComplexOption2DRealImaginaryPhase/** Real, imaginary and phase angle of the complex data for 2D plot */,
                ComplexOption2DPolar/** Polar for 2D plot */,
                ComplexOption2DArgand/** Argand for 2D plot */,
                ComplexOption2DPolar3D/** Polar for 3D plot */,
                ComplexOption2DArgand3D/** Argand for 3D plot which z coordindate come from the x coordinate */,
                ComplexOption2DPhaseMagnitude/** Phase angle and Magnitude of complex data for 2D plot */,
                ComplexOption2DImaginaryReal/** Real and imaginary of the complex data for 2D plot */,
                ComplexOption2DPhaseRealImaginary/** Phase angle, real and imaginary of the complex data for 2D plot */,
                ComplexOption2DImaginaryRealPhase/** Imaginary, real and phase angle of the complex data for 2D plot */,
                ComplexOption2DPhaseImaginaryReal/** Phase angle, imaginary and real of the complex data for 2D plot */,
                ComplexOption2DNichols/** Nichols for 2D plot */,
                ComplexOption2DAtPhaseAngle/** At phase angle for 2D plot */,
                ComplexOption2DSignedMagnitude/** Signed magnitude for 2D plot */
            };

            /** Represents the 3D plot complex option */
            enum ComplexOption3D
            {
                ComplexOption3DMagnitude/** Magnitude of the complex data for 3D plot */,
                ComplexOption3DPhase/** Phase of the complex data for 3D plot */,
                ComplexOption3DReal/** Real part of the complex data for 3D plot */,
                ComplexOption3DImaginary/** Imaginary part of the complex data for 3D plot */,
                ComplexOption3DArgand/** Argand for 3D plot which use the real z coordindate */,
                ComplexOption3DOrbit/** Orbit for 3D plot */,
                ComplexOption3DNichols/** Nichols for 3D plot */,
                ComplexOption3DAtPhaseAngle/** At phase angle for 3D plot */,
                ComplexOption3DSignedMagnitude/** Signed magnitude for 3D plot */
            };

            /** Prepresents the phase range option */
            enum PhaseRangeOption
            {
                PhaseRangeOptionNegativeTwoPiToZero/** Displays phase between -360 and 0 */,
                PhaseRangeOptionZeroToTwoPi/** Displays phase between 0 and 360 */,
                PhaseRangeOptionNegativePiToPi/** Displays phase between -180 and 180 */,
                PhaseRangeOptionNegativeOneHalfPiToHalfPi/** Displays phase between -270 and 90 */,
                PhaseRangeOptionNegativeHalfPiToOneHalfPi/** Displays phase between -90 and 270 */
            };

            /** Represents the label text type */
            enum TextType
            {
                TextTypeNone/** Not defined type */,
                TextTypeTitle/** Title label */,
                TextTypeLegend/** Legend label */,
                TextTypeGraphName/** Graph name label */,
                TextTypePageNumber/** Page number label */,
                TextTypeMarker/** Marker label */,
                TextTypeNote/** Note label */,
                TextTypeProbingText/** Probing label */,
                TextTypeXLabel/** X Axis name label */,
                TextTypeYLabel/** Y Axis name label */,
                TextTypeZLabel/** Z Axis name label */,
                TextTypeXNumber/** X Axis number label */,
                TextTypeYNumber/** Y Axis number label */,
                TextTypeZNumber/** Z Axis number label */
            };

            /** Represents the font type */
            enum Fonttype
            {
                FonttypeNx/** NX Font */,
                FonttypeStandard/** Standard Font */
            };

            /** Represents the axis direction */
            enum AxisDirection
            {
                AxisDirectionX/** X-axis */,
                AxisDirectionY/** Y-axis */,
                AxisDirectionZ/** Z-axis */
            };

            /** Represents the text alignment */
            enum TextAlignment
            {
                TextAlignmentLeft/** Left align text */,
                TextAlignmentCenter/** Center align text */,
                TextAlignmentRight/** Right align text */
            };

            /** Represents the text orientation */
            enum TextOrientation
            {
                TextOrientationHorizontal/** Horizontal text orientation */,
                TextOrientationUpward/** Upward text orientation */,
                TextOrientationDownward/** Downward text orientation */
            };

            /** Represents the type of scale for X or Y axis */
            enum AxisType
            {
                AxisTypeAuto/** Automatic type */,
                AxisTypeLinear/** Linear type */,
                AxisTypeLog/** Log type */,
                AxisTypeDb/** Db type */
            };

            /** Represents the DB scale for plot */
            enum AxisDBScale
            {
                AxisDBScaleTen/** Db 10 */,
                AxisDBScaleTwenty/** Db 20 */
            };

            /** Represents the unit system */
            enum UnitSystem
            {
                UnitSystemFunction/** Function unit */,
                UnitSystemModel/** Model unit */,
                UnitSystemSi/** International standard unit */,
                UnitSystemMn/** Milliforce unit */,
                UnitSystemMm/** Millimeter unit */,
                UnitSystemIn/** Inch unit */,
                UnitSystemCustom/** Custom unit */
            };

            /** Represents the grid style for plot */
            enum GridStyle
            {
                GridStyleNoGrid/** No grid displayed */,
                GridStyleGridOnly/** Only display grid */,
                GridStyleTicksOnly/** Only display tick */,
                GridStyleGridAndTicks/** Display both grid and tick */,
                GridStyleDenseGrid/** Display dense grid */
            };

            /** Represents the point marker */
            enum PointMarker
            {
                PointMarkerNone/** No marker */,
                PointMarkerPlus/** Plus marker */,
                PointMarkerDot/** Dot marker */,
                PointMarkerAsterisk/** Asterisk marker */,
                PointMarkerCircle/** Circle marker */,
                PointMarkerPoundsign/** Pound sign marker */,
                PointMarkerCross/** Cross marker */,
                PointMarkerSquare/** Square marker */,
                PointMarkerTriangle/** Triangle marker */,
                PointMarkerDiamond/** Diamond marker */,
                PointMarkerCenterLine/** Center line marker */
            };

            /** Represents the contouring range */
            enum ContouringRange
            {
                ContouringRangeBorderGrid/** Option to show contour range on the border of the grid */,
                ContouringRangeFullGrid/** Option to show contour range on the face of the grid */
            };

            /** Represents the direction option */
            enum Direction
            {
                DirectionX/** Option to show plot in the X axis direction */,
                DirectionZ/** Option to show plot in the Z axis direction */,
                DirectionXz/** Option to show plot in the both X and Z axis direction */
            };

            /** Represents the bar filling color option */
            enum BarColorOption
            {
                BarColorOptionFill/** Fill color or contour color with no shading */,
                BarColorOptionHidden/** Background color as fill */,
                BarColorOptionShaded/** Fill Color or contour color with shading */
            };

            /** Represents the plot type */
            enum PlotType
            {
                PlotTypePlot2D/** 2D plot */,
                PlotTypePlot2DInStack/** 2D plot in stacked sequence */,
                PlotTypePlot3D/** 3D plot */
            };

            /** Represents the plate filling color option */
            enum PlateColorOption
            {
                PlateColorOptionFill/** Fill color with no shading */,
                PlateColorOptionHidden/** Background color as fill */,
                PlateColorOptionShaded/** Fill Color with shading */
            };

            /** Represents the surface filling color option */
            enum SurfaceColorOption
            {
                SurfaceColorOptionNone/** No shading */,
                SurfaceColorOptionHidden/** Background color as fill */,
                SurfaceColorOptionShaded/** Fill Color or contour color with shading */
            };

            /** Represents the decimal number format */
            enum DecimalFormat
            {
                DecimalFormatActual/** Show decimal automatically */,
                DecimalFormatX/** Displays one digit followed by period */,
                DecimalFormatXx/** Displays two digits followed by period */,
                DecimalFormatXxx/** Displays three digits followed by period */,
                DecimalFormatXxxx/** Displays four digits followed by period */,
                DecimalFormatXexx/** Scientific notation with one digit followed by period,
                                                                 for example: 5.3E+05 */,
                DecimalFormatXxexx/** Scientific notation with two digits followed by period */,
                DecimalFormatXxxexx/** Scientific notation with three digits followed by period */,
                DecimalFormatXxxxexx/** Scientific notation with four digits followed by period */
            };

        }
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

#endif