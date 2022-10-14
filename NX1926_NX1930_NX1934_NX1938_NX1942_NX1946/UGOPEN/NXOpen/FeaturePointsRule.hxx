#ifndef NXOpen_FEATUREPOINTSRULE_HXX_INCLUDED
#define NXOpen_FEATUREPOINTSRULE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     FeaturePointsRule.ja
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
#include <NXOpen/SelectionIntentRule.hxx>
#include <NXOpen/SelectionIntentRule.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    class FeaturePointsRule;
    namespace Features
    {
        class Feature;
    }
    class SelectionIntentRule;
    class FeaturePointsRuleImpl;
    /** Represents a @link  NXOpen::SelectionIntentRule   NXOpen::SelectionIntentRule @endlink  that collects all points created by a feature. 
     <br>  Created in NX5.0.2.  <br>  
    */
    class NXOPENCPPEXPORT  FeaturePointsRule : public NXOpen::SelectionIntentRule
    {
        private: FeaturePointsRuleImpl * m_featurepointsrule_impl;
        /// \cond NX_NO_DOC 
        public: explicit FeaturePointsRule(void *ptr);
        /// \endcond 
        /** Frees the object from memory.
         <br>  Created in NX5.0.2.  <br>  
         <br> License requirements : None */
        public: virtual ~FeaturePointsRule();
        /** Gets the data for the feature points rule: @link  NXOpen::FeaturePointsRule   NXOpen::FeaturePointsRule @endlink  
         <br>  Created in NX5.0.2.  <br>  
         <br> License requirements : gateway ("UG GATEWAY") */
        public: void GetData
        (
            std::vector<NXOpen::Features::Feature *> & features /** Features whose points are used to create this rule */
        );
    }; //lint !e1712 default constructor not defined for class  

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