#ifndef NXOpen_TYPE_HXX_INCLUDED
#define NXOpen_TYPE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     type.ja
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
    /** Specifies axis orientation */
    enum AxisOrientation
    {
        AxisOrientationHorizontal/** horizontal */ ,
        AxisOrientationVertical/** vertical */ 
    };

    /** Specifies sense direction */
    enum Sense
    {
        SenseForward/** forward */ ,
        SenseReverse/** reverse */ 
    };

    /** Specifies the orientation of a plane's normal */
    enum PlaneNormalOrientation
    {
        PlaneNormalOrientationInward/** inward */ ,
        PlaneNormalOrientationOutward/** outward */ 
    };

    /** Specifies rotation direction */
    enum RotationDirection
    {
        RotationDirectionRightHand/** right hand */ ,
        RotationDirectionLeftHand/** left hand */ 
    };

    /** Specifies persistence */
    enum Persistence
    {
        PersistenceTemporary/** temporary */ ,
        PersistencePermanent/** permanent */ 
    };

    /** Specifies curve parameter type as arc length or percent arc length */
    enum CurveParameterType
    {
        CurveParameterTypeArcLength/** arc length */ ,
        CurveParameterTypePercentArcLength/** percent arc length */ ,
        CurveParameterTypeThroughPoint/** through point */ 
    };

    /** Specifies the X, Y, or Z axis */
    enum XYZAxis
    {
        XYZAxisXAxis/** X axis */,
        XYZAxisYAxis/** Y axis */,
        XYZAxisZAxis/** Z axis */
    };

}
#undef EXPORTLIBRARY
#endif
