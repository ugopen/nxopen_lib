#ifndef NXOpen_CAM_INPATHEVENTSETDATA_HXX_INCLUDED
#define NXOpen_CAM_INPATHEVENTSETDATA_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_InPathEventSetData.ja
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
#include <NXOpen/CAM_InPathEventSetData.hxx>
#include <NXOpen/CAM_UdeSet.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAM
    {
        class InPathEventSetData;
    }
    namespace CAM
    {
        class UdeSet;
    }
    namespace CAM
    {
        class _InPathEventSetDataBuilder;
        class InPathEventSetDataImpl;
        /** Represents in path event   <br> This is a sub-builder class and cannot be directly instantiated <br> */
        class NXOPENCPPEXPORT  InPathEventSetData : public TaggedObject
        {
            private: InPathEventSetDataImpl * m_inpatheventsetdata_impl;
            private: friend class  _InPathEventSetDataBuilder;
            protected: InPathEventSetData();
            public: ~InPathEventSetData();
            /**Returns  the ude set   <br> License requirements : None */
            public: NXOpen::CAM::UdeSet * UdeSet
            (
            );
            /**Returns  the ude set status  <br> License requirements : None */
            public: bool UdeSetStatus
            (
            );
            /**Sets  the ude set status  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetUdeSetStatus
            (
                bool status /** the ude set status */
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif