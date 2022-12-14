#ifndef NXOpen_EDGEDUMBRULE_HXX_INCLUDED
#define NXOpen_EDGEDUMBRULE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     EdgeDumbRule.ja
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
    class EdgeDumbRule;
    class Edge;
    class SelectionIntentRule;
    class EdgeDumbRuleImpl;
    /** Represents an edge dumb rule */
    class NXOPENCPPEXPORT  EdgeDumbRule : public SelectionIntentRule
    {
        private: EdgeDumbRuleImpl * m_edgedumbrule_impl;
        public: explicit EdgeDumbRule(void *ptr);
        /** Frees the object from memory. <br> License requirements : None */
        public: virtual ~EdgeDumbRule();
        /** Gets the data of the edge dumb rule.  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: void GetData
        (
            std::vector<NXOpen::Edge *> & edges /** Edges which creates this rule*/
        );
    }; //lint !e1712 default constructor not defined for class  

}
#undef EXPORTLIBRARY
#endif
