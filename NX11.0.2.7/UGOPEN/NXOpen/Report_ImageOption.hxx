#ifndef NXOpen_REPORT_IMAGEOPTION_HXX_INCLUDED
#define NXOpen_REPORT_IMAGEOPTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Report_ImageOption.ja
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
#include <NXOpen/Report_ImageOption.hxx>
#include <NXOpen/libnxopencpp_report_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Report
    {
        class ImageOption;
    }
    namespace Report
    {
        class _ImageOptionBuilder;
        class ImageOptionImpl;
        /** Represents an image option object.  
         <br>  Created in NX11.0.0.  <br>  
        */
        class NXOPENCPP_REPORTEXPORT  ImageOption : public NXOpen::TaggedObject
        {
            private: ImageOptionImpl * m_imageoption_impl;
            private: friend class  _ImageOptionBuilder;
            protected: ImageOption();
            public: ~ImageOption();
            /**Returns  the image height . 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: double ImageHeight
            (
            );
            /**Sets  the image height . 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: void SetImageHeight
            (
                double imageHeight /** imageheight */ 
            );
            /**Returns  the image width . 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: double ImageWidth
            (
            );
            /**Sets  the image width . 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: void SetImageWidth
            (
                double imageWidth /** imagewidth */ 
            );
            /**Returns  the image rotation angle in degree. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: double ImageRotation
            (
            );
            /**Sets  the image rotation angle in degree. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: void SetImageRotation
            (
                double imageRotation /** imagerotation */ 
            );
            /**Returns   @brief  a value that indicates whether locks original image aspect ratio. If locks ratio, the image
                        width will be updated according to the ratio when image height changes , and vice versa. 

              
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: bool LockOriginalAspectRatio
            (
            );
            /**Sets   @brief  a value that indicates whether locks original image aspect ratio. If locks ratio, the image
                        width will be updated according to the ratio when image height changes , and vice versa. 

              
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: void SetLockOriginalAspectRatio
            (
                bool lockOriginalRatio /** lockoriginalratio */ 
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
