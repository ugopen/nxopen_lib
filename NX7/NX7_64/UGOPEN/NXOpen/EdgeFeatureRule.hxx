#ifndef NXOpen_EDGEFEATURERULE_HXX_INCLUDED
#define NXOpen_EDGEFEATURERULE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     EdgeFeatureRule.ja
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
    class EdgeFeatureRule;
    namespace Features
    {
        class Feature;
    }
    class SelectionIntentRule;
    /** Represents an edge feature rule */
    class NXOPENCPPEXPORT EdgeFeatureRule : public SelectionIntentRule
    {
        public: explicit EdgeFeatureRule(void *ptr);
        /** Frees the object from memory. <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: virtual ~EdgeFeatureRule();
        /**  Gets the data of the edge feature rule. <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: void GetData
        (
            std::vector<NXOpen::Features::Feature *> & features /** Features whose edges are used to create edge feature rule. */
        );
    };
}
#undef EXPORTLIBRARY
#endif