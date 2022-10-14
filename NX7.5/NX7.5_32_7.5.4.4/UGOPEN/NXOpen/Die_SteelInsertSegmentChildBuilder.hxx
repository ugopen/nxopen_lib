#ifndef NXOpen_DIE_STEELINSERTSEGMENTCHILDBUILDER_HXX_INCLUDED
#define NXOpen_DIE_STEELINSERTSEGMENTCHILDBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Die_SteelInsertSegmentChildBuilder.ja
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
#include <NXOpen/Die.hxx>
#include <NXOpen/Features_FeatureBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Die
    {
        class SteelInsertSegmentChildBuilder;
    }
    class Direction;
    class Expression;
    namespace Features
    {
        class FeatureBuilder;
    }
    class IOrientation;
    namespace Die
    {
        class _SteelInsertSegmentChildBuilderBuilder;
        class SteelInsertSegmentChildBuilderImpl;
        /** Represents a Steel Insert Segment Child sub feature.  <br> This sub feature is created via the main feature builder. <br> */
        class NXOPENCPPEXPORT  SteelInsertSegmentChildBuilder : public Features::FeatureBuilder
        {
            /** Settings for the insert type. */
            public: enum InsertTypeOption
            {
                InsertTypeOptionTrim/** trim */,
                InsertTypeOptionFlange/** flange */,
                InsertTypeOptionOffsetFlange/** offset_flange */
            };

            /** Settings for the extension type. */
            public: enum ExtensionTypeOption
            {
                ExtensionTypeOptionConstant/** constant */,
                ExtensionTypeOptionMaxdistPlusConst/** maximum distance + constant */,
                ExtensionTypeOptionLaw/** law */
            };

            private: SteelInsertSegmentChildBuilderImpl * m_steelinsertsegmentchildbuilder_impl;
            private: friend class  _SteelInsertSegmentChildBuilderBuilder;
            protected: SteelInsertSegmentChildBuilder();
            public: ~SteelInsertSegmentChildBuilder();
            /**Sets  the steel insert seg point or plane  <br> License requirements : ug_die_design ("Die Design") */
            public: void SetSegPoint
            (
                NXOpen::IOrientation * segPoint /** seg end point or plane */
            );
            /**Returns  the steel insert seg point or plane  <br> License requirements : ug_die_design ("Die Design") */
            public: NXOpen::IOrientation * SegPoint
            (
            );
            /**Sets  the steel insert seg directions  <br> License requirements : ug_die_design ("Die Design") */
            public: void SetSegDirection
            (
                NXOpen::Direction * segDirection /** seg direction */
            );
            /**Returns  the steel insert seg directions  <br> License requirements : ug_die_design ("Die Design") */
            public: NXOpen::Direction * SegDirection
            (
            );
            /**  <br> License requirements : ug_die_design ("Die Design") */
            public: void SetBeltThickness
            (
                const NXString & beltThickness /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /**Returns  the belt thickness  <br> License requirements : ug_die_design ("Die Design") */
            public: NXOpen::Expression * BeltThickness
            (
            );
            /**  <br> License requirements : ug_die_design ("Die Design") */
            public: void SetReliefAngle
            (
                const NXString & reliefAngle /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /**Returns  the relief angle  <br> License requirements : ug_die_design ("Die Design") */
            public: NXOpen::Expression * ReliefAngle
            (
            );
            /**  <br> License requirements : ug_die_design ("Die Design") */
            public: void SetProfileRelief
            (
                const NXString & profileRelief /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /**Returns  the profile relief  <br> License requirements : ug_die_design ("Die Design") */
            public: NXOpen::Expression * ProfileRelief
            (
            );
            /**  <br> License requirements : ug_die_design ("Die Design") */
            public: void SetExtensionDistance
            (
                const NXString & extensionDistance /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /**Returns  the extension distance  <br> License requirements : ug_die_design ("Die Design") */
            public: NXOpen::Expression * ExtensionDistance
            (
            );
            /**Sets  the insert type  <br> License requirements : ug_die_design ("Die Design") */
            public: void SetInsertType
            (
                NXOpen::Die::SteelInsertSegmentChildBuilder::InsertTypeOption insertType /** insert type */ 
            );
            /**Returns  the insert type  <br> License requirements : ug_die_design ("Die Design") */
            public: NXOpen::Die::SteelInsertSegmentChildBuilder::InsertTypeOption InsertType
            (
            );
            /**Sets  the extension type  <br> License requirements : ug_die_design ("Die Design") */
            public: void SetExtensionType
            (
                NXOpen::Die::SteelInsertSegmentChildBuilder::ExtensionTypeOption extensionType /** extension type */ 
            );
            /**Returns  the extension type  <br> License requirements : ug_die_design ("Die Design") */
            public: NXOpen::Die::SteelInsertSegmentChildBuilder::ExtensionTypeOption ExtensionType
            (
            );
            /**Sets  the profile relief toggle  <br> License requirements : ug_die_design ("Die Design") */
            public: void SetProfileReliefToggle
            (
                bool profileReliefToggle /** profile relief toggle */ 
            );
            /**Returns  the profile relief toggle  <br> License requirements : ug_die_design ("Die Design") */
            public: bool ProfileReliefToggle
            (
            );
            /**Sets  the design status of die sisegs  <br> License requirements : ug_die_design ("Die Design") */
            public: void SetDesignStatus
            (
                bool designStatus /** design status */ 
            );
            /**Returns  the design status of die sisegs  <br> License requirements : ug_die_design ("Die Design") */
            public: bool DesignStatus
            (
            );
            /**Returns  the build status of die sisegs  <br> License requirements : ug_die_design ("Die Design") */
            public: NXOpen::Die::DieBuildStatusOption BuildStatus
            (
            );
            /**Sets  the display status of die sisegs  <br> License requirements : ug_die_design ("Die Design") */
            public: void SetDisplayStatus
            (
                bool displayStatus /** display status */ 
            );
            /**Returns  the display status of die sisegs  <br> License requirements : ug_die_design ("Die Design") */
            public: bool DisplayStatus
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif