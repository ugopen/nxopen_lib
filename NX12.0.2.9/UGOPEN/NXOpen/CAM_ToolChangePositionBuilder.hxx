#ifndef NXOpen_CAM_TOOLCHANGEPOSITIONBUILDER_HXX_INCLUDED
#define NXOpen_CAM_TOOLCHANGEPOSITIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_ToolChangePositionBuilder.ja
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
#include <NXOpen/CAM_MoveBuilder.hxx>
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
        class ToolChangePositionBuilder;
    }
    namespace CAM
    {
        class MoveBuilder;
    }
    class Direction;
    class Point;
    namespace CAM
    {
        class _ToolChangePositionBuilderBuilder;
        class ToolChangePositionBuilderImpl;

        /// \cond NX_NO_DOC 
        /** represents the Rotary Move To Point Builder  <br> To create a new instance of this class, use @link NXOpen::CAM::MoveCollection::CreateToolChangePositionBuilder  NXOpen::CAM::MoveCollection::CreateToolChangePositionBuilder @endlink  <br> 
         <br>  Created in NX11.0.2.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  ToolChangePositionBuilder : public NXOpen::CAM::MoveBuilder
        {
            private: ToolChangePositionBuilderImpl * m_toolchangepositionbuilder_impl;
            private: friend class  _ToolChangePositionBuilderBuilder;
            protected: ToolChangePositionBuilder();
            public: ~ToolChangePositionBuilder();
            /**Returns  the location 
             <br>  Created in NX11.0.2.  <br>  
             <br> License requirements : None */
            public: NXOpen::Point * Point
            (
            );
            /**Sets  the location 
             <br>  Created in NX11.0.2.  <br>  
             <br> License requirements : None */
            public: void SetPoint
            (
                NXOpen::Point * location /** location */ 
            );
            /**Returns  the vector 
             <br>  Created in NX11.0.2.  <br>  
             <br> License requirements : None */
            public: NXOpen::Direction * Vector
            (
            );
            /**Sets  the vector 
             <br>  Created in NX11.0.2.  <br>  
             <br> License requirements : None */
            public: void SetVector
            (
                NXOpen::Direction * vec /** vec */ 
            );
        };

        /// \endcond 
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
