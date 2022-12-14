#ifndef NXOpen_SKETCHDIMENSIONALCONSTRAINT_HXX_INCLUDED
#define NXOpen_SKETCHDIMENSIONALCONSTRAINT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     SketchDimensionalConstraint.ja
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
#include <NXOpen/Sketch.hxx>
#include <NXOpen/SketchConstraint.hxx>
#include <NXOpen/ugmath.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    class SketchDimensionalConstraint;
    namespace Annotations
    {
        class Dimension;
    }
    class Expression;
    class NXObject;
    class SketchConstraint;
    class _SketchDimensionalConstraintBuilder;
    class SketchDimensionalConstraintImpl;
    /** Represents a dimensional constraint  <br> To create an instance of this class refer to @link Sketch Sketch@endlink  <br> */
    class NXOPENCPPEXPORT  SketchDimensionalConstraint : public SketchConstraint
    {
        /** Dimension status. */
        public: enum DimensionStateType
        {
            DimensionStateTypeDriving/** Driving dimension */,
            DimensionStateTypeReference/** Reference dimension   */,
            DimensionStateTypeAutomatic/** Automatic dimension */
        };

        private: SketchDimensionalConstraintImpl * m_sketchdimensionalconstraint_impl;
        private: friend class  _SketchDimensionalConstraintBuilder;
        protected: SketchDimensionalConstraint();
        public: ~SketchDimensionalConstraint();
        /** Returns the geometry associated with the dimension  @return  the geometry associated with the dimension  <br> License requirements : None */
        public: std::vector<NXOpen::Sketch::DimensionGeometry> GetDimensionGeometry
        (
        );
        /**Returns  the dimension associated with the dimensional constraint  <br> License requirements : None */
        public: NXOpen::Annotations::Dimension * AssociatedDimension
        (
        );
        /**Returns  the expression associated with the dimensional constraint  <br> License requirements : None */
        public: NXOpen::Expression * AssociatedExpression
        (
        );
        /** Switches the constraint to an alternate solution  <br> License requirements : solid_modeling ("SOLIDS MODELING") OR drafting ("DRAFTING") */
        public: void UseAlternateSolution
        (
        );
        /**Returns  the dimension status.  <br> License requirements : solid_modeling ("SOLIDS MODELING") OR drafting ("DRAFTING") */
        public: NXOpen::SketchDimensionalConstraint::DimensionStateType DimensionState
        (
        );
    };
}
#undef EXPORTLIBRARY
#endif
