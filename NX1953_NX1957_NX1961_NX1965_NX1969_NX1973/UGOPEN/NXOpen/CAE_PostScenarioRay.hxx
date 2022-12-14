#ifndef NXOpen_CAE_POSTSCENARIORAY_HXX_INCLUDED
#define NXOpen_CAE_POSTSCENARIORAY_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_PostScenarioRay.ja
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
#include <NXOpen/ugmath.hxx>
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
        class PostScenarioRay;
    }
    namespace CAE
    {
        class _PostScenarioRayBuilder;
        class PostScenarioRayImpl;
        /** The collection of Rays in a Ray Model View, in the context of a @link CAE::PostScenario CAE::PostScenario@endlink .
               <br> You can retrieve rays from @link CAE::PostScenarioRayCollection CAE::PostScenarioRayCollection@endlink .  <br> 
         <br>  Created in NX1953.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  PostScenarioRay : public NXOpen::TaggedObject
        {
            private: PostScenarioRayImpl * m_postscenarioray_impl;
            private: friend class  _PostScenarioRayBuilder;
            protected: PostScenarioRay();
            public: ~PostScenarioRay();
            /**Returns  the Ray number within its plot. 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: int Number
            (
            );
            /** Read ray data. 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXOpen::Point3d> GetPoints
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
