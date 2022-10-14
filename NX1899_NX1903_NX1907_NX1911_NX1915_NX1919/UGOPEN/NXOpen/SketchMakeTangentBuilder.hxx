#ifndef NXOpen_SKETCHMAKETANGENTBUILDER_HXX_INCLUDED
#define NXOpen_SKETCHMAKETANGENTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     SketchMakeTangentBuilder.ja
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
#include <NXOpen/SketchMakeRelationBuilder.hxx>
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
    class SketchMakeTangentBuilder;
    class SketchMakeRelationBuilder;
    class _SketchMakeTangentBuilderBuilder;
    class SketchMakeTangentBuilderImpl;
    /**
        Represents a @link NXOpen::SketchMakeTangentBuilder NXOpen::SketchMakeTangentBuilder@endlink  builder. 
         <br> To create a new instance of this class, use @link NXOpen::SketchCollection::CreateSketchMakeTangentBuilder  NXOpen::SketchCollection::CreateSketchMakeTangentBuilder @endlink  <br> 
     <br>  Created in NX1847.0.0.  <br>  
    */
    class NXOPENCPPEXPORT  SketchMakeTangentBuilder : public NXOpen::SketchMakeRelationBuilder
    {
        private: SketchMakeTangentBuilderImpl * m_sketchmaketangentbuilder_impl;
        private: friend class  _SketchMakeTangentBuilderBuilder;
        protected: SketchMakeTangentBuilder();
        public: ~SketchMakeTangentBuilder();
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