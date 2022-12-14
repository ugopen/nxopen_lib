#ifndef NXOpen_CAM_INSPECTIONOPERATION_HXX_INCLUDED
#define NXOpen_CAM_INSPECTIONOPERATION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_InspectionOperation.ja
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
#include <NXOpen/CAM_InspectionOperationEnums.hxx>
#include <NXOpen/CAM_Move.hxx>
#include <NXOpen/CAM_Operation.hxx>
#include <NXOpen/CAM_Operation.hxx>
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
        class InspectionOperation;
    }
    namespace CAM
    {
        class InspectionMoveCollection;
    }
    namespace CAM
    {
        class Move;
    }
    namespace CAM
    {
        class Operation;
    }
    namespace CAM
    {
        class _InspectionOperationBuilder;
        class InspectionOperationImpl;
        /** Represents an Inspection operation  <br> To obtain an instance of this class use @link NXOpen::CAM::InspectionOperationCollection NXOpen::CAM::InspectionOperationCollection@endlink   <br> 
         <br>  Created in NX7.0.0.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  InspectionOperation : public NXOpen::CAM::Operation
        {
            private: InspectionOperationImpl * m_inspectionoperation_impl;
            private: friend class  _InspectionOperationBuilder;
            protected: InspectionOperation();
            public: ~InspectionOperation();
            /** Returns the Operation Feature Type  @return  
             <br>  Created in NX7.5.3.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::CamInspectionOperationFeaturetypes GetFeatureType
            (
            );
            /** Appends a move subop 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void AppendSubopMove
            (
                NXOpen::CAM::Move * move /** move */ 
            );
            /** Inserts a move subop 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void InsertSubopMove
            (
                NXOpen::CAM::Move * insertAfter /** insert after */ ,
                NXOpen::CAM::Move * move /** move */ 
            );


            /** Represents the Inspection Move Collection 
             <br>  Created in NX7.0.0.  <br>  
            */
            public: NXOpen::CAM::InspectionMoveCollection *CmmInspectionMoveCollection();
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
