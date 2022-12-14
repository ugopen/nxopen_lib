#ifndef NXOpen_CAM_POINTTOPOINTBUILDER_HXX_INCLUDED
#define NXOpen_CAM_POINTTOPOINTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_PointToPointBuilder.ja
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
#include <NXOpen/CAM_MillOperationBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAM
    {
        class PointToPointBuilder;
    }
    namespace CAM
    {
        class DrillSurfaceBuilder;
    }
    namespace CAM
    {
        class MillOperationBuilder;
    }
    namespace CAM
    {
        class _PointToPointBuilderBuilder;
        class PointToPointBuilderImpl;
        /** Represents a Point to Point Builder (Drilling)  <br> To create a new instance of this class, use @link CAM::OperationCollection::CreatePointToPointBuilder CAM::OperationCollection::CreatePointToPointBuilder@endlink  <br> */
        class NXOPENCPPEXPORT  PointToPointBuilder : public CAM::MillOperationBuilder
        {
            /** Available types for cycle type */
            public: enum CycleTypes
            {
                CycleTypesNoCycle/** No Cycle */,
                CycleTypesPeckDrill/** Peck Drill... */,
                CycleTypesBreakChip/** Break Chip... */,
                CycleTypesStandardText/** Standard Text... */,
                CycleTypesStandardDrill/** Standard Drill... */,
                CycleTypesStandardDrillCsink/** Standard Drill,Csink... */,
                CycleTypesStandardDrillDeep/** Standard Drill,Deep... */,
                CycleTypesStandardDrillBreakChip/** Standard Drill,Break Chip... */,
                CycleTypesStandardTap/** Standard Tap... */,
                CycleTypesStandardBore/** Standard Bore... */,
                CycleTypesStandardBoreDrag/** Standard Bore,Drag... */,
                CycleTypesStandardBoreNoDrag/** Standard Bore,No Drag... */,
                CycleTypesStandardBoreBack/** Standard Bore,Back... */,
                CycleTypesStandardBoreManual/** Standard Bore,Manual... */
            };

            /** Available types for tool axis type */
            public: enum TlaxisTypes
            {
                TlaxisTypesNone/** +ZM Axis */,
                TlaxisTypesFixed/** Specify Vector */,
                TlaxisTypesNormalToPart/** Normal to Part Surface */
            };

            /** Available types for project vector in point to point operation*/
            public: enum ProjectVectorTypes
            {
                ProjectVectorTypesNone/** None */,
                ProjectVectorTypesSpecifyVetor/** Specify vector */,
                ProjectVectorTypesToolAxis/** Tools axis */
            };

            /** Available types for material side in point to point operation*/
            public: enum MaterialSideTypes
            {
                MaterialSideTypesNone/** None */,
                MaterialSideTypesSpecifyVetor/** Specify vector */,
                MaterialSideTypesToolAxis/** Tools axis */
            };

            private: PointToPointBuilderImpl * m_pointtopointbuilder_impl;
            private: friend class  _PointToPointBuilderBuilder;
            protected: PointToPointBuilder();
            public: ~PointToPointBuilder();
            /**Returns  the top surface builder   <br> License requirements : None */
            public: NXOpen::CAM::DrillSurfaceBuilder * TopSurface
            (
            );
            /**Returns  the bottom surface builder   <br> License requirements : None */
            public: NXOpen::CAM::DrillSurfaceBuilder * BottomSurface
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
