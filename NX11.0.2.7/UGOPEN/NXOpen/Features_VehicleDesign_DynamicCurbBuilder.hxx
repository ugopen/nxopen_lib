#ifndef NXOpen_FEATURES_VEHICLEDESIGN_DYNAMICCURBBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_VEHICLEDESIGN_DYNAMICCURBBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_VehicleDesign_DynamicCurbBuilder.ja
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
#include <NXOpen/Features_VehicleDesign_DynamicCurbBuilder.hxx>
#include <NXOpen/Features_FeatureBuilder.hxx>
#include <NXOpen/ScCollector.hxx>
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
            class DynamicCurbBuilder;
        }
    }
    class Expression;
    namespace Features
    {
        class FeatureBuilder;
    }
    class ScCollector;
    namespace Features
    {
        namespace VehicleDesign
        {
            class _DynamicCurbBuilderBuilder;
            class DynamicCurbBuilderImpl;
            /**
                    Represents a @link NXOpen::Features::VehicleDesign::DynamicCurb NXOpen::Features::VehicleDesign::DynamicCurb@endlink  builder
                     <br> To create a new instance of this class, use @link NXOpen::Features::VehicleDesignCollection::CreateDynamicCurbBuilder  NXOpen::Features::VehicleDesignCollection::CreateDynamicCurbBuilder @endlink  <br> 
            Default values.
            <table border="1"> 
             
            <tr><th> 
            Property</th>  <th> 
            Value</th> </tr>
            <tr><td> 
             
            InnerLineType </td> <td> 
             
            Horizontal </td> </tr> 

            <tr><td> 
             
            Position </td> <td> 
             
            Front </td> </tr> 

            <tr><td> 
             
            RequirementsControl </td> <td> 
             
            StandardDriven </td> </tr> 

            <tr><td> 
             
            ShowClearance </td> <td> 
             
            0 </td> </tr> 

            <tr><td> 
             
            Visualization </td> <td> 
             
            Surface </td> </tr> 

            <tr><td> 
             
            WheelSize </td> <td> 
             
            StaticRadius </td> </tr> 

            </table>  

             <br>  Created in NX8.5.0.  <br>  
            */
            class NXOPENCPP_FEATURESEXPORT  DynamicCurbBuilder : public NXOpen::Features::FeatureBuilder
            {
                /** Represents the requirements control types to define the dynamic curb. */
                public: enum RequirementsControlType
                {
                    RequirementsControlTypeStandardDriven/** standard driven */ ,
                    RequirementsControlTypeUserDefined/** user defined */ 
                };

                /** Represents the type of the wheel size option for dynamic curb. */
                public: enum WheelType
                {
                    WheelTypeStaticRadius/** static radius */ ,
                    WheelTypeDiameter/** diameter */ 
                };

                /** Represents the dynamic curb positions. */
                public: enum PositionType
                {
                    PositionTypeFront/** front */ ,
                    PositionTypeRear/** rear */ ,
                    PositionTypeBoth/** both */ 
                };

                /** Represents the type of inner line to create dynamic curb. */
                public: enum MethodType
                {
                    MethodTypeHorizontal/** horizontal */ ,
                    MethodTypeVerticalTangent/** vertical tangent */ ,
                    MethodTypeParallelTangent/** parallel tangent */ 
                };

                /** Represents the visualization types of the output. */
                public: enum VisualizationType
                {
                    VisualizationTypeCurve/** curve */ ,
                    VisualizationTypeSurface/** surface */ ,
                    VisualizationTypeCurveSurface/** curve surface */ 
                };

                private: DynamicCurbBuilderImpl * m_dynamiccurbbuilder_impl;
                private: friend class  _DynamicCurbBuilderBuilder;
                protected: DynamicCurbBuilder();
                public: ~DynamicCurbBuilder();
                /**Returns  the requirements control for standard driven or user defined. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::VehicleDesign::DynamicCurbBuilder::RequirementsControlType RequirementsControl
                (
                );
                /**Sets  the requirements control for standard driven or user defined. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetRequirementsControl
                (
                    NXOpen::Features::VehicleDesign::DynamicCurbBuilder::RequirementsControlType requirementsControl /** requirementscontrol */ 
                );
                /**Returns  the standard used to define the dynamic curb. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: NXString Standard
                (
                );
                /**Sets  the standard used to define the dynamic curb. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetStandard
                (
                    const NXString & standard /** standard */ 
                );
                /**Sets  the standard used to define the dynamic curb. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                void SetStandard
                (
                    const char * standard /** standard */ 
                );
                /**Returns  the loading used in the dynamic curb. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: NXString Loading
                (
                );
                /**Sets  the loading used in the dynamic curb. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetLoading
                (
                    const NXString & loading /** loading */ 
                );
                /**Sets  the loading used in the dynamic curb. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                void SetLoading
                (
                    const char * loading /** loading */ 
                );
                /**Returns  the wheel size option which determines the size of the wheels in the dynamic curb. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::VehicleDesign::DynamicCurbBuilder::WheelType WheelSize
                (
                );
                /**Sets  the wheel size option which determines the size of the wheels in the dynamic curb. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetWheelSize
                (
                    NXOpen::Features::VehicleDesign::DynamicCurbBuilder::WheelType wheelSize /** wheelsize */ 
                );
                /**Returns  the dynamic curb position. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::VehicleDesign::DynamicCurbBuilder::PositionType Position
                (
                );
                /**Sets  the dynamic curb position. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetPosition
                (
                    NXOpen::Features::VehicleDesign::DynamicCurbBuilder::PositionType position /** position */ 
                );
                /**Returns  the inner line type for dynamic curb. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::VehicleDesign::DynamicCurbBuilder::MethodType InnerLineType
                (
                );
                /**Sets  the inner line type for dynamic curb. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetInnerLineType
                (
                    NXOpen::Features::VehicleDesign::DynamicCurbBuilder::MethodType innerLineType /** innerlinetype */ 
                );
                /**Returns  the expression defining the value of outer offset in front for dynamic curb. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * FrontOuterOffset
                (
                );
                /**Returns  the expression defining the length of the inner line in front for dynamic curb. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * FrontInnerLength
                (
                );
                /**Returns  the expression defining the value of inner offset in front for dynamic curb. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * FrontInnerOffset
                (
                );
                /**Returns  the expression defining the value of outer offset in rear for dynamic curb. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * RearOuterOffset
                (
                );
                /**Returns  the expression defining the length of the inner line in rear for dynamic curb. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * RearInnerLength
                (
                );
                /**Returns  the expression defining the value of inner offset in rear for dynamic curb. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * RearInnerOffset
                (
                );
                /**Returns  the faces representing the front car body geometry for the measurement. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::ScCollector * FrontSelector
                (
                );
                /**Returns  the indication if the distance measurement will be shown. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: bool ShowClearance
                (
                );
                /**Sets  the indication if the distance measurement will be shown. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetShowClearance
                (
                    bool showClearance /** showclearance */ 
                );
                /**Returns  the faces representing the rear car body geometry for the measurement. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::ScCollector * RearSelector
                (
                );
                /**Returns  the visualization type of the dynamic curb output.
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::VehicleDesign::DynamicCurbBuilder::VisualizationType Visualization
                (
                );
                /**Sets  the visualization type of the dynamic curb output.
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetVisualization
                (
                    NXOpen::Features::VehicleDesign::DynamicCurbBuilder::VisualizationType visualization /** visualization */ 
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
