#ifndef NXOpen_CAM_BLADEFINISHGEOM_HXX_INCLUDED
#define NXOpen_CAM_BLADEFINISHGEOM_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_BladeFinishGeom.ja
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
#include <NXOpen/CAM_BladeFinishGeom.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAM
    {
        class BladeFinishGeom;
    }
    namespace CAM
    {
        class _BladeFinishGeomBuilder;
        class BladeFinishGeomImpl;
        /** Represents BladeFinishGeom Builder */
        class NXOPENCPPEXPORT  BladeFinishGeom : public TaggedObject
        {
            /** Available types for geometry to finish */
            public: enum Types
            {
                TypesBlade/**Blade*/,
                TypesSplitterOne/**Splitter 1*/,
                TypesSplitterTwo/**Splitter 2*/,
                TypesSplitterThree/**Splitter 3*/,
                TypesSplitterFour/**Splitter 4*/,
                TypesSplitterFive/**Splitter 5*/
            };

            private: BladeFinishGeomImpl * m_bladefinishgeom_impl;
            private: friend class  _BladeFinishGeomBuilder;
            protected: BladeFinishGeom();
            public: ~BladeFinishGeom();
            /**Returns  the Geometry to Finish  <br> License requirements : None */
            public: NXOpen::CAM::BladeFinishGeom::Types Type
            (
            );
            /**Sets  the Geometry to Finish  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetType
            (
                NXOpen::CAM::BladeFinishGeom::Types geomToFinish /** the Geometry to Finish value */
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif