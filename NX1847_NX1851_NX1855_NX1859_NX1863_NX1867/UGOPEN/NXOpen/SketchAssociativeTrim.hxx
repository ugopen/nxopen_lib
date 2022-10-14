#ifndef NXOpen_SKETCHASSOCIATIVETRIM_HXX_INCLUDED
#define NXOpen_SKETCHASSOCIATIVETRIM_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     SketchAssociativeTrim.ja
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
    class SketchAssociativeTrim;
    class SketchGeometricConstraint;
    class _SketchAssociativeTrimBuilder;
    class SketchAssociativeTrimImpl;
    /** Represents a sketch associative trim constraint  <br> Use @link SketchCollection::CreateSketchAssociativeTrimBuilder SketchCollection::CreateSketchAssociativeTrimBuilder@endlink  to create an instance of this class.  <br> 
     <br>  Created in NX6.0.0.  <br>  
    */
    class NXOPENCPPEXPORT  SketchAssociativeTrim : public NXOpen::SketchGeometricConstraint
    {
        private: SketchAssociativeTrimImpl * m_sketchassociativetrim_impl;
        private: friend class  _SketchAssociativeTrimBuilder;
        protected: SketchAssociativeTrim();
        public: ~SketchAssociativeTrim();
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