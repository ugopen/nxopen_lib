#ifndef NXOpen_EXPRESSIONGROUP_HXX_INCLUDED
#define NXOpen_EXPRESSIONGROUP_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     ExpressionGroup.ja
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
    class ExpressionGroup;
    class Expression;
    class NXObject;
    class _ExpressionGroupBuilder;
    class ExpressionGroupImpl;
    /** Represents an expression group.  <br> To create a new instance of this class, use @link NXOpen::ExpressionGroupCollection::Create  NXOpen::ExpressionGroupCollection::Create @endlink  <br> 
     <br>  Created in NX10.0.0.  <br>  
    */
    class NXOPENCPPEXPORT  ExpressionGroup : public NXOpen::NXObject
    {
        private: ExpressionGroupImpl * m_expressiongroup_impl;
        private: friend class  _ExpressionGroupBuilder;
        protected: ExpressionGroup();
        public: ~ExpressionGroup();
        /**Sets  an expression group's  visibility
         <br>  Created in NX10.0.0.  <br>  
         <br> License requirements : None */
        public: void SetVisibility
        (
            bool visibile /** True - make group visible, False - make group invisible */
        );
        /**Returns  an expression group's  visibility
         <br>  Created in NX10.0.0.  <br>  
         <br> License requirements : None */
        public: bool Visibility
        (
        );
        /**Returns  an expression group's parent group or NULL
         <br>  Created in NX10.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::ExpressionGroup * Parent
        (
        );
        /**Sets  an expression group's parent group or NULL
         <br>  Created in NX10.0.0.  <br>  
         <br> License requirements : None */
        public: void SetParent
        (
            NXOpen::ExpressionGroup * parentGroup /** Tag of parent group or NULL */
        );
        /** Get an array of member expression groups in a group.  To remove member groups, 
                use set_parent property  @return  array of expression groups 
         <br>  Created in NX10.0.0.  <br>  
         <br> License requirements : None */
        public: std::vector<NXOpen::ExpressionGroup *> GetMemberGroups
        (
        );
        /** Return an array of expressions in a group.   @return  array of expressions 
         <br>  Created in NX10.0.0.  <br>  
         <br> License requirements : None */
        public: std::vector<NXOpen::Expression *> GetExpressions
        (
        );
        /** Add expressions to an expression group 
         <br>  Created in NX10.0.0.  <br>  
         <br> License requirements : None */
        public: void SetExpressions
        (
            const std::vector<NXOpen::Expression *> & expressions /** array of expressions */
        );
        /** Remove expressions from a group.  This DOES NOT delete the expression from NX.
                Once removed from a group, an expression will be added to the Default Group 
         <br>  Created in NX10.0.0.  <br>  
         <br> License requirements : None */
        public: void RemoveExpressions
        (
            const std::vector<NXOpen::Expression *> & expressions /** array of expressions */
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
