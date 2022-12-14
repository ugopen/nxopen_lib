#ifndef NXOpen_CAM_CUTSIDES_HXX_INCLUDED
#define NXOpen_CAM_CUTSIDES_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_CutSides.ja
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
        class CutSides;
    }
    namespace CAM
    {
        class _CutSidesBuilder;
        class CutSidesImpl;
        /** Represents a Cut Sides Builder 
         <br>  Created in NX7.5.0.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  CutSides : public NXOpen::TaggedObject
        {
            /** Available types for sides to cut */
            public: enum SideType
            {
                SideTypeAll/**All Sides*/,
                SideTypeLeft/**Left Side*/,
                SideTypeRight/**Right Side*/,
                SideTypeLeftRight/**Left and Right Side*/,
                SideTypeOpposing/**Opposing Sides*/,
                SideTypeLeftRightLeadingEdge/**Left, Right, Leading Edge*/,
                SideTypeLeadingEdge/**Leading Edge*/,
                SideTypeTrailingEdge/**Trailing Edge*/
            };

            private: CutSidesImpl * m_cutsides_impl;
            private: friend class  _CutSidesBuilder;
            protected: CutSides();
            public: ~CutSides();
            /**Returns  the Sides to Cut 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::CutSides::SideType Side
            (
            );
            /**Sets  the Sides to Cut 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetSide
            (
                NXOpen::CAM::CutSides::SideType sideType /** the Sides to Cut value */
            );
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
