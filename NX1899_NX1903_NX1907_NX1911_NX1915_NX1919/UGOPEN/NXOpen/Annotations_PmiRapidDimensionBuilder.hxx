#ifndef NXOpen_ANNOTATIONS_PMIRAPIDDIMENSIONBUILDER_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_PMIRAPIDDIMENSIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_PmiRapidDimensionBuilder.ja
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
#include <NXOpen/Annotations_AssociatedObjectsBuilder.hxx>
#include <NXOpen/Annotations_BaseRapidDimensionBuilder.hxx>
#include <NXOpen/libnxopencpp_annotations_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Annotations
    {
        class PmiRapidDimensionBuilder;
    }
    namespace Annotations
    {
        class AssociatedObjectsBuilder;
    }
    namespace Annotations
    {
        class BaseRapidDimensionBuilder;
    }
    namespace Annotations
    {
        class _PmiRapidDimensionBuilderBuilder;
        class PmiRapidDimensionBuilderImpl;
        /** Represents a @link NXOpen::Annotations::Dimension NXOpen::Annotations::Dimension@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::Annotations::DimensionCollection::CreatePmiRapidDimensionBuilder  NXOpen::Annotations::DimensionCollection::CreatePmiRapidDimensionBuilder @endlink  <br> 
         <br>  Created in NX9.0.0.  <br>  
        */
        class NXOPENCPP_ANNOTATIONSEXPORT  PmiRapidDimensionBuilder : public NXOpen::Annotations::BaseRapidDimensionBuilder
        {
            private: PmiRapidDimensionBuilderImpl * m_pmirapiddimensionbuilder_impl;
            private: friend class  _PmiRapidDimensionBuilderBuilder;
            protected: PmiRapidDimensionBuilder();
            public: ~PmiRapidDimensionBuilder();
            /**Returns  the associated objects 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::AssociatedObjectsBuilder * AssociatedObjects
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