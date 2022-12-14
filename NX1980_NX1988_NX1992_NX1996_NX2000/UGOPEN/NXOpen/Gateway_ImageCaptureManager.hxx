#ifndef NXOpen_GATEWAY_IMAGECAPTUREMANAGER_HXX_INCLUDED
#define NXOpen_GATEWAY_IMAGECAPTUREMANAGER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Gateway_ImageCaptureManager.ja
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
#include <NXOpen/Gateway_ImageCaptureBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_gateway_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Gateway
    {
        class ImageCaptureManager;
    }
    class BasePart;
    namespace Gateway
    {
        class ImageCaptureBuilder;
    }
    namespace Gateway
    {
        class ImageCaptureManagerImpl;
        /** The ImageCaptureManager class provides methods to create 
            @link NXOpen::Gateway::ImageCaptureBuilder NXOpen::Gateway::ImageCaptureBuilder@endlink  object <br> To obtain an instance of this class, refer to @link NXOpen::BasePart  NXOpen::BasePart @endlink  <br> 
         <br>  Created in NX7.5.0.  <br>  
        */
        class NXOPENCPP_GATEWAYEXPORT  ImageCaptureManager
        {
            private: ImageCaptureManagerImpl * m_imagecapturemanager_impl;
            private: NXOpen::BasePart* m_owner;
            /// \cond NX_NO_DOC 
            public: explicit ImageCaptureManager(NXOpen::BasePart *owner);


            /// \endcond 
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~ImageCaptureManager();
            /** Creates a @link NXOpen::Gateway::ImageCaptureBuilder NXOpen::Gateway::ImageCaptureBuilder@endlink  
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Gateway::ImageCaptureBuilder * CreateImageCaptureBuilder
            (
            );
        }; //lint !e1712 default constructor not defined for class  

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
