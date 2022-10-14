#ifndef NXOpen_CAM_VARIABLEZLEVELMILLING_HXX_INCLUDED
#define NXOpen_CAM_VARIABLEZLEVELMILLING_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_VariableZLevelMilling.ja
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
#include <NXOpen/CAM_PlanarOperation.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAM
    {
        class VariableZLevelMilling;
    }
    namespace CAM
    {
        class PlanarOperation;
    }
    namespace CAM
    {
        class _VariableZLevelMillingBuilder;
        class VariableZLevelMillingImpl;
        /** Represents a Variable Z Level Milling Operation */
        class NXOPENCPPEXPORT  VariableZLevelMilling : public CAM::PlanarOperation
        {
            private: VariableZLevelMillingImpl * m_variablezlevelmilling_impl;
            private: friend class  _VariableZLevelMillingBuilder;
            protected: VariableZLevelMilling();
            public: ~VariableZLevelMilling();
        };
    }
}
#undef EXPORTLIBRARY
#endif