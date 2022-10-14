#ifndef NXOpen_CAM_MANUALVECTORLISTBUILDER_HXX_INCLUDED
#define NXOpen_CAM_MANUALVECTORLISTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_ManualVectorListBuilder.ja
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
#include <NXOpen/libnxopencpp_cam_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace CAM
    {
        class ManualVectorListBuilder;
    }
    class Direction;
    class Point;
    namespace CAM
    {
        class _ManualVectorListBuilderBuilder;
        class ManualVectorListBuilderImpl;
        /** Represents a builder which holds the data for a set of point and vector. 
         <br>  Created in NX1980.0.0.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  ManualVectorListBuilder : public NXOpen::TaggedObject
        {
            private: ManualVectorListBuilderImpl * m_manualvectorlistbuilder_impl;
            private: friend class  _ManualVectorListBuilderBuilder;
            protected: ManualVectorListBuilder();
            public: ~ManualVectorListBuilder();
            /** Add a new item 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void Add
            (
                int indexAfterPosition /** the index which new item will be added after */,
                NXOpen::Point * point /** the point for new item */,
                NXOpen::Direction * vector /** the vector for new item */
            );
            /** Modify item 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void Modify
            (
                int index /** the index which item will be modified */,
                NXOpen::Point * point /** the new point for item */,
                NXOpen::Direction * vector /** the new vector for item */
            );
            /** Delete a item 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void Delete
            (
                int index /** the index of item to be deleted */
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