#ifndef NXOpen_SKETCHMANAGESYMMETRYLINESBUILDER_HXX_INCLUDED
#define NXOpen_SKETCHMANAGESYMMETRYLINESBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     SketchManageSymmetryLinesBuilder.ja
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
#include <NXOpen/SelectObject.hxx>
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
    class SketchManageSymmetryLinesBuilder;
    class Builder;
    class NXObject;
    class SelectNXObject;
    class _SketchManageSymmetryLinesBuilderBuilder;
    class SketchManageSymmetryLinesBuilderImpl;
    /**
        Represents a @link NXOpen::SketchManageSymmetryLinesBuilder NXOpen::SketchManageSymmetryLinesBuilder@endlink 
         <br> To create a new instance of this class, use @link NXOpen::SketchCollection::CreateSketchManageSymmetryLinesBuilder  NXOpen::SketchCollection::CreateSketchManageSymmetryLinesBuilder @endlink  <br> 
     <br>  Created in NX1847.0.0.  <br>  
    */
    class NXOPENCPPEXPORT  SketchManageSymmetryLinesBuilder : public NXOpen::Builder
    {
        private: SketchManageSymmetryLinesBuilderImpl * m_sketchmanagesymmetrylinesbuilder_impl;
        private: friend class  _SketchManageSymmetryLinesBuilderBuilder;
        protected: SketchManageSymmetryLinesBuilder();
        public: ~SketchManageSymmetryLinesBuilder();
        /**Returns  the object selected to be defined as a symmetry line 
         <br>  Created in NX1847.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::SelectNXObject * ObjectSelected
        (
        );
        /** Change symmetry line status between active and inactive 
         <br>  Created in NX1847.0.0.  <br>  
         <br> License requirements : solid_modeling ("SOLIDS MODELING") OR drafting ("DRAFTING") OR geometric_tol ("GDT") */
        public: void ChangeSymmetryLineStatus
        (
            NXOpen::NXObject * symmetryLine /** symmetryline */ ,
            bool isActivated /** isactivated */ 
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
