#ifndef NXOpen_ANNOTATIONS_PMICHAMFERDIMENSIONBUILDER_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_PMICHAMFERDIMENSIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_PmiChamferDimensionBuilder.ja
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
#include <NXOpen/Annotations_PmiChamferDimensionBuilder.hxx>
#include <NXOpen/Annotations_BaseChamferDimensionBuilder.hxx>
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
        class PmiChamferDimensionBuilder;
    }
    namespace Annotations
    {
        class AssociatedObjectsBuilder;
    }
    namespace Annotations
    {
        class BaseChamferDimensionBuilder;
    }
    namespace Annotations
    {
        class _PmiChamferDimensionBuilderBuilder;
        class PmiChamferDimensionBuilderImpl;
        /** Represents a @link NXOpen::Annotations::PmiChamferDimension NXOpen::Annotations::PmiChamferDimension@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::Annotations::DimensionCollection::CreatePmiChamferDimensionBuilder  NXOpen::Annotations::DimensionCollection::CreatePmiChamferDimensionBuilder @endlink  <br> 
         <br>  Created in NX9.0.0.  <br>  
        */
        class NXOPENCPP_ANNOTATIONSEXPORT  PmiChamferDimensionBuilder : public NXOpen::Annotations::BaseChamferDimensionBuilder
        {
            private: PmiChamferDimensionBuilderImpl * m_pmichamferdimensionbuilder_impl;
            private: friend class  _PmiChamferDimensionBuilderBuilder;
            protected: PmiChamferDimensionBuilder();
            public: ~PmiChamferDimensionBuilder();
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
