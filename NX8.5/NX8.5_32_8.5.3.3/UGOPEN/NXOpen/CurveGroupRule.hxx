#ifndef NXOpen_CURVEGROUPRULE_HXX_INCLUDED
#define NXOpen_CURVEGROUPRULE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CurveGroupRule.ja
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
    class CurveGroupRule;
    class Group;
    class SelectionIntentRule;
    class CurveGroupRuleImpl;
    /** Represents a @link  SelectionIntentRule   SelectionIntentRule @endlink  that collects all curves of a group. 
     <br>  Created in NX7.5.0.  <br>  
    */
    class NXOPENCPPEXPORT  CurveGroupRule : public SelectionIntentRule
    {
        private: CurveGroupRuleImpl * m_curvegrouprule_impl;
        /// \cond NX_NO_DOC 
        public: explicit CurveGroupRule(void *ptr);
        /// \endcond 
        /** Frees the object from memory.
         <br>  Created in NX7.5.0.  <br>  
         <br> License requirements : None */
        public: virtual ~CurveGroupRule();
        /** Gets the data for the curve group rule: @link  CurveGroupRule   CurveGroupRule @endlink  
         <br>  Created in NX7.5.0.  <br>  
         <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: void GetData
        (
            std::vector<NXOpen::Group *> & groups /** Groups whose curves are used to create this rule*/
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
