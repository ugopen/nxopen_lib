#ifndef NXOpen_AME_CABINETNODE_HXX_INCLUDED
#define NXOpen_AME_CABINETNODE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     AME_CabinetNode.ja
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
#include <NXOpen/AME_CabinetComponentNode.hxx>
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
        class CabinetNode;
    }
    namespace AME
    {
        class AMEBaseNode;
    }
    namespace AME
    {
        class CabinetComponentNode;
    }
    namespace AME
    {
        class _CabinetNodeBuilder;
        class CabinetNodeImpl;
        /** Cabinet Node class  <br> This object does not need a creator.  <br> 
         <br>  Created in NX12.0.0.  <br>  
        */
        class AMEOPENCPPEXPORT  CabinetNode : public NXOpen::AME::AMEBaseNode
        {
            private: CabinetNodeImpl * m_cabinetnode_impl;
            private: friend class  _CabinetNodeBuilder;
            protected: CabinetNode();
            public: ~CabinetNode();
            /** Removes cabinet component 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void RemoveObjects
            (
                const std::vector<NXOpen::AME::CabinetComponentNode *> & cabinetComponentNodes /** cabinetcomponentnodes */ 
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
