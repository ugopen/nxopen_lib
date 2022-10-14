#ifndef NXOpen_FEATURES_ASSOCIATIVELINEBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_ASSOCIATIVELINEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_AssociativeLineBuilder.ja
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
#include <NXOpen/Features_AssociativeLineBuilder.hxx>
#include <NXOpen/GeometricUtilities_CurveLimitsData.hxx>
#include <NXOpen/GeometricUtilities_SupportPlaneData.hxx>
#include <NXOpen/Features_FeatureBuilder.hxx>
#include <NXOpen/SelectObject.hxx>
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
        class AssociativeLineBuilder;
    }
    class Expression;
    namespace Features
    {
        class FeatureBuilder;
    }
    namespace GeometricUtilities
    {
        class CurveLimitsData;
    }
    namespace GeometricUtilities
    {
        class SupportPlaneData;
    }
    class SelectCartesianCoordinateSystem;
    class SelectDisplayableObject;
    class SelectICurve;
    class SelectObject;
    class SelectPoint;
    namespace Features
    {
        class _AssociativeLineBuilderBuilder;
        class AssociativeLineBuilderImpl;
        /**
            Represents a @link NXOpen::Features::AssociativeLine NXOpen::Features::AssociativeLine@endlink  builder
             <br> To create a new instance of this class, use @link NXOpen::Features::BaseFeatureCollection::CreateAssociativeLineBuilder  NXOpen::Features::BaseFeatureCollection::CreateAssociativeLineBuilder @endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        Associative </td> <td> 
         
        True </td> </tr> 

        <tr><td> 
         
        Limits.EndLimit.LimitOption </td> <td> 
         
        AtPoint </td> </tr> 

        <tr><td> 
         
        SupportPlaneData.SupportPlaneLockStatus </td> <td> 
         
        No </td> </tr> 

        </table>  

         <br>  Created in NX5.0.0.  <br>  
        */
        class NXOPENCPP_FEATURESEXPORT  AssociativeLineBuilder : public NXOpen::Features::FeatureBuilder
        {
            /** Represents start options type. */
            public: enum StartOption
            {
                StartOptionInferred/** Inferred */,
                StartOptionPoint/** Point */,
                StartOptionTangent/** Tangent */,
                StartOptionAtAngle/** At angle */,
                StartOptionAlongXc/** Along XC */,
                StartOptionAlongYc/** Along YC */,
                StartOptionAlongZc/** Along ZC */,
                StartOptionNormal/** Normal */
            };

            /** Represents references for start point */
            public: enum StartReference
            {
                StartReferenceWcs/** WCS */,
                StartReferenceAbsolute/** Absolute */,
                StartReferenceCordinatesSystem/** CSYS */
            };

            /** Represents end options type. */
            public: enum EndOption
            {
                EndOptionInferred/** Inferred */,
                EndOptionPoint/** Point */,
                EndOptionTangent/** Tangent */,
                EndOptionAtAngle/** At angle */,
                EndOptionAlongXc/** Along XC */,
                EndOptionAlongYc/** Along YC */,
                EndOptionAlongZc/** Along ZC */,
                EndOptionNormal/** Normal */
            };

            /** Represents references for end point */
            public: enum EndReference
            {
                EndReferenceWcs/** WCS */,
                EndReferenceAbsolute/** Absolute */,
                EndReferenceCordinatesSystem/** CSYS */
            };

            private: AssociativeLineBuilderImpl * m_associativelinebuilder_impl;
            private: friend class  _AssociativeLineBuilderBuilder;
            protected: AssociativeLineBuilder();
            public: ~AssociativeLineBuilder();
            /**Returns  the start point options 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::AssociativeLineBuilder::StartOption StartPointOptions
            (
            );
            /**Sets  the start point options 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR drafting ("DRAFTING") OR cam_base ("CAM BASE") */
            public: void SetStartPointOptions
            (
                NXOpen::Features::AssociativeLineBuilder::StartOption startPointOptions /** startpointoptions */ 
            );
            /**Returns  the start inferred constraint 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectObject * StartInferredConstraint
            (
            );
            /**Returns  the start point reference 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::AssociativeLineBuilder::StartReference StartPointReference
            (
            );
            /**Sets  the start point reference 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR drafting ("DRAFTING") OR cam_base ("CAM BASE") */
            public: void SetStartPointReference
            (
                NXOpen::Features::AssociativeLineBuilder::StartReference startPointReference /** startpointreference */ 
            );
            /**Returns  the start reference coordinate system 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectCartesianCoordinateSystem * StartReferenceCsys
            (
            );
            /**Returns  the start point 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectPoint * StartPoint
            (
            );
            /**Returns  the start tangent 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectICurve * StartTangent
            (
            );
            /**Returns  the start at angle 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectDisplayableObject * StartAtAngle
            (
            );
            /**Returns  the start angle 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * StartAngle
            (
            );
            /**Returns  the start normal 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectDisplayableObject * StartNormal
            (
            );
            /**Returns  the end point options 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::AssociativeLineBuilder::EndOption EndPointOptions
            (
            );
            /**Sets  the end point options 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR drafting ("DRAFTING") OR cam_base ("CAM BASE") */
            public: void SetEndPointOptions
            (
                NXOpen::Features::AssociativeLineBuilder::EndOption endPointOptions /** endpointoptions */ 
            );
            /**Returns  the end inferred constraint 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectObject * EndInferredConstraint
            (
            );
            /**Returns  the end point reference 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::AssociativeLineBuilder::EndReference EndPointReference
            (
            );
            /**Sets  the end point reference 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR drafting ("DRAFTING") OR cam_base ("CAM BASE") */
            public: void SetEndPointReference
            (
                NXOpen::Features::AssociativeLineBuilder::EndReference endPointReference /** endpointreference */ 
            );
            /**Returns  the end reference coordinate system 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectCartesianCoordinateSystem * EndReferenceCsys
            (
            );
            /**Returns  the end point 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectPoint * EndPoint
            (
            );
            /**Returns  the end tangent 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectICurve * EndTangent
            (
            );
            /**Returns  the end at angle 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectDisplayableObject * EndAtAngle
            (
            );
            /**Returns  the end angle 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * EndAngle
            (
            );
            /**Returns  the end normal 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectDisplayableObject * EndNormal
            (
            );
            /**Returns  the support plane data 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricUtilities::SupportPlaneData * SupportPlaneData
            (
            );
            /**Returns  the limits 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricUtilities::CurveLimitsData * Limits
            (
            );
            /**Returns  the associative 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: bool Associative
            (
            );
            /**Sets  the associative 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR drafting ("DRAFTING") OR cam_base ("CAM BASE") */
            public: void SetAssociative
            (
                bool associative /** associative */ 
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