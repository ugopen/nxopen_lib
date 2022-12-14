#ifndef NXOpen_EDGEVERTEXRULE_HXX_INCLUDED
#define NXOpen_EDGEVERTEXRULE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     EdgeVertexRule.ja
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
    class EdgeVertexRule;
    class Edge;
    class SelectionIntentRule;
    class EdgeVertexRuleImpl;
    /** Represents a @link  SelectionIntentRule   SelectionIntentRule @endlink  that collects the vertex edge and and its adjacent edges. 
     <br>  Created in NX4.0.0.  <br>  
    */
    class NXOPENCPPEXPORT  EdgeVertexRule : public SelectionIntentRule
    {
        private: EdgeVertexRuleImpl * m_edgevertexrule_impl;
        /// \cond NX_NO_DOC 
        public: explicit EdgeVertexRule(void *ptr);
        /// \endcond 
        /** Frees the object from memory.
         <br>  Created in NX4.0.0.  <br>  
         <br> License requirements : None */
        public: virtual ~EdgeVertexRule();
        /** Gets the data for the edge vertex rule: @link  EdgeVertexRule   EdgeVertexRule @endlink  
         <br>  Created in NX4.0.0.  <br>  
         <br> License requirements : gateway ("UG GATEWAY") */
        public: void GetData
        (
            NXOpen::Edge ** startEdge /** Start edge of edge vertex rule*/,
            bool* isFromStart /** True: the tangent starts from the start
                                                     point of the start edge if end edge is provided*/
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
