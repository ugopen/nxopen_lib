#ifndef NXOpen_CAE_SURFACECOATBUILDER_HXX_INCLUDED
#define NXOpen_CAE_SURFACECOATBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_SurfaceCoatBuilder.ja
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
#include <NXOpen/Builder.hxx>
#include <NXOpen/CAE_ElementTypeBuilder.hxx>
#include <NXOpen/CAE_SelectElementsBuilder.hxx>
#include <NXOpen/CAE_SurfaceCoatBuilder.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAE
    {
        class SurfaceCoatBuilder;
    }
    class Builder;
    namespace CAE
    {
        class ElementTypeBuilder;
    }
    namespace CAE
    {
        class Mesh;
    }
    namespace CAE
    {
        class SelectElementsBuilder;
    }
    class SelectTaggedObjectList;
    namespace CAE
    {
        class _SurfaceCoatBuilderBuilder;
        class SurfaceCoatBuilderImpl;
        /**
            Builder for creating Surface Coat
             <br> To create a new instance of this class, use @link CAE::MeshManager::CreateSurfaceCoatBuilder CAE::MeshManager::CreateSurfaceCoatBuilder@endlink  <br> */
        class NXOPENCPPEXPORT  SurfaceCoatBuilder : public Builder
        {
            /** Represents the selection method to be used */
            public: enum SelectionMethod
            {
                SelectionMethodThreeDimensionMesh/** 3D mesh */,
                SelectionMethodElementFreeFace/** Element free faces */,
                SelectionMethodGeometry/** Face or body */
            };

            private: SurfaceCoatBuilderImpl * m_surfacecoatbuilder_impl;
            private: friend class  _SurfaceCoatBuilderBuilder;
            protected: SurfaceCoatBuilder();
            public: ~SurfaceCoatBuilder();
            /**Returns  the selection method for different ways of selection  <br> License requirements : None */
            public: NXOpen::CAE::SurfaceCoatBuilder::SelectionMethod SelectionMethodType
            (
            );
            /**Sets  the selection method for different ways of selection  <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetSelectionMethodType
            (
                NXOpen::CAE::SurfaceCoatBuilder::SelectionMethod selectionMethodType /** selectionmethodtype */ 
            );
            /**Returns  the selected source object(s)  <br> License requirements : None */
            public: NXOpen::SelectTaggedObjectList * SourceMesh
            (
            );
            /**Returns  the selected geometry object(s)  <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::SelectTaggedObjectList * SelectGeometry
            (
            );
            /**Returns  the selected element face(s)  <br> License requirements : None */
            public: NXOpen::CAE::SelectElementsBuilder * ElementFace
            (
            );
            /**Returns  the element type to be created <br> License requirements : None */
            public: NXOpen::CAE::ElementTypeBuilder * ElementType
            (
            );
            /**Returns  the export to solver toggle  <br> License requirements : None */
            public: bool ExportToSolver
            (
            );
            /**Sets  the export to solver toggle  <br> License requirements : None */
            public: void SetExportToSolver
            (
                bool fExportToSolver /** fexporttosolver */ 
            );
            /** Commit the mesh  @return   <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::CAE::Mesh * CommitMesh
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif