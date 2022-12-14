#ifndef NXOpen_CAM_LASERHEADORIENTATION_HXX_INCLUDED
#define NXOpen_CAM_LASERHEADORIENTATION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_LaserHeadOrientation.ja
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
        class LaserHeadOrientation;
    }
    class CartesianCoordinateSystem;
    namespace CAM
    {
        class _LaserHeadOrientationBuilder;
        class LaserHeadOrientationImpl;
        /** Represents head orientation settings for laser sub move 
         <br>  Created in NX9.0.0.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  LaserHeadOrientation : public NXOpen::TaggedObject
        {
            /** the Head Orientation Type enum 
             <br>  Created in NX9.0.0.  <br>  
            */
            public: enum Types
            {
                TypesNoChange/** No Change */,
                TypesMcsZy/** MCS Z/Y */,
                TypesSpecify/** Specify */,
                TypesDynamic/** Dynamic */,
                TypesNormalToPart/** Normal to Part*/
            };

            private: LaserHeadOrientationImpl * m_laserheadorientation_impl;
            private: friend class  _LaserHeadOrientationBuilder;
            protected: LaserHeadOrientation();
            public: ~LaserHeadOrientation();
            /**Returns  the Head Orientation Type 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::LaserHeadOrientation::Types OrientationType
            (
            );
            /**Sets  the Head Orientation Type 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetOrientationType
            (
                NXOpen::CAM::LaserHeadOrientation::Types type /** the head orientation type*/
            );
            /**Returns  the Head Orientation 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CartesianCoordinateSystem * Csys
            (
            );
            /**Sets  the Head Orientation 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetCsys
            (
                NXOpen::CartesianCoordinateSystem * mcs /** the head orientation */
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
