#ifndef NXOpen_ASSEMBLIES_PRODUCTOUTLINEBUILDER_HXX_INCLUDED
#define NXOpen_ASSEMBLIES_PRODUCTOUTLINEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Assemblies_ProductOutlineBuilder.ja
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
#include <NXOpen/Assemblies_ProductOutlineBuilder.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Assemblies
    {
        class ProductOutlineBuilder;
    }
    class Builder;
    class NXColor;
    class SelectDisplayableObjectList;
    namespace Assemblies
    {
        class _ProductOutlineBuilderBuilder;
        /**
               Represents a builder @link Assemblies::ProductOutlineBuilder Assemblies::ProductOutlineBuilder@endlink .
             <br> To create a new instance of this class, use @link Assemblies::ProductOutlineManager::CreateProductOutlineBuilder Assemblies::ProductOutlineManager::CreateProductOutlineBuilder@endlink  <br> 
        Default values:
        LineFontType: Solid
        OverrideColor: false
        Translucency: 50
        */
        class NXOPENCPPEXPORT ProductOutlineBuilder : public Builder
        {
            /** Represents the line font types*/
            public: enum LineFont
            {
                LineFontSolid/** Solid Line */,
                LineFontDashed/** Dashed Line */,
                LineFontPhantom/** Phantom Line */,
                LineFontCenterline/** Center Line */,
                LineFontDotted/** Dotted Line */,
                LineFontLongdash/** Longdash Line */,
                LineFontDotdash/** Dotdash Line */
            };

            private: friend class  _ProductOutlineBuilderBuilder;
            protected: ProductOutlineBuilder();
            /**Returns  the objects defined in Product Outline.  <br> License requirements : None */
            public: NXOpen::SelectDisplayableObjectList * SelectObject
            (
            );
            /**Returns  the flag to override-color switch. If "true" the facet representation is in original color of selected object, 
                        else representation is in the color defined by @link Assemblies::ProductOutlineBuilder::OutlineColor Assemblies::ProductOutlineBuilder::OutlineColor@endlink .
                       <br> License requirements : None */
            public: bool OverrideColor
            (
            );
            /**Sets  the flag to override-color switch. If "true" the facet representation is in original color of selected object, 
                        else representation is in the color defined by @link Assemblies::ProductOutlineBuilder::OutlineColor Assemblies::ProductOutlineBuilder::OutlineColor@endlink .
                       <br> License requirements : assemblies ("ASSEMBLIES MODULE") */
            public: void SetOverrideColor
            (
                bool overrideColor /** overridecolor */ 
            );
            /**Returns  the color for all the objects defined in Product Outline.  The range is 1-216 <br> License requirements : None */
            public: NXOpen::NXColor * OutlineColor
            (
            );
            /**Sets  the color for all the objects defined in Product Outline.  The range is 1-216 <br> License requirements : assemblies ("ASSEMBLIES MODULE") */
            public: void SetOutlineColor
            (
                NXOpen::NXColor * outlineColor /** outlinecolor */ 
            );
            /**Returns  the line font type for the objects defined in Product Outline. The font types are mentioned in 
                        @link Assemblies::ProductOutlineBuilder::LineFont Assemblies::ProductOutlineBuilder::LineFont@endlink .
                        <br> License requirements : None */
            public: NXOpen::Assemblies::ProductOutlineBuilder::LineFont LineFontType
            (
            );
            /**Sets  the line font type for the objects defined in Product Outline. The font types are mentioned in 
                        @link Assemblies::ProductOutlineBuilder::LineFont Assemblies::ProductOutlineBuilder::LineFont@endlink .
                        <br> License requirements : assemblies ("ASSEMBLIES MODULE") */
            public: void SetLineFontType
            (
                NXOpen::Assemblies::ProductOutlineBuilder::LineFont lineFontType /** linefonttype */ 
            );
            /**Returns  the translucency of faceted bodies/objects defined in Product Outline. The range is 0-100. <br> License requirements : None */
            public: int Translucency
            (
            );
            /**Sets  the translucency of faceted bodies/objects defined in Product Outline. The range is 0-100. <br> License requirements : assemblies ("ASSEMBLIES MODULE") */
            public: void SetTranslucency
            (
                int translucency /** translucency */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif