#ifndef NXOpen_AME_ECLASSGLOBALOBJECTNODE_HXX_INCLUDED
#define NXOpen_AME_ECLASSGLOBALOBJECTNODE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     AME_EClassGlobalObjectNode.ja
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
        class EClassGlobalObjectNode;
    }
    namespace AME
    {
        class AMEBaseNode;
    }
    namespace AME
    {
        class _EClassGlobalObjectNodeBuilder;
        class EClassGlobalObjectNodeImpl;
        /** EClassGlobalObject Tree Node class  <br> This object does not need a creator.  <br> 
         <br>  Created in NX1847.0.0.  <br>  
        */
        class AMEOPENCPPEXPORT  EClassGlobalObjectNode : public NXOpen::AME::AMEBaseNode
        {
            private: EClassGlobalObjectNodeImpl * m_eclassglobalobjectnode_impl;
            private: friend class  _EClassGlobalObjectNodeBuilder;
            protected: EClassGlobalObjectNode();
            public: ~EClassGlobalObjectNode();
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
