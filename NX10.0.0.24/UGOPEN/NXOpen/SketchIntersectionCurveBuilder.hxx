#ifndef NXOpen_SKETCHINTERSECTIONCURVEBUILDER_HXX_INCLUDED
#define NXOpen_SKETCHINTERSECTIONCURVEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     SketchIntersectionCurveBuilder.ja
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
#include <NXOpen/GeometricUtilities_CurveFitOptions.hxx>
#include <NXOpen/Features_FeatureBuilder.hxx>
#include <NXOpen/SketchIntersectionCurveBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    class SketchIntersectionCurveBuilder;
    namespace Features
    {
        class FeatureBuilder;
    }
    namespace GeometricUtilities
    {
        class CurveFitOptions;
    }
    class ScCollector;
    class _SketchIntersectionCurveBuilderBuilder;
    class SketchIntersectionCurveBuilderImpl;
    /** Represents a @link NXOpen::SketchIntersectionCurve NXOpen::SketchIntersectionCurve@endlink  builder  <br> To obtain an instance of this class use @link NXOpen::SketchCollection::CreateIntersectionCurveBuilder NXOpen::SketchCollection::CreateIntersectionCurveBuilder@endlink .  <br> 
    Default values.
    <table border="1"> 
     
    <tr><th> 
    Property</th>  <th> 
    Value</th> </tr>
    <tr><td> 
     
    CurveFitMethod.FitOption </td> <td> 
     
    Cubic </td> </tr> 

    <tr><td> 
     
    CurveFitMethod.MaximumDegree </td> <td> 
     
    7 </td> </tr> 

    <tr><td> 
     
    CurveFitMethod.MaximumSegments </td> <td> 
     
    1 </td> </tr> 

    </table>  

     <br>  Created in NX5.0.0.  <br>  
    */
    class NXOPENCPPEXPORT  SketchIntersectionCurveBuilder : public NXOpen::Features::FeatureBuilder
    {
        private: SketchIntersectionCurveBuilderImpl * m_sketchintersectioncurvebuilder_impl;
        private: friend class  _SketchIntersectionCurveBuilderBuilder;
        protected: SketchIntersectionCurveBuilder();
        public: ~SketchIntersectionCurveBuilder();
        /**Returns  the faces to intersect 
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::ScCollector * FaceCollector
        (
        );
        /** This method needs to be called whenever the number of faces to intersect changes
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : solid_modeling ("SOLIDS MODELING") OR geometric_tol ("GDT") */
        public: void CollectorUpdated
        (
        );
        /**Returns  the ignore holes option 
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : None */
        public: bool IgnoreHoles
        (
        );
        /**Sets  the ignore holes option 
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : solid_modeling ("SOLIDS MODELING") OR geometric_tol ("GDT") */
        public: void SetIgnoreHoles
        (
            bool ignoreHoles /** ignore holes */ 
        );
        /**Returns  the join curves option 
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : None */
        public: bool JoinCurves
        (
        );
        /**Sets  the join curves option 
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : solid_modeling ("SOLIDS MODELING") OR geometric_tol ("GDT") */
        public: void SetJoinCurves
        (
            bool joinCurves /** join curves */ 
        );
        /**Returns  the distance tolerance 
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : None */
        public: double DistanceTolerance
        (
        );
        /**Sets  the distance tolerance 
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : solid_modeling ("SOLIDS MODELING") OR geometric_tol ("GDT") */
        public: void SetDistanceTolerance
        (
            double distanceTolerance /** distance tolerance */ 
        );
        /**Returns  the angular tolerance 
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : None */
        public: double AngleTolerance
        (
        );
        /**Sets  the angular tolerance 
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : solid_modeling ("SOLIDS MODELING") OR geometric_tol ("GDT") */
        public: void SetAngleTolerance
        (
            double angleTolerance /** angle tolerance */ 
        );
        /** Method to get the alternate solution corresponding to solutionIndex
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : solid_modeling ("SOLIDS MODELING") OR geometric_tol ("GDT") */
        public: void AlternateSolution
        (
            int solutionIndex /** solutionindex */ 
        );
        /**Returns  the curve fit method 
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : solid_modeling ("SOLIDS MODELING") OR geometric_tol ("GDT") */
        public: NXOpen::GeometricUtilities::CurveFitOptions * CurveFitMethod
        (
        );
        /** This method needs to be called whenever the curve fit options changes 
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : solid_modeling ("SOLIDS MODELING") OR geometric_tol ("GDT") */
        public: void CurveFitMethodUpdated
        (
        );
    };
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