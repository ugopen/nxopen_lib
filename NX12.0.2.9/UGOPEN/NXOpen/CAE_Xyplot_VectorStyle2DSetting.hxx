#ifndef NXOpen_CAE_XYPLOT_VECTORSTYLE2DSETTING_HXX_INCLUDED
#define NXOpen_CAE_XYPLOT_VECTORSTYLE2DSETTING_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_Xyplot_VectorStyle2DSetting.ja
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
#include <NXOpen/CAE_Xyplot_BaseLineStyleSetting.hxx>
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
            class VectorStyle2DSetting;
        }
    }
    namespace CAE
    {
        namespace Xyplot
        {
            class BaseLineStyleSetting;
        }
    }
    class NXColor;
    namespace CAE
    {
        namespace Xyplot
        {
            class _VectorStyle2DSettingBuilder;
            class VectorStyle2DSettingImpl;
            /** Represents the 2D vector display style.  <br> Not support KF.  <br> 
             <br>  Created in NX12.0.0.  <br>  
            */
            class NXOPENCPP_CAEEXPORT  VectorStyle2DSetting : public NXOpen::CAE::Xyplot::BaseLineStyleSetting
            {
                private: VectorStyle2DSettingImpl * m_vectorstyle2dsetting_impl;
                private: friend class  _VectorStyle2DSettingBuilder;
                protected: VectorStyle2DSetting();
                public: ~VectorStyle2DSetting();
                /**Returns  a value indicating whether to draw annotation text 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: bool DrawText
                (
                );
                /**Sets  a value indicating whether to draw annotation text 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: void SetDrawText
                (
                    bool canDrawText /** candrawtext */ 
                );
                /**Returns  a value indicating whether to customize annotation text count 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: bool IsAutoTextCount
                (
                );
                /**Sets  a value indicating whether to customize annotation text count 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: void SetAutoTextCount
                (
                    bool isAutoTextCount /** isautotextcount */ 
                );
                /**Returns  the maximum of customized text count 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: int MaximumTextCount
                (
                );
                /**Sets  the maximum of customized text count 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: void SetMaximumTextCount
                (
                    int maximumTextCount /** maximumtextcount */ 
                );
                /**Returns  a value indicating whether to allow the annotation text overlap with vector 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: bool OverlapTextAndVector
                (
                );
                /**Sets  a value indicating whether to allow the annotation text overlap with vector 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: void SetOverlapTextAndVector
                (
                    bool overlapTextAndVector /** Whether to allow the annotation text to overlap with vector */
                );
                /** Get the vector display colors  @return  Get the display vector colors 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: std::vector<NXOpen::NXColor *> GetVectorColors
                (
                );
                /** Set the vector display colors 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: void SetVectorColors
                (
                    const std::vector<NXOpen::NXColor *> & vectorColors /** Set the display vector colors */
                );
                /** Get the nth vector display color  @return  Get the nth display vector color 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::NXColor * GetNthVectorColor
                (
                    int index /** index */ 
                );
                /** Set the nth vector display color 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: void SetNthVectorColors
                (
                    int index /** index */ ,
                    NXOpen::NXColor * vectorColors /** Set the nth display vector color */
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
