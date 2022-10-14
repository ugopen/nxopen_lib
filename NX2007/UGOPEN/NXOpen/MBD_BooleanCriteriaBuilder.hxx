#ifndef NXOpen_MBD_BOOLEANCRITERIABUILDER_HXX_INCLUDED
#define NXOpen_MBD_BOOLEANCRITERIABUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     MBD_BooleanCriteriaBuilder.ja
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
        class BooleanCriteriaBuilder;
    }
    class Builder;
    namespace MBD
    {
        class _BooleanCriteriaBuilderBuilder;
        class BooleanCriteriaBuilderImpl;

        /// \cond NX_NO_DOC 
        /**
            Represents a @link NXOpen::MBD::BooleanCriteriaBuilder NXOpen::MBD::BooleanCriteriaBuilder@endlink 
             <br> This is a sub-builder class and cannot be directly instantiated  <br> 
         <br>  Created in NX1899.0.0.  <br>  
        */
        class MBDOPENCPPEXPORT  BooleanCriteriaBuilder : public NXOpen::Builder
        {
            private: BooleanCriteriaBuilderImpl * m_booleancriteriabuilder_impl;
            private: friend class  _BooleanCriteriaBuilderBuilder;
            protected: BooleanCriteriaBuilder();
            public: ~BooleanCriteriaBuilder();

            /// \cond NX_NO_DOC 
            /**Returns  the Boolean Value 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: bool BooleanValue
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the Boolean Value 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: void SetBooleanValue
            (
                bool booleanValue /** booleanvalue */ 
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