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
#include <NXOpen/Callback.hxx>
#include <NXOpen/DisplayableObject.hxx>
#include <NXOpen/ScCollector.hxx>
#include <NXOpen/SelectionIntentRule.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    class ScCollector;
    class DisplayableObject;
    class SelectionIntentRule;
    class TaggedObject;
    class _ScCollectorBuilder;
    /** Sc Collector  <br> To create a new instance of this class, use @link ScCollectorCollection::CreateCollector ScCollectorCollection::CreateCollector@endlink  <br> */
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
            bool createRulesWoUpdate /** Flag to tell whether rules should be created wo_update */
        );
        /** Replace collector rules and specify negated entities.  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: void ReplaceRules
        (
            const std::vector<NXOpen::SelectionIntentRule *> & rules /** Selection intent rules. To create selection intent rules see
                                             documentation of @link ScRuleFactory ScRuleFactory@endlink 
                                             for more details. */,
            const std::vector<NXOpen::DisplayableObject *> & negatedEntities /** Entities in the rules that should be removed from the collector. */,
            bool createRulesWoUpdate /** Flag to tell whether rules should be created wo_update */
        );
        /** Destroy the ScCollector object  <br> License requirements : None */
        public: void Destroy
        (
        );
        /** Returns  the contents of a collector.  @return   <br> License requirements : None */
        public: std::vector<NXOpen::TaggedObject *> GetObjects
        (
        );
        /** Returns the rules of the a collector.  <br> License requirements : None */
        public: void GetRules
        (
            std::vector<NXOpen::SelectionIntentRule *> & rules /** Selection intent rules. */
        );
        /** Sets inter-part status <br> License requirements : None */
        public: void SetInterpart
        (
            bool interpart /** True to set collector as interpart*/
        );
        /** Remove collector rule  <br> License requirements : None */
        public: void RemoveRule
        (
            int ruleIndex /** index (starting from 0) of the rule to be removed */
        );
    };
}
#undef EXPORTLIBRARY
#endif
