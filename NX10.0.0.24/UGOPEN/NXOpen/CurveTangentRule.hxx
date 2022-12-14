#ifndef NXOpen_CURVETANGENTRULE_HXX_INCLUDED
#define NXOpen_CURVETANGENTRULE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CurveTangentRule.ja
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
    class CurveTangentRule;
    class Curve;
    class SelectionIntentRule;
    class CurveTangentRuleImpl;
    /** Represents a @link  NXOpen::SelectionIntentRule   NXOpen::SelectionIntentRule @endlink  that collects tangent connected curves from the seed curve. 
     <br>  Created in NX9.0.0.  <br>  
    */
    class NXOPENCPPEXPORT  CurveTangentRule : public NXOpen::SelectionIntentRule
    {
        private: CurveTangentRuleImpl * m_curvetangentrule_impl;
        /// \cond NX_NO_DOC 
        public: explicit CurveTangentRule(void *ptr);
        /// \endcond 
        /** Frees the object from memory.
         <br>  Created in NX9.0.0.  <br>  
         <br> License requirements : None */
        public: virtual ~CurveTangentRule();
        /** Gets the data for the curve tangent rule: @link  NXOpen::CurveTangentRule   NXOpen::CurveTangentRule @endlink  
         <br>  Created in NX9.0.0.  <br>  
         <br> License requirements : None */
        public: void GetData
        (
            NXOpen::Curve ** seedCurve /** Seed curve */,
            NXOpen::Curve ** endCurve /** End curve. It can be null (Nothing) */,
            bool* isFromSeedStart /** True: the chain starts from the start
                                                 point of the seed curve */,
            double* angleTolerance /** Angle tolerance for tangent curves */,
            double* gapTolerance /** Gap tolerance for tangent curves */
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
