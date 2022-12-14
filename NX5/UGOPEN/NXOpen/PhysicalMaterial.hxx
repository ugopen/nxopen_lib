#ifndef NXOpen_PHYSICALMATERIAL_HXX_INCLUDED
#define NXOpen_PHYSICALMATERIAL_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     PhysicalMaterial.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/Material.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    class PhysicalMaterial;
    class Material;
    class _PhysicalMaterialBuilder;
    /** Represents Physical Material */
    class NXOPENCPPEXPORT PhysicalMaterial : public Material
    {
        private: friend class  _PhysicalMaterialBuilder;
        protected: PhysicalMaterial();
    };
}
#undef EXPORTLIBRARY
#endif
