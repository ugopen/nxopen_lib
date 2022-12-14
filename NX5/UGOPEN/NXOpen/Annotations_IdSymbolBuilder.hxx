#ifndef NXOpen_ANNOTATIONS_IDSYMBOLBUILDER_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_IDSYMBOLBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_IdSymbolBuilder.ja
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
#include <NXOpen/Annotations_AnnotationPlacement.hxx>
#include <NXOpen/Annotations_IdSymbolBuilder.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/SelectObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Annotations
    {
        class IdSymbolBuilder;
    }
    namespace Annotations
    {
        class AnnotationPlacement;
    }
    namespace Annotations
    {
        class IdSymbol;
    }
    class Builder;
    class SelectObject;
    namespace Annotations
    {
        class _IdSymbolBuilderBuilder;
        /**
            Represents an ID Symbol Builder
             <br> To create a new instance of this class, use @link Annotations::IdSymbolCollection::CreateIdSymbolBuilder Annotations::IdSymbolCollection::CreateIdSymbolBuilder@endlink  <br> */
        class NXOPENCPPEXPORT IdSymbolBuilder : public Builder
        {
            /** the valid types for an id symbol */
            public: enum SymbolTypes
            {
                SymbolTypesCircle/** Circle */,
                SymbolTypesDividedCircle/** Divided circle */,
                SymbolTypesTriangle/** Triangle with point down */,
                SymbolTypesTriangleUp/** Triangle with point up */,
                SymbolTypesSquare/** Square */,
                SymbolTypesDividedSquare/** Divided square */,
                SymbolTypesHexagon/** Hexagon */,
                SymbolTypesDividedHexagon/** Divided hexagon */,
                SymbolTypesQuadrantCircle/** Quadrant circle */,
                SymbolTypesRoundedBox/** Rounded box */
            };

            private: friend class  _IdSymbolBuilderBuilder;
            protected: IdSymbolBuilder();
            /**Returns  the symbol type  <br> License requirements : None */
            public: NXOpen::Annotations::IdSymbolBuilder::SymbolTypes SymbolType
            (
            );
            /**Sets  the symbol type  <br> License requirements : drafting ("DRAFTING") */
            public: void SetSymbolType
            (
                NXOpen::Annotations::IdSymbolBuilder::SymbolTypes symbolType /** symboltype */ 
            );
            /**Returns  the upper text  <br> License requirements : None */
            public: NXString UpperText
            (
            );
            /**Sets  the upper text  <br> License requirements : drafting ("DRAFTING") */
            public: void SetUpperText
            (
                const NXString & upperText /** uppertext */ 
            );
            /**Returns  the lower text  <br> License requirements : None */
            public: NXString LowerText
            (
            );
            /**Sets  the lower text  <br> License requirements : drafting ("DRAFTING") */
            public: void SetLowerText
            (
                const NXString & lowerText /** lowertext */ 
            );
            /**Returns  the size  <br> License requirements : None */
            public: double Size
            (
            );
            /**Sets  the size  <br> License requirements : drafting ("DRAFTING") */
            public: void SetSize
            (
                double size /** size */ 
            );
            /**Returns  the id symbol from which the size will be inherited  <br> License requirements : None */
            public: NXOpen::SelectObject * Inherit
            (
            );
            /**Returns  an annotation placement object  <br> License requirements : None */
            public: NXOpen::Annotations::AnnotationPlacement * Placement
            (
            );
            /** Sets the preview object for dialog creation of id symbols  <br> License requirements : None */
            public: void SetPreviewObject
            (
                NXOpen::Annotations::IdSymbol * symbol /** rubberbanding symbol */
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
