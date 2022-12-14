#ifndef NXOpen_ANNOTATIONS_PMIVEHICLEGRID_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_PMIVEHICLEGRID_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_PmiVehicleGrid.ja
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
#include <NXOpen/Annotations_BaseVehicleGrid.hxx>
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
        class PmiVehicleGrid;
    }
    namespace Annotations
    {
        class BaseVehicleGrid;
    }
    namespace Annotations
    {
        class _PmiVehicleGridBuilder;
        class PmiVehicleGridImpl;

        /// \cond NX_NO_DOC 
        /** Represents a pmi vehicle grid  <br> To create or edit an instance of this class, use @link NXOpen::Annotations::PmiVehicleGridBuilder  NXOpen::Annotations::PmiVehicleGridBuilder @endlink  <br> 
         <br>  Created in NX1980.0.0.  <br>  
        */
        class NXOPENCPP_ANNOTATIONSEXPORT  PmiVehicleGrid : public NXOpen::Annotations::BaseVehicleGrid
        {
            private: PmiVehicleGridImpl * m_pmivehiclegrid_impl;
            private: friend class  _PmiVehicleGridBuilder;
            protected: PmiVehicleGrid();
            public: ~PmiVehicleGrid();
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
