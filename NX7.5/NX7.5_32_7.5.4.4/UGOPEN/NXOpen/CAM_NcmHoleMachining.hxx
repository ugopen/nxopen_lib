#ifndef NXOpen_CAM_NCMHOLEMACHINING_HXX_INCLUDED
#define NXOpen_CAM_NCMHOLEMACHINING_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_NcmHoleMachining.ja
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
#include <NXOpen/CAM_NcmHoleMachining.hxx>
#include <NXOpen/CAM_NcmSubopBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAM
    {
        class NcmHoleMachining;
    }
    namespace CAM
    {
        class InheritableToolDepBuilder;
    }
    namespace CAM
    {
        class NcmAvoidancePointBuilder;
    }
    namespace CAM
    {
        class NcmClearanceBuilder;
    }
    namespace CAM
    {
        class NcmHoleMachiningEngRet;
    }
    namespace CAM
    {
        class NcmSubopBuilder;
    }
    namespace CAM
    {
        class NcmTransferBuilder;
    }
    namespace CAM
    {
        class _NcmHoleMachiningBuilder;
        class NcmHoleMachiningImpl;
        /**
            Represents a @link CAM::NcmHoleMachining CAM::NcmHoleMachining@endlink 
            */
        class NXOPENCPPEXPORT  NcmHoleMachining : public CAM::NcmSubopBuilder
        {
            /** Available types for overlap types */
            public: enum OverlapTypes
            {
                OverlapTypesAxial/** axial */,
                OverlapTypesAlongCut/** along cut*/
            };

            /** Available types for initial clearance in hole machining */
            public: enum InitialTypes
            {
                InitialTypesClearance/** clearance */,
                InitialTypesDistance/** distance */,
                InitialTypesNone/** none */,
                InitialTypesBlankPlane/** blank plane */
            };

            /** Available types for final clearance in hole machining */
            public: enum FinalTypes
            {
                FinalTypesClearance/** clearance */,
                FinalTypesDistance/** distance */,
                FinalTypesNone/** none */
            };

            /** Available types for cutter compensation in hole machining */
            public: enum CutcomTypes
            {
                CutcomTypesNone/** cutter compensation off */,
                CutcomTypesAllPasses/** cutter compensation on all passes */,
                CutcomTypesFinalPass/** cutter compensation on last pass */
            };

            private: NcmHoleMachiningImpl * m_ncmholemachining_impl;
            private: friend class  _NcmHoleMachiningBuilder;
            protected: NcmHoleMachining();
            public: ~NcmHoleMachining();
            /**Returns  the engage settings  <br> License requirements : None */
            public: NXOpen::CAM::NcmHoleMachiningEngRet * Engage
            (
            );
            /**Returns  the initial engage settings  <br> License requirements : None */
            public: NXOpen::CAM::NcmHoleMachiningEngRet * InitialEngage
            (
            );
            /**Returns  the retract settings  <br> License requirements : None */
            public: NXOpen::CAM::NcmHoleMachiningEngRet * Retract
            (
            );
            /**Returns  the final retract settings  <br> License requirements : None */
            public: NXOpen::CAM::NcmHoleMachiningEngRet * FinalRetract
            (
            );
            /**Returns  the region start type  <br> License requirements : None */
            public: NXOpen::CAM::NcmHoleMachining::OverlapTypes OverlapType
            (
            );
            /**Sets  the region start type  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetOverlapType
            (
                NXOpen::CAM::NcmHoleMachining::OverlapTypes overlapType /** overlaptype */ 
            );
            /**Returns  the overlap distance  <br> License requirements : None */
            public: double OverlapDistance
            (
            );
            /**Sets  the overlap distance  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetOverlapDistance
            (
                double overlapDistance /** overlapdistance */ 
            );
            /**Returns  the number of threads  <br> License requirements : None */
            public: double NumberOfThreads
            (
            );
            /**Sets  the number of threads  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetNumberOfThreads
            (
                double numberOfThreads /** numberofthreads */ 
            );
            /**Returns  the overlap angle  <br> License requirements : None */
            public: double OverlapAngle
            (
            );
            /**Sets  the overlap angle  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetOverlapAngle
            (
                double overlapAngle /** overlapangle */ 
            );
            /**Returns  the region start angle  <br> License requirements : None */
            public: double RegionStartAngle
            (
            );
            /**Sets  the region start angle  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetRegionStartAngle
            (
                double regionStartAngle /** regionstartangle */ 
            );
            /**Returns  the clearance setting  <br> License requirements : None */
            public: NXOpen::CAM::NcmClearanceBuilder * TransferClearance
            (
            );
            /**Returns  the transfer settings for initial and final  <br> License requirements : None */
            public: NXOpen::CAM::NcmTransferBuilder * TransferInitialFinal
            (
            );
            /**Returns  the initial type  <br> License requirements : None */
            public: NXOpen::CAM::NcmHoleMachining::InitialTypes InitialType
            (
            );
            /**Sets  the initial type  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetInitialType
            (
                NXOpen::CAM::NcmHoleMachining::InitialTypes initialType /** initialtype */ 
            );
            /**Returns  the initial safe distance builder (inheritable tool dep)  <br> License requirements : None */
            public: NXOpen::CAM::InheritableToolDepBuilder * InitialSafeDistance
            (
            );
            /**Returns  the final type  <br> License requirements : None */
            public: NXOpen::CAM::NcmHoleMachining::FinalTypes FinalType
            (
            );
            /**Sets  the final type  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetFinalType
            (
                NXOpen::CAM::NcmHoleMachining::FinalTypes finalType /** finaltype */ 
            );
            /**Returns  the final safe distance builder (inheritable tool dep)  <br> License requirements : None */
            public: NXOpen::CAM::InheritableToolDepBuilder * FinalSafeDistance
            (
            );
            /**Returns  the from point builder  <br> License requirements : None */
            public: NXOpen::CAM::NcmAvoidancePointBuilder * TransferAvoidanceFrom
            (
            );
            /**Returns  the start point builder  <br> License requirements : None */
            public: NXOpen::CAM::NcmAvoidancePointBuilder * TransferAvoidanceStart
            (
            );
            /**Returns  the return point builder  <br> License requirements : None */
            public: NXOpen::CAM::NcmAvoidancePointBuilder * TransferAvoidanceReturn
            (
            );
            /**Returns  the gohome point builder  <br> License requirements : None */
            public: NXOpen::CAM::NcmAvoidancePointBuilder * TransferAvoidanceGohome
            (
            );
            /**Returns  the cutter compensation type  <br> License requirements : None */
            public: NXOpen::CAM::NcmHoleMachining::CutcomTypes CutcomType
            (
            );
            /**Sets  the cutter compensation type  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetCutcomType
            (
                NXOpen::CAM::NcmHoleMachining::CutcomTypes cutcomType /** cutcomtype */ 
            );
            /**Returns  the cutter compensation minimum move builder (inheritable tool dep)  <br> License requirements : None */
            public: NXOpen::CAM::InheritableToolDepBuilder * CutcomMinimumMove
            (
            );
            /**Returns  the cutter compensation minimum angle  <br> License requirements : None */
            public: double CutcomMinimumAngle
            (
            );
            /**Sets  the cutter compensation minimum angle  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetCutcomMinimumAngle
            (
                double minimumAngle /** minimumangle */ 
            );
            /**Returns  the cutter compensation output plane status  <br> License requirements : None */
            public: bool CutcomOutputPlane
            (
            );
            /**Sets  the cutter compensation output plane status  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetCutcomOutputPlane
            (
                bool outputPlane /** outputplane */ 
            );
            /**Returns  the suppress cutter compensation  <br> License requirements : None */
            public: bool SuppressCutcom
            (
            );
            /**Sets  the suppress cutter compensation  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetSuppressCutcom
            (
                bool suppressCutcom /** suppresscutcom */ 
            );
            /**Returns  the cutter compensation output contact point status  <br> License requirements : None */
            public: bool CutcomOutputContactPoint
            (
            );
            /**Sets  the cutter compensation output contact point status  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetCutcomOutputContactPoint
            (
                bool newValue /** newvalue */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
