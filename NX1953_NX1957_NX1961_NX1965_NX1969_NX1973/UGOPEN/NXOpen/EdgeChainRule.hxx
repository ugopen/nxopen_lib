#ifndef NXOpen_EDGECHAINRULE_HXX_INCLUDED
#define NXOpen_EDGECHAINRULE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     EdgeChainRule.ja
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
    class EdgeChainRule;
    class Edge;
    class SelectionIntentRule;
    class EdgeChainRuleImpl;
    /** Represents a @link  NXOpen::SelectionIntentRule   NXOpen::SelectionIntentRule @endlink  that collects end-to-end connected edges from the body of the seed edge. 
     <br>  Created in NX3.0.0.  <br>  
    */
    class NXOPENCPPEXPORT  EdgeChainRule : public NXOpen::SelectionIntentRule
    {
        private: EdgeChainRuleImpl * m_edgechainrule_impl;
        /// \cond NX_NO_DOC 
        public: explicit EdgeChainRule(void *ptr);
        /// \endcond 
        /** Frees the object from memory.
         <br>  Created in NX3.0.0.  <br>  
         <br> License requirements : None */
        public: virtual ~EdgeChainRule();
        /** Gets the data for the edge chain rule: @link  NXOpen::EdgeChainRule   NXOpen::EdgeChainRule @endlink  
         <br>  Created in NX3.0.0.  <br>  
         <br> License requirements : gateway ("UG GATEWAY") */
        public: void GetData
        (
            NXOpen::Edge ** startEdge /** Start edge of edge chain. */,
            NXOpen::Edge ** endEdge /** End edge of edge chain. */,
            bool* isFromStart /** True: the chain starts from the start
                                                   point of the start edge */
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
