#ifndef NXOpen_FEATURES_MOVECURVEBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_MOVECURVEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_MoveCurveBuilder.ja
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
#include <NXOpen/Features_CurveFinderBuilder.hxx>
#include <NXOpen/Features_MoveCurveBuilder.hxx>
#include <NXOpen/GeometricUtilities_ModlMotion.hxx>
#include <NXOpen/Features_FeatureBuilder.hxx>
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
        class MoveCurveBuilder;
    }
    namespace Features
    {
        class CurveFinderBuilder;
    }
    namespace Features
    {
        class FeatureBuilder;
    }
    namespace GeometricUtilities
    {
        class ModlMotion;
    }
    namespace Features
    {
        class _MoveCurveBuilderBuilder;
        class MoveCurveBuilderImpl;
        /**
            Represents a @link NXOpen::Features::MoveCurve NXOpen::Features::MoveCurve@endlink  builder
             <br> To create a new instance of this class, use @link NXOpen::Features::SynchronousCurveCollection::CreateMoveCurveBuilder  NXOpen::Features::SynchronousCurveCollection::CreateMoveCurveBuilder @endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        CurveFinder.ChamferEnabled </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        CurveFinder.CoincidentVertex2dComponentEnabled </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        CurveFinder.CoincidentVertexEnabled </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        CurveFinder.CoincidentVertexSketchGroupEnabled </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        CurveFinder.Collinear2dComponentEnabled </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        CurveFinder.CollinearEnabled </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        CurveFinder.CollinearSketchGroupEnabled </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        CurveFinder.Concentric2dComponentEnabled </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        CurveFinder.ConcentricEnabled </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        CurveFinder.ConcentricSketchGroupEnabled </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        CurveFinder.EqualRadius2dComponentEnabled </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        CurveFinder.EqualRadiusEnabled </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        CurveFinder.EqualRadiusSketchGroupEnabled </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        CurveFinder.Offset2dComponentEnabled </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        CurveFinder.OffsetEnabled </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        CurveFinder.OffsetSketchGroupEnabled </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        CurveFinder.Parallel2dComponentEnabled </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        CurveFinder.ParallelEnabled </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        CurveFinder.ParallelSketchGroupEnabled </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        CurveFinder.SymmetricEnabled </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        CurveFinder.Tangent2dComponentEnabled </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        CurveFinder.TangentEnabled </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        CurveFinder.TangentSketchGroupEnabled </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        CurveFinder.UseCurveFinder </td> <td> 
         
        1 </td> </tr> 

        <tr><td> 
         
        CurveFinder.VertexOnCurve2dComponentEnabled </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        CurveFinder.VertexOnCurveEnabled </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        CurveFinder.VertexOnCurveSketchGroupEnabled </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        TransformMotion.DeltaEnum </td> <td> 
         
        ReferenceWcsWorkPart </td> </tr> 

        <tr><td> 
         
        TransformMotion.DeltaXc.Value </td> <td> 
         
        0.0 </td> </tr> 

        <tr><td> 
         
        TransformMotion.DeltaYc.Value </td> <td> 
         
        0.0 </td> </tr> 

        <tr><td> 
         
        TransformMotion.DeltaZc.Value </td> <td> 
         
        0.0 </td> </tr> 

        <tr><td> 
         
        TransformMotion.Option </td> <td> 
         
        Dynamic </td> </tr> 

        </table>  

         <br>  Created in NX9.0.0.  <br>  
        */
        class NXOPENCPP_FEATURESEXPORT  MoveCurveBuilder : public NXOpen::Features::FeatureBuilder
        {
            private: MoveCurveBuilderImpl * m_movecurvebuilder_impl;
            private: friend class  _MoveCurveBuilderBuilder;
            protected: MoveCurveBuilder();
            public: ~MoveCurveBuilder();
            /**Returns  the curve section 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::CurveFinderBuilder * CurveFinder
            (
            );
            /**Returns  the transform motion 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricUtilities::ModlMotion * TransformMotion
            (
            );
            /**Returns  the distance tolerance
                    
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: double DistanceTolerance
            (
            );
            /**Sets  the distance tolerance
                    
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR geometric_tol ("GDT") */
            public: void SetDistanceTolerance
            (
                double distanceTolerance /** distancetolerance */ 
            );
            /**Returns  a value that indicates which size option is selected
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: int SizeOption
            (
            );
            /**Sets  a value that indicates which size option is selected
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR geometric_tol ("GDT") */
            public: void SetSizeOption
            (
                int sizeOption /** sizeoption */ 
            );
            /**Returns  a value that indicates which keep tangent support is selected
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: int KeepTangent
            (
            );
            /**Sets  a value that indicates which keep tangent support is selected
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR geometric_tol ("GDT") */
            public: void SetKeepTangent
            (
                int keepTangent /** keeptangent */ 
            );
            /**Returns  a value that indicates whether keep orthogonal is enabled 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: bool KeepOrthogonal
            (
            );
            /**Sets  a value that indicates whether keep orthogonal is enabled 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR geometric_tol ("GDT") */
            public: void SetKeepOrthogonal
            (
                bool keepOrthogonal /** keeporthogonal */ 
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