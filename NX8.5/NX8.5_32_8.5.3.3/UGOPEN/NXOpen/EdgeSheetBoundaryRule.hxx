#ifndef NXOpen_EDGESHEETBOUNDARYRULE_HXX_INCLUDED
#define NXOpen_EDGESHEETBOUNDARYRULE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     EdgeSheetBoundaryRule.ja
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
    class EdgeSheetBoundaryRule;
    class Body;
    class SelectionIntentRule;
    class EdgeSheetBoundaryRuleImpl;
    /** Represents a @link  SelectionIntentRule   SelectionIntentRule @endlink  that collects boundary edges of a sheet body. 
     <br>  Created in NX3.0.0.  <br>  
    */
    class NXOPENCPPEXPORT  EdgeSheetBoundaryRule : public SelectionIntentRule
    {
        private: EdgeSheetBoundaryRuleImpl * m_edgesheetboundaryrule_impl;
        /// \cond NX_NO_DOC 
        public: explicit EdgeSheetBoundaryRule(void *ptr);
        /// \endcond 
        /** Frees the object from memory.
         <br>  Created in NX3.0.0.  <br>  
         <br> License requirements : None */
        public: virtual ~EdgeSheetBoundaryRule();
        /** Gets the data for the edge sheet boundary rule: @link  EdgeSheetBoundaryRule   EdgeSheetBoundaryRule @endlink  
         <br>  Created in NX3.0.0.  <br>  
         <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: void GetData
        (
            NXOpen::Body ** sheet /** Sheet body whose boundary edges are used to create this rule*/
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
