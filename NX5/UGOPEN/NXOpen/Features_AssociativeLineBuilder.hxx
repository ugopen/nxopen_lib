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
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/Expression.hxx>
#include <NXOpen/Features_FeatureBuilder.hxx>
#include <NXOpen/Features_AssociativeLineBuilder.hxx>
#include <NXOpen/GeometricUtilities_CurveLimitsData.hxx>
#include <NXOpen/GeometricUtilities_SupportPlaneData.hxx>
#include <NXOpen/SelectObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
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
    class SelectICurve;
    class SelectObject;
    class SelectPoint;
    namespace Features
    {
        class _AssociativeLineBuilderBuilder;
        /**
            Represents a @link Features::AssociativeLine Features::AssociativeLine@endlink  builder
             <br> To create a new instance of this class, use @link Features::BaseFeatureCollection::CreateAssociativeLineBuilder Features::BaseFeatureCollection::CreateAssociativeLineBuilder@endlink  <br> */
        class NXOPENCPPEXPORT AssociativeLineBuilder : public Features::FeatureBuilder
        {
            /** Represents start options type. */
            public: enum StartOption
            {
                StartOptionInferred/** Inferred */,
                StartOptionPoint/** Point */,
                StartOptionTangent/** Tangent */
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

            private: friend class  _AssociativeLineBuilderBuilder;
            protected: AssociativeLineBuilder();
            /**Returns  the start point options  <br> License requirements : None */
            public: NXOpen::Features::AssociativeLineBuilder::StartOption StartPointOptions
            (
            );
            /**Sets  the start point options  <br> License requirements : solid_modeling ("SOLIDS MODELING") OR drafting ("DRAFTING") */
            public: void SetStartPointOptions
            (
                NXOpen::Features::AssociativeLineBuilder::StartOption startPointOptions /** startpointoptions */ 
            );
            /**Returns  the start inferred constraint  <br> License requirements : None */
            public: NXOpen::SelectObject * StartInferredConstraint
            (
            );
            /**Returns  the start point reference  <br> License requirements : None */
            public: NXOpen::Features::AssociativeLineBuilder::StartReference StartPointReference
            (
            );
            /**Sets  the start point reference  <br> License requirements : solid_modeling ("SOLIDS MODELING") OR drafting ("DRAFTING") */
            public: void SetStartPointReference
            (
                NXOpen::Features::AssociativeLineBuilder::StartReference startPointReference /** startpointreference */ 
            );
            /**Returns  the start reference coordinate system  <br> License requirements : None */
            public: NXOpen::SelectCartesianCoordinateSystem * StartReferenceCsys
            (
            );
            /**Returns  the start point  <br> License requirements : None */
            public: NXOpen::SelectPoint * StartPoint
            (
            );
            /**Returns  the start tangent  <br> License requirements : None */
            public: NXOpen::SelectICurve * StartTangent
            (
            );
            /**Returns  the end point options  <br> License requirements : None */
            public: NXOpen::Features::AssociativeLineBuilder::EndOption EndPointOptions
            (
            );
            /**Sets  the end point options  <br> License requirements : solid_modeling ("SOLIDS MODELING") OR drafting ("DRAFTING") */
            public: void SetEndPointOptions
            (
                NXOpen::Features::AssociativeLineBuilder::EndOption endPointOptions /** endpointoptions */ 
            );
            /**Returns  the end inferred constraint  <br> License requirements : None */
            public: NXOpen::SelectObject * EndInferredConstraint
            (
            );
            /**Returns  the end point reference  <br> License requirements : None */
            public: NXOpen::Features::AssociativeLineBuilder::EndReference EndPointReference
            (
            );
            /**Sets  the end point reference  <br> License requirements : solid_modeling ("SOLIDS MODELING") OR drafting ("DRAFTING") */
            public: void SetEndPointReference
            (
                NXOpen::Features::AssociativeLineBuilder::EndReference endPointReference /** endpointreference */ 
            );
            /**Returns  the end reference coordinate system  <br> License requirements : None */
            public: NXOpen::SelectCartesianCoordinateSystem * EndReferenceCsys
            (
            );
            /**Returns  the end point  <br> License requirements : None */
            public: NXOpen::SelectPoint * EndPoint
            (
            );
            /**Returns  the end tangent  <br> License requirements : None */
            public: NXOpen::SelectICurve * EndTangent
            (
            );
            /**Returns  the at angle  <br> License requirements : None */
            public: NXOpen::SelectICurve * AtAngle
            (
            );
            /**Returns  the angle  <br> License requirements : None */
            public: NXOpen::Expression * Angle
            (
            );
            /**Returns  the end normal  <br> License requirements : None */
            public: NXOpen::SelectICurve * EndNormal
            (
            );
            /**Returns  the support plane data  <br> License requirements : None */
            public: NXOpen::GeometricUtilities::SupportPlaneData * SupportPlaneData
            (
            );
            /**Returns  the limits  <br> License requirements : None */
            public: NXOpen::GeometricUtilities::CurveLimitsData * Limits
            (
            );
            /**Returns  the associative  <br> License requirements : None */
            public: bool Associative
            (
            );
            /**Sets  the associative  <br> License requirements : solid_modeling ("SOLIDS MODELING") OR drafting ("DRAFTING") */
            public: void SetAssociative
            (
                bool associative /** associative */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
