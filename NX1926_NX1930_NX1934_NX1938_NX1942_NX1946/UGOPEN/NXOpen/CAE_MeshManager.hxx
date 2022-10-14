#ifndef NXOpen_CAE_MESHMANAGER_HXX_INCLUDED
#define NXOpen_CAE_MESHMANAGER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_MeshManager.ja
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
#include <NXOpen/CAE_PrimitiveRecipeMeshBuilder.hxx>
#include <NXOpen/CAE_IMeshManager.hxx>
#include <NXOpen/libnxopencpp_cae_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace CAE
    {
        class MeshManager;
    }
    class Body;
    namespace CAE
    {
        class CAEBody;
    }
    namespace CAE
    {
        class CAEFace;
    }
    namespace CAE
    {
        class ContactMeshBuilder;
    }
    namespace CAE
    {
        class DependentMesh;
    }
    namespace CAE
    {
        class DependentMeshBuilder;
    }
    namespace CAE
    {
        class IMeshCollector;
    }
    namespace CAE
    {
        class IMeshManager;
    }
    namespace CAE
    {
        class ImmersedBoundaryMeshBuilder;
    }
    namespace CAE
    {
        class LocalRemeshBuilder;
    }
    namespace CAE
    {
        class MappedMesh;
    }
    namespace CAE
    {
        class MappedMeshBuilder;
    }
    namespace CAE
    {
        class Mesh;
    }
    namespace CAE
    {
        class Mesh0d;
    }
    namespace CAE
    {
        class Mesh0dBuilder;
    }
    namespace CAE
    {
        class Mesh1d;
    }
    namespace CAE
    {
        class Mesh1dBuilder;
    }
    namespace CAE
    {
        class Mesh2d;
    }
    namespace CAE
    {
        class Mesh2dBuilder;
    }
    namespace CAE
    {
        class Mesh2dFromFacets;
    }
    namespace CAE
    {
        class Mesh2dFromFacetsBuilder;
    }
    namespace CAE
    {
        class Mesh3d;
    }
    namespace CAE
    {
        class Mesh3dHexBuilder;
    }
    namespace CAE
    {
        class Mesh3dHybridBuilder;
    }
    namespace CAE
    {
        class Mesh3dTetBuilder;
    }
    namespace CAE
    {
        class MeshCollector;
    }
    namespace CAE
    {
        class MeshCollectorBuilder;
    }
    namespace CAE
    {
        class MeshRefinementBuilder;
    }
    namespace CAE
    {
        class MeshShellFromSolid;
    }
    namespace CAE
    {
        class PrimitiveMeshBuilder;
    }
    namespace CAE
    {
        class PrimitiveRecipeMesh;
    }
    namespace CAE
    {
        class PrimitiveRecipeMeshBuilder;
    }
    namespace CAE
    {
        class ProjectNodesToCadGeometryBuilder;
    }
    namespace CAE
    {
        class ReassignElementsBuilder;
    }
    namespace CAE
    {
        class Shell2SolidBuilder;
    }
    namespace CAE
    {
        class ShellTo3dHybridBuilder;
    }
    namespace CAE
    {
        class ShipMeshAutomation;
    }
    namespace CAE
    {
        class ShipMeshAutomationBuilder;
    }
    namespace CAE
    {
        class SurfaceCoatBuilder;
    }
    namespace CAE
    {
        class SweptMesh;
    }
    namespace CAE
    {
        class WeldBuilder;
    }
    class Face;
    namespace CAE
    {
        class _MeshManagerBuilder;
        class MeshManagerImpl;
        /**  @brief  Creates Meshes@link NXOpen::CAE::Mesh NXOpen::CAE::Mesh@endlink  in a fem part  

          
         <br>  Created in NX6.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  MeshManager : public NXOpen::CAE::IMeshManager
        {
            private: MeshManagerImpl * m_meshmanager_impl;
            private: friend class  _MeshManagerBuilder;
            protected: MeshManager();
            public: ~MeshManager();
            /** Creates a mapped mesh builder 
                      @return  Mapped Mesh Builder is created 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::CAE::MappedMeshBuilder * CreateMappedMeshBuilder
            (
                NXOpen::CAE::MappedMesh * mappedMesh /** Mapped Mesh entity to be edited, if NULL then create a new one */
            );
            /** Creates a dependent mesh builder 
                      @return  Dependent Mesh Builder is created 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::CAE::DependentMeshBuilder * CreateDependentMeshBuilder
            (
                NXOpen::CAE::DependentMesh * dependentMesh /** Dependent Mesh entity to be edited, if NULL then create a new one */
            );
            /** Creates a 0d mesh builder 
                      @return  0d Mesh Builder is created 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::CAE::Mesh0dBuilder * CreateMesh0dBuilder
            (
                NXOpen::CAE::Mesh0d * mesh /** 0d Mesh entity to be edited, if NULL then create a new one */
            );
            /** Creates a 1d mesh builder 
                      @return  1d Mesh Builder is created 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::CAE::Mesh1dBuilder * CreateMesh1dBuilder
            (
                NXOpen::CAE::Mesh1d * mesh /** 1d Mesh entity to be edited, if NULL then create a new one */
            );
            /** Creates a 2d mesh builder 
                      @return  2d Mesh Builder is created 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_easyfill_advanced (" Easy Fill Advanced") */
            public: NXOpen::CAE::Mesh2dBuilder * CreateMesh2dBuilder
            (
                NXOpen::CAE::Mesh2d * mesh /** 2d Mesh entity to be edited, if NULL then create a new one */
            );
            /** Creates a ship mesh automation builder 
                      @return  Ship Mesh Automation Builder is created 
             <br>  Created in NX11.0.2.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling"), nx_ship_basic ("Ship Basic Design") */
            public: NXOpen::CAE::ShipMeshAutomationBuilder * CreateShipMeshAutomationBuilder
            (
                NXOpen::CAE::ShipMeshAutomation * mesh /** Ship Mesh Automation entity to be edited, if NULL then create a new one */
            );
            /** Creates a 3d Tet mesh builder 
                      @return  2d Mesh Builder is created 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::CAE::Mesh3dTetBuilder * CreateMesh3dTetBuilder
            (
                NXOpen::CAE::Mesh3d * mesh /** 3d Mesh entity to be edited, if NULL then create a new one */
            );
            /** Creates a 3d Hex mesh builder 
                      @return  2d Mesh Builder is created 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::CAE::Mesh3dHexBuilder * CreateMesh3dHexBuilder
            (
                NXOpen::CAE::SweptMesh * mesh /** 3d Mesh entity to be edited, if NULL then create a new one */
            );
            /** Creates a hybrid mesh builder 
                      @return  2d Mesh Builder is created 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::CAE::Mesh3dHybridBuilder * CreateMesh3dHybridBuilder
            (
                NXOpen::CAE::Mesh * mesh /** Mesh entity to be edited, if NULL then create a new one */
            );
            /** Creates an immersed boundary mesh builder 
                      @return  Immersed Boundary Mesh Builder is created 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::CAE::ImmersedBoundaryMeshBuilder * CreateImmersedBoundaryMeshBuilder
            (
                NXOpen::CAE::Mesh * mesh /** Mesh entity to be edited, if NULL then create a new one */
            );
            /** Creates a shell to solid builder 
                      @return  2d Mesh Builder is created 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::CAE::Shell2SolidBuilder * CreateShell2solidBuilder
            (
                NXOpen::CAE::Mesh3d * mesh /** 3d Mesh entity to be edited, if NULL then create a new one */
            );
            /** Creates a shell to 3d hybrid builder 
                      @return  2d Mesh Builder is created 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::CAE::ShellTo3dHybridBuilder * CreateShellto3dhybridBuilder
            (
                NXOpen::CAE::Mesh3d * mesh /** 3d Mesh entity to be edited, if NULL then create a new one */
            );
            /** Creates a shell from solid (surface coat) builder 
                      @return  Mesh Builder is created 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::CAE::SurfaceCoatBuilder * CreateSurfaceCoatBuilder
            (
                NXOpen::CAE::MeshShellFromSolid * mesh /** Mesh entity to be edited, if NULL then create a new one */
            );
            /** Creates a local remesh builder 
                      @return  Mesh Builder is created 
             <br>  Created in NX7.5.2.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::CAE::LocalRemeshBuilder * CreateLocalRemeshBuilder
            (
            );
            /** Creates a builder for editing an existng primitive mesh.
                      @return  Mesh Builder is created 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::CAE::PrimitiveMeshBuilder * CreatePrimitiveMeshBuilder
            (
                NXOpen::CAE::Mesh * mesh /** Primitive Mesh entity to be edited. */
            );
            /** Creates a builder for creating a primitive mesh of the specified type.
                      @return  Mesh Builder is created 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::CAE::PrimitiveMeshBuilder * CreatePrimitiveMeshBuilder
            (
                const NXString & meshType /** name of the type of primitive mesh */
            );
            /** Creates a builder for creating a primitive mesh of the specified type.
                      @return  Mesh Builder is created 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            NXOpen::CAE::PrimitiveMeshBuilder * CreatePrimitiveMeshBuilder
            (
                const char * meshType /** name of the type of primitive mesh */
            );
            /** Creates a mesh collector builder for the mesh collector object
                      @return  MeshCollector Builder 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::CAE::MeshCollectorBuilder * CreateCollectorBuilder
            (
                NXOpen::CAE::MeshCollector * meshCollector /** @link NXOpen::CAE::MeshCollector NXOpen::CAE::MeshCollector@endlink  to be edited,
                                                                                        if NULL  then create a new one */,
                const NXString & pElementCollectorContainerName /** the valid Element Collector Container descriptor neutral name */
            );
            /** Creates a mesh collector builder for the mesh collector object
                      @return  MeshCollector Builder 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            NXOpen::CAE::MeshCollectorBuilder * CreateCollectorBuilder
            (
                NXOpen::CAE::MeshCollector * meshCollector /** @link NXOpen::CAE::MeshCollector NXOpen::CAE::MeshCollector@endlink  to be edited,
                                                                                        if NULL  then create a new one */,
                const char * pElementCollectorContainerName /** the valid Element Collector Container descriptor neutral name */
            );
            /** Creates a builder for element transfer to collector command
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::CAE::ReassignElementsBuilder * CreateReassignElementsBuilder
            (
            );
            /** Renames a mesh collector object 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetMeshCollectorName
            (
                NXOpen::CAE::MeshCollector * meshCollector /** @link NXOpen::CAE::MeshCollector NXOpen::CAE::MeshCollector@endlink  to be renamed */,
                const NXString & collectorName /** The new name being assigned or set */
            );
            /** Renames a mesh collector object 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            void SetMeshCollectorName
            (
                NXOpen::CAE::MeshCollector * meshCollector /** @link NXOpen::CAE::MeshCollector NXOpen::CAE::MeshCollector@endlink  to be renamed */,
                const char * collectorName /** The new name being assigned or set */
            );
            /** Call for doing Drag n Drop of a given Mesh across Mesh Collectors 
             <br>  @deprecated Deprecated in NX12.0.0.  Use @link NXOpen::CAE::MeshManager::MoveMeshToNewCollector NXOpen::CAE::MeshManager::MoveMeshToNewCollector@endlink  instead. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NX_DEPRECATED("Deprecated in NX12.0.0.  Use NXOpen::CAE::MeshManager::MoveMeshToNewCollector instead.") void DragNDropMesh
            (
                NXOpen::CAE::Mesh * mesh /** @link NXOpen::CAE::Mesh NXOpen::CAE::Mesh@endlink  being Dragged and Dropped */,
                NXOpen::CAE::MeshCollector * sourceMeshCollector /** Source @link NXOpen::CAE::MeshCollector NXOpen::CAE::MeshCollector@endlink  */,
                NXOpen::CAE::MeshCollector * targetMeshCollector /** Target @link NXOpen::CAE::MeshCollector NXOpen::CAE::MeshCollector@endlink  */
            );
            /** Call for moving a Mesh to a new Mesh Collector 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void MoveMeshToNewCollector
            (
                NXOpen::CAE::Mesh * mesh /** @link NXOpen::CAE::Mesh NXOpen::CAE::Mesh@endlink  being Dragged and Dropped */,
                bool keepMeshDisplaySettings /** if true, keep the Mesh display settings intact, else assign the MeshCollector defaults */,
                NXOpen::CAE::MeshCollector * sourceMeshCollector /** Source @link NXOpen::CAE::MeshCollector NXOpen::CAE::MeshCollector@endlink  */,
                NXOpen::CAE::MeshCollector * targetMeshCollector /** Target @link NXOpen::CAE::MeshCollector NXOpen::CAE::MeshCollector@endlink  */
            );
            /** Creates a project nodes to cad geometry builder 
                      @return   
             <br>  Created in NX6.0.4.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::CAE::ProjectNodesToCadGeometryBuilder * CreateProjectNodesToCadGeometryBuilder
            (
            );
            /** Call for doing Merge Meshes  @return  The Merged Mesh @link NXOpen::CAE::Mesh NXOpen::CAE::Mesh@endlink  
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::CAE::Mesh * MergeMeshes
            (
                const std::vector<NXOpen::CAE::Mesh *> & selectedMeshes /** Array of Meshes being merged @link NXOpen::CAE::Mesh NXOpen::CAE::Mesh@endlink  */
            );
            /** Creates a @link NXOpen::CAE::WeldBuilder NXOpen::CAE::WeldBuilder@endlink 
                      @return  Weld Builder is created 
             <br>  Created in NX7.5.2.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::CAE::WeldBuilder * CreateWeldBuilder
            (
                NXOpen::CAE::Mesh * mesh /** Weld entity to be edited, if NULL then creates a new one */
            );
            /** Creates a @link NXOpen::CAE::ContactMeshBuilder NXOpen::CAE::ContactMeshBuilder@endlink 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::CAE::ContactMeshBuilder * CreateContactMeshBuilder
            (
                NXOpen::CAE::Mesh1d * contactMesh /** @link NXOpen::CAE::Mesh1d NXOpen::CAE::Mesh1d@endlink  to be edited, 
                                                                                             if NULL then create a new one */
            );
            /** Creates a @link NXOpen::CAE::MeshRefinementBuilder NXOpen::CAE::MeshRefinementBuilder@endlink 
                      @return  Mesh Refinement Builder is created 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::CAE::MeshRefinementBuilder * CreateMeshRefinementBuilder
            (
            );
            /** Creates a builder for editing an existing primitive recipe mesh.
                      @return  Primitive Recipe Mesh Builder is created 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::CAE::PrimitiveRecipeMeshBuilder * CreatePrimitiveRecipeMeshBuilder
            (
                NXOpen::CAE::PrimitiveRecipeMesh * mesh /** Primitive Recipe Mesh entity to be edited. */
            );
            /** Creates a builder for creating a new primitive recipe mesh of the specified type.
                      @return  Primitive Recipe Mesh Builder is created 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::CAE::PrimitiveRecipeMeshBuilder * CreatePrimitiveRecipeMeshBuilder
            (
                NXOpen::CAE::PrimitiveRecipeMeshBuilder::Type primitiveType /** type of primitive recipe mesh */
            );
            /** Creates a 2d mesh from facets builder 
                      @return  2d Mesh Form Facets Builder is created 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::CAE::Mesh2dFromFacetsBuilder * CreateMesh2dFromFacetsBuilder
            (
                NXOpen::CAE::Mesh2dFromFacets * mesh /** 2d Mesh From Facets entity to be edited, if NULL then create a new one */
            );
            /** Clone a Mesh Collector
                      @return  Newly created 2d Mesh Collector 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::CAE::MeshCollector * MeshCollectorClone
            (
                NXOpen::CAE::IMeshCollector * sourceColl /** 2d Mesh Collector to be cloned. Must be in the same part as the CAE.MeshManager */
            );
            /** Calculate the auto element size for a given array of bodies
                      @return  the calculated element size 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: double GetAutoElementSize
            (
                const std::vector<NXOpen::CAE::CAEBody *> & bodies /** array of bodies */
            );
            /** Calculate the auto element size for a given array of faces
                      @return  the calculated element size 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: double GetAutoElementSize
            (
                const std::vector<NXOpen::CAE::CAEFace *> & faces /** array of faces */
            );
            /** Calculate the auto element size for a given array of solid bodies
                      @return  the calculated element size 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: double GetAutoElementSize
            (
                const std::vector<NXOpen::Body *> & faces /** array of solid modeling bodies */
            );
            /** Calculate the auto element size for a given array of solid faces
                      @return  the calculated element size 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: double GetAutoElementSize
            (
                const std::vector<NXOpen::Face *> & faces /** array of solid modeling faces */
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