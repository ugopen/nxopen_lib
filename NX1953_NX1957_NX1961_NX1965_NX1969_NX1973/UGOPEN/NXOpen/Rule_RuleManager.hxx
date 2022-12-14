#ifndef NXOpen_RULE_RULEMANAGER_HXX_INCLUDED
#define NXOpen_RULE_RULEMANAGER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Rule_RuleManager.ja
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
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libruleopencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Rule
    {
        class RuleManager;
    }
    class Session;
    class Part;
    namespace Rule
    {
        class RuleInstance;
    }
    namespace Rule
    {
        class RuleInstanceCollection;
    }
    namespace Rule
    {
        class RuleManagerImpl;
        /** Represents an object that manages Rule application specific objects and preferences.
              <br> This is an abstract class, and cannot be instantiated.  <br> 
         <br>  Created in NX1899.0.0.  <br>  
        */
        class RULEOPENCPPEXPORT  RuleManager
        {
            private: RuleManagerImpl * m_rulemanager_impl;
            private: NXOpen::Session* m_owner;
            /// \cond NX_NO_DOC 
            public: explicit RuleManager(NXOpen::Session *owner);


            /// \endcond 
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            private: static RuleManager* theRuleManager;
            /** Returns the RuleManager object for the running session which serves as the 'gateway' class for the application API.  
                References to all other objects in this API are obtained either directly or indirectly via methods and properties on this class.  
                Platform Session should be initialized using 'GetSession' method from NXOpen API prior to this call.  
            */
            public: static RuleManager* GetRuleManager(NXOpen::Session *owner);
            public: ~RuleManager();
            /** Save created rule 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : features_modeling ("FEATURES MODELING") OR assemblies ("ASSEMBLIES MODULE") */
            public: void SaveRule
            (
                NXOpen::Rule::RuleInstance * ruleInstance /** ruleinstance */ ,
                const NXString & filename /** filename */ 
            );
            /** Save created rule 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : features_modeling ("FEATURES MODELING") OR assemblies ("ASSEMBLIES MODULE") */
            void SaveRule
            (
                NXOpen::Rule::RuleInstance * ruleInstance /** ruleinstance */ ,
                const char * filename /** filename */ 
            );
            /** Open existing rule 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : features_modeling ("FEATURES MODELING") OR assemblies ("ASSEMBLIES MODULE") */
            public: NXOpen::Rule::RuleInstance * OpenRuleInPart
            (
                const NXString & path /** path */ 
            );
            /** Open existing rule 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : features_modeling ("FEATURES MODELING") OR assemblies ("ASSEMBLIES MODULE") */
            NXOpen::Rule::RuleInstance * OpenRuleInPart
            (
                const char * path /** path */ 
            );
            /** Create a rule from the rule file  @return  Rule Instance 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : features_modeling ("FEATURES MODELING") OR assemblies ("ASSEMBLIES MODULE") */
            public: NXOpen::Rule::RuleInstance * InstantiateRule
            (
                const NXString & path /** file path of the rule */
            );
            /** Create a rule from the rule file  @return  Rule Instance 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : features_modeling ("FEATURES MODELING") OR assemblies ("ASSEMBLIES MODULE") */
            NXOpen::Rule::RuleInstance * InstantiateRule
            (
                const char * path /** file path of the rule */
            );
            /** Create rule object. 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : features_modeling ("FEATURES MODELING") OR assemblies ("ASSEMBLIES MODULE") */
            public: NXOpen::Rule::RuleInstance * CreateRule
            (
                NXOpen::Part * part /** part */ ,
                const NXString & applicaton /** applicaton */ ,
                const NXString & ruleName /** rulename */ 
            );
            /** Create rule object. 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : features_modeling ("FEATURES MODELING") OR assemblies ("ASSEMBLIES MODULE") */
            NXOpen::Rule::RuleInstance * CreateRule
            (
                NXOpen::Part * part /** part */ ,
                const char * applicaton /** applicaton */ ,
                const char * ruleName /** rulename */ 
            );


            /** Returns the RuleInstanceCollection instance belonging to this part 
             <br>  Created in NX1953.0.0.  <br>  
            */
            public: NXOpen::Rule::RuleInstanceCollection *RuleInstanceCollection();
        }; //lint !e1712 default constructor not defined for class  

    }
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
