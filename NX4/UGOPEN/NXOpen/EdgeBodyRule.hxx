#ifndef NXOpen_EDGEBODYRULE_HXX_INCLUDED
#define NXOpen_EDGEBODYRULE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     EdgeBodyRule.ja
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
    class EdgeBodyRule;
    class Body;
    class SelectionIntentRule;
    /** Represents an edge body rule */
    class NXOPENCPPEXPORT EdgeBodyRule : public SelectionIntentRule
    {
        public: explicit EdgeBodyRule(void *ptr);
        /** Frees the object from memory. <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: virtual ~EdgeBodyRule();
        /** Gets the data of the edge body rule.  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: void GetData
        (
            NXOpen::Body ** body /** Body whose edges are uded to create this rule*/
        );
    };
}
#undef EXPORTLIBRARY
#endif
