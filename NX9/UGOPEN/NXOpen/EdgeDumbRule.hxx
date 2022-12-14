#ifndef NXOpen_EDGEDUMBRULE_HXX_INCLUDED
#define NXOpen_EDGEDUMBRULE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     EdgeDumbRule.ja
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
    class EdgeDumbRule;
    class Edge;
    class SelectionIntentRule;
    class EdgeDumbRuleImpl;
    /** Represents a @link  SelectionIntentRule   SelectionIntentRule @endlink  that collects edges without any intent i.e. as if collected with Single Curve rule. 
     <br>  Created in NX3.0.0.  <br>  
    */
    class NXOPENCPPEXPORT  EdgeDumbRule : public SelectionIntentRule
    {
        private: EdgeDumbRuleImpl * m_edgedumbrule_impl;
        /// \cond NX_NO_DOC 
        public: explicit EdgeDumbRule(void *ptr);
        /// \endcond 
        /** Frees the object from memory.
         <br>  Created in NX3.0.0.  <br>  
         <br> License requirements : None */
        public: virtual ~EdgeDumbRule();
        /** Gets the data for the edge dumb rule: @link  EdgeDumbRule   EdgeDumbRule @endlink  
         <br>  Created in NX3.0.0.  <br>  
         <br> License requirements : gateway ("UG GATEWAY") */
        public: void GetData
        (
            std::vector<NXOpen::Edge *> & edges /** Edges which creates edge dumb rule*/
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
