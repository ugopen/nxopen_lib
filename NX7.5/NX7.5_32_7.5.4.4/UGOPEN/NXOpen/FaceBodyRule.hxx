#ifndef NXOpen_FACEBODYRULE_HXX_INCLUDED
#define NXOpen_FACEBODYRULE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     FaceBodyRule.ja
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
    class FaceBodyRule;
    class Body;
    class SelectionIntentRule;
    class FaceBodyRuleImpl;
    /** Represents an face body rule */
    class NXOPENCPPEXPORT  FaceBodyRule : public SelectionIntentRule
    {
        private: FaceBodyRuleImpl * m_facebodyrule_impl;
        public: explicit FaceBodyRule(void *ptr);
        /** Frees the object from memory. <br> License requirements : None */
        public: virtual ~FaceBodyRule();
        /** Gets the data of the face body rule.  @return  Body which creates this rule <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: NXOpen::Body * GetBodyData
        (
        );
    }; //lint !e1712 default constructor not defined for class  

}
#undef EXPORTLIBRARY
#endif