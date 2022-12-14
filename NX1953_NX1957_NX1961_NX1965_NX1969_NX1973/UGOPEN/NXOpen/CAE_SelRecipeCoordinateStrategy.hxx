#ifndef NXOpen_CAE_SELRECIPECOORDINATESTRATEGY_HXX_INCLUDED
#define NXOpen_CAE_SELRECIPECOORDINATESTRATEGY_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_SelRecipeCoordinateStrategy.ja
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
#include <NXOpen/CAE_SelRecipeStrategy.hxx>
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
        class SelRecipeCoordinateStrategy;
    }
    namespace CAE
    {
        class SelRecipeStrategy;
    }
    namespace CAE
    {
        class _SelRecipeCoordinateStrategyBuilder;
        class SelRecipeCoordinateStrategyImpl;
        /**  @brief  Represents a coordinate strategy that resolves to a single node  

          <br> Use the @link NXOpen::CAE::SelRecipeBuilder NXOpen::CAE::SelRecipeBuilder@endlink  class to add strategy.  <br> 
         <br>  Created in NX1847.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  SelRecipeCoordinateStrategy : public NXOpen::CAE::SelRecipeStrategy
        {
            /** the resolve preference */
            public: enum Pref
            {
                PrefLowestLabel/** lowest label */ ,
                PrefHighestLabel/** highest label */ ,
                PrefClosestNode/** closest node */ 
            };

            private: SelRecipeCoordinateStrategyImpl * m_selrecipecoordinatestrategy_impl;
            private: friend class  _SelRecipeCoordinateStrategyBuilder;
            protected: SelRecipeCoordinateStrategy();
            public: ~SelRecipeCoordinateStrategy();
            /**Returns  the target coordinates. 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::Point3d Coordinates
            (
            );
            /**Returns  the tolerance. 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: double Tolerance
            (
            );
            /** Set the target coordinates. 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetCoordinatesAndTolerance
            (
                const NXOpen::Point3d & coordinates /** coordinates */ ,
                double tolerance /** tolerance */ 
            );
            /**Returns  the resolve preference. Set to Lowest Label by default.Used as declash in case the recipe finds multiple nodes within tolerance 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::SelRecipeCoordinateStrategy::Pref ResolvePreference
            (
            );
            /** Set the resolve preference. 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetResolvePreference
            (
                NXOpen::CAE::SelRecipeCoordinateStrategy::Pref resolvePref /** resolvepref */ 
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
