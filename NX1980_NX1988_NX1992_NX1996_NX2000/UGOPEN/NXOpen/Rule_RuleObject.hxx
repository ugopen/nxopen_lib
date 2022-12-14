#ifndef NXOpen_RULE_RULEOBJECT_HXX_INCLUDED
#define NXOpen_RULE_RULEOBJECT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Rule_RuleObject.ja
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
#include <NXOpen/NXObject.hxx>
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
        class RuleObject;
    }
    class NXObject;
    namespace Rule
    {
        class Connector;
    }
    namespace Rule
    {
        class Node;
    }
    namespace Rule
    {
        class NodeCollection;
    }
    namespace Rule
    {
        class _RuleObjectBuilder;
        class RuleObjectImpl;
        /** Represents a @link NXOpen::Rule::RuleObject NXOpen::Rule::RuleObject@endlink   <br> This is a rule object class.  <br> 
         <br>  Created in NX1953.0.0.  <br>  
        */
        class RULEOPENCPPEXPORT  RuleObject : public NXOpen::NXObject
        {
            private: RuleObjectImpl * m_ruleobject_impl;
            private: friend class  _RuleObjectBuilder;
            protected: RuleObject();
            public: ~RuleObject();
            /** Connect the nodes 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Rule::Connector * ConnectNode
            (
                NXOpen::Rule::Node * startNode /** startnode */ ,
                const NXString & fromPort /** fromport */ ,
                NXOpen::Rule::Node * endNode /** endnode */ ,
                const NXString & toPort /** toport */ 
            );
            /** Connect the nodes 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            NXOpen::Rule::Connector * ConnectNode
            (
                NXOpen::Rule::Node * startNode /** startnode */ ,
                const char * fromPort /** fromport */ ,
                NXOpen::Rule::Node * endNode /** endnode */ ,
                const char * toPort /** toport */ 
            );
            /** Create rule node  @return   
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Rule::Node * CreateNode
            (
                const NXString & applicationName /** applicationname */ ,
                const NXString & objectName /** objectname */ 
            );
            /** Create rule node  @return   
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            NXOpen::Rule::Node * CreateNode
            (
                const char * applicationName /** applicationname */ ,
                const char * objectName /** objectname */ 
            );
            /** Create snippet rule node  @return   
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Rule::Node * CreateSnippetNode
            (
                const NXString & snippetRuleFile /** snippetrulefile */ 
            );
            /** Create snippet rule node  @return   
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            NXOpen::Rule::Node * CreateSnippetNode
            (
                const char * snippetRuleFile /** snippetrulefile */ 
            );
            /** Destroy the rule. 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: void Destroy
            (
            );
            /**Returns  the rule description. 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: NXString Description
            (
            );
            /**Sets  the rule description. 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: void SetDescription
            (
                const NXString & description /** description */ 
            );
            /**Sets  the rule description. 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            void SetDescription
            (
                const char * description /** description */ 
            );
            /**Returns  the rule object name. 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: NXString RuleName
            (
            );
            /**Sets  the rule object name. 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: void SetRuleName
            (
                const NXString & name /** name */ 
            );
            /**Sets  the rule object name. 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            void SetRuleName
            (
                const char * name /** name */ 
            );
            /** Set password of the rule. 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: void SetPassword
            (
                const NXString & password /** rule password */
            );
            /** Set password of the rule. 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            void SetPassword
            (
                const char * password /** rule password */
            );
            /** Unlock the password protected rule. 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: void Unlock
            (
                const NXString & password /** rule password */
            );
            /** Unlock the password protected rule. 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            void Unlock
            (
                const char * password /** rule password */
            );
            /** Reset the lock status of the password protected rule. 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: void Lock
            (
            );
            /** Returns the library rule path of given rule, if rule is not linked with library rule then path will be empty.  @return  library rule path 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : features_modeling ("FEATURES MODELING") OR assemblies ("ASSEMBLIES MODULE") */
            public: NXString GetLibraryRulePath
            (
            );
            /** Removes the library link of the rule. 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : features_modeling ("FEATURES MODELING") OR assemblies ("ASSEMBLIES MODULE") */
            public: void RemoveLibraryLink
            (
            );


            /** Returns the RuleNodeCollection instance belonging to this rule object 
             <br>  Created in NX1953.0.0.  <br>  
            */
            public: NXOpen::Rule::NodeCollection *RuleNodeCollection();
        };
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
