#ifndef NXOpen_VALIDATE_CHECKCHANNELRATIOBUILDER_HXX_INCLUDED
#define NXOpen_VALIDATE_CHECKCHANNELRATIOBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Validate_CheckChannelRatioBuilder.ja
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
#include <NXOpen/GeometricUtilities_DisplayResolutionBuilder.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/ugmath.hxx>
#include <NXOpen/libnxopencpp_validate_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Validate
    {
        class CheckChannelRatioBuilder;
    }
    class Body;
    class Builder;
    class Face;
    namespace GeometricUtilities
    {
        class DisplayResolutionBuilder;
    }
    class NXColor;
    namespace Validate
    {
        class _CheckChannelRatioBuilderBuilder;
        class CheckChannelRatioBuilderImpl;
        /** Represents a Check Channel Ratio Builder  <br> To create a new instance of this class, use @link NXOpen::Validate::AnalysisResultCollection::CreateCheckChannelRatioBuilder  NXOpen::Validate::AnalysisResultCollection::CreateCheckChannelRatioBuilder @endlink  <br> 
        Default values.
        <list type="table"> 
         
        <listheader><term> 
        Property</term>  <description> 
        Value</description> </listheader>
        <item><term> 
         
        AutomaticUpdate </term> <description> 
         
        1 </description> </item> 

        <item><term> 
         
        DisplayResolution.AngleTolerance </term> <description> 
         
        15.0 </description> </item> 

        <item><term> 
         
        DisplayResolution.EdgeTolerance </term> <description> 
         
        0.005 </description> </item> 

        <item><term> 
         
        DisplayResolution.FaceTolerance </term> <description> 
         
        0.005 </description> </item> 

        <item><term> 
         
        DisplayResolution.Resolution </term> <description> 
         
        Standard </description> </item> 

        <item><term> 
         
        DisplayResolution.WidthTolerance </term> <description> 
         
        0.3 </description> </item> 

        <item><term> 
         
        FailedSegmentsColor </term> <description> 
         
        186 </description> </item> 

        <item><term> 
         
        MaximumWidth </term> <description> 
         
        3.0 (millimeters part), 0.1 (inches part) </description> </item> 

        <item><term> 
         
        MinimumRatio </term> <description> 
         
        0.02 (millimeters part), 0.02 (inches part) </description> </item> 

        <item><term> 
         
        PassedSegmentsColor </term> <description> 
         
        36 </description> </item> 

        <item><term> 
         
        PreviewState </term> <description> 
         
        1 </description> </item> 

        <item><term> 
         
        SegmentLength </term> <description> 
         
        50.0 (millimeters part), 2.0 (inches part) </description> </item> 

        <item><term> 
         
        ShowOnlyFailedSegments </term> <description> 
         
        1 </description> </item> 

        </list> 

         <br>  Created in NX1926.0.0.  <br>  
        */
        class NXOPENCPP_VALIDATEEXPORT  CheckChannelRatioBuilder : public NXOpen::Builder
        {
             
            public:
            struct TableData
            {
                public: /** angle value in table */double Angle;
                public: /** minimum diameter value in table*/double MinimumDiameter;
                public: TableData() :
                    Angle(),
                    MinimumDiameter()
                {
                }
                /** Constructor for the TableData struct. */ 
                public: TableData(double angleInitial /** angle value in table */, 
                        double minimumDiameterInitial /** minimum diameter value in table*/) :
                    Angle(angleInitial),
                    MinimumDiameter(minimumDiameterInitial)
                {
                }
            };

            private: CheckChannelRatioBuilderImpl * m_checkchannelratiobuilder_impl;
            private: friend class  _CheckChannelRatioBuilderBuilder;
            protected: CheckChannelRatioBuilder();
            public: ~CheckChannelRatioBuilder();
            /** Gets angle and minimum diameter pair values. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: void GetTableData
            (
                std::vector<NXOpen::Validate::CheckChannelRatioBuilder::TableData> & tableData /** TableData type values. */
            );
            /** Sets angle and minimum diameter pair values. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: void SetTableData
            (
                const std::vector<NXOpen::Validate::CheckChannelRatioBuilder::TableData> & tableData /** TableData type values. */
            );
            /** Returns the selected faces  @return  
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXOpen::Face *> GetFaces
            (
            );
            /** Set the selected faces 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: void SetFaces
            (
                const std::vector<NXOpen::Face *> & faces /** The objects to apply the attributes to. */
            );
            /** Returns the selected Bodies  @return  
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXOpen::Body *> GetBodies
            (
            );
            /** Set the Bodies 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: void SetBodies
            (
                const std::vector<NXOpen::Body *> & bodies /** The objects to apply the attributes to. */
            );
            /**Returns  the maximum width of channel openings 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: double MaximumWidth
            (
            );
            /**Sets  the maximum width of channel openings 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: void SetMaximumWidth
            (
                double maximumWidth /** maximumwidth */ 
            );
            /**Returns  the draw origin 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Point3d Origin
            (
            );
            /**Sets  the draw origin 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: void SetOrigin
            (
                const NXOpen::Point3d & origin /** origin */ 
            );
            /**Returns  the draw orientation 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Matrix3x3 Orientation
            (
            );
            /**Sets  the draw orientation 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: void SetOrientation
            (
                const NXOpen::Matrix3x3 & orientation /** orientation */ 
            );
            /**Returns  the segment length  
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: double SegmentLength
            (
            );
            /**Sets  the segment length  
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: void SetSegmentLength
            (
                double segmentLength /** segmentlength */ 
            );
            /**Returns  the minimum ratio  
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: double MinimumRatio
            (
            );
            /**Sets  the minimum ratio  
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: void SetMinimumRatio
            (
                double minimumRatio /** minimumratio */ 
            );
            /**Returns  the color for segments with sufficient diameters. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::NXColor * PassedSegmentsColor
            (
            );
            /**Sets  the color for segments with sufficient diameters. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: void SetPassedSegmentsColor
            (
                NXOpen::NXColor * passedColor /** passedcolor */ 
            );
            /**Returns  the color for segments with insufficient diameters. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::NXColor * FailedSegmentsColor
            (
            );
            /**Sets  the color for segments with insufficient diameters. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: void SetFailedSegmentsColor
            (
                NXOpen::NXColor * failedColor /** failedcolor */ 
            );
            /**Returns  the toggle that show only failed segments 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: bool ShowOnlyFailedSegments
            (
            );
            /**Sets  the toggle that show only failed segments 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: void SetShowOnlyFailedSegments
            (
                bool showOnlyFailedSegments /** showonlyfailedsegments */ 
            );
            /**Returns  the automatic update toggle 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: bool AutomaticUpdate
            (
            );
            /**Sets  the automatic update toggle 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: void SetAutomaticUpdate
            (
                bool automaticUpdate /** automaticupdate */ 
            );
            /**Returns  the preview toggle 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: bool PreviewState
            (
            );
            /**Sets  the preview toggle 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: void SetPreviewState
            (
                bool previewState /** previewstate */ 
            );
            /** Sets the needRegenerateFacets toggle 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: void SetNeedRegenerateFacets
            (
                bool needRegenerateFacets /** needregeneratefacets */ 
            );
            /**Returns  the display resolution 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricUtilities::DisplayResolutionBuilder * DisplayResolution
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