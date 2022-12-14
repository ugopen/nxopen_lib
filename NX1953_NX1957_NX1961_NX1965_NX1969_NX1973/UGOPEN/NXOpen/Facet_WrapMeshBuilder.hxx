#ifndef NXOpen_FACET_WRAPMESHBUILDER_HXX_INCLUDED
#define NXOpen_FACET_WRAPMESHBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Facet_WrapMeshBuilder.ja
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
#include <NXOpen/ScCollector.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/libnxopencpp_facet_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Facet
    {
        class WrapMeshBuilder;
    }
    class Builder;
    class Expression;
    class ScCollector;
    class SelectDisplayableObjectList;
    namespace Facet
    {
        class _WrapMeshBuilderBuilder;
        class WrapMeshBuilderImpl;
        /** Represents a @link NXOpen::Facet::WrapMeshBuilder NXOpen::Facet::WrapMeshBuilder@endlink .
                This class wraps a facet body around one or more bodies. <br> To create a new instance of this class, use @link NXOpen::Facet::FacetModelingCollection::CreateWrapMeshBuilder  NXOpen::Facet::FacetModelingCollection::CreateWrapMeshBuilder @endlink  <br> 
        Default values.
        <list type="table"> 
         
        <listheader><term> 
        Property</term>  <description> 
        Value</description> </listheader>
        <item><term> 
         
        AngleThreshold </term> <description> 
         
        50 </description> </item> 

        <item><term> 
         
        AverageSize.Value </term> <description> 
         
        5 (millimeters part), 0.2 (inches part) </description> </item> 

        <item><term> 
         
        ChordalTolerance </term> <description> 
         
        0.1 (millimeters part), 0.004 (inches part) </description> </item> 

        <item><term> 
         
        InputBodyOption </term> <description> 
         
        Hide </description> </item> 

        <item><term> 
         
        KeepSharpEdges </term> <description> 
         
        True </description> </item> 

        <item><term> 
         
        MaxGapSize.Value </term> <description> 
         
        10 (millimeters part), 0.4 (inches part) </description> </item> 

        <item><term> 
         
        MaximumSize.Value </term> <description> 
         
        5 (millimeters part), 0.2 (inches part) </description> </item> 

        </list> 

         <br>  Created in NX1926.0.0.  <br>  
        */
        class NXOPENCPP_FACETEXPORT  WrapMeshBuilder : public NXOpen::Builder
        {
            /** Methods based on wrapped volume. */
            public: enum MethodType
            {
                MethodTypeExternal/** external */ ,
                MethodTypeLargestInternal/** largest internal */ ,
                MethodTypeInternalBySeedPoint/** internal by seed point */ 
            };

            /** Mesh wrapping modes. */
            public: enum WrapMeshModeType
            {
                WrapMeshModeTypeConstant/** constant */ ,
                WrapMeshModeTypeVariable/** variable */ 
            };

            /** Input body visibility options. */
            public: enum KeepInputBodyType
            {
                KeepInputBodyTypeKeep/** keep */ ,
                KeepInputBodyTypeHide/** hide */ 
            };

            private: WrapMeshBuilderImpl * m_wrapmeshbuilder_impl;
            private: friend class  _WrapMeshBuilderBuilder;
            protected: WrapMeshBuilder();
            public: ~WrapMeshBuilder();
            /**Returns  the input body collector 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::ScCollector * InputBodyCollector
            (
            );
            /**Returns  the method for selected volume
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Facet::WrapMeshBuilder::MethodType Method
            (
            );
            /**Sets  the method for selected volume
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_polygon_modeling (" NX Polygon Modeling") */
            public: void SetMethod
            (
                NXOpen::Facet::WrapMeshBuilder::MethodType method /** method */ 
            );
            /**Returns  the seed point 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectDisplayableObjectList * SeedPoint
            (
            );
            /**Returns  the mode for wrap mesh
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Facet::WrapMeshBuilder::WrapMeshModeType WrapMeshMode
            (
            );
            /**Sets  the mode for wrap mesh
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_polygon_modeling (" NX Polygon Modeling") */
            public: void SetWrapMeshMode
            (
                NXOpen::Facet::WrapMeshBuilder::WrapMeshModeType wrapMeshMode /** wrapmeshmode */ 
            );
            /**Returns  the average size for wrap mesh
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * AverageSize
            (
            );
            /**Returns  the maximum size for wrap mesh
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * MaximumSize
            (
            );
            /**Returns  the chordal tolerance for wrap mesh
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: double ChordalTolerance
            (
            );
            /**Sets  the chordal tolerance for wrap mesh
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_polygon_modeling (" NX Polygon Modeling") */
            public: void SetChordalTolerance
            (
                double chordalTolerance /** chordaltolerance */ 
            );
            /**Returns  the maximum gap size
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * MaxGapSize
            (
            );
            /**Returns  the select gap faces
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::ScCollector * GapFaces
            (
            );
            /**Returns  the intended gap size
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * IntendedGapSize
            (
            );
            /**Returns  the flag indicating if sharp edges should be kept. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: bool KeepSharpEdges
            (
            );
            /**Sets  the flag indicating if sharp edges should be kept. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_polygon_modeling (" NX Polygon Modeling") */
            public: void SetKeepSharpEdges
            (
                bool keepSharpEdges /** keepsharpedges */ 
            );
            /**Returns  the angle threshold
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: double AngleThreshold
            (
            );
            /**Sets  the angle threshold
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_polygon_modeling (" NX Polygon Modeling") */
            public: void SetAngleThreshold
            (
                double angleThreshold /** anglethreshold */ 
            );
            /**Returns  the input body visibility option. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Facet::WrapMeshBuilder::KeepInputBodyType InputBodyOption
            (
            );
            /**Sets  the input body visibility option. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_polygon_modeling (" NX Polygon Modeling") */
            public: void SetInputBodyOption
            (
                NXOpen::Facet::WrapMeshBuilder::KeepInputBodyType inputBodyOption /** inputbodyoption */ 
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
