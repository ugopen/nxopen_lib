#ifndef NXOpen_FEATURES_EMBOSSPROJECTION_HXX_INCLUDED
#define NXOpen_FEATURES_EMBOSSPROJECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_EmbossProjection.ja
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
#include <NXOpen/TaggedObject.hxx>
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
        class EmbossProjection;
    }
    class ISurface;
    class ScCollector;
    namespace Features
    {
        class _EmbossProjectionBuilder;
        class EmbossProjectionImpl;
        /** Represents a projection object.
                 <br>     
                Emboss projection object describes how to project section and to help build sidewall geometry.
                 <br>     
                 <br> 
                Following are default values and options:
                 <br> 

                 <br> 
                <b>Projection Option</b>    @link  Features::EmbossProjection::ProjectionOptionEndcap   Features::EmbossProjection::ProjectionOptionEndcap @endlink 
                 <br> 
                 <br> 
                <b>Projection Face</b>    User must set it when projection option is face.   
                 <br> 
                 <br> 
                <b>Projection Datum Plane</b>    User must set it when projection option is plane.
                 <br>                                 
                        
            
         <br>  Created in NX4.0.0.  <br>  
        */
        class NXOPENCPP_FEATURESEXPORT  EmbossProjection : public NXOpen::TaggedObject
        {
            /** Describes the geometry for projection */
            public: enum ProjectionOption
            {
                ProjectionOptionEndcap/** Indicates the geometry is End-Cap. */,
                ProjectionOptionTarget/** Indicates the geometry is target. */,
                ProjectionOptionFace/** Indicates the geometries are selected faces. */,
                ProjectionOptionPlane/** Indicates the geometry is datum plane.  */,
                ProjectionOptionNone/** Indicates no geometry. */
            };

            private: EmbossProjectionImpl * m_embossprojection_impl;
            private: friend class  _EmbossProjectionBuilder;
            protected: EmbossProjection();
            public: ~EmbossProjection();
            /**Sets  the projection option 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetOption
            (
                NXOpen::Features::EmbossProjection::ProjectionOption option /**The projection option to decide where the profile projects*/
            );
            /**Returns  the projection option 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: NXOpen::Features::EmbossProjection::ProjectionOption Option
            (
            );
            /**Sets  the projection face 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetFace
            (
                NXOpen::ScCollector * projectionFace /**Faces for projection, if the projection option is @link  Features::EmbossProjection::ProjectionOptionFace   Features::EmbossProjection::ProjectionOptionFace @endlink */
            );
            /**Returns  the projection face 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::ScCollector * Face
            (
            );
            /**Sets  the projection plane 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetPlane
            (
                NXOpen::ISurface * projectionPlane /**Plane for projection, if the projection option is @link  Features::EmbossProjection::ProjectionOptionPlane   Features::EmbossProjection::ProjectionOptionPlane @endlink */
            );
            /**Returns  the projection plane 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::ISurface * Plane
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
