#ifndef NXOpen_CAE_EDGESTICHERBUILDER_HXX_INCLUDED
#define NXOpen_CAE_EDGESTICHERBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_EdgeSticherBuilder.ja
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
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/libnxopencpp_cae_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace CAE
    {
        class EdgeSticherBuilder;
    }
    class Builder;
    namespace CAE
    {
        class SelectCAEBodyList;
    }
    namespace CAE
    {
        class SelectCAEEdgeList;
    }
    namespace CAE
    {
        class SelectCAEFaceList;
    }
    class Expression;
    namespace CAE
    {
        class _EdgeSticherBuilderBuilder;
        class EdgeSticherBuilderImpl;
        /** Represents a @link NXOpen::CAE::EdgeSticherBuilder NXOpen::CAE::EdgeSticherBuilder@endlink   <br> To create a new instance of this class, use @link NXOpen::CAE::FemPart::CreateEdgeSticherBuilder  NXOpen::CAE::FemPart::CreateEdgeSticherBuilder @endlink  <br> 
        Default values.
        <list type="table"> 
         
        <listheader><term> 
        Property</term>  <description> 
        Value</description> </listheader>
        <item><term> 
         
        SearchDistance.Value </term> <description> 
         
        0.1 (millimeters part), 0.004 (inches part) </description> </item> 

        <item><term> 
         
        SnapEnds.Value </term> <description> 
         
        0.1 (millimeters part), 0.004 (inches part) </description> </item> 

        </list> 

         <br>  Created in NX6.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  EdgeSticherBuilder : public NXOpen::Builder
        {
            /** Type of edge stitch : For Pre-NX7.5 */
            public: enum Types
            {
                TypesAutomaticFreeEdgeToAllEdges/** automatic free edge to all edges */ ,
                TypesManualEdgeToEdge/** manual edge to edge */ ,
                TypesManualEdgeToFace/** manual edge to face */ 
            };

            /** Stitch method : NX7.5 onwards */
            public: enum StitchMethods
            {
                StitchMethodsAutomatic/** automatic */ ,
                StitchMethodsManual/** manual */ 
            };

            /** Stitch option for stitch : NX7.5 onwards  */
            public: enum StitchOptions
            {
                StitchOptionsEdgeToEdges/** edge to edges */ ,
                StitchOptionsEdgeToFaces/** edge to faces */ ,
                StitchOptionsBoth/** both */ 
            };

            private: EdgeSticherBuilderImpl * m_edgesticherbuilder_impl;
            private: friend class  _EdgeSticherBuilderBuilder;
            protected: EdgeSticherBuilder();
            public: ~EdgeSticherBuilder();
            /**Returns  the body selection for Auto-Stitch Edge
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::SelectCAEBodyList * BodySelection
            (
            );
            /**Returns  the edges to be excluded from auto-stitch operation
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::SelectCAEEdgeList * ExclusionEdgeSelection
            (
            );
            /**Returns  the source edge selection for Stitch Edge
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::SelectCAEEdgeList * SourceEdgeSelection
            (
            );
            /**Returns  the target edge selection for stitch edge when type is @link NXOpen::CAE::EdgeSticherBuilder::TypesManualEdgeToEdge NXOpen::CAE::EdgeSticherBuilder::TypesManualEdgeToEdge@endlink  
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::SelectCAEEdgeList * TargetEdgeSelection
            (
            );
            /**Returns  the target face selection for stitch edge when type is @link NXOpen::CAE::EdgeSticherBuilder::TypesManualEdgeToFace NXOpen::CAE::EdgeSticherBuilder::TypesManualEdgeToFace@endlink  
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::SelectCAEFaceList * TargetFaceSelection
            (
            );
            /**Returns  the search distance value to check overlap 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * SearchDistance
            (
            );
            /**Returns  the snap ends value to snap to vertex at the end of edge 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * SnapEnds
            (
            );
            /**Returns  the type : (Obsolete from NX07.5 onwards) 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::EdgeSticherBuilder::Types Type
            (
            );
            /**Sets  the type : (Obsolete from NX07.5 onwards) 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetType
            (
                NXOpen::CAE::EdgeSticherBuilder::Types type /** type */ 
            );
            /**Returns  the stitch method 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::EdgeSticherBuilder::StitchMethods StitchMethod
            (
            );
            /**Sets  the stitch method 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetStitchMethod
            (
                NXOpen::CAE::EdgeSticherBuilder::StitchMethods type /** type */ 
            );
            /**Returns  the operand type for auto-stitch edge 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::EdgeSticherBuilder::StitchOptions StitchOption
            (
            );
            /**Sets  the operand type for auto-stitch edge 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetStitchOption
            (
                NXOpen::CAE::EdgeSticherBuilder::StitchOptions stitchOption /** stitch option */ 
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
