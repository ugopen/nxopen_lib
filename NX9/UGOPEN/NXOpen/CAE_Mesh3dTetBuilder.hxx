#ifndef NXOpen_CAE_MESH3DTETBUILDER_HXX_INCLUDED
#define NXOpen_CAE_MESH3DTETBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_Mesh3dTetBuilder.ja
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
#include <NXOpen/CAE_Mesh3dTetBuilder.hxx>
#include <NXOpen/SelectObjectList.hxx>
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
        class Mesh3dTetBuilder;
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
        class PropertyTable;
    }
    namespace CAE
    {
        class SelectCAEFaceList;
    }
    class SelectDisplayableObjectList;
    namespace CAE
    {
        class _Mesh3dTetBuilderBuilder;
        class Mesh3dTetBuilderImpl;
        /** Represents 3D Mesh
             *  Used to create a @link CAE::Mesh3d CAE::Mesh3d@endlink 
             <br> To create a new instance of this class, use @link CAE::MeshManager::CreateMesh3dTetBuilder  CAE::MeshManager::CreateMesh3dTetBuilder @endlink  <br> 
         <br>  Created in NX6.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  Mesh3dTetBuilder : public Builder
        {
            private: Mesh3dTetBuilderImpl * m_mesh3dtetbuilder_impl;
            private: friend class  _Mesh3dTetBuilderBuilder;
            protected: Mesh3dTetBuilder();
            public: ~Mesh3dTetBuilder();
            /**Returns  the fillet selection 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::CAE::SelectCAEFaceList * SelectionFillet
            (
            );
            /**Returns  the cylinder selection 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: bool AutoSizeOption
            (
            );
            /**Sets  the cylinder selection 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetAutoSizeOption
            (
                bool fAutoSize /** fautosize */ 
            );
            /**Returns  the auto reset geometry option. All manually performed edits will be removed if this option is true.
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: bool AutoResetOption
            (
            );
            /**Sets  the auto reset geometry option. All manually performed edits will be removed if this option is true.
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetAutoResetOption
            (
                bool fAutoReset /** fautoreset */ 
            );
            /**Returns  the selection objects 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::SelectDisplayableObjectList * SelectionList
            (
            );
            /**Returns  the element type builder.  
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::CAE::ElementTypeBuilder * ElementType
            (
            );
            /**Returns  the property table associated with the mesh. 
                        The property table contains the parameters needed for the generation
                        of the mesh.  
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::CAE::PropertyTable * PropertyTable
            (
            );
            /** Commits the creation of the 
                                     @link CAE::Mesh0d CAE::Mesh0d@endlink ,
                                     @link CAE::Mesh1d CAE::Mesh1d@endlink ,
                                     @link CAE::Mesh2d CAE::Mesh2d@endlink ,
                                     @link CAE::Mesh3d CAE::Mesh3d@endlink  object
                        or Commits the changes made to the @link CAE::Mesh0d CAE::Mesh0d@endlink ,
                                     @link CAE::Mesh1d CAE::Mesh1d@endlink ,
                                     @link CAE::Mesh2d CAE::Mesh2d@endlink ,
                                     @link CAE::Mesh3d CAE::Mesh3d@endlink  object.
                      @return  
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: std::vector<NXOpen::CAE::Mesh *> CommitMesh
            (
            );
            /** Commits the creation of the @link CAE::Mesh3d CAE::Mesh3d@endlink  object
                        or Commits the changes made to the @link CAE::Mesh3d CAE::Mesh3d@endlink  object 
                        returns with partial meshes if 3d Tetrahedral meshing fails.
                      @return  
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: std::vector<NXOpen::CAE::Mesh *> CommitWithPartialMesh
            (
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
