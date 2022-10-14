#ifndef NXOpen_FEATURES_ASSEMBLYCUTBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_ASSEMBLYCUTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_AssemblyCutBuilder.ja
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
#include <NXOpen/Features_AssemblyCutBuilder.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Features
    {
        class AssemblyCutBuilder;
    }
    namespace Features
    {
        class FeatureBuilder;
    }
    class SelectBodyList;
    namespace Features
    {
        class _AssemblyCutBuilderBuilder;
        /**
            Represents a @link Features::AssemblyCut Features::AssemblyCut@endlink  builder
             <br> To create a new instance of this class, use @link Features::FeatureCollection::CreateAssemblyCutBuilder Features::FeatureCollection::CreateAssemblyCutBuilder@endlink  <br> 
        Default values:
        HideToolBodyFlag: 1
        */
        class NXOPENCPPEXPORT AssemblyCutBuilder : public Features::FeatureBuilder
        {
            private: friend class  _AssemblyCutBuilderBuilder;
            protected: AssemblyCutBuilder();
            /**Returns  the target body  <br> License requirements : None */
            public: NXOpen::SelectBodyList * TargetBody
            (
            );
            /**Returns  the tool body  <br> License requirements : None */
            public: NXOpen::SelectBodyList * ToolBody
            (
            );
            /**Returns  the hide tool body flag  <br> License requirements : None */
            public: bool HideToolBodyFlag
            (
            );
            /**Sets  the hide tool body flag  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetHideToolBodyFlag
            (
                bool hideToolBodyFlag /** hidetoolbodyflag */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif