#ifndef NXOpen_FEATURES_SPLITBODYBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_SPLITBODYBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_SplitBodyBuilder.ja
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
#include <NXOpen/Features_SplitBodyBuilder.hxx>
#include <NXOpen/GeometricUtilities_BooleanToolBuilder.hxx>
#include <NXOpen/ScCollector.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Features
    {
        class SplitBodyBuilder;
    }
    namespace Features
    {
        class FeatureBuilder;
    }
    namespace GeometricUtilities
    {
        class BooleanToolBuilder;
    }
    class ScCollector;
    class SelectBodyList;
    namespace Features
    {
        class _SplitBodyBuilderBuilder;
        class SplitBodyBuilderImpl;
        /**
            Represents a @link Features::SplitBody Features::SplitBody@endlink  builder
             <br> To create a new instance of this class, use @link Features::FeatureCollection::CreateSplitBodyBuilderUsingCollector Features::FeatureCollection::CreateSplitBodyBuilderUsingCollector@endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        BooleanTool.ToolOption </td> <td> 
         
        FaceOrPlane </td> </tr> 

        </table>  
        */
        class NXOPENCPPEXPORT  SplitBodyBuilder : public Features::FeatureBuilder
        {
            private: SplitBodyBuilderImpl * m_splitbodybuilder_impl;
            private: friend class  _SplitBodyBuilderBuilder;
            protected: SplitBodyBuilder();
            public: ~SplitBodyBuilder();
            /**Returns  the target body to split. It can be a single
                      * solid/sheet body, or multiple solid/sheet bodies
                       <br> License requirements : None */
            public: NXOpen::SelectBodyList * TargetBody
            (
            );
            /**Returns  the collector of target bodies to split. It can be a single
                      * solid/sheet body, or multiple solid/sheet bodies
                       <br> License requirements : None */
            public: NXOpen::ScCollector * TargetBodyCollector
            (
            );
            /**Sets  the collector of target bodies to split. It can be a single
                      * solid/sheet body, or multiple solid/sheet bodies
                       <br> License requirements : None */
            public: void SetTargetBodyCollector
            (
                NXOpen::ScCollector * toolBodyCollector /** toolbodycollector */ 
            );
            /**Returns  the tool bodies to split the target body(s). The tool bodies are
                      * gotten through the BooleanTool Builder <br> License requirements : None */
            public: NXOpen::GeometricUtilities::BooleanToolBuilder * BooleanTool
            (
            );
            /**Returns  the keep imprinted edges option  <br> License requirements : None */
            public: bool KeepImprintedEdges
            (
            );
            /**Sets  the keep imprinted edges option  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetKeepImprintedEdges
            (
                bool keepImprintedEdges /** keepimprintededges */ 
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