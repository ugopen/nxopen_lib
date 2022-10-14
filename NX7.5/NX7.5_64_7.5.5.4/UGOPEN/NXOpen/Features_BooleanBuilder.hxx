#ifndef NXOpen_FEATURES_BOOLEANBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_BOOLEANBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_BooleanBuilder.ja
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
#include <NXOpen/Features_BooleanBuilder.hxx>
#include <NXOpen/Features_Feature.hxx>
#include <NXOpen/ScCollector.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Features
    {
        class BooleanBuilder;
    }
    class Body;
    class DisplayableObject;
    namespace Features
    {
        class FeatureBuilder;
    }
    class ScCollector;
    class SelectBodyList;
    class SelectDisplayableObjectList;
    namespace Features
    {
        class _BooleanBuilderBuilder;
        class BooleanBuilderImpl;
        /** Represents a boolean feature builder.
             <br> To create a new instance of this class, use @link Features::FeatureCollection::CreateBooleanBuilderUsingCollector Features::FeatureCollection::CreateBooleanBuilderUsingCollector@endlink  <br> */
        class NXOPENCPPEXPORT  BooleanBuilder : public Features::FeatureBuilder
        {
            private: BooleanBuilderImpl * m_booleanbuilder_impl;
            private: friend class  _BooleanBuilderBuilder;
            protected: BooleanBuilder();
            public: ~BooleanBuilder();
            /**Returns  the boolean operation  <br> License requirements : None */
            public: NXOpen::Features::Feature::BooleanType Operation
            (
            );
            /**Returns  the target body  <br> License requirements : None */
            public: NXOpen::Body * Target
            (
            );
            /**Returns  the tool body 
             @deprecated Deprecated in NX5.0.2 <br> 
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX5.0.2") NXOpen::DisplayableObject * Tool
            (
            );
            /**Returns  the retain target flag  <br> License requirements : None */
            public: bool RetainTarget
            (
            );
            /**Returns  the retain tool flag  <br> License requirements : None */
            public: bool RetainTool
            (
            );
            /**Sets  the boolean operation  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetOperation
            (
                NXOpen::Features::Feature::BooleanType operation /** Type of boolean operation. */
            );
            /**Sets  the target body  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetTarget
            (
                NXOpen::Body * target /** Target body for boolean operation. This parameter may not be NULL.*/
            );
            /**Sets  the tool body 
             @deprecated Deprecated in NX5.0.2 <br> 
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public:  NX_DEPRECATED("Deprecated in NX5.0.2") void SetTool
            (
                NXOpen::DisplayableObject * tool /** Tool body for boolean operation. This parameter may not be NULL.*/
            );
            /**Sets  the retain target flag  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetRetainTarget
            (
                bool retainTarget /** Retain target flag */
            );
            /**Sets  the retain tool flag  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetRetainTool
            (
                bool retainTool /** Retain tool flag */
            );
            /**Returns  the target bodies for the boolean operation  <br> License requirements : None */
            public: NXOpen::SelectBodyList * Targets
            (
            );
            /**Returns  the tool bodies for the boolean operation  <br> License requirements : None */
            public: NXOpen::SelectDisplayableObjectList * Tools
            (
            );
            /**Returns  the tool body collector for the boolean operation  <br> License requirements : None */
            public: NXOpen::ScCollector * ToolBodyCollector
            (
            );
            /**Sets  the tool body collector for the boolean operation  <br> License requirements : None */
            public: void SetToolBodyCollector
            (
                NXOpen::ScCollector * toolBodyCollector /** toolbodycollector */ 
            );
            /**Returns  the copy targets flag  <br> License requirements : None */
            public: bool CopyTargets
            (
            );
            /**Sets  the copy targets flag  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetCopyTargets
            (
                bool copyTargets /** copytargets */ 
            );
            /**Returns  the copy tools flag  <br> License requirements : None */
            public: bool CopyTools
            (
            );
            /**Sets  the copy tools flag  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetCopyTools
            (
                bool copyTools /** copytools */ 
            );
            /**Returns  the convert to sew flag  <br> License requirements : None */
            public: bool ConvertToSew
            (
            );
            /**Sets  the convert to sew flag  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetConvertToSew
            (
                bool convertToSew /** converttosew */ 
            );
            /**Returns  the tolerance  <br> License requirements : None */
            public: double Tolerance
            (
            );
            /**Sets  the tolerance  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetTolerance
            (
                double tolerance /** tolerance */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif