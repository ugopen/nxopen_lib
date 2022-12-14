#ifndef NXOpen_FEATURES_REFLECTIONDATABUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_REFLECTIONDATABUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_ReflectionDataBuilder.ja
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
#include <NXOpen/Features_ReflectionDataBuilder.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Features
    {
        class ReflectionDataBuilder;
    }
    namespace Features
    {
        class FeatureBuilder;
    }
    class Point;
    class SelectCurveList;
    class SelectFaceList;
    namespace Features
    {
        class _ReflectionDataBuilderBuilder;
        /**
            Represents a @link Features::ReflectionData Features::ReflectionData@endlink  builder
             <br> To create a new instance of this class, use @link Features::FeatureCollection::CreateReflectionDataBuilder Features::FeatureCollection::CreateReflectionDataBuilder@endlink  <br> 
        Default values:
        IsReflectData: 1
        IsReflectTraceCurve: 0
        IsRefractData: 0
        IsRefractTraceCurve: 0
        ReflectAccuracy: 20
        RefractionIndex: 1.5
        Resolution: Medium
        Thickness: 5
        */
        class NXOPENCPPEXPORT ReflectionDataBuilder : public Features::FeatureBuilder
        {
            /** the resolution type */
            public: enum ResolutionType
            {
                ResolutionTypeLow/** low */,
                ResolutionTypeMedium/** medium */,
                ResolutionTypeHigh/** high */,
                ResolutionTypeCustomized/** user defined */
            };

            private: friend class  _ReflectionDataBuilderBuilder;
            protected: ReflectionDataBuilder();
            /**Returns  the eye point  <br> License requirements : None */
            public: NXOpen::Point * EyePoint
            (
            );
            /**Sets  the eye point  <br> License requirements : nx_general_packaging ("NX General Packaging") */
            public: void SetEyePoint
            (
                NXOpen::Point * eyePoint /** eyepoint */ 
            );
            /**Returns  the target object to be reflected on the faces and/or planes  <br> License requirements : None */
            public: NXOpen::SelectCurveList * TargetObject
            (
            );
            /**Returns  the reflection object to reflect the input target objects  <br> License requirements : None */
            public: NXOpen::SelectFaceList * ReflectionObject
            (
            );
            /**Returns  the thickness of the reflection objects  <br> License requirements : None */
            public: double Thickness
            (
            );
            /**Sets  the thickness of the reflection objects  <br> License requirements : nx_general_packaging ("NX General Packaging") */
            public: void SetThickness
            (
                double thickness /** thickness */ 
            );
            /**Returns  whether the direction of reflection objects is reversed to determine their thickness  <br> License requirements : None */
            public: bool ReverseDir
            (
            );
            /**Sets  whether the direction of reflection objects is reversed to determine their thickness  <br> License requirements : nx_general_packaging ("NX General Packaging") */
            public: void SetReverseDir
            (
                bool reverseDir /** reversedir */ 
            );
            /**Returns  the refraction index  <br> License requirements : None */
            public: double RefractionIndex
            (
            );
            /**Sets  the refraction index  <br> License requirements : nx_general_packaging ("NX General Packaging") */
            public: void SetRefractionIndex
            (
                double refractionIndex /** refractionindex */ 
            );
            /**Returns  the resolution type   <br> License requirements : None */
            public: NXOpen::Features::ReflectionDataBuilder::ResolutionType Resolution
            (
            );
            /**Sets  the resolution type   <br> License requirements : nx_general_packaging ("NX General Packaging") */
            public: void SetResolution
            (
                NXOpen::Features::ReflectionDataBuilder::ResolutionType resolution /** resolution */ 
            );
            /**Returns  the customized reflection accuracy, which is the number of dispersed points for the input target objects  <br> License requirements : None */
            public: int ReflectAccuracy
            (
            );
            /**Sets  the customized reflection accuracy, which is the number of dispersed points for the input target objects  <br> License requirements : nx_general_packaging ("NX General Packaging") */
            public: void SetReflectAccuracy
            (
                int reflectAccuracy /** reflectaccuracy */ 
            );
            /**Returns  whether to create reflection data as output or not   <br> License requirements : None */
            public: bool IsReflectData
            (
            );
            /**Sets  whether to create reflection data as output or not   <br> License requirements : nx_general_packaging ("NX General Packaging") */
            public: void SetReflectData
            (
                bool isReflectData /** isreflectdata */ 
            );
            /**Returns  whether to create reflection trace curves as output or not  <br> License requirements : None */
            public: bool IsReflectTraceCurve
            (
            );
            /**Sets  whether to create reflection trace curves as output or not  <br> License requirements : nx_general_packaging ("NX General Packaging") */
            public: void SetReflectTraceCurve
            (
                bool isReflectTraceCurve /** isreflecttracecurve */ 
            );
            /**Returns  whether to create refraction data as output or not   <br> License requirements : None */
            public: bool IsRefractData
            (
            );
            /**Sets  whether to create refraction data as output or not   <br> License requirements : nx_general_packaging ("NX General Packaging") */
            public: void SetRefractData
            (
                bool isRefractData /** isrefractdata */ 
            );
            /**Returns  whether to create refraction trace curves as output or not   <br> License requirements : None */
            public: bool IsRefractTraceCurve
            (
            );
            /**Sets  whether to create refraction trace curves as output or not   <br> License requirements : nx_general_packaging ("NX General Packaging") */
            public: void SetRefractTraceCurve
            (
                bool isRefractTraceCurve /** isrefracttracecurve */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
