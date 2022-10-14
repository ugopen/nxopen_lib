#ifndef NXOpen_CAE_RESPONSESIMULATION_ROTATIONALNODALFUNCTIONEXCITATION_HXX_INCLUDED
#define NXOpen_CAE_RESPONSESIMULATION_ROTATIONALNODALFUNCTIONEXCITATION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_ResponseSimulation_RotationalNodalFunctionExcitation.ja
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
#include <NXOpen/CAE_ResponseSimulation_NodalFunctionExcitation.hxx>
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
        namespace ResponseSimulation
        {
            class RotationalNodalFunctionExcitation;
        }
    }
    namespace CAE
    {
        namespace ResponseSimulation
        {
            class NodalFunctionExcitation;
        }
    }
    namespace CAE
    {
        namespace ResponseSimulation
        {
            class _RotationalNodalFunctionExcitationBuilder;
            class RotationalNodalFunctionExcitationImpl;
            /** Represents a rotational nodal function excitation  <br> To create or edit an instance of this class, use @link NXOpen::CAE::ResponseSimulation::RotationalNodalFunctionExcitationBuilder  NXOpen::CAE::ResponseSimulation::RotationalNodalFunctionExcitationBuilder @endlink  <br> 
             <br>  Created in NX5.0.0.  <br>  
            */
            class NXOPENCPP_CAEEXPORT  RotationalNodalFunctionExcitation : public NXOpen::CAE::ResponseSimulation::NodalFunctionExcitation
            {
                private: RotationalNodalFunctionExcitationImpl * m_rotationalnodalfunctionexcitation_impl;
                private: friend class  _RotationalNodalFunctionExcitationBuilder;
                protected: RotationalNodalFunctionExcitation();
                public: ~RotationalNodalFunctionExcitation();
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