#ifndef NXOpen_CAM_FEATUREGEOMETRYGROUP_HXX_INCLUDED
#define NXOpen_CAM_FEATUREGEOMETRYGROUP_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_FeatureGeometryGroup.ja
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
#include <NXOpen/CAM_FeatureGeometry.hxx>
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
        class FeatureGeometryGroup;
    }
    namespace CAM
    {
        class CAMFeature;
    }
    namespace CAM
    {
        class FeatureGeometry;
    }
    namespace CAM
    {
        class Operation;
    }
    namespace CAM
    {
        class _FeatureGeometryGroupBuilder;
        class FeatureGeometryGroupImpl;
        /** Represents a CAM Feature Group  <br> To obtain an instance of this class use @link NXOpen::CAM::FeatureRecognitionBuilder NXOpen::CAM::FeatureRecognitionBuilder@endlink   <br> 
         <br>  Created in NX8.0.0.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  FeatureGeometryGroup : public NXOpen::CAM::FeatureGeometry
        {
            /** Update status of the feature */
            public: enum ProcessStatus
            {
                ProcessStatusUnknown/** Feature group status is unknown */,
                ProcessStatusOk/** Feature group status is ok */,
                ProcessStatusSuspect/** Feature group status is suspected */
            };

            private: FeatureGeometryGroupImpl * m_featuregeometrygroup_impl;
            private: friend class  _FeatureGeometryGroupBuilder;
            protected: FeatureGeometryGroup();
            public: ~FeatureGeometryGroup();
            /**Returns  the name of the feature group 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXString Name
            (
            );
            /**Sets  the name of the feature group 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetName
            (
                const NXString & name /** name */ 
            );
            /**Sets  the name of the feature group 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            void SetName
            (
                const char * name /** name */ 
            );
            /**Returns  the feature type of the feature group 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXString Type
            (
            );
            /** Get the status of the input object.  @return  the object's status 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::CAMObject::Status GetStatus
            (
            );
            /**Returns  the update status of the feature group 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::FeatureGeometryGroup::ProcessStatus Status
            (
            );
            /** Get the features in the feature group   @return  
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXOpen::CAM::CAMFeature *> GetFeatures
            (
            );
            /** Get the operations of the feature group  @return  
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXOpen::CAM::Operation *> GetOperations
            (
            );
            /** Adds a feature to the feature geometry group 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void AddFeature
            (
                NXOpen::CAM::CAMFeature * feature /** feature */ 
            );
            /** Removes a feature from the feature geometry group 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void RemoveFeature
            (
                NXOpen::CAM::CAMFeature * feature /** feature */ 
            );
            /** Redistributes the geometry of the feature geometry group 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void Redistribute
            (
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