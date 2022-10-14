#ifndef NXOpen_FEATURES_DRAFTBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_DRAFTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_DraftBuilder.ja
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
#include <NXOpen/Features_FeatureBuilder.hxx>
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
        class DraftBuilder;
    }
    class Direction;
    class ExpressionCollectorSetList;
    namespace Features
    {
        class FeatureBuilder;
    }
    namespace GeometricUtilities
    {
        class DraftVariableAngleData;
    }
    namespace GeometricUtilities
    {
        class TwoExpressionsCollectorSetList;
    }
    class NXObject;
    class ScCollector;
    namespace Features
    {
        class _DraftBuilderBuilder;
        class DraftBuilderImpl;
        /** Represents a Draft Feature Builder that creates or edits a draft (Old name Taper) feature.
             <br> 
            This class provides methods to set and get various Draft feature parameters and input entities.
             <br> 

             <br> 
            Following are default values and options.
             <br> 
             <br> 
            <b> Direction </b> Z direction
             <br> 
             <br> 
            <b> Draft method </b> @link  Features::DraftBuilder::MethodIsocline   Features::DraftBuilder::MethodIsocline @endlink 
             <br> 
             <br> 
            <b> Draft All instances </b> true
             <br> 
             <br> 
            <b> Angle tolerance </b> 0.002/0.1 [rad/deg]
             <br> 
             <br> 
            <b> Distance tolerance </b> 0.004/0.1 [in/mm]
             <br> 
             <br> To create a new instance of this class, use @link Features::FeatureCollection::CreateDraftBuilder  Features::FeatureCollection::CreateDraftBuilder @endlink  <br> 
         <br>  Created in NX4.0.0.  <br>  
        */
        class NXOPENCPP_FEATURESEXPORT  DraftBuilder : public Features::FeatureBuilder
        {
            /** Describes the Draft type as true draft or isocline draft.
                   */
            public: enum Method
            {
                MethodIsocline/** Indicates use of isocline algorithm to create draft. Default value. */,
                MethodTrueDraft/** Indicates use of true draft algorithm to create draft.*/
            };

            /** Describes the different Draft types
                   */
            public: enum Type
            {
                TypeFace/** Face Draft type */,
                TypeEdge/** From Edges type */,
                TypeTangent/** Tangent Draft type */,
                TypePartingEdge/** Draft with Parting Edges type */
            };

            /** Describes the different Draft Methods in Draft References
                   */
            public: enum DraftReferencesMethods
            {
                DraftReferencesMethodsStationaryFace/** Draft from stationary face. */,
                DraftReferencesMethodsPartingFace/** Draft from stationary parting face. */,
                DraftReferencesMethodsStationaryAndPartingFace/** Draft from stationary face to parting face. */
            };

            private: DraftBuilderImpl * m_draftbuilder_impl;
            private: friend class  _DraftBuilderBuilder;
            protected: DraftBuilder();
            public: ~DraftBuilder();
            /**Sets  the smart direction for draft
                   
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetDirection
            (
                NXOpen::Direction * direction /** direction */ 
            );
            /**Returns  the smart direction for draft
                   
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: NXOpen::Direction * Direction
            (
            );
            /**Sets  the stationary entity for draft.
                   
             <br>  @deprecated Deprecated in NX8.5.0.  Use @link Features::DraftBuilder::StationaryReference Features::DraftBuilder::StationaryReference@endlink  instead.  Note that this API cannot be used together with the new API. <br>  

             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public:  NX_DEPRECATED("Deprecated in NX8.5.0.  Use Features::DraftBuilder::StationaryReference instead.  Note that this API cannot be used together with the new API.") void SetStationaryEntity
            (
                NXOpen::NXObject * stationaryEntity /** stationary entity */ 
            );
            /**Returns  the stationary entity for draft.
                   
             <br>  @deprecated Deprecated in NX8.5.0.  Use @link Features::DraftBuilder::StationaryReference Features::DraftBuilder::StationaryReference@endlink  instead.  Note that this API cannot be used together with the new API. <br>  

             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public:  NX_DEPRECATED("Deprecated in NX8.5.0.  Use Features::DraftBuilder::StationaryReference instead.  Note that this API cannot be used together with the new API.") NXOpen::NXObject * StationaryEntity
            (
            );
            /**Returns  the list of draft faces SC Collectors and corresponding draft angles.
                       <br> 
                      If the Draft is From Plane or Surface, use @link Features::DraftBuilder::TwoDimensionFaceSetsData Features::DraftBuilder::TwoDimensionFaceSetsData@endlink  instead.
                       <br> 
                   
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: NXOpen::ExpressionCollectorSetList * FaceSetAngleExpressionList
            (
            );
            /**Returns  the list of draft edges SC Collectors and corresponding draft angles.
                   
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: NXOpen::ExpressionCollectorSetList * EdgeSetAngleExpressionList
            (
            );
            /**Returns  the Data object for Variable Angle Draft
                   
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: NXOpen::GeometricUtilities::DraftVariableAngleData * VariableAngleData
            (
            );
            /**Sets  the option "Draft all instances" [true/false]
                   
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetDraftAllInstances
            (
                bool draftAllInstances /** draft all instances */ 
            );
            /**Returns  the option "Draft all instances" [true/false]
                   
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: bool DraftAllInstances
            (
            );
            /**Sets  the distance tolerance in [in/mm]
                   
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetDistanceTolerance
            (
                double distanceTolerance /** distance tolerance */ 
            );
            /**Returns  the distance tolerance in [in/mm]
                   
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: double DistanceTolerance
            (
            );
            /**Sets  the angle tolerance in [rad/deg]
                   
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetAngleTolerance
            (
                double angleTolerance /** angle tolerance */ 
            );
            /**Returns  the angle tolerance in [rad/deg]
                   
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: double AngleTolerance
            (
            );
            /**Sets  the Draft method
                   
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetDraftIsoclineOrTruedraft
            (
                NXOpen::Features::DraftBuilder::Method draftMethod /** draft method */ 
            );
            /**Returns  the Draft method
                   
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: NXOpen::Features::DraftBuilder::Method DraftIsoclineOrTruedraft
            (
            );
            /**Sets  the Draft type
                   
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetTypeOfDraft
            (
                NXOpen::Features::DraftBuilder::Type type /** type */ 
            );
            /**Returns  the Draft type
                   
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: NXOpen::Features::DraftBuilder::Type TypeOfDraft
            (
            );
            /** Sets the Variable Angle option
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetVariableAngleOption
            (
            );
            /**Returns  the stationary reference as SC Collector containing only faces or only one datum plane or only one point 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::ScCollector * StationaryReference
            (
            );
            /**Returns  the stationary parting reference as SC Collector containing only faces or only one datum plane or only one point
                  Note that DraftBuilder.StationaryPartingReference and DraftBuilder.PartingReference refer to the same collector. 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::ScCollector * StationaryPartingReference
            (
            );
            /**Returns  the parting reference as SC Collector containing only faces or only one datum plane or only one point.
                  Note that DraftBuilder.StationaryPartingReference and DraftBuilder.PartingReference refer to the same collector. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::ScCollector * PartingReference
            (
            );
            /**Returns  the draft references method 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::DraftBuilder::DraftReferencesMethods DraftReferencesMethod
            (
            );
            /**Sets  the draft references method 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetDraftReferencesMethod
            (
                NXOpen::Features::DraftBuilder::DraftReferencesMethods draftReferencesMethod /** draft references method */ 
            );
            /**Returns  whether to draft on both sides of the reference 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: bool DraftBothSides
            (
            );
            /**Sets  whether to draft on both sides of the reference 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetDraftBothSides
            (
                bool draftBothSides /** draft both sides */ 
            );
            /**Returns  whether draft angles on both sides of the parting reference are symmetric 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: bool SymmetricAngle
            (
            );
            /**Sets  whether draft angles on both sides of the parting reference are symmetric 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetSymmetricAngle
            (
                bool symmetricAngle /** symmetric angle */ 
            );
            /**Returns  the list of draft faces SC Collectors and corresponding draft angles above and below the parting reference.
                   
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricUtilities::TwoExpressionsCollectorSetList * TwoDimensionFaceSetsData
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