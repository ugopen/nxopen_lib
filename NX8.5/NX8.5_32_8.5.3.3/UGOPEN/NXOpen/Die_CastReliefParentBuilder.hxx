#ifndef NXOpen_DIE_CASTRELIEFPARENTBUILDER_HXX_INCLUDED
#define NXOpen_DIE_CASTRELIEFPARENTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Die_CastReliefParentBuilder.ja
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
#include <NXOpen/Die.hxx>
#include <NXOpen/Features_FeatureBuilder.hxx>
#include <NXOpen/libnxopencpp_die_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Die
    {
        class CastReliefParentBuilder;
    }
    class Body;
    namespace Features
    {
        class FeatureBuilder;
    }
    class IProfile;
    namespace Die
    {
        class _CastReliefParentBuilderBuilder;
        class CastReliefParentBuilderImpl;
        /** Represents a Die Cast Relief sub feature.  <br> This sub feature is created via the main feature builder.  <br> 
         <br>  Created in NX4.0.0.  <br>  
        */
        class NXOPENCPP_DIEEXPORT  CastReliefParentBuilder : public Features::FeatureBuilder
        {
            private: CastReliefParentBuilderImpl * m_castreliefparentbuilder_impl;
            private: friend class  _CastReliefParentBuilderBuilder;
            protected: CastReliefParentBuilder();
            public: ~CastReliefParentBuilder();
            /** Sets the profile of the cast relief. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetCastRelief
            (
                NXOpen::Die::DirectionOption direction /** Profile direction. */,
                const std::vector<NXOpen::IProfile *> & profileEntries /** The profile entries, can be curves, edges, faces, sketches or curve features. */
            );
            /** Gets the profile of the cast relief.  @return  The profile entries, will be curves, edges, faces, sketches or curve features. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: std::vector<NXOpen::IProfile *> GetCastRelief
            (
                NXOpen::Die::DirectionOption* direction /** Profile direction. */
            );
            /**Sets  the relief sheet of cast relief. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetReliefSheet
            (
                NXOpen::Body * reliefSheet /** relief sheet */ 
            );
            /**Returns  the relief sheet of cast relief. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: NXOpen::Body * ReliefSheet
            (
            );
            /**Sets  the relief depth of cast relief. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetReliefDepth
            (
                double reliefDepth /** relief depth */ 
            );
            /**Returns  the relief depth of cast relief. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: double ReliefDepth
            (
            );
            /**Sets  the design status of cast relief, if true the cast relief will be built into the model, if false it will not. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetDesignStatus
            (
                bool designStatus /** design status */ 
            );
            /**Returns  the design status of cast relief, if true the cast relief will be built into the model, if false it will not. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: bool DesignStatus
            (
            );
            /**Returns  the build status of cast relief. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: NXOpen::Die::DieBuildStatusOption BuildStatus
            (
            );
            /**Sets  the display status of cast relief, if true input data to the cast relief will be displayed, if false the input data will not be displayed. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetDisplayStatus
            (
                bool displayStatus /** display status */ 
            );
            /**Returns  the display status of cast relief, if true input data to the cast relief will be displayed, if false the input data will not be displayed. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: bool DisplayStatus
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
