#ifndef NXOpen_CUTVIEW_HXX_INCLUDED
#define NXOpen_CUTVIEW_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CutView.ja
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
#include <NXOpen/ModelingView.hxx>
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
    class CutView;
    class DisplayableObject;
    class ModelingView;
    class _CutViewBuilder;
    class CutViewImpl;
    /**
     Represents a Cut View
     <br> Cut Views may only be created via a Master Cut Builder.  <br> 
     <br>  Created in NX4.0.0.  <br>  
    */
    class NXOPENCPPEXPORT  CutView : public NXOpen::ModelingView
    {
        private: CutViewImpl * m_cutview_impl;
        private: friend class  _CutViewBuilder;
        protected: CutView();
        public: ~CutView();
        /**Returns  a "true" if the view is a sectioned (persistent) model view 
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: bool IsModelingTypeCut
        (
        );
        /**Returns  a "true" if the cut view is out of date 
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: bool IsCutViewOutOfDate
        (
        );
        /** Find the cut bodies in a cut view.  @return  
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: std::vector<NXOpen::DisplayableObject *> GetCutBodies
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