#ifndef NXOpen_SKETCHIGNORERELATIONBUILDER_HXX_INCLUDED
#define NXOpen_SKETCHIGNORERELATIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     SketchIgnoreRelationBuilder.ja
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
#include <NXOpen/SketchOperationBuilder.hxx>
#include <NXOpen/SelectObject.hxx>
#include <NXOpen/SelectObjectList.hxx>
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
    class SketchIgnoreRelationBuilder;
    class SelectNXObject;
    class SelectNXObjectList;
    class SketchOperationBuilder;
    class _SketchIgnoreRelationBuilderBuilder;
    class SketchIgnoreRelationBuilderImpl;
    /** Represents a @link NXOpen::SketchIgnoreRelationBuilder NXOpen::SketchIgnoreRelationBuilder@endlink   <br> To create a new instance of this class, use @link NXOpen::SketchCollection::CreateIgnoreRelationBuilder  NXOpen::SketchCollection::CreateIgnoreRelationBuilder @endlink  <br> 
     <br>  Created in NX1847.0.0.  <br>  
    */
    class NXOPENCPPEXPORT  SketchIgnoreRelationBuilder : public NXOpen::SketchOperationBuilder
    {
        private: SketchIgnoreRelationBuilderImpl * m_sketchignorerelationbuilder_impl;
        private: friend class  _SketchIgnoreRelationBuilderBuilder;
        protected: SketchIgnoreRelationBuilder();
        public: ~SketchIgnoreRelationBuilder();
        /**Returns  the geometry or dimension. The geometry or dimension is near the intended geometric relationship
                to be found and probably involves one of the geometric objects of that relationship. 
         <br>  Created in NX1847.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::SelectNXObject * GeometryOrDimension
        (
        );
        /**Returns  the relations to ignore. These relations are found by @link NXOpen::SketchOperationBuilder::FindRelations NXOpen::SketchOperationBuilder::FindRelations@endlink .
                One or more of those relations can be added to this list of relations to ignore. 
         <br>  Created in NX1847.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::SelectNXObjectList * RelationsToIgnore
        (
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
