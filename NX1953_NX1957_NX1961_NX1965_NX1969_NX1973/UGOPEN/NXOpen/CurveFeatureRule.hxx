#ifndef NXOpen_CURVEFEATURERULE_HXX_INCLUDED
#define NXOpen_CURVEFEATURERULE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CurveFeatureRule.ja
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
    class CurveFeatureRule;
    namespace Features
    {
        class Feature;
    }
    class SelectionIntentRule;
    class CurveFeatureRuleImpl;
    /** Represents a @link  NXOpen::SelectionIntentRule   NXOpen::SelectionIntentRule @endlink  that collects all curves created by a feature. 
     <br>  Created in NX3.0.0.  <br>  
    */
    class NXOPENCPPEXPORT  CurveFeatureRule : public NXOpen::SelectionIntentRule
    {
        private: CurveFeatureRuleImpl * m_curvefeaturerule_impl;
        /// \cond NX_NO_DOC 
        public: explicit CurveFeatureRule(void *ptr);
        /// \endcond 
        /** Frees the object from memory.
         <br>  Created in NX3.0.0.  <br>  
         <br> License requirements : None */
        public: virtual ~CurveFeatureRule();
        /** Gets the data for the curve feature rule: @link  NXOpen::CurveFeatureRule   NXOpen::CurveFeatureRule @endlink  
         <br>  Created in NX3.0.0.  <br>  
         <br> License requirements : gateway ("UG GATEWAY") */
        public: void GetData
        (
            std::vector<NXOpen::Features::Feature *> & features /** Features whose curves are used to create this rule*/
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
