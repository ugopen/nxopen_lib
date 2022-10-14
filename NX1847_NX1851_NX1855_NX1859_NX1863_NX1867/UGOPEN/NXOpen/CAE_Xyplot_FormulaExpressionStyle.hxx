#ifndef NXOpen_CAE_XYPLOT_FORMULAEXPRESSIONSTYLE_HXX_INCLUDED
#define NXOpen_CAE_XYPLOT_FORMULAEXPRESSIONSTYLE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_Xyplot_FormulaExpressionStyle.ja
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
#include <NXOpen/CAE_XyplotDataTypes.hxx>
#include <NXOpen/CAE_Xyplot_BaseDisplayStyleSetting.hxx>
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
        namespace Xyplot
        {
            class FormulaExpressionStyle;
        }
    }
    namespace CAE
    {
        namespace Xyplot
        {
            class BaseDisplayStyleSetting;
        }
    }
    namespace CAE
    {
        namespace Xyplot
        {
            class _FormulaExpressionStyleBuilder;
            class FormulaExpressionStyleImpl;
            /** Represents the formula expression style.  <br> Not support KF.  <br> 
             <br>  Created in NX1847.0.0.  <br>  
            */
            class NXOPENCPP_CAEEXPORT  FormulaExpressionStyle : public NXOpen::CAE::Xyplot::BaseDisplayStyleSetting
            {
                private: FormulaExpressionStyleImpl * m_formulaexpressionstyle_impl;
                private: friend class  _FormulaExpressionStyleBuilder;
                protected: FormulaExpressionStyle();
                public: ~FormulaExpressionStyle();
                /**Returns  the formula grid type 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::CAE::Xyplot::FormulaGridType FormulaGridType
                (
                );
                /**Sets  the formula grid type 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : None */
                public: void SetFormulaGridType
                (
                    NXOpen::CAE::Xyplot::FormulaGridType formulaGridType /** formulagridtype */ 
                );
                /** Get the variable values  @return  Get the variable values 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : None */
                public: std::vector<double> GetVariableValues
                (
                );
                /** Set the variable values 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : None */
                public: void SetVariableValues
                (
                    const std::vector<double> & variableValues /** Set the variable values */
                );
                /**Returns  a value indicating whether to include positive infinity 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : None */
                public: bool IsIncludePositiveInfinity
                (
                );
                /**Sets  a value indicating whether to include positive infinity 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : None */
                public: void SetIncludePositiveInfinity
                (
                    bool isInclude /** isinclude */ 
                );
                /**Returns  a value indicating whether to include negative infinity 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : None */
                public: bool IsIncludeNegativeInfinity
                (
                );
                /**Sets  a value indicating whether to include negative infinity 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : None */
                public: void SetIncludeNegativeInfinity
                (
                    bool isInclude /** isinclude */ 
                );
            };
        }
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