#ifndef NXOpen_CAM_TOOLPATHDISPLAY_HXX_INCLUDED
#define NXOpen_CAM_TOOLPATHDISPLAY_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_ToolPathDisplay.ja
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
    namespace CAM
    {
        class ToolPathDisplay;
    }
    class DebugSession;
    namespace CAM
    {
        class CAMObject;
    }
    namespace CAM
    {
        class ToolPathDisplayImpl;
        /** Represents a class that is used for NX testing.  This class should not
            be made available to customers  <br> To obtain an instance of this class, refer to @link NXOpen::DebugSession  NXOpen::DebugSession @endlink  <br> 
         <br>  Created in NX9.0.2.  <br>  
        */
        class NXOPENDEBUGSESSIONCPPEXPORT  ToolPathDisplay
        {
            /** Choices for coloring the tool path motions */
            public: enum ColorBy
            {
                ColorByMotionType/** motion type */ ,
                ColorByOperation/** operation */ ,
                ColorByTool/** tool */ ,
                ColorByMotionLength/** motion length */ 
            };

            private: ToolPathDisplayImpl * m_toolpathdisplay_impl;
            private: NXOpen::DebugSession* m_owner;
            /// \cond NX_NO_DOC 
            public: explicit ToolPathDisplay(NXOpen::DebugSession *owner);


            /// \endcond 
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~ToolPathDisplay();
            /** Set the option for coloring the tool path motions. 
             <br>  Created in NX9.0.2.  <br>  
             <br> License requirements : None */
            public: void SetColorBy
            (
                NXOpen::CAM::ToolPathDisplay::ColorBy colorBy /** colorby */ 
            );
            /** Displays the tool path at the tool center instead of the tool tip for a ball mill. 
             <br>  Created in NX9.0.2.  <br>  
             <br> License requirements : None */
            public: void ShowToolCenter
            (
                bool isOn /** ison */ 
            );
            /** Displays the cutting moves in a milling tool path. 
             <br>  Created in NX9.0.2.  <br>  
             <br> License requirements : None */
            public: void ShowCutting
            (
                bool isOn /** ison */ 
            );
            /** Displays the non cutting moves in a milling tool path. 
             <br>  Created in NX9.0.2.  <br>  
             <br> License requirements : None */
            public: void ShowNoncutting
            (
                bool isOn /** ison */ 
            );
            /** Displays a symbol at the end of each motion. 
             <br>  Created in NX9.0.2.  <br>  
             <br> License requirements : None */
            public: void ShowEndpoints
            (
                bool isOn /** ison */ 
            );
            /** Debug Trace user button presses. 
             <br>  Created in NX9.0.2.  <br>  
             <br> License requirements : None */
            public: void ButtonDown
            (
                bool isOn /** ison */ 
            );
            /** Debug Measure display time 
             <br>  Created in NX9.0.2.  <br>  
             <br> License requirements : None */
            public: void Timer
            (
                bool isOn /** ison */ 
            );
            /** Debug Trace display functions 
             <br>  Created in NX9.0.2.  <br>  
             <br> License requirements : None */
            public: void Trace
            (
                bool isOn /** ison */ 
            );
            /** Debug Table of tool path display motions 
             <br>  Created in NX9.0.2.  <br>  
             <br> License requirements : None */
            public: void Table
            (
                bool isOn /** ison */ 
            );
            /** Show tool path 
             <br>  Created in NX9.0.2.  <br>  
             <br> License requirements : None */
            public: void ShowToolPath
            (
                NXOpen::CAM::CAMObject * opr /** opr */ 
            );
            /** Hide tool path 
             <br>  Created in NX9.0.2.  <br>  
             <br> License requirements : None */
            public: void HideToolPath
            (
                NXOpen::CAM::CAMObject * opr /** opr */ 
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
