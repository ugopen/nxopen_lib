#ifndef NXOpen_CAM_LAYOUTCIBUILDER_HXX_INCLUDED
#define NXOpen_CAM_LAYOUTCIBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_LayoutCiBuilder.ja
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
        class LayoutCiBuilder;
    }
    namespace CAM
    {
        class _LayoutCiBuilderBuilder;
        class LayoutCiBuilderImpl;
        /** Represents a layout ci Builder 
         <br>  Created in NX5.0.0.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  LayoutCiBuilder : public NXOpen::TaggedObject
        {
            private: LayoutCiBuilderImpl * m_layoutcibuilder_impl;
            private: friend class  _LayoutCiBuilderBuilder;
            protected: LayoutCiBuilder();
            public: ~LayoutCiBuilder();
            /**Returns  the save layer settings toggle value 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: int LayoutSaveSettings
            (
            );
            /**Sets  the save layer settings toggle value 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetLayoutSaveSettings
            (
                int toggleValue /** the new toggle value */
            );
            /**Returns  the layer name value 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: NXString LayoutName
            (
            );
            /**Sets  the layer name value 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetLayoutName
            (
                const NXString & stringValue /** the new string value */
            );
            /**Sets  the layer name value 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            void SetLayoutName
            (
                const char * stringValue /** the new string value */
            );
            /** Method to save the layer layout. This applies only in the interactive mode and does not do anything in batch mode 
             <br>  Created in NX9.0.1.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SaveLayout
            (
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
