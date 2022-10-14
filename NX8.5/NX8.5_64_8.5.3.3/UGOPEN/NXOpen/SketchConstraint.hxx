#ifndef NXOpen_SKETCHCONSTRAINT_HXX_INCLUDED
#define NXOpen_SKETCHCONSTRAINT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     SketchConstraint.ja
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
#include <NXOpen/DisplayableObject.hxx>
#include <NXOpen/Sketch.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    class SketchConstraint;
    class DisplayableObject;
    class _SketchConstraintBuilder;
    class SketchConstraintImpl;
    /** Represents a constraint in a sketch.  There are two classes of constraints:
    geometric and dimensional  <br> This is an abstract class.  <br> 
     <br>  Created in NX3.0.0.  <br>  
    */
    class NXOPENCPPEXPORT  SketchConstraint : public DisplayableObject
    {
        private: SketchConstraintImpl * m_sketchconstraint_impl;
        private: friend class  _SketchConstraintBuilder;
        protected: SketchConstraint();
        public: ~SketchConstraint();
        /**Returns  the constraint's type 
         <br>  Created in NX3.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::Sketch::ConstraintType ConstraintType
        (
        );
        /** Refreshes the display of a sketch dimension 
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : solid_modeling ("SOLIDS MODELING") OR drafting ("DRAFTING") */
        public: void RefreshDimension
        (
        );
    };
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