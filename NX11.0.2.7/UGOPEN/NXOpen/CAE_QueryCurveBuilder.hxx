#ifndef NXOpen_CAE_QUERYCURVEBUILDER_HXX_INCLUDED
#define NXOpen_CAE_QUERYCURVEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_QueryCurveBuilder.ja
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
#include <NXOpen/CAE_OrderedSelection.hxx>
#include <NXOpen/CAE_QueryCurveBuilder.hxx>
#include <NXOpen/Builder.hxx>
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
        class QueryCurveBuilder;
    }
    class Builder;
    namespace CAE
    {
        class OrderedSelection;
    }
    namespace CAE
    {
        class _QueryCurveBuilderBuilder;
        class QueryCurveBuilderImpl;
        /**
            Represents a @link NXOpen::CAE::QueryCurveBuilder NXOpen::CAE::QueryCurveBuilder@endlink 
             <br> To create a new instance of this class, use @link NXOpen::CAE::QueryCurveManager::CreateQueryCurveBuilder  NXOpen::CAE::QueryCurveManager::CreateQueryCurveBuilder @endlink  <br> 
         <br>  Created in NX11.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  QueryCurveBuilder : public NXOpen::Builder
        {
            private: QueryCurveBuilderImpl * m_querycurvebuilder_impl;
            private: friend class  _QueryCurveBuilderBuilder;
            protected: QueryCurveBuilder();
            public: ~QueryCurveBuilder();
            /**Returns  the curve name 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXString CurveName
            (
            );
            /**Sets  the curve name 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetCurveName
            (
                const NXString & curveName /** curvename */ 
            );
            /**Sets  the curve name 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            void SetCurveName
            (
                const char * curveName /** curvename */ 
            );
            /**Returns  the selection 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::CAE::OrderedSelection * Selection
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