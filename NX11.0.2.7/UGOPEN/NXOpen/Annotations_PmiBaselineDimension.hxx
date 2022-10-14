#ifndef NXOpen_ANNOTATIONS_PMIBASELINEDIMENSION_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_PMIBASELINEDIMENSION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_PmiBaselineDimension.ja
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
#include <NXOpen/Annotations_BaselineDimension.hxx>
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
        class PmiBaselineDimension;
    }
    namespace Annotations
    {
        class BaselineDimension;
    }
    namespace Annotations
    {
        class _PmiBaselineDimensionBuilder;
        class PmiBaselineDimensionImpl;
        /** Represents a PMI baseline dimension. It is a set of horizontal or vertical
                dimensions.  <br> There is no KF creator for this class.  <br> 
         <br>  Created in NX4.0.0.  <br>  
        */
        class NXOPENCPP_ANNOTATIONSEXPORT  PmiBaselineDimension : public NXOpen::Annotations::BaselineDimension
        {
            private: PmiBaselineDimensionImpl * m_pmibaselinedimension_impl;
            private: friend class  _PmiBaselineDimensionBuilder;
            protected: PmiBaselineDimension();
            public: ~PmiBaselineDimension();
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