#ifndef NXOpen_FEATURES_DESIGNGROUPBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_DESIGNGROUPBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_DesignGroupBuilder.ja
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
#include <NXOpen/Features_FeatureBuilder.hxx>
#include <NXOpen/libnxopencpp_features_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Features
    {
        class DesignGroupBuilder;
    }
    namespace Features
    {
        class FeatureBuilder;
    }
    namespace Features
    {
        class _DesignGroupBuilderBuilder;
        class DesignGroupBuilderImpl;

        /// \cond NX_NO_DOC 
        /** Represents a @link NXOpen::Features::DesignGroup NXOpen::Features::DesignGroup@endlink  builder for Design Group.  <br> To create a new instance of this class, use @link NXOpen::Features::FeatureCollection::CreateDesignGroupBuilder  NXOpen::Features::FeatureCollection::CreateDesignGroupBuilder @endlink  <br> 
         <br>  Created in NX1847.0.0.  <br>  
        */
        class NXOPENCPP_FEATURESEXPORT  DesignGroupBuilder : public NXOpen::Features::FeatureBuilder
        {
            private: DesignGroupBuilderImpl * m_designgroupbuilder_impl;
            private: friend class  _DesignGroupBuilderBuilder;
            protected: DesignGroupBuilder();
            public: ~DesignGroupBuilder();

            /// \cond NX_NO_DOC 
            /**Returns  the design group name 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : usr_defined_features ("USER DEFINED FEATURES") */
            public: NXString Name
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the design group name 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : usr_defined_features ("USER DEFINED FEATURES") */
            public: void SetName
            (
                const NXString & name /** name */ 
            );
            /**Sets  the design group name 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : usr_defined_features ("USER DEFINED FEATURES") */
            void SetName
            (
                const char * name /** name */ 
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
