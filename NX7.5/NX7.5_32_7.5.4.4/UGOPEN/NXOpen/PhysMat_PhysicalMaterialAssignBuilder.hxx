#ifndef NXOpen_PHYSMAT_PHYSICALMATERIALASSIGNBUILDER_HXX_INCLUDED
#define NXOpen_PHYSMAT_PHYSICALMATERIALASSIGNBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     PhysMat_PhysicalMaterialAssignBuilder.ja
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
#include <NXOpen/Builder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace PhysMat
    {
        class PhysicalMaterialAssignBuilder;
    }
    class Builder;
    namespace PhysMat
    {
        class _PhysicalMaterialAssignBuilderBuilder;
        class PhysicalMaterialAssignBuilderImpl;
        /** Represents a Physical Material Assign Builder  <br> To create a new instance of this class, use @link PhysicalMaterialCollection::CreateMaterialAssignBuilder PhysicalMaterialCollection::CreateMaterialAssignBuilder@endlink  <br> */
        class NXOPENCPPEXPORT  PhysicalMaterialAssignBuilder : public Builder
        {
            private: PhysicalMaterialAssignBuilderImpl * m_physicalmaterialassignbuilder_impl;
            private: friend class  _PhysicalMaterialAssignBuilderBuilder;
            protected: PhysicalMaterialAssignBuilder();
            public: ~PhysicalMaterialAssignBuilder();
        };
    }
}
#undef EXPORTLIBRARY
#endif
