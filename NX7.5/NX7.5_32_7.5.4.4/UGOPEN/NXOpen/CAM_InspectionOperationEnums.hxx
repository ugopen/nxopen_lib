#ifndef NXOpen_CAM_INSPECTIONOPERATIONENUMS_HXX_INCLUDED
#define NXOpen_CAM_INSPECTIONOPERATIONENUMS_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_InspectionOperationEnums.ja
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
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAM
    {
        /** Coordinate system that the inspection feature data is relative to */
        enum CamInspectionOperationCsysreferencetypes
        {
            CamInspectionOperationCsysreferencetypesRelativetoPCS/** Relative to Part Coordinate System */,
            CamInspectionOperationCsysreferencetypesAbsolute/** Relative to Absolute Coordinate System */
        };

        /** Directionality of feature surface */
        enum CamInspectionOperationInneroutertypes
        {
            CamInspectionOperationInneroutertypesInner/** Feature with surface normal pointing inward (hole)*/,
            CamInspectionOperationInneroutertypesOuter/** Feature with surface normal pointing outward (pin)*/
        };

        /** Specifies whether the feature extent is bounded or unbounded */
        enum CamInspectionOperationExtenttypes
        {
            CamInspectionOperationExtenttypesBounded/** Feature extent has bounds */,
            CamInspectionOperationExtenttypesUnbounded/** Feature extent is infinite */
        };

        /** Specifies the type of an inspection feature */
        enum CamInspectionOperationFeaturetypes
        {
            CamInspectionOperationFeaturetypesNone = -1/** Not a Feature */,
            CamInspectionOperationFeaturetypesArc/** Arc */,
            CamInspectionOperationFeaturetypesCircle/** Circle */,
            CamInspectionOperationFeaturetypesPoint/** Point */,
            CamInspectionOperationFeaturetypesSphere/** Sphere */,
            CamInspectionOperationFeaturetypesSurface/** Surface */,
            CamInspectionOperationFeaturetypesPattern/** Pattern */,
            CamInspectionOperationFeaturetypesCurve/** Curve */,
            CamInspectionOperationFeaturetypesCylinder/** Cylinder */,
            CamInspectionOperationFeaturetypesCone/** Cone */,
            CamInspectionOperationFeaturetypesPlane/** Plane */,
            CamInspectionOperationFeaturetypesLine/** Line */,
            CamInspectionOperationFeaturetypesCparln/** Closed Parallel Line bounded slot */,
            CamInspectionOperationFeaturetypesSlotTab/** Slot or Tab */,
            CamInspectionOperationFeaturetypesSurfaceOfRevolution/** Surface of Revolution */,
            CamInspectionOperationFeaturetypesTorus/** Torus */
        };

    }
}
#undef EXPORTLIBRARY
#endif
