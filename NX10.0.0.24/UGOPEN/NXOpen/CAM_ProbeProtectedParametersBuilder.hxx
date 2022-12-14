#ifndef NXOpen_CAM_PROBEPROTECTEDPARAMETERSBUILDER_HXX_INCLUDED
#define NXOpen_CAM_PROBEPROTECTEDPARAMETERSBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_ProbeProtectedParametersBuilder.ja
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
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_cam_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace CAM
    {
        class ProbeProtectedParametersBuilder;
    }
    namespace CAM
    {
        class _ProbeProtectedParametersBuilderBuilder;
        class ProbeProtectedParametersBuilderImpl;
        /** Represents the Probe Protected Parameters Builder 
         <br>  Created in NX5.0.0.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  ProbeProtectedParametersBuilder : public NXOpen::TaggedObject
        {
            /** the collision flag types */
            public: enum CollisionFlagTypes
            {
                CollisionFlagTypesAlarm/** PATH OBSTRUCTED alarm */,
                CollisionFlagTypesFlag/** Error flag */
            };

            /** the approach types */
            public: enum AppMethodTypes
            {
                AppMethodTypesNone/** none */,
                AppMethodTypesClearance/** from/to clearance */,
                AppMethodTypesDirect/** direct */,
                AppMethodTypesRadialAxial/** radial and then axial */,
                AppMethodTypesAxialRadial/** axial and then radial */,
                AppMethodTypesRadialAxialWithClearance/** radial and then axial from/to clearance */,
                AppMethodTypesAxialRadialWithClearance/** axial and then radial from/to clearance */
            };

            /** the departure types */
            public: enum DepMethodTypes
            {
                DepMethodTypesNone/** none */,
                DepMethodTypesClearance/** from/to clearance */
            };

            private: ProbeProtectedParametersBuilderImpl * m_probeprotectedparametersbuilder_impl;
            private: friend class  _ProbeProtectedParametersBuilderBuilder;
            protected: ProbeProtectedParametersBuilder();
            public: ~ProbeProtectedParametersBuilder();
            /**Returns  the standoff distance 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: double StandoffDistance
            (
            );
            /**Sets  the standoff distance 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetStandoffDistance
            (
                double standoffDistance /** standoffdistance */ 
            );
            /**Returns  the safe clearance distance for external features 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: double ClearanceDistance
            (
            );
            /**Sets  the safe clearance distance for external features 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetClearanceDistance
            (
                double clearanceDistance /** clearancedistance */ 
            );
            /**Returns  the approach from clearance plane flag 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::ProbeProtectedParametersBuilder::AppMethodTypes ApproachFlag
            (
            );
            /**Sets  the approach from clearance plane flag 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetApproachFlag
            (
                NXOpen::CAM::ProbeProtectedParametersBuilder::AppMethodTypes approachFrom /** approach from */ 
            );
            /**Returns  the return to clearance plane flag 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::ProbeProtectedParametersBuilder::DepMethodTypes ReturnFlag
            (
            );
            /**Sets  the return to clearance plane flag 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetReturnFlag
            (
                NXOpen::CAM::ProbeProtectedParametersBuilder::DepMethodTypes returnTo /** return to */ 
            );
            /**Returns  the collision flag 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::ProbeProtectedParametersBuilder::CollisionFlagTypes CollisionFlag
            (
            );
            /**Sets  the collision flag 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetCollisionFlag
            (
                NXOpen::CAM::ProbeProtectedParametersBuilder::CollisionFlagTypes collFlag /** coll flag */ 
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
