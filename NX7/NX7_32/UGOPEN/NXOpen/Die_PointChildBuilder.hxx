#ifndef NXOpen_DIE_POINTCHILDBUILDER_HXX_INCLUDED
#define NXOpen_DIE_POINTCHILDBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Die_PointChildBuilder.ja
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
#include <NXOpen/Die.hxx>
#include <NXOpen/Features_FeatureBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Die
    {
        class PointChildBuilder;
    }
    namespace Features
    {
        class FeatureBuilder;
    }
    class Point;
    namespace Die
    {
        class _PointChildBuilderBuilder;
        /** Represents a Die Point Child sub feature.  <br> This sub feature is created via the main feature builder. <br> */
        class NXOPENCPPEXPORT PointChildBuilder : public Features::FeatureBuilder
        {
            private: friend class  _PointChildBuilderBuilder;
            protected: PointChildBuilder();
            /**Sets  the location of the point.  <br> License requirements : ug_die_design ("Die Design") */
            public: void SetPoint
            (
                NXOpen::Point * point /** point */ 
            );
            /**Returns  the location of the point.  <br> License requirements : ug_die_design ("Die Design") */
            public: NXOpen::Point * Point
            (
            );
            /**Sets  the design status of the point, if true the point will be built into the model, if false it will not.  <br> License requirements : ug_die_design ("Die Design") */
            public: void SetDesignStatus
            (
                bool designStatus /** design status */ 
            );
            /**Returns  the design status of the point, if true the point will be built into the model, if false it will not.  <br> License requirements : ug_die_design ("Die Design") */
            public: bool DesignStatus
            (
            );
            /**Returns  the build status of the point.  <br> License requirements : ug_die_design ("Die Design") */
            public: NXOpen::Die::DieBuildStatusOption BuildStatus
            (
            );
            /**Sets  the display status of the point, if true input data to the point will be displayed, 
                    if false the input data will not be displayed.  <br> License requirements : ug_die_design ("Die Design") */
            public: void SetDisplayStatus
            (
                bool displayStatus /** display status */ 
            );
            /**Returns  the display status of the point, if true input data to the point will be displayed, 
                    if false the input data will not be displayed.  <br> License requirements : ug_die_design ("Die Design") */
            public: bool DisplayStatus
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif