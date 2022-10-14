#ifndef NXOpen_CAM_MIRRORBUILDER_HXX_INCLUDED
#define NXOpen_CAM_MIRRORBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_MirrorBuilder.ja
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
#include <NXOpen/CAM_MirrorBuilder.hxx>
#include <NXOpen/Builder.hxx>
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
        class MirrorBuilder;
    }
    class Builder;
    namespace CAM
    {
        class NCGroup;
    }
    class Plane;
    namespace CAM
    {
        class _MirrorBuilderBuilder;
        class MirrorBuilderImpl;
        /** Represents a Mirror Builder.  <br> To create a new instance of this class, use @link NXOpen::CAM::CAMSetup::CreateMirrorBuilder  NXOpen::CAM::CAMSetup::CreateMirrorBuilder @endlink  <br> 
         <br>  Created in NX9.0.3.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  MirrorBuilder : public NXOpen::Builder
        {
            private: MirrorBuilderImpl * m_mirrorbuilder_impl;
            private: friend class  _MirrorBuilderBuilder;
            protected: MirrorBuilder();
            public: ~MirrorBuilder();
            /**Returns  the mirror plane 
             <br>  Created in NX9.0.3.  <br>  
             <br> License requirements : None */
            public: NXOpen::Plane * Plane
            (
            );
            /**Sets  the mirror plane 
             <br>  Created in NX9.0.3.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetPlane
            (
                NXOpen::Plane * plane /** plane */ 
            );
            /**Returns  the selected program group 
             <br>  Created in NX9.0.3.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::NCGroup * ProgramGroup
            (
            );
            /**Sets  the selected program group 
             <br>  Created in NX9.0.3.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetProgramGroup
            (
                NXOpen::CAM::NCGroup * programGroup /** programgroup */ 
            );
            /**Returns  the selected geometry group 
             <br>  Created in NX9.0.3.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::NCGroup * GeometryGroup
            (
            );
            /**Sets  the selected geometry group 
             <br>  Created in NX9.0.3.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetGeometryGroup
            (
                NXOpen::CAM::NCGroup * geometryGroup /** geometrygroup */ 
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