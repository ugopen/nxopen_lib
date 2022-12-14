#ifndef NXOpen_GEOMETRICUTILITIES_TRANSITIONCURVEBUILDER_HXX_INCLUDED
#define NXOpen_GEOMETRICUTILITIES_TRANSITIONCURVEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     GeometricUtilities_TransitionCurveBuilder.ja
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
#include <NXOpen/Expression.hxx>
#include <NXOpen/GeometricUtilities_TransitionCurveBuilder.hxx>
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
        class TransitionCurveBuilder;
    }
    class Expression;
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    namespace GeometricUtilities
    {
        class _TransitionCurveBuilderBuilder;
        class TransitionCurveBuilderImpl;
        /** 
                This class provides ability to create a transition(bridge) curve between two adjacent setback curves.
             <br> To create a new instance of this class, use @link NXOpen::Part::CreateEmptyTransitionCurveBuilder  NXOpen::Part::CreateEmptyTransitionCurveBuilder @endlink  <br> 
         <br>  Created in NX9.0.0.  <br>  
        */
        class NXOPENCPP_GEOMETRICUTILITIESEXPORT  TransitionCurveBuilder : public NXOpen::TaggedObject, public virtual NXOpen::GeometricUtilities::IComponentBuilder
        {
            /** Tangent direction options */
            public: enum TangentDirections
            {
                TangentDirectionsRail/** transition curve will be tangent to the blend rail curve */,
                TangentDirectionsLimit/** transition curve will be tangent to the limit curve */
            };

            private: TransitionCurveBuilderImpl * m_transitioncurvebuilder_impl;
            private: friend class  _TransitionCurveBuilderBuilder;
            protected: TransitionCurveBuilder();
            public: ~TransitionCurveBuilder();
            /**Returns  the start tangent direction 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricUtilities::TransitionCurveBuilder::TangentDirections StartTangentDirection
            (
            );
            /**Sets  the start tangent direction 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetStartTangentDirection
            (
                NXOpen::GeometricUtilities::TransitionCurveBuilder::TangentDirections direction /** direction */ 
            );
            /**Returns  the end tangent direction 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricUtilities::TransitionCurveBuilder::TangentDirections EndTangentDirection
            (
            );
            /**Sets  the end tangent direction 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetEndTangentDirection
            (
                NXOpen::GeometricUtilities::TransitionCurveBuilder::TangentDirections direction /** direction */ 
            );
            /**Returns  the start tangent magnitude 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * StartTangentMagnitude
            (
            );
            /**Returns  the end tangent magnitude 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * EndTangentMagnitude
            (
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
