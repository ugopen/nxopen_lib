#ifndef NXOpen_FEATURES_SHIPDESIGN_PLATECHAMFERBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_SHIPDESIGN_PLATECHAMFERBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_ShipDesign_PlateChamferBuilder.ja
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
        namespace ShipDesign
        {
            class PlateChamferBuilder;
        }
    }
    class Expression;
    namespace Features
    {
        class FeatureBuilder;
    }
    class Plane;
    class ScCollector;
    namespace Features
    {
        namespace ShipDesign
        {
            class _PlateChamferBuilderBuilder;
            class PlateChamferBuilderImpl;
            /**
                Represents a @link NXOpen::Features::ShipDesign::PlateChamfer NXOpen::Features::ShipDesign::PlateChamfer@endlink  builder. It is used to create and edit a plate chamfer feature.
                 <br> To create a new instance of this class, use @link NXOpen::Features::ShipCollection::CreatePlateChamferBuilder  NXOpen::Features::ShipCollection::CreatePlateChamferBuilder @endlink  <br> 
            Default values.
            <list type="table"> 
             
            <listheader><term> 
            Property</term>  <description> 
            Value</description> </listheader>
            <item><term> 
             
            AngleOption </term> <description> 
             
            Angle </description> </item> 

            <item><term> 
             
            AngularDimension.Value </term> <description> 
             
            30 </description> </item> 

            <item><term> 
             
            ChamferBothSides </term> <description> 
             
            0 </description> </item> 

            <item><term> 
             
            ChordalTolerance </term> <description> 
             
            0.0254 </description> </item> 

            <item><term> 
             
            ClearanceTolerance </term> <description> 
             
            0.0254 </description> </item> 

            <item><term> 
             
            Depth.Value </term> <description> 
             
            10 (millimeters part), 0.4 (inches part) </description> </item> 

            <item><term> 
             
            OffsetOption </term> <description> 
             
            Depth </description> </item> 

            <item><term> 
             
            Ratio.Value </term> <description> 
             
            0.3 </description> </item> 

            <item><term> 
             
            RestDepth.Value </term> <description> 
             
            0 (millimeters part), 0 (inches part) </description> </item> 

            <item><term> 
             
            UseLimits </term> <description> 
             
            0 </description> </item> 

            </list> 

             <br>  Created in NX8.0.0.  <br>  
            */
            class NXOPENCPP_FEATURESEXPORT  PlateChamferBuilder : public NXOpen::Features::FeatureBuilder
            {
                /**
                        The option for the type of associativity for chamfer.
                        */
                public: enum Types
                {
                    TypesOnEdge/** Create a chamfer on the edge */,
                    TypesToPlate/** Create a chamfer on the common edges between plates */
                };

                /**
                        The option to specify the method for defining angle or ratio.
                        */
                public: enum AngleMethod
                {
                    AngleMethodAngle/** Use the angle for the chamfer parameters */,
                    AngleMethodRatio/** Use the ratio for the chamfer parameters */
                };

                /**
                        The option to specify the method for chamfer offset method.
                        */
                public: enum OffsetMethod
                {
                    OffsetMethodDepth/** Use depth parameter to define ramp */,
                    OffsetMethodRestDepth/** Use rest depth to define ramp */,
                    OffsetMethodThinnerPlate/** Use the thickness of the thinner plate to define ramp depth */
                };

                private: PlateChamferBuilderImpl * m_platechamferbuilder_impl;
                private: friend class  _PlateChamferBuilderBuilder;
                protected: PlateChamferBuilder();
                public: ~PlateChamferBuilder();
                /**Returns  the select edge 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::ScCollector * SelectEdge
                (
                );
                /**Returns  the select target 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::ScCollector * SelectTarget
                (
                );
                /**Returns  the reverse direction 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: bool ReverseDirection
                (
                );
                /**Sets  the reverse direction 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : nx_ship_detail ("Ship Detail Design") */
                public: void SetReverseDirection
                (
                    bool reverseDirection /** reversedirection */ 
                );
                /**Returns  the chamfer both sides 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: bool ChamferBothSides
                (
                );
                /**Sets  the chamfer both sides 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : nx_ship_detail ("Ship Detail Design") */
                public: void SetChamferBothSides
                (
                    bool chamferBothSides /** chamferbothsides */ 
                );
                /**Returns  the select tool 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::ScCollector * SelectTool
                (
                );
                /**Returns  the angle option 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::ShipDesign::PlateChamferBuilder::AngleMethod AngleOption
                (
                );
                /**Sets  the angle option 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : nx_ship_detail ("Ship Detail Design") */
                public: void SetAngleOption
                (
                    NXOpen::Features::ShipDesign::PlateChamferBuilder::AngleMethod angleOption /** angleoption */ 
                );
                /**Returns  the angular dimension 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * AngularDimension
                (
                );
                /**Returns  the ratio 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * Ratio
                (
                );
                /**Returns  the offset option 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::ShipDesign::PlateChamferBuilder::OffsetMethod OffsetOption
                (
                );
                /**Sets  the offset option 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : nx_ship_detail ("Ship Detail Design") */
                public: void SetOffsetOption
                (
                    NXOpen::Features::ShipDesign::PlateChamferBuilder::OffsetMethod offsetOption /** offsetoption */ 
                );
                /**Returns  the depth 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * Depth
                (
                );
                /**Returns  the rest depth 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * RestDepth
                (
                );
                /**Returns  the select thinner plate 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::ScCollector * SelectThinnerPlate
                (
                );
                /**Returns  the use limits 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: bool UseLimits
                (
                );
                /**Sets  the use limits 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : nx_ship_detail ("Ship Detail Design") */
                public: void SetUseLimits
                (
                    bool useLimits /** uselimits */ 
                );
                /**Returns  the start plane 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Plane * StartPlane
                (
                );
                /**Sets  the start plane 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : nx_ship_detail ("Ship Detail Design") */
                public: void SetStartPlane
                (
                    NXOpen::Plane * startPlane /** startplane */ 
                );
                /**Returns  the end plane 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Plane * EndPlane
                (
                );
                /**Sets  the end plane 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : nx_ship_detail ("Ship Detail Design") */
                public: void SetEndPlane
                (
                    NXOpen::Plane * endPlane /** endplane */ 
                );
                /**Returns  the chordal tolerance 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: double ChordalTolerance
                (
                );
                /**Sets  the chordal tolerance 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : nx_ship_detail ("Ship Detail Design") */
                public: void SetChordalTolerance
                (
                    double chordalTolerance /** chordaltolerance */ 
                );
                /**Returns  the clearance tolerance 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: double ClearanceTolerance
                (
                );
                /**Sets  the clearance tolerance 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : nx_ship_detail ("Ship Detail Design") */
                public: void SetClearanceTolerance
                (
                    double clearanceTolerance /** clearancetolerance */ 
                );
                /**Returns  the type 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::ShipDesign::PlateChamferBuilder::Types Type
                (
                );
                /**Sets  the type 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : nx_ship_detail ("Ship Detail Design") */
                public: void SetType
                (
                    NXOpen::Features::ShipDesign::PlateChamferBuilder::Types type /** type */ 
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
