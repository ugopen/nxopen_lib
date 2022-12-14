#ifndef NXOpen_JOIN_REFPOINTSPOINTSBUILDER_HXX_INCLUDED
#define NXOpen_JOIN_REFPOINTSPOINTSBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Join_RefPointsPointsBuilder.ja
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
#include <NXOpen/GeometricUtilities_IComponentBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/ugmath.hxx>
#include <NXOpen/libjoinopencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Join
    {
        class RefPointsPointsBuilder;
    }
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    class Point;
    namespace Join
    {
        class _RefPointsPointsBuilderBuilder;
        class RefPointsPointsBuilderImpl;
        /** Used to create or edit a point in the list of points for Jointmark  <br> To create a new instance of this class, use @link NXOpen::Join::RefPointsBuilder::NewPoints  NXOpen::Join::RefPointsBuilder::NewPoints @endlink  <br> 
         <br>  Created in NX1872.0.0.  <br>  
        */
        class JOINOPENCPPEXPORT  RefPointsPointsBuilder : public NXOpen::TaggedObject, public virtual NXOpen::GeometricUtilities::IComponentBuilder
        {
            /** The point classification */
            public: enum PointPosition
            {
                PointPositionNone/** None specifed. */,
                PointPositionMovedAlongGuide/** User moved point from default location along the guide curve */,
                PointPositionMovedOffGuide/** User moved point from default location off the guide curve */
            };

            private: RefPointsPointsBuilderImpl * m_refpointspointsbuilder_impl;
            private: friend class  _RefPointsPointsBuilderBuilder;
            protected: RefPointsPointsBuilder();
            public: ~RefPointsPointsBuilder();
            /**Returns  the point  at which the feature is created 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_join (" NX Join") */
            public: NXOpen::Point * Point
            (
            );
            /**Sets  the point  at which the feature is created 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_join (" NX Join") */
            public: void SetPoint
            (
                NXOpen::Point * point /** point */ 
            );
            /** Update the csys using a new matrix. 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_join (" NX Join") */
            public: void UpdateCsys
            (
                const NXOpen::Matrix3x3 & matrix /** rotate matrix */
            );
            /** Validate whether the inputs to the component are sufficient for 
                        commit to be called.  If the component is not in a state to commit
                        then an exception is thrown.  For example, if the component requires
                        you to set some property, this method will throw an exception if
                        you haven't set it.  This method throws a not yet implemented
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
