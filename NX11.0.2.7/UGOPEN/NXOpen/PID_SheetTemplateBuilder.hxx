#ifndef NXOpen_PID_SHEETTEMPLATEBUILDER_HXX_INCLUDED
#define NXOpen_PID_SHEETTEMPLATEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     PID_SheetTemplateBuilder.ja
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
#include <NXOpen/Diagramming_SheetBuilder.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/PID_SheetTemplateBuilder.hxx>
#include <NXOpen/libpidopencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace PID
    {
        class SheetTemplateBuilder;
    }
    class Builder;
    namespace Diagramming
    {
        class SheetBuilder;
    }
    namespace PID
    {
        class _SheetTemplateBuilderBuilder;
        class SheetTemplateBuilderImpl;
        /** Represents a @link NXOpen::PID::SheetTemplateBuilder NXOpen::PID::SheetTemplateBuilder@endlink  builder, and the builder is used to model a sheet template.  <br> To create a new instance of this class, use @link NXOpen::PID::PidManager::CreateSheetTemplateBuilder  NXOpen::PID::PidManager::CreateSheetTemplateBuilder @endlink  <br> 
         <br>  Created in NX11.0.0.  <br>  
        */
        class PIDOPENCPPEXPORT  SheetTemplateBuilder : public NXOpen::Builder
        {
            private: SheetTemplateBuilderImpl * m_sheettemplatebuilder_impl;
            private: friend class  _SheetTemplateBuilderBuilder;
            protected: SheetTemplateBuilder();
            public: ~SheetTemplateBuilder();
            /**Returns  the diagramming sheet builder. 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : None */
            public: NXOpen::Diagramming::SheetBuilder * Sheet
            (
            );
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