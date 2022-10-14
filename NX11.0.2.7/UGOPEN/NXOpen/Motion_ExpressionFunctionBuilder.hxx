#ifndef NXOpen_MOTION_EXPRESSIONFUNCTIONBUILDER_HXX_INCLUDED
#define NXOpen_MOTION_EXPRESSIONFUNCTIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Motion_ExpressionFunctionBuilder.ja
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
#include <NXOpen/Motion_ExpressionFunctionBuilder.hxx>
#include <NXOpen/GeometricUtilities_IComponentBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_motion_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Motion
    {
        class ExpressionFunctionBuilder;
    }
    class Expression;
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    namespace Motion
    {
        class MotionFunction;
    }
    namespace Motion
    {
        class _ExpressionFunctionBuilderBuilder;
        class ExpressionFunctionBuilderImpl;
        /** Represents a ExpressionFunctionBuilder builder 
         <br>  Created in NX11.0.0.  <br>  
        */
        class NXOPENCPP_MOTIONEXPORT  ExpressionFunctionBuilder : public NXOpen::TaggedObject, public virtual NXOpen::GeometricUtilities::IComponentBuilder
        {
            /** The block type can be Constant when a constant expression is used or Function when a spline curve is used.
                    */
            public: enum Type
            {
                TypeExpression/** expression */ ,
                TypeFunction/** function */ 
            };

            private: ExpressionFunctionBuilderImpl * m_expressionfunctionbuilder_impl;
            private: friend class  _ExpressionFunctionBuilderBuilder;
            protected: ExpressionFunctionBuilder();
            public: ~ExpressionFunctionBuilder();
            /**Returns  the type.
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: NXOpen::Motion::ExpressionFunctionBuilder::Type DataType
            (
            );
            /**Sets  the type.
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetDataType
            (
                NXOpen::Motion::ExpressionFunctionBuilder::Type type /** type */ 
            );
            /**Returns  the Expression of this block
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: NXOpen::Expression * Expression
            (
            );
            /**Returns  the Function.
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: NXOpen::Motion::MotionFunction * Function
            (
            );
            /**Sets  the Function.
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetFunction
            (
                NXOpen::Motion::MotionFunction * func /** func */ 
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