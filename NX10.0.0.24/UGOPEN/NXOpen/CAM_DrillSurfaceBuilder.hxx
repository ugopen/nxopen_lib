#ifndef NXOpen_CAM_DRILLSURFACEBUILDER_HXX_INCLUDED
#define NXOpen_CAM_DRILLSURFACEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_DrillSurfaceBuilder.ja
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
        class DrillSurfaceBuilder;
    }
    class NXObject;
    namespace CAM
    {
        class _DrillSurfaceBuilderBuilder;
        class DrillSurfaceBuilderImpl;
        /** Represents a Drill Surface Builder  <br> This is an abstract class and cannot be instantiated.  <br> 
         <br>  Created in NX7.5.0.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  DrillSurfaceBuilder : public NXOpen::TaggedObject
        {
            /** Drill surface type */
            public: enum SurfaceType
            {
                SurfaceTypeFace/** face */,
                SurfaceTypePlane/** plane */,
                SurfaceTypeZcConstant/** zc constant */,
                SurfaceTypeNone/** none */
            };

            private: DrillSurfaceBuilderImpl * m_drillsurfacebuilder_impl;
            private: friend class  _DrillSurfaceBuilderBuilder;
            protected: DrillSurfaceBuilder();
            public: ~DrillSurfaceBuilder();
            /**Returns  the surface option 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::DrillSurfaceBuilder::SurfaceType SurfaceOption
            (
            );
            /**Sets  the surface option 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetSurfaceOption
            (
                NXOpen::CAM::DrillSurfaceBuilder::SurfaceType surfaceOption /** surfaceoption */ 
            );
            /**Returns  the selected surface,surface entity type covers Xform,Plane and Face 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::NXObject * Surface
            (
            );
            /**Sets  the selected surface,surface entity type covers Xform,Plane and Face 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetSurface
            (
                NXOpen::NXObject * surface /** entity type can be XFORM, PLANE or FACE.If surface type is PLANE, zcConstant value also is changed based on it */
            );
            /**Returns  the zc constant, will create one plane based on this value 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: double ZcConstant
            (
            );
            /**Sets  the zc constant, will create one plane based on this value 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetZcConstant
            (
                double zcConstant /** zcconstant */ 
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
