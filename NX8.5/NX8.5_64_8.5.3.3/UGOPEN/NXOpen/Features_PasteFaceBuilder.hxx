#ifndef NXOpen_FEATURES_PASTEFACEBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_PASTEFACEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_PasteFaceBuilder.ja
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
#include <NXOpen/Features_FeatureBuilder.hxx>
#include <NXOpen/Features_PasteFaceBuilder.hxx>
#include <NXOpen/SelectObject.hxx>
#include <NXOpen/SelectObjectList.hxx>
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
        class PasteFaceBuilder;
    }
    namespace Features
    {
        class FeatureBuilder;
    }
    class SelectBody;
    class SelectBodyList;
    namespace Features
    {
        class _PasteFaceBuilderBuilder;
        class PasteFaceBuilderImpl;
        /**
            Represents a builder for a paste face feature.
             <br> To create a new instance of this class, use @link Features::FeatureCollection::CreatePasteFaceBuilder  Features::FeatureCollection::CreatePasteFaceBuilder @endlink  <br> 
         <br>  Created in NX6.0.0.  <br>  
        */
        class NXOPENCPP_FEATURESEXPORT  PasteFaceBuilder : public Features::FeatureBuilder
        {
            /** represents the paste option which defines whether the tool body is additive or subtractive.
                        The paste option can be determined automatically from the add or subtract attributes on the tool body, or manually for a tool body lacking the said attributes. */
            public: enum PasteOptionType
            {
                PasteOptionTypeAutomatic/** determined automatically from the 'add' or 'subtract' attributes on each tool body. */,
                PasteOptionTypeAdd/** each tool body will add to the target body. */,
                PasteOptionTypeSubtract/** each tool body will subtract from the target body. */
            };

            private: PasteFaceBuilderImpl * m_pastefacebuilder_impl;
            private: friend class  _PasteFaceBuilderBuilder;
            protected: PasteFaceBuilder();
            public: ~PasteFaceBuilder();
            /**Returns  the target body.
                        The target body can be a solid or sheet. 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectBody * TargetBody
            (
            );
            /**Returns  the reverse target.
                        A flag to indicate whether the target body direction is reversed, disabled if target body is solid. 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: bool ReverseTarget
            (
            );
            /**Sets  the reverse target.
                        A flag to indicate whether the target body direction is reversed, disabled if target body is solid. 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetReverseTarget
            (
                bool reverseTarget /** reverse target */ 
            );
            /**Returns  the collector holding the tool bodies.
                        The tool bodies will be trimmed or extended then united to the target body.
                        The tool bodies should be sheet bodies. 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectBodyList * ToolBody
            (
            );
            /**Returns  the reverse tool.
                        A flag to indicate whether the tool body direction is reversed. 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: bool ReverseTool
            (
            );
            /**Sets  the reverse tool.
                        A flag to indicate whether the tool body direction is reversed. 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetReverseTool
            (
                bool reverseTool /** reverse tool */ 
            );
            /**Returns  the paste option defines whether the tool body is additive or subtractive. 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::PasteFaceBuilder::PasteOptionType PasteOption
            (
            );
            /**Sets  the paste option defines whether the tool body is additive or subtractive. 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetPasteOption
            (
                NXOpen::Features::PasteFaceBuilder::PasteOptionType pasteOption /** paste option */ 
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