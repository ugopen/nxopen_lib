#ifndef NXOpen_FEATURES_SHEETMETAL_EDITBENDBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_SHEETMETAL_EDITBENDBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_SheetMetal_EditBendBuilder.ja
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
#include <NXOpen/Features_SheetMetal_BendOptions.hxx>
#include <NXOpen/Features_SheetMetal_EditBendBuilder.hxx>
#include <NXOpen/Features_FeatureBuilder.hxx>
#include <NXOpen/ScCollector.hxx>
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
            class EditBendBuilder;
        }
    }
    namespace Features
    {
        class FeatureBuilder;
    }
    namespace Features
    {
        namespace SheetMetal
        {
            class BendOptions;
        }
    }
    class ScCollector;
    namespace Features
    {
        namespace SheetMetal
        {
            class _EditBendBuilderBuilder;
            class EditBendBuilderImpl;
            /**
                    Represents a @link Features::EditBend Features::EditBend@endlink  builder
                     <br> To create a new instance of this class, use @link NXOpen::Features::SheetMetal::SheetmetalManager::CreateEditBendBuilder  NXOpen::Features::SheetMetal::SheetmetalManager::CreateEditBendBuilder @endlink  <br> 
             <br>  Created in NX7.5.0.  <br>  
            */
            class NXOPENCPP_FEATURESEXPORT  EditBendBuilder : public NXOpen::Features::FeatureBuilder
            {
                private: EditBendBuilderImpl * m_editbendbuilder_impl;
                private: friend class  _EditBendBuilderBuilder;
                protected: EditBendBuilder();
                public: ~EditBendBuilder();
                /**Returns  the select bend 
                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::ScCollector * SelectBend
                (
                );
                /**Returns  the bend options 
                 <br>  Created in NX7.5.0.  <br>  
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
