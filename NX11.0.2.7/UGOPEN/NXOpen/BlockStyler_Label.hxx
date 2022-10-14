#ifndef NXOpen_BLOCKSTYLER_LABEL_HXX_INCLUDED
#define NXOpen_BLOCKSTYLER_LABEL_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     BlockStyler_Label.ja
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
#include <NXOpen/BlockStyler_Label.hxx>
#include <NXOpen/BlockStyler_UIBlock.hxx>
#include <NXOpen/libnxopenuicpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace BlockStyler
    {
        class Label;
    }
    namespace BlockStyler
    {
        class UIBlock;
    }
    namespace BlockStyler
    {
        class _LabelBuilder;
        class LabelImpl;
        /** Represents a Label
         <br>  Created in NX8.5.0.  <br>  
        */
        class NXOPENUICPPEXPORT  Label : public NXOpen::BlockStyler::UIBlock
        {
            private: LabelImpl * m_label_impl;
            private: friend class  _LabelBuilder;
            protected: Label();
            public: ~Label();
            /**Returns  the BalloonTooltipImage
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXString BalloonTooltipImage
            (
            );
            /**Sets  the BalloonTooltipImage
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetBalloonTooltipImage
            (
                const NXString & imageString /** image string */ 
            );
            /**Sets  the BalloonTooltipImage
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            void SetBalloonTooltipImage
            (
                const char * imageString /** image string */ 
            );
            /**Returns  the BalloonTooltipLayout as string
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXString BalloonTooltipLayoutAsString
            (
            );
            /**Sets  the BalloonTooltipLayout as string
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetBalloonTooltipLayoutAsString
            (
                const NXString & enumString /** enumstring */ 
            );
            /**Sets  the BalloonTooltipLayout as string
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            void SetBalloonTooltipLayoutAsString
            (
                const char * enumString /** enumstring */ 
            );
            /** Gets the BalloonTooltipLayout members  @return Values to get from the property 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXString> GetBalloonTooltipLayoutMembers
            (
            );
            /**Returns  the BalloonTooltipText
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXString BalloonTooltipText
            (
            );
            /**Sets  the BalloonTooltipText
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetBalloonTooltipText
            (
                const NXString & tooltipText /** tooltiptext */ 
            );
            /**Sets  the BalloonTooltipText
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            void SetBalloonTooltipText
            (
                const char * tooltipText /** tooltiptext */ 
            );
            /**Returns  the Bitmap
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXString Bitmap
            (
            );
            /**Sets  the Bitmap
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetBitmap
            (
                const NXString & bitmapString /** bitmap string */ 
            );
            /**Sets  the Bitmap
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            void SetBitmap
            (
                const char * bitmapString /** bitmap string */ 
            );
            /**Returns  the HighQualityBitmap
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: bool HighQualityBitmap
            (
            );
            /**Sets  the HighQualityBitmap
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetHighQualityBitmap
            (
                bool highQuality /** high quality */ 
            );
            /**Returns  the Localize. If true, translates the Label string into the current locale language.
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: bool Localize
            (
            );
            /**Sets  the Localize. If true, translates the Label string into the current locale language.
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetLocalize
            (
                bool localize /** localize */ 
            );
            /**Returns  the DisplayBitmapLabel
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: bool DisplayBitmapLabel
            (
            );
            /**Sets  the DisplayBitmapLabel
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetDisplayBitmapLabel
            (
                bool display /** display */ 
            );
            /**Returns  the Tooltip
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXString Tooltip
            (
            );
            /**Sets  the Tooltip
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetTooltip
            (
                const NXString & tooltipString /** tooltip string */ 
            );
            /**Sets  the Tooltip
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            void SetTooltip
            (
                const char * tooltipString /** tooltip string */ 
            );
            /**Returns  the WordWrap
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: bool WordWrap
            (
            );
            /**Sets  the WordWrap
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetWordWrap
            (
                bool wordwrap /** wordwrap */ 
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