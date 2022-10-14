#ifndef NXOpen_FEATURES_WAVEPOINTBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_WAVEPOINTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_WavePointBuilder.ja
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
#include <NXOpen/Features_WavePointBuilder.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Features
    {
        class WavePointBuilder;
    }
    namespace Features
    {
        class FeatureBuilder;
    }
    class SelectPointList;
    namespace Features
    {
        class _WavePointBuilderBuilder;
        /**
            Represents a @link Features::Feature Features::Feature@endlink  builder
             <br> To create a new instance of this class, use @link Features::FeatureCollection::CreateWavePointBuilder Features::FeatureCollection::CreateWavePointBuilder@endlink  <br> */
        class NXOPENCPPEXPORT WavePointBuilder : public Features::FeatureBuilder
        {
            private: friend class  _WavePointBuilderBuilder;
            protected: WavePointBuilder();
            /**Returns  the point to link  <br> License requirements : None */
            public: NXOpen::SelectPointList * Points
            (
            );
            /**Returns  the draw line  <br> License requirements : None */
            public: bool DrawLineBetweenPoints
            (
            );
            /**Sets  the draw line  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetDrawLineBetweenPoints
            (
                bool drawLine /** drawline */ 
            );
            /**Returns  the fix at timestamp  <br> License requirements : None */
            public: bool FixAtCurrentTimestamp
            (
            );
            /**Sets  the fix at timestamp  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetFixAtCurrentTimestamp
            (
                bool timestamp /** timestamp */ 
            );
            /**Returns  the associative  <br> License requirements : None */
            public: bool Associative
            (
            );
            /**Sets  the associative  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetAssociative
            (
                bool associative /** associative */ 
            );
            /**Returns  the makepositionindependent  <br> License requirements : None */
            public: bool MakePositionIndependent
            (
            );
            /**Sets  the makepositionindependent  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetMakePositionIndependent
            (
                bool makePositionIndependent /** makepositionindependent */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif