#ifndef NXOpen_AME_PORTATTRIBUTEHOLDER_HXX_INCLUDED
#define NXOpen_AME_PORTATTRIBUTEHOLDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     AME_PortAttributeHolder.ja
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
#include <NXOpen/AME_AttributeHolder.hxx>
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
        class PortAttributeHolder;
    }
    namespace AME
    {
        class AttributeHolder;
    }
    namespace AME
    {
        class _PortAttributeHolderBuilder;
        class PortAttributeHolderImpl;
        /** Port Object Atributes Holder <br> This does not need a creator.  <br> 
         <br>  Created in NX12.0.0.  <br>  
        */
        class AMEOPENCPPEXPORT  PortAttributeHolder : public NXOpen::AME::AttributeHolder
        {
            private: PortAttributeHolderImpl * m_portattributeholder_impl;
            private: friend class  _PortAttributeHolderBuilder;
            protected: PortAttributeHolder();
            public: ~PortAttributeHolder();
            /** Set CurrentClassId 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetCurrentClassId
            (
                const NXString & classId /** classid */ 
            );
            /** Set CurrentClassId 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            void SetCurrentClassId
            (
                const char * classId /** classid */ 
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
