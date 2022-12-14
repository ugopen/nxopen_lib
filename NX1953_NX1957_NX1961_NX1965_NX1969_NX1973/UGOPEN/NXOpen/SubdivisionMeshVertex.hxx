#ifndef NXOpen_SUBDIVISIONMESHVERTEX_HXX_INCLUDED
#define NXOpen_SUBDIVISIONMESHVERTEX_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     SubdivisionMeshVertex.ja
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
#include <NXOpen/ugmath.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    class SubdivisionMeshVertex;
    class DisplayableObject;
    class SubdivisionMeshBody;
    class SubdivisionMeshEdge;
    class SubdivisionMeshFace;
    class _SubdivisionMeshVertexBuilder;
    class SubdivisionMeshVertexImpl;
    /** Represents a subdivision mesh vertex. 
     <br>  Created in NX9.0.0.  <br>  
    */
    class NXOPENCPPEXPORT  SubdivisionMeshVertex : public NXOpen::DisplayableObject
    {
        private: SubdivisionMeshVertexImpl * m_subdivisionmeshvertex_impl;
        private: friend class  _SubdivisionMeshVertexBuilder;
        protected: SubdivisionMeshVertex();
        public: ~SubdivisionMeshVertex();
        /** Returns the mesh owning this vertex.  @return  
         <br>  Created in NX9.0.0.  <br>  
         <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
        public: NXOpen::SubdivisionMeshBody * GetBody
        (
        );
        /** Returns the faces connected to the vertex.  @return  
         <br>  Created in NX9.0.0.  <br>  
         <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
        public: std::vector<NXOpen::SubdivisionMeshFace *> GetFaces
        (
        );
        /** Returns the edges connected to the vertex.  @return  
         <br>  Created in NX9.0.0.  <br>  
         <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
        public: std::vector<NXOpen::SubdivisionMeshEdge *> GetEdges
        (
        );
        /**Returns  the position of the vertex. 
         <br>  Created in NX9.0.0.  <br>  
         <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
        public: NXOpen::Point3d Coordinates
        (
        );
        /**Sets  the position of the vertex. 
         <br>  Created in NX9.0.0.  <br>  
         <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
        public: void SetCoordinates
        (
            const NXOpen::Point3d & position /** position */ 
        );
    };
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
