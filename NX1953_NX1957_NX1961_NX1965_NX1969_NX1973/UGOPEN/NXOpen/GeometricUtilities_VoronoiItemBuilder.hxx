#ifndef NXOpen_GEOMETRICUTILITIES_VORONOIITEMBUILDER_HXX_INCLUDED
#define NXOpen_GEOMETRICUTILITIES_VORONOIITEMBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     GeometricUtilities_VoronoiItemBuilder.ja
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
#include <NXOpen/Expression.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/SelectObjectList.hxx>
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
        class VoronoiItemBuilder;
    }
    class Builder;
    class Expression;
    class SelectDisplayableObjectList;
    namespace GeometricUtilities
    {
        class _VoronoiItemBuilderBuilder;
        class VoronoiItemBuilderImpl;
        /** Represents a local specification of pore size and rod diameter for a Voronoi lattice  <br> To create a new instance of this class, use @link NXOpen::GeometricUtilities::VoronoiItemListBuilder::CreateVoronoiItemBuilder  NXOpen::GeometricUtilities::VoronoiItemListBuilder::CreateVoronoiItemBuilder @endlink  <br> 
        Default values.
        <list type="table"> 
         
        <listheader><term> 
        Property</term>  <description> 
        Value</description> </listheader>
        <item><term> 
         
        PoreSize.Value </term> <description> 
         
        10 (millimeters part), 0.4 (inches part) </description> </item> 

        <item><term> 
         
        RodDiameter.Value </term> <description> 
         
        1 (millimeters part), 0.04 (inches part) </description> </item> 

        </list> 

         <br>  Created in NX1953.0.0.  <br>  
        */
        class NXOPENCPP_GEOMETRICUTILITIESEXPORT  VoronoiItemBuilder : public NXOpen::Builder
        {
            private: VoronoiItemBuilderImpl * m_voronoiitembuilder_impl;
            private: friend class  _VoronoiItemBuilderBuilder;
            protected: VoronoiItemBuilder();
            public: ~VoronoiItemBuilder();
            /**Returns  the select object list which contains faces or points 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectDisplayableObjectList * Selection
            (
            );
            /**Returns  the pore size for the given item in the list 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * PoreSize
            (
            );
            /**Returns  the rod diameter for the given iteem in the list
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * RodDiameter
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
