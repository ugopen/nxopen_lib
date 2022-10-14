#ifndef NXOpen_FEATURES_SUBDIVISION_SUBDIVISIONPRIMITIVESHAPEBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_SUBDIVISION_SUBDIVISIONPRIMITIVESHAPEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_Subdivision_SubdivisionPrimitiveShapeBuilder.ja
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
#include <NXOpen/Expression.hxx>
#include <NXOpen/Features_Subdivision_SubdivisionPrimitiveShapeBuilder.hxx>
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
            class SubdivisionPrimitiveShapeBuilder;
        }
    }
    class Builder;
    class Expression;
    class Point;
    namespace Features
    {
        namespace Subdivision
        {
            class _SubdivisionPrimitiveShapeBuilderBuilder;
            class SubdivisionPrimitiveShapeBuilderImpl;
            /** Represents a @link Features::Subdivision::SubdivisionPrimitiveShapeBuilder Features::Subdivision::SubdivisionPrimitiveShapeBuilder@endlink  builder.  <br> To create a new instance of this class, use @link Features::Subdivision::SubdivisionBodyCollection::CreateSubdivisionPrimitiveShapeBuilder  Features::Subdivision::SubdivisionBodyCollection::CreateSubdivisionPrimitiveShapeBuilder @endlink  <br> 
            Default values.
            <table border="1"> 
             
            <tr><th> 
            Property</th>  <th> 
            Value</th> </tr>
            <tr><td> 
             
            Height.Value </td> <td> 
             
            100 (millimeters part), 4 (inches part) </td> </tr> 

            <tr><td> 
             
            HeightZ.Value </td> <td> 
             
            100 (millimeters part), 4 (inches part) </td> </tr> 

            <tr><td> 
             
            LengthX.Value </td> <td> 
             
            100 (millimeters part), 4 (inches part) </td> </tr> 

            <tr><td> 
             
            Size.Value </td> <td> 
             
            100 (millimeters part), 4 (inches part) </td> </tr> 

            <tr><td> 
             
            WidthY.Value </td> <td> 
             
            100 (millimeters part), 4 (inches part) </td> </tr> 

            </table>  

             <br>  Created in NX9.0.0.  <br>  
            */
            class NXOPENCPP_FEATURESEXPORT  SubdivisionPrimitiveShapeBuilder : public Builder
            {
                /** Type of primitive. */
                public: enum Types
                {
                    TypesSphere/** sphere */ ,
                    TypesCylinder/** cylinder */ ,
                    TypesBlock/** block */ ,
                    TypesCircle/** circle */ ,
                    TypesRectangle/** rectangle */ 
                };

                private: SubdivisionPrimitiveShapeBuilderImpl * m_subdivisionprimitiveshapebuilder_impl;
                private: friend class  _SubdivisionPrimitiveShapeBuilderBuilder;
                protected: SubdivisionPrimitiveShapeBuilder();
                public: ~SubdivisionPrimitiveShapeBuilder();
                /**Returns  the type. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::Subdivision::SubdivisionPrimitiveShapeBuilder::Types Type
                (
                );
                /**Sets  the type. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_subdivision (" NX SUBDIVISION") */
                public: void SetType
                (
                    NXOpen::Features::Subdivision::SubdivisionPrimitiveShapeBuilder::Types type /** type */ 
                );
                /**Returns  the origin. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Point * Origin
                (
                );
                /**Sets  the origin. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_subdivision (" NX SUBDIVISION") */
                public: void SetOrigin
                (
                    NXOpen::Point * origin /** origin */ 
                );
                /**Returns  the size. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * Size
                (
                );
                /**Returns  the height. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * Height
                (
                );
                /**Returns  the length in x direction. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * LengthX
                (
                );
                /**Returns  the width in y direction. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * WidthY
                (
                );
                /**Returns  the height in z direction. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * HeightZ
                (
                );
                /** Updates the mesh data after changes in the origin. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: void UpdateMesh
                (
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