#ifndef NXOpen_CAM_CHAMFERMILLINGBUILDER_HXX_INCLUDED
#define NXOpen_CAM_CHAMFERMILLINGBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_ChamferMillingBuilder.ja
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
#include <NXOpen/CAM_ChamferMillingBuilder.hxx>
#include <NXOpen/CAM_HoleMachiningBuilder.hxx>
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
        class ChamferMillingBuilder;
    }
    namespace CAM
    {
        class FeatureMillingCutParameters;
    }
    namespace CAM
    {
        class HoleMachiningBuilder;
    }
    namespace CAM
    {
        class _ChamferMillingBuilderBuilder;
        class ChamferMillingBuilderImpl;
        /** Represents a ChamferMillingBuilder Builder  <br> To create a new instance of this class, use @link NXOpen::CAM::OperationCollection::CreateChamferMillingBuilder  NXOpen::CAM::OperationCollection::CreateChamferMillingBuilder @endlink  <br> 
         <br>  Created in NX9.0.2.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  ChamferMillingBuilder : public NXOpen::CAM::HoleMachiningBuilder
        {
            private: ChamferMillingBuilderImpl * m_chamfermillingbuilder_impl;
            private: friend class  _ChamferMillingBuilderBuilder;
            protected: ChamferMillingBuilder();
            public: ~ChamferMillingBuilder();
            /**Returns  the Chamfer Milling Cut Parameters 
             <br>  @deprecated Deprecated in NX9.0.3.  Use @link CAM::HoleMachiningBuilder::CuttingParameters CAM::HoleMachiningBuilder::CuttingParameters@endlink  instead. <br>  

             <br>  Created in NX9.0.2.  <br>  
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX9.0.3.  Use CAM::HoleMachiningBuilder::CuttingParameters instead.") NXOpen::CAM::FeatureMillingCutParameters * CutParameters
            (
            );
            /**Returns  the drive point 
             <br>  Created in NX9.0.2.  <br>  
             <br> License requirements : None */
            public: NXString DrivePoint
            (
            );
            /**Sets  the drive point 
             <br>  Created in NX9.0.2.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetDrivePoint
            (
                const NXString & drivePoint /** The drive point name */
            );
            /**Sets  the drive point 
             <br>  Created in NX9.0.2.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            void SetDrivePoint
            (
                const char * drivePoint /** The drive point name */
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
