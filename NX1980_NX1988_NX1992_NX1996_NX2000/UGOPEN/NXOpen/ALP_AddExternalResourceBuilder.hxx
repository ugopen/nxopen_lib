#ifndef NXOpen_ALP_ADDEXTERNALRESOURCEBUILDER_HXX_INCLUDED
#define NXOpen_ALP_ADDEXTERNALRESOURCEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     ALP_AddExternalResourceBuilder.ja
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
#include <NXOpen/libalpopencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace ALP
    {
        class AddExternalResourceBuilder;
    }
    class Builder;
    class SelectDisplayableObjectList;
    namespace ALP
    {
        class _AddExternalResourceBuilderBuilder;
        class AddExternalResourceBuilderImpl;
        /** use for add external resource  <br> To create a new instance of this class, use @link NXOpen::ALP::ALPManager::CreateAddExternalResourceBuilder  NXOpen::ALP::ALPManager::CreateAddExternalResourceBuilder @endlink  <br> 
         <br>  Created in NX1980.0.0.  <br>  
        */
        class ALPOPENCPPEXPORT  AddExternalResourceBuilder : public NXOpen::Builder
        {
            private: AddExternalResourceBuilderImpl * m_addexternalresourcebuilder_impl;
            private: friend class  _AddExternalResourceBuilderBuilder;
            protected: AddExternalResourceBuilder();
            public: ~AddExternalResourceBuilder();
            /**Returns  the select components 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectDisplayableObjectList * SelectComponents
            (
            );
            /**Returns  the select resources 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectDisplayableObjectList * SelectResources
            (
            );
            /** The search resources 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: void SearchResources
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
