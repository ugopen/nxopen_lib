#ifndef NXOpen_FEATURES_VEHICLEDESIGN_REFLECTIONDATABUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_VEHICLEDESIGN_REFLECTIONDATABUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_VehicleDesign_ReflectionDataBuilder.ja
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
#include <NXOpen/Features_VehicleDesign_ReflectionDataBuilder.hxx>
#include <NXOpen/Features_FeatureBuilder.hxx>
#include <NXOpen/ScCollector.hxx>
#include <NXOpen/Section.hxx>
#include <NXOpen/libnxopencpp_features_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Features
    {
        namespace VehicleDesign
        {
            class ReflectionDataBuilder;
        }
    }
    namespace Features
    {
        class FeatureBuilder;
    }
    class Point;
    class ScCollector;
    class Section;
    namespace Features
    {
        namespace VehicleDesign
        {
            class _ReflectionDataBuilderBuilder;
            class ReflectionDataBuilderImpl;
            /**
                Represents a @link NXOpen::Features::VehicleDesign::ReflectionData NXOpen::Features::VehicleDesign::ReflectionData@endlink  builder
                 <br> To create a new instance of this class, use @link NXOpen::Features::VehicleDesignCollection::CreateReflectionDataBuilder  NXOpen::Features::VehicleDesignCollection::CreateReflectionDataBuilder @endlink  <br> 
            Default values.
            <table border="1"> 
             
            <tr><th> 
            Property</th>  <th> 
            Value</th> </tr>
            <tr><td> 
             
            IsReflectData </td> <td> 
             
            1 </td> </tr> 

            <tr><td> 
             
            IsReflectTraceCurve </td> <td> 
             
            0 </td> </tr> 

            <tr><td> 
             
            IsRefractData </td> <td> 
             
            0 </td> </tr> 

            <tr><td> 
             
            IsRefractTraceCurve </td> <td> 
             
            0 </td> </tr> 

            <tr><td> 
             
            ReflectAccuracy </td> <td> 
             
            20 </td> </tr> 

            <tr><td> 
             
            RefractionIndex </td> <td> 
             
            1.5 </td> </tr> 

            <tr><td> 
             
            Resolution </td> <td> 
             
            Medium </td> </tr> 

            <tr><td> 
             
            Thickness </td> <td> 
             
            5 </td> </tr> 

            </table>  

             <br>  Created in NX6.0.0.  <br>  
            */
            class NXOPENCPP_FEATURESEXPORT  ReflectionDataBuilder : public NXOpen::Features::FeatureBuilder
            {
                /** the resolution type */
                public: enum ResolutionType
                {
                    ResolutionTypeLow/** low */,
                    ResolutionTypeMedium/** medium */,
                    ResolutionTypeHigh/** high */,
                    ResolutionTypeCustomized/** user defined */
                };

                private: ReflectionDataBuilderImpl * m_reflectiondatabuilder_impl;
                private: friend class  _ReflectionDataBuilderBuilder;
                protected: ReflectionDataBuilder();
                public: ~ReflectionDataBuilder();
                /**Returns  the eye point 
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Point * EyePoint
                (
                );
                /**Sets  the eye point 
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetEyePoint
                (
                    NXOpen::Point * eyePoint /** eyepoint */ 
                );
                /**Returns  the target object to be reflected on the faces and/or planes 
                         the target object 
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Section * TargetObject
                (
                );
                /**Returns  the reflection object to reflect the input target objects 
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::ScCollector * ReflectionObject
                (
                );
                /**Returns  the thickness of the reflection objects 
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : None */
                public: double Thickness
                (
                );
                /**Sets  the thickness of the reflection objects 
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetThickness
                (
                    double thickness /** thickness */ 
                );
                /**Returns  whether the direction of reflection objects is reversed to determine their thickness 
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : None */
                public: bool ReverseDir
                (
                );
                /**Sets  whether the direction of reflection objects is reversed to determine their thickness 
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetReverseDir
                (
                    bool reverseDir /** reversedir */ 
                );
                /**Returns  the refraction index 
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : None */
                public: double RefractionIndex
                (
                );
                /**Sets  the refraction index 
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetRefractionIndex
                (
                    double refractionIndex /** refractionindex */ 
                );
                /**Returns  the resolution type  
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::VehicleDesign::ReflectionDataBuilder::ResolutionType Resolution
                (
                );
                /**Sets  the resolution type  
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetResolution
                (
                    NXOpen::Features::VehicleDesign::ReflectionDataBuilder::ResolutionType resolution /** resolution */ 
                );
                /**Returns  the customized reflection accuracy, which is the number of dispersed points for the input target objects 
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : None */
                public: int ReflectAccuracy
                (
                );
                /**Sets  the customized reflection accuracy, which is the number of dispersed points for the input target objects 
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetReflectAccuracy
                (
                    int reflectAccuracy /** reflectaccuracy */ 
                );
                /**Returns  whether to create reflection data as output or not  
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : None */
                public: bool IsReflectData
                (
                );
                /**Sets  whether to create reflection data as output or not  
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetReflectData
                (
                    bool isReflectData /** isreflectdata */ 
                );
                /**Returns  whether to create reflection trace curves as output or not 
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : None */
                public: bool IsReflectTraceCurve
                (
                );
                /**Sets  whether to create reflection trace curves as output or not 
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetReflectTraceCurve
                (
                    bool isReflectTraceCurve /** isreflecttracecurve */ 
                );
                /**Returns  whether to create refraction data as output or not  
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : None */
                public: bool IsRefractData
                (
                );
                /**Sets  whether to create refraction data as output or not  
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetRefractData
                (
                    bool isRefractData /** isrefractdata */ 
                );
                /**Returns  whether to create refraction trace curves as output or not  
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : None */
                public: bool IsRefractTraceCurve
                (
                );
                /**Sets  whether to create refraction trace curves as output or not  
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetRefractTraceCurve
                (
                    bool isRefractTraceCurve /** isrefracttracecurve */ 
                );
            };
        }
    }
}

#ifdef _MSC_VER
#pragma warning(pop)
#endif
#ifdef __GNUC__
#ifndef NX_NO_GCC_DEPRECATION_WARNINGS
#pragma GCC diagnostic warning "-Wdeprecated-declarations"
#endif
#endif

#undef EXPORTLIBRARY
#endif