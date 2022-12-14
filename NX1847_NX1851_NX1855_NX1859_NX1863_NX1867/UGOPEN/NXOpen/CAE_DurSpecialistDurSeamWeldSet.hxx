#ifndef NXOpen_CAE_DURSPECIALISTDURSEAMWELDSET_HXX_INCLUDED
#define NXOpen_CAE_DURSPECIALISTDURSEAMWELDSET_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_DurSpecialistDurSeamWeldSet.ja
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
#include <NXOpen/CAE_DurSpecialistDurWeldSet.hxx>
#include <NXOpen/libnxopencpp_cae_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace CAE
    {
        class DurSpecialistDurSeamWeldSet;
    }
    namespace CAE
    {
        class DurSpecialistDurWeldSet;
    }
    namespace CAE
    {
        class _DurSpecialistDurSeamWeldSetBuilder;
        class DurSpecialistDurSeamWeldSetImpl;

        /// \cond NX_NO_DOC 
        /** Represents a @link NXOpen::CAE::DurSpecialistDurSeamWeldSet NXOpen::CAE::DurSpecialistDurSeamWeldSet@endlink . 
         <br>  Created in NX1847.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  DurSpecialistDurSeamWeldSet : public NXOpen::CAE::DurSpecialistDurWeldSet
        {
            private: DurSpecialistDurSeamWeldSetImpl * m_durspecialistdurseamweldset_impl;
            private: friend class  _DurSpecialistDurSeamWeldSetBuilder;
            protected: DurSpecialistDurSeamWeldSet();
            public: ~DurSpecialistDurSeamWeldSet();
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
