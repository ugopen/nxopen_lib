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
#include <NXOpen/Diagramming_CoordinateBuilder.hxx>
#include <NXOpen/Diagramming_DataType.hxx>
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
        class CoordinateBuilder;
    }
    namespace Diagramming
    {
        class SheetElement;
    }
    namespace Diagramming
    {
        class _LocationBuilderBuilder;
        class LocationBuilderImpl;

        /// \cond NX_NO_DOC 
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
            /** Gets coordinate.  @return  
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Diagramming::CoordinateBuilder * GetCoordinate
            (
                NXOpen::Diagramming::Axis axis /** axis */ 
            );
            /**Returns  the up to date flag.
                        If true, @link Diagramming::CoordinateBuilder::EvaluatedValue Diagramming::CoordinateBuilder::EvaluatedValue@endlink 
                        of @link Diagramming::CoordinateBuilder Diagramming::CoordinateBuilder@endlink  may be used; Otherwise it must be evaluated.
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: bool UpToDate
            (
            );
            /**Returns  the modifiable flag.
                        If false, the @link Diagramming::CoordinateBuilder::InputValue Diagramming::CoordinateBuilder::InputValue@endlink 
                        and reference of @link Diagramming::CoordinateBuilder Diagramming::CoordinateBuilder@endlink  can not be changed.
                        The @link Diagramming::CoordinateBuilder::EvaluatedValue Diagramming::CoordinateBuilder::EvaluatedValue@endlink  may change if the object moves.
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: bool Modifiable
            (
            );
            /**Sets  the modifiable flag.
                        If false, the @link Diagramming::CoordinateBuilder::InputValue Diagramming::CoordinateBuilder::InputValue@endlink 
                        and reference of @link Diagramming::CoordinateBuilder Diagramming::CoordinateBuilder@endlink  can not be changed.
                        The @link Diagramming::CoordinateBuilder::EvaluatedValue Diagramming::CoordinateBuilder::EvaluatedValue@endlink  may change if the object moves.
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void SetModifiable
            (
                bool modifiable /** modifiable */ 
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