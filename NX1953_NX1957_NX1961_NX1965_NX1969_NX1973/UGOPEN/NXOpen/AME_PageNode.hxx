#ifndef NXOpen_AME_PAGENODE_HXX_INCLUDED
#define NXOpen_AME_PAGENODE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     AME_PageNode.ja
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
#include <NXOpen/AME_AMEBaseNode.hxx>
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
        class PageNode;
    }
    namespace AME
    {
        class AMEBaseNode;
    }
    namespace AME
    {
        class _PageNodeBuilder;
        class PageNodeImpl;
        /** Represents a Page Node  <br> This object can not be created directly.  <br> 
         <br>  Created in NX11.0.0.  <br>  
        */
        class AMEOPENCPPEXPORT  PageNode : public NXOpen::AME::AMEBaseNode
        {
            private: PageNodeImpl * m_pagenode_impl;
            private: friend class  _PageNodeBuilder;
            protected: PageNode();
            public: ~PageNode();
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
