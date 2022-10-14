#ifndef NXOpen_CAM_PATTERNDIRECTION_HXX_INCLUDED
#define NXOpen_CAM_PATTERNDIRECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_PatternDirection.ja
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
#include <NXOpen/CAM_ElementIntBuilder.hxx>
#include <NXOpen/CAM_ElementIntBuilder.hxx>
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
        class PatternDirection;
    }
    namespace CAM
    {
        class ElementIntBuilder;
    }
    namespace CAM
    {
        class _PatternDirectionBuilder;
        class PatternDirectionImpl;
        /** Represents a builder for an option menu of pattern direction type 
         <br>  Created in NX1980.0.0.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  PatternDirection : public NXOpen::CAM::ElementIntBuilder
        {
            /** Available types for pattern direction customizable item */
            public: enum Types
            {
                TypesClockwise/** Clockwise*/,
                TypesCounterClockwise/** Counter clockwise*/,
                TypesClockwiseAlternate/** Clockwise alternate*/,
                TypesCounterClockwiseAlternate/** Counter clockwise alternate*/
            };

            private: PatternDirectionImpl * m_patterndirection_impl;
            private: friend class  _PatternDirectionBuilder;
            protected: PatternDirection();
            public: ~PatternDirection();
            /**Returns  the current value 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::PatternDirection::Types EnumValue
            (
            );
            /**Sets  the current value 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetEnumValue
            (
                NXOpen::CAM::PatternDirection::Types newValue /** the new value */
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