#ifndef NXOpen_CLDKIN_POSEEDITORBUILDER_HXX_INCLUDED
#define NXOpen_CLDKIN_POSEEDITORBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CLDKin_PoseEditorBuilder.ja
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
#include <NXOpen/SelectObject.hxx>
#include <NXOpen/libcldkinopencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace CLDKin
    {
        class PoseEditorBuilder;
    }
    class Builder;
    class SelectDisplayableObject;
    namespace CLDKin
    {
        class _PoseEditorBuilderBuilder;
        class PoseEditorBuilderImpl;
        /**   <br> To create a new instance of this class, use @link NXOpen::CLDKin::CldKinematicsManager::CreatePoseEditorBuilder  NXOpen::CLDKin::CldKinematicsManager::CreatePoseEditorBuilder @endlink  <br> 
         <br>  Created in NX12.0.1.  <br>  
        */
        class CLDKINOPENCPPEXPORT  PoseEditorBuilder : public NXOpen::Builder
        {
            private: PoseEditorBuilderImpl * m_poseeditorbuilder_impl;
            private: friend class  _PoseEditorBuilderBuilder;
            protected: PoseEditorBuilder();
            public: ~PoseEditorBuilder();
            /**Returns  the select device 
             <br>  Created in NX12.0.1.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectDisplayableObject * SelectDevice
            (
            );
            /** TODO: fill in a description for this 
             <br>  Created in NX12.0.1.  <br>  
             <br> License requirements : fp_fixture_planner ("FULL FIXTURE PLANNER") OR ld_line_designer ("FULL LINE DESIGNER") */
            public: void AddPoseButton
            (
            );
            /** TODO: fill in a description for this 
             <br>  Created in NX12.0.1.  <br>  
             <br> License requirements : fp_fixture_planner ("FULL FIXTURE PLANNER") OR ld_line_designer ("FULL LINE DESIGNER") */
            public: void EditPoseButton
            (
            );
            /** TODO: fill in a description for this 
             <br>  Created in NX12.0.1.  <br>  
             <br> License requirements : fp_fixture_planner ("FULL FIXTURE PLANNER") OR ld_line_designer ("FULL LINE DESIGNER") */
            public: void DeletePoseButton
            (
            );
            /** TODO: fill in a description for this 
             <br>  Created in NX12.0.1.  <br>  
             <br> License requirements : fp_fixture_planner ("FULL FIXTURE PLANNER") OR ld_line_designer ("FULL LINE DESIGNER") */
            public: void JumpPoseButton
            (
            );
            /**Returns  the poseName returned
             <br>  Created in NX12.0.2.  <br>  
             <br> License requirements : None */
            public: NXString PoseName
            (
            );
            /**Sets  the poseName returned
             <br>  Created in NX12.0.2.  <br>  
             <br> License requirements : fp_fixture_planner ("FULL FIXTURE PLANNER") OR ld_line_designer ("FULL LINE DESIGNER") */
            public: void SetPoseName
            (
                const NXString & poseName /** posename */ 
            );
            /**Sets  the poseName returned
             <br>  Created in NX12.0.2.  <br>  
             <br> License requirements : fp_fixture_planner ("FULL FIXTURE PLANNER") OR ld_line_designer ("FULL LINE DESIGNER") */
            void SetPoseName
            (
                const char * poseName /** posename */ 
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
