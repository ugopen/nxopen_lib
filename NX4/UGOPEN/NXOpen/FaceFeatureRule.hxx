#ifndef NXOpen_FACEFEATURERULE_HXX_INCLUDED
#define NXOpen_FACEFEATURERULE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     FaceFeatureRule.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/SelectionIntentRule.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    class FaceFeatureRule;
    namespace Features
    {
        class Feature;
    }
    class SelectionIntentRule;
    /** Represents an face feature rule */
    class NXOPENCPPEXPORT FaceFeatureRule : public SelectionIntentRule
    {
        public: explicit FaceFeatureRule(void *ptr);
        /** Frees the object from memory. <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: virtual ~FaceFeatureRule();
        /** Gets the data of the face feature rule.  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: void GetData
        (
            std::vector<NXOpen::Features::Feature *> & features /** Fetures which create this rule*/
        );
    };
}
#undef EXPORTLIBRARY
#endif
