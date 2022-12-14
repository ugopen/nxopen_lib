#ifndef NXOpen_FACE_HXX_INCLUDED
#define NXOpen_FACE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Face.ja
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
#include <NXOpen/INXObject.hxx>
#include <NXOpen/IOrientation.hxx>
#include <NXOpen/IParameterizedSurface.hxx>
#include <NXOpen/IProfile.hxx>
#include <NXOpen/IReferenceAxis.hxx>
#include <NXOpen/ISurface.hxx>
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
    class Face;
    namespace Assemblies
    {
        class Component;
    }
    class BasePart;
    class Body;
    class ConvergentFacet;
    class DisplayableObject;
    class Edge;
    class INXObject;
    class IOrientation;
    class IParameterizedSurface;
    class IProfile;
    class IReferenceAxis;
    class ISurface;
    class _FaceBuilder;
    class FaceImpl;
    /** Represents a face 
     <br>  Created in NX3.0.0.  <br>  
    */
    class NXOPENCPPEXPORT  Face : public NXOpen::DisplayableObject, public virtual NXOpen::ISurface, public virtual NXOpen::IReferenceAxis, public virtual NXOpen::IProfile, public virtual NXOpen::IOrientation, public virtual NXOpen::IParameterizedSurface
    {
        /** Solid face type. */
        public: enum FaceType
        {
            FaceTypeRubber/** Rubber face, no surface attached */,
            FaceTypePlanar/** Planar face */,
            FaceTypeCylindrical/** Cylindrical face */,
            FaceTypeConical/** Conical face */,
            FaceTypeSpherical/** Spherical face */,
            FaceTypeSurfaceOfRevolution/** Face from surface of revolution */,
            FaceTypeParametric/** Parametric face */,
            FaceTypeBlending/** Blending face */,
            FaceTypeOffset/** Offset face */,
            FaceTypeSwept/** Swept face */,
            FaceTypeConvergent/** Convergent face */,
            FaceTypeUndefined/** Undefined face type */
        };

        /** Chamfer type for Skylight */
        public: enum ChamferType
        {
            ChamferTypeOffsetOffset/** 1. The chamfer is defined by two offsets from the boundaries of the chamfer to the intersection of the face normals;
                                                            2. The chamfer is defined by two offsets from the edge to the boundaries of the chamfer */,
            ChamferTypeOffsetAngle/** The chamfer is defined by an edge offset and an angle */,
            ChamferTypeVertex/** The chamfer whose unders are all chamfers */
        };

        private: FaceImpl * m_face_impl;
        private: friend class  _FaceBuilder;
        protected: Face();
        public: ~Face();
        /**Returns  the Parasolid type of the face 
         <br>  Created in NX3.0.0.  <br>  
         <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: NXOpen::Face::FaceType SolidFaceType
        (
        );
        /**  @brief Returns the edges in the face 

         
                The edges are sorted according to the journal identifier of the edge.
             @return  
         <br>  Created in NX3.0.0.  <br>  
         <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: std::vector<NXOpen::Edge *> GetEdges
        (
        );
        /**  @brief Returns the edges in the face 

         
                The edges returned from this method are in no guaranteed order. 
                    This method will be faster than @link NXOpen::Face::GetEdges NXOpen::Face::GetEdges@endlink .
                
             @return  
         <br>  Created in NX12.0.0.  <br>  
         <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: std::vector<NXOpen::Edge *> GetUnsortedEdges
        (
        );
        /** Returns the body containing this face  @return  
         <br>  Created in NX3.0.0.  <br>  
         <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: NXOpen::Body * GetBody
        (
        );
        /**  @brief Returns the number of facets on a convergent face. 

         
                This method is valid only for convergent faces. If this face is not a convergent face, then an error is returned 
                  @return  the number of facets on a face
         <br>  Created in NX11.0.2.  <br>  
         <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: int GetNumberOfFacets
        (
        );
        /**  @brief Returns the number of vertices on this convergent face. 

         
                This method is valid only for convergent faces. If this face is not a convergent face, then an error is returned.
                  @return  the number of vertices on a face
         <br>  Created in NX11.0.2.  <br>  
         <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: int GetNumberOfVertices
        (
        );
        /**  @brief Returns a facet next to the input facet on a convergent face. 

         
                
                Note that, the next facet is the facet immediately next to the given facet in an internal ordered sequence of facets. It is not
                necessarily adjacent to the given facet. If the input facet is the last facet on the face, then NULL is returned.
                This method is valid only for convergent faces. If this face is not a convergent face, then an error is returned. 
                 @return  the next facet. 
         <br>  Created in NX11.0.2.  <br>  
         <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: NXOpen::ConvergentFacet * GetNextFacet
        (
            NXOpen::ConvergentFacet * inputFacet /** the input facet, next to which facet is to find. */
        );
        /**  @brief Returns first facet on convergent face. 

         
                This method is valid only for convergent faces. If this face is not a convergent face, then an error is returned.
                  @return  the first facet on a face. 
         <br>  Created in NX11.0.2.  <br>  
         <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: NXOpen::ConvergentFacet * GetFirstFacetOnFace
        (
        );
        /**
                Destroys all @link IFacet IFacet@endlink  objects owned by this face.
                 
                Please note that this method does not geometrically delete a facet from its surface mesh leaving a hole. 
                It only deletes the tagged object created to represent the individual facet.
                
            
         <br>  Created in NX12.0.0.  <br>  
         <br> License requirements : None */
        public: void DestroyOwnedFacets
        (
        );
        /** Check whether a face is chamfer and return the chamfer data for chamfer face  @return  is chamfer or not 
         <br>  Created in NX1872.0.0.  <br>  
         <br> License requirements : None */
        public: bool GetChamferData
        (
            NXOpen::Face::ChamferType* chamferType /** chamfertype */ ,
            std::vector<double> & offsets /** OffsetOffset type: offsets[0] and offsets[1] are the two offset distances;
                                                                 OffsetAngle: offsets[0] is the offset distance, offsets[1] is the angle;
                                                                 Vertex, there is no offsets values */
        );
        /** Identify blend face and get it's radius 
         <br>  Created in NX1872.0.0.  <br>  
         <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: void GetBlendData
        (
            double* radius /** radius */ ,
            bool* isBlendFace /** isblendface */ 
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
