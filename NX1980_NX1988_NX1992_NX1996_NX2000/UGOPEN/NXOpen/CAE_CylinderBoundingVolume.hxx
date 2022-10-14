#ifndef NXOpen_CAE_CYLINDERBOUNDINGVOLUME_HXX_INCLUDED
#define NXOpen_CAE_CYLINDERBOUNDINGVOLUME_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_CylinderBoundingVolume.ja
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
#include <NXOpen/CAE_BoundingVolumePrimitive.hxx>
#include <NXOpen/libnxopencpp_cae_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace CAE
    {
        class CylinderBoundingVolume;
    }
    namespace CAE
    {
        class BoundingVolumePrimitive;
    }
    class CoordinateSystem;
    class Expression;
    class Point;
    namespace CAE
    {
        class _CylinderBoundingVolumeBuilder;
        class CylinderBoundingVolumeImpl;
        /** Represents Box Bounding Volume for Selection Recipe <br> This is a sub object  <br> 
         <br>  Created in NX12.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  CylinderBoundingVolume : public NXOpen::CAE::BoundingVolumePrimitive
        {
            /** Start Height Options */
            public: enum StartHeight
            {
                StartHeightNotDefined/** not defined */ ,
                StartHeightValue/** value */ ,
                StartHeightPositiveInfinity/** positive infinity */ ,
                StartHeightNegativeInfinity/** negative infinity */ 
            };

            /** End Height Options */
            public: enum EndHeight
            {
                EndHeightValue/** value */ ,
                EndHeightPositiveInfinity/** positive infinity */ ,
                EndHeightNegativeInfinity/** negative infinity */ 
            };

            /** Inner Diameter Options */
            public: enum InnerDiameter
            {
                InnerDiameterNotDefined/** not defined */ ,
                InnerDiameterValue/** value */ 
            };

            /** Outer Diameter Options */
            public: enum OuterDiameter
            {
                OuterDiameterValue/** value */ ,
                OuterDiameterInfinity/** infinity */ 
            };

            /** Start Angle Options */
            public: enum StartAngle
            {
                StartAngleNotDefined/** not defined */ ,
                StartAngleValue/** value */ 
            };

            /** End Angle Options */
            public: enum EndAngle
            {
                EndAngleNotDefined/** not defined */ ,
                EndAngleValue/** value */ 
            };

            private: CylinderBoundingVolumeImpl * m_cylinderboundingvolume_impl;
            private: friend class  _CylinderBoundingVolumeBuilder;
            protected: CylinderBoundingVolume();
            public: ~CylinderBoundingVolume();
            /**Gets the coordinate system, diameter and height for the Cylinder Bounding Volume.
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: void GetCsysDiameterHeight
            (
                NXOpen::CoordinateSystem ** centerCsys /** centercsys */ ,
                NXOpen::Expression ** diameter /** diameter */ ,
                NXOpen::Expression ** cylinderHeight /** cylinderheight */ 
            );
            /**Sets the coordinate system, diameter and height for the Cylinder Bounding Volume.
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetCsysDiameterHeight
            (
                NXOpen::CoordinateSystem * centerCsys /** centercsys */ ,
                NXOpen::Expression * diameter /** diameter */ ,
                NXOpen::Expression * cylinderHeight /** cylinderheight */ 
            );
            /**Gets the coordinate system, diameters and height for the Cylinder Bounding Volume.
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: void GetCsysDiametersHeight
            (
                NXOpen::CoordinateSystem ** centerCsys /** centercsys */ ,
                NXOpen::CAE::CylinderBoundingVolume::InnerDiameter* innerDiaOption /** innerdiaoption */ ,
                NXOpen::CAE::CylinderBoundingVolume::OuterDiameter* outerDiaOption /** outerdiaoption */ ,
                NXOpen::Expression ** innerDiameter /** innerdiameter */ ,
                NXOpen::Expression ** outerDiameter /** outerdiameter */ ,
                NXOpen::Expression ** cylinderHeight /** cylinderheight */ 
            );
            /**Sets the coordinate system, diameters and height for the Cylinder Bounding Volume.
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetCsysDiametersHeight
            (
                NXOpen::CoordinateSystem * centerCsys /** centercsys */ ,
                NXOpen::CAE::CylinderBoundingVolume::InnerDiameter innerDiaOption /** innerdiaoption */ ,
                NXOpen::CAE::CylinderBoundingVolume::OuterDiameter outerDiaOption /** outerdiaoption */ ,
                NXOpen::Expression * innerDiameter /** innerdiameter */ ,
                NXOpen::Expression * outerDiameter /** outerdiameter */ ,
                NXOpen::Expression * cylinderHeight /** cylinderheight */ 
            );
            /**Gets the coordinate system, diameter, height and angles for the Cylinder Bounding Volume.
             <br>  @deprecated Deprecated in NX1980.0.0.  Use @link NXOpen::CAE::CylinderBoundingVolume::GetCsysDiametersHeightsAngles NXOpen::CAE::CylinderBoundingVolume::GetCsysDiametersHeightsAngles@endlink  which uses inner dimensions as arguments. <br>  

             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX1980.0.0.  Use NXOpen::CAE::CylinderBoundingVolume::GetCsysDiametersHeightsAngles which uses inner dimensions as arguments.") void GetCsysDiameterHeightAngles
            (
                NXOpen::CoordinateSystem ** centerCsys /** centercsys */ ,
                NXOpen::Expression ** diameter /** diameter */ ,
                NXOpen::Expression ** cylinderHeight /** cylinderheight */ ,
                bool* isStartActive /** isstartactive */ ,
                NXOpen::Expression ** startAngle /** startangle */ ,
                bool* isEndActive /** isendactive */ ,
                NXOpen::Expression ** endAngle /** endangle */ 
            );
            /**Sets the coordinate system, diameter, height and angles for the Cylinder Bounding Volume.
             <br>  @deprecated Deprecated in NX1980.0.0.  Use @link NXOpen::CAE::CylinderBoundingVolume::SetCsysDiametersHeightsAngles NXOpen::CAE::CylinderBoundingVolume::SetCsysDiametersHeightsAngles@endlink  which uses inner dimensions as arguments. <br>  

             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NX_DEPRECATED("Deprecated in NX1980.0.0.  Use NXOpen::CAE::CylinderBoundingVolume::SetCsysDiametersHeightsAngles which uses inner dimensions as arguments.") void SetCsysDiameterHeightAngles
            (
                NXOpen::CoordinateSystem * centerCsys /** centercsys */ ,
                NXOpen::Expression * diameter /** diameter */ ,
                NXOpen::Expression * cylinderHeight /** cylinderheight */ ,
                bool isStartActive /** isstartactive */ ,
                NXOpen::Expression * startAngle /** startangle */ ,
                bool isEndActive /** isendactive */ ,
                NXOpen::Expression * endAngle /** endangle */ 
            );
            /**Gets the coordinate system, inner diameter, outer diameter and angles for the Cylinder Bounding Volume.
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: void GetCsysDiametersHeightsAngles
            (
                NXOpen::CoordinateSystem ** centerCsys /** centercsys */ ,
                NXOpen::Expression ** innerDiameter /** innerdiameter */ ,
                NXOpen::Expression ** outerDiameter /** outerdiameter */ ,
                NXOpen::Expression ** startHeight /** startheight */ ,
                NXOpen::Expression ** endHeight /** endheight */ ,
                NXOpen::Expression ** startAngle /** startangle */ ,
                NXOpen::Expression ** endAngle /** endangle */ ,
                NXOpen::CAE::CylinderBoundingVolume::InnerDiameter* innerDiaOption /** innerdiaoption */ ,
                NXOpen::CAE::CylinderBoundingVolume::OuterDiameter* outerDiaOption /** outerdiaoption */ ,
                NXOpen::CAE::CylinderBoundingVolume::StartHeight* startHeightOption /** startheightoption */ ,
                NXOpen::CAE::CylinderBoundingVolume::EndHeight* endHeightOption /** endheightoption */ ,
                NXOpen::CAE::CylinderBoundingVolume::StartAngle* startAngleOption /** startangleoption */ ,
                NXOpen::CAE::CylinderBoundingVolume::EndAngle* endAngleOption /** endangleoption */ 
            );
            /**Sets the coordinate system, inner diameter, outer diameter and angles for the Cylinder Bounding Volume.
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetCsysDiametersHeightsAngles
            (
                NXOpen::CoordinateSystem * centerCsys /** centercsys */ ,
                NXOpen::Expression * innerDiameter /** innerdiameter */ ,
                NXOpen::Expression * outerDiameter /** outerdiameter */ ,
                NXOpen::Expression * startHeight /** startheight */ ,
                NXOpen::Expression * endHeight /** endheight */ ,
                NXOpen::Expression * startAngle /** startangle */ ,
                NXOpen::Expression * endAngle /** endangle */ ,
                NXOpen::CAE::CylinderBoundingVolume::InnerDiameter innerDiaOption /** innerdiaoption */ ,
                NXOpen::CAE::CylinderBoundingVolume::OuterDiameter outerDiaOption /** outerdiaoption */ ,
                NXOpen::CAE::CylinderBoundingVolume::StartHeight startHeightOption /** startheightoption */ ,
                NXOpen::CAE::CylinderBoundingVolume::EndHeight endHeightOption /** endheightoption */ ,
                NXOpen::CAE::CylinderBoundingVolume::StartAngle startAngleOption /** startangleoption */ ,
                NXOpen::CAE::CylinderBoundingVolume::EndAngle endAngleOption /** endangleoption */ 
            );
            /**Gets the end points and diameter for the Cylinder Bounding Volume.
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: void GetEndpointsDiameter
            (
                NXOpen::Point ** baseCenter /** basecenter */ ,
                NXOpen::Point ** topCenter /** topcenter */ ,
                NXOpen::Expression ** diameter /** diameter */ 
            );
            /**Sets the end points and diameter for the Cylinder Bounding Volume.
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetEndpointsDiameter
            (
                NXOpen::Point * baseCenter /** basecenter */ ,
                NXOpen::Point * topCenter /** topcenter */ ,
                NXOpen::Expression * diameter /** diameter */ 
            );
            /**Gets the end points and diameters for the Cylinder Bounding Volume.
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: void GetEndpointsDiameters
            (
                NXOpen::Point ** baseCenter /** basecenter */ ,
                NXOpen::Point ** topCenter /** topcenter */ ,
                NXOpen::CAE::CylinderBoundingVolume::InnerDiameter* innerDiaOption /** innerdiaoption */ ,
                NXOpen::CAE::CylinderBoundingVolume::OuterDiameter* outerDiaOption /** outerdiaoption */ ,
                NXOpen::Expression ** innerDiameter /** innerdiameter */ ,
                NXOpen::Expression ** outerDiameter /** outerdiameter */ 
            );
            /**Sets the end points and diameters for the Cylinder Bounding Volume.
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetEndpointsDiameters
            (
                NXOpen::Point * baseCenter /** basecenter */ ,
                NXOpen::Point * topCenter /** topcenter */ ,
                NXOpen::CAE::CylinderBoundingVolume::InnerDiameter innerDiaOption /** innerdiaoption */ ,
                NXOpen::CAE::CylinderBoundingVolume::OuterDiameter outerDiaOption /** outerdiaoption */ ,
                NXOpen::Expression * innerDiameter /** innerdiameter */ ,
                NXOpen::Expression * outerDiameter /** outerdiameter */ 
            );
        };
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