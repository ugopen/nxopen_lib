#ifndef NXOpen_FEATURES_USERDEFINEDFEATUREEXPRESSIONDATA_HXX_INCLUDED
#define NXOpen_FEATURES_USERDEFINEDFEATUREEXPRESSIONDATA_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_UserDefinedFeatureExpressionData.ja
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
#include <NXOpen/libnxopencpp_features_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Features
    {
        class UserDefinedFeatureExpressionData;
    }
    class Expression;
    namespace Features
    {
        class _UserDefinedFeatureExpressionDataBuilder;
        class UserDefinedFeatureExpressionDataImpl;
        /** JA interface for UserDefinedFeatureExpressionData object. Object of this class contain an expression of a user defined feature and the corresponding prompt.  <br> This calls cannot be created  <br> 
         <br>  Created in NX8.0.0.  <br>  
        */
        class NXOPENCPP_FEATURESEXPORT  UserDefinedFeatureExpressionData : public NXOpen::TaggedObject
        {
            private: UserDefinedFeatureExpressionDataImpl * m_userdefinedfeatureexpressiondata_impl;
            private: friend class  _UserDefinedFeatureExpressionDataBuilder;
            protected: UserDefinedFeatureExpressionData();
            public: ~UserDefinedFeatureExpressionData();
            /**Returns  the expression of the user defined feature 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * Expression
            (
            );
            /**Returns  the prompt for the expression of the user defined feature 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXString Prompt
            (
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