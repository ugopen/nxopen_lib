#ifndef NXOpen_CAE_RESPONSESIMULATION_STRAINGAGE_HXX_INCLUDED
#define NXOpen_CAE_RESPONSESIMULATION_STRAINGAGE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_ResponseSimulation_StrainGage.ja
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
#include <NXOpen/CAE_ResponseSimulation_RSDisplayObject.hxx>
#include <NXOpen/DisplayableObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAE
    {
        namespace ResponseSimulation
        {
            class StrainGage;
        }
    }
    namespace CAE
    {
        namespace ResponseSimulation
        {
            class RSDisplayObject;
        }
    }
    class DisplayableObject;
    namespace CAE
    {
        namespace ResponseSimulation
        {
            class _StrainGageBuilder;
            class StrainGageImpl;
            /** Represents a @link CAE::ResponseSimulation::StrainGage CAE::ResponseSimulation::StrainGage@endlink 
                    */
            class NXOPENCPPEXPORT  StrainGage : public DisplayableObject
            {
                private: StrainGageImpl * m_straingage_impl;
                private: friend class  _StrainGageBuilder;
                protected: StrainGage();
                public: ~StrainGage();
                /** Get display attribute of gage  @return    <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: NXOpen::CAE::ResponseSimulation::RSDisplayObject * GetDisplayAttribute
                (
                );
            };
        }
    }
}
#undef EXPORTLIBRARY
#endif