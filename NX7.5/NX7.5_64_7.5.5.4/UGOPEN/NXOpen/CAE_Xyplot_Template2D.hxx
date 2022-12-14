#ifndef NXOpen_CAE_XYPLOT_TEMPLATE2D_HXX_INCLUDED
#define NXOpen_CAE_XYPLOT_TEMPLATE2D_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_Xyplot_Template2D.ja
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
#include <NXOpen/CAE_Xyplot_BaseTemplate.hxx>
#include <NXOpen/CAE_XyplotDataTypes.hxx>
#include <NXOpen/CAE_Xyplot_Template2D.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAE
    {
        namespace Xyplot
        {
            class Template2D;
        }
    }
    namespace CAE
    {
        namespace Xyplot
        {
            class BaseTemplate;
        }
    }
    namespace CAE
    {
        namespace Xyplot
        {
            class _Template2DBuilder;
            class Template2DImpl;
            /** Manages the 2D display style  <br> Not support KF. <br> */
            class NXOPENCPPEXPORT  Template2D : public CAE::Xyplot::BaseTemplate
            {
                private: Template2DImpl * m_template2d_impl;
                private: friend class  _Template2DBuilder;
                protected: Template2D();
                public: ~Template2D();
                /**Returns  the complex option  <br> License requirements : nx_ftk ("NX Advanced Graphing") */
                public: NXOpen::CAE::Xyplot::ComplexOption2D ComplexOption
                (
                );
                /**Sets  the complex option  <br> License requirements : nx_ftk ("NX Advanced Graphing") */
                public: void SetComplexOption
                (
                    NXOpen::CAE::Xyplot::ComplexOption2D complexOption /** Complex option */
                );
                /**Returns  the grid layout style  <br> License requirements : nx_ftk ("NX Advanced Graphing") */
                public: NXOpen::CAE::Xyplot::GridLayout2D GridLayout
                (
                );
                /**Sets  the grid layout style  <br> License requirements : nx_ftk ("NX Advanced Graphing") */
                public: void SetGridLayout
                (
                    const NXOpen::CAE::Xyplot::GridLayout2D & gridLayout /** Grid layout style */
                );
                /** Gets line style option  @return  Line style option  <br> License requirements : nx_ftk ("NX Advanced Graphing") */
                public: NXOpen::CAE::Xyplot::LineOption2D GetLineOption
                (
                    int styleIndex /** Style index */
                );
                /** Sets line style option  <br> License requirements : nx_ftk ("NX Advanced Graphing") */
                public: void SetLineOption
                (
                    int styleIndex /** Style index */,
                    const NXOpen::CAE::Xyplot::LineOption2D & lineOption /** Line style option */
                );
                /** Gets bar style option  @return  Bar style option  <br> License requirements : nx_ftk ("NX Advanced Graphing") */
                public: NXOpen::CAE::Xyplot::BarOption2D GetBarOption
                (
                    int styleIndex /** Style index */
                );
                /** Sets bar style option  <br> License requirements : nx_ftk ("NX Advanced Graphing") */
                public: void SetBarOption
                (
                    int styleIndex /** Style index */,
                    const NXOpen::CAE::Xyplot::BarOption2D & barOption /** Bar style option */
                );
                /** Gets plate style option  @return  Plate style option  <br> License requirements : nx_ftk ("NX Advanced Graphing") */
                public: NXOpen::CAE::Xyplot::PlateOption2D GetPlateOption
                (
                    int styleIndex /** Style index */
                );
                /** Sets plate style option  <br> License requirements : nx_ftk ("NX Advanced Graphing") */
                public: void SetPlateOption
                (
                    int styleIndex /** Style index */,
                    const NXOpen::CAE::Xyplot::PlateOption2D & plateOption /** Plate style option */
                );
                /** Switchs the X/Y axis  <br> License requirements : nx_ftk ("NX Advanced Graphing") */
                public: void SwitchXyAxis
                (
                );
            };
        }
    }
}
#undef EXPORTLIBRARY
#endif
