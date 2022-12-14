#ifndef NXOpen_APPARENTCHAININGRULE_HXX_INCLUDED
#define NXOpen_APPARENTCHAININGRULE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     ApparentChainingRule.ja
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
    class ApparentChainingRule;
    class ICurve;
    class SelectionIntentRule;
    class View;
    class ApparentChainingRuleImpl;
    /** Represents a @link  SelectionIntentRule   SelectionIntentRule @endlink  that collects curves which appear connected or tangent connected in a particular drafting view. 
     <br>  Created in NX8.0.0.  <br>  
    */
    class NXOPENCPPEXPORT  ApparentChainingRule : public SelectionIntentRule
    {
        private: ApparentChainingRuleImpl * m_apparentchainingrule_impl;
        /// \cond NX_NO_DOC 
        public: explicit ApparentChainingRule(void *ptr);
        /// \endcond 
        /** Frees the object from memory.
         <br>  Created in NX8.0.0.  <br>  
         <br> License requirements : None */
        public: virtual ~ApparentChainingRule();
        /** Gets the data for the apparent chaining rule: @link  ApparentChainingRule   ApparentChainingRule @endlink  
         <br>  Created in NX8.0.0.  <br>  
         <br> License requirements : gateway ("UG GATEWAY") */
        public: void GetData
        (
            NXOpen::ICurve ** seed /** The seed curve. */,
            NXOpen::View ** view /** The view. */,
            NXOpen::ApparentChainingRuleType* chainingRule /** Selection Intent method, either of Connected Curves, Tangent Curves or Single Curve. */,
            NXOpen::ApparentChainingRuleSelection* selectionMask /** The selection type none, edge or curve. */,
            double* chainingTolerance /** Gap tolerance*/,
            double* angleTolerance /** Angle tolerance*/
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
