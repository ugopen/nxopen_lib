#ifndef NXOpen_FACEBOSSPOCKETFACESRULE_HXX_INCLUDED
#define NXOpen_FACEBOSSPOCKETFACESRULE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     FaceBossPocketFacesRule.ja
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
    class FaceBossPocketFacesRule;
    class Face;
    class SelectionIntentRule;
    /** Represents a boss pocket faces rule */
    class NXOPENCPPEXPORT FaceBossPocketFacesRule : public SelectionIntentRule
    {
        public: explicit FaceBossPocketFacesRule(void *ptr);
        /** Frees the object from memory. <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: virtual ~FaceBossPocketFacesRule();
        /** Gets the data of the boss pocket faces rule.  @return  Faces which creates this rule <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: NXOpen::Face * GetData
        (
        );
        /** Gets the data of the boss pocket faces rule.  @return  Faces which creates this rule <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: NXOpen::Face * GetDefiningData
        (
            bool* includeBoundaryBlends /** true if the rule is not to identify any blends at the boundary */
        );
    };
}
#undef EXPORTLIBRARY
#endif
