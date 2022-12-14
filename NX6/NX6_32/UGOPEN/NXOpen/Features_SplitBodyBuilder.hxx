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
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/Features_FeatureBuilder.hxx>
#include <NXOpen/Features_SplitBodyBuilder.hxx>
#include <NXOpen/GeometricUtilities_BooleanToolBuilder.hxx>
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
    class SelectBodyList;
    namespace Features
    {
        class _SplitBodyBuilderBuilder;
        /**
            Represents a @link Features::SplitBody Features::SplitBody@endlink  builder
             <br> To create a new instance of this class, use @link Features::FeatureCollection::CreateSplitBodyBuilder Features::FeatureCollection::CreateSplitBodyBuilder@endlink  <br> 
        Default values:
        BooleanTool.ToolOption: FaceOrPlane
        */
        class NXOPENCPPEXPORT SplitBodyBuilder : public Features::FeatureBuilder
        {
            private: friend class  _SplitBodyBuilderBuilder;
            protected: SplitBodyBuilder();
            /**Returns  the target body to split. It can be a single
                      * solid/sheet body, or multiple solid/sheet bodies
                       <br> License requirements : None */
            public: NXOpen::SelectBodyList * TargetBody
            (
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
        };
    }
}
#undef EXPORTLIBRARY
#endif
