#ifndef NXOpen_FEATURES_VEHICLEDESIGN_BASEDATALOADINGWHEELBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_VEHICLEDESIGN_BASEDATALOADINGWHEELBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_VehicleDesign_BaseDataLoadingWheelBuilder.ja
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
#include <NXOpen/Features_VehicleDesign_BaseDataLoadingWheelBuilder.hxx>
#include <NXOpen/Features_VehicleDesign_BaseDataWheelBuilder.hxx>
#include <NXOpen/Builder.hxx>
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
            class BaseDataLoadingWheelBuilder;
        }
    }
    class Builder;
    namespace Features
    {
        namespace VehicleDesign
        {
            class BaseDataWheelBuilder;
        }
    }
    namespace Features
    {
        namespace VehicleDesign
        {
            class _BaseDataLoadingWheelBuilderBuilder;
            class BaseDataLoadingWheelBuilderImpl;
            /** Represents a @link NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder@endlink .  <br> This class can only be used in base data, thus cannot be created directly by user.  <br> 
             <br>  Created in NX8.5.0.  <br>  
            */
            class NXOPENCPP_FEATURESEXPORT  BaseDataLoadingWheelBuilder : public NXOpen::Builder
            {
                /** This enum represents the options to define the wheel position. */
                public: enum DataDefinitionOptions
                {
                    DataDefinitionOptionsRelative/** Relative: The wheel data of this loading will use relative values to design data. */,
                    DataDefinitionOptionsAbsolute/** Absolute: The wheel data of this loading will use absolute values. */
                };

                private: BaseDataLoadingWheelBuilderImpl * m_basedataloadingwheelbuilder_impl;
                private: friend class  _BaseDataLoadingWheelBuilderBuilder;
                protected: BaseDataLoadingWheelBuilder();
                public: ~BaseDataLoadingWheelBuilder();
                /**Returns  the design data of the wheel. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::VehicleDesign::BaseDataWheelBuilder * DesignData
                (
                );
                /**Sets  the design data of the wheel. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetDesignData
                (
                    NXOpen::Features::VehicleDesign::BaseDataWheelBuilder * wheel /** wheel */ 
                );
                /**Returns  the value to indicate which definition option will be used to define the loading wheel data. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinitionOptions DataDefinition
                (
                );
                /**Sets  the value to indicate which definition option will be used to define the loading wheel data. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetDataDefinition
                (
                    NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinitionOptions dataDefinition /** datadefinition */ 
                );
                /**Returns  the delta x value of wheel center point. 
                                It is used only when @link NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinition NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinition@endlink  is
                                 @link NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinitionOptionsRelative NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinitionOptionsRelative@endlink .
                            
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: double DeltaX
                (
                );
                /**Sets  the delta x value of wheel center point. 
                                It is used only when @link NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinition NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinition@endlink  is
                                 @link NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinitionOptionsRelative NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinitionOptionsRelative@endlink .
                            
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetDeltaX
                (
                    double deltaX /** deltax */ 
                );
                /**Returns  the delta y value of wheel center point. 
                                It is used only when @link NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinition NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinition@endlink 
                                 is @link NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinitionOptionsRelative NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinitionOptionsRelative@endlink .
                            
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: double DeltaY
                (
                );
                /**Sets  the delta y value of wheel center point. 
                                It is used only when @link NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinition NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinition@endlink 
                                 is @link NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinitionOptionsRelative NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinitionOptionsRelative@endlink .
                            
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetDeltaY
                (
                    double deltaY /** deltay */ 
                );
                /**Returns  the delta z value of wheel center point. 
                                It is used only when @link NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinition NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinition@endlink  is 
                                @link NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinitionOptionsRelative NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinitionOptionsRelative@endlink .
                            
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: double DeltaZ
                (
                );
                /**Sets  the delta z value of wheel center point. 
                                It is used only when @link NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinition NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinition@endlink  is 
                                @link NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinitionOptionsRelative NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinitionOptionsRelative@endlink .
                            
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetDeltaZ
                (
                    double deltaZ /** deltaz */ 
                );
                /**Returns  the delta width of wheel, for front or rear wheel, they have a wheel width. For each loading, they have a delta width,
                                the loading width will be sum of wheel width and delta width.
                                It is used only when @link NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinition NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinition@endlink  is
                                 @link NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinitionOptionsRelative NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinitionOptionsRelative@endlink .
                            
                 <br>  Created in NX11.0.1.  <br>  
                 <br> License requirements : None */
                public: double DeltaWidth
                (
                );
                /**Sets  the delta width of wheel, for front or rear wheel, they have a wheel width. For each loading, they have a delta width,
                                the loading width will be sum of wheel width and delta width.
                                It is used only when @link NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinition NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinition@endlink  is
                                 @link NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinitionOptionsRelative NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinitionOptionsRelative@endlink .
                            
                 <br>  Created in NX11.0.1.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetDeltaWidth
                (
                    double deltaWidth /** deltawidth */ 
                );
                /**Returns  the delta static radius of wheel. 
                                It is used only when @link NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinition NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinition@endlink  is
                                 @link NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinitionOptionsRelative NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinitionOptionsRelative@endlink .
                            
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: double DeltaStaticRadius
                (
                );
                /**Sets  the delta static radius of wheel. 
                                It is used only when @link NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinition NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinition@endlink  is
                                 @link NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinitionOptionsRelative NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinitionOptionsRelative@endlink .
                            
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetDeltaStaticRadius
                (
                    double deltaStaticRadius /** deltastaticradius */ 
                );
                /**Returns  the delta camber of wheel.  
                                It is used only when @link NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinition NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinition@endlink  
                                is @link NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinitionOptionsRelative NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinitionOptionsRelative@endlink .
                            
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: double DeltaCamber
                (
                );
                /**Sets  the delta camber of wheel.  
                                It is used only when @link NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinition NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinition@endlink  
                                is @link NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinitionOptionsRelative NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinitionOptionsRelative@endlink .
                            
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetDeltaCamber
                (
                    double deltaCamber /** deltacamber */ 
                );
                /**Returns  the delta toe of wheel.  
                                It is used only when @link NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinition NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinition@endlink  is
                                 @link NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinitionOptionsRelative NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinitionOptionsRelative@endlink .
                            
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: double DeltaToe
                (
                );
                /**Sets  the delta toe of wheel.  
                                It is used only when @link NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinition NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinition@endlink  is
                                 @link NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinitionOptionsRelative NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinitionOptionsRelative@endlink .
                            
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetDeltaToe
                (
                    double deltaToe /** deltatoe */ 
                );
                /**Returns  the x coordinate of wheel center point.
                                Used only when @link NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinition NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinition@endlink  is 
                                @link NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinitionOptionsAbsolute NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinitionOptionsAbsolute@endlink .
                            
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: double CoordinateX
                (
                );
                /**Sets  the x coordinate of wheel center point.
                                Used only when @link NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinition NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinition@endlink  is 
                                @link NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinitionOptionsAbsolute NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinitionOptionsAbsolute@endlink .
                            
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetCoordinateX
                (
                    double absX /** absx */ 
                );
                /**Returns  the y coordinate of wheel center point.
                                Used only when @link NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinition NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinition@endlink  is 
                                 @link NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinitionOptionsAbsolute NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinitionOptionsAbsolute@endlink .
                            
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: double CoordinateY
                (
                );
                /**Sets  the y coordinate of wheel center point.
                                Used only when @link NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinition NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinition@endlink  is 
                                 @link NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinitionOptionsAbsolute NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinitionOptionsAbsolute@endlink .
                            
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetCoordinateY
                (
                    double absY /** absy */ 
                );
                /**Returns  the z coordinate of wheel center point.
                                Used only when @link NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinition NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinition@endlink  is
                                 @link NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinitionOptionsAbsolute NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinitionOptionsAbsolute@endlink .
                            
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: double CoordinateZ
                (
                );
                /**Sets  the z coordinate of wheel center point.
                                Used only when @link NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinition NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinition@endlink  is
                                 @link NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinitionOptionsAbsolute NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinitionOptionsAbsolute@endlink .
                            
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetCoordinateZ
                (
                    double absZ /** absz */ 
                );
                /**Returns  the width of front or rear width, it's value is sum of wheel width and delta width.
                                Used only when @link NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinition NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinition@endlink  is
                                 @link NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinitionOptionsAbsolute NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinitionOptionsAbsolute@endlink .
                            
                 <br>  Created in NX11.0.1.  <br>  
                 <br> License requirements : None */
                public: double Width
                (
                );
                /**Sets  the width of front or rear width, it's value is sum of wheel width and delta width.
                                Used only when @link NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinition NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinition@endlink  is
                                 @link NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinitionOptionsAbsolute NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinitionOptionsAbsolute@endlink .
                            
                 <br>  Created in NX11.0.1.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetWidth
                (
                    double width /** width */ 
                );
                /**Returns  the static radius of wheel.
                                Used only when @link NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinition NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinition@endlink  is
                                 @link NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinitionOptionsAbsolute NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinitionOptionsAbsolute@endlink .
                            
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: double StaticRadius
                (
                );
                /**Sets  the static radius of wheel.
                                Used only when @link NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinition NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinition@endlink  is
                                 @link NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinitionOptionsAbsolute NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinitionOptionsAbsolute@endlink .
                            
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetStaticRadius
                (
                    double staticRadius /** staticradius */ 
                );
                /**Returns  the camber of wheel in degree.
                                Used only when @link NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinition NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinition@endlink  is 
                                @link NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinitionOptionsAbsolute NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinitionOptionsAbsolute@endlink .
                            
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: double Camber
                (
                );
                /**Sets  the camber of wheel in degree.
                                Used only when @link NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinition NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinition@endlink  is 
                                @link NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinitionOptionsAbsolute NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinitionOptionsAbsolute@endlink .
                            
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetCamber
                (
                    double camber /** camber */ 
                );
                /**Returns  the toe in/out of wheel in degree.
                                Used only when @link NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinition NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinition@endlink  is 
                                @link NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinitionOptionsAbsolute NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinitionOptionsAbsolute@endlink .
                            
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: double Toe
                (
                );
                /**Sets  the toe in/out of wheel in degree.
                                Used only when @link NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinition NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinition@endlink  is 
                                @link NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinitionOptionsAbsolute NXOpen::Features::VehicleDesign::BaseDataLoadingWheelBuilder::DataDefinitionOptionsAbsolute@endlink .
                            
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetToe
                (
                    double toe /** toe */ 
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