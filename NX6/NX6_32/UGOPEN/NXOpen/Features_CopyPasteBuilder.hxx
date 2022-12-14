#ifndef NXOpen_FEATURES_COPYPASTEBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_COPYPASTEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_CopyPasteBuilder.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/Features_CopyPasteBuilder.hxx>
#include <NXOpen/Features_FeatureReferencesBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Features
    {
        class CopyPasteBuilder;
    }
    class Builder;
    namespace Features
    {
        class FeatureReferencesBuilder;
    }
    namespace Features
    {
        class _CopyPasteBuilderBuilder;
        /**
            Represents a @link Features::CopyPasteBuilder Features::CopyPasteBuilder@endlink 
             <br> To create a new instance of this class, use @link Features::FeatureCollection::CreateCopyPasteBuilder Features::FeatureCollection::CreateCopyPasteBuilder@endlink  <br> */
        class NXOPENCPPEXPORT CopyPasteBuilder : public Builder
        {
            /** Types of expression transfer mode */
            public: enum ExpressionTransferOption
            {
                ExpressionTransferOptionCreateNew/** New */,
                ExpressionTransferOptionLinkToOriginal/** Link to Original */,
                ExpressionTransferOptionOriginalInstance/** Instance of Original */
            };

            /** Types of parent transfer mode */
            public: enum ParentTransferOption
            {
                ParentTransferOptionPromptForNew/** Copy Original Curves */,
                ParentTransferOptionCopyOriginalCurve/** Prompt for New */,
                ParentTransferOptionOriginalInstance/** Instance of Original */
            };

            private: friend class  _CopyPasteBuilderBuilder;
            protected: CopyPasteBuilder();
            /**Returns  the expression option  <br> License requirements : None */
            public: NXOpen::Features::CopyPasteBuilder::ExpressionTransferOption ExpressionOption
            (
            );
            /**Sets  the expression option  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetExpressionOption
            (
                NXOpen::Features::CopyPasteBuilder::ExpressionTransferOption expressionOption /** expressionoption */ 
            );
            /**Returns  the parent option  <br> License requirements : None */
            public: NXOpen::Features::CopyPasteBuilder::ParentTransferOption ParentOption
            (
            );
            /**Sets  the parent option  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetParentOption
            (
                NXOpen::Features::CopyPasteBuilder::ParentTransferOption parentOption /** parentoption */ 
            );
            /** Returns the feature references builder @return   <br> License requirements : None */
            public: NXOpen::Features::FeatureReferencesBuilder * GetFeatureReferences
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
