#ifndef NXOpen_JOIN_JOINBUILDER_HXX_INCLUDED
#define NXOpen_JOIN_JOINBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Join_JoinBuilder.ja
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
#include <NXOpen/Expression.hxx>
#include <NXOpen/Features_FeatureBuilder.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/libjoinopencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Join
    {
        class JoinBuilder;
    }
    class Expression;
    namespace Features
    {
        class FeatureBuilder;
    }
    class SelectBodyList;
    class TaggedObject;
    namespace Join
    {
        class _JoinBuilderBuilder;
        class JoinBuilderImpl;
        /**
            Base class for all NXOpen.Join builders.
             <br> This is an abstract class and cannot be instantiated  <br> 
         <br>  Created in NX1872.0.0.  <br>  
        */
        class JOINOPENCPPEXPORT  JoinBuilder : public NXOpen::Features::FeatureBuilder
        {
            private: JoinBuilderImpl * m_joinbuilder_impl;
            private: friend class  _JoinBuilderBuilder;
            protected: JoinBuilder();
            public: ~JoinBuilder();
            /**Returns  the Subtype 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_join (" NX Join") */
            public: NXString Subtype
            (
            );
            /**Sets  the Subtype 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_join (" NX Join") */
            public: void SetSubtype
            (
                const NXString & type /** type */ 
            );
            /**Sets  the Subtype 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_join (" NX Join") */
            void SetSubtype
            (
                const char * type /** type */ 
            );
            /**Returns  the Connected Bodies 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_join (" NX Join") */
            public: NXOpen::SelectBodyList * ConnectedBodies
            (
            );
            /**Returns  a delayed feature update. A logical true delays updating the join feature 
                    when the dependency geometries change. False updates the join feature normally. 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_join (" NX Join") */
            public: bool DelayUpdate
            (
            );
            /**Sets  a delayed feature update. A logical true delays updating the join feature 
                    when the dependency geometries change. False updates the join feature normally. 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_join (" NX Join") */
            public: void SetDelayUpdate
            (
                bool delayUpdate /** delayupdate */ 
            );
            /**Returns  the associative option for join creation 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_join (" NX Join") */
            public: bool Associative
            (
            );
            /**Sets  the associative option for join creation 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_join (" NX Join") */
            public: void SetAssociative
            (
                bool associative /** associative */ 
            );
            /**Returns  the distance tolerance 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_join (" NX Join") */
            public: NXOpen::Expression * DistanceTolerance
            (
            );
            /**Returns  a custom attribute holder object that holds the attributes temporarily.
                    The custom attributes for the @link NXOpen::Features::BodyFeature NXOpen::Features::BodyFeature@endlink  could be set on this object. 
                    If the attributes match the attributes' description in the join feature description, the custom attributes are created on the feature. Otherwise, ignored.
                    Do not delete this object, deletion results in undefined behavior. 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_join (" NX Join") */
            public: NXOpen::TaggedObject * CustomAttributesHolder
            (
            );
            /** Indicates whether the output objects should show through on creation 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : nx_join (" NX Join") */
            public: void SetShowThroughState
            (
                bool status /** true- Add show through attribute to point. */
            );
            /** Indicates whether the output should be hidden on creation 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : nx_join (" NX Join") */
            public: void SetHideSolid
            (
                bool hideSolid /** true- Hide output solid. */
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
