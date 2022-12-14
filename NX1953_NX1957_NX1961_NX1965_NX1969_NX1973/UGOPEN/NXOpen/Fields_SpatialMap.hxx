#ifndef NXOpen_FIELDS_SPATIALMAP_HXX_INCLUDED
#define NXOpen_FIELDS_SPATIALMAP_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Fields_SpatialMap.ja
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
#include <NXOpen/NXObject.hxx>
#include <NXOpen/libnxopencpp_fields_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Fields
    {
        class SpatialMap;
    }
    class NXObject;
    namespace Fields
    {
        class _SpatialMapBuilder;
        class SpatialMapImpl;
        /**  @brief  Represents the Field Domain Map  

         
             <br> A Spatial Map provides a mapping from a field's independent domain into a new domain space.
            This Particular map type is designed to map into cartesian, cylindrical, spherical or parametric
            space, allowing the field to be used where these independent domains are required. <br> 
             <br> To obtain an instance of this class see @link NXOpen::Fields::FieldManager NXOpen::Fields::FieldManager@endlink .  <br> 
         <br>  Created in NX6.0.0.  <br>  
        */
        class NXOPENCPP_FIELDSEXPORT  SpatialMap : public NXOpen::NXObject
        {
            /** Type of Spatial Map */
            public: enum TypeEnum
            {
                TypeEnumNone/** No Map */,
                TypeEnumGlobal/** Map to global csys - defaults to cartesian */,
                TypeEnumCartesian/** Map to cartesian csys */,
                TypeEnumCylindrical/** Map to cylindrical csys */,
                TypeEnumSpherical/** Map to spherical csys */,
                TypeEnumParametricSpace/** Map to parametric space - see @link NXOpen::Fields::SpatialMap::BoundingBoxMapEnum NXOpen::Fields::SpatialMap::BoundingBoxMapEnum@endlink  */,
                TypeEnumParametricPlane/** Map to parametric plane - see @link NXOpen::Fields::SpatialMap::ParametricPlaneMapEnum NXOpen::Fields::SpatialMap::ParametricPlaneMapEnum@endlink  */,
                TypeEnumParametricLine/** Map to parametric line */,
                TypeEnumImportedParametricLine/** map to imported parametric line */
            };

            /** Subtype of Spatial Map */
            public: enum SubtypeEnum
            {
                SubtypeEnumNone/** No subtype */,
                SubtypeEnumSurface/** 3D degenerate to existing surface */,
                SubtypeEnumFitSurface/** 3D degenerate to fit surface */
            };

            /** Subtype Mapping */
            public: enum SubtypeMappingEnum
            {
                SubtypeMappingEnumFaces/** Map 3D degenerate data to faces */,
                SubtypeMappingEnumIsoSections/** Map 3D degenerate data using parametric plane using U curves */,
                SubtypeMappingEnumIsoLines/** Map 3D degenerate data using parametric plane using UV curves */
            };

            /** Bounding Box Map  */
            public: enum BoundingBoxMapEnum
            {
                BoundingBoxMapEnumOppositeCorner/** opposite corner */ ,
                BoundingBoxMapEnumObjects/** objects */ 
            };

            /** Parametric Plane Map */
            public: enum ParametricPlaneMapEnum
            {
                ParametricPlaneMapEnumIsoSections/** iso sections */ ,
                ParametricPlaneMapEnumIsoLines/** iso lines */ ,
                ParametricPlaneMapEnumImportedIsoLines/** imported iso lines */ 
            };

            private: SpatialMapImpl * m_spatialmap_impl;
            private: friend class  _SpatialMapBuilder;
            protected: SpatialMap();
            public: ~SpatialMap();
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
