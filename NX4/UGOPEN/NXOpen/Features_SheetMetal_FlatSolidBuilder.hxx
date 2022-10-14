#ifndef NXOpen_FEATURES_SHEETMETAL_FLATSOLIDBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_SHEETMETAL_FLATSOLIDBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_SheetMetal_FlatSolidBuilder.ja
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
#include <NXOpen/ugmath.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Features
    {
        namespace SheetMetal
        {
            class FlatSolidBuilder;
        }
    }
    class Edge;
    class Face;
    namespace Features
    {
        class FeatureBuilder;
    }
    namespace Features
    {
        namespace SheetMetal
        {
            class _FlatSolidBuilderBuilder;
            /** Represents a Flat As Solid feature builder. */
            class NXOPENCPPEXPORT FlatSolidBuilder : public Features::FeatureBuilder
            {
                private: friend class  _FlatSolidBuilderBuilder;
                protected: FlatSolidBuilder();
                /**Returns  the face on which the flat as solid is created.
                                 <br> 
                                The face should be planar and should not be an unformed bend face.
                                 <br> 
                             <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: NXOpen::Face * ReferenceFace
                (
                );
                /**Sets  the face on which the flat as solid is created.
                                 <br> 
                                The face should be planar and should not be an unformed bend face.
                                 <br> 
                             <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: void SetReferenceFace
                (
                    NXOpen::Face * face /** The flat as solid is created on this face. */
                );
                /**Returns  the edge which decides the X axis of the flat as solid.
                                 <br> 
                                The edge should not be a thickness edge.
                                 <br> 
                             <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: NXOpen::Edge * ReferenceEdge
                (
                );
                /**Sets  the edge which decides the X axis of the flat as solid.
                                 <br> 
                                The edge should not be a thickness edge.
                                 <br> 
                             <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: void SetReferenceEdge
                (
                    NXOpen::Edge * edge /** The flange is created on this edge. */
                );
                /**Returns  the end of the edge where the tangent will define the x axis for flat as solid.
                             <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: NXOpen::Point3d ReferenceVertex
                (
                );
                /**Sets  the end of the edge where the tangent will define the x axis for flat as solid.
                             <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: void SetReferenceVertex
                (
                    const NXOpen::Point3d & vertex /** One of the end points of the reference edge. */
                );
                /**Returns  the flag which decides if the flattened solid will be transformed to Absolute CSYS.
                             <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: bool TransformToAbsoluteCsys
                (
                );
                /**Sets  the flag which decides if the flattened solid will be transformed to Absolute CSYS.
                             <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: void SetTransformToAbsoluteCsys
                (
                    bool transform_flag /** True = Transform to ABS, False = Do not transform to ABS. */
                );
                /** Validate the builder data  @return  0 Means no errors.  <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: int ValidateBuilderData
                (
                );
            };
        }
    }
}
#undef EXPORTLIBRARY
#endif