#ifndef NXOpen_ALP_STATIONDETAILINGPREFERENCESBUILDER_HXX_INCLUDED
#define NXOpen_ALP_STATIONDETAILINGPREFERENCESBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     ALP_StationDetailingPreferencesBuilder.ja
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
#include <NXOpen/libalpopencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace ALP
    {
        class StationDetailingPreferencesBuilder;
    }
    class Builder;
    namespace ALP
    {
        class _StationDetailingPreferencesBuilderBuilder;
        class StationDetailingPreferencesBuilderImpl;

        /// \cond NX_NO_DOC 
        /**  <br> To create a new instance of this class, use @link NXOpen::ALP::ALPManager::CreateStationDetailingPreferencesBuilder  NXOpen::ALP::ALPManager::CreateStationDetailingPreferencesBuilder @endlink  <br> 
         <br>  Created in NX1926.0.0.  <br>  
        */
        class ALPOPENCPPEXPORT  StationDetailingPreferencesBuilder : public NXOpen::Builder
        {
            private: StationDetailingPreferencesBuilderImpl * m_stationdetailingpreferencesbuilder_impl;
            private: friend class  _StationDetailingPreferencesBuilderBuilder;
            protected: StationDetailingPreferencesBuilder();
            public: ~StationDetailingPreferencesBuilder();

            /// \cond NX_NO_DOC 
            /**Returns  the object type 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: NXString ObjectType
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the object type 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : alp_planner ("Assembly Line Planner") */
            public: void SetObjectType
            (
                const NXString & objectType /** objecttype */ 
            );
            /**Sets  the object type 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : alp_planner ("Assembly Line Planner") */
            void SetObjectType
            (
                const char * objectType /** objecttype */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** TODO fill in a description for this 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : alp_planner ("Assembly Line Planner") */
            public: void NewOperationButton
            (
            );

            /// \endcond 
        };

        /// \endcond 
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
