#ifndef NXOpen_FEATURES_GUIDEDEXTENSIONBUILDEREX_HXX_INCLUDED
#define NXOpen_FEATURES_GUIDEDEXTENSIONBUILDEREX_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_GuidedExtensionBuilderEx.ja
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
#include <NXOpen/Section.hxx>
#include <NXOpen/ugmath.hxx>
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
        class GuidedExtensionBuilderEx;
    }
    class Builder;
    class Curve;
    class Direction;
    class Edge;
    class Expression;
    class Point;
    class ScCollector;
    class Section;
    namespace Features
    {
        class _GuidedExtensionBuilderExBuilder;
        class GuidedExtensionBuilderExImpl;
        /**
            Represents a @link NXOpen::Features::GuidedExtensionEx NXOpen::Features::GuidedExtensionEx@endlink  builder
             <br> To create a new instance of this class, use @link NXOpen::Features::FeatureCollection::CreateGuidedExtensionBuilderEx  NXOpen::Features::FeatureCollection::CreateGuidedExtensionBuilderEx @endlink  <br> 
        Default values.
        <list type="table"> 
         
        <listheader><term> 
        Property</term>  <description> 
        Value</description> </listheader>
        <item><term> 
         
        AngleTolerance </term> <description> 
         
        0.5 </description> </item> 

        <item><term> 
         
        CheckSurfaces </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        DistanceTolerance </term> <description> 
         
        0.01 </description> </item> 

        <item><term> 
         
        ExtendLength.Value </term> <description> 
         
        10 (millimeters part), 10 (inches part) </description> </item> 

        <item><term> 
         
        GuideLineAngle1.Value </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        GuideLineAngle2.Value </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        PlanarSurfacePreferred </term> <description> 
         
        1 </description> </item> 

        </list> 

         <br>  Created in NX10.0.0.  <br>  
        */
        class NXOPENCPP_FEATURESEXPORT  GuidedExtensionBuilderEx : public NXOpen::Builder
        {
            /** Option types to create guided extension surface */
            public: enum Types
            {
                TypesTangentFromFaces/** Extend tangentially from faces */,
                TypesVector/** Perpendicular to a vector */
            };

            /** Segment type for segments */
            public: enum SegmentType
            {
                SegmentTypeNormal/** Normal segment type */,
                SegmentTypeTransition/** Transition segment type */,
                SegmentTypeBypass/** Bypass segment type */
            };

            private: GuidedExtensionBuilderExImpl * m_guidedextensionbuilderex_impl;
            private: friend class  _GuidedExtensionBuilderExBuilder;
            protected: GuidedExtensionBuilderEx();
            public: ~GuidedExtensionBuilderEx();
            /**Returns  the sheet edges of a sheet body 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR nx_freeform_2 ("advanced freeform modeling") OR ug_mold_design ("UG MOLD") OR die_engineering ("DIE ENGINEERING") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: NXOpen::Section * SheetEdges
            (
            );
            /**Returns  the reference vector which is active when the type is vector 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR nx_freeform_2 ("advanced freeform modeling") OR ug_mold_design ("UG MOLD") OR die_engineering ("DIE ENGINEERING") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: NXOpen::Direction * ReferenceVector
            (
            );
            /**Sets  the reference vector which is active when the type is vector 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR nx_freeform_2 ("advanced freeform modeling") OR ug_mold_design ("UG MOLD") OR die_engineering ("DIE ENGINEERING") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetReferenceVector
            (
                NXOpen::Direction * referenceVector /** referencevector */ 
            );
            /**Returns  the origin of the reference vector 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR nx_freeform_2 ("advanced freeform modeling") OR ug_mold_design ("UG MOLD") OR die_engineering ("DIE ENGINEERING") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: NXOpen::Point * VectorOrigin
            (
            );
            /**Sets  the origin of the reference vector 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR nx_freeform_2 ("advanced freeform modeling") OR ug_mold_design ("UG MOLD") OR die_engineering ("DIE ENGINEERING") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetVectorOrigin
            (
                NXOpen::Point * vectorOrigin /** vectororigin */ 
            );
            /**Returns  the list of segment edges that represent a segment 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR nx_freeform_2 ("advanced freeform modeling") OR ug_mold_design ("UG MOLD") OR die_engineering ("DIE ENGINEERING") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: NXOpen::ScCollector * SegmentEdges
            (
            );
            /** The action that resets all the segments in the loop to their original state 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR nx_freeform_2 ("advanced freeform modeling") OR ug_mold_design ("UG MOLD") OR die_engineering ("DIE ENGINEERING") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void ResetAllSegments
            (
            );
            /**Returns  the extend length for use in creating the guided extension surfaces 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR nx_freeform_2 ("advanced freeform modeling") OR ug_mold_design ("UG MOLD") OR die_engineering ("DIE ENGINEERING") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: NXOpen::Expression * ExtendLength
            (
            );
            /**Returns  the rotation angle for the first guide line at one of the end points of the selected segment 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR nx_freeform_2 ("advanced freeform modeling") OR ug_mold_design ("UG MOLD") OR die_engineering ("DIE ENGINEERING") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: NXOpen::Expression * GuideLineAngle1
            (
            );
            /**Returns  the rotation angle for the second guide line at one of the end points of the selected segment 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR nx_freeform_2 ("advanced freeform modeling") OR ug_mold_design ("UG MOLD") OR die_engineering ("DIE ENGINEERING") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: NXOpen::Expression * GuideLineAngle2
            (
            );
            /**Returns  the option for checking the resulting guided extension surfaces for geometry issues 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR nx_freeform_2 ("advanced freeform modeling") OR ug_mold_design ("UG MOLD") OR die_engineering ("DIE ENGINEERING") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: bool CheckSurfaces
            (
            );
            /**Sets  the option for checking the resulting guided extension surfaces for geometry issues 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR nx_freeform_2 ("advanced freeform modeling") OR ug_mold_design ("UG MOLD") OR die_engineering ("DIE ENGINEERING") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetCheckSurfaces
            (
                bool checkSurfaces /** checksurfaces */ 
            );
            /**Returns  the option to create planar surface when possible 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR nx_freeform_2 ("advanced freeform modeling") OR ug_mold_design ("UG MOLD") OR die_engineering ("DIE ENGINEERING") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: bool PlanarSurfacePreferred
            (
            );
            /**Sets  the option to create planar surface when possible 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR nx_freeform_2 ("advanced freeform modeling") OR ug_mold_design ("UG MOLD") OR die_engineering ("DIE ENGINEERING") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetPlanarSurfacePreferred
            (
                bool planarSurfacePreferred /** planarsurfacepreferred */ 
            );
            /**Returns  the distance tolerance for use in creating the guided extension surfaces 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR nx_freeform_2 ("advanced freeform modeling") OR ug_mold_design ("UG MOLD") OR die_engineering ("DIE ENGINEERING") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: double DistanceTolerance
            (
            );
            /**Sets  the distance tolerance for use in creating the guided extension surfaces 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR nx_freeform_2 ("advanced freeform modeling") OR ug_mold_design ("UG MOLD") OR die_engineering ("DIE ENGINEERING") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetDistanceTolerance
            (
                double distanceTolerance /** distancetolerance */ 
            );
            /**Returns  the angle tolerance for use in creating the guided extension surfaces 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR nx_freeform_2 ("advanced freeform modeling") OR ug_mold_design ("UG MOLD") OR die_engineering ("DIE ENGINEERING") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: double AngleTolerance
            (
            );
            /**Sets  the angle tolerance for use in creating the guided extension surfaces 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR nx_freeform_2 ("advanced freeform modeling") OR ug_mold_design ("UG MOLD") OR die_engineering ("DIE ENGINEERING") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetAngleTolerance
            (
                double angleTolerance /** angletolerance */ 
            );
            /**Returns  the option type to create guided extension surface 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR nx_freeform_2 ("advanced freeform modeling") OR ug_mold_design ("UG MOLD") OR die_engineering ("DIE ENGINEERING") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: NXOpen::Features::GuidedExtensionBuilderEx::Types Type
            (
            );
            /**Sets  the option type to create guided extension surface 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR nx_freeform_2 ("advanced freeform modeling") OR ug_mold_design ("UG MOLD") OR die_engineering ("DIE ENGINEERING") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetType
            (
                NXOpen::Features::GuidedExtensionBuilderEx::Types type /** type */ 
            );
            /** Updates the information for the sheet edges of the selected section whenever sheet edges are selected or de-selected. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR nx_freeform_2 ("advanced freeform modeling") OR ug_mold_design ("UG MOLD") OR die_engineering ("DIE ENGINEERING") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void UpdateSheetEdges
            (
            );
            /** Updates the extend direction of curves and guide lines whenever the type of guided extension or the draw direction changes. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR nx_freeform_2 ("advanced freeform modeling") OR ug_mold_design ("UG MOLD") OR die_engineering ("DIE ENGINEERING") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void UpdateExtendDirectionsAndGuideLines
            (
                bool typeChanged /** typechanged */ 
            );
            /** Sets the segment type for the selected segment. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR nx_freeform_2 ("advanced freeform modeling") OR ug_mold_design ("UG MOLD") OR die_engineering ("DIE ENGINEERING") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetSelectedSegmentType
            (
                NXOpen::Features::GuidedExtensionBuilderEx::SegmentType segmentType /** Segment type for the selected segment */
            );
            /** Merges the selected segment with its neighboring segments. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR nx_freeform_2 ("advanced freeform modeling") OR ug_mold_design ("UG MOLD") OR die_engineering ("DIE ENGINEERING") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void MergeSegment
            (
            );
            /** Splits the selected segment into multiple segments by placing guide lines at end points of the edges for the selected segment. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR nx_freeform_2 ("advanced freeform modeling") OR ug_mold_design ("UG MOLD") OR die_engineering ("DIE ENGINEERING") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SplitSegment
            (
            );
            /** Unmerges the selected segment restoring the original segments before the merge using @link NXOpen::Features::GuidedExtensionBuilderEx::MergeSegment NXOpen::Features::GuidedExtensionBuilderEx::MergeSegment@endlink . 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR nx_freeform_2 ("advanced freeform modeling") OR ug_mold_design ("UG MOLD") OR die_engineering ("DIE ENGINEERING") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void RestoreSegments
            (
            );
            /** Creates a guide line at one of the end points of the sheet edge in the selection.  @return  Guide line created 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR nx_freeform_2 ("advanced freeform modeling") OR ug_mold_design ("UG MOLD") OR die_engineering ("DIE ENGINEERING") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: NXOpen::Curve * CreateGuideLine
            (
                NXOpen::Edge * assocEdge /** Associated curve of the guide line to be created */,
                const NXOpen::Point3d & guideLinePnt /** Guide line point */,
                const NXOpen::Vector3d & guideLineVector /** Guide line vector */,
                double guideLineLength /** Guide line length */
            );
            /** Updates the length of all the guide lines whenever the user changes the extend length of the surfaces interactively. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR nx_freeform_2 ("advanced freeform modeling") OR ug_mold_design ("UG MOLD") OR die_engineering ("DIE ENGINEERING") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void UpdateAllGuideLinesLength
            (
            );
            /** Changes the direction and length of a guide line. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR nx_freeform_2 ("advanced freeform modeling") OR ug_mold_design ("UG MOLD") OR die_engineering ("DIE ENGINEERING") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void ChangeGuideLineDirectionAndLength
            (
                NXOpen::Curve * guideLine /** Guide line to be changed */,
                const NXOpen::Vector3d & guideLineVector /** Direction vector */,
                double guideLineLength /** Length of guide line */
            );
            /**Returns  the loop index for the last selected loop which contains the last selected edge. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR nx_freeform_2 ("advanced freeform modeling") OR ug_mold_design ("UG MOLD") OR die_engineering ("DIE ENGINEERING") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: int LastSelectedLoopIndex
            (
            );
            /**Sets  the loop index for the last selected loop which contains the last selected edge. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR nx_freeform_2 ("advanced freeform modeling") OR ug_mold_design ("UG MOLD") OR die_engineering ("DIE ENGINEERING") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetLastSelectedLoopIndex
            (
                int lastSelectedLoopIndex /** lastselectedloopindex */ 
            );
            /** Reverses surface extend direction 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR nx_freeform_2 ("advanced freeform modeling") OR ug_mold_design ("UG MOLD") OR die_engineering ("DIE ENGINEERING") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetReverseExtendDirection
            (
                bool reverseExtendDirection /** Reverse surface extend direction */
            );
            /** Changes the option for the side of faces 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR nx_freeform_2 ("advanced freeform modeling") OR ug_mold_design ("UG MOLD") OR die_engineering ("DIE ENGINEERING") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void ChangeFacesSideOption
            (
                bool flipFacesSideOption /** Change the side of faces option */
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