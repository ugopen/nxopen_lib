#ifndef NXOpen_CAM_PATHDISPLAY_HXX_INCLUDED
#define NXOpen_CAM_PATHDISPLAY_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_PathDisplay.ja
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
        class PathDisplay;
    }
    namespace CAM
    {
        class CAMSession;
    }
    namespace CAM
    {
        class CAMObject;
    }
    namespace CAM
    {
        class PathDisplayImpl;
        /** Represents a class that is used for NX testing.  This class should not
            be made available to customers  <br> To obtain an instance of this class, refer to @link NXOpen::CAM::CAMSession  NXOpen::CAM::CAMSession @endlink  <br> 
         <br>  Created in NX10.0.2.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  PathDisplay
        {
            /** Choices for coloring the tool path motions */
            public: enum ColorByType
            {
                ColorByTypeMotionType/** motion type */ ,
                ColorByTypeOperation/** operation */ ,
                ColorByTypeTool/** tool */ ,
                ColorByTypeMotionLength/** motion length */ ,
                ColorByTypeMotionGeometry/** motion geometry */ ,
                ColorByTypeFinding/** finding */ 
            };

            private: PathDisplayImpl * m_pathdisplay_impl;
            private: NXOpen::CAM::CAMSession* m_owner;
            /// \cond NX_NO_DOC 
            public: explicit PathDisplay(NXOpen::CAM::CAMSession *owner);


            /// \endcond 
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~PathDisplay();
            /**Returns  the color by property 
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::PathDisplay::ColorByType ColorBy
            (
            );
            /**Sets  the color by property 
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : None */
            public: void SetColorBy
            (
                NXOpen::CAM::PathDisplay::ColorByType colorBy /** colorby */ 
            );
            /**Returns  the indicator to display tool path at the tool center instead of the tool tip for a ball mill. 
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : None */
            public: bool ShowToolCenter
            (
            );
            /**Sets  the indicator to display tool path at the tool center instead of the tool tip for a ball mill. 
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : None */
            public: void SetShowToolCenter
            (
                bool isOn /** ison */ 
            );
            /**Returns  the indicator to display only cutting moves in a tool path. 
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : None */
            public: bool ShowCutting
            (
            );
            /**Sets  the indicator to display only cutting moves in a tool path. 
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : None */
            public: void SetShowCutting
            (
                bool isOn /** ison */ 
            );
            /**Returns  the indicator to display only non cutting moves in a tool path. 
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : None */
            public: bool ShowNoncutting
            (
            );
            /**Sets  the indicator to display only non cutting moves in a tool path. 
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : None */
            public: void SetShowNoncutting
            (
                bool isOn /** ison */ 
            );
            /**Returns  the indicator to display symbol at the end of each motion. 
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : None */
            public: bool ShowEndpoints
            (
            );
            /**Sets  the indicator to display symbol at the end of each motion. 
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : None */
            public: void SetShowEndpoints
            (
                bool isOn /** ison */ 
            );
            /** Show tool path 
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : None */
            public: void ShowToolPath
            (
                NXOpen::CAM::CAMObject * opr /** opr */ 
            );
            /** Hide tool path 
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : None */
            public: void HideToolPath
            (
                NXOpen::CAM::CAMObject * opr /** opr */ 
            );

            /// \cond NX_NO_DOC 
            /** Animates the selected operation's tool path display. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: void Play
            (
                bool isFwd /** isfwd */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Animates one (1) frame of the selected operation's tool path display. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: void Step
            (
                bool isFwd /** isfwd */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Animate one path event of the selected operation's tool path display. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: void StepDisplay
            (
                bool isFwd /** isfwd */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Set animation speed 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: void SetAnimationSpeed
            (
                int speed /** speed */ 
            );

            /// \endcond 
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
