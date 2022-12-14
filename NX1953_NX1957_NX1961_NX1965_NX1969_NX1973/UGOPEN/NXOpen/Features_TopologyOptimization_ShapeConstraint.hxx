#ifndef NXOpen_FEATURES_TOPOLOGYOPTIMIZATION_SHAPECONSTRAINT_HXX_INCLUDED
#define NXOpen_FEATURES_TOPOLOGYOPTIMIZATION_SHAPECONSTRAINT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_TopologyOptimization_ShapeConstraint.ja
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
            class ShapeConstraint;
        }
    }
    class NXObject;
    namespace Features
    {
        namespace TopologyOptimization
        {
            class _ShapeConstraintBuilder;
            class ShapeConstraintImpl;
            /** Represents a @link Features::TopologyOptimization::ShapeConstraint Features::TopologyOptimization::ShapeConstraint@endlink  for a @link Features::TopologyOptimization::DesignSpace Features::TopologyOptimization::DesignSpace@endlink  of @link Features::TopologyOptimizationFeature Features::TopologyOptimizationFeature@endlink .  <br> To create or edit an instance of this class, use @link NXOpen::Features::TopologyOptimization::ShapeConstraintBuilder  NXOpen::Features::TopologyOptimization::ShapeConstraintBuilder @endlink  <br> 
             <br>  Created in NX1953.0.0.  <br>  
            */
            class NXOPENCPP_FEATURESEXPORT  ShapeConstraint : public NXOpen::NXObject
            {
                private: ShapeConstraintImpl * m_shapeconstraint_impl;
                private: friend class  _ShapeConstraintBuilder;
                protected: ShapeConstraint();
                public: ~ShapeConstraint();
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
