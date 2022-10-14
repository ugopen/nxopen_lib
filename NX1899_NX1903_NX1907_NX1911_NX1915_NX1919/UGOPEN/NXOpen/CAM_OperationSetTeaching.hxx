#ifndef NXOpen_CAM_OPERATIONSETTEACHING_HXX_INCLUDED
#define NXOpen_CAM_OPERATIONSETTEACHING_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_OperationSetTeaching.ja
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
#include <NXOpen/CAM_Teaching.hxx>
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
        class OperationSetTeaching;
    }
    namespace CAM
    {
        class FeatureGeometry;
    }
    namespace CAM
    {
        class Teaching;
    }
    namespace CAM
    {
        class _OperationSetTeachingBuilder;
        class OperationSetTeachingImpl;

        /// \cond NX_NO_DOC 
        /** Represents a OperationSetTeaching Builder  <br> To create a new instance of this class, use @link NXOpen::CAM::CAMSetup::CreateOperationSetTeaching  NXOpen::CAM::CAMSetup::CreateOperationSetTeaching @endlink  <br> 
         <br>  Created in NX10.0.2.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  OperationSetTeaching : public NXOpen::CAM::Teaching
        {
            private: OperationSetTeachingImpl * m_operationsetteaching_impl;
            private: friend class  _OperationSetTeachingBuilder;
            protected: OperationSetTeaching();
            public: ~OperationSetTeaching();
            /** Gets the feature group priority 
             <br>  Created in NX10.0.3.  <br>  
             <br> License requirements : fbm_author ("FBM Author") */
            public: double GetFeatureGroupPriority
            (
                const NXString & name /** name */ 
            );
            /** Gets the feature group priority 
             <br>  Created in NX10.0.3.  <br>  
             <br> License requirements : fbm_author ("FBM Author") */
            double GetFeatureGroupPriority
            (
                const char * name /** name */ 
            );
            /** Sets the feature group priority 
             <br>  Created in NX10.0.3.  <br>  
             <br> License requirements : fbm_author ("FBM Author") */
            public: void SetFeatureGroupPriority
            (
                const NXString & name /** name */ ,
                double priority /** priority */ 
            );
            /** Sets the feature group priority 
             <br>  Created in NX10.0.3.  <br>  
             <br> License requirements : fbm_author ("FBM Author") */
            void SetFeatureGroupPriority
            (
                const char * name /** name */ ,
                double priority /** priority */ 
            );
            /** Gets the feature group conditions 
             <br>  Created in NX10.0.3.  <br>  
             <br> License requirements : fbm_author ("FBM Author") */
            public: NXString GetFeatureGroupCondition
            (
                const NXString & name /** name */ 
            );
            /** Gets the feature group conditions 
             <br>  Created in NX10.0.3.  <br>  
             <br> License requirements : fbm_author ("FBM Author") */
            NXString GetFeatureGroupCondition
            (
                const char * name /** name */ 
            );
            /** Sets the feature group conditions 
             <br>  Created in NX10.0.3.  <br>  
             <br> License requirements : fbm_author ("FBM Author") */
            public: void SetFeatureGroupCondition
            (
                const NXString & name /** name */ ,
                const NXString & condition /** condition */ 
            );
            /** Sets the feature group conditions 
             <br>  Created in NX10.0.3.  <br>  
             <br> License requirements : fbm_author ("FBM Author") */
            void SetFeatureGroupCondition
            (
                const char * name /** name */ ,
                const char * condition /** condition */ 
            );
            /** Gets the operation conditions 
             <br>  Created in NX10.0.3.  <br>  
             <br> License requirements : fbm_author ("FBM Author") */
            public: NXString GetOperationCondition
            (
                const NXString & name /** name */ 
            );
            /** Gets the operation conditions 
             <br>  Created in NX10.0.3.  <br>  
             <br> License requirements : fbm_author ("FBM Author") */
            NXString GetOperationCondition
            (
                const char * name /** name */ 
            );
            /** Sets the operation conditions 
             <br>  Created in NX10.0.3.  <br>  
             <br> License requirements : fbm_author ("FBM Author") */
            public: void SetOperationCondition
            (
                const NXString & name /** name */ ,
                const NXString & condition /** condition */ 
            );
            /** Sets the operation conditions 
             <br>  Created in NX10.0.3.  <br>  
             <br> License requirements : fbm_author ("FBM Author") */
            void SetOperationCondition
            (
                const char * name /** name */ ,
                const char * condition /** condition */ 
            );
            /** Gets the operation addon conditions 
             <br>  Created in NX10.0.3.  <br>  
             <br> License requirements : fbm_author ("FBM Author") */
            public: NXString GetOperationAddonCondition
            (
                const NXString & name /** name */ ,
                const NXString & operationName /** operation name */ 
            );
            /** Gets the operation addon conditions 
             <br>  Created in NX10.0.3.  <br>  
             <br> License requirements : fbm_author ("FBM Author") */
            NXString GetOperationAddonCondition
            (
                const char * name /** name */ ,
                const char * operationName /** operation name */ 
            );
            /** Sets the operation addon conditions 
             <br>  Created in NX10.0.3.  <br>  
             <br> License requirements : fbm_author ("FBM Author") */
            public: void SetOperationAddonCondition
            (
                const NXString & name /** name */ ,
                const NXString & operationName /** operation name */ ,
                const NXString & condition /** condition */ 
            );
            /** Sets the operation addon conditions 
             <br>  Created in NX10.0.3.  <br>  
             <br> License requirements : fbm_author ("FBM Author") */
            void SetOperationAddonCondition
            (
                const char * name /** name */ ,
                const char * operationName /** operation name */ ,
                const char * condition /** condition */ 
            );
            /** Gets the selected feature groups 
             <br>  Created in NX10.0.3.  <br>  
             <br> License requirements : fbm_author ("FBM Author") */
            public: std::vector<NXOpen::CAM::FeatureGeometry *> GetFeatureGroups
            (
            );
            /** Sets the selected feature groups 
             <br>  Created in NX10.0.3.  <br>  
             <br> License requirements : fbm_author ("FBM Author") */
            public: void SetFeatureGroups
            (
                const std::vector<NXOpen::CAM::FeatureGeometry *> & aFeatureGroups /** a feature groups */ 
            );

            /// \cond NX_NO_DOC 
            /** Teaches new operation sets 
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : fbm_author ("FBM Author") */
            public: void Teach
            (
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