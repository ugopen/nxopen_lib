#ifndef NXOpen_SKETCHTANGENTTOSTRINGCONSTRAINT_HXX_INCLUDED
#define NXOpen_SKETCHTANGENTTOSTRINGCONSTRAINT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     SketchTangentToStringConstraint.ja
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
#include <NXOpen/SketchHelpedGeometricConstraint.hxx>
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
    class SketchTangentToStringConstraint;
    class SketchHelpedGeometricConstraint;
    class _SketchTangentToStringConstraintBuilder;
    class SketchTangentToStringConstraintImpl;
    /** Represents a sketch tangent to string constraint  <br> Use @link SketchCollection::CreateConstraintBuilder SketchCollection::CreateConstraintBuilder@endlink  to create an instance of this class.  <br> 
     <br>  Created in NX11.0.0.  <br>  
    */
    class NXOPENCPPEXPORT  SketchTangentToStringConstraint : public NXOpen::SketchHelpedGeometricConstraint
    {
        private: SketchTangentToStringConstraintImpl * m_sketchtangenttostringconstraint_impl;
        private: friend class  _SketchTangentToStringConstraintBuilder;
        protected: SketchTangentToStringConstraint();
        public: ~SketchTangentToStringConstraint();
        /** Switches the constraint to an alternate solution 
         <br>  Created in NX11.0.0.  <br>  
         <br> License requirements : solid_modeling ("SOLIDS MODELING") OR drafting ("DRAFTING") */
        public: void UseAlternateSolution
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
