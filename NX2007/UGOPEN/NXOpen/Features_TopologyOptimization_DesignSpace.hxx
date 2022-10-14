#ifndef NXOpen_FEATURES_TOPOLOGYOPTIMIZATION_DESIGNSPACE_HXX_INCLUDED
#define NXOpen_FEATURES_TOPOLOGYOPTIMIZATION_DESIGNSPACE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_TopologyOptimization_DesignSpace.ja
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
#include <NXOpen/Features_TopologyOptimization_ConstructionBody.hxx>
#include <NXOpen/Features_TopologyOptimization_ConstructionBodyCollector.hxx>
#include <NXOpen/NXObject.hxx>
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
            class DesignSpace;
        }
    }
    namespace Features
    {
        namespace TopologyOptimization
        {
            class ConstructionBody;
        }
    }
    namespace Features
    {
        namespace TopologyOptimization
        {
            class ConstructionBodyCollector;
        }
    }
    class NXObject;
    namespace Features
    {
        namespace TopologyOptimization
        {
            class _DesignSpaceBuilder;
            class DesignSpaceImpl;
            /** Represents a Topology Optimization Design Space data  <br> To create or edit an instance of this class, use @link NXOpen::Features::TopologyOptimization::DesignSpaceBuilder  NXOpen::Features::TopologyOptimization::DesignSpaceBuilder @endlink  <br> 
             <br>  Created in NX1953.0.0.  <br>  
            */
            class NXOPENCPP_FEATURESEXPORT  DesignSpace : public NXOpen::NXObject
            {
                private: DesignSpaceImpl * m_designspace_impl;
                private: friend class  _DesignSpaceBuilder;
                protected: DesignSpace();
                public: ~DesignSpace();
                /** Creates a @link Features::TopologyOptimization::ConstructionBodyCollector Features::TopologyOptimization::ConstructionBodyCollector@endlink  from @link Features::TopologyOptimization::ConstructionBody Features::TopologyOptimization::ConstructionBody@endlink  members. 
                 <br>  Created in NX1953.0.0.  <br>  
                 <br> License requirements : des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") */
                public: NXOpen::Features::TopologyOptimization::ConstructionBodyCollector * CreateConstructionBodyGroup
                (
                    const std::vector<NXOpen::Features::TopologyOptimization::ConstructionBody *> & constructionBodies /** constructionbodies */ 
                );
                /**Add a @link Features::TopologyOptimization::ShapeConstraint Features::TopologyOptimization::ShapeConstraint@endlink  or @link Features::TopologyOptimization::OptimizationConstraint Features::TopologyOptimization::OptimizationConstraint@endlink  to the @link Features::TopologyOptimization::DesignSpace Features::TopologyOptimization::DesignSpace@endlink .
                 <br>  Created in NX1980.0.0.  <br>  
                 <br> License requirements : des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") */
                public: void AddConstraint
                (
                    NXOpen::NXObject * constraintObjectTag /** constraintobjecttag */ 
                );
                /**Remove a @link Features::TopologyOptimization::ShapeConstraint Features::TopologyOptimization::ShapeConstraint@endlink  or @link Features::TopologyOptimization::OptimizationConstraint Features::TopologyOptimization::OptimizationConstraint@endlink   from the @link Features::TopologyOptimization::DesignSpace Features::TopologyOptimization::DesignSpace@endlink .
                 <br>  Created in NX1980.0.0.  <br>  
                 <br> License requirements : des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") */
                public: void RemoveConstraint
                (
                    NXOpen::NXObject * constraintObjectTag /** constraintobjecttag */ 
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