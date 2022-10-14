#ifndef NXOpen_CAE_MAPPEDMESHBUILDER_HXX_INCLUDED
#define NXOpen_CAE_MAPPEDMESHBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_MappedMeshBuilder.ja
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
#include <NXOpen/CAE_MappedMeshBuilder.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAE
    {
        class MappedMeshBuilder;
    }
    class Builder;
    class NXObject;
    class SelectDisplayableObjectList;
    namespace CAE
    {
        class _MappedMeshBuilderBuilder;
        /**
            Represents a Mapped Mesh Builder.  Used to create a @link CAE::MappedMesh CAE::MappedMesh@endlink 
             <br> To create a new instance of this class, use @link CAE::MeshManager::CreateMappedMeshBuilder CAE::MeshManager::CreateMappedMeshBuilder@endlink  <br> */
        class NXOPENCPPEXPORT MappedMeshBuilder : public Builder
        {
            /** Mid-node placement options */
            public: enum MidNodeType
            {
                MidNodeTypeMixed/** Mixed    Option */,
                MidNodeTypeStraight/** Straight Option */,
                MidNodeTypeCurved/** Curved   Option */
            };

            private: friend class  _MappedMeshBuilderBuilder;
            protected: MappedMeshBuilder();
            /** Returns the corner data  @return   <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: std::vector<NXOpen::NXObject *> GetCornerData
            (
                NXOpen::NXObject ** face /** face */ 
            );
            public: void SetCornerData
            (
                NXOpen::NXObject * face /** face */ ,
                const std::vector<NXOpen::NXObject *> & vertexList /** vertex list */ 
            );
            /**Returns  the elem type name. This name is solver environment dependent. These are
                        the same names that show up in the meshing dialogues. Refer to the 
                        release specific CAE user documentation to set a specific element name
                        desired for a specific solver environment in a given release, refer
                        to the release specific user manual   <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXString ElementType
            (
            );
            /**Sets  the elem type name. This name is solver environment dependent. These are
                        the same names that show up in the meshing dialogues. Refer to the 
                        release specific CAE user documentation to set a specific element name
                        desired for a specific solver environment in a given release, refer
                        to the release specific user manual   <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetElementType
            (
                const NXString & typeOfElement /** type of element */ 
            );
            /**Returns  the ECC automatic mode option  <br> License requirements : None */
            public: bool EccAuto
            (
            );
            /**Sets  the ECC automatic mode option  <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetEccAuto
            (
                bool eccAutoOption /** ecc auto option */ 
            );
            /**Returns  the ECC name  <br> License requirements : None */
            public: NXString EccName
            (
            );
            /**Sets  the ECC name  <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetEccName
            (
                const NXString & eccName /** eccname */ 
            );
            /**Returns  the selection face  <br> License requirements : None */
            public: NXOpen::SelectDisplayableObjectList * SelectionFace
            (
            );
            /** Returns the edge density  <br> License requirements : None */
            public: void ChangeEdgeDensity
            (
                NXOpen::NXObject * edge /** edge */ ,
                int numberElements /** number elements */ 
            );
            /**Returns  the element size  <br> License requirements : None */
            public: double ElementSize
            (
            );
            /**Sets  the element size  <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetElementSize
            (
                double elementSize /** element size */ 
            );
            /**  Auto-generated element size  @return   <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: double AutoSize
            (
            );
            /**Returns  the jacobian  <br> License requirements : None */
            public: double Jacobian
            (
            );
            /**Sets  the jacobian  <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetJacobian
            (
                double jacobian /** jacobian */ 
            );
            /**Returns  the mid node opt  <br> License requirements : None */
            public: NXOpen::CAE::MappedMeshBuilder::MidNodeType MidNodeOption
            (
            );
            /**Sets  the mid node opt  <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetMidNodeOption
            (
                NXOpen::CAE::MappedMeshBuilder::MidNodeType midNodeType /** mid node type */ 
            );
            /**Returns  the edge match tolerance  <br> License requirements : None */
            public: double EdgeMatchTolerance
            (
            );
            /**Sets  the edge match tolerance  <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetEdgeMatchTolerance
            (
                double edgeMatchTolerance /** edge match tolerance */ 
            );
            /**Returns  the format mesh option  <br> License requirements : None */
            public: bool FormatMesh
            (
            );
            /**Sets  the format mesh option  <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetFormatMesh
            (
                bool formatMeshOption /** format mesh option */ 
            );
            /**Returns  the quad only mesh option  <br> License requirements : None */
            public: bool QuadOnlyMesh
            (
            );
            /**Sets  the quad only mesh option  <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetQuadOnlyMesh
            (
                bool quadOnlyMeshOption /** quad only mesh option */ 
            );
            /**Returns  the keep free meshes option  <br> License requirements : None */
            public: bool KeepFreeMeshes
            (
            );
            /**Sets  the keep free meshes option  <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetKeepFreeMeshes
            (
                bool quadOnlyMeshOption /** quad only mesh option */ 
            );
            /**Returns  the merge edges option  <br> License requirements : None */
            public: bool MergeEdges
            (
            );
            /**Sets  the merge edges option  <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetMergeEdges
            (
                bool mergeEdgesOption /** merge edges option */ 
            );
            /**Returns  the edge merge angle  <br> License requirements : None */
            public: double EdgeMergeAngle
            (
            );
            /**Sets  the edge merge angle  <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetEdgeMergeAngle
            (
                double edgeMergeAngle /** edge merge angle */ 
            );
            /** Previews the mapped mesh for further edit. After preview, corner definition is allowed.  <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void PreviewMesh
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif