#ifndef NXOpen_CAM_DRIVEMODE_HXX_INCLUDED
#define NXOpen_CAM_DRIVEMODE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_DriveMode.ja
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
#include <NXOpen/CAM_DriveMode.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAM
    {
        class DriveMode;
    }
    namespace CAM
    {
        class InheritableDoubleBuilder;
    }
    namespace CAM
    {
        class _DriveModeBuilder;
        class DriveModeImpl;
        /** Drive Mode Builder */
        class NXOPENCPPEXPORT  DriveMode : public TaggedObject
        {
            /** Available types for Drive Mode  
             @deprecated Deprecated in NX7.5.0 <br> 
            */
            public:  NX_DEPRECATED("Deprecated in NX7.5.0") enum Type
            {
                TypeLowerBlendEdge/**Lower Blend Edge*/,
                TypeReferenceTool/**Reference Tool*/
            };

            private: DriveModeImpl * m_drivemode_impl;
            private: friend class  _DriveModeBuilder;
            protected: DriveMode();
            public: ~DriveMode();
            /**Returns  the Drive Mode Type  <br> License requirements : None */
            public: NXOpen::CAM::DriveMode::Type Mode
            (
            );
            /**Sets  the Drive Mode Type  <br> License requirements : None */
            public: void SetMode
            (
                NXOpen::CAM::DriveMode::Type type /** the Drive Mode */
            );
            /**Returns  the Reference Tool Diameter  <br> License requirements : None */
            public: double ReferenceToolDiameter
            (
            );
            /**Sets  the Reference Tool Diameter  <br> License requirements : None */
            public: void SetReferenceToolDiameter
            (
                double toolDia /** the Reference Tool Diameter */
            );
            /**Returns  the Floor Overlap Distance <br> License requirements : None */
            public: NXOpen::CAM::InheritableDoubleBuilder * FloorOverlap
            (
            );
            /**Returns  the Wall Overlap Distance <br> License requirements : None */
            public: NXOpen::CAM::InheritableDoubleBuilder * WallOverlap
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif