#ifndef NXOpen_MBD_STRINGCRITERIABUILDER_HXX_INCLUDED
#define NXOpen_MBD_STRINGCRITERIABUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     MBD_StringCriteriaBuilder.ja
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
#include <NXOpen/libmbdopencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace MBD
    {
        class StringCriteriaBuilder;
    }
    class Builder;
    namespace MBD
    {
        class _StringCriteriaBuilderBuilder;
        class StringCriteriaBuilderImpl;

        /// \cond NX_NO_DOC 
        /**
            Represents a @link NXOpen::MBD::StringCriteriaBuilder NXOpen::MBD::StringCriteriaBuilder@endlink 
             <br> This is a sub-builder class and cannot be directly instantiated  <br> 
        Default values.
        <list type="table"> 
         
        <listheader><term> 
        Property</term>  <description> 
        Value</description> </listheader>
        <item><term> 
         
        Criteria </term> <description> 
         
        Any </description> </item> 

        <item><term> 
         
        Value </term> <description> 
         
         </description> </item> 

        </list> 

         <br>  Created in NX1872.0.0.  <br>  
        */
        class MBDOPENCPPEXPORT  StringCriteriaBuilder : public NXOpen::Builder
        {
            /** filtering criteria options. */

            /// \cond NX_NO_DOC 
            public: enum FilterCriteria
            {
                FilterCriteriaAny/** any */ ,
                FilterCriteriaContains/** contains */ ,
                FilterCriteriaDoesNotContain/** does not contain */ ,
                FilterCriteriaNone/** none */ ,
                FilterCriteriaIs/** is */ ,
                FilterCriteriaStartswith/** startswith */ ,
                FilterCriteriaEndswith/** endswith */ 
            };


            /// \endcond 
            private: StringCriteriaBuilderImpl * m_stringcriteriabuilder_impl;
            private: friend class  _StringCriteriaBuilderBuilder;
            protected: StringCriteriaBuilder();
            public: ~StringCriteriaBuilder();

            /// \cond NX_NO_DOC 
            /**Returns  the filtering Criteria 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::MBD::StringCriteriaBuilder::FilterCriteria Criteria
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the filtering Criteria 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: void SetCriteria
            (
                NXOpen::MBD::StringCriteriaBuilder::FilterCriteria criteria /** criteria */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the value for filtering
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NXString Value
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the value for filtering
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: void SetValue
            (
                const NXString & criteriaValue /** criteriavalue */ 
            );
            /**Sets  the value for filtering
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            void SetValue
            (
                const char * criteriaValue /** criteriavalue */ 
            );

            /// \endcond 
        };

        /// \endcond 
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
