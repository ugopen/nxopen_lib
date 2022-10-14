#ifndef NXOpen_AME_ASSIGNSUBNETBUILDER_HXX_INCLUDED
#define NXOpen_AME_ASSIGNSUBNETBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     AME_AssignSubnetBuilder.ja
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
#include <NXOpen/SelectObject.hxx>
#include <NXOpen/SelectObjectList.hxx>
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
        class AssignSubnetBuilder;
    }
    class Builder;
    class SelectNXObject;
    class SelectNXObjectList;
    namespace AME
    {
        class _AssignSubnetBuilderBuilder;
        class AssignSubnetBuilderImpl;
        /** Reassign a single aspect of an Engineering Object  <br> To create a new instance of this class, use @link NXOpen::AME::AMEManager::CreateAssignSubnetBuilder  NXOpen::AME::AMEManager::CreateAssignSubnetBuilder @endlink  <br> 
         <br>  Created in NX12.0.0.  <br>  
        */
        class AMEOPENCPPEXPORT  AssignSubnetBuilder : public NXOpen::Builder
        {
            private: AssignSubnetBuilderImpl * m_assignsubnetbuilder_impl;
            private: friend class  _AssignSubnetBuilderBuilder;
            protected: AssignSubnetBuilder();
            public: ~AssignSubnetBuilder();
            /**Returns  the selection of com. interfaces to be assigned
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::SelectNXObjectList * SelectedComInterfaces
            (
            );
            /**Returns  the selection where the object will be reassigned. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::SelectNXObject * SelectedSubnet
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