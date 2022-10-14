#ifndef NXOpen_ANNOTATIONS_PARTIDENTIFICATION_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_PARTIDENTIFICATION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_PartIdentification.ja
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
        class PartIdentification;
    }
    namespace Annotations
    {
        class PmiAttribute;
    }
    namespace Annotations
    {
        class _PartIdentificationBuilder;
        /** Represents a Part Identification */
        class NXOPENCPPEXPORT PartIdentification : public Annotations::PmiAttribute
        {
            private: friend class  _PartIdentificationBuilder;
            protected: PartIdentification();
        };
    }
}
#undef EXPORTLIBRARY
#endif