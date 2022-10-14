#ifndef NXOpen_CURVEFEATURETANGENTRULE_HXX_INCLUDED
#define NXOpen_CURVEFEATURETANGENTRULE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CurveFeatureTangentRule.ja
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
    class CurveFeatureTangentRule;
    class Curve;
    namespace Features
    {
        class Feature;
    }
    class SelectionIntentRule;
    class CurveFeatureTangentRuleImpl;
    /** Represents a @link  SelectionIntentRule   SelectionIntentRule @endlink  that collects tangent connected curves from the feature of the seed. 
     <br>  Created in NX3.0.0.  <br>  
    */
    class NXOPENCPPEXPORT  CurveFeatureTangentRule : public SelectionIntentRule
    {
        private: CurveFeatureTangentRuleImpl * m_curvefeaturetangentrule_impl;
        /// \cond NX_NO_DOC 
        public: explicit CurveFeatureTangentRule(void *ptr);
        /// \endcond 
        /** Frees the object from memory.
         <br>  Created in NX3.0.0.  <br>  
         <br> License requirements : None */
        public: virtual ~CurveFeatureTangentRule();
        /** Gets the data for the curve feature tangent rule: @link  CurveFeatureTangentRule   CurveFeatureTangentRule @endlink  
         <br>  Created in NX3.0.0.  <br>  
         <br> License requirements : gateway ("UG GATEWAY") */
        public: void GetData
        (
            std::vector<NXOpen::Features::Feature *> & features /** Feaures whose tangent curves are used to create this rule*/,
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