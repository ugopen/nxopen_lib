#ifndef NXOpen_CAE_MODELINGOBJECTPROPERTYTABLE_HXX_INCLUDED
#define NXOpen_CAE_MODELINGOBJECTPROPERTYTABLE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_ModelingObjectPropertyTable.ja
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
#include <NXOpen/CAE_NamedPropertyTable.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAE
    {
        class ModelingObjectPropertyTable;
    }
    namespace CAE
    {
        class NamedPropertyTable;
    }
    namespace CAE
    {
        class _ModelingObjectPropertyTableBuilder;
        class ModelingObjectPropertyTableImpl;
        /**  @brief  Represents a Modeling Object Property Table  

          */
        class NXOPENCPPEXPORT  ModelingObjectPropertyTable : public CAE::NamedPropertyTable
        {
            private: ModelingObjectPropertyTableImpl * m_modelingobjectpropertytable_impl;
            private: friend class  _ModelingObjectPropertyTableBuilder;
            protected: ModelingObjectPropertyTable();
            public: ~ModelingObjectPropertyTable();
        };
    }
}
#undef EXPORTLIBRARY
#endif