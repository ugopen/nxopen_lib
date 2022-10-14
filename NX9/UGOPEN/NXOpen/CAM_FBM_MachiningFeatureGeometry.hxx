#ifndef NXOpen_CAM_FBM_MACHININGFEATUREGEOMETRY_HXX_INCLUDED
#define NXOpen_CAM_FBM_MACHININGFEATUREGEOMETRY_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_FBM_MachiningFeatureGeometry.ja
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
#include <NXOpen/CAM_Geometry.hxx>
#include <NXOpen/CAM_FBM_FeatureSet.hxx>
#include <NXOpen/CAM_FBM_MachiningFeatureGeometry.hxx>
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
        namespace FBM
        {
            class MachiningFeatureGeometry;
        }
    }
    namespace CAM
    {
        class CAMFeature;
    }
    namespace CAM
    {
        namespace FBM
        {
            class FeatureSet;
        }
    }
    namespace CAM
    {
        class Geometry;
    }
    namespace CAM
    {
        namespace FBM
        {
            class _MachiningFeatureGeometryBuilder;
            class MachiningFeatureGeometryImpl;
            /** Represents a feature geometry builder  <br> An instance of this class can be obtained from @link CAM::HoleBossGeom::GetCenterHoleGeometry CAM::HoleBossGeom::GetCenterHoleGeometry@endlink  or @link CAM::HoleBossGeom::GetChamferHoleGeometry CAM::HoleBossGeom::GetChamferHoleGeometry@endlink   <br> 
             <br>  Created in NX9.0.0.  <br>  
            */
            class NXOPENCPP_CAMEXPORT  MachiningFeatureGeometry : public CAM::Geometry
            {
                private: MachiningFeatureGeometryImpl * m_machiningfeaturegeometry_impl;
                private: friend class  _MachiningFeatureGeometryBuilder;
                protected: MachiningFeatureGeometry();
                public: ~MachiningFeatureGeometry();
                /** Create a new empty in process feature editor @return  the new in process feature set 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : cam_base ("CAM BASE") */
                public: NXOpen::CAM::FBM::FeatureSet * CreateFeatureSet
                (
                );
                /** Create a new in process feature editor @return  the new in process feature set 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : cam_base ("CAM BASE") */
                public: NXOpen::CAM::FBM::FeatureSet * AddFeatureSet
                (
                    NXOpen::CAM::CAMFeature * tagMachiningFeature /** the machining feature */,
                    const NXString & featureType /** the in process feature type */
                );
                /** Create a new in process feature editor @return  the new in process feature set 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : cam_base ("CAM BASE") */
                NXOpen::CAM::FBM::FeatureSet * AddFeatureSet
                (
                    NXOpen::CAM::CAMFeature * tagMachiningFeature /** the machining feature */,
                    const char * featureType /** the in process feature type */
                );
                /** Get the in process feature editor at the specified index  @return  the in process feature set 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : cam_base ("CAM BASE") */
                public: NXOpen::CAM::FBM::FeatureSet * GetFeatureSet
                (
                    int nIndex /** the index of the feature set editor */
                );
            };
        }
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