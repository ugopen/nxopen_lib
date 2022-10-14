#ifndef NXOpen_AME_LINEARDIMENSIONBUILDER_HXX_INCLUDED
#define NXOpen_AME_LINEARDIMENSIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     AME_LinearDimensionBuilder.ja
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
#include <NXOpen/Diagramming_Port.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/libameopencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace AME
    {
        class LinearDimensionBuilder;
    }
    class Builder;
    namespace Diagramming
    {
        class Port;
    }
    namespace AME
    {
        class _LinearDimensionBuilderBuilder;
        class LinearDimensionBuilderImpl;
        /** Represents a Linear Dimension class Builder   <br> To create a new instance of this class, use @link NXOpen::AME::AMEManager::CreateLinearDimensionBuilder  NXOpen::AME::AMEManager::CreateLinearDimensionBuilder @endlink  <br> 
        Default values.
        <list type="table"> 
         
        <listheader><term> 
        Property</term>  <description> 
        Value</description> </listheader>
        <item><term> 
         
        DimensionSetType </term> <description> 
         
        Single </description> </item> 

        <item><term> 
         
        MeasurementDirectionType </term> <description> 
         
        Horizontal </description> </item> 

        </list> 

         <br>  Created in NX1980.0.0.  <br>  
        */
        class AMEOPENCPPEXPORT  LinearDimensionBuilder : public NXOpen::Builder
        {
            /** Represents the Dimension Set type */
            public: enum Dimensionset
            {
                DimensionsetSingle/** single */ ,
                DimensionsetChain/** chain */ ,
                DimensionsetBaseline/** baseline */ 
            };

            /** Represents the Direction of Measurement for Dimension. */
            public: enum MeasurementDirection
            {
                MeasurementDirectionHorizontal/** horizontal */ ,
                MeasurementDirectionVertical/** vertical */ 
            };

            private: LinearDimensionBuilderImpl * m_lineardimensionbuilder_impl;
            private: friend class  _LinearDimensionBuilderBuilder;
            protected: LinearDimensionBuilder();
            public: ~LinearDimensionBuilder();
            /**Returns  the Dimension Set type 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : ad_electrical_design ("AUTOMATION DESIGNER ELECTRICAL DESIGN") */
            public: NXOpen::AME::LinearDimensionBuilder::Dimensionset DimensionSetType
            (
            );
            /**Sets  the Dimension Set type 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : ad_electrical_design ("AUTOMATION DESIGNER ELECTRICAL DESIGN") */
            public: void SetDimensionSetType
            (
                NXOpen::AME::LinearDimensionBuilder::Dimensionset dimenset /** dimenset */ 
            );
            /**Returns  the Measurement Direction type 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : ad_electrical_design ("AUTOMATION DESIGNER ELECTRICAL DESIGN") */
            public: NXOpen::AME::LinearDimensionBuilder::MeasurementDirection MeasurementDirectionType
            (
            );
            /**Sets  the Measurement Direction type 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : ad_electrical_design ("AUTOMATION DESIGNER ELECTRICAL DESIGN") */
            public: void SetMeasurementDirectionType
            (
                NXOpen::AME::LinearDimensionBuilder::MeasurementDirection measurementdirectn /** measurementdirectn */ 
            );
            /** Sets the Selected Source Dimension Point 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : ad_electrical_design ("AUTOMATION DESIGNER ELECTRICAL DESIGN") */
            public: void SetSourceDimensionPoint
            (
                NXOpen::Diagramming::Port * sourceDimensionPoint /** sourcedimensionpoint */ 
            );
            /** Sets the Selected Target Dimension Point 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : ad_electrical_design ("AUTOMATION DESIGNER ELECTRICAL DESIGN") */
            public: void SetTargetDimensionPoint
            (
                NXOpen::Diagramming::Port * targetDimensionPoint /** targetdimensionpoint */ 
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