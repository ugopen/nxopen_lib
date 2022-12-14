#ifndef NXOpen_CLDKIN_JOINTJOGBUILDER_HXX_INCLUDED
#define NXOpen_CLDKIN_JOINTJOGBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CLDKin_JointJogBuilder.ja
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
        class JointJogBuilder;
    }
    class Builder;
    class NXObject;
    class SelectDisplayableObject;
    class TaggedObject;
    namespace CLDKin
    {
        class _JointJogBuilderBuilder;
        class JointJogBuilderImpl;
        /**   <br> To create a new instance of this class, use @link NXOpen::CLDKin::CldKinematicsManager::CreateJointJogBuilderBuilder  NXOpen::CLDKin::CldKinematicsManager::CreateJointJogBuilderBuilder @endlink  <br> 
         <br>  Created in NX12.0.1.  <br>  
        */
        class CLDKINOPENCPPEXPORT  JointJogBuilder : public NXOpen::Builder
        {
            private: JointJogBuilderImpl * m_jointjogbuilder_impl;
            private: friend class  _JointJogBuilderBuilder;
            protected: JointJogBuilder();
            public: ~JointJogBuilder();
            /**Returns  the select device 
             <br>  Created in NX12.0.1.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectDisplayableObject * SelectDevice
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
             <br> License requirements : None */
            public: void SetPoseName
            (
                const NXString & poseName /** posename */ 
            );
            /**Sets  the poseName returned
             <br>  Created in NX12.0.2.  <br>  
             <br> License requirements : None */
            void SetPoseName
            (
                const char * poseName /** posename */ 
            );
            /**Returns  the last selected device 
             <br>  Created in NX12.0.2.  <br>  
             <br> License requirements : None */
            public: NXOpen::NXObject * LastSelectedDevice
            (
            );
            /**Sets  the last selected device 
             <br>  Created in NX12.0.2.  <br>  
             <br> License requirements : None */
            public: void SetLastSelectedDevice
            (
                NXOpen::NXObject * lastDeviceSelectedTag /** lastdeviceselectedtag */ 
            );
            /** Apply Joints 
             <br>  Created in NX12.0.2.  <br>  
             <br> License requirements : None */
            public: void ApplyJoints
            (
            );
            /** Apply Pose 
             <br>  Created in NX12.0.2.  <br>  
             <br> License requirements : None */
            public: void ApplyPose
            (
                NXOpen::NXObject * selectedPartOccTag /** selectedpartocctag */ 
            );
            /** Set Joint Jog dialog behaviour data 
             <br>  Created in NX1938.0.0.  <br>  
             <br> License requirements : None */
            public: void SetJointJogBehaviour
            (
                const NXString & sDlgTitle /** sdlgtitle */ ,
                int eDlgState /** edlgstate */ ,
                const NXString & sPoseName /** sposename */ ,
                NXOpen::NXObject * tDeviceTag /** tdevicetag */ 
            );
            /** Set Joint Jog dialog behaviour data 
             <br>  Created in NX1938.0.0.  <br>  
             <br> License requirements : None */
            void SetJointJogBehaviour
            (
                const char * sDlgTitle /** sdlgtitle */ ,
                int eDlgState /** edlgstate */ ,
                const char * sPoseName /** sposename */ ,
                NXOpen::NXObject * tDeviceTag /** tdevicetag */ 
            );
            /** Add JointToMap
             <br>  Created in NX1938.0.0.  <br>  
             <br> License requirements : None */
            public: void AddJointToMap
            (
                NXOpen::TaggedObject * nxkJoint /** nxkjoint */ ,
                double distance /** distance */ 
            );
            /** Update JointToMap
             <br>  Created in NX1938.0.0.  <br>  
             <br> License requirements : None */
            public: void UpdateJointToMap
            (
                NXOpen::TaggedObject * nxkJoint /** nxkjoint */ ,
                double newValue /** newvalue */ 
            );
            /** Remove JointToMap
             <br>  Created in NX1938.0.0.  <br>  
             <br> License requirements : None */
            public: void RemoveAllJointMap
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
