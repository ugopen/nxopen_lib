#ifndef NXOpen_CAE_POSTGENERALPREFERENCE_HXX_INCLUDED
#define NXOpen_CAE_POSTGENERALPREFERENCE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_PostGeneralPreference.ja
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
#include <NXOpen/libnxopencpp_cae_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace CAE
    {
        class PostGeneralPreference;
    }
    namespace CAE
    {
        class PostPreference;
    }
    namespace CAE
    {
        class PostGeneralPreferenceImpl;
        /** Represents General Post Preferences  <br> To obtain an instance of this class use CAE::CaePost::Preference  <br> 
         <br>  Created in NX1847.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  PostGeneralPreference
        {
            private: PostGeneralPreferenceImpl * m_postgeneralpreference_impl;
            private: NXOpen::CAE::PostPreference* m_owner;
            /// \cond NX_NO_DOC 
            public: explicit PostGeneralPreference(NXOpen::CAE::PostPreference *owner);


            /// \endcond 
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~PostGeneralPreference();
            /**Returns  the tolerance for distance to mesh 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: double DistToMeshTolerance
            (
            );
            /**Sets  the tolerance for distance to mesh 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: void SetDistToMeshTolerance
            (
                double distToMeshTol /** disttomeshtol */ 
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
