#ifndef NXOpen_CAE_SHOWADJACENTBUILDER_HXX_INCLUDED
#define NXOpen_CAE_SHOWADJACENTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_ShowAdjacentBuilder.ja
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
#include <NXOpen/CAE_ShowAdjacentBuilder.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/libnxopencpp_cae_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace CAE
    {
        class ShowAdjacentBuilder;
    }
    class Builder;
    class SelectObjectList;
    namespace CAE
    {
        class _ShowAdjacentBuilderBuilder;
        class ShowAdjacentBuilderImpl;
        /**
            Represents a @link NXOpen::CAE::ShowAdjacentBuilder NXOpen::CAE::ShowAdjacentBuilder@endlink 
             <br> To create a new instance of this class, use @link NXOpen::CAE::ShowHideManager::CreateShowAdjacentBuilder  NXOpen::CAE::ShowHideManager::CreateShowAdjacentBuilder @endlink  <br> 
         <br>  Created in NX5.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  ShowAdjacentBuilder : public NXOpen::Builder
        {
            private: ShowAdjacentBuilderImpl * m_showadjacentbuilder_impl;
            private: friend class  _ShowAdjacentBuilderBuilder;
            protected: ShowAdjacentBuilder();
            public: ~ShowAdjacentBuilder();
            /**Returns  the selection 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectObjectList * Selection
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