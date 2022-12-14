#ifndef NXOpen_FEATURES_DIRECTVISIONBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_DIRECTVISIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_DirectVisionBuilder.ja
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
#include <NXOpen/Features_FeatureBuilder.hxx>
#include <NXOpen/SelectObject.hxx>
#include <NXOpen/libnxopencpp_features_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Features
    {
        class DirectVisionBuilder;
    }
    namespace Features
    {
        class FeatureBuilder;
    }
    namespace Features
    {
        class SelectFeature;
    }
    namespace Features
    {
        class _DirectVisionBuilderBuilder;
        class DirectVisionBuilderImpl;

        /// \cond NX_NO_DOC 
        /**
            Represents a @link Features::DirectVision Features::DirectVision@endlink  builder
             <br> To create a new instance of this class, use @link NXOpen::Features::AVDACollection::CreateDirectVisionBuilder  NXOpen::Features::AVDACollection::CreateDirectVisionBuilder @endlink  <br> 
        Default values.
        <list type="table"> 
         
        <listheader><term> 
        Property</term>  <description> 
        Value</description> </listheader>
        <item><term> 
         
        EyePointType </term> <description> 
         
        Monocular </description> </item> 

        </list> 

         <br>  Created in NX1953.0.0.  <br>  
        */
        class NXOPENCPP_FEATURESEXPORT  DirectVisionBuilder : public NXOpen::Features::FeatureBuilder
        {
            /** Represents the eyepoint type */
            public: enum VisionType
            {
                VisionTypeMonocular/** monocular */ ,
                VisionTypeBinocular/** binocular */ 
            };

            private: DirectVisionBuilderImpl * m_directvisionbuilder_impl;
            private: friend class  _DirectVisionBuilderBuilder;
            protected: DirectVisionBuilder();
            public: ~DirectVisionBuilder();

            /// \cond NX_NO_DOC 
            /**Returns  the eye point type 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::DirectVisionBuilder::VisionType EyePointType
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the eye point type 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_general_packaging ("NX General Packaging") */
            public: void SetEyePointType
            (
                NXOpen::Features::DirectVisionBuilder::VisionType eyePointType /** eyepointtype */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the eyellipse 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::SelectFeature * Eyellipse
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the standard 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: NXString Standard
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the standard 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_general_packaging ("NX General Packaging") */
            public: void SetStandard
            (
                const NXString & standard /** standard */ 
            );
            /**Sets  the standard 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_general_packaging ("NX General Packaging") */
            void SetStandard
            (
                const char * standard /** standard */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the eye point 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: NXString EyePoint
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the eye point 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_general_packaging ("NX General Packaging") */
            public: void SetEyePoint
            (
                const NXString & eyePoint /** eyepoint */ 
            );
            /**Sets  the eye point 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_general_packaging ("NX General Packaging") */
            void SetEyePoint
            (
                const char * eyePoint /** eyepoint */ 
            );

            /// \endcond 
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
