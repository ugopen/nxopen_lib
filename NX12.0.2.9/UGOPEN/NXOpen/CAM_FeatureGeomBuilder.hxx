#ifndef NXOpen_CAM_FEATUREGEOMBUILDER_HXX_INCLUDED
#define NXOpen_CAM_FEATUREGEOMBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_FeatureGeomBuilder.ja
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
#include <NXOpen/CAM_NCGroupBuilder.hxx>
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
        class FeatureGeomBuilder;
    }
    namespace CAM
    {
        class GeometryCiBuilder;
    }
    namespace CAM
    {
        class InheritableDoubleBuilder;
    }
    namespace CAM
    {
        class LayoutCiBuilder;
    }
    namespace CAM
    {
        class NCGroupBuilder;
    }
    class NXObject;
    namespace CAM
    {
        class _FeatureGeomBuilderBuilder;
        class FeatureGeomBuilderImpl;
        /** Represents a FeatureGeom Builder  <br> This is an abstract class, and cannot be instantiated.  <br> 
         <br>  Created in NX5.0.0.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  FeatureGeomBuilder : public NXOpen::CAM::NCGroupBuilder
        {
            private: FeatureGeomBuilderImpl * m_featuregeombuilder_impl;
            private: friend class  _FeatureGeomBuilderBuilder;
            protected: FeatureGeomBuilder();
            public: ~FeatureGeomBuilder();
            /**Returns  the part material 
             <br>  @deprecated Deprecated in NX8.0.2.  Use method GetMaterialData instead. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: NX_DEPRECATED("Deprecated in NX8.0.2.  Use method GetMaterialData instead.") NXOpen::NXObject * PartMaterialBuilder
            (
            );
            /**Sets  the part material 
             <br>  @deprecated Deprecated in NX8.0.2.  Use method SetMaterial instead. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: NX_DEPRECATED("Deprecated in NX8.0.2.  Use method SetMaterial instead.") void SetPartMaterialBuilder
            (
                NXOpen::NXObject * partMaterial /** the part material tag */
            );
            /**Returns  the part offset (inheritable double)
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::InheritableDoubleBuilder * PartOffsetBuilder
            (
            );
            /**Returns  the blank offset (inheritable double)
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::InheritableDoubleBuilder * BlankOffsetBuilder
            (
            );
            /**Returns  the check offset (inheritable double)
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::InheritableDoubleBuilder * CheckOffsetBuilder
            (
            );
            /**Returns  the trim offset (inheritable double)
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::InheritableDoubleBuilder * TrimOffsetBuilder
            (
            );
            /**Returns  the geometry builder 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::GeometryCiBuilder * GeometryCiBuilder
            (
            );
            /**Returns  the save/layer layout builder 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::LayoutCiBuilder * LayoutCiBuilder
            (
            );
            /**Get part material @return  
             <br>  Created in NX8.0.1.  <br>  
             <br> License requirements : None */
            public: NXString GetMaterial
            (
            );
            /**Set part material
             <br>  Created in NX8.0.1.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetMaterial
            (
                const NXString & libRef /** libref */ 
            );
            /**Set part material
             <br>  Created in NX8.0.1.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            void SetMaterial
            (
                const char * libRef /** libref */ 
            );
            /** Get material data
             <br>  Created in NX8.0.2.  <br>  
             <br> License requirements : None */
            public: void GetMaterialData
            (
                NXString* libRef /** libref */ ,
                NXString* name /** name */ ,
                NXString* description /** description */ ,
                NXString* code /** code */ ,
                NXString* hardness /** hardness */ 
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