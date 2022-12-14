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
#ifdef _MSC_VER
#pragma once
#endif

#include <NXOpen/NXDeprecation.hxx>
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/DisplayableObject.hxx>
#include <NXOpen/SelectionIntentRule.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    class ScCollector;
    class DisplayableObject;
    class SelectionIntentRule;
    class TaggedObject;
    /** Tokens used to create different evaluation filters on ScCollector */
    enum ScEvaluationFiltertype
    {
        ScEvaluationFiltertypeSleepyEntity/** sleepy entity */  = 1,
        ScEvaluationFiltertypeLaminarEdge/** laminar edge */ 
    };

    /** Defines entity types allowed */
    enum ScCollectorAllowTypes
    {
        ScCollectorAllowTypesUninitialized/** This is uninitialized state. Do not use this.*/,
        ScCollectorAllowTypesOnlyCurves/** Allow only curves in ScCollector*/,
        ScCollectorAllowTypesOnlyPoints/** Allow only points in ScCollector*/,
        ScCollectorAllowTypesCurvesAndPoints/** Allow both points and curves in ScCollector*/
    };

    class _ScCollectorBuilder;
    class ScCollectorImpl;
    /** Represents a collector 
     <br> 
    ScCollector consists of collection of either faces, bodies, edges, curves or a mixed collection of these entities. 
    The collection is defined by selection intent rules. Please refer documentation of @link ScRuleFactory ScRuleFactory@endlink 
    for more details on available selection intent rules. 
    @link ScRuleFactory ScRuleFactory@endlink .
     <br> 
     <br> To create a new instance of this class, use @link NXOpen::ScCollectorCollection::CreateCollector  NXOpen::ScCollectorCollection::CreateCollector @endlink  <br> 
     <br>  Created in NX4.0.0.  <br>  
    */
    class NXOPENCPPEXPORT  ScCollector : public NXOpen::DisplayableObject
    {
        private: ScCollectorImpl * m_sccollector_impl;
        private: friend class  _ScCollectorBuilder;
        protected: ScCollector();
        public: ~ScCollector();
        /** Replace collector rules. 
         <br>  Created in NX4.0.0.  <br>  
         <br> License requirements : gateway ("UG GATEWAY") */
        public: void ReplaceRules
        (
            const std::vector<NXOpen::SelectionIntentRule *> & rules /** Selection intent rules. To create selection intent rules see
                                             documentation of @link ScRuleFactory ScRuleFactory@endlink 
                                             for more details. */,
            bool createRulesWoUpdate /** Flag to tell whether rules should be created wo_update */
        );
        /** Replace collector rules and specify negated entities. 
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : gateway ("UG GATEWAY") */
        public: void ReplaceRules
        (
            const std::vector<NXOpen::SelectionIntentRule *> & rules /** Selection intent rules. To create selection intent rules see
                                             documentation of @link ScRuleFactory ScRuleFactory@endlink 
                                             for more details. */,
            const std::vector<NXOpen::DisplayableObject *> & negatedEntities /** Entities in the rules that should be removed from the collector. */,
            bool createRulesWoUpdate /** Flag to tell whether rules should be created wo_update */
        );
        /** Destroy the ScCollector object 
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : None */
        public: void Destroy
        (
        );
        /** Returns the contents of a collector.  @return  
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        public: std::vector<NXOpen::TaggedObject *> GetObjects
        (
        );
        /** Returns the rules of the a collector. 
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        public: void GetRules
        (
            std::vector<NXOpen::SelectionIntentRule *> & rules /** Selection intent rules. */
        );
        /** Sets inter-part status
             <br> 
            This function sets the value of interpart flag on ScCollector. Error will be raised while setting this option on ScCollector in following conditions:
            (1) ScCollector is NULL.
            (2) ScCollector object is not of SC_collector class.
            (3) ScCollector is of hybrid part option.
            (4) Multi-component option is already set on ScCollector.
             <br> 
            
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        public: void SetInterpart
        (
            bool interpart /** True to set collector as interpart*/
        );
        /** Remove collector rule 
         <br>  Created in NX7.0.0.  <br>  
         <br> License requirements : None */
        public: void RemoveRule
        (
            int ruleIndex /** index (starting from 0) of the rule to be removed */
        );
        /** Remove collector rules 
         <br>  Created in NX8.0.0.  <br>  
         <br> License requirements : None */
        public: void RemoveRules
        (
            const std::vector<NXOpen::SelectionIntentRule *> & rules /** Selection intent rules to be removed */
        );
        /** Copy collector object 
         <br>  Created in NX8.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::ScCollector * CopyCollector
        (
        );
        /** Gets the option set on ScCollector for collection from multiple components.
             <br> 
            A multi-component ScCollector can have collection from multiple components i.e., multiple parts or multiple instances of same part or both.
             <br>  
             @return  Multi-component option set on ScCollector 
         <br>  Created in NX9.0.0.  <br>  
         <br> License requirements : None */
        public: bool GetMultiComponent
        (
        );
        /** Sets the true option on ScCollector for collection from multiple components.
             <br> 
            A multi-component ScCollector can have collection from multiple components i.e., multiple parts or multiple instances of same part or both.
            This method should be used only if such collection is desired.
            Error will be raised while setting this option on ScCollector in following conditions:
            (1) Inter-part option is already set on ScCollector.
             <br>  
            
         <br>  Created in NX9.0.0.  <br>  
         <br> License requirements : None */
        public: void SetMultiComponent
        (
        );
        /** Gets the option set on ScCollector for collection in non-feature mode.
             <br> 
            An ScCollector in non-feature mode does not reference the feature data of the part from which the collection is done.
             <br> 
             @return  Non-feature mode set on ScCollector 
         <br>  Created in NX9.0.0.  <br>  
         <br> License requirements : None */
        public: bool GetNonFeatureMode
        (
        );
        /** Sets the true option on ScCollector for collection in non-feature mode.
             <br> 
            An ScCollector in non-feature mode does not reference the feature data of the part from which the collection is done.
            The option should be set on an empty ScCollector only.
            For a non-empty ScCollector, setting this option will raise error in following conditions:
            (1) ScCollector is referencing feature data and non-feature mode is set true.
            (2) ScCollector is not referencing feature data and non-feature mode is set false.
             <br> 
            
         <br>  Created in NX9.0.0.  <br>  
         <br> License requirements : None */
        public: void SetNonFeatureMode
        (
        );
        /** Returns the contents of a collector which are guaranteed to be sorted.  @return  
         <br>  Created in NX11.0.0.  <br>  
         <br> License requirements : None */
        public: std::vector<NXOpen::TaggedObject *> GetObjectsSortedById
        (
        );
        /** Sets the evaluation filter on ScCollector 
         <br>  Created in NX11.0.0.  <br>  
         <br> License requirements : None */
        public: void AddEvaluationFilter
        (
            NXOpen::ScEvaluationFiltertype filterType /** Enum Value*/
        );
        /** Removes the evaluation filter on ScCollector 
         <br>  Created in NX11.0.0.  <br>  
         <br> License requirements : None */
        public: void RemoveEvaluationFilter
        (
            NXOpen::ScEvaluationFiltertype filterType /** Enum Value*/
        );
        /** Checks whether the evaluation filter is present on ScCollector 
         <br>  Created in NX11.0.0.  <br>  
         <br> License requirements : None */
        public: bool IsEvaluationFilterEnabled
        (
            NXOpen::ScEvaluationFiltertype filterType /** Enum Value*/
        );
        /** Sets whether to allow reference curves or not in the ScCollector 
         <br>  Created in NX11.0.2.  <br>  
         <br> License requirements : None */
        public: void SetAllowRefCurves
        (
            bool allowRefCurves /** True to allow reference curves in ScCollector */
        );
        /** Get the allowed wireframe type(viz. curve, point or both) on the curve ScCollector  @return  Allowed entity types. 
         <br>  Created in NX1847.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::ScCollectorAllowTypes GetAllowedWireframeType
        (
        );
        /** Set the allowed wireframe type(viz. curve, point or both) on the curve ScCollector 
         <br>  Created in NX1847.0.0.  <br>  
         <br> License requirements : None */
        public: void SetAllowedWireframeType
        (
            NXOpen::ScCollectorAllowTypes allowedEntityTypes /** Allowed entity types. */
        );
        /** Deletes the references of missing parents from collector 
         <br>  Created in NX1847.0.0.  <br>  
         <br> License requirements : None */
        public: void RemoveMissingParents
        (
        );
    };
}

#ifdef _MSC_VER
#pragma warning(pop)
#endif
#ifdef __GNUC__
#ifndef NX_NO_GCC_DEPRECATION_WARNINGS
#pragma GCC diagnostic warning "-Wdeprecated-declarations"
#endif
#endif

#undef EXPORTLIBRARY
#endif
