#ifndef NXOpen_USERDEFINEDTEMPLATE_ITEMNODELABEL_HXX_INCLUDED
#define NXOpen_USERDEFINEDTEMPLATE_ITEMNODELABEL_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     UserDefinedTemplate_ItemNodeLabel.ja
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
        class ItemNodeLabel;
    }
    namespace UserDefinedTemplate
    {
        class ConfigurableObject;
    }
    namespace UserDefinedTemplate
    {
        class _ItemNodeLabelBuilder;
        class ItemNodeLabelImpl;
        /** Represents a @link NXOpen::UserDefinedTemplate::ItemNodeLabel NXOpen::UserDefinedTemplate::ItemNodeLabel@endlink   <br> This is the collapsible label node class.  <br> 
         <br>  Created in NX2007.0.0.  <br>  
        */
        class NXOPENCPP_USERDEFINEDTEMPLATEEXPORT  ItemNodeLabel : public NXOpen::UserDefinedTemplate::ConfigurableObject
        {
            private: ItemNodeLabelImpl * m_itemnodelabel_impl;
            private: friend class  _ItemNodeLabelBuilder;
            protected: ItemNodeLabel();
            public: ~ItemNodeLabel();
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