#ifndef NXOpen_DIAGRAMMING_LOCATIONBUILDER_HXX_INCLUDED
#define NXOpen_DIAGRAMMING_LOCATIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Diagramming_LocationBuilder.ja
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
#include <NXOpen/Diagramming_LocationBuilder.hxx>
#include <NXOpen/Diagramming_SheetElement.hxx>
#include <NXOpen/Diagramming_BaseSubObjectBuilder.hxx>
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
        class LocationBuilder;
    }
    namespace Diagramming
    {
        class BaseSubObjectBuilder;
    }
    namespace Diagramming
    {
        class SheetElement;
    }
    namespace Diagramming
    {
        class _LocationBuilderBuilder;
        class LocationBuilderImpl;
        /**
            Represents a LocationBuilder.
             <br> This is a sub-builder class and cannot be directly instantiated  <br> 
         <br>  Created in NX10.0.0.  <br>  
        */
        class NXOPENCPP_DIAGRAMMINGEXPORT  LocationBuilder : public NXOpen::Diagramming::BaseSubObjectBuilder
        {
            private: LocationBuilderImpl * m_locationbuilder_impl;
            private: friend class  _LocationBuilderBuilder;
            protected: LocationBuilder();
            public: ~LocationBuilder();
            /**Returns  the sheet element whose coordinate system the coordinate is specified in. If this is NULL, the coordinate is in the Sheet's coordinate system. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Diagramming::SheetElement * Reference
            (
            );
            /**Sets  the sheet element whose coordinate system the coordinate is specified in. If this is NULL, the coordinate is in the Sheet's coordinate system. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void SetReference
            (
                NXOpen::Diagramming::SheetElement * reference /** reference */ 
            );
            /**Returns  the evaluated X coordinate value that is the result calculated by the input percentage and offset. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: double EvaluatedValueX
            (
            );
            /**Returns  the user input X coordinate.
                        If the location refers to an object, the input X is the offset to the X coordinate of the object; Otherwise, it's the X coordinate value. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: double InputValueX
            (
            );
            /**Sets  the user input X coordinate.
                        If the location refers to an object, the input X is the offset to the X coordinate of the object; Otherwise, it's the X coordinate value. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void SetInputValueX
            (
                double inputValueX /** inputvaluex */ 
            );
            /**Returns  the user input percentage (0.0 to 1.0) of the width of the referenced object. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: double InputPercentX
            (
            );
            /**Sets  the user input percentage (0.0 to 1.0) of the width of the referenced object. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void SetInputPercentX
            (
                double inputPercentX /** inputpercentx */ 
            );
            /**Returns  the evaluated Y coordinate value that is the result calculated by input percentage and offset. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: double EvaluatedValueY
            (
            );
            /**Returns  the user input Y coordinate.
                        If the location refers to an object, the input Y is the offset to the Y coordinate of the object; Otherwise, it's the Y coordinate value. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: double InputValueY
            (
            );
            /**Sets  the user input Y coordinate.
                        If the location refers to an object, the input Y is the offset to the Y coordinate of the object; Otherwise, it's the Y coordinate value. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void SetInputValueY
            (
                double inputValueY /** inputvaluey */ 
            );
            /**Returns  the user input percentage (0.0 to 1.0) of the height of the referenced object. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: double InputPercentY
            (
            );
            /**Sets  the user input percentage (0.0 to 1.0) of the height of the referenced object. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void SetInputPercentY
            (
                double inputPercentY /** inputpercenty */ 
            );
            /**Returns  the up to date flag.
                        If true, @link NXOpen::Diagramming::LocationBuilder::EvaluatedValueX NXOpen::Diagramming::LocationBuilder::EvaluatedValueX@endlink  and @link NXOpen::Diagramming::LocationBuilder::EvaluatedValueY NXOpen::Diagramming::LocationBuilder::EvaluatedValueY@endlink 
                        of @link NXOpen::Diagramming::LocationBuilder NXOpen::Diagramming::LocationBuilder@endlink  may be used; Otherwise it must be evaluated.
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: bool UpToDate
            (
            );
            /** Set the x value of the location. 
                        The inputPercent means of the x coordinate value as a percentage of the size of its reference object. The valid value is from 0.0 to 1.0, and 1.0 means 100%.
                        The inputValue means the offset value of the x coordinate from the calculated location by the inputPercent value. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void SetValueX
            (
                double inputPercent /** inputpercent */ ,
                double inputValue /** inputvalue */ 
            );
            /** Set the y value of the location. 
                        The inputPercent means of the y coordinate value as a percentage of the size of its reference object. The valid value is from 0.0 to 1.0, and 1.0 means 100%.
                        The inputValue means the offset value of the y coordinate from the calculated location by the inputPercent value. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void SetValueY
            (
                double inputPercent /** inputpercent */ ,
                double inputValue /** inputvalue */ 
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
