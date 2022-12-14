#ifndef NXOpen_FEATURES_SHIPDESIGN_STIFFENERSYSTEMBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_SHIPDESIGN_STIFFENERSYSTEMBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_ShipDesign_StiffenerSystemBuilder.ja
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
#include <NXOpen/Features_ShipDesign_OrientationDefinitionBuilder.hxx>
#include <NXOpen/Features_ShipDesign_PlanePairBuilder.hxx>
#include <NXOpen/Features_ShipDesign_ShipNamesBuilder.hxx>
#include <NXOpen/Features_ShipDesign_StiffenerBySupportPathBuilder.hxx>
#include <NXOpen/Features_ShipDesign_StiffenerStockBuilder.hxx>
#include <NXOpen/Features_ShipDesign_StiffenerSystemBuilder.hxx>
#include <NXOpen/GeometricUtilities_ProjectionOptions.hxx>
#include <NXOpen/Features_ShipDesign_ProfileSystemBuilder.hxx>
#include <NXOpen/ObjectList.hxx>
#include <NXOpen/Section.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/Weld_CharacteristicsBuilder.hxx>
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
            class StiffenerSystemBuilder;
        }
    }
    class Direction;
    class Expression;
    namespace Features
    {
        namespace ShipDesign
        {
            class OrientationDefinitionBuilder;
        }
    }
    namespace Features
    {
        namespace ShipDesign
        {
            class PlaneListBuilderList;
        }
    }
    namespace Features
    {
        namespace ShipDesign
        {
            class PlanePairBuilder;
        }
    }
    namespace Features
    {
        namespace ShipDesign
        {
            class ProfileSystemBuilder;
        }
    }
    namespace Features
    {
        namespace ShipDesign
        {
            class ShipNamesBuilder;
        }
    }
    namespace Features
    {
        namespace ShipDesign
        {
            class StiffenerBySupportPathBuilder;
        }
    }
    namespace Features
    {
        namespace ShipDesign
        {
            class StiffenerStockBuilder;
        }
    }
    namespace GeometricUtilities
    {
        class ProjectionOptions;
    }
    class NXObjectList;
    class Plane;
    class Section;
    class SelectNXObjectList;
    namespace Weld
    {
        class CharacteristicsBuilder;
    }
    namespace Features
    {
        namespace ShipDesign
        {
            class _StiffenerSystemBuilderBuilder;
            class StiffenerSystemBuilderImpl;
            /**
                This class is used to create or edit a @link NXOpen::Features::ShipDesign::StiffenerSystem NXOpen::Features::ShipDesign::StiffenerSystem@endlink  feature.
                 <br> To create a new instance of this class, use @link NXOpen::Features::ShipCollection::CreateStiffenerSystemBuilder  NXOpen::Features::ShipCollection::CreateStiffenerSystemBuilder @endlink  <br> 
            Default values.
            <table border="1"> 
             
            <tr><th> 
            Property</th>  <th> 
            Value</th> </tr>
            <tr><td> 
             
            EndCutEnd </td> <td> 
             
            Connected </td> </tr> 

            <tr><td> 
             
            EndCutStart </td> <td> 
             
            Connected </td> </tr> 

            <tr><td> 
             
            MeasureAlongMode </td> <td> 
             
            AlongSurfaceLength </td> </tr> 

            <tr><td> 
             
            MountingMethod </td> <td> 
             
            NoOffset </td> </tr> 

            <tr><td> 
             
            OffsetDistance.Value </td> <td> 
             
            0 (millimeters part), 0 (inches part) </td> </tr> 

            <tr><td> 
             
            OffsetDistanceEnd.Value </td> <td> 
             
            0 (millimeters part), 0 (inches part) </td> </tr> 

            <tr><td> 
             
            OffsetDistanceStart.Value </td> <td> 
             
            0 (millimeters part), 0 (inches part) </td> </tr> 

            <tr><td> 
             
            OffsetNumber </td> <td> 
             
            0 </td> </tr> 

            <tr><td> 
             
            OffsetSpacing.Value </td> <td> 
             
            0 (millimeters part), 0 (inches part) </td> </tr> 

            <tr><td> 
             
            OffsetSpacingEnd.Value </td> <td> 
             
            0 (millimeters part), 0 (inches part) </td> </tr> 

            <tr><td> 
             
            OffsetSpacingMode </td> <td> 
             
            Single </td> </tr> 

            <tr><td> 
             
            OffsetSpacingStart.Value </td> <td> 
             
            0 (millimeters part), 0 (inches part) </td> </tr> 

            <tr><td> 
             
            OrientationAngle.Value </td> <td> 
             
            0 (millimeters part), 0 (inches part) </td> </tr> 

            <tr><td> 
             
            OrientationDefinitionBuilder.MeasureAngles </td> <td> 
             
            NormaltoCurve </td> </tr> 

            <tr><td> 
             
            OrientationDefinitionBuilder.ShowSurfaceAngles </td> <td> 
             
            0 </td> </tr> 

            <tr><td> 
             
            OrientationDefinitionBuilder.ShowTwistRate </td> <td> 
             
            0 </td> </tr> 

            <tr><td> 
             
            OrientationDefinitionBuilder.ShowWebAngles </td> <td> 
             
            0 </td> </tr> 

            <tr><td> 
             
            OrientationMethod </td> <td> 
             
            FaceNormal </td> </tr> 

            <tr><td> 
             
            StiffenerBySupportPathData.LengthParams.Value </td> <td> 
             
            300 (millimeters part), 100 (inches part) </td> </tr> 

            <tr><td> 
             
            StiffenerBySupportPathData.OrientationBySupport </td> <td> 
             
            0 </td> </tr> 

            <tr><td> 
             
            StockData.AnchorPoint </td> <td> 
             
            0 </td> </tr> 

            <tr><td> 
             
            StockData.PlateHeight.Value </td> <td> 
             
            50 (millimeters part), 2 (inches part) </td> </tr> 

            <tr><td> 
             
            StockData.PlateStockData.KnuckleRatio </td> <td> 
             
            3.0 </td> </tr> 

            <tr><td> 
             
            StockData.PlateStockData.KnuckleSmoothAngle </td> <td> 
             
            3.0 </td> </tr> 

            <tr><td> 
             
            StockData.PlateStockData.MaterialOption </td> <td> 
             
            0 </td> </tr> 

            <tr><td> 
             
            StockData.PlateStockData.OppositeThickness.Value </td> <td> 
             
            0 (millimeters part), 0 (inches part) </td> </tr> 

            <tr><td> 
             
            StockData.PlateStockData.RestrictThicknessToMaterial </td> <td> 
             
            true </td> </tr> 

            <tr><td> 
             
            StockData.PlateStockData.ThickenOption </td> <td> 
             
            SingleSided </td> </tr> 

            <tr><td> 
             
            StockData.PlateStockData.Thickness.Value </td> <td> 
             
            10 (millimeters part), 0.5 (inches part) </td> </tr> 

            <tr><td> 
             
            StockData.PlateStockData.ThicknessSourceOption </td> <td> 
             
            List </td> </tr> 

            <tr><td> 
             
            StockData.SectionType </td> <td> 
             
            Profile </td> </tr> 

            <tr><td> 
             
            Type </td> <td> 
             
            Curves </td> </tr> 

            </table>  

             <br>  Created in NX8.0.0.  <br>  
            */
            class NXOPENCPP_FEATURESEXPORT  StiffenerSystemBuilder : public NXOpen::Features::ShipDesign::ProfileSystemBuilder
            {
                /** Used to specify how the path of the stiffener system is defined. */
                public: enum Types
                {
                    TypesCurves/** curves */ ,
                    TypesPlanes/** planes */ ,
                    TypesOffsetPlanes/** offset planes */ ,
                    TypesPoints/** points */ ,
                    TypesBySupport/** by support */ 
                };

                /** Used to specify if a single or double offset and spacing definition is to be used. */
                public: enum OffsetSpacingModes
                {
                    OffsetSpacingModesSingle/** single */ ,
                    OffsetSpacingModesDouble/** double */ 
                };

                /** Used to specify how the spacing and offset is to be measured. */
                public: enum MeasureAlongModes
                {
                    MeasureAlongModesAlongSurfaceLength/** along surface length */ ,
                    MeasureAlongModesNormaltoPlane/** normalto plane */ ,
                    MeasureAlongModesAlongSurfaceChord/** along surface chord */ 
                };

                /** Used to specify whether points or planes are being used for the points definition. */
                public: enum PointMethods
                {
                    PointMethodsPlanes/** planes */ ,
                    PointMethodsPoints/** points */ 
                };

                /** Used to specify the type of end cut to be used at the extreme ends of the stiffener system. */
                public: enum EndCutTypes
                {
                    EndCutTypesConnected/** connected */ ,
                    EndCutTypesFlangeFree/** flange free */ ,
                    EndCutTypesSniped/** sniped */ ,
                    EndCutTypesSnipedSquare/** sniped square */ 
                };

                /** Used to specify the type of reference to use for specifying the orientation of the stiffener system. */
                public: enum OrientationMethods
                {
                    OrientationMethodsFaceNormal/** face normal */ ,
                    OrientationMethodsVector/** vector */ 
                };

                /** the mounting method offset type */
                public: enum MountingMethods
                {
                    MountingMethodsNoOffset/** No mounting offset */,
                    MountingMethodsAlongWeb/** Offset stiffener along web direction */,
                    MountingMethodsFaceNormal/** Offset stiffener along placement face normal */
                };

                private: StiffenerSystemBuilderImpl * m_stiffenersystembuilder_impl;
                private: friend class  _StiffenerSystemBuilderBuilder;
                protected: StiffenerSystemBuilder();
                public: ~StiffenerSystemBuilder();
                /**Returns  the method used to define the path of the stiffener system. 
                            Four types are supported: curves, planes, offset planes, and points. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::ShipDesign::StiffenerSystemBuilder::Types Type
                (
                );
                /**Sets  the method used to define the path of the stiffener system. 
                            Four types are supported: curves, planes, offset planes, and points. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : nx_ship_basic ("Ship Basic Design") */
                public: void SetType
                (
                    NXOpen::Features::ShipDesign::StiffenerSystemBuilder::Types type /** type */ 
                );
                /**Returns  the stock data used to define the stock information of the stiffener.
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::ShipDesign::StiffenerStockBuilder * StockData
                (
                );
                /**Returns  the indication whether the direction of the stiffener flange should be reversed. The default
                            direction is based on the ship structure that the stiffener is being built upon. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: bool Reverse
                (
                );
                /**Sets  the indication whether the direction of the stiffener flange should be reversed. The default
                            direction is based on the ship structure that the stiffener is being built upon. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : nx_ship_basic ("Ship Basic Design") */
                public: void SetReverse
                (
                    bool reverse /** reverse */ 
                );
                /**Returns  the ship structure upon which to create the stiffener system. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::SelectNXObjectList * ShipStructure
                (
                );
                /**Returns  the indication whether the side of the ship structure should be switched. The default
                            direction is based on the ship structure that the stiffener is being built upon. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: bool SwitchSide
                (
                );
                /**Sets  the indication whether the side of the ship structure should be switched. The default
                            direction is based on the ship structure that the stiffener is being built upon. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : nx_ship_basic ("Ship Basic Design") */
                public: void SetSwitchSide
                (
                    bool switchSide /** switchside */ 
                );
                /**Returns  the curves selected that define the path of the stiffener system. 
                            Only used when Type is @link NXOpen::Features::ShipDesign::StiffenerSystemBuilder::TypesCurves NXOpen::Features::ShipDesign::StiffenerSystemBuilder::TypesCurves@endlink . 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Section * Curves
                (
                );
                /**Returns  the planes selected that define the path of the stiffener system. 
                            Only used when Type is @link NXOpen::Features::ShipDesign::StiffenerSystemBuilder::TypesPlanes NXOpen::Features::ShipDesign::StiffenerSystemBuilder::TypesPlanes@endlink . 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::SelectNXObjectList * Planes
                (
                );
                /**Returns  the list of defined planes that define the path of the stiffener system. 
                            Only used when Type is @link NXOpen::Features::ShipDesign::StiffenerSystemBuilder::TypesPlanes NXOpen::Features::ShipDesign::StiffenerSystemBuilder::TypesPlanes@endlink . 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::ShipDesign::PlaneListBuilderList * PlaneList
                (
                );
                /**Returns  the first plane of the set of offset planes that define the path of the stiffener system. 
                            Only used when Type is @link NXOpen::Features::ShipDesign::StiffenerSystemBuilder::TypesOffsetPlanes NXOpen::Features::ShipDesign::StiffenerSystemBuilder::TypesOffsetPlanes@endlink . 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Plane * OffsetPlane
                (
                );
                /**Sets  the first plane of the set of offset planes that define the path of the stiffener system. 
                            Only used when Type is @link NXOpen::Features::ShipDesign::StiffenerSystemBuilder::TypesOffsetPlanes NXOpen::Features::ShipDesign::StiffenerSystemBuilder::TypesOffsetPlanes@endlink . 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : nx_ship_basic ("Ship Basic Design") */
                public: void SetOffsetPlane
                (
                    NXOpen::Plane * offsetPlane /** offsetplane */ 
                );
                /**Returns  the number of offset planes to generate that define the path of the stiffener system. 
                            Only used when Type is @link NXOpen::Features::ShipDesign::StiffenerSystemBuilder::TypesOffsetPlanes NXOpen::Features::ShipDesign::StiffenerSystemBuilder::TypesOffsetPlanes@endlink . 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: int OffsetNumber
                (
                );
                /**Sets  the number of offset planes to generate that define the path of the stiffener system. 
                            Only used when Type is @link NXOpen::Features::ShipDesign::StiffenerSystemBuilder::TypesOffsetPlanes NXOpen::Features::ShipDesign::StiffenerSystemBuilder::TypesOffsetPlanes@endlink . 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : nx_ship_basic ("Ship Basic Design") */
                public: void SetOffsetNumber
                (
                    int number /** number */ 
                );
                /**Returns  the indication whether spacing of the offset planes is defined at each end of the stiffener system, 
                            or if a constant spacing is desired. 
                            Only used when Type is @link NXOpen::Features::ShipDesign::StiffenerSystemBuilder::TypesOffsetPlanes NXOpen::Features::ShipDesign::StiffenerSystemBuilder::TypesOffsetPlanes@endlink . 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::ShipDesign::StiffenerSystemBuilder::OffsetSpacingModes OffsetSpacingMode
                (
                );
                /**Sets  the indication whether spacing of the offset planes is defined at each end of the stiffener system, 
                            or if a constant spacing is desired. 
                            Only used when Type is @link NXOpen::Features::ShipDesign::StiffenerSystemBuilder::TypesOffsetPlanes NXOpen::Features::ShipDesign::StiffenerSystemBuilder::TypesOffsetPlanes@endlink . 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : nx_ship_basic ("Ship Basic Design") */
                public: void SetOffsetSpacingMode
                (
                    NXOpen::Features::ShipDesign::StiffenerSystemBuilder::OffsetSpacingModes offsetSpacingMode /** offsetspacingmode */ 
                );
                /**Returns  the distance from the OffsetPlane to generate the first plane. 
                            Only used when Type is @link NXOpen::Features::ShipDesign::StiffenerSystemBuilder::TypesOffsetPlanes NXOpen::Features::ShipDesign::StiffenerSystemBuilder::TypesOffsetPlanes@endlink  
                            and OffsetSpacing is @link NXOpen::Features::ShipDesign::StiffenerSystemBuilder::OffsetSpacingModesSingle NXOpen::Features::ShipDesign::StiffenerSystemBuilder::OffsetSpacingModesSingle@endlink . 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * OffsetDistance
                (
                );
                /**Returns  the distance between generated planes. 
                            Only used when Type is @link NXOpen::Features::ShipDesign::StiffenerSystemBuilder::TypesOffsetPlanes NXOpen::Features::ShipDesign::StiffenerSystemBuilder::TypesOffsetPlanes@endlink  
                            and OffsetSpacing is @link NXOpen::Features::ShipDesign::StiffenerSystemBuilder::OffsetSpacingModesSingle NXOpen::Features::ShipDesign::StiffenerSystemBuilder::OffsetSpacingModesSingle@endlink . 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * OffsetSpacing
                (
                );
                /**Returns  the distance from the OffsetPlane to generate the location at the start of the stiffener system. 
                            Only used when Type is @link NXOpen::Features::ShipDesign::StiffenerSystemBuilder::TypesOffsetPlanes NXOpen::Features::ShipDesign::StiffenerSystemBuilder::TypesOffsetPlanes@endlink  
                            and OffsetSpacing is @link NXOpen::Features::ShipDesign::StiffenerSystemBuilder::OffsetSpacingModesDouble NXOpen::Features::ShipDesign::StiffenerSystemBuilder::OffsetSpacingModesDouble@endlink .
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * OffsetDistanceStart
                (
                );
                /**Returns  the distance between generated locations at the start of the stiffener system. 
                            Only used when Type is @link NXOpen::Features::ShipDesign::StiffenerSystemBuilder::TypesOffsetPlanes NXOpen::Features::ShipDesign::StiffenerSystemBuilder::TypesOffsetPlanes@endlink  
                            and OffsetSpacing is @link NXOpen::Features::ShipDesign::StiffenerSystemBuilder::OffsetSpacingModesDouble NXOpen::Features::ShipDesign::StiffenerSystemBuilder::OffsetSpacingModesDouble@endlink .
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * OffsetSpacingStart
                (
                );
                /**Returns  the distance from the OffsetPlane to generate the location at the end of the stiffener system. 
                            Only used when Type is @link NXOpen::Features::ShipDesign::StiffenerSystemBuilder::TypesOffsetPlanes NXOpen::Features::ShipDesign::StiffenerSystemBuilder::TypesOffsetPlanes@endlink  
                            and OffsetSpacing is @link NXOpen::Features::ShipDesign::StiffenerSystemBuilder::OffsetSpacingModesDouble NXOpen::Features::ShipDesign::StiffenerSystemBuilder::OffsetSpacingModesDouble@endlink .
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * OffsetDistanceEnd
                (
                );
                /**Returns  the distance between generated locations at the end of the stiffener system. 
                            Only used when Type is @link NXOpen::Features::ShipDesign::StiffenerSystemBuilder::TypesOffsetPlanes NXOpen::Features::ShipDesign::StiffenerSystemBuilder::TypesOffsetPlanes@endlink  
                            and OffsetSpacing is @link NXOpen::Features::ShipDesign::StiffenerSystemBuilder::OffsetSpacingModesDouble NXOpen::Features::ShipDesign::StiffenerSystemBuilder::OffsetSpacingModesDouble@endlink .
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * OffsetSpacingEnd
                (
                );
                /**Returns  the method used to measure distances between planes. 
                            Only used when Type is @link NXOpen::Features::ShipDesign::StiffenerSystemBuilder::TypesOffsetPlanes NXOpen::Features::ShipDesign::StiffenerSystemBuilder::TypesOffsetPlanes@endlink . 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::ShipDesign::StiffenerSystemBuilder::MeasureAlongModes MeasureAlongMode
                (
                );
                /**Sets  the method used to measure distances between planes. 
                            Only used when Type is @link NXOpen::Features::ShipDesign::StiffenerSystemBuilder::TypesOffsetPlanes NXOpen::Features::ShipDesign::StiffenerSystemBuilder::TypesOffsetPlanes@endlink . 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : nx_ship_basic ("Ship Basic Design") */
                public: void SetMeasureAlongMode
                (
                    NXOpen::Features::ShipDesign::StiffenerSystemBuilder::MeasureAlongModes measureAlongMode /** measurealongmode */ 
                );
                /**Returns  the list of pairs of planes that generate points on the ship structure to define the path of the stiffener system. 
                            Only used when Type is @link NXOpen::Features::ShipDesign::StiffenerSystemBuilder::TypesPoints NXOpen::Features::ShipDesign::StiffenerSystemBuilder::TypesPoints@endlink  
                            and PointMethod is @link NXOpen::Features::ShipDesign::StiffenerSystemBuilder::PointMethodsPlanes NXOpen::Features::ShipDesign::StiffenerSystemBuilder::PointMethodsPlanes@endlink . 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::NXObjectList * PlanePairList
                (
                );
                /**Returns  the method used to define the generated points on the ship structure to define the path of the stiffener system. 
                            Only used when Type is @link NXOpen::Features::ShipDesign::StiffenerSystemBuilder::TypesPoints NXOpen::Features::ShipDesign::StiffenerSystemBuilder::TypesPoints@endlink .
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::ShipDesign::StiffenerSystemBuilder::PointMethods PointMethod
                (
                );
                /**Sets  the method used to define the generated points on the ship structure to define the path of the stiffener system. 
                            Only used when Type is @link NXOpen::Features::ShipDesign::StiffenerSystemBuilder::TypesPoints NXOpen::Features::ShipDesign::StiffenerSystemBuilder::TypesPoints@endlink .
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : nx_ship_basic ("Ship Basic Design") */
                public: void SetPointMethod
                (
                    NXOpen::Features::ShipDesign::StiffenerSystemBuilder::PointMethods method /** method */ 
                );
                /**Returns  the list of selected or defined points that define the path of the stiffener system. 
                            Only used when Type is @link NXOpen::Features::ShipDesign::StiffenerSystemBuilder::TypesPoints NXOpen::Features::ShipDesign::StiffenerSystemBuilder::TypesPoints@endlink 
                            and PointMethod is @link NXOpen::Features::ShipDesign::StiffenerSystemBuilder::PointMethodsPoints NXOpen::Features::ShipDesign::StiffenerSystemBuilder::PointMethodsPoints@endlink . 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::NXObjectList * PointList
                (
                );
                /**Returns  the end cut to use at the start of the complete stiffener system. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::ShipDesign::StiffenerSystemBuilder::EndCutTypes EndCutStart
                (
                );
                /**Sets  the end cut to use at the start of the complete stiffener system. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : nx_ship_basic ("Ship Basic Design") */
                public: void SetEndCutStart
                (
                    NXOpen::Features::ShipDesign::StiffenerSystemBuilder::EndCutTypes endCutStart /** endcutstart */ 
                );
                /**Returns  the end cut to use at the end of the complete stiffener system. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::ShipDesign::StiffenerSystemBuilder::EndCutTypes EndCutEnd
                (
                );
                /**Sets  the end cut to use at the end of the complete stiffener system. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : nx_ship_basic ("Ship Basic Design") */
                public: void SetEndCutEnd
                (
                    NXOpen::Features::ShipDesign::StiffenerSystemBuilder::EndCutTypes endCutEnd /** endcutend */ 
                );
                /**Returns  the method used to define the reference for the orientation angle of stiffener system.
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::ShipDesign::StiffenerSystemBuilder::OrientationMethods OrientationMethod
                (
                );
                /**Sets  the method used to define the reference for the orientation angle of stiffener system.
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : nx_ship_basic ("Ship Basic Design") */
                public: void SetOrientationMethod
                (
                    NXOpen::Features::ShipDesign::StiffenerSystemBuilder::OrientationMethods orientationMethod /** orientationmethod */ 
                );
                /**Returns  the vector specified for the orientation angle reference. 
                            Only used when when Method is @link NXOpen::Features::ShipDesign::StiffenerSystemBuilder::OrientationMethodsVector NXOpen::Features::ShipDesign::StiffenerSystemBuilder::OrientationMethodsVector@endlink .. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Direction * OrientationVector
                (
                );
                /**Sets  the vector specified for the orientation angle reference. 
                            Only used when when Method is @link NXOpen::Features::ShipDesign::StiffenerSystemBuilder::OrientationMethodsVector NXOpen::Features::ShipDesign::StiffenerSystemBuilder::OrientationMethodsVector@endlink .. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : nx_ship_basic ("Ship Basic Design") */
                public: void SetOrientationVector
                (
                    NXOpen::Direction * orientationVector /** orientationvector */ 
                );
                /**Returns  the angle at which the stiffener system is placed relative to the reference.
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * OrientationAngle
                (
                );
                /**Returns  the builder used to specify the welding characteristics for the stiffener system. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Weld::CharacteristicsBuilder * Weld
                (
                );
                /** Creates a @link NXOpen::Features::ShipDesign::PlanePairBuilder NXOpen::Features::ShipDesign::PlanePairBuilder@endlink  to add another pair of planes to the list.  @return  
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : nx_ship_basic ("Ship Basic Design") */
                public: NXOpen::Features::ShipDesign::PlanePairBuilder * CreatePlanePairBuilder
                (
                );
                /**Returns  the path data used to define the support information of the stiffener.
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::ShipDesign::StiffenerBySupportPathBuilder * StiffenerBySupportPathData
                (
                );
                /**Returns  the connect angle of stiffener by support in degrees, negative value is not allowed 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: double ConnectAngle
                (
                );
                /**Sets  the connect angle of stiffener by support in degrees, negative value is not allowed 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_ship_detail ("Ship Detail Design") */
                public: void SetConnectAngle
                (
                    double connectAngle /** connectangle */ 
                );
                /**Returns  the flange set back option for stiffener by support, which indicates if the flange set back should be applied or not 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: bool ApplyFlangeSetback
                (
                );
                /**Sets  the flange set back option for stiffener by support, which indicates if the flange set back should be applied or not 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_ship_detail ("Ship Detail Design") */
                public: void SetApplyFlangeSetback
                (
                    bool applyFlangeSetback /** applyflangesetback */ 
                );
                /**Returns  the web set back option for stiffener by support, which indicates if the web set back should be applied or not 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: bool ApplyWebSetback
                (
                );
                /**Sets  the web set back option for stiffener by support, which indicates if the web set back should be applied or not 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_ship_detail ("Ship Detail Design") */
                public: void SetApplyWebSetback
                (
                    bool applyWebSetback /** applywebsetback */ 
                );
                /**Returns  the builder used to define the orientation for the stiffener system. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::ShipDesign::OrientationDefinitionBuilder * OrientationDefinitionBuilder
                (
                );
                /**Returns  the direction used to project the stiffener path object
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::GeometricUtilities::ProjectionOptions * ProjectionDirection
                (
                );
                /**Returns  the Ship Names builder, used to assign names to the Stiffener Systems created. 
                 <br>  Created in NX9.0.2.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::ShipDesign::ShipNamesBuilder * ShipNames
                (
                );
                /**Returns  the mounting method 
                 <br>  Created in NX10.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::ShipDesign::StiffenerSystemBuilder::MountingMethods MountingMethod
                (
                );
                /**Sets  the mounting method 
                 <br>  Created in NX10.0.0.  <br>  
                 <br> License requirements : nx_ship_basic ("Ship Basic Design") */
                public: void SetMountingMethod
                (
                    NXOpen::Features::ShipDesign::StiffenerSystemBuilder::MountingMethods mountingMethod /** mountingmethod */ 
                );
                /**Returns  the indication of whether to build a solid for the stiffener system or just the curve. 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : None */
                public: bool BuildSolid
                (
                );
                /**Sets  the indication of whether to build a solid for the stiffener system or just the curve. 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : nx_ship_basic ("Ship Basic Design") */
                public: void SetBuildSolid
                (
                    bool buildSolid /** buildsolid */ 
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
