#ifndef NXOpen_PREFERENCES_PARTVISUALIZATIONLINE_HXX_INCLUDED
#define NXOpen_PREFERENCES_PARTVISUALIZATIONLINE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Preferences_PartVisualizationLine.ja
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
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Preferences
    {
        class PartVisualizationLine;
    }
    namespace Preferences
    {
        class PartPreferences;
    }
    namespace Preferences
    {
        class PartVisualizationLineImpl;
        /** Represents the set of visualization preferences under Line tab applicable to part  <br> To obtain an instance of this class, refer to @link Preferences::PartPreferences Preferences::PartPreferences@endlink  <br> */
        class NXOPENCPPEXPORT  PartVisualizationLine
        {
            /** Describes whether Line Font Display type is hardware or software. */
            public: enum LineFontDisplayType
            {
                LineFontDisplayTypeSoftware/** software */ ,
                LineFontDisplayTypeHardware/** hardware */ 
            };

            private: PartVisualizationLineImpl * m_partvisualizationline_impl;
            private: NXOpen::Preferences::PartPreferences* m_owner;
            /** Constructor */
            public: explicit PartVisualizationLine(NXOpen::Preferences::PartPreferences *owner);
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~PartVisualizationLine();
            /**Returns  the line font display. Controls the line font. The Hardware option uses the system graphics library to generate the 
            seven standard line fonts. Selecting hardware line fonts can improve drawing performance and reduce memory consumption. 
            The Software option generates non-solid curves with the values entered for the Dash, Space, and Symbol size.  <br> License requirements : None */
            public: NXOpen::Preferences::PartVisualizationLine::LineFontDisplayType LineFontDisplay
            (
            );
            /**Sets  the line font display. Controls the line font. The Hardware option uses the system graphics library to generate the 
            seven standard line fonts. Selecting hardware line fonts can improve drawing performance and reduce memory consumption. 
            The Software option generates non-solid curves with the values entered for the Dash, Space, and Symbol size.  <br> License requirements : None */
            public: void SetLineFontDisplay
            (
                NXOpen::Preferences::PartVisualizationLine::LineFontDisplayType lineFontDisplay /** line font display */ 
            );
            /**Returns  the dash size. Sets the length of a segment of a dashed curve.  <br> License requirements : None */
            public: double DashSize
            (
            );
            /**Sets  the dash size. Sets the length of a segment of a dashed curve.  <br> License requirements : None */
            public: void SetDashSize
            (
                double lineDashSize /** line dash size */ 
            );
            /**Returns  the space size. Sets the distance between two segments of a dashed curve.  <br> License requirements : None */
            public: double SpaceSize
            (
            );
            /**Sets  the space size. Sets the distance between two segments of a dashed curve.  <br> License requirements : None */
            public: void SetSpaceSize
            (
                double lineSpaceSize /** line space size */ 
            );
            /**Returns  the symbol size. Controls the displayed size of symbols used in software line fonts.  <br> License requirements : None */
            public: double SymbolSize
            (
            );
            /**Sets  the symbol size. Controls the displayed size of symbols used in software line fonts.  <br> License requirements : None */
            public: void SetSymbolSize
            (
                double lineSymbolSize /** line symbol size */ 
            );
            /**Returns  the curve tolerance. Specifies the level of detail for the current Display Mode.  <br> License requirements : None */
            public: double CurveTolerance
            (
            );
            /**Sets  the curve tolerance. Specifies the level of detail for the current Display Mode.  <br> License requirements : None */
            public: void SetCurveTolerance
            (
                double lineCurveTolerance /** line curve tolerance */ 
            );
            /**Returns  the show widths option. If true, the object width attribute determines the displayed width of lines or curves used 
            to represent an object.If false, all curves are drawn thin, regardless of object width settings.  <br> License requirements : None */
            public: bool ShowWidths
            (
            );
            /**Sets  the show widths option. If true, the object width attribute determines the displayed width of lines or curves used 
            to represent an object.If false, all curves are drawn thin, regardless of object width settings.  <br> License requirements : None */
            public: void SetShowWidths
            (
                bool isShowWidthOn /** isshowwidthon */ 
            );
        }; //lint !e1712 default constructor not defined for class  

    }
}
#undef EXPORTLIBRARY
#endif