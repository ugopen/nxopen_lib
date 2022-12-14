#ifndef NXOpen_FEATURES_VEHICLEDESIGN_WINDSHIELDDATUMBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_VEHICLEDESIGN_WINDSHIELDDATUMBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_VehicleDesign_WindshieldDatumBuilder.ja
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
#include <NXOpen/Expression.hxx>
#include <NXOpen/Features_FeatureBuilder.hxx>
#include <NXOpen/ScCollector.hxx>
#include <NXOpen/SelectObject.hxx>
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
            class WindshieldDatumBuilder;
        }
    }
    class Expression;
    namespace Features
    {
        class FeatureBuilder;
    }
    namespace Features
    {
        class SelectFeature;
    }
    class Point;
    class ScCollector;
    namespace Features
    {
        namespace VehicleDesign
        {
            class _WindshieldDatumBuilderBuilder;
            class WindshieldDatumBuilderImpl;
            /**
                    Represents a @link NXOpen::Features::VehicleDesign::WindshieldDatum NXOpen::Features::VehicleDesign::WindshieldDatum@endlink  builder used to create or edit a Windshield Datum.
                     <br> To create a new instance of this class, use @link NXOpen::Features::VehicleDesignCollection::CreateWindshieldDatumBuilder  NXOpen::Features::VehicleDesignCollection::CreateWindshieldDatumBuilder @endlink  <br> 
            Default values.
            <list type="table"> 
             
            <listheader><term> 
            Property</term>  <description> 
            Value</description> </listheader>
            <item><term> 
             
            AssoToggle </term> <description> 
             
            1 </description> </item> 

            <item><term> 
             
            BottomAngle.Value </term> <description> 
             
            5 </description> </item> 

            <item><term> 
             
            EyeType </term> <description> 
             
            EyeFeature </description> </item> 

            <item><term> 
             
            HorizontalAngle.Value </term> <description> 
             
            17 </description> </item> 

            <item><term> 
             
            RayLength.Value </term> <description> 
             
            3000 (millimeters part), 0 (inches part) </description> </item> 

            <item><term> 
             
            ShowPoints </term> <description> 
             
            1 </description> </item> 

            <item><term> 
             
            ShowRays </term> <description> 
             
            1 </description> </item> 

            <item><term> 
             
            TopAngle.Value </term> <description> 
             
            7 </description> </item> 

            <item><term> 
             
            UseStandardLoading </term> <description> 
             
            1 </description> </item> 

            <item><term> 
             
            VisionType </term> <description> 
             
            Standard </description> </item> 

            </list> 

             <br>  Created in NX6.0.0.  <br>  
            */
            class NXOPENCPP_FEATURESEXPORT  WindshieldDatumBuilder : public NXOpen::Features::FeatureBuilder
            {
                /** Represents the eye definition type to define the Windshield Datum. */
                public: enum EnumEyeType
                {
                    EnumEyeTypeEyeFeature/** eye feature */,
                    EnumEyeTypeV1Point/** v1 point */,
                    EnumEyeTypeV2Point/** v2 point */
                };

                /** Represents the vision angle type to define the Windshield Datum. */
                public: enum CustomVisionAngle
                {
                    CustomVisionAngleStandard/** standard */,
                    CustomVisionAngleCustom/** customized */
                };

                private: WindshieldDatumBuilderImpl * m_windshielddatumbuilder_impl;
                private: friend class  _WindshieldDatumBuilderBuilder;
                protected: WindshieldDatumBuilder();
                public: ~WindshieldDatumBuilder();
                /**Returns  the option that determines whether to use the loading specified by standard or not. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: bool UseStandardLoading
                (
                );
                /**Sets  the option that determines whether to use the loading specified by standard or not. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetUseStandardLoading
                (
                    bool useStandardLoading /** usestandardloading */ 
                );
                /**Returns  the name of the used loading in the Windshield Datum.
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NXString LoadingName
                (
                );
                /**Sets  the name of the used loading in the Windshield Datum.
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetLoadingName
                (
                    const NXString & loadingName /** loadingname */ 
                );
                /**Sets  the name of the used loading in the Windshield Datum.
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                void SetLoadingName
                (
                    const char * loadingName /** loadingname */ 
                );
                /**Returns  the eye type to determine which type of v points to be used. 
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::VehicleDesign::WindshieldDatumBuilder::EnumEyeType EyeType
                (
                );
                /**Sets  the eye type to determine which type of v points to be used. 
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetEyeType
                (
                    NXOpen::Features::VehicleDesign::WindshieldDatumBuilder::EnumEyeType eyeType /** eyetype */ 
                );
                /**Returns  the eye feature; select eec feature when eye type specified. 
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::SelectFeature * EyeFeature
                (
                );
                /**Returns  the point v1; select one point when eye type specified. 
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Point * PointV1
                (
                );
                /**Sets  the point v1; select one point when eye type specified. 
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetPointV1
                (
                    NXOpen::Point * pointV1 /** pointv1 */ 
                );
                /**Returns  the point v2; select one point when eye type specified. 
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Point * PointV2
                (
                );
                /**Sets  the point v2; select one point when eye type specified. 
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetPointV2
                (
                    NXOpen::Point * pointV2 /** pointv2 */ 
                );
                /**Returns  the show points to determine whether to create points or not. 
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : None */
                public: bool ShowPoints
                (
                );
                /**Sets  the show points to determine whether to create points or not. 
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetShowPoints
                (
                    bool showPoints /** showpoints */ 
                );
                /**Returns  the windshield collector which the v points will be projected onto. 
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::ScCollector * SelectWindshield
                (
                );
                /**Returns  the show rays to determine whether to create ray lines or not. 
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : None */
                public: bool ShowRays
                (
                );
                /**Sets  the show rays to determine whether to create ray lines or not. 
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetShowRays
                (
                    bool showRays /** showrays */ 
                );
                /**Returns  the ray length. 
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * RayLength
                (
                );
                /**Returns  the vision type; standard or customer defined. 
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::VehicleDesign::WindshieldDatumBuilder::CustomVisionAngle VisionType
                (
                );
                /**Sets  the vision type; standard or customer defined. 
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetVisionType
                (
                    NXOpen::Features::VehicleDesign::WindshieldDatumBuilder::CustomVisionAngle visionType /** visiontype */ 
                );
                /**Returns  the top inclined angle. 
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * TopAngle
                (
                );
                /**Returns  the bottom inclined angle. 
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * BottomAngle
                (
                );
                /**Returns  the horizontal inclined angle. 
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * HorizontalAngle
                (
                );
                /**Returns  the associative option that determines whether to create feature or not. 
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : None */
                public: bool AssoToggle
                (
                );
                /**Sets  the associative option that determines whether to create feature or not. 
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetAssoToggle
                (
                    bool assoToggle /** assotoggle */ 
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
