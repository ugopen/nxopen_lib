#ifndef NXOpen_GEOMETRICUTILITIES_FLOWDIRECTION_HXX_INCLUDED
#define NXOpen_GEOMETRICUTILITIES_FLOWDIRECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     GeometricUtilities_FlowDirection.ja
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
#include <NXOpen/GeometricUtilities_FlowDirection.hxx>
#include <NXOpen/GeometricUtilities_IComponentBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_geometricutilities_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace GeometricUtilities
    {
        class FlowDirection;
    }
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    namespace GeometricUtilities
    {
        class _FlowDirectionBuilder;
        class FlowDirectionImpl;
        /**
            Represents a @link NXOpen::GeometricUtilities::FlowDirection NXOpen::GeometricUtilities::FlowDirection@endlink 
            Allows user to specify different flow direction to control output surface shape.
            
         <br>  Created in NX5.0.0.  <br>  
        */
        class NXOPENCPP_GEOMETRICUTILITIESEXPORT  FlowDirection : public NXOpen::TaggedObject, public virtual NXOpen::GeometricUtilities::IComponentBuilder
        {
            /** flow direction type. 
                    */
            public: enum Type
            {
                TypeNotSpecified/** Not Specified */,
                TypeIsoparametric/** Iso Parametric */,
                TypeIsoCurveU/** Iso Curve U */,
                TypeIsoCurveV/** Iso Curve V */,
                TypePerpendicular/** Perpendicular */,
                TypeAdjacentEdges/** Adjacent Edges */
            };

            private: FlowDirectionImpl * m_flowdirection_impl;
            private: friend class  _FlowDirectionBuilder;
            protected: FlowDirection();
            public: ~FlowDirection();
            /**Returns  the flow direction type.
                    
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricUtilities::FlowDirection::Type FlowDirectionType
            (
            );
            /**Sets  the flow direction type.
                    
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : nx_freeform_1 ("basic freeform modeling") */
            public: void SetFlowDirectionType
            (
                NXOpen::GeometricUtilities::FlowDirection::Type flowDirectionType /** flowdirectiontype */ 
            );
            /** Validate whether the inputs to the component are sufficient for 
                        commit to be called.  If the component is not in a state to commit
                        then an exception is thrown.  For example, if the component requires
                        you to set some property, this method will throw an exception if
                        you haven't set it.  This method throws a not-yet-implemented
                        NXException for some components.
                     @return  Was self validation successful 
             <br>  Created in NX3.0.1.  <br>  
             <br> License requirements : None */
            public: virtual bool Validate
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
