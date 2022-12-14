#ifndef NXOpen_SKETCHDEFINEWORKREGIONBUILDER_HXX_INCLUDED
#define NXOpen_SKETCHDEFINEWORKREGIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     SketchDefineWorkRegionBuilder.ja
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
#include <NXOpen/ScCollector.hxx>
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
    class SketchDefineWorkRegionBuilder;
    class Builder;
    class ScCollector;
    class _SketchDefineWorkRegionBuilderBuilder;
    class SketchDefineWorkRegionBuilderImpl;
    /** 
    Represents a @link NXOpen::SketchDefineWorkRegionBuilder NXOpen::SketchDefineWorkRegionBuilder@endlink  builder.
     <br> To create a new instance of this class, use @link NXOpen::SketchCollection::CreateDefineWorkRegionBuilder  NXOpen::SketchCollection::CreateDefineWorkRegionBuilder @endlink  <br> 
     <br>  Created in NX1847.0.0.  <br>  
    */
    class NXOPENCPPEXPORT  SketchDefineWorkRegionBuilder : public NXOpen::Builder
    {
        /** Represents the options to specify the work region. */
        public: enum ScopeType
        {
            ScopeTypeSelectedObjects/** Only the selected objects can be modified. */,
            ScopeTypeEntireSketch/** All objects in the active sketch can be modified. */
        };

        private: SketchDefineWorkRegionBuilderImpl * m_sketchdefineworkregionbuilder_impl;
        private: friend class  _SketchDefineWorkRegionBuilderBuilder;
        protected: SketchDefineWorkRegionBuilder();
        public: ~SketchDefineWorkRegionBuilder();
        /**Returns  the scope of work region. When it is EntireSketch, all object in the active sketch can be modified; 
            when it is SelectedObjects, only the selected objects can be modified. 
         <br>  Created in NX1847.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::SketchDefineWorkRegionBuilder::ScopeType Scope
        (
        );
        /**Sets  the scope of work region. When it is EntireSketch, all object in the active sketch can be modified; 
            when it is SelectedObjects, only the selected objects can be modified. 
         <br>  Created in NX1847.0.0.  <br>  
         <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: void SetScope
        (
            NXOpen::SketchDefineWorkRegionBuilder::ScopeType scope /** scope */ 
        );
        /**Returns  the work region objects. The work region defines the curves can be modified. The curves outside the region are 
                frozen in the solver. User can only get the work region objects when the Scope is set to SelectedObjects 
         <br>  Created in NX1847.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::ScCollector * WorkRegionObjects
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
