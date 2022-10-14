#ifndef NXOpen_GEOMETRICUTILITIES_MATCHSURFACEBUILDER_HXX_INCLUDED
#define NXOpen_GEOMETRICUTILITIES_MATCHSURFACEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     GeometricUtilities_MatchSurfaceBuilder.ja
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
#include <NXOpen/GeometricUtilities_MatchSurfaceBuilder.hxx>
#include <NXOpen/GeometricUtilities_OnPathDimensionBuilder.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/SelectObject.hxx>
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
        class MatchSurfaceBuilder;
    }
    class Builder;
    namespace GeometricUtilities
    {
        class OnPathDimensionBuilder;
    }
    class SelectEdge;
    class SelectFace;
    namespace GeometricUtilities
    {
        class _MatchSurfaceBuilderBuilder;
        class MatchSurfaceBuilderImpl;
        /** Represents a @link GeometricUtilities::MatchSurfaceBuilder GeometricUtilities::MatchSurfaceBuilder@endlink  builder.This builder's Commit can create a b-surface  <br> To create a new instance of this class, use @link NXOpen::GeometricUtilities::CAMDataPrepManager::CreateMatchSurfaceBuilder  NXOpen::GeometricUtilities::CAMDataPrepManager::CreateMatchSurfaceBuilder @endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        Constraint </td> <td> 
         
        Tangent </td> </tr> 

        <tr><td> 
         
        EndToEnd </td> <td> 
         
        1 </td> </tr> 

        <tr><td> 
         
        KeepSheet </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        MatchExact </td> <td> 
         
        1 </td> </tr> 

        </table>  

         <br>  Created in NX9.0.0.  <br>  
        */
        class NXOPENCPP_GEOMETRICUTILITIESEXPORT  MatchSurfaceBuilder : public NXOpen::Builder
        {
            /** This enum represents the type of constaints */
            public: enum MatchConstaint
            {
                MatchConstaintPosition/** position */ ,
                MatchConstaintTangent/** tangent */ 
            };

            private: MatchSurfaceBuilderImpl * m_matchsurfacebuilder_impl;
            private: friend class  _MatchSurfaceBuilderBuilder;
            protected: MatchSurfaceBuilder();
            public: ~MatchSurfaceBuilder();
            /**Returns  the selected edge for matching 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectEdge * EditEdge
            (
            );
            /**Returns  the selected reference edge or curve  
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectEdge * Reference
            (
            );
            /**Returns  the selected face for reference curve  
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectFace * ReferenceFace
            (
            );
            /**Returns  the continuity type for matching 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricUtilities::MatchSurfaceBuilder::MatchConstaint Constraint
            (
            );
            /**Sets  the continuity type for matching 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_freeform_2 ("advanced freeform modeling") OR die_engineering ("DIE ENGINEERING") */
            public: void SetConstraint
            (
                NXOpen::GeometricUtilities::MatchSurfaceBuilder::MatchConstaint constraint /** constraint */ 
            );
            /**Returns  the distance limit of deformation region 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricUtilities::OnPathDimensionBuilder * RegionLimit
            (
            );
            /**Returns  the option to keep original sheet 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: bool KeepSheet
            (
            );
            /**Sets  the option to keep original sheet 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_freeform_2 ("advanced freeform modeling") OR die_engineering ("DIE ENGINEERING") */
            public: void SetKeepSheet
            (
                bool keepSheet /** keepsheet */ 
            );
            /**Returns  the option to match end-to-end, between the end of edit edge and the reference egde or curve 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: bool EndToEnd
            (
            );
            /**Sets  the option to match end-to-end, between the end of edit edge and the reference egde or curve 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_freeform_2 ("advanced freeform modeling") OR die_engineering ("DIE ENGINEERING") */
            public: void SetEndToEnd
            (
                bool endToEnd /** endtoend */ 
            );
            /**Returns  the option to match exact, between the end of edit edge and the reference egde or curve 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: bool MatchExact
            (
            );
            /**Sets  the option to match exact, between the end of edit edge and the reference egde or curve 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_freeform_2 ("advanced freeform modeling") OR die_engineering ("DIE ENGINEERING") */
            public: void SetMatchExact
            (
                bool matchExact /** matchexact */ 
            );
            /**Returns  the distance tolerance 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: double DistanceTolerance
            (
            );
            /**Sets  the distance tolerance 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_freeform_2 ("advanced freeform modeling") OR die_engineering ("DIE ENGINEERING") */
            public: void SetDistanceTolerance
            (
                double distTolerance /** disttolerance */ 
            );
            /**Returns  the angle tolerance 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: double AngleTolerance
            (
            );
            /**Sets  the angle tolerance 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_freeform_2 ("advanced freeform modeling") OR die_engineering ("DIE ENGINEERING") */
            public: void SetAngleTolerance
            (
                double angleTolerance /** angletolerance */ 
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