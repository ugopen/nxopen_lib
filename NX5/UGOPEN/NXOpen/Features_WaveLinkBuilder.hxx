#ifndef NXOpen_FEATURES_WAVELINKBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_WAVELINKBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_WaveLinkBuilder.ja
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
#include <NXOpen/Features_CompositeCurveBuilder.hxx>
#include <NXOpen/Features_ExtractFaceBuilder.hxx>
#include <NXOpen/Features_MirrorBodyBuilder.hxx>
#include <NXOpen/Features_WaveDatumBuilder.hxx>
#include <NXOpen/Features_WaveLinkBuilder.hxx>
#include <NXOpen/Features_WavePointBuilder.hxx>
#include <NXOpen/Features_WaveRoutingBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Features
    {
        class WaveLinkBuilder;
    }
    namespace Features
    {
        class CompositeCurveBuilder;
    }
    namespace Features
    {
        class ExtractFaceBuilder;
    }
    namespace Features
    {
        class FeatureBuilder;
    }
    namespace Features
    {
        class MirrorBodyBuilder;
    }
    namespace Features
    {
        class WaveDatumBuilder;
    }
    namespace Features
    {
        class WavePointBuilder;
    }
    namespace Features
    {
        class WaveRoutingBuilder;
    }
    namespace Features
    {
        class _WaveLinkBuilderBuilder;
        /**
            Represents a Wavelink Feature builder
             <br> To create a new instance of this class, use @link Features::BaseFeatureCollection::CreateWaveLinkBuilder Features::BaseFeatureCollection::CreateWaveLinkBuilder@endlink  <br> */
        class NXOPENCPPEXPORT WaveLinkBuilder : public Features::FeatureBuilder
        {

            public: enum Types
            {
                TypesCurveLink/** curve link */ ,
                TypesPointLink/** point link */ ,
                TypesDatumLink/** datum link */ ,
                TypesFaceLink/** face link */ ,
                TypesRegionLink/** region link */ ,
                TypesBodyLink/** body link */ ,
                TypesMirrorBodyLink/** mirror body link */ ,
                TypesRoutingObjectLink/** routing object link */ 
            };

            private: friend class  _WaveLinkBuilderBuilder;
            protected: WaveLinkBuilder();
            /**Returns  the type  <br> License requirements : None */
            public: NXOpen::Features::WaveLinkBuilder::Types Type
            (
            );
            /**Sets  the type  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetType
            (
                NXOpen::Features::WaveLinkBuilder::Types type /** type */ 
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
            /**Returns  the blank original  <br> License requirements : None */
            public: bool BlankOriginal
            (
            );
            /**Sets  the blank original  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetBlankOriginal
            (
                bool blankoriginal /** blankoriginal */ 
            );
            /**Returns  the fix at timestamp option  <br> License requirements : None */
            public: bool FixAtCurrentTimestamp
            (
            );
            /**Sets  the fix at timestamp option  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetFixAtCurrentTimestamp
            (
                bool timestamp /** timestamp */ 
            );
            /**Returns the composite curve builder  <br> License requirements : None */
            public: NXOpen::Features::CompositeCurveBuilder * CompositeCurveBuilder
            (
            );
            /**Returns the extractfacebuilder  <br> License requirements : None */
            public: NXOpen::Features::ExtractFaceBuilder * ExtractFaceBuilder
            (
            );
            /**Sets the extractfacebuilder  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetExtractFaceBuilder
            (
                NXOpen::Features::ExtractFaceBuilder * extractFaceBuilder /** extractfacebuilder */ 
            );
            /**Returns the wave datum builder  <br> License requirements : None */
            public: NXOpen::Features::WaveDatumBuilder * WaveDatumBuilder
            (
            );
            /**Sets the wave datum builder  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetWaveDatumBuilder
            (
                NXOpen::Features::WaveDatumBuilder * wavedatumBuilder /** wavedatumbuilder */ 
            );
            /**Returns the wave routing builder  <br> License requirements : None */
            public: NXOpen::Features::WaveRoutingBuilder * WaveRoutingBuilder
            (
            );
            /**Sets the wave routing builder  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetWaveRoutingBuilder
            (
                NXOpen::Features::WaveRoutingBuilder * waveroutingBuilder /** waveroutingbuilder */ 
            );
            /**Returns the wave point builder  <br> License requirements : None */
            public: NXOpen::Features::WavePointBuilder * WavePointBuilder
            (
            );
            /**Sets the wave point builder  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetWavePointBuilder
            (
                NXOpen::Features::WavePointBuilder * wavepointBuilder /** wavepointbuilder */ 
            );
            /**Returns the mirrorbodybuilder <br> License requirements : None */
            public: NXOpen::Features::MirrorBodyBuilder * MirrorBodyBuilder
            (
            );
            /**Sets the mirrorbodybuilder <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetMirrorBodyBuilder
            (
                NXOpen::Features::MirrorBodyBuilder * mirrorBodyBuilder /** mirrorbodybuilder */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
