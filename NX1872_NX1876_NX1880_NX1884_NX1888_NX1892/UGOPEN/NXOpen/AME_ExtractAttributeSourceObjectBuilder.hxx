#ifndef NXOpen_AME_EXTRACTATTRIBUTESOURCEOBJECTBUILDER_HXX_INCLUDED
#define NXOpen_AME_EXTRACTATTRIBUTESOURCEOBJECTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     AME_ExtractAttributeSourceObjectBuilder.ja
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
#include <NXOpen/AME_ExtractAttributeBaseBuilder.hxx>
#include <NXOpen/libameopencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace AME
    {
        class ExtractAttributeSourceObjectBuilder;
    }
    namespace AME
    {
        class ExtractAttributeBaseBuilder;
    }
    namespace AME
    {
        class _ExtractAttributeSourceObjectBuilderBuilder;
        class ExtractAttributeSourceObjectBuilderImpl;
        /** Create a extract attribute   <br> This object does not need a creator.  <br> 
         <br>  Created in NX1872.0.0.  <br>  
        */
        class AMEOPENCPPEXPORT  ExtractAttributeSourceObjectBuilder : public NXOpen::AME::ExtractAttributeBaseBuilder
        {
            /** sourec object Type */
            public: enum SourceType
            {
                SourceTypeSelectObject/** select object */ ,
                SourceTypeMemoryArea/** memory area */ ,
                SourceTypeUserPorts/** user ports */ ,
                SourceTypeTypedPorts/** typed ports */ 
            };

            private: ExtractAttributeSourceObjectBuilderImpl * m_extractattributesourceobjectbuilder_impl;
            private: friend class  _ExtractAttributeSourceObjectBuilderBuilder;
            protected: ExtractAttributeSourceObjectBuilder();
            public: ~ExtractAttributeSourceObjectBuilder();
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
