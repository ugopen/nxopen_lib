#ifndef NXOpen_FEATURES_SUBDIVISION_SUBDIVISIONPRIMITIVESHAPEBUILDEREX_HXX_INCLUDED
#define NXOpen_FEATURES_SUBDIVISION_SUBDIVISIONPRIMITIVESHAPEBUILDEREX_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_Subdivision_SubdivisionPrimitiveShapeBuilderEx.ja
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
#include <NXOpen/Features_Subdivision_SubdivisionPrimitiveShapeBuilderEx.hxx>
#include <NXOpen/GeometricUtilities_TransformerData.hxx>
#include <NXOpen/Builder.hxx>
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
        namespace Subdivision
        {
            class SubdivisionPrimitiveShapeBuilderEx;
        }
    }
    class Builder;
    class Expression;
    namespace GeometricUtilities
    {
        class TransformerData;
    }
    class Point;
    namespace Features
    {
        namespace Subdivision
        {
            class _SubdivisionPrimitiveShapeBuilderExBuilder;
            class SubdivisionPrimitiveShapeBuilderExImpl;
            /** Represents a @link Features::Subdivision::SubdivisionPrimitiveShapeBuilderEx Features::Subdivision::SubdivisionPrimitiveShapeBuilderEx@endlink  builder.  <br> To create a new instance of this class, use @link NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateSubdivisionPrimitiveShapeBuilderEx  NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateSubdivisionPrimitiveShapeBuilderEx @endlink  <br> 
            Default values.
            <table border="1"> 
             
            <tr><th> 
            Property</th>  <th> 
            Value</th> </tr>
            <tr><td> 
             
            CircularSegments </td> <td> 
             
            4 </td> </tr> 

            <tr><td> 
             
            Height.Value </td> <td> 
             
            100 (millimeters part), 4 (inches part) </td> </tr> 

            <tr><td> 
             
            HeightZ.Value </td> <td> 
             
            100 (millimeters part), 4 (inches part) </td> </tr> 

            <tr><td> 
             
            InnerSize.Value </td> <td> 
             
            50 (millimeters part), 2 (inches part) </td> </tr> 

            <tr><td> 
             
            LengthX.Value </td> <td> 
             
            100 (millimeters part), 4 (inches part) </td> </tr> 

            <tr><td> 
             
            LinearSegments </td> <td> 
             
            1 </td> </tr> 

            <tr><td> 
             
            OuterSize.Value </td> <td> 
             
            100 (millimeters part), 4 (inches part) </td> </tr> 

            <tr><td> 
             
            RadialSegments </td> <td> 
             
            8 </td> </tr> 

            <tr><td> 
             
            Size.Value </td> <td> 
             
            100 (millimeters part), 4 (inches part) </td> </tr> 

            <tr><td> 
             
            WidthY.Value </td> <td> 
             
            100 (millimeters part), 4 (inches part) </td> </tr> 

            <tr><td> 
             
            XSegments </td> <td> 
             
            1 </td> </tr> 

            <tr><td> 
             
            YSegments </td> <td> 
             
            1 </td> </tr> 

            <tr><td> 
             
            ZSegments </td> <td> 
             
            1 </td> </tr> 

            </table>  

             <br>  Created in NX11.0.0.  <br>  
            */
            class NXOPENCPP_FEATURESEXPORT  SubdivisionPrimitiveShapeBuilderEx : public NXOpen::Builder
            {
                /** Type of primitive. */
                public: enum Types
                {
                    TypesSphere/** sphere */ ,
                    TypesCylinder/** cylinder */ ,
                    TypesBlock/** block */ ,
                    TypesCircle/** circle */ ,
                    TypesRectangle/** rectangle */ ,
                    TypesTorus/** torus */ 
                };

                /** Level of subdivisions of cubical cage to construct spherical primitive. */
                public: enum SphereSubdivisionLevel
                {
                    SphereSubdivisionLevelBase/** base */ ,
                    SphereSubdivisionLevelFirst/** first */ ,
                    SphereSubdivisionLevelSecond/** second */ 
                };

                private: SubdivisionPrimitiveShapeBuilderExImpl * m_subdivisionprimitiveshapebuilderex_impl;
                private: friend class  _SubdivisionPrimitiveShapeBuilderExBuilder;
                protected: SubdivisionPrimitiveShapeBuilderEx();
                public: ~SubdivisionPrimitiveShapeBuilderEx();
                /**Returns  the type. 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::Subdivision::SubdivisionPrimitiveShapeBuilderEx::Types Type
                (
                );
                /**Sets  the type. 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : nx_subdivision (" NX SUBDIVISION") */
                public: void SetType
                (
                    NXOpen::Features::Subdivision::SubdivisionPrimitiveShapeBuilderEx::Types type /** type */ 
                );
                /**Returns  the origin. 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Point * Origin
                (
                );
                /**Sets  the origin. 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : nx_subdivision (" NX SUBDIVISION") */
                public: void SetOrigin
                (
                    NXOpen::Point * origin /** origin */ 
                );
                /**Returns  the size. 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * Size
                (
                );
                /**Returns  the height. 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * Height
                (
                );
                /**Returns  the length in X direction. 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * LengthX
                (
                );
                /**Returns  the width in Y direction. 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * WidthY
                (
                );
                /**Returns  the height in Z direction. 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * HeightZ
                (
                );
                /** Updates the mesh data after changes in the origin. 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : None */
                public: void UpdateMesh
                (
                );
                /**Returns  the transformation tool. 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::GeometricUtilities::TransformerData * Transformer
                (
                );
                /**Returns  the inner size of torus. 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * InnerSize
                (
                );
                /**Returns  the outer size of torus. 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * OuterSize
                (
                );
                /**Returns  the subdivision level. 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::Subdivision::SubdivisionPrimitiveShapeBuilderEx::SphereSubdivisionLevel SphereSubdivisionLevelOption
                (
                );
                /**Sets  the subdivision level. 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : nx_subdivision (" NX SUBDIVISION") */
                public: void SetSphereSubdivisionLevelOption
                (
                    NXOpen::Features::Subdivision::SubdivisionPrimitiveShapeBuilderEx::SphereSubdivisionLevel level /** level */ 
                );
                /**Returns  the number of segments in X direction. 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : None */
                public: int XSegments
                (
                );
                /**Sets  the number of segments in X direction. 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : nx_subdivision (" NX SUBDIVISION") */
                public: void SetXSegments
                (
                    int numSegments /** numsegments */ 
                );
                /**Returns  the number of segments in Y direction. 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : None */
                public: int YSegments
                (
                );
                /**Sets  the number of segments in Y direction. 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : nx_subdivision (" NX SUBDIVISION") */
                public: void SetYSegments
                (
                    int numSegments /** numsegments */ 
                );
                /**Returns  the number of segments in Z direction. 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : None */
                public: int ZSegments
                (
                );
                /**Sets  the number of segments in Z direction. 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : nx_subdivision (" NX SUBDIVISION") */
                public: void SetZSegments
                (
                    int numSegments /** numsegments */ 
                );
                /**Returns  the number of segments in radial direction. 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : None */
                public: int RadialSegments
                (
                );
                /**Sets  the number of segments in radial direction. 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : nx_subdivision (" NX SUBDIVISION") */
                public: void SetRadialSegments
                (
                    int numSegments /** numsegments */ 
                );
                /**Returns  the number of segments in circular direction. 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : None */
                public: int CircularSegments
                (
                );
                /**Sets  the number of segments in circular direction. 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : nx_subdivision (" NX SUBDIVISION") */
                public: void SetCircularSegments
                (
                    int numSegments /** numsegments */ 
                );
                /**Returns  the number of segments in linear direction. 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : None */
                public: int LinearSegments
                (
                );
                /**Sets  the number of segments in linear direction. 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : nx_subdivision (" NX SUBDIVISION") */
                public: void SetLinearSegments
                (
                    int numSegments /** numsegments */ 
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
