#ifndef NXOpen_FEATURES_GEOMCOPY_HXX_INCLUDED
#define NXOpen_FEATURES_GEOMCOPY_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_Geomcopy.ja
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
#include <NXOpen/Features_Feature.hxx>
#include <NXOpen/libnxopencpp_features_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Features
    {
        class Geomcopy;
    }
    class Body;
    class Edge;
    class Face;
    namespace Features
    {
        class Feature;
    }
    namespace Features
    {
        class _GeomcopyBuilder;
        class GeomcopyImpl;
        /** Represents a geomcopy feature  <br> To create or edit an instance of this class, use @link NXOpen::Features::GeomcopyBuilder  NXOpen::Features::GeomcopyBuilder @endlink  <br> 
         <br>  Created in NX5.0.0.  <br>  
        */
        class NXOPENCPP_FEATURESEXPORT  Geomcopy : public NXOpen::Features::Feature
        {
            private: GeomcopyImpl * m_geomcopy_impl;
            private: friend class  _GeomcopyBuilder;
            protected: Geomcopy();
            public: ~Geomcopy();
            /** Returns the bodies created by the feature  @return  
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: std::vector<NXOpen::Body *> GetBodies
            (
            );
            /** Returns the faces created by the feature  @return  
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: std::vector<NXOpen::Face *> GetFaces
            (
            );
            /** Returns the edges created by the feature  @return  
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: std::vector<NXOpen::Edge *> GetEdges
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
