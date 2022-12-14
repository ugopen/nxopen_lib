#ifndef NXOpen_FEATURES_TOPOLOGYOPTIMIZATION_SCENERYBODYBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_TOPOLOGYOPTIMIZATION_SCENERYBODYBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_TopologyOptimization_SceneryBodyBuilder.ja
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
#include <NXOpen/SelectObjectList.hxx>
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
        namespace TopologyOptimization
        {
            class SceneryBodyBuilder;
        }
    }
    class Builder;
    class Material;
    class SelectBodyList;
    namespace Features
    {
        namespace TopologyOptimization
        {
            class _SceneryBodyBuilderBuilder;
            class SceneryBodyBuilderImpl;
            /**
                    Represents a @link Features::TopologyOptimization::SceneryBody Features::TopologyOptimization::SceneryBody@endlink  builder
                     <br> To create a new instance of this class, use @link NXOpen::Features::TopologyOptimization::Study::CreateSceneryBodyBuilder  NXOpen::Features::TopologyOptimization::Study::CreateSceneryBodyBuilder @endlink  <br> 
             <br>  Created in NX1953.0.0.  <br>  
            */
            class NXOPENCPP_FEATURESEXPORT  SceneryBodyBuilder : public NXOpen::Builder
            {
                private: SceneryBodyBuilderImpl * m_scenerybodybuilder_impl;
                private: friend class  _SceneryBodyBuilderBuilder;
                protected: SceneryBodyBuilder();
                public: ~SceneryBodyBuilder();
                /**Returns  the scenery body name 
                 <br>  Created in NX1953.0.0.  <br>  
                 <br> License requirements : None */
                public: NXString SceneryBodyName
                (
                );
                /**Sets  the scenery body name 
                 <br>  Created in NX1953.0.0.  <br>  
                 <br> License requirements : des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") */
                public: void SetSceneryBodyName
                (
                    const NXString & sceneryBodyName /** scenerybodyname */ 
                );
                /**Sets  the scenery body name 
                 <br>  Created in NX1953.0.0.  <br>  
                 <br> License requirements : des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") */
                void SetSceneryBodyName
                (
                    const char * sceneryBodyName /** scenerybodyname */ 
                );
                /**Returns  the selected body 
                 <br>  Created in NX1953.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::SelectBodyList * Bodies
                (
                );
                /**Returns  the assigned material 
                 <br>  Created in NX1953.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Material * Material
                (
                );
                /**Sets  the assigned material 
                 <br>  Created in NX1953.0.0.  <br>  
                 <br> License requirements : des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") */
                public: void SetMaterial
                (
                    NXOpen::Material * assignedMaterial /** assignedmaterial */ 
                );
            };
        }
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
