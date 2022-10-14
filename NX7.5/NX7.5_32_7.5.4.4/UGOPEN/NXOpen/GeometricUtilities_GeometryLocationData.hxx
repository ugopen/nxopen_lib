#ifndef NXOpen_GEOMETRICUTILITIES_GEOMETRYLOCATIONDATA_HXX_INCLUDED
#define NXOpen_GEOMETRICUTILITIES_GEOMETRYLOCATIONDATA_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     GeometricUtilities_GeometryLocationData.ja
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
#include <NXOpen/GeometricUtilities_IComponentBuilder.hxx>
#include <NXOpen/GeometricUtilities_GeometryLocationData.hxx>
#include <NXOpen/SelectObject.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace GeometricUtilities
    {
        class GeometryLocationData;
    }
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    class Point;
    class SelectObject;
    namespace GeometricUtilities
    {
        class _GeometryLocationDataBuilder;
        class GeometryLocationDataImpl;
        /** Represents a @link GeometricUtilities::GeometryLocationData GeometricUtilities::GeometryLocationData@endlink 
             <br> To create a new instance of this class, use @link GeometricUtilities::GeometryLocationDataCollection::CreateGeometryLocationData GeometricUtilities::GeometryLocationDataCollection::CreateGeometryLocationData@endlink  <br> */
        class NXOPENCPPEXPORT  GeometryLocationData : public TaggedObject, public virtual GeometricUtilities::IComponentBuilder
        {
            /**Represents the entity type. */
            public: enum EntityTypes
            {
                EntityTypesPoint/** point */ ,
                EntityTypesCsys/** csys */ 
            };

            private: GeometryLocationDataImpl * m_geometrylocationdata_impl;
            private: friend class  _GeometryLocationDataBuilder;
            protected: GeometryLocationData();
            public: ~GeometryLocationData();
            /**Returns  the type  <br> License requirements : None */
            public: NXOpen::GeometricUtilities::GeometryLocationData::EntityTypes EntityType
            (
            );
            /**Sets  the type  <br> License requirements : None */
            public: void SetEntityType
            (
                NXOpen::GeometricUtilities::GeometryLocationData::EntityTypes entityType /** entitytype */ 
            );
            /**Returns  the csys  <br> License requirements : None */
            public: NXOpen::SelectObject * Csys
            (
            );
            /**Returns  the point  <br> License requirements : None */
            public: NXOpen::Point * Point
            (
            );
            /**Sets  the point  <br> License requirements : None */
            public: void SetPoint
            (
                NXOpen::Point * point /** point */ 
            );
            /** Returns true if the inputs to the component are sufficient for 
                        commit to be called.  For example, if the component requires
                        you to set some property, this method will return false if
                        you haven't set it.  This method throws a not-yet-implemented
                        NXException for some components.
                     @return  Was self validation successful  <br> License requirements : None */
            public: virtual bool Validate
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif