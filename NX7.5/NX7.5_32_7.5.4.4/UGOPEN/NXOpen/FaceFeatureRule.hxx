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
    class FaceFeatureRule;
    namespace Features
    {
        class Feature;
    }
    class SelectionIntentRule;
    class FaceFeatureRuleImpl;
    /** Represents an face feature rule */
    class NXOPENCPPEXPORT  FaceFeatureRule : public SelectionIntentRule
    {
        private: FaceFeatureRuleImpl * m_facefeaturerule_impl;
        public: explicit FaceFeatureRule(void *ptr);
        /** Frees the object from memory. <br> License requirements : None */
        public: virtual ~FaceFeatureRule();
        /** Gets the data of the face feature rule.  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: void GetData
        (
            std::vector<NXOpen::Features::Feature *> & features /** Fetures which create this rule*/
        );
    }; //lint !e1712 default constructor not defined for class  

}
#undef EXPORTLIBRARY
#endif