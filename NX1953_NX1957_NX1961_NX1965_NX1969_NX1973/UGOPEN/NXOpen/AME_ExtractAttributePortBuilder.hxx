#ifndef NXOpen_AME_EXTRACTATTRIBUTEPORTBUILDER_HXX_INCLUDED
#define NXOpen_AME_EXTRACTATTRIBUTEPORTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     AME_ExtractAttributePortBuilder.ja
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
        class ExtractAttributePortBuilder;
    }
    namespace AME
    {
        class ExtractAttributeBaseBuilder;
    }
    class NXObject;
    namespace AME
    {
        class _ExtractAttributePortBuilderBuilder;
        class ExtractAttributePortBuilderImpl;
        /** Create a extract port attribute builder  <br> This object does not need a creator.  <br> 
         <br>  Created in NX11.0.0.  <br>  
        */
        class AMEOPENCPPEXPORT  ExtractAttributePortBuilder : public NXOpen::AME::ExtractAttributeBaseBuilder
        {
            private: ExtractAttributePortBuilderImpl * m_extractattributeportbuilder_impl;
            private: friend class  _ExtractAttributePortBuilderBuilder;
            protected: ExtractAttributePortBuilder();
            public: ~ExtractAttributePortBuilder();

            /// \cond NX_NO_DOC 
            /** Creates or gets attribute proxy objects which hold proxy attributes of EngObject and Plc Symbols 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: std::vector<NXOpen::NXObject *> CreateOrGetAttributeproxyObjects
            (
            );

            /// \endcond 
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
