#ifndef NXOpen_DISPLAY_IMAGETESTBUILDER_HXX_INCLUDED
#define NXOpen_DISPLAY_IMAGETESTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Display_ImageTestBuilder.ja
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
#include <NXOpen/Display_ImageTestBuilder.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/libnxopendebugsessioncpp_exports.hxx>

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
        class ImageTestBuilder;
    }
    class Builder;
    namespace Display
    {
        class _ImageTestBuilderBuilder;
        class ImageTestBuilderImpl;

        /// \cond NX_NO_DOC 
        /** Supports debug dialog UGS::DebugUI::UICompImageTest which is used to
                test Gateway::ImageIO, DSS, CGP, AW2D, and CGM image functionality.  <br> To create a new instance of this class, use @link NXOpen::DebugSession::CreateImageTestBuilder  NXOpen::DebugSession::CreateImageTestBuilder @endlink  <br> 
         <br>  Created in NX9.0.0.  <br>  
        */
        class NXOPENDEBUGSESSIONCPPEXPORT  ImageTestBuilder : public NXOpen::Builder
        {
            /** Indicates the Format used to display the image. */
            public: enum FormatType
            {
                FormatTypeOriginal/** original */ ,
                FormatTypeRgb/** rgb */ ,
                FormatTypeRgba/** rgba */ ,
                FormatTypeGrayscale/** grayscale */ ,
                FormatTypeGrayscaleAlpha/** grayscale alpha */ ,
                FormatTypeBitonal/** bitonal */ ,
                FormatTypeAlpha/** alpha */ 
            };

            /** Indicates the location on the image that represents its origin. */
            public: enum OriginLocationType
            {
                OriginLocationTypeTopLeft/** top left */ ,
                OriginLocationTypeTopCenter/** top center */ ,
                OriginLocationTypeTopRight/** top right */ ,
                OriginLocationTypeMiddleLeft/** middle left */ ,
                OriginLocationTypeMiddleCenter/** middle center */ ,
                OriginLocationTypeMiddleRight/** middle right */ ,
                OriginLocationTypeBottomLeft/** bottom left */ ,
                OriginLocationTypeBottomCenter/** bottom center */ ,
                OriginLocationTypeBottomRight/** bottom right */ 
            };

            /** Indicates the extra display attribute that is enabled for
                        the display object (DISP_OBJ) that displays the image in
                        the graphics window. */
            public: enum AttributeType
            {
                AttributeTypeNone/** none */ ,
                AttributeTypeDeEmphasis/** de emphasis */ ,
                AttributeTypeShowThrough/** show through */ ,
                AttributeTypeOverlay/** overlay */ 
            };

            private: ImageTestBuilderImpl * m_imagetestbuilder_impl;
            private: friend class  _ImageTestBuilderBuilder;
            protected: ImageTestBuilder();
            public: ~ImageTestBuilder();
            /**Returns  the path of the image file. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXString ImageFile
            (
            );
            /**Sets  the path of the image file. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: void SetImageFile
            (
                const NXString & filename /** filename */ 
            );
            /**Sets  the path of the image file. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            void SetImageFile
            (
                const char * filename /** filename */ 
            );
            /**Returns  the image details 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXString ImageDetails
            (
            );
            /**Sets  the image details 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: void SetImageDetails
            (
                const NXString & imageDetails /** imagedetails */ 
            );
            /**Sets  the image details 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            void SetImageDetails
            (
                const char * imageDetails /** imagedetails */ 
            );
            /**Returns  the Format of the image. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Display::ImageTestBuilder::FormatType PixelFormat
            (
            );
            /**Sets  the Format of the image. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: void SetPixelFormat
            (
                NXOpen::Display::ImageTestBuilder::FormatType pixelFormat /** pixelformat */ 
            );
            /**Returns  the Format used to display the image. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Display::ImageTestBuilder::FormatType DisplayFormat
            (
            );
            /**Sets  the Format used to display the image. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: void SetDisplayFormat
            (
                NXOpen::Display::ImageTestBuilder::FormatType displayFormat /** displayformat */ 
            );
            /**Returns  the X coordinate of the upper-left corner of the SubimageRectangle. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: int SubimageRectangleX
            (
            );
            /**Sets  the X coordinate of the upper-left corner of the SubimageRectangle. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: void SetSubimageRectangleX
            (
                int subimageRectangleX /** subimagerectanglex */ 
            );
            /**Returns  the Y coordinate of the upper-left corner of the SubimageRectangle. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: int SubimageRectangleY
            (
            );
            /**Sets  the Y coordinate of the upper-left corner of the SubimageRectangle. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: void SetSubimageRectangleY
            (
                int subimageRectangleY /** subimagerectangley */ 
            );
            /**Returns  the width of the SubimageRectangle. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: int SubimageRectangleWidth
            (
            );
            /**Sets  the width of the SubimageRectangle. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: void SetSubimageRectangleWidth
            (
                int subimageRectangleWidth /** subimagerectanglewidth */ 
            );
            /**Returns  the height of the SubimageRectangle. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: int SubimageRectangleHeight
            (
            );
            /**Sets  the height of the SubimageRectangle. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: void SetSubimageRectangleHeight
            (
                int subimageRectangleHeight /** subimagerectangleheight */ 
            );
            /**Returns  the matrix vectors 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXString MatrixVectors
            (
            );
            /**Sets  the matrix vectors 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: void SetMatrixVectors
            (
                const NXString & matrixVectors /** matrixvectors */ 
            );
            /**Sets  the matrix vectors 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            void SetMatrixVectors
            (
                const char * matrixVectors /** matrixvectors */ 
            );
            /**Returns  the UseTransparencyPixel setting. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: bool UseTransparencyPixel
            (
            );
            /**Sets  the UseTransparencyPixel setting. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: void SetUseTransparencyPixel
            (
                bool useTransparencyPixel /** usetransparencypixel */ 
            );
            /** Returns the TransparencyPixel.  @return  Array of 3 RGB values, each between 0 and 1 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<double> GetTransparencyPixel
            (
            );
            /** Sets the TransparencyPixel. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: void SetTransparencyPixel
            (
                const std::vector<double> & transparencyPixel /** Array of 3 RGB values, each between 0 and 1 */
            );
            /** Returns the ForegroundColor.  @return  Array of 3 RGB values, each between 0 and 1 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<double> GetForegroundColor
            (
            );
            /** Sets the ForegroundColor. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: void SetForegroundColor
            (
                const std::vector<double> & foregroundColor /** Array of 3 RGB values, each between 0 and 1 */
            );
            /** Returns the BackgroundColor.  @return  Array of 3 RGB values, each between 0 and 1 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<double> GetBackgroundColor
            (
            );
            /** Sets the BackgroundColor. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: void SetBackgroundColor
            (
                const std::vector<double> & backgroundColor /** Array of 3 RGB values, each between 0 and 1 */
            );
            /**Returns  the location on the image that represents its origin. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Display::ImageTestBuilder::OriginLocationType OriginLocation
            (
            );
            /**Sets  the location on the image that represents its origin. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: void SetOriginLocation
            (
                NXOpen::Display::ImageTestBuilder::OriginLocationType originLocation /** originlocation */ 
            );
            /**Returns  the Pixels Per Inch setting. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: int PixelsPerInch
            (
            );
            /**Sets  the Pixels Per Inch setting. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: void SetPixelsPerInch
            (
                int pixelsPerInch /** pixelsperinch */ 
            );
            /**Returns  the Translucency setting. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: int Translucency
            (
            );
            /**Sets  the Translucency setting. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: void SetTranslucency
            (
                int translucency /** translucency */ 
            );
            /**Returns  the DrawBorder setting. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: bool DrawBorder
            (
            );
            /**Sets  the DrawBorder setting. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: void SetDrawBorder
            (
                bool drawBorder /** drawborder */ 
            );
            /**Returns  the SuppressDeEmphasis setting. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: bool SuppressDeEmphasis
            (
            );
            /**Sets  the SuppressDeEmphasis setting. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: void SetSuppressDeEmphasis
            (
                bool suppressDeEmphasis /** suppressdeemphasis */ 
            );
            /**Returns  the SuppressSmoothing setting. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: bool SuppressSmoothing
            (
            );
            /**Sets  the SuppressSmoothing setting. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: void SetSuppressSmoothing
            (
                bool suppressSmoothing /** suppresssmoothing */ 
            );
            /**Returns  the Delete Previous Images setting. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: bool DeletePreviousImages
            (
            );
            /**Sets  the Delete Previous Images setting. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: void SetDeletePreviousImages
            (
                bool deletePreviousImages /** deletepreviousimages */ 
            );
            /**Returns  the extra display attribute that is enabled for the display object
                        (DISP_OBJ) that displays the image in the graphics window. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Display::ImageTestBuilder::AttributeType ExtraAttribute
            (
            );
            /**Sets  the extra display attribute that is enabled for the display object
                        (DISP_OBJ) that displays the image in the graphics window. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: void SetExtraAttribute
            (
                NXOpen::Display::ImageTestBuilder::AttributeType extraAttribute /** extraattribute */ 
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
