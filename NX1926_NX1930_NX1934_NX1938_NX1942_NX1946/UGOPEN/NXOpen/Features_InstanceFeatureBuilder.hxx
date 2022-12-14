#ifndef NXOpen_FEATURES_INSTANCEFEATUREBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_INSTANCEFEATUREBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_InstanceFeatureBuilder.ja
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
#include <NXOpen/GeometricUtilities_InstanceEditedExpressionsList.hxx>
#include <NXOpen/GeometricUtilities_PatternClockingBuilder.hxx>
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
        class InstanceFeatureBuilder;
    }
    namespace Features
    {
        class FeatureBuilder;
    }
    namespace GeometricUtilities
    {
        class InstanceEditedExpressionsList;
    }
    namespace GeometricUtilities
    {
        class PatternClockingBuilder;
    }
    namespace Features
    {
        class _InstanceFeatureBuilderBuilder;
        class InstanceFeatureBuilderImpl;
        /** instance feature builder  <br> To create a new instance of this class, use @link NXOpen::Features::FeatureCollection::CreateInstanceFeatureBuilder  NXOpen::Features::FeatureCollection::CreateInstanceFeatureBuilder @endlink  <br> 
        Default values.
        <list type="table"> 
         
        <listheader><term> 
        Property</term>  <description> 
        Value</description> </listheader>
        <item><term> 
         
        InstanceClocking.Motion.DeltaEnum </term> <description> 
         
        ReferenceWcsWorkPart </description> </item> 

        <item><term> 
         
        InstanceClocking.Motion.DeltaXc.Value </term> <description> 
         
        0.0 </description> </item> 

        <item><term> 
         
        InstanceClocking.Motion.DeltaYc.Value </term> <description> 
         
        0.0 </description> </item> 

        <item><term> 
         
        InstanceClocking.Motion.DeltaZc.Value </term> <description> 
         
        0.0 </description> </item> 

        </list> 

         <br>  Created in NX8.0.0.  <br>  
        */
        class NXOPENCPP_FEATURESEXPORT  InstanceFeatureBuilder : public NXOpen::Features::FeatureBuilder
        {
            private: InstanceFeatureBuilderImpl * m_instancefeaturebuilder_impl;
            private: friend class  _InstanceFeatureBuilderBuilder;
            protected: InstanceFeatureBuilder();
            public: ~InstanceFeatureBuilder();
            /**Returns  the edited expressions list @link NXOpen::GeometricUtilities::InstanceEditedExpressionsList NXOpen::GeometricUtilities::InstanceEditedExpressionsList@endlink . 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricUtilities::InstanceEditedExpressionsList * EditedExpressionsList
            (
            );
            /**Returns  the instance clocking @link NXOpen::GeometricUtilities::PatternClockingBuilder NXOpen::GeometricUtilities::PatternClockingBuilder@endlink . 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricUtilities::PatternClockingBuilder * InstanceClocking
            (
            );
            /** Removes clocking from (unclocks) a @link NXOpen::Features::InstanceFeature NXOpen::Features::InstanceFeature@endlink . 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void RemoveClocking
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
