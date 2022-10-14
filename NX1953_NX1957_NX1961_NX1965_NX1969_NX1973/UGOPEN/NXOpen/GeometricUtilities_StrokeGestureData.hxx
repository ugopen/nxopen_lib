#ifndef NXOpen_GEOMETRICUTILITIES_STROKEGESTUREDATA_HXX_INCLUDED
#define NXOpen_GEOMETRICUTILITIES_STROKEGESTUREDATA_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     GeometricUtilities_StrokeGestureData.ja
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
        class StrokeGestureData;
    }
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    namespace GeometricUtilities
    {
        class _StrokeGestureDataBuilder;
        class StrokeGestureDataImpl;
        /** Represents a @link NXOpen::GeometricUtilities::StrokeGestureData NXOpen::GeometricUtilities::StrokeGestureData@endlink .
                A stroke is an ordered list of points. 
         <br>  Created in NX1926.0.0.  <br>  
        */
        class NXOPENCPP_GEOMETRICUTILITIESEXPORT  StrokeGestureData : public NXOpen::TaggedObject, public virtual NXOpen::GeometricUtilities::IComponentBuilder
        {
             /** Structure representing stroke point in absolute space. 
             <br>  Created in NX1926.0.0.  <br>  
            */
            public:
            struct Point
            {
                public: /** The point */NXOpen::Point3d Position;
                public: /** The speed */double Speed;
                public: Point() :
                    Position(),
                    Speed()
                {
                }
                /** Constructor for the Point struct. */ 
                public: Point(const NXOpen::Point3d &positionInitial /** The point */, 
                        double speedInitial /** The speed */) :
                    Position(positionInitial),
                    Speed(speedInitial)
                {
                }
            };

            private: StrokeGestureDataImpl * m_strokegesturedata_impl;
            private: friend class  _StrokeGestureDataBuilder;
            protected: StrokeGestureData();
            public: ~StrokeGestureData();
            /** Appends a point to the stroke 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_draw_shape (" NX Draw Shape Functionality") */
            public: void AddPoint
            (
                const NXOpen::GeometricUtilities::StrokeGestureData::Point & point /** point */ 
            );
            /** Queries all the points  @return  
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_draw_shape (" NX Draw Shape Functionality") */
            public: std::vector<NXOpen::GeometricUtilities::StrokeGestureData::Point> GetPoints
            (
            );
            /** Deletes all the points 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_draw_shape (" NX Draw Shape Functionality") */
            public: void Clear
            (
            );
            /** Defines the plane in which stroke gesture is executed. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_draw_shape (" NX Draw Shape Functionality") */
            public: void SetDrawingPlane
            (
                const NXOpen::Matrix3x3 & matrix /** matrix */ 
            );
            /**Returns  the drawing scale. The view scale at which stroke is drawn. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_draw_shape (" NX Draw Shape Functionality") */
            public: double DrawingScale
            (
            );
            /**Sets  the drawing scale. The view scale at which stroke is drawn. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_draw_shape (" NX Draw Shape Functionality") */
            public: void SetDrawingScale
            (
                double scale /** scale */ 
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