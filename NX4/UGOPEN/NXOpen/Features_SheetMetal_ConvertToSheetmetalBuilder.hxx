#ifndef NXOpen_FEATURES_SHEETMETAL_CONVERTTOSHEETMETALBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_SHEETMETAL_CONVERTTOSHEETMETALBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_SheetMetal_ConvertToSheetmetalBuilder.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Features_FeatureBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Features
    {
        namespace SheetMetal
        {
            class ConvertToSheetmetalBuilder;
        }
    }
    class Edge;
    class Expression;
    class Face;
    namespace Features
    {
        class FeatureBuilder;
    }
    namespace Features
    {
        class SketchFeature;
    }
    class Section;
    namespace Features
    {
        namespace SheetMetal
        {
            class _ConvertToSheetmetalBuilderBuilder;
            /** This is the feature builder for the convert to sheetmetal feature. */
            class NXOPENCPPEXPORT ConvertToSheetmetalBuilder : public Features::FeatureBuilder
            {
                /** This enum represents the bend relief type. */
                public: enum BendReliefTypeOptions
                {
                    BendReliefTypeOptionsNone/**  */,
                    BendReliefTypeOptionsSquare/**  */,
                    BendReliefTypeOptionsRound
                };

                private: friend class  _ConvertToSheetmetalBuilderBuilder;
                protected: ConvertToSheetmetalBuilder();
                /**Returns  the base face from which the thickness of the part is determined.
                         <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: NXOpen::Face * BaseFace
                (
                );
                /**Sets  the base face from which the thickness of the part is determined.
                         <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: void SetBaseFace
                (
                    NXOpen::Face * base_face /** */
                );
                /**Returns  the section containing curves that need to be ripped while converting to sheetmetal.
                         <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: NXOpen::Section * RipSection
                (
                );
                /**Sets  the section containing curves that need to be ripped while converting to sheetmetal.
                         <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: void SetRipSection
                (
                    NXOpen::Section * section /** */
                );
                /** Gets the array of edges selected for ripping while converting to sheetmetal.
                         @return   <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: std::vector<NXOpen::Edge *> GetRipEdges
                (
                );
                /**  Sets the array of edges that need to be ripped while converting to sheetmetal.
                         <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: void SetRipEdges
                (
                    const std::vector<NXOpen::Edge *> & rip_edges /** */
                );
                /**Returns  the bend relief type.
                         <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: NXOpen::Features::SheetMetal::ConvertToSheetmetalBuilder::BendReliefTypeOptions BendReliefType
                (
                );
                /**Sets  the bend relief type.
                         <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: void SetBendReliefType
                (
                    NXOpen::Features::SheetMetal::ConvertToSheetmetalBuilder::BendReliefTypeOptions bend_relief_type /** */
                );
                /**Returns  the bend relief width.
                         <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: NXOpen::Expression * BendReliefWidth
                (
                );
                /**  <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: void SetBendReliefWidth
                (
                    const NXString & bend_relief_width /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
                );
                /**Returns  the bend relief depth.
                         <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: NXOpen::Expression * BendReliefDepth
                (
                );
                /**  <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: void SetBendReliefDepth
                (
                    const NXString & bend_relief_depth /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
                );
                /**Returns  the internal sketch (used to specify rip curves), if it exists.
                         <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: NXOpen::Features::SketchFeature * Sketch
                (
                );
                /**Sets  the internal sketch (used to specify rip curves), if it exists.
                         <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: void SetSketch
                (
                    NXOpen::Features::SketchFeature * sketch /** */
                );
                /** Verify that the builder data is valid for feature creation. 
                             <br> 
                                 If the builder data is valid, it returns a value of 0.
                             <br> 
                         @return  data validity flag (0 - valid, 1 - invalid)  <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: int ValidateBuilderData
                (
                );
            };
        }
    }
}
#undef EXPORTLIBRARY
#endif