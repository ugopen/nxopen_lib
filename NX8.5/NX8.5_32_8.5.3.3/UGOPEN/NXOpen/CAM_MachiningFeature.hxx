#ifndef NXOpen_CAM_MACHININGFEATURE_HXX_INCLUDED
#define NXOpen_CAM_MACHININGFEATURE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_MachiningFeature.ja
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
#include <NXOpen/CAM_MachiningFeature.hxx>
#include <NXOpen/ObjectList.hxx>
#include <NXOpen/ScCollector.hxx>
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
        class MachiningFeature;
    }
    namespace CAM
    {
        class CAMFeatureList;
    }
    class CoordinateSystem;
    class ScCollector;
    namespace CAM
    {
        class _MachiningFeatureBuilder;
        class MachiningFeatureImpl;
        /** Represents a @link CAM::CAMFeature CAM::CAMFeature@endlink  builder  <br> To obtain an instance of this class use @link CAM::FeatureRecognitionBuilder CAM::FeatureRecognitionBuilder@endlink   <br> 
         <br>  Created in NX8.0.0.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  MachiningFeature : public TaggedObject
        {
            private: MachiningFeatureImpl * m_machiningfeature_impl;
            private: friend class  _MachiningFeatureBuilder;
            protected: MachiningFeature();
            public: ~MachiningFeature();
            /**Returns  the feature type of the feature to create 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXString FeatureType
            (
            );
            /**Sets  the feature type of the feature to create 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetFeatureType
            (
                const NXString & name /** name */ 
            );
            /**Sets  the feature type of the feature to create 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            void SetFeatureType
            (
                const char * name /** name */ 
            );
            /**Returns  the face selection 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::ScCollector * Faces
            (
            );
            /**Returns  the list features 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::CAMFeatureList * Features
            (
            );
            /**Returns  the csys feature 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CoordinateSystem * CoordinateSystem
            (
            );
            /**Sets  the csys feature 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetCoordinateSystem
            (
                NXOpen::CoordinateSystem * csysFeature /** csysfeature */ 
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
