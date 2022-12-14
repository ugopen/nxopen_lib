#ifndef NXOpen_CAM_NCMTRANSFERTYPES_HXX_INCLUDED
#define NXOpen_CAM_NCMTRANSFERTYPES_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_NcmTransferTypes.ja
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
        class NcmTransferTypes;
    }
    namespace CAM
    {
        class InheritableToolDepBuilder;
    }
    namespace CAM
    {
        class NcmTransferBuilder;
    }
    namespace CAM
    {
        class _NcmTransferTypesBuilder;
        class NcmTransferTypesImpl;
        /**
            Represents a @link CAM::NcmTransferTypes CAM::NcmTransferTypes@endlink 
            
         <br>  Created in NX10.0.1.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  NcmTransferTypes : public NXOpen::TaggedObject
        {
            /** Available types for initial clearance in hole machining */
            public: enum InitialTypes
            {
                InitialTypesClearance/** Clearance - Tool Axis */,
                InitialTypesDistance/** distance */,
                InitialTypesNone/** none */,
                InitialTypesBlankPlane/** blank plane */,
                InitialTypesClearanceShortestDistance/** Clearance - Shortest Distance */,
                InitialTypesClearanceCutPlane/** Clearance - Cut Plane */
            };

            /** Available types for final clearance in hole machining */
            public: enum FinalTypes
            {
                FinalTypesClearance/** clearance */,
                FinalTypesDistance/** distance */,
                FinalTypesNone/** none */,
                FinalTypesClearanceShortestDistance/** Clearance - Shortest Distance */,
                FinalTypesClearanceCutPlane/** Clearance - Cut Plane */
            };

            private: NcmTransferTypesImpl * m_ncmtransfertypes_impl;
            private: friend class  _NcmTransferTypesBuilder;
            protected: NcmTransferTypes();
            public: ~NcmTransferTypes();
            /**Returns  the transfer settings for initial and final 
             <br>  Created in NX10.0.1.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::NcmTransferBuilder * TransferInitialFinal
            (
            );
            /**Returns  the initial type 
             <br>  Created in NX10.0.1.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::NcmTransferTypes::InitialTypes InitialType
            (
            );
            /**Sets  the initial type 
             <br>  Created in NX10.0.1.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetInitialType
            (
                NXOpen::CAM::NcmTransferTypes::InitialTypes initialType /** initialtype */ 
            );
            /**Returns  the initial safe distance builder (inheritable tool dep) 
             <br>  Created in NX10.0.1.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InheritableToolDepBuilder * InitialSafeDistance
            (
            );
            /**Returns  the final type 
             <br>  Created in NX10.0.1.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::NcmTransferTypes::FinalTypes FinalType
            (
            );
            /**Sets  the final type 
             <br>  Created in NX10.0.1.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetFinalType
            (
                NXOpen::CAM::NcmTransferTypes::FinalTypes finalType /** finaltype */ 
            );
            /**Returns  the final safe distance builder (inheritable tool dep) 
             <br>  Created in NX10.0.1.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InheritableToolDepBuilder * FinalSafeDistance
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
