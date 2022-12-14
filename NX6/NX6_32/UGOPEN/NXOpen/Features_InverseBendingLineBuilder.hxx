#ifndef NXOpen_FEATURES_INVERSEBENDINGLINEBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_INVERSEBENDINGLINEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_InverseBendingLineBuilder.ja
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
#include <NXOpen/Features_FeatureBuilder.hxx>
#include <NXOpen/Features_InverseBendingLineBuilder.hxx>
#include <NXOpen/Features_TabNoteCfgBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Features
    {
        class InverseBendingLineBuilder;
    }
    namespace Features
    {
        class FeatureBuilder;
    }
    namespace Features
    {
        class TabNoteCfgBuilder;
    }
    namespace Features
    {
        class _InverseBendingLineBuilderBuilder;
        /**
            Represents a @link Features::InverseBendingLine Features::InverseBendingLine@endlink  builder
             <br> To create a new instance of this class, use @link Features::FeatureCollection::CreateInverseBendingLineBuilder Features::FeatureCollection::CreateInverseBendingLineBuilder@endlink  <br> */
        class NXOPENCPPEXPORT InverseBendingLineBuilder : public Features::FeatureBuilder
        {
            /** the bending line build method type. */
            public: enum Method
            {
                MethodAuto/** 0 : Auto */,
                MethodCurve/** 1 : Using curve quantity */,
                MethodFill/** 2 : Using filling coefficient */
            };

            private: friend class  _InverseBendingLineBuilderBuilder;
            protected: InverseBendingLineBuilder();
            /**Returns  the bending line build method.  <br> License requirements : None */
            public: NXOpen::Features::InverseBendingLineBuilder::Method BuildMethod
            (
            );
            /**Sets  the bending line build method.  <br> License requirements : nx_ship_concept ("Ship Concept") */
            public: void SetBuildMethod
            (
                NXOpen::Features::InverseBendingLineBuilder::Method buildMethod /** buildmethod */ 
            );
            /**Returns  the curve count  <br> License requirements : None */
            public: int CurveCount
            (
            );
            /**Sets  the curve count  <br> License requirements : nx_ship_concept ("Ship Concept") */
            public: void SetCurveCount
            (
                int curveCount /** curvecount */ 
            );
            /**Returns  the grid distance  <br> License requirements : None */
            public: double GridDistance
            (
            );
            /**Sets  the grid distance  <br> License requirements : nx_ship_concept ("Ship Concept") */
            public: void SetGridDistance
            (
                double gridDistance /** griddistance */ 
            );
            /**Returns  the filling coefficient  <br> License requirements : None */
            public: double FillingCoefficient
            (
            );
            /**Sets  the filling coefficient  <br> License requirements : nx_ship_concept ("Ship Concept") */
            public: void SetFillingCoefficient
            (
                double fillingCoefficient /** fillingcoefficient */ 
            );
            /**Returns  the nonlinear coefficient  <br> License requirements : None */
            public: double NlCoefficient
            (
            );
            /**Sets  the nonlinear coefficient  <br> License requirements : nx_ship_concept ("Ship Concept") */
            public: void SetNlCoefficient
            (
                double nlCoefficient /** nlcoefficient */ 
            );
            /**Returns  the tab note group  <br> License requirements : None */
            public: NXOpen::Features::TabNoteCfgBuilder * TabNoteGroup
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
