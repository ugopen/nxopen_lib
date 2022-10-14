#ifndef NXOpen_USERDEFINEDTEMPLATE_ITEMNODESTRING_HXX_INCLUDED
#define NXOpen_USERDEFINEDTEMPLATE_ITEMNODESTRING_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     UserDefinedTemplate_ItemNodeString.ja
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
#include <NXOpen/UserDefinedTemplate_ItemNodeExpression.hxx>
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
        class ItemNodeString;
    }
    namespace UserDefinedTemplate
    {
        class ItemNodeExpression;
    }
    namespace UserDefinedTemplate
    {
        class _ItemNodeStringBuilder;
        class ItemNodeStringImpl;
        /** Represents a @link NXOpen::UserDefinedTemplate::ItemNodeString NXOpen::UserDefinedTemplate::ItemNodeString@endlink   <br> This is the string expression node class.  <br> 
         <br>  Created in NX2007.0.0.  <br>  
        */
        class NXOPENCPP_USERDEFINEDTEMPLATEEXPORT  ItemNodeString : public NXOpen::UserDefinedTemplate::ItemNodeExpression
        {
            private: ItemNodeStringImpl * m_itemnodestring_impl;
            private: friend class  _ItemNodeStringBuilder;
            protected: ItemNodeString();
            public: ~ItemNodeString();
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