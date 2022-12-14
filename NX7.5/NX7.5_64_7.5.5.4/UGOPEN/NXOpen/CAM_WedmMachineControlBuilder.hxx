#ifndef NXOpen_CAM_WEDMMACHINECONTROLBUILDER_HXX_INCLUDED
#define NXOpen_CAM_WEDMMACHINECONTROLBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_WedmMachineControlBuilder.ja
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
#include <NXOpen/CAM_UdeSet.hxx>
#include <NXOpen/CAM_OperationBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAM
    {
        class WedmMachineControlBuilder;
    }
    namespace CAM
    {
        class OperationBuilder;
    }
    namespace CAM
    {
        class UdeSet;
    }
    namespace CAM
    {
        class _WedmMachineControlBuilderBuilder;
        class WedmMachineControlBuilderImpl;
        /** Represents a WedmMachineControl Builder  <br> To create a new instance of this class, use @link CAM::OperationCollection::CreateWedmMachineControlBuilder CAM::OperationCollection::CreateWedmMachineControlBuilder@endlink  <br> */
        class NXOPENCPPEXPORT  WedmMachineControlBuilder : public CAM::OperationBuilder
        {
            private: WedmMachineControlBuilderImpl * m_wedmmachinecontrolbuilder_impl;
            private: friend class  _WedmMachineControlBuilderBuilder;
            protected: WedmMachineControlBuilder();
            public: ~WedmMachineControlBuilder();
            /**Returns  the ude set  <br> License requirements : None */
            public: NXOpen::CAM::UdeSet * UdeSet
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
