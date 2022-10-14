#ifndef NXOpen_TANGENTFACETSRULE_HXX_INCLUDED
#define NXOpen_TANGENTFACETSRULE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     TangentFacetsRule.ja
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
#include <NXOpen/FacetSelectionRule.hxx>
#include <NXOpen/FacetSelectionRule.hxx>
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
    class TangentFacetsRule;
    class FacetSelectionRule;
    class IFacet;
    class TangentFacetsRuleImpl;
    /**  @brief Represents a @link  NXOpen::TangentFacetsRule   NXOpen::TangentFacetsRule @endlink  that collects facets maintaining the tangency within given tolerance. 

     
         
        This rule chains to add all neighbouring facets of seed (and the neighbour-neighbours) which satisfy the tangency condition. 
     <br>  Created in NX12.0.2.  <br>  
    */
    class NXOPENCPPEXPORT  TangentFacetsRule : public NXOpen::FacetSelectionRule
    {
        private: TangentFacetsRuleImpl * m_tangentfacetsrule_impl;
        /// \cond NX_NO_DOC 
        public: explicit TangentFacetsRule(void *ptr);
        /// \endcond 
        /** Frees the object from memory.
         <br>  Created in NX12.0.2.  <br>  
         <br> License requirements : None */
        public: virtual ~TangentFacetsRule();
        /** Gets the data for the tangent facets rule: @link  NXOpen::TangentFacetsRule   NXOpen::TangentFacetsRule @endlink   @return  seed facet for tangent facets collection 
         <br>  Created in NX12.0.2.  <br>  
         <br> License requirements : gateway ("UG GATEWAY") */
        public: NXOpen::IFacet * GetData
        (
            double* tangencyTolerance /** tolerance to expand facet selection */
        );
        /** Update the tangency tolerance for the tangent facets rule: @link  NXOpen::TangentFacetsRule   NXOpen::TangentFacetsRule @endlink  
         <br>  Created in NX12.0.2.  <br>  
         <br> License requirements : gateway ("UG GATEWAY") */
        public: void UpdateTangencyTolerance
        (
            double tangencyTolerance /** update the primitive shape tolerance factor */
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