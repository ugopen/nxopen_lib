#ifndef NXOpen_ANNOTATIONS_MATERIALSPECIFICATION_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_MATERIALSPECIFICATION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_MaterialSpecification.ja
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
#include <NXOpen/Annotations_PmiAttribute.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Annotations
    {
        class MaterialSpecification;
    }
    namespace Annotations
    {
        class PmiAttribute;
    }
    namespace Annotations
    {
        class _MaterialSpecificationBuilder;
        /** Represents a Material Specification */
        class NXOPENCPPEXPORT MaterialSpecification : public Annotations::PmiAttribute
        {
            private: friend class  _MaterialSpecificationBuilder;
            protected: MaterialSpecification();
        };
    }
}
#undef EXPORTLIBRARY
#endif
