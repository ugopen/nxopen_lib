#ifndef NXOpen_DISPLAY_STUDIOIMAGECAPTUREBUILDER_HXX_INCLUDED
#define NXOpen_DISPLAY_STUDIOIMAGECAPTUREBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Display_StudioImageCaptureBuilder.ja
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
        class StudioImageCaptureBuilder;
    }
    class Builder;
    namespace Display
    {
        class _StudioImageCaptureBuilderBuilder;
        class StudioImageCaptureBuilderImpl;
        /** Represents a @link NXOpen::Display::StudioImageCaptureBuilder NXOpen::Display::StudioImageCaptureBuilder@endlink   
             <br> This class is restricted to being called from a program running during an 
            Interactive NX session.  If run from a non-interactive session it will 
            return NULL. <br>  <br> To create a new instance of this class, use @link NXOpen::ViewCollection::CreateStudioImageCaptureBuilder  NXOpen::ViewCollection::CreateStudioImageCaptureBuilder @endlink  <br> 
        Default values.
        <list type="table"> 
         
        <listheader><term> 
        Property</term>  <description> 
        Value</description> </listheader>
        <item><term> 
         
        AASamplesEnum </term> <description> 
         
        Sam0X </description> </item> 

        <item><term> 
         
        DpiEnum </term> <description> 
         
        Dpi72 </description> </item> 

        <item><term> 
         
        DrawingSizeEnum </term> <description> 
         
        Isoa4 </description> </item> 

        <item><term> 
         
        OrientEnum </term> <description> 
         
        Landscape </description> </item> 

        <item><term> 
         
        UnitsEnum </term> <description> 
         
        Pixels </description> </item> 

        </list> 

         <br>  Created in NX6.0.4.  <br>  
        */
        class NXOPENCPP_DISPLAYEXPORT  StudioImageCaptureBuilder : public NXOpen::Builder
        {
            /** Provide the following resolution unit options to screen capture */
            public: enum UnitsEnumType
            {
                UnitsEnumTypePixels/** Use pixel to define resolution */,
                UnitsEnumTypeMm/** Use Millimeters to define resolution */,
                UnitsEnumTypeInches/** Use Inched to define resolution */
            };

            /** Provide the following options to image orientation */
            public: enum OrientEnumType
            {
                OrientEnumTypeLandscape/** Capture image in landscape mode */,
                OrientEnumTypePortrait/** Capture image in portrait mode */
            };

            /** Provide the following standard Drawing sizes */
            public: enum DrawingSizeEnumType
            {
                DrawingSizeEnumTypeIsoa4/** Use ISO A4 drawing size */,
                DrawingSizeEnumTypeIsoa3/** Use ISO A3 drawing size */,
                DrawingSizeEnumTypeIsoa2/** Use ISO A2 drawing size */,
                DrawingSizeEnumTypeIsoa1/** Use ISO A1 drawing size */,
                DrawingSizeEnumTypeIsoa0/** Use ISO A0 drawing size */,
                DrawingSizeEnumTypeAnsia/** Use ANSI A drawing size */,
                DrawingSizeEnumTypeAnsib/** Use ANSI B drawing size */,
                DrawingSizeEnumTypeAnsic/** Use ANSI C drawing size */,
                DrawingSizeEnumTypeAnsid/** Use ANSI D drawing size */,
                DrawingSizeEnumTypeAnsie/** Use ANSI E drawing size */,
                DrawingSizeEnumTypeCustom/** Use custom defined drawing size */
            };

            /** Provide the following screen capture resolutions in dots per inch */
            public: enum DPIEnumType
            {
                DPIEnumTypeDpi72/** Set image at 72 DPI resolution */,
                DPIEnumTypeDpi150/** Set image at 150 DPI resolution */,
                DPIEnumTypeDpi400/** Set image at 400 DPI resolution */
            };

            /** Provide the following anti-aliasing sample size for off screen image capture */
            public: enum AASamplesEnumType
            {
                AASamplesEnumTypeSam0X/** Do not set sampling option */,
                AASamplesEnumTypeSam2X/** Set sampling at 2 times */,
                AASamplesEnumTypeSam4X/** Set sampling at 4 times */,
                AASamplesEnumTypeSam8X/** Set sampling at 8 times */,
                AASamplesEnumTypeSam16X/** Set sampling at 16 times */
            };

            private: StudioImageCaptureBuilderImpl * m_studioimagecapturebuilder_impl;
            private: friend class  _StudioImageCaptureBuilderBuilder;
            protected: StudioImageCaptureBuilder();
            public: ~StudioImageCaptureBuilder();
            /**Returns  the units enum 
             <br>  Created in NX6.0.4.  <br>  
             <br> License requirements : None */
            public: NXOpen::Display::StudioImageCaptureBuilder::UnitsEnumType UnitsEnum
            (
            );
            /**Sets  the units enum 
             <br>  Created in NX6.0.4.  <br>  
             <br> License requirements : None */
            public: void SetUnitsEnum
            (
                NXOpen::Display::StudioImageCaptureBuilder::UnitsEnumType unitsEnum /** unitsenum */ 
            );
            /**Returns  the orient enum 
             <br>  Created in NX6.0.4.  <br>  
             <br> License requirements : None */
            public: NXOpen::Display::StudioImageCaptureBuilder::OrientEnumType OrientEnum
            (
            );
            /**Sets  the orient enum 
             <br>  Created in NX6.0.4.  <br>  
             <br> License requirements : None */
            public: void SetOrientEnum
            (
                NXOpen::Display::StudioImageCaptureBuilder::OrientEnumType orientEnum /** orientenum */ 
            );
            /**Returns  the drawing size enum 
             <br>  Created in NX6.0.4.  <br>  
             <br> License requirements : None */
            public: NXOpen::Display::StudioImageCaptureBuilder::DrawingSizeEnumType DrawingSizeEnum
            (
            );
            /**Sets  the drawing size enum 
             <br>  Created in NX6.0.4.  <br>  
             <br> License requirements : None */
            public: void SetDrawingSizeEnum
            (
                NXOpen::Display::StudioImageCaptureBuilder::DrawingSizeEnumType drawingSizeEnum /** drawingsizeenum */ 
            );
            /**Returns  the dpi enum 
             <br>  Created in NX6.0.4.  <br>  
             <br> License requirements : None */
            public: NXOpen::Display::StudioImageCaptureBuilder::DPIEnumType DpiEnum
            (
            );
            /**Sets  the dpi enum 
             <br>  Created in NX6.0.4.  <br>  
             <br> License requirements : None */
            public: void SetDpiEnum
            (
                NXOpen::Display::StudioImageCaptureBuilder::DPIEnumType dpiEnum /** dpienum */ 
            );
            /**Returns  the antialiasing samples enum 
             <br>  Created in NX6.0.4.  <br>  
             <br> License requirements : None */
            public: NXOpen::Display::StudioImageCaptureBuilder::AASamplesEnumType AASamplesEnum
            (
            );
            /**Sets  the antialiasing samples enum 
             <br>  Created in NX6.0.4.  <br>  
             <br> License requirements : None */
            public: void SetAASamplesEnum
            (
                NXOpen::Display::StudioImageCaptureBuilder::AASamplesEnumType aASamplesEnum /** aasamplesenum */ 
            );
            /**Returns  the native file browser for image type to produce 
             <br>  Created in NX6.0.4.  <br>  
             <br> License requirements : None */
            public: NXString NativeFileBrowser
            (
            );
            /**Sets  the native file browser for image type to produce 
             <br>  Created in NX6.0.4.  <br>  
             <br> License requirements : None */
            public: void SetNativeFileBrowser
            (
                const NXString & filename /** filename */ 
            );
            /**Sets  the native file browser for image type to produce 
             <br>  Created in NX6.0.4.  <br>  
             <br> License requirements : None */
            void SetNativeFileBrowser
            (
                const char * filename /** filename */ 
            );
            /** Gets the double image dimensions, height and width  @return  array of 2 doubles 
             <br>  Created in NX6.0.4.  <br>  
             <br> License requirements : None */
            public: std::vector<double> GetImageDimensionsDouble
            (
            );
            /** Sets the double image dimensions, height and width 
             <br>  Created in NX6.0.4.  <br>  
             <br> License requirements : None */
            public: void SetImageDimensionsDouble
            (
                const std::vector<double> & imageDimensionsDouble /** array of 2 doubles */
            );
            /** Gets the integer image dimensions, height and width  @return  array of 2 integers 
             <br>  Created in NX6.0.4.  <br>  
             <br> License requirements : None */
            public: std::vector<int> GetImageDimensionsInteger
            (
            );
            /** Sets the integer image dimensions, height and width 
             <br>  Created in NX6.0.4.  <br>  
             <br> License requirements : None */
            public: void SetImageDimensionsInteger
            (
                const std::vector<int> & imageDimensionsInteger /** array of 2 integers */
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
