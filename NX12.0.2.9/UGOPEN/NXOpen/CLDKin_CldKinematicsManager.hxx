#ifndef NXOpen_CLDKIN_CLDKINEMATICSMANAGER_HXX_INCLUDED
#define NXOpen_CLDKIN_CLDKINEMATICSMANAGER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CLDKin_CldKinematicsManager.ja
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
#include <NXOpen/BasePart.hxx>
#include <NXOpen/TaggedObject.hxx>
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
        class CldKinematicsManager;
    }
    class Session;
    namespace CLDKin
    {
        class JointJogBuilder;
    }
    namespace CLDKin
    {
        class PoseEditorBuilder;
    }
    class Part;
    namespace CLDKin
    {
        class CldKinematicsManagerImpl;
        /** Represents a Manager of CLD Kinematics dialogs  <br> Use the static method in this class to obtain an instance.  <br> 
         <br>  Created in NX12.0.1.  <br>  
        */
        class CLDKINOPENCPPEXPORT  CldKinematicsManager
        {
            private: CldKinematicsManagerImpl * m_cldkinematicsmanager_impl;
            private: NXOpen::Session* m_owner;
            /// \cond NX_NO_DOC 
            public: explicit CldKinematicsManager(NXOpen::Session *owner);


            /// \endcond 
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            private: static CldKinematicsManager* theCldKinematicsManager;
            /** Returns the CldKinematicsManager object for the running session which serves as the 'gateway' class for the application API.  
                References to all other objects in this API are obtained either directly or indirectly via methods and properties on this class.  
                Platform Session should be initialized using 'GetSession' method from NXOpen API prior to this call.  
            */
            public: static CldKinematicsManager* GetCldKinematicsManager(NXOpen::Session *owner);
            public: ~CldKinematicsManager();
            /** To calculate and set attribute group name  @return  
             <br>  Created in NX12.0.1.  <br>  
             <br> License requirements : fp_fixture_planner ("FULL FIXTURE PLANNER") OR ld_line_designer ("FULL LINE DESIGNER") */
            public: NXOpen::CLDKin::JointJogBuilder * CreateJointJogBuilderBuilder
            (
                NXOpen::Part * part /** part */ 
            );
            /** To create pose editor builder  @return  
             <br>  Created in NX12.0.1.  <br>  
             <br> License requirements : fp_fixture_planner ("FULL FIXTURE PLANNER") OR ld_line_designer ("FULL LINE DESIGNER") */
            public: NXOpen::CLDKin::PoseEditorBuilder * CreatePoseEditorBuilder
            (
                NXOpen::Part * part /** part */ 
            );
            /** Export the PLMXML from Mfg Kinematics. 
             <br>  Created in NX12.0.1.  <br>  
             <br> License requirements : fp_fixture_planner ("FULL FIXTURE PLANNER") OR ld_line_designer ("FULL LINE DESIGNER") */
            public: void ExportPlmxml
            (
            );
            /** Import the PLMXML for Mfg Kinematics. 
             <br>  Created in NX12.0.1.  <br>  
             <br> License requirements : fp_fixture_planner ("FULL FIXTURE PLANNER") OR ld_line_designer ("FULL LINE DESIGNER") */
            public: void ImportPlmxml
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
