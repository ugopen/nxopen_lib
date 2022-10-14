#ifndef NXOpen_CAM_VALUECOMPARATOR_HXX_INCLUDED
#define NXOpen_CAM_VALUECOMPARATOR_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_ValueComparator.ja
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
#include <NXOpen/libnxopencpp_cam_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace CAM
    {
        class ValueComparator;
    }
    class Builder;
    namespace CAM
    {
        class _ValueComparatorBuilder;
        class ValueComparatorImpl;

        /// \cond NX_NO_DOC 
        /** This class is used for set the facet tolerance.
                A call to @link Builder::Commit Builder::Commit@endlink  on this builder will only return NULL.
             <br> Use the @link Part Part@endlink  class to create a object.  <br> 
         <br>  Created in NX1899.0.0.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  ValueComparator : public NXOpen::Builder
        {
            private: ValueComparatorImpl * m_valuecomparator_impl;
            private: friend class  _ValueComparatorBuilder;
            protected: ValueComparator();
            public: ~ValueComparator();
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