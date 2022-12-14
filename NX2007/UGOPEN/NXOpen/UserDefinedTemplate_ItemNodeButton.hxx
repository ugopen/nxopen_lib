#ifndef NXOpen_USERDEFINEDTEMPLATE_ITEMNODEBUTTON_HXX_INCLUDED
#define NXOpen_USERDEFINEDTEMPLATE_ITEMNODEBUTTON_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     UserDefinedTemplate_ItemNodeButton.ja
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
#include <NXOpen/UserDefinedTemplate_ConfigurableObject.hxx>
#include <NXOpen/libnxopencpp_userdefinedtemplate_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace UserDefinedTemplate
    {
        class ItemNodeButton;
    }
    namespace UserDefinedTemplate
    {
        class ConfigurableObject;
    }
    namespace UserDefinedTemplate
    {
        class _ItemNodeButtonBuilder;
        class ItemNodeButtonImpl;
        /** Represents a @link NXOpen::UserDefinedTemplate::ItemNodeButton NXOpen::UserDefinedTemplate::ItemNodeButton@endlink   <br> This is the button node class.  <br> 
         <br>  Created in NX2007.0.0.  <br>  
        */
        class NXOPENCPP_USERDEFINEDTEMPLATEEXPORT  ItemNodeButton : public NXOpen::UserDefinedTemplate::ConfigurableObject
        {
            private: ItemNodeButtonImpl * m_itemnodebutton_impl;
            private: friend class  _ItemNodeButtonBuilder;
            protected: ItemNodeButton();
            public: ~ItemNodeButton();
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
