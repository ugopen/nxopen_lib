#ifndef NXOpen_FEATURES_GRIDTARGETBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_GRIDTARGETBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_GridTargetBuilder.ja
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
        class GridTargetBuilder;
    }
    class Direction;
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
    namespace Features
    {
        class _GridTargetBuilderBuilder;
        class GridTargetBuilderImpl;

        /// \cond NX_NO_DOC 
        /**
            Represents a @link Features::GridTarget Features::GridTarget@endlink  builder
             <br> To create a new instance of this class, use @link NXOpen::Features::AVDACollection::CreateGridTargetBuilder  NXOpen::Features::AVDACollection::CreateGridTargetBuilder @endlink  <br> 
        Default values.
        <list type="table"> 
         
        <listheader><term> 
        Property</term>  <description> 
        Value</description> </listheader>
        <item><term> 
         
        AngleIncrement.Value </term> <description> 
         
        15 </description> </item> 

        <item><term> 
         
        BoundaryOffset.Value </term> <description> 
         
        1000 (millimeters part), 39.370 (inches part) </description> </item> 

        <item><term> 
         
        DisplayAngleValues </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        DriverSideForGrid </term> <description> 
         
        LeftDriven </description> </item> 

        <item><term> 
         
        EndAngle.Value </term> <description> 
         
        75 </description> </item> 

        <item><term> 
         
        EndRadius.Value </term> <description> 
         
        12000 (millimeters part), 472.441 (inches part) </description> </item> 

        <item><term> 
         
        GridLocation </term> <description> 
         
        Floor </description> </item> 

        <item><term> 
         
        GridPosition </term> <description> 
         
        FrontSide </description> </item> 

        <item><term> 
         
        GridType </term> <description> 
         
        Quadrilateral </description> </item> 

        <item><term> 
         
        RadLinesAngleIncrement.Value </term> <description> 
         
        45 </description> </item> 

        <item><term> 
         
        RadiusIncrement.Value </term> <description> 
         
        3000 (millimeters part), 118.110 (inches part) </description> </item> 

        <item><term> 
         
        ReferencePointMethod </term> <description> 
         
        DirectVision </description> </item> 

        <item><term> 
         
        ShowRadiatingLines </term> <description> 
         
        1 </description> </item> 

        <item><term> 
         
        ShowRectangularBoundary </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        Standard </term> <description> 
         
        ECER46ClassI </description> </item> 

        <item><term> 
         
        StartAngle.Value </term> <description> 
         
        15 </description> </item> 

        <item><term> 
         
        StartRadius.Value </term> <description> 
         
        3000 (millimeters part), 118.110 (inches part) </description> </item> 

        <item><term> 
         
        TargetDistanceFar.Value </term> <description> 
         
        0 (millimeters part), 0 (inches part) </description> </item> 

        <item><term> 
         
        TargetDistanceInfinite.Value </term> <description> 
         
        0 (millimeters part), 0 (inches part) </description> </item> 

        <item><term> 
         
        TargetDistanceNear.Value </term> <description> 
         
        0 (millimeters part), 0 (inches part) </description> </item> 

        <item><term> 
         
        TargetDistanceRef </term> <description> 
         
        DriverOcularPoint </description> </item> 

        <item><term> 
         
        TargetWidthFar.Value </term> <description> 
         
        0 (millimeters part), 0 (inches part) </description> </item> 

        <item><term> 
         
        TargetWidthInfinite.Value </term> <description> 
         
        0 (millimeters part), 0 (inches part) </description> </item> 

        <item><term> 
         
        TargetWidthNear.Value </term> <description> 
         
        0 (millimeters part), 0 (inches part) </description> </item> 

        <item><term> 
         
        UseLoadingSpecifiedStandard </term> <description> 
         
        1 </description> </item> 

        </list> 

         <br>  Created in NX1953.0.0.  <br>  
        */
        class NXOPENCPP_FEATURESEXPORT  GridTargetBuilder : public NXOpen::Features::FeatureBuilder
        {
            /**
                    Used to indicate the grid location
                    */
            public: enum GridLocations
            {
                GridLocationsFloor/** floor */ ,
                GridLocationsWall/** wall */ ,
                GridLocationsNotDefined/** not defined */ 
            };

            /**
                    Used to indicate the grid standard
                    */
            public: enum GridStandards
            {
                GridStandardsECER46ClassI/** ecer46class i */ ,
                GridStandardsECER46ClassII/** ecer46class ii */ ,
                GridStandardsECER46ClassIII/** ecer46class iii */ ,
                GridStandardsECER46ClassIV/** ecer46class iv */ ,
                GridStandardsECER46ClassVClose/** ecer46class vclose */ ,
                GridStandardsECER46ClassVLarge/** ecer46class vlarge */ ,
                GridStandardsECER46ClassVI/** ecer46class vi */ ,
                GridStandardsECER46ClassVII/** ecer46class vii */ ,
                GridStandardsIso5006/** iso5006 */ ,
                GridStandardsIso5721/** iso5721 */ ,
                GridStandardsISO57212Behind/** iso57212behind */ ,
                GridStandardsISO57212Side/** iso57212side */ ,
                GridStandardsISO144012FOVClassA/** iso144012fovclass a */ ,
                GridStandardsISO144012FOVClassB/** iso144012fovclass b */ ,
                GridStandardsISO144012FOVClassC/** iso144012fovclass c */ ,
                GridStandardsISO144012FOVClassD/** iso144012fovclass d */ ,
                GridStandardsMLIT44TruckLT8t/** mlit44truck lt8t */ ,
                GridStandardsMLIT44TruckGE8t/** mlit44truck ge8t */ ,
                GridStandardsUsacanadafmvss111cmvsss111/** usacanadafmvss111cmvsss111 */ ,
                GridStandardsUserDefined/** user defined */ ,
                GridStandardsNotDefined/** not defined */ 
            };

            /**
                    Used to indicate the driver side for center driven vehicle
                    */
            public: enum GridDriverSide
            {
                GridDriverSideLeftDriven/** left driven */ ,
                GridDriverSideRightDriven/** right driven */ ,
                GridDriverSideCenterDriven/** center driven */ ,
                GridDriverSideNotDefined/** not defined */ 
            };

            /**
                    Used to indicate the position of grid whether it is on front, left, rear or right
                    */
            public: enum GridPositions
            {
                GridPositionsFrontSide/** front side */ ,
                GridPositionsLeftSide/** left side */ ,
                GridPositionsRearSide/** rear side */ ,
                GridPositionsRightSide/** right side */ ,
                GridPositionsNotDefined/** not defined */ 
            };

            /**
                    Used to indicate the grid types based on grid shape
                    */
            public: enum GridTypes
            {
                GridTypesCircularRadius/** circular radius */ ,
                GridTypesCircularConical/** circular conical */ ,
                GridTypesCircularDefaultConical/** circular default conical */ ,
                GridTypesQuadrilateral/** quadrilateral */ ,
                GridTypesPentagonal/** pentagonal */ ,
                GridTypesLShape/** lshape */ ,
                GridTypesStandard/** standard */ 
            };

            /**
                    Used to indicate the point selection type for grid 
                    */
            public: enum GridPointSelectionType
            {
                GridPointSelectionTypeDirectVision/** direct vision */ ,
                GridPointSelectionTypeExistingPoint/** existing point */ ,
                GridPointSelectionTypeNotDefined/** not defined */ 
            };

            /**
                    Used to indicate reference for target distance
                    */
            public: enum TargetDistanceReferences
            {
                TargetDistanceReferencesDriverOcularPoint/** driver ocular point */ ,
                TargetDistanceReferencesVehicleRearSide/** vehicle rear side */ 
            };

            private: GridTargetBuilderImpl * m_gridtargetbuilder_impl;
            private: friend class  _GridTargetBuilderBuilder;
            protected: GridTargetBuilder();
            public: ~GridTargetBuilder();

            /// \cond NX_NO_DOC 
            /**Returns  the grid location 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::GridTargetBuilder::GridLocations GridLocation
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the grid location 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : vehicle_des_val (" Vehicle Design and Validation") */
            public: void SetGridLocation
            (
                NXOpen::Features::GridTargetBuilder::GridLocations gridLocation /** gridlocation */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the standard 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::GridTargetBuilder::GridStandards Standard
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the standard 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : vehicle_des_val (" Vehicle Design and Validation") */
            public: void SetStandard
            (
                NXOpen::Features::GridTargetBuilder::GridStandards standard /** standard */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the use loading specified standard 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: bool UseLoadingSpecifiedStandard
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the use loading specified standard 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : vehicle_des_val (" Vehicle Design and Validation") */
            public: void SetUseLoadingSpecifiedStandard
            (
                bool useLoadingSpecifiedStandard /** useloadingspecifiedstandard */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the driver side for center driven 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::GridTargetBuilder::GridDriverSide DriverSideForGrid
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the driver side for center driven 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : vehicle_des_val (" Vehicle Design and Validation") */
            public: void SetDriverSideForGrid
            (
                NXOpen::Features::GridTargetBuilder::GridDriverSide driverSideForGrid /** driversideforgrid */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the loading 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: NXString Loading
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the loading 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : vehicle_des_val (" Vehicle Design and Validation") */
            public: void SetLoading
            (
                const NXString & loading /** loading */ 
            );
            /**Sets  the loading 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : vehicle_des_val (" Vehicle Design and Validation") */
            void SetLoading
            (
                const char * loading /** loading */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the grid position 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::GridTargetBuilder::GridPositions GridPosition
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the grid position 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : vehicle_des_val (" Vehicle Design and Validation") */
            public: void SetGridPosition
            (
                NXOpen::Features::GridTargetBuilder::GridPositions gridPosition /** gridposition */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the grid type 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::GridTargetBuilder::GridTypes GridType
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the grid type 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : vehicle_des_val (" Vehicle Design and Validation") */
            public: void SetGridType
            (
                NXOpen::Features::GridTargetBuilder::GridTypes gridType /** gridtype */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the reference point method 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::GridTargetBuilder::GridPointSelectionType ReferencePointMethod
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the reference point method 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : vehicle_des_val (" Vehicle Design and Validation") */
            public: void SetReferencePointMethod
            (
                NXOpen::Features::GridTargetBuilder::GridPointSelectionType referencePointMethod /** referencepointmethod */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the direct vision 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::SelectFeature * DirectVision
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the grid reference point 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Point * GridReferencePoint
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the grid reference point 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : vehicle_des_val (" Vehicle Design and Validation") */
            public: void SetGridReferencePoint
            (
                NXOpen::Point * gridReferencePoint /** gridreferencepoint */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the ground wide point 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Point * GroundWidePoint
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the ground wide point 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : vehicle_des_val (" Vehicle Design and Validation") */
            public: void SetGroundWidePoint
            (
                NXOpen::Point * groundWidePoint /** groundwidepoint */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the start radius 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * StartRadius
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the end radius 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * EndRadius
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the radius increment 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * RadiusIncrement
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the start angle 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * StartAngle
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the end angle 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * EndAngle
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the angle increment 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * AngleIncrement
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the show radiating lines 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: bool ShowRadiatingLines
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the show radiating lines 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : vehicle_des_val (" Vehicle Design and Validation") */
            public: void SetShowRadiatingLines
            (
                bool showRadiatingLines /** showradiatinglines */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the start direction 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Direction * StartDirection
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the start direction 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : vehicle_des_val (" Vehicle Design and Validation") */
            public: void SetStartDirection
            (
                NXOpen::Direction * startDirection /** startdirection */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the rad lines angle increment 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * RadLinesAngleIncrement
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the display angle values 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: bool DisplayAngleValues
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the display angle values 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : vehicle_des_val (" Vehicle Design and Validation") */
            public: void SetDisplayAngleValues
            (
                bool displayAngleValues /** displayanglevalues */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the show rectangular boundary 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: bool ShowRectangularBoundary
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the show rectangular boundary 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : vehicle_des_val (" Vehicle Design and Validation") */
            public: void SetShowRectangularBoundary
            (
                bool showRectangularBoundary /** showrectangularboundary */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the boundary offset 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * BoundaryOffset
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the target distance ref 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::GridTargetBuilder::TargetDistanceReferences TargetDistanceRef
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the target distance ref 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : vehicle_des_val (" Vehicle Design and Validation") */
            public: void SetTargetDistanceRef
            (
                NXOpen::Features::GridTargetBuilder::TargetDistanceReferences targetDistanceRef /** targetdistanceref */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the target distance near 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * TargetDistanceNear
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the target width near 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * TargetWidthNear
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the target distance far 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * TargetDistanceFar
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the target width far 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * TargetWidthFar
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the target distance infinite 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * TargetDistanceInfinite
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the target width infinite 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * TargetWidthInfinite
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Create ground wide point 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Point * CreateGroundWidePointForGrid
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Create outer ground contact point 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Point * CreateOuterGroundContactPoint
            (
            );

            /// \endcond 
        };

        /// \endcond 
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
