#ifndef NXOpen_MFGVIEWMAKER_MFGVIEWMAKERAPPLICATIONBUILDER_HXX_INCLUDED
#define NXOpen_MFGVIEWMAKER_MFGVIEWMAKERAPPLICATIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     MFGViewMaker_MFGViewMakerApplicationBuilder.ja
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
#include <NXOpen/NXObject.hxx>
#include <NXOpen/libmfgviewmakeropencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace MFGViewMaker
    {
        class MFGViewMakerApplicationBuilder;
    }
    class NXObject;
    namespace MFGViewMaker
    {
        class _MFGViewMakerApplicationBuilderBuilder;
        class MFGViewMakerApplicationBuilderImpl;
        /**
            Represents a class to create enter and exit the MFGViewMaker application
            
         <br>  Created in NX11.0.1.  <br>  
        */
        class MFGVIEWMAKEROPENCPPEXPORT  MFGViewMakerApplicationBuilder : public NXOpen::NXObject
        {
            private: MFGViewMakerApplicationBuilderImpl * m_mfgviewmakerapplicationbuilder_impl;
            private: friend class  _MFGViewMakerApplicationBuilderBuilder;
            protected: MFGViewMakerApplicationBuilder();
            public: ~MFGViewMakerApplicationBuilder();
            /**  Enter the MFGViewMaker application 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: void Enter
            (
            );
            /**  Exit the MFGViewMaker application this call will destroy the builder
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: void Exit
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