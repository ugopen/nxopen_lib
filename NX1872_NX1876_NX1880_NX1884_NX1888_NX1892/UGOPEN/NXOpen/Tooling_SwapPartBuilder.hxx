#ifndef NXOpen_TOOLING_SWAPPARTBUILDER_HXX_INCLUDED
#define NXOpen_TOOLING_SWAPPARTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Tooling_SwapPartBuilder.ja
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
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/libnxopencpp_tooling_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Tooling
    {
        class SwapPartBuilder;
    }
    class Builder;
    class SelectNXObjectList;
    namespace Tooling
    {
        class _SwapPartBuilderBuilder;
        class SwapPartBuilderImpl;
        /** Creates swap part for progressive die.No entity is returned.  <br> To create a new instance of this class, use @link NXOpen::Tooling::ProgressiveDieManager::CreateSwapPartBuilder  NXOpen::Tooling::ProgressiveDieManager::CreateSwapPartBuilder @endlink  <br> 
         <br>  Created in NX1872.0.0.  <br>  
        */
        class NXOPENCPP_TOOLINGEXPORT  SwapPartBuilder : public NXOpen::Builder
        {
            private: SwapPartBuilderImpl * m_swappartbuilder_impl;
            private: friend class  _SwapPartBuilderBuilder;
            protected: SwapPartBuilder();
            public: ~SwapPartBuilder();
            /** Select new part as component 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SelectNewPartAsComponentButton
            (
            );
            /**Returns  the select body and make linked body 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectNXObjectList * SelectBodyAndMakeLinkedBody
            (
            );
            /**Returns  the select body in new component 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectNXObjectList * SelectBodyInNewComponent
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
