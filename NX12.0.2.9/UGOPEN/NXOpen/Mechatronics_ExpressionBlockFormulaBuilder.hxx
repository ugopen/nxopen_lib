#ifndef NXOpen_MECHATRONICS_EXPRESSIONBLOCKFORMULABUILDER_HXX_INCLUDED
#define NXOpen_MECHATRONICS_EXPRESSIONBLOCKFORMULABUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Mechatronics_ExpressionBlockFormulaBuilder.ja
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
#include <NXOpen/Mechatronics_RuntimeFormulaBuilder.hxx>
#include <NXOpen/libnxopencpp_mechatronics_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Mechatronics
    {
        class ExpressionBlockFormulaBuilder;
    }
    namespace Mechatronics
    {
        class RuntimeFormulaBuilder;
    }
    namespace Mechatronics
    {
        class _ExpressionBlockFormulaBuilderBuilder;
        class ExpressionBlockFormulaBuilderImpl;
        /**
            Represents a @link Mechatronics::ExpressionBlockFormulaBuilder Mechatronics::ExpressionBlockFormulaBuilder@endlink .
             <br> To create a new instance of this class, use @link NXOpen::Mechatronics::ExpressionBlockFormulaCollection::CreateExpressionBlockFormulaBuilder  NXOpen::Mechatronics::ExpressionBlockFormulaCollection::CreateExpressionBlockFormulaBuilder @endlink  <br> 
         <br>  Created in NX11.0.0.  <br>  
        */
        class NXOPENCPP_MECHATRONICSEXPORT  ExpressionBlockFormulaBuilder : public NXOpen::Mechatronics::RuntimeFormulaBuilder
        {
            private: ExpressionBlockFormulaBuilderImpl * m_expressionblockformulabuilder_impl;
            private: friend class  _ExpressionBlockFormulaBuilderBuilder;
            protected: ExpressionBlockFormulaBuilder();
            public: ~ExpressionBlockFormulaBuilder();
            /**Returns  the formula comment. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: NXString FormulaComment
            (
            );
            /**Sets  the formula comment. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: void SetFormulaComment
            (
                const NXString & formulaComment /** formulacomment */ 
            );
            /**Sets  the formula comment. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            void SetFormulaComment
            (
                const char * formulaComment /** formulacomment */ 
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
