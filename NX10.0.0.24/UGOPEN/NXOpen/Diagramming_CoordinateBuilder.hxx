#ifndef NXOpen_DIAGRAMMING_COORDINATEBUILDER_HXX_INCLUDED
#define NXOpen_DIAGRAMMING_COORDINATEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Diagramming_CoordinateBuilder.ja
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
#include <NXOpen/Diagramming_CoordinateBuilder.hxx>
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
        class CoordinateBuilder;
    }
    namespace Diagramming
    {
        class BaseSubObjectBuilder;
    }
    namespace Diagramming
    {
        class _CoordinateBuilderBuilder;
        class CoordinateBuilderImpl;

        /// \cond NX_NO_DOC 
        /**
            Represents a CoordinateBuilder.
             <br> This is a sub-builder class and cannot be directly instantiated  <br> 
         <br>  Created in NX10.0.0.  <br>  
        */
        class NXOPENCPP_DIAGRAMMINGEXPORT  CoordinateBuilder : public NXOpen::Diagramming::BaseSubObjectBuilder
        {
            private: CoordinateBuilderImpl * m_coordinatebuilder_impl;
            private: friend class  _CoordinateBuilderBuilder;
            protected: CoordinateBuilder();
            public: ~CoordinateBuilder();
            /**Returns  the evaluated coordinate value. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: double EvaluatedValue
            (
            );
            /**Returns  the fixed after creation flag. if true, the @link NXOpen::Diagramming::DiagrammingCoordinatemode NXOpen::Diagramming::DiagrammingCoordinatemode@endlink  
                        becomes @link NXOpen::Diagramming::DiagrammingCoordinatemodeAbsolute NXOpen::Diagramming::DiagrammingCoordinatemodeAbsolute@endlink  after the initial evaluation.
                        This provides the application a mechanism to initially specify that the coordinate is 
                        @link NXOpen::Diagramming::DiagrammingCoordinatemodePercent NXOpen::Diagramming::DiagrammingCoordinatemodePercent@endlink  in relation 
                        to the sheet or some sheet element. Once the @link NXOpen::Diagramming::CoordinateBuilder NXOpen::Diagramming::CoordinateBuilder@endlink  is evaluated, 
                        the @link NXOpen::Diagramming::DiagrammingCoordinatemode NXOpen::Diagramming::DiagrammingCoordinatemode@endlink  is treated as though it 
                        were @link NXOpen::Diagramming::DiagrammingCoordinatemodeAbsolute NXOpen::Diagramming::DiagrammingCoordinatemodeAbsolute@endlink . 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: bool FixedAfterCreation
            (
            );
            /**Returns  the user input coordinate. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: double InputValue
            (
            );
            /**Sets  the user input coordinate. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void SetInputValue
            (
                double inputValue /** inputvalue */ 
            );
            /**Returns  the user input coordinate as a percentage (0.0 to 1.0). 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: double InputPercent
            (
            );
            /**Sets  the user input coordinate as a percentage (0.0 to 1.0). 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void SetInputPercent
            (
                double inputPercent /** inputpercent */ 
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
