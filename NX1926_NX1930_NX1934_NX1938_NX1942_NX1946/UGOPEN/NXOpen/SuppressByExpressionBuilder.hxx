#ifndef NXOpen_SUPPRESSBYEXPRESSIONBUILDER_HXX_INCLUDED
#define NXOpen_SUPPRESSBYEXPRESSIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     SuppressByExpressionBuilder.ja
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
#include <NXOpen/SelectObjectList.hxx>
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
    class SuppressByExpressionBuilder;
    class Builder;
    namespace Features
    {
        class SelectFeatureList;
    }
    class _SuppressByExpressionBuilderBuilder;
    class SuppressByExpressionBuilderImpl;
    /**
        Represents a @link NXOpen::SuppressByExpressionBuilder NXOpen::SuppressByExpressionBuilder@endlink 
         <br> To create a new instance of this class, use @link NXOpen::ExpressionCollection::CreateSuppressByExpressionBuilder  NXOpen::ExpressionCollection::CreateSuppressByExpressionBuilder @endlink  <br> 
    Default values.
    <list type="table"> 
     
    <listheader><term> 
    Property</term>  <description> 
    Value</description> </listheader>
    <item><term> 
     
    SuppressAction </term> <description> 
     
    CreateEach </description> </item> 

    </list> 

     <br>  Created in NX5.0.0.  <br>  
    */
    class NXOPENCPPEXPORT  SuppressByExpressionBuilder : public NXOpen::Builder
    {
        /** Represents the expression action type.*/
        public: enum ExpressionAction
        {
            ExpressionActionCreateEach/**Create one expression per feature*/,
            ExpressionActionCreateShared/**Create one common expression for all features*/,
            ExpressionActionDeleteEach/**Delete expression of one feature*/,
            ExpressionActionDeleteShared/**Delete the common expression being shared by group of features*/
        };

        private: SuppressByExpressionBuilderImpl * m_suppressbyexpressionbuilder_impl;
        private: friend class  _SuppressByExpressionBuilderBuilder;
        protected: SuppressByExpressionBuilder();
        public: ~SuppressByExpressionBuilder();
        /**Returns  the suppress expression action. This enumeration decides the action to be taken
                on the selected group of features. A suppress expression can created per feature or
                as shared expression for a group of features. The expressions can be deleted individually
                for all features that have suppress expressions associated. For a group of features sharing
                an expression, the expression can also be deleted from the whole group.
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::SuppressByExpressionBuilder::ExpressionAction SuppressAction
        (
        );
        /**Sets  the suppress expression action. This enumeration decides the action to be taken
                on the selected group of features. A suppress expression can created per feature or
                as shared expression for a group of features. The expressions can be deleted individually
                for all features that have suppress expressions associated. For a group of features sharing
                an expression, the expression can also be deleted from the whole group.
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : None */
        public: void SetSuppressAction
        (
            NXOpen::SuppressByExpressionBuilder::ExpressionAction suppressAction /** suppressaction */ 
        );
        /**Returns  the feautre list. For create each and create shared options, the selected features
                must not have pre existing suppress expressions. For delete each option, the selected
                features must have associated suppress expressions. If the expression is being shared
                by multiple features, the expression will be deleted only for the selected feature. For
                delete shared option, the complete group that shares a single expression must be selected.
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::Features::SelectFeatureList * FeatureList
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
