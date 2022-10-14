#ifndef NXOpen_DISPLAY_CGFXATTRIBUTEVALUEFLOAT4BUILDER_HXX_INCLUDED
#define NXOpen_DISPLAY_CGFXATTRIBUTEVALUEFLOAT4BUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Display_CgfxAttributeValueFloat4Builder.ja
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
#include <NXOpen/Builder.hxx>
#include <NXOpen/Display_CgfxAttributeValueFloat4Builder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Display
    {
        class CgfxAttributeValueFloat4Builder;
    }
    class Builder;
    namespace Display
    {
        class _CgfxAttributeValueFloat4BuilderBuilder;
        /** Represents a @link Display::CgfxAttributeValueFloat4Builder Display::CgfxAttributeValueFloat4Builder@endlink  builder  <br>  <br> */
        class NXOPENCPPEXPORT CgfxAttributeValueFloat4Builder : public Builder
        {
            private: friend class  _CgfxAttributeValueFloat4BuilderBuilder;
            protected: CgfxAttributeValueFloat4Builder();
            /** Gets the CgFX material attribute's array of 4 double values; these are float data types in a CgFX file  @return  array of 4 doubles  <br> License requirements : None */
            public: std::vector<double> GetFloat4Value
            (
            );
            /** Sets the CgFX material attribute's array of 4 double values; these are float data types in a CgFX file  <br> License requirements : None */
            public: void SetFloat4Value
            (
                const std::vector<double> & doubleTableValue /** array of 4 doubles */
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif