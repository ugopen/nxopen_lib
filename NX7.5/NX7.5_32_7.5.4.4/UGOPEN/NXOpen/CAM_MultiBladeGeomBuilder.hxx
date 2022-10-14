#ifndef NXOpen_CAM_MULTIBLADEGEOMBUILDER_HXX_INCLUDED
#define NXOpen_CAM_MULTIBLADEGEOMBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_MultiBladeGeomBuilder.ja
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
#include <NXOpen/CAM_MultiBladeGeomBuilder.hxx>
#include <NXOpen/CAM_FeatureGeomBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAM
    {
        class MultiBladeGeomBuilder;
    }
    namespace CAM
    {
        class FeatureGeomBuilder;
    }
    namespace CAM
    {
        class InheritableIntBuilder;
    }
    class Point;
    class SmartObject;
    namespace CAM
    {
        class _MultiBladeGeomBuilderBuilder;
        class MultiBladeGeomBuilderImpl;
        /** Represents a MultiBladeGeomBuilder Builder  <br> To create a new instance of this class, use @link CAM::NCGroupCollection::CreateMultiBladeGeometryBuilder CAM::NCGroupCollection::CreateMultiBladeGeometryBuilder@endlink  <br> */
        class NXOPENCPPEXPORT  MultiBladeGeomBuilder : public CAM::FeatureGeomBuilder
        {
            /** Available types for Part Axis of Rotation */
            public: enum PartAxisOfRotationTypes
            {
                PartAxisOfRotationTypesZm/** +ZM */,
                PartAxisOfRotationTypesSpecify/** Specify */
            };

            private: MultiBladeGeomBuilderImpl * m_multibladegeombuilder_impl;
            private: friend class  _MultiBladeGeomBuilderBuilder;
            protected: MultiBladeGeomBuilder();
            public: ~MultiBladeGeomBuilder();
            /**Returns  the axis of rotation mode  <br> License requirements : None */
            public: NXOpen::CAM::MultiBladeGeomBuilder::PartAxisOfRotationTypes AxisOfRotation
            (
            );
            /**Sets  the axis of rotation mode  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetAxisOfRotation
            (
                NXOpen::CAM::MultiBladeGeomBuilder::PartAxisOfRotationTypes axis /** the axis of rotation mode */
            );
            /**Returns  the part axis vector  <br> License requirements : None */
            public: NXOpen::SmartObject * PartAxisVector
            (
            );
            /**Sets  the part axis vector  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetPartAxisVector
            (
                NXOpen::SmartObject * vector /** the part axis vector */
            );
            /**Returns  the part axis point  <br> License requirements : None */
            public: NXOpen::Point * PartAxisPoint
            (
            );
            /**Sets  the part axis point  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetPartAxisPoint
            (
                NXOpen::Point * point /** the part axis point */
            );
            /**Returns  the number of blades  <br> License requirements : None */
            public: NXOpen::CAM::InheritableIntBuilder * NumberOfBlades
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif