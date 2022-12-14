#ifndef NXOpen_ANNOTATIONS_PMIATTRIBUTEVALUEINTEGERBUILDER_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_PMIATTRIBUTEVALUEINTEGERBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_PmiAttributeValueIntegerBuilder.ja
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
#include <NXOpen/Annotations_PmiAttributeValueIntegerBuilder.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Annotations
    {
        class PmiAttributeValueIntegerBuilder;
    }
    class Builder;
    namespace Annotations
    {
        class _PmiAttributeValueIntegerBuilderBuilder;
        class PmiAttributeValueIntegerBuilderImpl;
        /** Represents a @link Annotations::PmiAttributeValueInteger Annotations::PmiAttributeValueInteger@endlink  builder  <br> To create a new instance of this class, use @link Annotations::PmiAttributeCollection::CreatePmiAttributeValueIntegerBuilder Annotations::PmiAttributeCollection::CreatePmiAttributeValueIntegerBuilder@endlink  <br> */
        class NXOPENCPPEXPORT  PmiAttributeValueIntegerBuilder : public Builder
        {
            private: PmiAttributeValueIntegerBuilderImpl * m_pmiattributevalueintegerbuilder_impl;
            private: friend class  _PmiAttributeValueIntegerBuilderBuilder;
            protected: PmiAttributeValueIntegerBuilder();
            public: ~PmiAttributeValueIntegerBuilder();
            /**Returns  the integer_value  <br> License requirements : None */
            public: int IntegerValue
            (
            );
            /**Sets  the integer_value  <br> License requirements : None */
            public: void SetIntegerValue
            (
                int integerValue /** integervalue */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
