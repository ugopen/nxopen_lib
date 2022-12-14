#ifndef NXOpen_RULE_NODEOUTPUT_HXX_INCLUDED
#define NXOpen_RULE_NODEOUTPUT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Rule_NodeOutput.ja
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
        class NodeOutput;
    }
    class NXObject;
    namespace Rule
    {
        class _NodeOutputBuilder;
        class NodeOutputImpl;
        /** Represents a @link NXOpen::Rule::NodeOutput NXOpen::Rule::NodeOutput@endlink   <br> This is a node output class.  <br> 
         <br>  Created in NX1953.0.0.  <br>  
        */
        class RULEOPENCPPEXPORT  NodeOutput : public NXOpen::NXObject
        {
            private: NodeOutputImpl * m_nodeoutput_impl;
            private: friend class  _NodeOutputBuilder;
            protected: NodeOutput();
            public: ~NodeOutput();
            /** Get the integer output 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: void GetIntOutput
            (
                const NXString & portId /** portid */ ,
                std::vector<int> & output /** output */ 
            );
            /** Get the integer output 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            void GetIntOutput
            (
                const char * portId /** portid */ ,
                std::vector<int> & output /** output */ 
            );
            /** Get the double output 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: void GetDoubleOutput
            (
                const NXString & portId /** portid */ ,
                std::vector<double> & output /** output */ 
            );
            /** Get the double output 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            void GetDoubleOutput
            (
                const char * portId /** portid */ ,
                std::vector<double> & output /** output */ 
            );
            /** Get the bool output 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: void GetBoolOutput
            (
                const NXString & portId /** portid */ ,
                std::vector<bool> & output /** output */ 
            );
            /** Get the bool output 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            void GetBoolOutput
            (
                const char * portId /** portid */ ,
                std::vector<bool> & output /** output */ 
            );
            /** Get the NX Object output 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: void GetNXObjectOutput
            (
                const NXString & portId /** portid */ ,
                std::vector<NXOpen::NXObject *> & output /** output */ 
            );
            /** Get the NX Object output 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            void GetNXObjectOutput
            (
                const char * portId /** portid */ ,
                std::vector<NXOpen::NXObject *> & output /** output */ 
            );
            /** Get the string output 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: void GetStringOutput
            (
                const NXString & portId /** portid */ ,
                std::vector<NXString> & output /** output */ 
            );
            /** Get the string output 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            void GetStringOutput
            (
                const char * portId /** portid */ ,
                std::vector<NXString> & output /** output */ 
            );
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
