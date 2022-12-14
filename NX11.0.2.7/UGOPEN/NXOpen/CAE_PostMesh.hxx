#ifndef NXOpen_CAE_POSTMESH_HXX_INCLUDED
#define NXOpen_CAE_POSTMESH_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_PostMesh.ja
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
#include <NXOpen/CAE_PostMesh.hxx>
#include <NXOpen/CAE_Result.hxx>
#include <NXOpen/TaggedObject.hxx>
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
        class PostMesh;
    }
    namespace CAE
    {
        class _PostMeshBuilder;
        class PostMeshImpl;
        /**  @brief  This class has the information related to post mesh group.
            Not Each attribute of this class is relevent for all the purpose. The best way 
            To use this class is to first check if the attribute is set before using it, 
            if user is not sure.
             

          <br> An instance of this class can not be obtained  <br> 
         <br>  Created in NX11.0.2.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  PostMesh : public NXOpen::TaggedObject
        {
            private: PostMeshImpl * m_postmesh_impl;
            private: friend class  _PostMeshBuilder;
            protected: PostMesh();
            public: ~PostMesh();
            /**Returns  the pid of the post mesh 
             <br>  Created in NX11.0.2.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: int PropertyId
            (
            );
            /**Returns  the mid of the post mesh 
             <br>  Created in NX11.0.2.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: int MaterialId
            (
            );
            /**Returns  the part id of the post mesh 
             <br>  Created in NX11.0.2.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: int PartId
            (
            );
            /**Returns  the cid of the post mesh 
             <br>  Created in NX11.0.2.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: int CollectorId
            (
            );
            /**Returns  the type of the post mesh 
             <br>  Created in NX11.0.2.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: int Type
            (
            );
            /**Returns  the typedesc of the post mesh 
             <br>  Created in NX11.0.2.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXString TypeDescription
            (
            );
            /**Returns  the matdesc of the post mesh 
             <br>  Created in NX11.0.2.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXString MaterialDescription
            (
            );
            /**Returns  the propdesc of the post mesh 
             <br>  Created in NX11.0.2.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXString PropertyDescription
            (
            );
            /**Returns  the number of elements in the post mesh 
             <br>  Created in NX11.0.2.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: int Numelem
            (
            );
            /**Returns  the imension of the mesh 
             <br>  Created in NX11.0.2.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::Result::GroupContainer MeshDimension
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
