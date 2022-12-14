#ifndef NXOpen_GEOMETRICUTILITIES_INSTANCEEDITEDEXPRESSIONSLIST_HXX_INCLUDED
#define NXOpen_GEOMETRICUTILITIES_INSTANCEEDITEDEXPRESSIONSLIST_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     GeometricUtilities_InstanceEditedExpressionsList.ja
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
#include <NXOpen/Expression.hxx>
#include <NXOpen/GeometricUtilities_InstanceEditedExpressionItem.hxx>
#include <NXOpen/GeometricUtilities_IComponentBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/ObjectList.hxx>
#include <NXOpen/libnxopencpp_geometricutilities_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace GeometricUtilities
    {
        class InstanceEditedExpressionsList;
    }
    class Expression;
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    namespace GeometricUtilities
    {
        class InstanceEditedExpressionItem;
    }
    namespace GeometricUtilities
    {
        class InstanceEditedExpressionItemList;
    }
    namespace GeometricUtilities
    {
        class _InstanceEditedExpressionsListBuilder;
        class InstanceEditedExpressionsListImpl;
        /** list of @link NXOpen::GeometricUtilities::InstanceEditedExpressionItem NXOpen::GeometricUtilities::InstanceEditedExpressionItem@endlink  objects. 
         <br>  Created in NX7.5.0.  <br>  
        */
        class NXOPENCPP_GEOMETRICUTILITIESEXPORT  InstanceEditedExpressionsList : public NXOpen::TaggedObject, public virtual NXOpen::GeometricUtilities::IComponentBuilder
        {
            private: InstanceEditedExpressionsListImpl * m_instanceeditedexpressionslist_impl;
            private: friend class  _InstanceEditedExpressionsListBuilder;
            protected: InstanceEditedExpressionsList();
            public: ~InstanceEditedExpressionsList();
            /**Returns  the list of @link NXOpen::GeometricUtilities::InstanceEditedExpressionItem NXOpen::GeometricUtilities::InstanceEditedExpressionItem@endlink  objects. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricUtilities::InstanceEditedExpressionItemList * List
            (
            );
            /** This is the default creator for @link NXOpen::GeometricUtilities::InstanceEditedExpressionItem NXOpen::GeometricUtilities::InstanceEditedExpressionItem@endlink .  @return  
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricUtilities::InstanceEditedExpressionItem * EditInstanceExpression
            (
            );
            /** This is the creator for @link NXOpen::GeometricUtilities::InstanceEditedExpressionItem NXOpen::GeometricUtilities::InstanceEditedExpressionItem@endlink  which should be used.  @return  
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricUtilities::InstanceEditedExpressionItem * EditInstanceExpression
            (
                NXOpen::Expression * masterExpression /** the master expression */,
                NXOpen::Expression * instanceExpression /** the instance expression */
            );
            /** Validate whether the inputs to the component are sufficient for 
                        commit to be called.  If the component is not in a state to commit
                        then an exception is thrown.  For example, if the component requires
                        you to set some property, this method will throw an exception if
                        you haven't set it.  This method throws a not-yet-implemented
                        NXException for some components.
                     @return  Was self validation successful 
             <br>  Created in NX3.0.1.  <br>  
             <br> License requirements : None */
            public: virtual bool Validate
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
