#ifndef NXOpen_FEATURES_THICKENBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_THICKENBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_ThickenBuilder.ja
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
#include <NXOpen/Features_ThickenBuilder.hxx>
#include <NXOpen/GeometricUtilities_BooleanOperation.hxx>
#include <NXOpen/ScCollector.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Features
    {
        class ThickenBuilder;
    }
    class Expression;
    namespace Features
    {
        class FeatureBuilder;
    }
    namespace GeometricUtilities
    {
        class BooleanOperation;
    }
    class ScCollector;
    namespace Features
    {
        class _ThickenBuilderBuilder;
        /**
            Represents a builder for a @link Features::Thicken Features::Thicken@endlink  feature. This allows creation and editing of a Thicken feature which takes a set of faces and offsets them along their normals to create a solid body which has constant thickness. Since this can not be done precisely for the supported geometry types there is a tolerance to specify the accuracy of the result.
             <br> To create a new instance of this class, use @link Features::FeatureCollection::CreateThickenBuilder Features::FeatureCollection::CreateThickenBuilder@endlink  <br> 
        Default values:
        ApproximateOffset: False
        BooleanOperation.Type: Create
        FirstOffset.RightHandSide: 2.5 (millimeters part), 0.1 (inches part)
        ReverseDirection: False
        SecondOffset.RightHandSide: 0.0 (millimeters part), 0.0 (inches part)
        */
        class NXOPENCPPEXPORT ThickenBuilder : public Features::FeatureBuilder
        {
            private: friend class  _ThickenBuilderBuilder;
            protected: ThickenBuilder();
            /**Returns  the faces to thicken.
                    A list of one or more faces to thicken.  <br> License requirements : None */
            public: NXOpen::ScCollector * FaceCollector
            (
            );
            /**Returns  the first offset.
                    The first offset for the Thicken feature.
                    A positive value is applied along the normal of the face to be thickened.
                    Negative values are applied in the opposite direction.
                    The difference between the first and second offset must be non-zero.  <br> License requirements : None */
            public: NXOpen::Expression * FirstOffset
            (
            );
            /**Returns  the reverse direction.
                    A flag to indicate whether the offset direction is reversed with respect to the normal of the face to be thickened.  <br> License requirements : None */
            public: bool ReverseDirection
            (
            );
            /**Sets  the reverse direction.
                    A flag to indicate whether the offset direction is reversed with respect to the normal of the face to be thickened.  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetReverseDirection
            (
                bool reverseDirection /** reversedirection */ 
            );
            /**Returns  the second offset.
                    the second offset for the Thicken feature.  <br> License requirements : None */
            public: NXOpen::Expression * SecondOffset
            (
            );
            /**Returns  the boolean operation.
                    The boolean operation associated with the Thicken feature  <br> License requirements : None */
            public: NXOpen::GeometricUtilities::BooleanOperation * BooleanOperation
            (
            );
            /**Returns  the approximate offset surface option.
                    The option to approximate offset surfaces for thickening operation.  <br> License requirements : None */
            public: bool ApproximateOffset
            (
            );
            /**Sets  the approximate offset surface option.
                    The option to approximate offset surfaces for thickening operation.  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetApproximateOffset
            (
                bool approximateOffset /** approximateoffset */ 
            );
            /**Returns  the tolerance.
                    The maximum allowable distance between the true theoretical sheet and the body created to approximate it.  <br> License requirements : None */
            public: double Tolerance
            (
            );
            /**Sets  the tolerance.
                    The maximum allowable distance between the true theoretical sheet and the body created to approximate it.  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetTolerance
            (
                double tolerance /** tolerance */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
