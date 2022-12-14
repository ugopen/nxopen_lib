#ifndef NXOpen_GEOMETRICUTILITIES_DESIGNMESHFACE_HXX_INCLUDED
#define NXOpen_GEOMETRICUTILITIES_DESIGNMESHFACE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     GeometricUtilities_DesignMeshFace.ja
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
#include <NXOpen/libnxopencpp_geometricutilities_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace GeometricUtilities
    {
        class DesignMeshFace;
    }
    class DisplayableObject;
    namespace GeometricUtilities
    {
        class DesignMeshBody;
    }
    namespace GeometricUtilities
    {
        class DesignMeshEdge;
    }
    namespace GeometricUtilities
    {
        class DesignMeshVertex;
    }
    namespace GeometricUtilities
    {
        class _DesignMeshFaceBuilder;
        class DesignMeshFaceImpl;
        /** Represents a facet mesh face. 
         <br>  Created in NX1847.0.0.  <br>  
        */
        class NXOPENCPP_GEOMETRICUTILITIESEXPORT  DesignMeshFace : public NXOpen::DisplayableObject
        {
            private: DesignMeshFaceImpl * m_designmeshface_impl;
            private: friend class  _DesignMeshFaceBuilder;
            protected: DesignMeshFace();
            public: ~DesignMeshFace();
            /** Returns the mesh owning this face.  @return  
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricUtilities::DesignMeshBody * GetBody
            (
            );
            /** Returns the edges of the face.  @return  
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXOpen::GeometricUtilities::DesignMeshEdge *> GetEdges
            (
            );
            /** Returns the vertexes of the face.  @return  
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXOpen::GeometricUtilities::DesignMeshVertex *> GetVertices
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
