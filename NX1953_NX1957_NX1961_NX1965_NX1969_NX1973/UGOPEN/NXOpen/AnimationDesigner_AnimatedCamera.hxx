#ifndef NXOpen_ANIMATIONDESIGNER_ANIMATEDCAMERA_HXX_INCLUDED
#define NXOpen_ANIMATIONDESIGNER_ANIMATEDCAMERA_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     AnimationDesigner_AnimatedCamera.ja
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
#include <NXOpen/DisplayableObject.hxx>
#include <NXOpen/libanimationdesigneropencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace AnimationDesigner
    {
        class AnimatedCamera;
    }
    class DisplayableObject;
    namespace AnimationDesigner
    {
        class _AnimatedCameraBuilder;
        class AnimatedCameraImpl;
        /** Represents an Animated Camera feature.  <br> To create or edit an instance of this class, use @link NXOpen::AnimationDesigner::AnimatedCameraBuilder  NXOpen::AnimationDesigner::AnimatedCameraBuilder @endlink  <br> 
         <br>  Created in NX1847.0.0.  <br>  
        */
        class ANIMATIONDESIGNEROPENCPPEXPORT  AnimatedCamera : public NXOpen::DisplayableObject
        {
            private: AnimatedCameraImpl * m_animatedcamera_impl;
            private: friend class  _AnimatedCameraBuilder;
            protected: AnimatedCamera();
            public: ~AnimatedCamera();
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