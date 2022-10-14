#ifndef NXOpen_ANNOTATIONS_BASEPRODUCTGRID_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_BASEPRODUCTGRID_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_BaseProductGrid.ja
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
#include <NXOpen/Annotations_Annotation.hxx>
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
        class BaseProductGrid;
    }
    namespace Annotations
    {
        class Annotation;
    }
    namespace Annotations
    {
        class _BaseProductGridBuilder;
        class BaseProductGridImpl;

        /// \cond NX_NO_DOC 
        /** Represents the base product grid class  <br> This is an abstract class and cannot be directly instantiated  <br> 
         <br>  Created in NX1980.0.0.  <br>  
        */
        class NXOPENCPP_ANNOTATIONSEXPORT  BaseProductGrid : public NXOpen::Annotations::Annotation
        {
            private: BaseProductGridImpl * m_baseproductgrid_impl;
            private: friend class  _BaseProductGridBuilder;
            protected: BaseProductGrid();
            public: ~BaseProductGrid();
        };

        /// \endcond 
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