#ifndef NXOpen_DISPLAY_DOWNLOADOFFLINERENDERINGBUILDER_HXX_INCLUDED
#define NXOpen_DISPLAY_DOWNLOADOFFLINERENDERINGBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Display_DownloadOfflineRenderingBuilder.ja
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
#include <NXOpen/Builder.hxx>
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
        class DownloadOfflineRenderingBuilder;
    }
    class Builder;
    namespace Display
    {
        class _DownloadOfflineRenderingBuilderBuilder;
        class DownloadOfflineRenderingBuilderImpl;
        /**
            Represents a @link NXOpen::Display::DownloadOfflineRenderingBuilder NXOpen::Display::DownloadOfflineRenderingBuilder@endlink .
             <br> Download Offline Rendering lists the batch jobs initiated in Ray Traced Studio
            Save Animation. Download Offline Rendering will show job progress and additional job details.
            NULL. <br> 
             <br> To create a new instance of this class, use @link NXOpen::ViewCollection::CreateDownloadOfflineRenderingBuilder  NXOpen::ViewCollection::CreateDownloadOfflineRenderingBuilder @endlink  <br> 
         <br>  Created in NX1953.0.0.  <br>  
        */
        class NXOPENCPP_DISPLAYEXPORT  DownloadOfflineRenderingBuilder : public NXOpen::Builder
        {
            /**the quality of rendering for each frame in the animation */
            public: enum FrameRateType
            {
                FrameRateTypeFps15/** 15 frames per second */,
                FrameRateTypeFps24/** 24 frames per second */,
                FrameRateTypeFps30/** 30 frames per second */,
                FrameRateTypeFps60/** 60 frames per second */,
                FrameRateTypeFps120/** 120 frames per second */,
                FrameRateTypeUserDefined/** User Defined frame rate */
            };

            private: DownloadOfflineRenderingBuilderImpl * m_downloadofflinerenderingbuilder_impl;
            private: friend class  _DownloadOfflineRenderingBuilderBuilder;
            protected: DownloadOfflineRenderingBuilder();
            public: ~DownloadOfflineRenderingBuilder();
            /**Returns the batch job details of the specified batch job.  
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: NXString SelectedBatchJob
            (
            );
            /**Sets the batch job details of the specified batch job.  
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : studio_render ("UG STUDIO RENDER") */
            public: void SetSelectedBatchJob
            (
                const NXString & jobName /** jobname */ 
            );
            /**Sets the batch job details of the specified batch job.  
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : studio_render ("UG STUDIO RENDER") */
            void SetSelectedBatchJob
            (
                const char * jobName /** jobname */ 
            );
            /**Returns the compression type for Microsoft AVIs 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: int AVICompression
            (
            );
            /**Sets the compression type for Microsoft AVIs 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : studio_render ("UG STUDIO RENDER") */
            public: void SetAVICompression
            (
                int aviCompression /** avicompression */ 
            );
            /**Returns the frames per second rate for the animation 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Display::DownloadOfflineRenderingBuilder::FrameRateType FrameRate
            (
            );
            /**Sets the frames per second rate for the animation 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : studio_render ("UG STUDIO RENDER") */
            public: void SetFrameRate
            (
                NXOpen::Display::DownloadOfflineRenderingBuilder::FrameRateType frameRate /** framerate */ 
            );
            /**Returns the user-defined frames per second rate for the animation 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: int CustomFrameRate
            (
            );
            /**Sets the user-defined frames per second rate for the animation 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : studio_render ("UG STUDIO RENDER") */
            public: void SetCustomFrameRate
            (
                int frameRate /** framerate */ 
            );
            /**Returns  the Download Offline Rendering AVI file browser 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: NXString AVIFileName
            (
            );
            /**Sets  the Download Offline Rendering AVI file browser 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: void SetAVIFileName
            (
                const NXString & aviFileName /** avifilename */ 
            );
            /**Sets  the Download Offline Rendering AVI file browser 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            void SetAVIFileName
            (
                const char * aviFileName /** avifilename */ 
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
