#ifndef NXOpen_CAE_MESH_HXX_INCLUDED
#define NXOpen_CAE_MESH_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_Mesh.ja
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
#include <NXOpen/DisplayableObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAE
    {
        class Mesh;
    }
    namespace CAE
    {
        class IMeshCollector;
    }
    namespace CAE
    {
        class PropertyTable;
    }
    class DisplayableObject;
    namespace CAE
    {
        class _MeshBuilder;
        class MeshImpl;
        /** Represents Mesh Recipe  <br> This is an abstract class <br> */
        class NXOPENCPPEXPORT  Mesh : public DisplayableObject
        {
            private: MeshImpl * m_mesh_impl;
            private: friend class  _MeshBuilder;
            protected: Mesh();
            public: ~Mesh();
            /**Returns  the element property table associated with the mesh object  <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::PropertyTable * ElementPropertyTable
            (
            );
            /**Returns  the lock status for this mesh. If a mesh is locked then it will not 
                        update when the FE Model is updated. Meshes are typically locked
                        by the use of manual node and element commands.  <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: bool LockStatus
            (
            );
            /**Sets  the lock status for this mesh. If a mesh is locked then it will not 
                        update when the FE Model is updated. Meshes are typically locked
                        by the use of manual node and element commands.  <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetLockStatus
            (
                bool lockStatus /** lock status */ 
            );
            /**Returns  the MeshCollector for this mesh.  
                      <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::IMeshCollector * MeshCollector
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
