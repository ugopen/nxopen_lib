#ifndef NXOpen_FACEANDADJACENTFACESRULE_HXX_INCLUDED
#define NXOpen_FACEANDADJACENTFACESRULE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     FaceAndAdjacentFacesRule.ja
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
namespace NXOpen
{
    class FaceAndAdjacentFacesRule;
    class Face;
    class SelectionIntentRule;
    class FaceAndAdjacentFacesRuleImpl;
    /** Represents a face and adjacent faces rule */
    class NXOPENCPPEXPORT  FaceAndAdjacentFacesRule : public SelectionIntentRule
    {
        private: FaceAndAdjacentFacesRuleImpl * m_faceandadjacentfacesrule_impl;
        public: explicit FaceAndAdjacentFacesRule(void *ptr);
        /** Frees the object from memory. <br> License requirements : None */
        public: virtual ~FaceAndAdjacentFacesRule();
        /** Gets the data of the face and adjacent faces rule.  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: void GetData
        (
            std::vector<NXOpen::Face *> & faces /** Faces which create this rule*/
        );
    }; //lint !e1712 default constructor not defined for class  

}
#undef EXPORTLIBRARY
#endif