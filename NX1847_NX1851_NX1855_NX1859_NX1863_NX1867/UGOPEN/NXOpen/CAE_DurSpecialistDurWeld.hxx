#ifndef NXOpen_CAE_DURSPECIALISTDURWELD_HXX_INCLUDED
#define NXOpen_CAE_DURSPECIALISTDURWELD_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_DurSpecialistDurWeld.ja
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
#include <NXOpen/NXObject.hxx>
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
        class DurSpecialistDurWeld;
    }
    class NXObject;
    namespace CAE
    {
        class _DurSpecialistDurWeldBuilder;
        class DurSpecialistDurWeldImpl;

        /// \cond NX_NO_DOC 
        /** Represents a @link NXOpen::CAE::DurSpecialistDurWeld NXOpen::CAE::DurSpecialistDurWeld@endlink . 
         <br>  Created in NX1847.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  DurSpecialistDurWeld : public NXOpen::NXObject
        {
            private: DurSpecialistDurWeldImpl * m_durspecialistdurweld_impl;
            private: friend class  _DurSpecialistDurWeldBuilder;
            protected: DurSpecialistDurWeld();
            public: ~DurSpecialistDurWeld();
            /**Returns  the activity status in this durability weld is returned 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: bool Active
            (
            );
            /**Sets  the activity status in this durability weld is returned 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: void SetActive
            (
                bool activity /** The Activity Status flag*/
            );
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
