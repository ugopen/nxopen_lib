#ifndef NXOpen_CAE_ELEMENTSPLITBUILDER_HXX_INCLUDED
#define NXOpen_CAE_ELEMENTSPLITBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_ElementSplitBuilder.ja
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
#include <NXOpen/CAE_ElementSplitBuilder.hxx>
#include <NXOpen/CAE_SelectElementsBuilder.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAE
    {
        class ElementSplitBuilder;
    }
    class Builder;
    namespace CAE
    {
        class SelectElementsBuilder;
    }
    namespace CAE
    {
        class SelectFEElementList;
    }
    class Point;
    namespace CAE
    {
        class _ElementSplitBuilderBuilder;
        /**
            Represents a @link CAE::ElementSplitBuilder CAE::ElementSplitBuilder@endlink 
             <br> To create a new instance of this class, use @link CAE::NodeElementManager::CreateElementSplitBuilder CAE::NodeElementManager::CreateElementSplitBuilder@endlink  <br> */
        class NXOPENCPPEXPORT ElementSplitBuilder : public Builder
        {
            /** the element split types */
            public: enum Types
            {
                TypesQuadTo2Tria/**Quad to 2 Tria */,
                TypesQuadTo2Quad/**Quad to 2 Quad */,
                TypesQuadTo4Quad/**Quad to 4 Quad */,
                TypesQuadTo3Quad/**Quad to 3 Quad */,
                TypesQuadTo3Tria/**Quad to 3 Tria */,
                TypesTriaTo4Tria/**Tria to 4 Tria */,
                TypesSplitByLine/**Split by line */
            };

            private: friend class  _ElementSplitBuilderBuilder;
            protected: ElementSplitBuilder();
            /**Returns  the split type  <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::CAE::ElementSplitBuilder::Types Type
            (
            );
            /**Sets  the split type  <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetType
            (
                NXOpen::CAE::ElementSplitBuilder::Types type /** type */ 
            );
            /**Returns  the selected elements in old journal files
                        JA_ELEMENT_SPLIT_BUILDER_get_elements to be removed in NX8.0 or later
             @deprecated Deprecated in NX7 <br> 
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::CAE::SelectFEElementList * Elements
            (
            );
            /**Returns  the selected elements  <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::CAE::SelectElementsBuilder * Elementsss
            (
            );
            /** Flip will not be journaled now <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void Flip
            (
            );
            /**Returns  the flip_type for first element in the selection list <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: int FirstElementSplitType
            (
            );
            /**Sets  the flip_type for first element in the selection list <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetFirstElementSplitType
            (
                int data /** data */ 
            );
            /**Returns  the point1, one end of line when split by line <br> License requirements : None */
            public: NXOpen::Point * Point1
            (
            );
            /**Sets  the point1, one end of line when split by line <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetPoint1
            (
                NXOpen::Point * point1 /** point1 */ 
            );
            /**Returns  the point2, the other end of line when split by line  <br> License requirements : None */
            public: NXOpen::Point * Point2
            (
            );
            /**Sets  the point2, the other end of line when split by line  <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetPoint2
            (
                NXOpen::Point * point2 /** point2 */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif