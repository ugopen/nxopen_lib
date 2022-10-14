#ifndef NXOpen_ANNOTATIONS_PMIATTRIBUTEVALUEMULTIPLESTRING_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_PMIATTRIBUTEVALUEMULTIPLESTRING_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_PmiAttributeValueMultipleString.ja
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
#include <NXOpen/Annotations_PmiAttributeValue.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Annotations
    {
        class PmiAttributeValueMultipleString;
    }
    namespace Annotations
    {
        class PmiAttributeValue;
    }
    namespace Annotations
    {
        class _PmiAttributeValueMultipleStringBuilder;
        class PmiAttributeValueMultipleStringImpl;
        /** Represents a PMI Attribute MultipleString Value */
        class NXOPENCPPEXPORT  PmiAttributeValueMultipleString : public Annotations::PmiAttributeValue
        {
            private: PmiAttributeValueMultipleStringImpl * m_pmiattributevaluemultiplestring_impl;
            private: friend class  _PmiAttributeValueMultipleStringBuilder;
            protected: PmiAttributeValueMultipleString();
            public: ~PmiAttributeValueMultipleString();
        };
    }
}
#undef EXPORTLIBRARY
#endif