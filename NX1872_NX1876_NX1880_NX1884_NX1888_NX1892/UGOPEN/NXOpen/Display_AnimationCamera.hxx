#ifndef NXOpen_DISPLAY_ANIMATIONCAMERA_HXX_INCLUDED
#define NXOpen_DISPLAY_ANIMATIONCAMERA_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Display_AnimationCamera.ja
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
#include <NXOpen/Display_Camera.hxx>
#include <NXOpen/libnxopencpp_display_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Display
    {
        class AnimationCamera;
    }
    namespace Display
    {
        class Camera;
    }
    namespace Display
    {
        class _AnimationCameraBuilder;
        class AnimationCameraImpl;
        /** Represents a animaiton camera  <br> To create or edit an instance of this class, use @link NXOpen::Display::AnimationCameraBuilder  NXOpen::Display::AnimationCameraBuilder @endlink  <br> 
         <br>  Created in NX1847.0.0.  <br>  
        */
        class NXOPENCPP_DISPLAYEXPORT  AnimationCamera : public NXOpen::Display::Camera
        {
            private: AnimationCameraImpl * m_animationcamera_impl;
            private: friend class  _AnimationCameraBuilder;
            protected: AnimationCamera();
            public: ~AnimationCamera();
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