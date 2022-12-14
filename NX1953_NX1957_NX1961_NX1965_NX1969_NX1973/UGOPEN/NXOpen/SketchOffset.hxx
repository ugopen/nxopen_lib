#ifndef NXOpen_SKETCHOFFSET_HXX_INCLUDED
#define NXOpen_SKETCHOFFSET_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     SketchOffset.ja
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
#include <NXOpen/SketchGeometricConstraint.hxx>
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
    class SketchOffset;
    class SketchGeometricConstraint;
    class _SketchOffsetBuilder;
    class SketchOffsetImpl;
    /** Represents a sketch offset constraint  <br> Use @link SketchCollection::CreateSketchOffsetBuilder SketchCollection::CreateSketchOffsetBuilder@endlink  to create an instance of this class.  <br> 
     <br>  Created in NX5.0.0.  <br>  
    */
    class NXOPENCPPEXPORT  SketchOffset : public NXOpen::SketchGeometricConstraint
    {
        /** Represents the cap type of the offset */
        public: enum CapType
        {
            CapTypeExtension/** The cap type is curve extension */,
            CapTypeArc/** The cap type is arc cap         */
        };

        private: SketchOffsetImpl * m_sketchoffset_impl;
        private: friend class  _SketchOffsetBuilder;
        protected: SketchOffset();
        public: ~SketchOffset();
        /** Updates the distance data of the constraint after its geometries are edited. Only vaild for offset without dimension. This function
                does not trigger an update. Whenever the parameters of an input geometry of a constraint is edited, this function should be called
                on all the offset constraints referencing that object so that the offset distance will update to new input value. 
         <br>  Created in NX10.0.0.  <br>  
         <br> License requirements : solid_modeling ("SOLIDS MODELING") OR drafting ("DRAFTING") */
        public: void UpdateDistance
        (
            double dist /** dist */ 
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
