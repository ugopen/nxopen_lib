#ifndef NXOpen_ANNOTATIONS_VEHICLEGRID_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_VEHICLEGRID_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_VehicleGrid.ja
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
        class VehicleGrid;
    }
    namespace Annotations
    {
        class BaseVehicleGrid;
    }
    namespace Annotations
    {
        class _VehicleGridBuilder;
        class VehicleGridImpl;

        /// \cond NX_NO_DOC 
        /** Represents a vehicle grid  <br> To create or edit an instance of this class, use @link NXOpen::Annotations::VehicleGridBuilder  NXOpen::Annotations::VehicleGridBuilder @endlink  <br> 
         <br>  Created in NX1980.0.0.  <br>  
        */
        class NXOPENCPP_ANNOTATIONSEXPORT  VehicleGrid : public NXOpen::Annotations::BaseVehicleGrid
        {
            private: VehicleGridImpl * m_vehiclegrid_impl;
            private: friend class  _VehicleGridBuilder;
            protected: VehicleGrid();
            public: ~VehicleGrid();
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