#ifndef NXOpen_EDGEINTERSECTRULE_HXX_INCLUDED
#define NXOpen_EDGEINTERSECTRULE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     EdgeIntersectRule.ja
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
    class EdgeIntersectRule;
    class Face;
    class SelectionIntentRule;
    class EdgeIntersectRuleImpl;
    /** Represents a @link  SelectionIntentRule   SelectionIntentRule @endlink  that collects all intersection edges between a set of faces. 
     <br>  Created in NX3.0.0.  <br>  
    */
    class NXOPENCPPEXPORT  EdgeIntersectRule : public SelectionIntentRule
    {
        private: EdgeIntersectRuleImpl * m_edgeintersectrule_impl;
        /// \cond NX_NO_DOC 
        public: explicit EdgeIntersectRule(void *ptr);
        /// \endcond 
        /** Frees the object from memory.
         <br>  Created in NX3.0.0.  <br>  
         <br> License requirements : None */
        public: virtual ~EdgeIntersectRule();
        /** Gets the data for the edge intersect rule: @link  EdgeIntersectRule   EdgeIntersectRule @endlink  
         <br>  Created in NX3.0.0.  <br>  
         <br> License requirements : gateway ("UG GATEWAY") */
        public: void GetData
        (
            std::vector<NXOpen::Face *> & facesOfFeatures1 /** Faces of feature1 whose boundary edges are used to create this rule.*/,
            std::vector<NXOpen::Face *> & facesOfFeatures2 /** Faces of feature2 whose boundary edges are used to create this rule.*/
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
