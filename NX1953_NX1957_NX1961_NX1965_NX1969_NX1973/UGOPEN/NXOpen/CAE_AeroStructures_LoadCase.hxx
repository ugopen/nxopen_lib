#ifndef NXOpen_CAE_AEROSTRUCTURES_LOADCASE_HXX_INCLUDED
#define NXOpen_CAE_AEROSTRUCTURES_LOADCASE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_AeroStructures_LoadCase.ja
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
#include <NXOpen/CAE_BaseLoadcase.hxx>
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
        namespace AeroStructures
        {
            class LoadCase;
        }
    }
    namespace CAE
    {
        class BaseLoadcase;
    }
    class NXObject;
    namespace CAE
    {
        namespace AeroStructures
        {
            class _LoadCaseBuilder;
            class LoadCaseImpl;
            /** Represents a @link NXOpen::CAE::AeroStructures::LoadCase NXOpen::CAE::AeroStructures::LoadCase@endlink . 
             <br>  Created in NX12.0.0.  <br>  
            */
            class NXOPENCPP_CAEEXPORT  LoadCase : public NXOpen::NXObject
            {
                /** the Loadcase type */
                public: enum LoadCaseType
                {
                    LoadCaseTypeUnitary/** Unitary loadcase */,
                    LoadCaseTypeCombined/** Combined loadcase */
                };

                private: LoadCaseImpl * m_loadcase_impl;
                private: friend class  _LoadCaseBuilder;
                protected: LoadCase();
                public: ~LoadCase();
                /**Returns  the strength requirement 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : nx_masterfem ("Finite Element Modeling") */
                public: NXString StrengthRequirement
                (
                );
                /**Returns  the associated CAE::BaseLoadCase 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : nx_masterfem ("Finite Element Modeling") */
                public: NXOpen::CAE::BaseLoadcase * BaseLoadCase
                (
                );
            };
        }
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
