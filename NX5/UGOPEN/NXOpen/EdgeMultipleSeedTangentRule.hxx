#ifndef NXOpen_EDGEMULTIPLESEEDTANGENTRULE_HXX_INCLUDED
#define NXOpen_EDGEMULTIPLESEEDTANGENTRULE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     EdgeMultipleSeedTangentRule.ja
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
    class EdgeMultipleSeedTangentRule;
    class Edge;
    class SelectionIntentRule;
    /** Represents tangent edges with multiple seeds rule */
    class NXOPENCPPEXPORT EdgeMultipleSeedTangentRule : public SelectionIntentRule
    {
        public: explicit EdgeMultipleSeedTangentRule(void *ptr);
        /** Frees the object from memory. <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: virtual ~EdgeMultipleSeedTangentRule();
        /**  Gets the data of the edge multiple seed tangent rule.  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: void GetData
        (
            std::vector<NXOpen::Edge *> & seed_edges /** Seed edges*/,
            double* angle_tolerance /** Angle tolerance for tangent edges */,
            bool* has_same_convexity /** True: will only find tangnet edges
                                                              that has the same convexity*/
        );
    };
}
#undef EXPORTLIBRARY
#endif