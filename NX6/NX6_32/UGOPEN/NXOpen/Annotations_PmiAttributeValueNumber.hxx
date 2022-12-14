#ifndef NXOpen_ANNOTATIONS_PMIATTRIBUTEVALUENUMBER_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_PMIATTRIBUTEVALUENUMBER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_PmiAttributeValueNumber.ja
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
#include <NXOpen/Annotations_PmiAttributeValue.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Annotations
    {
        class PmiAttributeValueNumber;
    }
    namespace Annotations
    {
        class PmiAttributeValue;
    }
    namespace Annotations
    {
        class _PmiAttributeValueNumberBuilder;
        /** Represents a PMI Attribute Number Value */
        class NXOPENCPPEXPORT PmiAttributeValueNumber : public Annotations::PmiAttributeValue
        {
            private: friend class  _PmiAttributeValueNumberBuilder;
            protected: PmiAttributeValueNumber();
        };
    }
}
#undef EXPORTLIBRARY
#endif
