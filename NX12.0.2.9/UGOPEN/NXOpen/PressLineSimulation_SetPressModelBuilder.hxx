#ifndef NXOpen_PRESSLINESIMULATION_SETPRESSMODELBUILDER_HXX_INCLUDED
#define NXOpen_PRESSLINESIMULATION_SETPRESSMODELBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     PressLineSimulation_SetPressModelBuilder.ja
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
        class SetPressModelBuilder;
    }
    class Builder;
    namespace PressLineSimulation
    {
        class _SetPressModelBuilderBuilder;
        class SetPressModelBuilderImpl;
        /** A builder to setup the press model <br> To create a new instance of this class, use @link NXOpen::PressLineSimulation::ApplicationManager::CreateSetPressModelBuilder  NXOpen::PressLineSimulation::ApplicationManager::CreateSetPressModelBuilder @endlink  <br> 
         <br>  Created in NX12.0.0.  <br>  
        */
        class PRESSLINESIMULOPENCPPEXPORT  SetPressModelBuilder : public NXOpen::Builder
        {
            private: SetPressModelBuilderImpl * m_setpressmodelbuilder_impl;
            private: friend class  _SetPressModelBuilderBuilder;
            protected: SetPressModelBuilder();
            public: ~SetPressModelBuilder();
            /**Returns  the file path to the press model root part 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXString PressModelPartPath
            (
            );
            /**Sets  the file path to the press model root part 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_pls_die_checker (" NX Press Die Checker") */
            public: void SetPressModelPartPath
            (
                const NXString & filename /** filename */ 
            );
            /**Sets  the file path to the press model root part 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_pls_die_checker (" NX Press Die Checker") */
            void SetPressModelPartPath
            (
                const char * filename /** filename */ 
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
