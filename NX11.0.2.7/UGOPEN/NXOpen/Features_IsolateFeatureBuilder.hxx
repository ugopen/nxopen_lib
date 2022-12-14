#ifndef NXOpen_FEATURES_ISOLATEFEATUREBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_ISOLATEFEATUREBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_IsolateFeatureBuilder.ja
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
#include <NXOpen/Features_IsolateFeatureBuilder.hxx>
#include <NXOpen/Features_FeatureBuilder.hxx>
#include <NXOpen/SelectObject.hxx>
#include <NXOpen/libnxopencpp_features_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Features
    {
        class IsolateFeatureBuilder;
    }
    namespace Features
    {
        class FeatureBuilder;
    }
    namespace Features
    {
        class SelectFeature;
    }
    class SelectDisplayableObject;
    namespace Features
    {
        class _IsolateFeatureBuilderBuilder;
        class IsolateFeatureBuilderImpl;
        /** Represents a @link NXOpen::Features::IsolateFeature NXOpen::Features::IsolateFeature@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::Features::FeatureCollection::CreateIsolateFeatureBuilder  NXOpen::Features::FeatureCollection::CreateIsolateFeatureBuilder @endlink  <br> 
         <br>  Created in NX8.5.0.  <br>  
        */
        class NXOPENCPP_FEATURESEXPORT  IsolateFeatureBuilder : public NXOpen::Features::FeatureBuilder
        {
            private: IsolateFeatureBuilderImpl * m_isolatefeaturebuilder_impl;
            private: friend class  _IsolateFeatureBuilderBuilder;
            protected: IsolateFeatureBuilder();
            public: ~IsolateFeatureBuilder();
            /** Returns the feature currently being edited by this builder. If
                    a new feature is being created, and the builder has not yet
                    been commited, returns NULL.
                  @return  
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR cam_base ("CAM BASE") OR geometric_tol ("GDT") OR insp_programming ("INSPECTION PROGRAMMING") */
            public: NXOpen::Features::Feature * GetFeature
            (
            );
            /**Returns  the Feature to Isolate 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::SelectFeature * Feature
            (
            );
            /**Returns  the Proximity Object. This could be either @link NXOpen::DatumPlane NXOpen::DatumPlane@endlink  or @link NXOpen::Point NXOpen::Point@endlink 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectDisplayableObject * ProximityObject
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
