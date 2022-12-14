#ifndef NXOpen_FEATURES_COMPOSITECURVEBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_COMPOSITECURVEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_CompositeCurveBuilder.ja
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
#include <NXOpen/GeometricUtilities_CurveFitData.hxx>
#include <NXOpen/Features_FeatureBuilder.hxx>
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
        class CompositeCurveBuilder;
    }
    namespace Assemblies
    {
        namespace ProductInterface
        {
            class InterfaceObject;
        }
    }
    namespace Features
    {
        class Feature;
    }
    namespace Features
    {
        class FeatureBuilder;
    }
    namespace GeometricUtilities
    {
        class CurveFitData;
    }
    class Section;
    class TaggedObject;
    namespace Features
    {
        class _CompositeCurveBuilderBuilder;
        class CompositeCurveBuilderImpl;
        /**
            Represents a @link NXOpen::Features::CompositeCurve NXOpen::Features::CompositeCurve@endlink  builder.
            Inputs to this class can be convergent objects.
             <br> To create a new instance of this class, use @link NXOpen::Features::FeatureCollection::CreateCompositeCurveBuilder  NXOpen::Features::FeatureCollection::CreateCompositeCurveBuilder @endlink  <br> 
        Default values.
        <list type="table"> 
         
        <listheader><term> 
        Property</term>  <description> 
        Value</description> </listheader>
        <item><term> 
         
        AllowSelfIntersection </term> <description> 
         
        False </description> </item> 

        <item><term> 
         
        Associative </term> <description> 
         
        True </description> </item> 

        <item><term> 
         
        CurveFitData.CurveJoinMethod </term> <description> 
         
        No </description> </item> 

        <item><term> 
         
        CurveFitData.Degree </term> <description> 
         
        7 </description> </item> 

        <item><term> 
         
        CurveFitData.FitMethod </term> <description> 
         
        DegreeAndSegments </description> </item> 

        <item><term> 
         
        CurveFitData.IsAdvancedFit </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        CurveFitData.IsAlignShape </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        CurveFitData.MaximumDegree </term> <description> 
         
        7 </description> </item> 

        <item><term> 
         
        CurveFitData.MaximumSegments </term> <description> 
         
        1 </description> </item> 

        <item><term> 
         
        CurveFitData.MinimumDegree </term> <description> 
         
        5 </description> </item> 

        <item><term> 
         
        CurveFitData.Segments </term> <description> 
         
        1 </description> </item> 

        <item><term> 
         
        HideOriginal </term> <description> 
         
        False </description> </item> 

        <item><term> 
         
        InheritDisplayProperties </term> <description> 
         
        False </description> </item> 

        </list> 

         <br>  Created in NX5.0.0.  <br>  
        */
        class NXOPENCPP_FEATURESEXPORT  CompositeCurveBuilder : public NXOpen::Features::FeatureBuilder
        {
            /** Composite Curve part type. */
            public: enum PartType
            {
                PartTypeWorkPart/** Work part */,
                PartTypeOtherPart/** Other part in assembly */
            };

            /** the join method */
            public: enum JoinMethod
            {
                JoinMethodNo/** No */,
                JoinMethodCubic/** Cubic */,
                JoinMethodGenernal/** General */,
                JoinMethodQuintic/** Quintic */
            };

            private: CompositeCurveBuilderImpl * m_compositecurvebuilder_impl;
            private: friend class  _CompositeCurveBuilderBuilder;
            protected: CompositeCurveBuilder();
            public: ~CompositeCurveBuilder();
            /**Returns  the parent part 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::CompositeCurveBuilder::PartType ParentPart
            (
            );
            /**Sets  the parent part 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR cam_base ("CAM BASE") OR geometric_tol ("GDT") OR insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetParentPart
            (
                NXOpen::Features::CompositeCurveBuilder::PartType parentPart /** parentpart */ 
            );
            /**Returns  the section 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Section * Section
            (
            );
            /**Returns  the associative 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: bool Associative
            (
            );
            /**Sets  the associative 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR cam_base ("CAM BASE") OR geometric_tol ("GDT") OR insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetAssociative
            (
                bool associative /** associative */ 
            );
            /**Returns  the hide original 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: bool HideOriginal
            (
            );
            /**Sets  the hide original 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR cam_base ("CAM BASE") OR geometric_tol ("GDT") OR insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetHideOriginal
            (
                bool hideOriginal /** hideoriginal */ 
            );
            /**Returns  the self intersection 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: bool AllowSelfIntersection
            (
            );
            /**Sets  the self intersection 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR cam_base ("CAM BASE") OR geometric_tol ("GDT") OR insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetAllowSelfIntersection
            (
                bool allowSelfIntersection /** allowselfintersection */ 
            );
            /**Returns  the fix at timestamp option 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: bool FixAtCurrentTimestamp
            (
            );
            /**Sets  the fix at timestamp option 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR cam_base ("CAM BASE") OR geometric_tol ("GDT") OR insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetFixAtCurrentTimestamp
            (
                bool timestamp /** timestamp */ 
            );
            /**Returns  the make position independent 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: bool MakePositionIndependent
            (
            );
            /**Sets  the make position independent 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR cam_base ("CAM BASE") OR geometric_tol ("GDT") OR insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetMakePositionIndependent
            (
                bool makePositionIndependent /** makepositionindependent */ 
            );
            /**Returns  the inherit display properties from source option 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: bool InheritDisplayProperties
            (
            );
            /**Sets  the inherit display properties from source option 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR cam_base ("CAM BASE") OR geometric_tol ("GDT") OR insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetInheritDisplayProperties
            (
                bool inheritDisplayProperties /** inheritdisplayproperties */ 
            );
            /** Commits the feature and set create on the fly flag  @return  
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR cam_base ("CAM BASE") OR geometric_tol ("GDT") OR insp_programming ("INSPECTION PROGRAMMING") */
            public: NXOpen::Features::Feature * CommitCreateOnTheFly
            (
            );
            /** Prints wave browser type information about link 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : wave ("WAVE FUNCTIONALITY") */
            public: void GetWaveLinkInformation
            (
                NXString* info /** queried wave information */,
                bool* xformExists /** true if there is a transform */,
                NXOpen::Point3d* xformOrigin /** transformation origin */,
                NXOpen::Matrix3x3* xformOrientation /** transformation matrix */,
                double* xformScale /** transformation scale */
            );
            /**Returns  the frec at time stamp 
             <br>  Created in NX6.0.1.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::Feature * FrecAtTimeStamp
            (
            );
            /**Sets  the frec at time stamp 
             <br>  Created in NX6.0.1.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR cam_base ("CAM BASE") OR geometric_tol ("GDT") OR insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetFrecAtTimeStamp
            (
                NXOpen::Features::Feature * terminalFrec /** terminal frec */ 
            );
            /**Returns  the join option 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::CompositeCurveBuilder::JoinMethod JoinOption
            (
            );
            /**Sets  the join option 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR cam_base ("CAM BASE") OR geometric_tol ("GDT") OR insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetJoinOption
            (
                NXOpen::Features::CompositeCurveBuilder::JoinMethod joinOption /** joinoption */ 
            );
            /**Returns  the tolerance 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: double Tolerance
            (
            );
            /**Sets  the tolerance 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR cam_base ("CAM BASE") OR geometric_tol ("GDT") OR insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetTolerance
            (
                double tolerance /** tolerance */ 
            );
            /** Gets selected product interface objects 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: void GetProductInterfaceObjects
            (
                std::vector<NXOpen::Assemblies::ProductInterface::InterfaceObject *> & selectedObjects /** items in list */
            );
            /** Sets selected product interface objects 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: void SetProductInterfaceObjects
            (
                const std::vector<NXOpen::Assemblies::ProductInterface::InterfaceObject *> & selectedObjects /** items in list */
            );
            /**Returns  the source part occurrence 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::TaggedObject * SourcePartOccurrence
            (
            );
            /**Sets  the source part occurrence 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: void SetSourcePartOccurrence
            (
                NXOpen::TaggedObject * sourcePartOcc /** sourcepartocc */ 
            );
            /** Gets source part occurrences 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void GetSourcePartOccurrences
            (
                std::vector<NXOpen::TaggedObject *> & sourcePartOccurrences /** sourcepartoccurrences */ 
            );
            /** Sets source part occurrences 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void SetSourcePartOccurrences
            (
                const std::vector<NXOpen::TaggedObject *> & sourcePartOccurrences /** sourcepartoccurrences */ 
            );
            /**Returns  the composite curve reverse direction 
             <br>  Created in NX9.0.2.  <br>  
             <br> License requirements : None */
            public: bool ReverseDirection
            (
            );
            /**Sets  the composite curve reverse direction 
             <br>  Created in NX9.0.2.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR cam_base ("CAM BASE") OR geometric_tol ("GDT") OR insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetReverseDirection
            (
                bool reverseDirection /** reversedirection */ 
            );
            /**Returns  the curve fit data 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricUtilities::CurveFitData * CurveFitData
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
