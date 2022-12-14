#ifndef NXOpen_FEATURES_SELECTIONPROGRAMFARTHESTBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_SELECTIONPROGRAMFARTHESTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_SelectionProgramFarthestBuilder.ja
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
        class SelectionProgramFarthestBuilder;
    }
    class Builder;
    class SelectNXObject;
    namespace Features
    {
        class _SelectionProgramFarthestBuilderBuilder;
        class SelectionProgramFarthestBuilderImpl;
        /** Represents a @link NXOpen::Features::SelectionProgramFarthestBuilder NXOpen::Features::SelectionProgramFarthestBuilder@endlink   <br> To create a new instance of this class, use @link NXOpen::Features::SelectionProgramCollection::CreateSelectionProgramFarthestBuilder  NXOpen::Features::SelectionProgramCollection::CreateSelectionProgramFarthestBuilder @endlink  <br> 
         <br>  Created in NX1980.0.0.  <br>  
        */
        class NXOPENCPP_FEATURESEXPORT  SelectionProgramFarthestBuilder : public NXOpen::Builder
        {
            private: SelectionProgramFarthestBuilderImpl * m_selectionprogramfarthestbuilder_impl;
            private: friend class  _SelectionProgramFarthestBuilderBuilder;
            protected: SelectionProgramFarthestBuilder();
            public: ~SelectionProgramFarthestBuilder();
            /**Returns  the proximity object
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectNXObject * ProximityObject
            (
            );
        };
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
