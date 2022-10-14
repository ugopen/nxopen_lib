#ifndef NXOpen_GEOMETRICUTILITIES_CIRCULARFRAMEBUILDER_HXX_INCLUDED
#define NXOpen_GEOMETRICUTILITIES_CIRCULARFRAMEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     GeometricUtilities_CircularFrameBuilder.ja
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
#include <NXOpen/GeometricUtilities_CircularFrameBuilder.hxx>
#include <NXOpen/GeometricUtilities_ShapeFrameBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace GeometricUtilities
    {
        class CircularFrameBuilder;
    }
    namespace GeometricUtilities
    {
        class ShapeFrameBuilder;
    }
    namespace GeometricUtilities
    {
        class _CircularFrameBuilderBuilder;
        class CircularFrameBuilderImpl;
        /**
            Represents a @link GeometricUtilities::CircularFrameBuilder GeometricUtilities::CircularFrameBuilder@endlink 
            */
        class NXOPENCPPEXPORT  CircularFrameBuilder : public GeometricUtilities::ShapeFrameBuilder
        {
            /** Represents the circular frame subtypes */
            public: enum Subtypes
            {
                SubtypesArbitrary/** Arbitrary circle */,
                SubtypesHalf/** Half circle */,
                SubtypesQuarter/** Quarter circle */,
                SubtypesFull/** Full circle */
            };

            private: CircularFrameBuilderImpl * m_circularframebuilder_impl;
            private: friend class  _CircularFrameBuilderBuilder;
            protected: CircularFrameBuilder();
            public: ~CircularFrameBuilder();
            /**Returns  the subtype  <br> License requirements : None */
            public: NXOpen::GeometricUtilities::CircularFrameBuilder::Subtypes Subtype
            (
            );
            /**Sets  the subtype  <br> License requirements : None */
            public: void SetSubtype
            (
                NXOpen::GeometricUtilities::CircularFrameBuilder::Subtypes subtype /** subtype */ 
            );
            /** Gets the i-th radius of the circular frame  @return  radius  <br> License requirements : None */
            public: double GetRadius
            (
                int index /** index of radius */
            );
            /** Sets the i-th radius of the circular frame  <br> License requirements : None */
            public: void SetRadius
            (
                int index /** index of radius */,
                double radius /** radius */
            );
            /** Gets the i-th angle of the circular frame  @return  angle  <br> License requirements : None */
            public: double GetAngle
            (
                int index /** index of angle */
            );
            /** Sets the i-th angle of the circular frame  <br> License requirements : None */
            public: void SetAngle
            (
                int index /** index of angle */,
                double angle /** angle */
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif