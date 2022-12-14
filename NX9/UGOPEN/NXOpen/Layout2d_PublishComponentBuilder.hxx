#ifndef NXOpen_LAYOUT2D_PUBLISHCOMPONENTBUILDER_HXX_INCLUDED
#define NXOpen_LAYOUT2D_PUBLISHCOMPONENTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Layout2d_PublishComponentBuilder.ja
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
#include <NXOpen/libnxopencpp_layout2d_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Layout2d
    {
        class PublishComponentBuilder;
    }
    class Builder;
    namespace Layout2d
    {
        class _PublishComponentBuilderBuilder;
        class PublishComponentBuilderImpl;
        /** Represents a Builder for Publish 2D component functionality which will allow
                local definitions to be exported into external storage locations  <br> To create a new instance of this class, use @link Layout2d::ComponentCollection::CreatePublishComponentBuilder  Layout2d::ComponentCollection::CreatePublishComponentBuilder @endlink  <br> 
         <br>  Created in NX9.0.0.  <br>  
        */
        class NXOPENCPP_LAYOUT2DEXPORT  PublishComponentBuilder : public Builder
        {
            private: PublishComponentBuilderImpl * m_publishcomponentbuilder_impl;
            private: friend class  _PublishComponentBuilderBuilder;
            protected: PublishComponentBuilder();
            public: ~PublishComponentBuilder();
        };
    }
}

#ifdef _MSC_VER
#pragma warning(pop)
#endif
#ifdef __GNUC__
#ifndef NX_NO_GCC_DEPRECATION_WARNINGS
#pragma GCC diagnostic warning "-Wdeprecated-declarations"
#endif
#endif

#undef EXPORTLIBRARY
#endif
