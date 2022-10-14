#ifndef NXOpen_FIELDS_SPATIALMAPBUILDER_HXX_INCLUDED
#define NXOpen_FIELDS_SPATIALMAPBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Fields_SpatialMapBuilder.ja
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
#include <NXOpen/Fields_PathObjects.hxx>
#include <NXOpen/Fields_SpatialMap.hxx>
#include <NXOpen/Fields_SpatialMapBuilder.hxx>
#include <NXOpen/ObjectList.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Fields
    {
        class SpatialMapBuilder;
    }
    class Builder;
    class CoordinateSystem;
    namespace Fields
    {
        class PathObjects;
    }
    namespace Fields
    {
        class PathObjectsList;
    }
    class Point;
    class SelectNXObjectList;
    namespace Fields
    {
        class _SpatialMapBuilderBuilder;
        class SpatialMapBuilderImpl;
        /**  @brief  Represents a @link Fields::SpatialMap Fields::SpatialMap@endlink  builder  

         
             <br> Used to create and or edit a @link Fields::SpatialMap Fields::SpatialMap@endlink . <br> 
             <br> To create a new instance of this class, use @link Fields::FieldManager::CreateSpatialMapBuilder Fields::FieldManager::CreateSpatialMapBuilder@endlink  <br> */
        class NXOPENCPPEXPORT  SpatialMapBuilder : public Builder
        {
            private: SpatialMapBuilderImpl * m_spatialmapbuilder_impl;
            private: friend class  _SpatialMapBuilderBuilder;
            protected: SpatialMapBuilder();
            public: ~SpatialMapBuilder();
            /**Returns  the map type  <br> License requirements : None */
            public: NXOpen::Fields::SpatialMap::TypeEnum MapType
            (
            );
            /**Sets  the map type  <br> License requirements : None */
            public: void SetMapType
            (
                NXOpen::Fields::SpatialMap::TypeEnum mapType /** maptype */ 
            );
            /**Returns  the parm plane map  <br> License requirements : None */
            public: NXOpen::Fields::SpatialMap::ParametricPlaneMapEnum ParametricPlaneMap
            (
            );
            /**Sets  the parm plane map  <br> License requirements : None */
            public: void SetParametricPlaneMap
            (
                NXOpen::Fields::SpatialMap::ParametricPlaneMapEnum parmPlaneMap /** parmplanemap */ 
            );
            /**Returns  the bound box map  <br> License requirements : None */
            public: NXOpen::Fields::SpatialMap::BoundingBoxMapEnum BoundingBoxMap
            (
            );
            /**Sets  the bound box map  <br> License requirements : None */
            public: void SetBoundingBoxMap
            (
                NXOpen::Fields::SpatialMap::BoundingBoxMapEnum boundBoxMap /** boundboxmap */ 
            );
            /**Returns  the csys  <br> License requirements : None */
            public: NXOpen::CoordinateSystem * CoordSystem
            (
            );
            /**Sets  the csys  <br> License requirements : None */
            public: void SetCoordSystem
            (
                NXOpen::CoordinateSystem * csys /** csys */ 
            );
            /**Returns  the bounded objects  <br> License requirements : None */
            public: NXOpen::SelectNXObjectList * BoundedObjects
            (
            );
            /**Returns  the opposite corner  <br> License requirements : None */
            public: NXOpen::Point * Origin
            (
            );
            /**Sets  the opposite corner  <br> License requirements : None */
            public: void SetOrigin
            (
                NXOpen::Point * origin /** origin */ 
            );
            /**Returns  the opposite corner  <br> License requirements : None */
            public: NXOpen::Point * OppositeCorner
            (
            );
            /**Sets  the opposite corner  <br> License requirements : None */
            public: void SetOppositeCorner
            (
                NXOpen::Point * oppositeCorner /** oppositecorner */ 
            );
            /**Returns  the lattice path objects  <br> License requirements : None */
            public: NXOpen::Fields::PathObjects * LatticePath
            (
            );
            /**Returns  the const uobjects 
             @deprecated Deprecated in NX6.0.1 <br> 
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX6.0.1") NXOpen::SelectNXObjectList * ConstantUObjects
            (
            );
            /**Returns  the const vobjects 
             @deprecated Deprecated in NX6.0.1 <br> 
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX6.0.1") NXOpen::SelectNXObjectList * ConstantVObjects
            (
            );
            /**Returns  the list of @link Fields::PathObjects Fields::PathObjects@endlink  objects that define sections of constant u  <br> License requirements : None */
            public: NXOpen::Fields::PathObjectsList * ConstUObjects
            (
            );
            /**Returns  the list of @link Fields::PathObjects Fields::PathObjects@endlink  objects that define sections of constant v  <br> License requirements : None */
            public: NXOpen::Fields::PathObjectsList * ConstVObjects
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif