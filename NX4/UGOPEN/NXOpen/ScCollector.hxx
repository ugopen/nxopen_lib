#ifndef NXOpen_SCCOLLECTOR_HXX_INCLUDED
#define NXOpen_SCCOLLECTOR_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     ScCollector.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/DisplayableObject.hxx>
#include <NXOpen/SelectionIntentRule.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    class ScCollector;
    class DisplayableObject;
    class SelectionIntentRule;
    class _ScCollectorBuilder;
    /** Sc Collector */
    class NXOPENCPPEXPORT ScCollector : public DisplayableObject
    {
        private: friend class  _ScCollectorBuilder;
        protected: ScCollector();
        /** Replace collector rules.  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: void ReplaceRules
        (
            const std::vector<NXOpen::SelectionIntentRule *> & rules /** Selection intent rules. To create selection intent rules see
                                             documentation of @link ScRuleFactory ScRuleFactory@endlink 
                                             for more details. */,
            bool create_rules_wo_update /** Flag to tell whether rules should be created wo_update */
        );
    };
}
#undef EXPORTLIBRARY
#endif