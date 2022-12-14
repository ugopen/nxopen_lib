#ifndef NXOpen_TOOLING_FASTENERASSEMCONFIGBUILDER_HXX_INCLUDED
#define NXOpen_TOOLING_FASTENERASSEMCONFIGBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Tooling_FastenerAssemConfigBuilder.ja
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
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Tooling
    {
        class FastenerAssemConfigBuilder;
    }
    class Builder;
    namespace Tooling
    {
        class _FastenerAssemConfigBuilderBuilder;
        /** Represents a Fastener Assem Config Collection.  <br> To create a new instance of this class, use @link Tooling::FastenerAssemConfigCollection::CreateBuilder Tooling::FastenerAssemConfigCollection::CreateBuilder@endlink  <br> */
        class NXOPENCPPEXPORT FastenerAssemConfigBuilder : public Builder
        {
            private: friend class  _FastenerAssemConfigBuilderBuilder;
            protected: FastenerAssemConfigBuilder();
        };
    }
}
#undef EXPORTLIBRARY
#endif
