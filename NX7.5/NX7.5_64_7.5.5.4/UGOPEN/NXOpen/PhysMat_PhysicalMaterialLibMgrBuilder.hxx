#ifndef NXOpen_PHYSMAT_PHYSICALMATERIALLIBMGRBUILDER_HXX_INCLUDED
#define NXOpen_PHYSMAT_PHYSICALMATERIALLIBMGRBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     PhysMat_PhysicalMaterialLibMgrBuilder.ja
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
        class PhysicalMaterialLibMgrBuilder;
    }
    class Builder;
    namespace PhysMat
    {
        class _PhysicalMaterialLibMgrBuilderBuilder;
        class PhysicalMaterialLibMgrBuilderImpl;
        /** Represents a @link PhysMat::PhysicalMaterialLibMgrBuilder PhysMat::PhysicalMaterialLibMgrBuilder@endlink  builder  <br> To create a new instance of this class, use @link PhysicalMaterialCollection::CreateMaterialLibmgrBuilder PhysicalMaterialCollection::CreateMaterialLibmgrBuilder@endlink  <br> */
        class NXOPENCPPEXPORT  PhysicalMaterialLibMgrBuilder : public Builder
        {
            private: PhysicalMaterialLibMgrBuilderImpl * m_physicalmateriallibmgrbuilder_impl;
            private: friend class  _PhysicalMaterialLibMgrBuilderBuilder;
            protected: PhysicalMaterialLibMgrBuilder();
            public: ~PhysicalMaterialLibMgrBuilder();
        };
    }
}
#undef EXPORTLIBRARY
#endif
