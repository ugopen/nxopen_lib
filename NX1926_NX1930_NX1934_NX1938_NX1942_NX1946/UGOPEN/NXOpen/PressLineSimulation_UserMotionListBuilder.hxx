#ifndef NXOpen_PRESSLINESIMULATION_USERMOTIONLISTBUILDER_HXX_INCLUDED
#define NXOpen_PRESSLINESIMULATION_USERMOTIONLISTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     PressLineSimulation_UserMotionListBuilder.ja
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
#include <NXOpen/ObjectList.hxx>
#include <NXOpen/libpresslinesimulopencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace PressLineSimulation
    {
        class UserMotionListBuilder;
    }
    class Builder;
    namespace PressLineSimulation
    {
        class UserMotionBuilderList;
    }
    namespace PressLineSimulation
    {
        class _UserMotionListBuilderBuilder;
        class UserMotionListBuilderImpl;
        /** Represents a @link PressLineSimulation::UserMotionListBuilder PressLineSimulation::UserMotionListBuilder@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::PressLineSimulation::ApplicationManager::CreateUserMotionListBuilder  NXOpen::PressLineSimulation::ApplicationManager::CreateUserMotionListBuilder @endlink  <br> 
         <br>  Created in NX12.0.0.  <br>  
        */
        class PRESSLINESIMULOPENCPPEXPORT  UserMotionListBuilder : public NXOpen::Builder
        {
            private: UserMotionListBuilderImpl * m_usermotionlistbuilder_impl;
            private: friend class  _UserMotionListBuilderBuilder;
            protected: UserMotionListBuilder();
            public: ~UserMotionListBuilder();
            /**Returns  the list of user motion builders. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::PressLineSimulation::UserMotionBuilderList * CamList
            (
            );
            /** To populate the list of user motion builders. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_pls_die_checker (" NX Press Die Checker") */
            public: void PopulateList
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