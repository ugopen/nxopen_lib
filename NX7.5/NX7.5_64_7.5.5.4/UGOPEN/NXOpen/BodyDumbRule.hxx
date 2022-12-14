#ifndef NXOpen_BODYDUMBRULE_HXX_INCLUDED
#define NXOpen_BODYDUMBRULE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     BodyDumbRule.ja
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
    class BodyDumbRule;
    class Body;
    class SelectionIntentRule;
    class BodyDumbRuleImpl;
    /** Represents a body dumb rule */
    class NXOPENCPPEXPORT  BodyDumbRule : public SelectionIntentRule
    {
        private: BodyDumbRuleImpl * m_bodydumbrule_impl;
        public: explicit BodyDumbRule(void *ptr);
        /** Frees the object from memory. <br> License requirements : None */
        public: virtual ~BodyDumbRule();
        /** Gets the data of the body dumb rule.  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: void GetData
        (
            std::vector<NXOpen::Body *> & bodies /** Bodies which create this rule*/
        );
    }; //lint !e1712 default constructor not defined for class  

}
#undef EXPORTLIBRARY
#endif
