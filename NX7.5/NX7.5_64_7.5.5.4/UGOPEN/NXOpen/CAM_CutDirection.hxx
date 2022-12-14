#ifndef NXOpen_CAM_CUTDIRECTION_HXX_INCLUDED
#define NXOpen_CAM_CUTDIRECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_CutDirection.ja
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
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAM
    {
        class CutDirection;
    }
    namespace CAM
    {
        class _CutDirectionBuilder;
        class CutDirectionImpl;
        /** Represents a boundary cut direction ci Builder  <br> This builder can not instantiated separately. <br> */
        class NXOPENCPPEXPORT  CutDirection : public TaggedObject
        {
            /** Available types for cut direction type in boundary cut direction customizable item */
            public: enum Types
            {
                TypesClimb/** Climb Cut */,
                TypesConventional/** Conventional Cut */,
                TypesForward/** Follow Boundary */,
                TypesReverse/** Reverse Boundary */,
                TypesMixed/** Mixed */
            };

            private: CutDirectionImpl * m_cutdirection_impl;
            private: friend class  _CutDirectionBuilder;
            protected: CutDirection();
            public: ~CutDirection();
            /**Returns  the cut direction type  <br> License requirements : None */
            public: NXOpen::CAM::CutDirection::Types Type
            (
            );
            /**Sets  the cut direction type  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetType
            (
                NXOpen::CAM::CutDirection::Types cutDirType /** the Cut Direction Type */
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
