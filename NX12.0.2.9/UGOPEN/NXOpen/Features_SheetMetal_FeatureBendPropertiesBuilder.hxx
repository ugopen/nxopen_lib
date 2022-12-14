#ifndef NXOpen_FEATURES_SHEETMETAL_FEATUREBENDPROPERTIESBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_SHEETMETAL_FEATUREBENDPROPERTIESBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_SheetMetal_FeatureBendPropertiesBuilder.ja
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
#include <NXOpen/Features_SheetMetal_BendOptions.hxx>
#include <NXOpen/Features_SheetMetal_SheetmetalComponentBuilder.hxx>
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
        namespace SheetMetal
        {
            class FeatureBendPropertiesBuilder;
        }
    }
    class Expression;
    namespace Features
    {
        namespace SheetMetal
        {
            class BendOptions;
        }
    }
    namespace Features
    {
        namespace SheetMetal
        {
            class SheetmetalComponentBuilder;
        }
    }
    namespace Features
    {
        namespace SheetMetal
        {
            class _FeatureBendPropertiesBuilderBuilder;
            class FeatureBendPropertiesBuilderImpl;
            /** Represents a Sheetmetal Feature bend properties builder class. This builder is used to
                    interrogate the feature properties in the list. <br> To create a new instance of this class, use @link NXOpen::Features::SheetMetal::FeatureBendPropertiesListBuilder::CreateFeatureProperties  NXOpen::Features::SheetMetal::FeatureBendPropertiesListBuilder::CreateFeatureProperties @endlink  <br> 
             <br>  Created in NX12.0.0.  <br>  
            */
            class NXOPENCPP_FEATURESEXPORT  FeatureBendPropertiesBuilder : public NXOpen::Features::SheetMetal::SheetmetalComponentBuilder
            {
                private: FeatureBendPropertiesBuilderImpl * m_featurebendpropertiesbuilder_impl;
                private: friend class  _FeatureBendPropertiesBuilderBuilder;
                protected: FeatureBendPropertiesBuilder();
                public: ~FeatureBendPropertiesBuilder();
                /**Returns  the offset 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * Value
                (
                );
                /**Returns  the Sheet Metal Bend Options 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::SheetMetal::BendOptions * BendOptions
                (
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
