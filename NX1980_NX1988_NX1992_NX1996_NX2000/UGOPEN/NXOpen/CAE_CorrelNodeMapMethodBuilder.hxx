#ifndef NXOpen_CAE_CORRELNODEMAPMETHODBUILDER_HXX_INCLUDED
#define NXOpen_CAE_CORRELNODEMAPMETHODBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_CorrelNodeMapMethodBuilder.ja
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
#include <NXOpen/Builder.hxx>
#include <NXOpen/libnxopencpp_cae_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace CAE
    {
        class CorrelNodeMapMethodBuilder;
    }
    class Builder;
    namespace CAE
    {
        class _CorrelNodeMapMethodBuilderBuilder;
        class CorrelNodeMapMethodBuilderImpl;
        /** Represents the correl node map method builder  <br> To create a new instance of this class, use @link NXOpen::CAE::CorrelNodeMap::CreateMethodBuilder  NXOpen::CAE::CorrelNodeMap::CreateMethodBuilder @endlink  <br> 
         <br>  Created in NX1980.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  CorrelNodeMapMethodBuilder : public NXOpen::Builder
        {
            /** Method type */
            public: enum Type
            {
                TypeProximity/** proximity */ ,
                TypeIdentifier/** identifier */ ,
                TypeManual/** manual */ 
            };

            /** ID matching type */
            public: enum MatchingBy
            {
                MatchingByLabel/** label */ ,
                MatchingByName/** name */ 
            };

            private: CorrelNodeMapMethodBuilderImpl * m_correlnodemapmethodbuilder_impl;
            private: friend class  _CorrelNodeMapMethodBuilderBuilder;
            protected: CorrelNodeMapMethodBuilder();
            public: ~CorrelNodeMapMethodBuilder();
            /**Returns  the method type 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::CorrelNodeMapMethodBuilder::Type MethodType
            (
            );
            /**Sets  the method type 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : nx_correl_base ("FE Correlation") */
            public: void SetMethodType
            (
                NXOpen::CAE::CorrelNodeMapMethodBuilder::Type type /** type */ 
            );
            /**Returns  the name 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXString Name
            (
            );
            /**Sets  the name 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : nx_correl_base ("FE Correlation") */
            public: void SetName
            (
                const NXString & name /** name */ 
            );
            /**Sets  the name 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : nx_correl_base ("FE Correlation") */
            void SetName
            (
                const char * name /** name */ 
            );
            /** Returns the description 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXString GetDescription
            (
            );
            /** Sets the description 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : nx_correl_base ("FE Correlation") */
            public: void SetDescription
            (
                const NXString & description /** description */ 
            );
            /** Sets the description 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : nx_correl_base ("FE Correlation") */
            void SetDescription
            (
                const char * description /** description */ 
            );
            /** Returns the search distance 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: double GetSearchDistance
            (
            );
            /** Sets the search distance 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : nx_correl_base ("FE Correlation") */
            public: void SetSearchDistance
            (
                double distance /** distance */ 
            );
            /**Returns  the check for coincident work nodes 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: bool CheckForCoincidentWorkNodes
            (
            );
            /**Sets  the check for coincident work nodes 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : nx_correl_base ("FE Correlation") */
            public: void SetCheckForCoincidentWorkNodes
            (
                bool flag /** flag */ 
            );
            /** Returns the coincidence tolerance 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: double GetCoincidenceTolerance
            (
            );
            /** Sets the coincidence tolerance 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : nx_correl_base ("FE Correlation") */
            public: void SetCoincidenceTolerance
            (
                double tolerance /** tolerance */ 
            );
            /**Returns  the type of ID matching  
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::CorrelNodeMapMethodBuilder::MatchingBy MatchBy
            (
            );
            /**Sets  the type of ID matching  
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : nx_correl_base ("FE Correlation") */
            public: void SetMatchBy
            (
                NXOpen::CAE::CorrelNodeMapMethodBuilder::MatchingBy type /** type */ 
            );
            /**Returns  the flag to control sequential mapping 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: bool MapSequentially
            (
            );
            /**Sets  the flag to control sequential mapping 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : nx_correl_base ("FE Correlation") */
            public: void SetMapSequentially
            (
                bool flag /** flag */ 
            );
            /**Returns  the offset 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: int Offset
            (
            );
            /**Sets  the offset 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : nx_correl_base ("FE Correlation") */
            public: void SetOffset
            (
                int flag /** flag */ 
            );
            /**Returns  the flag to control case sensitivity in name matching 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: bool MatchCase
            (
            );
            /**Sets  the flag to control case sensitivity in name matching 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : nx_correl_base ("FE Correlation") */
            public: void SetMatchCase
            (
                bool flag /** flag */ 
            );
            /**Returns  the flag to control special characters treatment in name matching 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: bool IgnoreSpecialChars
            (
            );
            /**Sets  the flag to control special characters treatment in name matching 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : nx_correl_base ("FE Correlation") */
            public: void SetIgnoreSpecialChars
            (
                bool flag /** flag */ 
            );
            /** Get manual pairs 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: void GetManualPairs
            (
                std::vector<int> & refLabels /** ref node labels */,
                std::vector<int> & workLabels /** work node labels */
            );
            /** Set manual pairs 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : nx_correl_base ("FE Correlation") */
            public: void SetManualPairs
            (
                const std::vector<int> & refLabels /** ref node labels */,
                const std::vector<int> & workLabels /** work node labels */
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