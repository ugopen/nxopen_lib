#ifndef NXOpen_FEATURES_DRAWSHAPES_DRAWSHAPEDATA_HXX_INCLUDED
#define NXOpen_FEATURES_DRAWSHAPES_DRAWSHAPEDATA_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_DrawShapes_DrawShapeData.ja
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
#include <NXOpen/Builder.hxx>
#include <NXOpen/ScCollector.hxx>
#include <NXOpen/libnxopencpp_features_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Features
    {
        namespace DrawShapes
        {
            class DrawShapeData;
        }
    }
    class Builder;
    class CoordinateSystem;
    class ScCollector;
    namespace Features
    {
        namespace DrawShapes
        {
            class _DrawShapeDataBuilder;
            class DrawShapeDataImpl;
            /** Represents @link  NXOpen::Features::DrawShapes::DrawShapeData   NXOpen::Features::DrawShapes::DrawShapeData @endlink 
                    allowing user to define input faces or datums for Draw Shape
                 <br> To create a new instance of this class, use @link NXOpen::Features::DrawShapes::DrawShapeCollection::CreateDrawShapeData  NXOpen::Features::DrawShapes::DrawShapeCollection::CreateDrawShapeData @endlink  <br> 
             <br>  Created in NX1926.0.0.  <br>  
            */
            class NXOPENCPP_FEATURESEXPORT  DrawShapeData : public NXOpen::Builder
            {
                /** the drawing base types */
                public: enum DrawingBaseTypes
                {
                    DrawingBaseTypesFaces/** faces */ ,
                    DrawingBaseTypesPlane/** plane */ 
                };

                private: DrawShapeDataImpl * m_drawshapedata_impl;
                private: friend class  _DrawShapeDataBuilder;
                protected: DrawShapeData();
                public: ~DrawShapeData();
                /**Returns  the drawing base type 
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::DrawShapes::DrawShapeData::DrawingBaseTypes DrawingBaseType
                (
                );
                /**Sets  the drawing base type 
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : nx_draw_shape (" NX Draw Shape Functionality") */
                public: void SetDrawingBaseType
                (
                    NXOpen::Features::DrawShapes::DrawShapeData::DrawingBaseTypes type /** type */ 
                );
                /**Returns  the coordinate system. XY Plane of the coordinate system is used as drawing base. 
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::CoordinateSystem * CoordinateSystem
                (
                );
                /**Sets  the coordinate system. XY Plane of the coordinate system is used as drawing base. 
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : nx_draw_shape (" NX Draw Shape Functionality") */
                public: void SetCoordinateSystem
                (
                    NXOpen::CoordinateSystem * csys /** csys */ 
                );
                /**Returns  the faces 
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::ScCollector * Faces
                (
                );
                /**Returns  whether to create the associative output or non associative output
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : None */
                public: bool Associative
                (
                );
                /**Sets  whether to create the associative output or non associative output
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : nx_draw_shape (" NX Draw Shape Functionality") */
                public: void SetAssociative
                (
                    bool associative /** associative */ 
                );
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

#undef EXPORTLIBRARY
#endif
