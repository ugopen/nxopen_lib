#ifndef NXOpen_CAM_TURNENGAGERETRACTBUILDER_HXX_INCLUDED
#define NXOpen_CAM_TURNENGAGERETRACTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_TurnEngageRetractBuilder.ja
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
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAM
    {
        class TurnEngageRetractBuilder;
    }
    class Point;
    namespace CAM
    {
        class _TurnEngageRetractBuilderBuilder;
        class TurnEngageRetractBuilderImpl;
        /** Represents a first plunge Builder */
        class NXOPENCPPEXPORT  TurnEngageRetractBuilder : public TaggedObject
        {
            /** The engage retract type */
            public: enum Types
            {
                TypesAutoCircular/** Auto Circular */,
                TypesAutoLinear/** Auto Linear */,
                TypesDelta/** Delta */,
                TypesAngleAndDistance/** Angle and Distance */,
                TypesRelativeLinear/** Relative Linear */,
                TypesFromAPoint/** From a Point */,
                TypesTwoCircles/** Two Circles */,
                TypesTwoPointTangent/** Two Point Tangent */
            };

            /** The auto engage retract options */
            public: enum AutoOptions
            {
                AutoOptionsUserDefinedValues/** User Defined Values */,
                AutoOptionsAutomaticValues/** Automatic Values */,
                AutoOptionsClearWallsByAngleAndDistance/** Clear Walls by Angle and Distance */,
                AutoOptionsWithdraw/** Withdraw */,
                AutoOptionsWithdrawByDistance/** Withdraw by Distance */,
                AutoOptionsClearWalls/** Clear Walls*/,
                AutoOptionsClearWallsByDistance/** Clear Walls by Distance*/,
                AutoOptionsSameAsPlungeRetract/** Same as Plunge Retract*/
            };

            /** the extend method options */
            public: enum ExtendMethods
            {
                ExtendMethodsDistance/** Extend by distance */,
                ExtendMethodsToBlank/** Extend to blank */
            };

            private: TurnEngageRetractBuilderImpl * m_turnengageretractbuilder_impl;
            private: friend class  _TurnEngageRetractBuilderBuilder;
            protected: TurnEngageRetractBuilder();
            public: ~TurnEngageRetractBuilder();
            /**Returns  the Engage(Retract) Type  <br> License requirements : None */
            public: NXOpen::CAM::TurnEngageRetractBuilder::Types EngageRetractType
            (
            );
            /**Sets  the Engage(Retract) Type  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetEngageRetractType
            (
                NXOpen::CAM::TurnEngageRetractBuilder::Types engageRetractType /** the Engage(Retract) Type value */
            );
            /**Returns  the Auto Engage(Retract) Option  <br> License requirements : None */
            public: NXOpen::CAM::TurnEngageRetractBuilder::AutoOptions AutomaticOption
            (
            );
            /**Sets  the Auto Engage(Retract) Option  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetAutomaticOption
            (
                NXOpen::CAM::TurnEngageRetractBuilder::AutoOptions engageRetractOption /** the Auto Engage(Retract) Option value */
            );
            /**Returns  the Delta XC  <br> License requirements : None */
            public: double DeltaXc
            (
            );
            /**Sets  the Delta XC  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetDeltaXc
            (
                double xc /** the Delta XC value */
            );
            /**Returns  the Delta YC  <br> License requirements : None */
            public: double DeltaYc
            (
            );
            /**Sets  the Delta YC  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetDeltaYc
            (
                double yc /** the Delta YC value */
            );
            /**Returns  the Angle  <br> License requirements : None */
            public: double Angle
            (
            );
            /**Sets  the Angle  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetAngle
            (
                double angle /** the Angle value */
            );
            /**Returns  the Radius  <br> License requirements : None */
            public: double Radius
            (
            );
            /**Sets  the Radius  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetRadius
            (
                double radius /** the Radius value */
            );
            /**Returns  the Distance  <br> License requirements : None */
            public: double Distance
            (
            );
            /**Sets  the Distance  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetDistance
            (
                double distance /** the Distance value */
            );
            /**Returns  the point  <br> License requirements : None */
            public: NXOpen::Point * Point
            (
            );
            /**Sets  the point  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetPoint
            (
                NXOpen::Point * turnPoint /** the point value */
            );
            /**Returns  the Extend Method  <br> License requirements : None */
            public: NXOpen::CAM::TurnEngageRetractBuilder::ExtendMethods ExtendMethod
            (
            );
            /**Sets  the Extend Method  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetExtendMethod
            (
                NXOpen::CAM::TurnEngageRetractBuilder::ExtendMethods newValue /** the Extend Method value */
            );
            /**Returns  the Extend Distance  <br> License requirements : None */
            public: double ExtendDistance
            (
            );
            /**Sets  the Extend Distance  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetExtendDistance
            (
                double extendDistance /** the Extend Distance value */
            );
            /**Returns  the Direct engage to(retract from) trim point  <br> License requirements : None */
            public: bool DirectTrimPoint
            (
            );
            /**Sets  the Direct engage to(retract from) trim point  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetDirectTrimPoint
            (
                bool directTrimPoint /** the Direct engage to(retract from) trim point */
            );
            /**Returns  the First Radius  <br> License requirements : None */
            public: double FirstRadius
            (
            );
            /**Sets  the First Radius  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetFirstRadius
            (
                double firstRadius /** the First Radius value */
            );
            /**Returns  the Second Radius  <br> License requirements : None */
            public: double SecondRadius
            (
            );
            /**Sets  the Second Radius  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetSecondRadius
            (
                double secondRadius /** the Second Radius value */
            );
            /**Returns  the Safe Distance  <br> License requirements : None */
            public: double SafeDistance
            (
            );
            /**Sets  the Safe Distance  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetSafeDistance
            (
                double safeDistance /** the Safe Distance value */
            );
            /**Returns  the Tangential Extension  <br> License requirements : None */
            public: bool TangentialExtension
            (
            );
            /**Sets  the Tangential Extension  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetTangentialExtension
            (
                bool tangentialExtension /** the Tangential Extension */
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
