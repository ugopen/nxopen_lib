#ifndef NXOpen_DIE_PRESSURESYSTEMCHILDBUILDER_HXX_INCLUDED
#define NXOpen_DIE_PRESSURESYSTEMCHILDBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Die_PressureSystemChildBuilder.ja
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
        class PressureSystemChildBuilder;
    }
    class CartesianCoordinateSystem;
    namespace Features
    {
        class FeatureBuilder;
    }
    class Point;
    namespace Die
    {
        class _PressureSystemChildBuilderBuilder;
        class PressureSystemChildBuilderImpl;
        /** Represents a Die Pressure System Child sub feature.  <br> This sub feature is created via the main feature builder.  <br> 
         <br>  Created in NX4.0.0.  <br>  
        */
        class NXOPENCPP_DIEEXPORT  PressureSystemChildBuilder : public Features::FeatureBuilder
        {
            private: PressureSystemChildBuilderImpl * m_pressuresystemchildbuilder_impl;
            private: friend class  _PressureSystemChildBuilderBuilder;
            protected: PressureSystemChildBuilder();
            public: ~PressureSystemChildBuilder();
            /**Sets  the location of the pressure system. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetPoint
            (
                NXOpen::Point * point /** point */ 
            );
            /**Returns  the location of the pressure system. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: NXOpen::Point * Point
            (
            );
            /**Sets  the csys of the pressure system. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetCsys
            (
                NXOpen::CartesianCoordinateSystem * csys /** csys */ 
            );
            /**Returns  the csys of the pressure system. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: NXOpen::CartesianCoordinateSystem * Csys
            (
            );
            /**Sets  the diameter of the pressure system. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetDiameter
            (
                double diameter /** diameter */ 
            );
            /**Returns  the diameter of the pressure system. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: double Diameter
            (
            );
            /**Sets  the height of the pressure system. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetHeight
            (
                double height /** height */ 
            );
            /**Returns  the height of the pressure system. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: double Height
            (
            );
            /**Sets  the clearance of the pressure system. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetClearance
            (
                double clearance /** clearance */ 
            );
            /**Returns  the clearance of the pressure system. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: double Clearance
            (
            );
            /**Sets  the design status of the pressure system, if true the pressure system will be built into the model, if false it will not. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetDesignStatus
            (
                bool designStatus /** design status */ 
            );
            /**Returns  the design status of the pressure system, if true the pressure system will be built into the model, if false it will not. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: bool DesignStatus
            (
            );
            /**Returns  the build status of the pressure system. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: NXOpen::Die::DieBuildStatusOption BuildStatus
            (
            );
            /**Sets  the display status of the pressure system, if true input data to the pressure system will be displayed, 
                    if false the input data will not be displayed. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetDisplayStatus
            (
                bool displayStatus /** display status */ 
            );
            /**Returns  the display status of the pressure system, if true input data to the pressure system will be displayed, 
                    if false the input data will not be displayed. 
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
