#ifndef NXOpen_CAM_MULTIBLADEBASEGEOMETRY_HXX_INCLUDED
#define NXOpen_CAM_MULTIBLADEBASEGEOMETRY_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_MultiBladeBaseGeometry.ja
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
#include <NXOpen/CAM_MultiBladeBaseGeometry.hxx>
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
        class MultiBladeBaseGeometry;
    }
    class NXObject;
    namespace CAM
    {
        class _MultiBladeBaseGeometryBuilder;
        class MultiBladeBaseGeometryImpl;
        /** Represents a selectoin geometry Builder  <br> This is an abstract class and cannot be instantiated.  <br> 
         <br>  Created in NX7.0.0.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  MultiBladeBaseGeometry : public TaggedObject
        {
            private: MultiBladeBaseGeometryImpl * m_multibladebasegeometry_impl;
            private: friend class  _MultiBladeBaseGeometryBuilder;
            protected: MultiBladeBaseGeometry();
            public: ~MultiBladeBaseGeometry();
            /** Get the selection faces  @return  the selected faces 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXOpen::NXObject *> GetFaces
            (
            );
            /** Set the selection faces 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetFaces
            (
                const std::vector<NXOpen::NXObject *> & faces /** the selected faces */
            );
            /** Remove the faces 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void RemoveFaces
            (
                const std::vector<NXOpen::NXObject *> & faces /** the deselection faces */
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