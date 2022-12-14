#ifndef NXOpen_FACERIBFACESRULE_HXX_INCLUDED
#define NXOpen_FACERIBFACESRULE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     FaceRibFacesRule.ja
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
    class FaceRibFacesRule;
    class Face;
    class SelectionIntentRule;
    class FaceRibFacesRuleImpl;
    /** Represents a @link  SelectionIntentRule   SelectionIntentRule @endlink  that collects all rib faces. 
     <br>  Created in NX5.0.0.  <br>  
    */
    class NXOPENCPPEXPORT  FaceRibFacesRule : public SelectionIntentRule
    {
        private: FaceRibFacesRuleImpl * m_faceribfacesrule_impl;
        /// \cond NX_NO_DOC 
        public: explicit FaceRibFacesRule(void *ptr);
        /// \endcond 
        /** Frees the object from memory.
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : None */
        public: virtual ~FaceRibFacesRule();
        /** Gets the data for the rib faces rule: @link  FaceRibFacesRule   FaceRibFacesRule @endlink   @return  Faces which creates this rule
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : gateway ("UG GATEWAY") */
        public: NXOpen::Face * GetData
        (
        );
        /** Gets the data for the rib faces rule: @link  FaceRibFacesRule   FaceRibFacesRule @endlink   @return  Faces which creates this rule
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : gateway ("UG GATEWAY") */
        public: NXOpen::Face * GetDefiningData
        (
            bool* includeBoundaryBlends /** true if the rule is not to identify any blends at the boundary */,
            bool* travserseInteriorLoops /** true if interrior loops are to be processed. */
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
