#ifndef NXOpen_BODYGROUPRULE_HXX_INCLUDED
#define NXOpen_BODYGROUPRULE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     BodyGroupRule.ja
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
    class BodyGroupRule;
    class Group;
    class SelectionIntentRule;
    class BodyGroupRuleImpl;
    /** Represents a body group rule */
    class NXOPENCPPEXPORT  BodyGroupRule : public SelectionIntentRule
    {
        private: BodyGroupRuleImpl * m_bodygrouprule_impl;
        public: explicit BodyGroupRule(void *ptr);
        /** Frees the object from memory. <br> License requirements : None */
        public: virtual ~BodyGroupRule();
        /** Gets the data of the body group rule.  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: void GetData
        (
            std::vector<NXOpen::Group *> & groups /** Groups which create this rule*/
        );
    }; //lint !e1712 default constructor not defined for class  

}
#undef EXPORTLIBRARY
#endif