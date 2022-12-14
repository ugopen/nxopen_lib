#ifndef NXOpen_DISPLAY_IRAYPLUSSTUDIOEDITORBUILDER_HXX_INCLUDED
#define NXOpen_DISPLAY_IRAYPLUSSTUDIOEDITORBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Display_IRayPlusStudioEditorBuilder.ja
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
#include <NXOpen/DateBuilder.hxx>
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
        class IRayPlusStudioEditorBuilder;
    }
    class Builder;
    class CartesianCoordinateSystem;
    class DateBuilder;
    namespace Display
    {
        class _IRayPlusStudioEditorBuilderBuilder;
        class IRayPlusStudioEditorBuilderImpl;
        /**
            Represents a @link NXOpen::Display::IRayPlusStudioEditorBuilder NXOpen::Display::IRayPlusStudioEditorBuilder@endlink .
            Ray Traced Studio Editor controls display and output of CPU-based real-time ray tracing.
             <br> This class is restricted to being called from a program running during an 
            Interactive NX session.  If run from a non-interactive session it will 
            return NULL. <br> 
             <br> To create a new instance of this class, use @link NXOpen::ViewCollection::CreateIrayPlusStudioEditorBuilder  NXOpen::ViewCollection::CreateIrayPlusStudioEditorBuilder @endlink  <br> 
         <br>  Created in NX10.0.2.  <br>  
        */
        class NXOPENCPP_DISPLAYEXPORT  IRayPlusStudioEditorBuilder : public NXOpen::Builder
        {
            /** To specify the quality and performance of the Ray Traced Studio display when dynamic interaction stops */
            public: enum DynamicIRayPlusStudioRenderModeType
            {
                DynamicIRayPlusStudioRenderModeTypePhotoreal/** Very good ray traced display quality when dynamic interaction stops */,
                DynamicIRayPlusStudioRenderModeTypeQualityInteractive/** Good ray traced display quality with good performance when dynamic interaction stops */,
                DynamicIRayPlusStudioRenderModeTypeFastInteractive/** The fastest ray traced display performance with preview quality when dynamic interaction stops */
            };

            /** To specify the Ray Traced Studio static image file format */
            public: enum IRayPlusStudioStaticImageFileFormatType
            {
                IRayPlusStudioStaticImageFileFormatTypeTif/** Tagged Image File Format (TIFF) file format */,
                IRayPlusStudioStaticImageFileFormatTypePng/** Portable Network Graphic (PNG) file format */,
                IRayPlusStudioStaticImageFileFormatTypeJpg/** Joint Photographic Experts Group (JPEG) file format */
            };

            /** To specify the Ray Traced Studio static image units */
            public: enum IRayPlusStudioStaticImageUnitsType
            {
                IRayPlusStudioStaticImageUnitsTypePixels/** static image size specified in pixel */,
                IRayPlusStudioStaticImageUnitsTypeMillimeters/** static image size specified in millimeters */,
                IRayPlusStudioStaticImageUnitsTypeInches/** static image size specified in inches */
            };

            /** To specify the Ray Traced Studio static image size */
            public: enum IRayPlusStudioStaticImageSizeType
            {
                IRayPlusStudioStaticImageSizeTypeRenderWindow/** Ray Traced Studio window size used for static image output */,
                IRayPlusStudioStaticImageSizeTypeUserDefined/** user specified size for static image output */
            };

            /** To specify the Ray Traced Studio static image orientation */
            public: enum IRayPlusStudioStaticImageOrientationType
            {
                IRayPlusStudioStaticImageOrientationTypeLandscape/** static image orientation where width is greater than height */,
                IRayPlusStudioStaticImageOrientationTypePortrait/** static image orientation where height is greater than width */
            };

            /** To specify the Ray Traced Studio static image resolution */
            public: enum IRayPlusStudioStaticImageResolutionType
            {
                IRayPlusStudioStaticImageResolutionTypeHigh/** static image output resolution of 300 DPI (dots per inch) */,
                IRayPlusStudioStaticImageResolutionTypeMedium/** static image output resolution of 150 DPI (dots per inch) */,
                IRayPlusStudioStaticImageResolutionTypeLow/** static image output resolution of 72 DPI (dots per inch) */,
                IRayPlusStudioStaticImageResolutionTypeUserDefined/** user specified image output resolution in DPI (dots per inch) */
            };

            /** To specify the Ray Traced Studio remote rendering video mode 
             <br>  @deprecated Deprecated in NX12.0.0.  This is removed. The video mode is determined by the Ray Traced Studio render mode. <br>  
            */
            public: enum NX_DEPRECATED("Deprecated in NX12.0.0.  This is removed. The video mode is determined by the Ray Traced Studio render mode.") IRayPlusStudioRemoteRenderVideoType
            {
                IRayPlusStudioRemoteRenderVideoTypeStreaming/** streaming */ ,
                IRayPlusStudioRemoteRenderVideoTypeSynchronous/** synchronous */ 
            };

            /** To specify the Ray Traced Studio remote rendering format */
            public: enum IRayPlusStudioRemoteRenderFormatType
            {
                IRayPlusStudioRemoteRenderFormatTypeH264/** h264 */ ,
                IRayPlusStudioRemoteRenderFormatTypeLossless/** lossless */ ,
                IRayPlusStudioRemoteRenderFormatTypePng/** png */ ,
                IRayPlusStudioRemoteRenderFormatTypeJpeg/** jpeg */ 
            };

            /** To specify the Ray Traced Studio remote rendering type */
            public: enum IRayPlusStudioRemoteRenderType
            {
                IRayPlusStudioRemoteRenderTypeCluster/** Network Cluster */,
                IRayPlusStudioRemoteRenderTypeVca/** VCA */,
                IRayPlusStudioRemoteRenderTypeSecuredCluster/** Secured Network Cluster*/
            };

            /** To specify the Ray Traced Studio lens distortion type */
            public: enum IRayPlusStudioLensType
            {
                IRayPlusStudioLensTypeMonospherical/** Mono Spherical */,
                IRayPlusStudioLensTypeStereospherical/** Stereo Spherical */
            };

            /** To specify the Ray Traced Studio static render auto-completion type */
            public: enum IRayPlusStudioAutoCompletionType
            {
                IRayPlusStudioAutoCompletionTypeSimple/**the automatic completion criteria for a simple scene with a limited number of emissive materials, reflective materials, and shadows*/,
                IRayPlusStudioAutoCompletionTypeNormal/**the automatic completion criteria for a normal scene with a balanced number of emissive materials, reflective materials, and shadows*/,
                IRayPlusStudioAutoCompletionTypeComplex/**the automatic completion criteria for a complex scene with numerous emissive materials, reflective materials, and shadows */,
                IRayPlusStudioAutoCompletionTypeNone/**the option to apply no automatic completion criteria*/,
                IRayPlusStudioAutoCompletionTypeCustom/**the automatic completion criteria to specify a custom threshold for automatically detecting the completion of an image */
            };

            /**the completion parameter for the static render */
            public: enum StaticRenderDurationType
            {
                StaticRenderDurationTypeNumberOfIterations/**the number of iterations specified to the renderer to the static render */,
                StaticRenderDurationTypeTimeLimit/**the amount of time specified to the renderer to reach for the static render */,
                StaticRenderDurationTypeAutoComplete/**the auto Complete criteria uses Iray+ based progressive completion criteria to determine render completion */,
                StaticRenderDurationTypeTimeLimitedAutoComplete/**the auto Complete criteria uses Iray+ based progressive completion criteria to determine render completion and a designated time limit */
            };

            /** To specify the Ray Traced Studio stereo layout  */
            public: enum IRayPlusStudioStereoLayoutType
            {
                IRayPlusStudioStereoLayoutTypeTopBottom/** Top-Bottom */,
                IRayPlusStudioStereoLayoutTypeSideBySide/** Side-by-Side */
            };

            private: IRayPlusStudioEditorBuilderImpl * m_irayplusstudioeditorbuilder_impl;
            private: friend class  _IRayPlusStudioEditorBuilderBuilder;
            protected: IRayPlusStudioEditorBuilder();
            public: ~IRayPlusStudioEditorBuilder();
            /**Returns  the Ray Traced Studio dynamic display rendering mode 
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : studio_render ("UG STUDIO RENDER") */
            public: NXOpen::Display::IRayPlusStudioEditorBuilder::DynamicIRayPlusStudioRenderModeType DynamicIRayPlusStudioRenderMode
            (
            );
            /**Sets  the Ray Traced Studio dynamic display rendering mode 
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : studio_render ("UG STUDIO RENDER") */
            public: void SetDynamicIRayPlusStudioRenderMode
            (
                NXOpen::Display::IRayPlusStudioEditorBuilder::DynamicIRayPlusStudioRenderModeType dynamicIRayPlusStudioRenderMode /** dynamicirayplusstudiorendermode */ 
            );
            /**Returns  the Ray Traced Studio dynamic display time-based rendering mode timer (read only) 
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : studio_render ("UG STUDIO RENDER") */
            public: NXOpen::DateBuilder * DynamicIRayPlusStudioTime
            (
            );
            /**Returns  the Ray Traced Studio dynamic antialiasing quality when dynamic interaction stops 
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : studio_render ("UG STUDIO RENDER") */
            public: bool DynamicIRayPlusCaustics
            (
            );
            /**Sets  the Ray Traced Studio dynamic antialiasing quality when dynamic interaction stops 
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : studio_render ("UG STUDIO RENDER") */
            public: void SetDynamicIRayPlusCaustics
            (
                bool dynamicIRayPlusCaustics /** dynamiciraypluscaustics */ 
            );
            /**Returns  the Ray Traced Studio static output image file format 
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : studio_render ("UG STUDIO RENDER") */
            public: NXOpen::Display::IRayPlusStudioEditorBuilder::IRayPlusStudioStaticImageFileFormatType IRayPlusStudioStaticImageFileFormat
            (
            );
            /**Sets  the Ray Traced Studio static output image file format 
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : studio_render ("UG STUDIO RENDER") */
            public: void SetIRayPlusStudioStaticImageFileFormat
            (
                NXOpen::Display::IRayPlusStudioEditorBuilder::IRayPlusStudioStaticImageFileFormatType iRayPlusStudioStaticImageFileFormat /** irayplusstudiostaticimagefileformat */ 
            );
            /**Returns  the Ray Traced Studio static image units 
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : studio_render ("UG STUDIO RENDER") */
            public: NXOpen::Display::IRayPlusStudioEditorBuilder::IRayPlusStudioStaticImageUnitsType IRayPlusStudioStaticImageUnits
            (
            );
            /**Sets  the Ray Traced Studio static image units 
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : studio_render ("UG STUDIO RENDER") */
            public: void SetIRayPlusStudioStaticImageUnits
            (
                NXOpen::Display::IRayPlusStudioEditorBuilder::IRayPlusStudioStaticImageUnitsType iRayPlusStudioStaticImageUnits /** irayplusstudiostaticimageunits */ 
            );
            /**Returns  the Ray Traced Studio static image size 
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : studio_render ("UG STUDIO RENDER") */
            public: NXOpen::Display::IRayPlusStudioEditorBuilder::IRayPlusStudioStaticImageSizeType IRayPlusStudioStaticImageSize
            (
            );
            /**Sets  the Ray Traced Studio static image size 
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : studio_render ("UG STUDIO RENDER") */
            public: void SetIRayPlusStudioStaticImageSize
            (
                NXOpen::Display::IRayPlusStudioEditorBuilder::IRayPlusStudioStaticImageSizeType iRayPlusStudioStaticImageSize /** irayplusstudiostaticimagesize */ 
            );
            /**Returns  the Ray Traced Studio static image orientation 
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : studio_render ("UG STUDIO RENDER") */
            public: NXOpen::Display::IRayPlusStudioEditorBuilder::IRayPlusStudioStaticImageOrientationType IRayPlusStudioStaticImageOrientation
            (
            );
            /**Sets  the Ray Traced Studio static image orientation 
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : studio_render ("UG STUDIO RENDER") */
            public: void SetIRayPlusStudioStaticImageOrientation
            (
                NXOpen::Display::IRayPlusStudioEditorBuilder::IRayPlusStudioStaticImageOrientationType iRayPlusStudioStaticImageOrientation /** irayplusstudiostaticimageorientation */ 
            );
            /**Returns  the Ray Traced Studio static image aspect ratio will be maintained 
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : studio_render ("UG STUDIO RENDER") */
            public: bool IRayPlusStudioStaticImageLockAspectRatio
            (
            );
            /**Sets  the Ray Traced Studio static image aspect ratio will be maintained 
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : studio_render ("UG STUDIO RENDER") */
            public: void SetIRayPlusStudioStaticImageLockAspectRatio
            (
                bool iRayPlusStudioStaticImageLockAspectRatio /** irayplusstudiostaticimagelockaspectratio */ 
            );
            /**Returns  the Ray Traced Studio static image pixel width 
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : studio_render ("UG STUDIO RENDER") */
            public: int IRayPlusStudioStaticImagePixelWidth
            (
            );
            /**Sets  the Ray Traced Studio static image pixel width 
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : studio_render ("UG STUDIO RENDER") */
            public: void SetIRayPlusStudioStaticImagePixelWidth
            (
                int iRayPlusStudioStaticImagePixelWidth /** irayplusstudiostaticimagepixelwidth */ 
            );
            /**Returns  the Ray Traced Studio static image pixel height 
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : studio_render ("UG STUDIO RENDER") */
            public: int IRayPlusStudioStaticImagePixelHeight
            (
            );
            /**Sets  the Ray Traced Studio static image pixel height 
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : studio_render ("UG STUDIO RENDER") */
            public: void SetIRayPlusStudioStaticImagePixelHeight
            (
                int iRayPlusStudioStaticImagePixelHeight /** irayplusstudiostaticimagepixelheight */ 
            );
            /**Returns  the Ray Traced Studio static image width 
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : studio_render ("UG STUDIO RENDER") */
            public: double IRayPlusStudioStaticImageDoubleWidth
            (
            );
            /**Sets  the Ray Traced Studio static image width 
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : studio_render ("UG STUDIO RENDER") */
            public: void SetIRayPlusStudioStaticImageDoubleWidth
            (
                double iRayPlusStudioStaticImageDoubleWidth /** irayplusstudiostaticimagedoublewidth */ 
            );
            /**Returns  the Ray Traced Studio static image height 
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : studio_render ("UG STUDIO RENDER") */
            public: double IRayPlusStudioStaticImageDoubleHeight
            (
            );
            /**Sets  the Ray Traced Studio static image height 
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : studio_render ("UG STUDIO RENDER") */
            public: void SetIRayPlusStudioStaticImageDoubleHeight
            (
                double iRayPlusStudioStaticImageDoubleHeight /** irayplusstudiostaticimagedoubleheight */ 
            );
            /**Returns  the Ray Traced Studio static image width when rendering a VR-ready image 
             <br>  Created in NX12.0.1.  <br>  
             <br> License requirements : studio_render ("UG STUDIO RENDER") */
            public: int IRayPlusStudioStaticImageVrWidth
            (
            );
            /**Sets  the Ray Traced Studio static image width when rendering a VR-ready image 
             <br>  Created in NX12.0.1.  <br>  
             <br> License requirements : studio_render ("UG STUDIO RENDER") */
            public: void SetIRayPlusStudioStaticImageVrWidth
            (
                int iRayPlusStudioStaticImageVrWidth /** irayplusstudiostaticimagevrwidth */ 
            );
            /**Returns  the Ray Traced Studio static image height when rendering a VR-ready image 
             <br>  Created in NX12.0.1.  <br>  
             <br> License requirements : studio_render ("UG STUDIO RENDER") */
            public: int IRayPlusStudioStaticImageVrHeight
            (
            );
            /**Sets  the Ray Traced Studio static image height when rendering a VR-ready image 
             <br>  Created in NX12.0.1.  <br>  
             <br> License requirements : studio_render ("UG STUDIO RENDER") */
            public: void SetIRayPlusStudioStaticImageVrHeight
            (
                int iRayPlusStudioStaticImageVrHeight /** irayplusstudiostaticimagevrheight */ 
            );
            /**Returns  the Ray Traced Studio static image resolution 
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : studio_render ("UG STUDIO RENDER") */
            public: NXOpen::Display::IRayPlusStudioEditorBuilder::IRayPlusStudioStaticImageResolutionType IRayPlusStudioStaticImageResolution
            (
            );
            /**Sets  the Ray Traced Studio static image resolution 
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : studio_render ("UG STUDIO RENDER") */
            public: void SetIRayPlusStudioStaticImageResolution
            (
                NXOpen::Display::IRayPlusStudioEditorBuilder::IRayPlusStudioStaticImageResolutionType iRayPlusStudioStaticImageResolution /** irayplusstudiostaticimageresolution */ 
            );
            /**Returns  the Ray Traced Studio static image dots per inch (DPI) 
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : studio_render ("UG STUDIO RENDER") */
            public: int IRayPlusStudioStaticImageDotsPerInch
            (
            );
            /**Sets  the Ray Traced Studio static image dots per inch (DPI) 
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : studio_render ("UG STUDIO RENDER") */
            public: void SetIRayPlusStudioStaticImageDotsPerInch
            (
                int iRayPlusStudioStaticImageDotsPerInch /** irayplusstudiostaticimagedotsperinch */ 
            );
            /**Returns  the Ray Traced Studio static display time-based rendering timer (read only) 
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : studio_render ("UG STUDIO RENDER") */
            public: NXOpen::DateBuilder * StaticIRayPlusStudioTime
            (
            );
            /**Returns  the Ray Traced Studio display remote rendering video mode 
             <br>  @deprecated Deprecated in NX12.0.0.  This is removed. The video mode is determined by the Ray Traced Studio render mode. <br>  

             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : studio_render ("UG STUDIO RENDER") */
            public: NX_DEPRECATED("Deprecated in NX12.0.0.  This is removed. The video mode is determined by the Ray Traced Studio render mode.") NXOpen::Display::IRayPlusStudioEditorBuilder::IRayPlusStudioRemoteRenderVideoType RemoteRenderVideoMode
            (
            );
            /**Sets  the Ray Traced Studio display remote rendering video mode 
             <br>  @deprecated Deprecated in NX12.0.0.  This is removed. The video mode is determined by the Ray Traced Studio render mode. <br>  

             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : studio_render ("UG STUDIO RENDER") */
            public: NX_DEPRECATED("Deprecated in NX12.0.0.  This is removed. The video mode is determined by the Ray Traced Studio render mode.") void SetRemoteRenderVideoMode
            (
                NXOpen::Display::IRayPlusStudioEditorBuilder::IRayPlusStudioRemoteRenderVideoType remoteRenderVideoType /** remoterendervideotype */ 
            );
            /**Returns  the Ray Traced Studio display remote rendering format 
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : studio_render ("UG STUDIO RENDER") */
            public: NXOpen::Display::IRayPlusStudioEditorBuilder::IRayPlusStudioRemoteRenderFormatType RemoteRenderFormat
            (
            );
            /**Sets  the Ray Traced Studio display remote rendering format 
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : studio_render ("UG STUDIO RENDER") */
            public: void SetRemoteRenderFormat
            (
                NXOpen::Display::IRayPlusStudioEditorBuilder::IRayPlusStudioRemoteRenderFormatType remoteRenderFormatType /** remoterenderformattype */ 
            );
            /**Returns  the Ray Traced Studio display remote rendering type 
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : studio_render ("UG STUDIO RENDER") */
            public: NXOpen::Display::IRayPlusStudioEditorBuilder::IRayPlusStudioRemoteRenderType RemoteRenderType
            (
            );
            /**Sets  the Ray Traced Studio display remote rendering type 
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : studio_render ("UG STUDIO RENDER") */
            public: void SetRemoteRenderType
            (
                NXOpen::Display::IRayPlusStudioEditorBuilder::IRayPlusStudioRemoteRenderType remoteRenderType /** remoterendertype */ 
            );
            /**Returns  the Ray Traced Studio display remote rendering IP address 
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : studio_render ("UG STUDIO RENDER") */
            public: NXString RemoteRenderIP
            (
            );
            /**Sets  the Ray Traced Studio display remote rendering IP address 
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : studio_render ("UG STUDIO RENDER") */
            public: void SetRemoteRenderIP
            (
                const NXString & remoteRenderIP /** remoterenderip */ 
            );
            /**Sets  the Ray Traced Studio display remote rendering IP address 
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : studio_render ("UG STUDIO RENDER") */
            void SetRemoteRenderIP
            (
                const char * remoteRenderIP /** remoterenderip */ 
            );
            /**Returns  the Ray Traced Studio display remote rendering security token 
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : studio_render ("UG STUDIO RENDER") */
            public: NXString RemoteRenderSecurityToken
            (
            );
            /**Sets  the Ray Traced Studio display remote rendering security token 
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : studio_render ("UG STUDIO RENDER") */
            public: void SetRemoteRenderSecurityToken
            (
                const NXString & remoteRenderSecurityToken /** remoterendersecuritytoken */ 
            );
            /**Sets  the Ray Traced Studio display remote rendering security token 
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : studio_render ("UG STUDIO RENDER") */
            void SetRemoteRenderSecurityToken
            (
                const char * remoteRenderSecurityToken /** remoterendersecuritytoken */ 
            );
            /**Returns  the Ray Traced Studio display if remote rendering is used 
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : studio_render ("UG STUDIO RENDER") */
            public: bool RemoteRenderToggle
            (
            );
            /**Sets  the Ray Traced Studio display if remote rendering is used 
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : studio_render ("UG STUDIO RENDER") */
            public: void SetRemoteRenderToggle
            (
                bool remoteRenderToggle /** remoterendertoggle */ 
            );
            /**Returns  the Ray Traced Studio display VR camera coordinate system 
             <br>  Created in NX12.0.1.  <br>  
             <br> License requirements : studio_render ("UG STUDIO RENDER") */
            public: NXOpen::CartesianCoordinateSystem * VrCamera
            (
            );
            /**Sets  the Ray Traced Studio display VR camera coordinate system 
             <br>  Created in NX12.0.1.  <br>  
             <br> License requirements : studio_render ("UG STUDIO RENDER") */
            public: void SetVrCamera
            (
                NXOpen::CartesianCoordinateSystem * vrCamera /** the VR camera coordinate system */
            );
            /**Returns  the Ray Traced Studio display if the image will be rendered in a VR-ready format 
             <br>  Created in NX12.0.1.  <br>  
             <br> License requirements : studio_render ("UG STUDIO RENDER") */
            public: bool VrEnabledToggle
            (
            );
            /**Sets  the Ray Traced Studio display if the image will be rendered in a VR-ready format 
             <br>  Created in NX12.0.1.  <br>  
             <br> License requirements : studio_render ("UG STUDIO RENDER") */
            public: void SetVrEnabledToggle
            (
                bool vrEnabledToggle /** vrenabledtoggle */ 
            );
            /**Returns  the Ray Traced Studio display lens distortion type to use if rendering a VR-ready image 
             <br>  Created in NX12.0.1.  <br>  
             <br> License requirements : studio_render ("UG STUDIO RENDER") */
            public: NXOpen::Display::IRayPlusStudioEditorBuilder::IRayPlusStudioLensType LensType
            (
            );
            /**Sets  the Ray Traced Studio display lens distortion type to use if rendering a VR-ready image 
             <br>  Created in NX12.0.1.  <br>  
             <br> License requirements : studio_render ("UG STUDIO RENDER") */
            public: void SetLensType
            (
                NXOpen::Display::IRayPlusStudioEditorBuilder::IRayPlusStudioLensType lensType /** lenstype */ 
            );
            /**Returns  the Ray Traced Studio display image layout to use if rendering a stereo image 
             <br>  Created in NX12.0.1.  <br>  
             <br> License requirements : studio_render ("UG STUDIO RENDER") */
            public: NXOpen::Display::IRayPlusStudioEditorBuilder::IRayPlusStudioStereoLayoutType StereoLayout
            (
            );
            /**Sets  the Ray Traced Studio display image layout to use if rendering a stereo image 
             <br>  Created in NX12.0.1.  <br>  
             <br> License requirements : studio_render ("UG STUDIO RENDER") */
            public: void SetStereoLayout
            (
                NXOpen::Display::IRayPlusStudioEditorBuilder::IRayPlusStudioStereoLayoutType stereoLayout /** stereolayout */ 
            );
            /**Returns  the Ray Traced Studio display eye separation distance to use if rendering a stereo image 
             <br>  Created in NX12.0.1.  <br>  
             <br> License requirements : studio_render ("UG STUDIO RENDER") */
            public: double EyeSeparation
            (
            );
            /**Sets  the Ray Traced Studio display eye separation distance to use if rendering a stereo image 
             <br>  Created in NX12.0.1.  <br>  
             <br> License requirements : studio_render ("UG STUDIO RENDER") */
            public: void SetEyeSeparation
            (
                double eyeSeparation /** eyeseparation */ 
            );
            /**Returns  the Ray Traced Studio progess status indicator percent complete display 
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : studio_render ("UG STUDIO RENDER") */
            public: bool IRayPlusStudioshowStatusIndicator
            (
            );
            /**Sets  the Ray Traced Studio progess status indicator percent complete display 
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : studio_render ("UG STUDIO RENDER") */
            public: void SetIRayPlusStudioshowStatusIndicator
            (
                bool iRayPlusStudioshowStatusIndicator /** irayplusstudioshowstatusindicator */ 
            );
            /**Returns  the Ray Traced Studio denoiser 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : studio_render ("UG STUDIO RENDER") */
            public: bool IRayPlusStudioDenoiserToggle
            (
            );
            /**Sets  the Ray Traced Studio denoiser 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : studio_render ("UG STUDIO RENDER") */
            public: void SetIRayPlusStudioDenoiserToggle
            (
                bool iRayPlusStudioDenoiserToggle /** irayplusstudiodenoisertoggle */ 
            );
            /**Returns  the Ray Traced Studio display remote rendering client Username
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : studio_render ("UG STUDIO RENDER") */
            public: NXString RemoteRenderUsername
            (
            );
            /**Sets  the Ray Traced Studio display remote rendering client Username
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : studio_render ("UG STUDIO RENDER") */
            public: void SetRemoteRenderUsername
            (
                const NXString & remoteRenderUsername /** remoterenderusername */ 
            );
            /**Sets  the Ray Traced Studio display remote rendering client Username
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : studio_render ("UG STUDIO RENDER") */
            void SetRemoteRenderUsername
            (
                const char * remoteRenderUsername /** remoterenderusername */ 
            );
            /**Returns  the Ray Traced Studio display remote rendering client Password
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : studio_render ("UG STUDIO RENDER") */
            public: NXString RemoteRenderPassword
            (
            );
            /**Sets  the Ray Traced Studio display remote rendering client Password
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : studio_render ("UG STUDIO RENDER") */
            public: void SetRemoteRenderPassword
            (
                const NXString & remoteRenderPassword /** remoterenderpassword */ 
            );
            /**Sets  the Ray Traced Studio display remote rendering client Password
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : studio_render ("UG STUDIO RENDER") */
            void SetRemoteRenderPassword
            (
                const char * remoteRenderPassword /** remoterenderpassword */ 
            );
            /**Returns  the Ray Traced Studio display remote rendering client reserve nodes
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : studio_render ("UG STUDIO RENDER") */
            public: int RemoteRenderReserveNodes
            (
            );
            /**Sets  the Ray Traced Studio display remote rendering client reserve nodes
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : studio_render ("UG STUDIO RENDER") */
            public: void SetRemoteRenderReserveNodes
            (
                int remoteRenderReserveNodes /** remoterenderreservenodes */ 
            );
            /**Returns  the Ray Traced Studio display static render auto-completion type 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : studio_render ("UG STUDIO RENDER") */
            public: NXOpen::Display::IRayPlusStudioEditorBuilder::IRayPlusStudioAutoCompletionType StaticAutoCompletionType
            (
            );
            /**Sets  the Ray Traced Studio display static render auto-completion type 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : studio_render ("UG STUDIO RENDER") */
            public: void SetStaticAutoCompletionType
            (
                NXOpen::Display::IRayPlusStudioEditorBuilder::IRayPlusStudioAutoCompletionType autoCompletionType /** autocompletiontype */ 
            );
            /**Returns  the Ray Traced Studio display static render duration type 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : studio_render ("UG STUDIO RENDER") */
            public: NXOpen::Display::IRayPlusStudioEditorBuilder::StaticRenderDurationType StaticRenderDuration
            (
            );
            /**Sets  the Ray Traced Studio display static render duration type 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : studio_render ("UG STUDIO RENDER") */
            public: void SetStaticRenderDuration
            (
                NXOpen::Display::IRayPlusStudioEditorBuilder::StaticRenderDurationType staticRenderDuration /** staticrenderduration */ 
            );
            /**Returns  the Ray Traced Studio static image number of iterations limit 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : studio_render ("UG STUDIO RENDER") */
            public: int StaticRenderNumberOfIterations
            (
            );
            /**Sets  the Ray Traced Studio static image number of iterations limit 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : studio_render ("UG STUDIO RENDER") */
            public: void SetStaticRenderNumberOfIterations
            (
                int staticRenderNumberOfIterations /** staticrendernumberofiterations */ 
            );
            /**Returns  the Ray Traced Studio display static render auto-completion custom quality factor. This control
                    defines a quality factor relative to the scene. The quality factor has a linear
                    scaling effect. For example, a quality factor set to 2.0 will roughly take twice as
                    long to render a scene with an assigned quality factor of 1.0.
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : studio_render ("UG STUDIO RENDER") */
            public: double AutoCompletionCustomQualityFactor
            (
            );
            /**Sets  the Ray Traced Studio display static render auto-completion custom quality factor. This control
                    defines a quality factor relative to the scene. The quality factor has a linear
                    scaling effect. For example, a quality factor set to 2.0 will roughly take twice as
                    long to render a scene with an assigned quality factor of 1.0.
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : studio_render ("UG STUDIO RENDER") */
            public: void SetAutoCompletionCustomQualityFactor
            (
                double autoCompletionCustomQualityFactor /** autocompletioncustomqualityfactor */ 
            );
            /**Returns  the Ray Traced Studio display static render auto-completion custom pixel ratio. This controls
                    "the number of pixels as a ratio of the total pixel count that must converge to the Quality Completion Factor."
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : studio_render ("UG STUDIO RENDER") */
            public: double AutoCompletionCustomPixelRatio
            (
            );
            /**Sets  the Ray Traced Studio display static render auto-completion custom pixel ratio. This controls
                    "the number of pixels as a ratio of the total pixel count that must converge to the Quality Completion Factor."
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : studio_render ("UG STUDIO RENDER") */
            public: void SetAutoCompletionCustomPixelRatio
            (
                double autoCompletionCustomPixelRatio /** autocompletioncustompixelratio */ 
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
