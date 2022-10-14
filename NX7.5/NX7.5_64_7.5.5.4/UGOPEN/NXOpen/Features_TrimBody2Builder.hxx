#ifndef NXOpen_FEATURES_TRIMBODY2BUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_TRIMBODY2BUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_TrimBody2Builder.ja
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
#include <NXOpen/Features_TrimBody2Builder.hxx>
#include <NXOpen/GeometricUtilities_BooleanToolBuilder.hxx>
#include <NXOpen/ScCollector.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Features
    {
        class TrimBody2Builder;
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
    namespace Features
    {
        class _TrimBody2BuilderBuilder;
        class TrimBody2BuilderImpl;
        /**
            Represents a @link Features::TrimBody2 Features::TrimBody2@endlink  builder for Trim Body
            feature. @link Features::TrimBody Features::TrimBody@endlink  and its builder 
            @link Features::TrimBodyBuilder Features::TrimBodyBuilder@endlink  are obsolete. Use 
            @link Features::TrimBody2 Features::TrimBody2@endlink  and this class instead.
             <br> To create a new instance of this class, use @link Features::FeatureCollection::CreateTrimBody2Builder Features::FeatureCollection::CreateTrimBody2Builder@endlink  <br> 
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
        class NXOPENCPPEXPORT  TrimBody2Builder : public Features::FeatureBuilder
        {
            private: TrimBody2BuilderImpl * m_trimbody2builder_impl;
            private: friend class  _TrimBody2BuilderBuilder;
            protected: TrimBody2Builder();
            public: ~TrimBody2Builder();
            /**Returns  the collector of target bodies to trim. It can be a single
                      * solid/sheet body, or multiple solid/sheet bodies
                       <br> License requirements : None */
            public: NXOpen::ScCollector * TargetBodyCollector
            (
            );
            /**Sets  the collector of target bodies to trim. It can be a single
                      * solid/sheet body, or multiple solid/sheet bodies
                       <br> License requirements : None */
            public: void SetTargetBodyCollector
            (
                NXOpen::ScCollector * targetBodyCollector /** targetbodycollector */ 
            );
            /**Returns  the tool bodies to trim the target body(s). The tool bodies are
                      * gotten through the BooleanTool Builder. Only tool options that can
                      * be set on @link TrimBody2Builder::BooleanTool TrimBody2Builder::BooleanTool @endlink and @link TrimBody2Builder::SetBooleanTool TrimBody2Builder::SetBooleanTool @endlink  are
                      * @link GeometricUtilities::BooleanToolBuilder::BooleanToolTypeFaceOrPlane GeometricUtilities::BooleanToolBuilder::BooleanToolTypeFaceOrPlane@endlink  or
                      * @link GeometricUtilities::BooleanToolBuilder::BooleanToolTypeNewPlane GeometricUtilities::BooleanToolBuilder::BooleanToolTypeNewPlane@endlink   <br> License requirements : None */
            public: NXOpen::GeometricUtilities::BooleanToolBuilder * BooleanTool
            (
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