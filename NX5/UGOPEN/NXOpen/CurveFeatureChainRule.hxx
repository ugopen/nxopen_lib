#ifndef NXOpen_CURVEFEATURECHAINRULE_HXX_INCLUDED
#define NXOpen_CURVEFEATURECHAINRULE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CurveFeatureChainRule.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/SelectionIntentRule.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    class CurveFeatureChainRule;
    class Curve;
    namespace Features
    {
        class Feature;
    }
    class SelectionIntentRule;
    /** Represents a curve feature chain rule */
    class NXOPENCPPEXPORT CurveFeatureChainRule : public SelectionIntentRule
    {
        public: explicit CurveFeatureChainRule(void *ptr);
        /** Frees the object from memory. <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: virtual ~CurveFeatureChainRule();
        /** Gets the data of the curve feature chain rule.  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: void GetData
        (
            std::vector<NXOpen::Features::Feature *> & features /** Features whose curves are used to create this rule */,
            NXOpen::Curve ** seed_curve /** Seed curve*/,
            NXOpen::Curve ** end_curve /** End Curve. It can be null (Nothing)*/,
            bool* from_seed_start /** True: the chain starts from the start
                                                 point of the seed curve */,
            double* gap_tolerance /** Gap tolerance*/
        );
    };
}
#undef EXPORTLIBRARY
#endif