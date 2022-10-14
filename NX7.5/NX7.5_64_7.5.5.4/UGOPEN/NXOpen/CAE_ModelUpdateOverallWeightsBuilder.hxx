#ifndef NXOpen_CAE_MODELUPDATEOVERALLWEIGHTSBUILDER_HXX_INCLUDED
#define NXOpen_CAE_MODELUPDATEOVERALLWEIGHTSBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_ModelUpdateOverallWeightsBuilder.ja
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
#include <NXOpen/Builder.hxx>
#include <NXOpen/CAE_ModelUpdateOverallWeightsBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAE
    {
        class ModelUpdateOverallWeightsBuilder;
    }
    class Builder;
    namespace CAE
    {
        class _ModelUpdateOverallWeightsBuilderBuilder;
        class ModelUpdateOverallWeightsBuilderImpl;
        /** Represents a @link CAE::ModelUpdateOverallWeightsBuilder CAE::ModelUpdateOverallWeightsBuilder@endlink   <br> To create a new instance of this class, use @link CAE::ModelUpdateSolution::CreateOverallWeightsBuilder CAE::ModelUpdateSolution::CreateOverallWeightsBuilder@endlink  <br> */
        class NXOPENCPPEXPORT  ModelUpdateOverallWeightsBuilder : public Builder
        {
            private: ModelUpdateOverallWeightsBuilderImpl * m_modelupdateoverallweightsbuilder_impl;
            private: friend class  _ModelUpdateOverallWeightsBuilderBuilder;
            protected: ModelUpdateOverallWeightsBuilder();
            public: ~ModelUpdateOverallWeightsBuilder();
            /**Returns  the overall weights of frequency targets  <br> License requirements : None */
            public: double Frequencies
            (
            );
            /**Sets  the overall weights of frequency targets  <br> License requirements : nx_correl_update ("FE Model Update") */
            public: void SetFrequencies
            (
                double frequencies /** frequencies */ 
            );
            /**Returns  the overall weights of mode shape targets  <br> License requirements : None */
            public: double ModeShapes
            (
            );
            /**Sets  the overall weights of mode shape targets  <br> License requirements : nx_correl_update ("FE Model Update") */
            public: void SetModeShapes
            (
                double modeShapes /** modeshapes */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif