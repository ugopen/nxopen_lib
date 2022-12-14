#ifndef NXOpen_DISPLAY_CGFXATTRIBUTEVALUENUMBERBUILDER_HXX_INCLUDED
#define NXOpen_DISPLAY_CGFXATTRIBUTEVALUENUMBERBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Display_CgfxAttributeValueNumberBuilder.ja
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
#include <NXOpen/Display_CgfxAttributeValueNumberBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Display
    {
        class CgfxAttributeValueNumberBuilder;
    }
    class Builder;
    namespace Display
    {
        class _CgfxAttributeValueNumberBuilderBuilder;
        class CgfxAttributeValueNumberBuilderImpl;
        /** Represents a @link Display::CgfxAttributeValueNumberBuilder Display::CgfxAttributeValueNumberBuilder@endlink  builder  <br>  <br> */
        class NXOPENCPPEXPORT  CgfxAttributeValueNumberBuilder : public Builder
        {
            private: CgfxAttributeValueNumberBuilderImpl * m_cgfxattributevaluenumberbuilder_impl;
            private: friend class  _CgfxAttributeValueNumberBuilderBuilder;
            protected: CgfxAttributeValueNumberBuilder();
            public: ~CgfxAttributeValueNumberBuilder();
            /**Returns  the CgFX material attribute's double number value  <br> License requirements : None */
            public: double NumberValue
            (
            );
            /**Sets  the CgFX material attribute's double number value  <br> License requirements : None */
            public: void SetNumberValue
            (
                double numberValue /** numbervalue */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
