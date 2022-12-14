#ifndef NXOpen_GEOMETRICANALYSIS_CONTACTANALYSISSECTIONCURVEBUILDER_HXX_INCLUDED
#define NXOpen_GEOMETRICANALYSIS_CONTACTANALYSISSECTIONCURVEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     GeometricAnalysis_ContactAnalysisSectionCurveBuilder.ja
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
#include <NXOpen/Display_DynamicSectionBuilder.hxx>
#include <NXOpen/libnxopencpp_geometricanalysis_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace GeometricAnalysis
    {
        class ContactAnalysisSectionCurveBuilder;
    }
    namespace Display
    {
        class DynamicSectionBuilder;
    }
    class Expression;
    class NXColor;
    class Point;
    namespace GeometricAnalysis
    {
        class _ContactAnalysisSectionCurveBuilderBuilder;
        class ContactAnalysisSectionCurveBuilderImpl;
        /** Represents Section Curve Builder in Contact Analysis
            After Contact Analysis to visualize how the analysis is performed at certain point Section curves is used
            User can select a point, A ball is placed at the selected point.
            The plane of the section is constructed from selected point, sphere center and the plane of minimum radius at that point
            the section curves and section preview is displayed
            Section Curves can be saved <br> To create a new instance of this class, use @link NXOpen::GeometricAnalysis::AnalysisResultCollection::CreateContactAnalysisSectionCurveBuilder  NXOpen::GeometricAnalysis::AnalysisResultCollection::CreateContactAnalysisSectionCurveBuilder @endlink  <br> 
        Default values.
        <list type="table"> 
         
        <listheader><term> 
        Property</term>  <description> 
        Value</description> </listheader>
        <item><term> 
         
        BoxExtentDelayUpdate </term> <description> 
         
        false </description> </item> 

        <item><term> 
         
        CapColorOption </term> <description> 
         
        Any </description> </item> 

        <item><term> 
         
        ClipType </term> <description> 
         
        Section </description> </item> 

        <item><term> 
         
        CurveColorOption </term> <description> 
         
        Any </description> </item> 

        <item><term> 
         
        DisplaySlice </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        LockPlanes </term> <description> 
         
        true </description> </item> 

        <item><term> 
         
        SectionBoundary.Value </term> <description> 
         
        300 (millimeters part), 11.812 (inches part) </description> </item> 

        <item><term> 
         
        ShowCap </term> <description> 
         
        true </description> </item> 

        <item><term> 
         
        ShowClip </term> <description> 
         
        true </description> </item> 

        <item><term> 
         
        ShowCurves (deprecated) </term> <description> 
         
        false </description> </item> 

        <item><term> 
         
        ShowGrid </term> <description> 
         
        false </description> </item> 

        <item><term> 
         
        ShowInterference </term> <description> 
         
        false </description> </item> 

        <item><term> 
         
        ShowViewer </term> <description> 
         
        false </description> </item> 

        <item><term> 
         
        Type </term> <description> 
         
        OnePlane </description> </item> 

        </list> 

         <br>  Created in NX1980.0.0.  <br>  
        */
        class NXOPENCPP_GEOMETRICANALYSISEXPORT  ContactAnalysisSectionCurveBuilder : public NXOpen::Display::DynamicSectionBuilder
        {
            private: ContactAnalysisSectionCurveBuilderImpl * m_contactanalysissectioncurvebuilder_impl;
            private: friend class  _ContactAnalysisSectionCurveBuilderBuilder;
            protected: ContactAnalysisSectionCurveBuilder();
            public: ~ContactAnalysisSectionCurveBuilder();
            /**Returns  the point to place sphere 
                        This points should be only on faces of selected bodies for Contact Analysis
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Point * PointToPlaceSphere
            (
            );
            /**Sets  the point to place sphere 
                        This points should be only on faces of selected bodies for Contact Analysis
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : studio_analyze ("STUDIO ANALYZE") */
            public: void SetPointToPlaceSphere
            (
                NXOpen::Point * pointToPlaceSphere /** pointtoplacesphere */ 
            );
            /**Returns  the range of circle up to which the Section curves will be trimmed 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * SectionBoundary
            (
            );
            /** Rotate the view to the section plane 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : studio_analyze ("STUDIO ANALYZE") */
            public: void OrientToPlane
            (
            );
            /**Returns  the toggle to display section view i.e. slice
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: bool DisplaySlice
            (
            );
            /**Sets  the toggle to display section view i.e. slice
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : studio_analyze ("STUDIO ANALYZE") */
            public: void SetDisplaySlice
            (
                bool displaySlice /** displayslice */ 
            );
            /**Returns  the Ball diameter of contact Analysis
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: double BallDiameter
            (
            );
            /**Sets  the Ball diameter of contact Analysis
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : studio_analyze ("STUDIO ANALYZE") */
            public: void SetBallDiameter
            (
                double ballDiameter /** balldiameter */ 
            );
            /**Returns  the Color for Section Curves 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::NXColor * SectionCurveColor
            (
            );
            /**Sets  the Color for Section Curves 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : studio_analyze ("STUDIO ANALYZE") */
            public: void SetSectionCurveColor
            (
                NXOpen::NXColor * curveColor /** curvecolor */ 
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
