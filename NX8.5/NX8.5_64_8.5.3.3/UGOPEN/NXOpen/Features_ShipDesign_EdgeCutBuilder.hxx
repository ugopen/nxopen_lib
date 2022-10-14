#ifndef NXOpen_FEATURES_SHIPDESIGN_EDGECUTBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_SHIPDESIGN_EDGECUTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_ShipDesign_EdgeCutBuilder.ja
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
#include <NXOpen/Features_FeatureBuilder.hxx>
#include <NXOpen/Features_ShipDesign_EdgeCutBuilder.hxx>
#include <NXOpen/Features_ShipDesign_ManufacturingStockBuilder.hxx>
#include <NXOpen/Features_ShipDesign_SteelFeatureSpreadsheetBuilder.hxx>
#include <NXOpen/GeometricUtilities_OnPathDimensionBuilder.hxx>
#include <NXOpen/Section.hxx>
#include <NXOpen/SelectObject.hxx>
#include <NXOpen/SelectObjectList.hxx>
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
        namespace ShipDesign
        {
            class EdgeCutBuilder;
        }
    }
    class Expression;
    namespace Features
    {
        class FeatureBuilder;
    }
    namespace Features
    {
        namespace ShipDesign
        {
            class ManufacturingStockBuilder;
        }
    }
    namespace Features
    {
        namespace ShipDesign
        {
            class SteelFeatureSpreadsheetBuilder;
        }
    }
    namespace GeometricUtilities
    {
        class OnPathDimensionBuilder;
    }
    class Section;
    class SelectFaceList;
    class SelectNXObject;
    namespace Features
    {
        namespace ShipDesign
        {
            class _EdgeCutBuilderBuilder;
            class EdgeCutBuilderImpl;
            /**
                Represents a @link Features::ShipDesign::EdgeCut Features::ShipDesign::EdgeCut@endlink  builder.  The Edge Cut creates a series of cuts with an offset from an edge or curve.
                 <br> To create a new instance of this class, use @link Features::ShipCollection::CreateEdgeCutBuilder  Features::ShipCollection::CreateEdgeCutBuilder @endlink  <br> 
            Default values.
            <table border="1"> 
             
            <tr><th> 
            Property</th>  <th> 
            Value</th> </tr>
            <tr><td> 
             
            CutCount </td> <td> 
             
            0 </td> </tr> 

            <tr><td> 
             
            CutOrientationAngle.Value </td> <td> 
             
            0 </td> </tr> 

            <tr><td> 
             
            GuideOffset.Value </td> <td> 
             
            50 (millimeters part), 2 (inches part) </td> </tr> 

            <tr><td> 
             
            SpaceBetweenCuts.Value </td> <td> 
             
            50 (millimeters part), 2 (inches part) </td> </tr> 

            <tr><td> 
             
            Spacing </td> <td> 
             
            EvenDistribution </td> </tr> 

            <tr><td> 
             
            SymmetricOffsets </td> <td> 
             
            0 </td> </tr> 

            </table>  

             <br>  Created in NX8.5.0.  <br>  
            */
            class NXOPENCPP_FEATURESEXPORT  EdgeCutBuilder : public Features::FeatureBuilder
            {
                /** available methods used to define the spacing between the cuts
                         */
                public: enum ArraySpacing
                {
                    ArraySpacingEvenDistribution/** Cuts will automatically be spaced evenly along the length of the guide */,
                    ArraySpacingCustomDefined/** The user can specify a custom amount of space between the cuts */
                };

                private: EdgeCutBuilderImpl * m_edgecutbuilder_impl;
                private: friend class  _EdgeCutBuilderBuilder;
                protected: EdgeCutBuilder();
                public: ~EdgeCutBuilder();
                /**Returns  the select target face 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::SelectFaceList * SelectTargetFace
                (
                );
                /**Returns  the guide curve used to place the cuts (may be made up of edges or curves) 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Section * GuideCurve
                (
                );
                /**Returns  the select start limit.  The start limit is used to trim the start of the guide curve. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::SelectNXObject * SelectStartLimit
                (
                );
                /**Returns  the select end limit.  The end limit is used to trim the end of the guide curve.  Note if the spacing is set to CustomDefined, 
                            you won't notice the end trim getting used, unless you try to place too many cuts between the start and end trim (including any offsets 
                            added by the Start and End positions on the guide). 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::SelectNXObject * SelectEndLimit
                (
                );
                /**Returns  the guide offset (how far away to place the cuts from the guide curve) 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * GuideOffset
                (
                );
                /**Returns  the cut orientation angle.  Typically the x axis of the cut's cross section sketch is parallel to the guide curve, the orientation angle rotates the sketch away from the guide curve 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * CutOrientationAngle
                (
                );
                /**Returns  the spacing (even distribution or custom defined) 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::ShipDesign::EdgeCutBuilder::ArraySpacing Spacing
                (
                );
                /**Sets  the spacing (even distribution or custom defined) 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : nx_ship_detail ("Ship Detail Design") */
                public: void SetSpacing
                (
                    NXOpen::Features::ShipDesign::EdgeCutBuilder::ArraySpacing spacing /** spacing */ 
                );
                /**Returns  the number of cuts 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: int CutCount
                (
                );
                /**Sets  the number of cuts 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : nx_ship_detail ("Ship Detail Design") */
                public: void SetCutCount
                (
                    int cutCount /** cutcount */ 
                );
                /**Returns  the symmetric offsets toggle.  Note this is ignored if spacing is set to custom defined.  When symmetric offsets are used, the length of the 
                            guide is divided by the number of cuts to define the space between cuts, and half of the distance between each cut is applied as a start and end 
                            offset along the guide. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: bool SymmetricOffsets
                (
                );
                /**Sets  the symmetric offsets toggle.  Note this is ignored if spacing is set to custom defined.  When symmetric offsets are used, the length of the 
                            guide is divided by the number of cuts to define the space between cuts, and half of the distance between each cut is applied as a start and end 
                            offset along the guide. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : nx_ship_detail ("Ship Detail Design") */
                public: void SetSymmetricOffsets
                (
                    bool symmetricOffsets /** symmetricoffsets */ 
                );
                /**Returns  the distance between each cut.  Note this is ignored if spacing is set to equal spacing. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * SpaceBetweenCuts
                (
                );
                /**Returns  the offset from the start of the guide curve (or start trim object) where cut placement will begin 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::GeometricUtilities::OnPathDimensionBuilder * StartPositionOnGuide
                (
                );
                /**Returns  the offset from the end of the guide curve (or end trim object) where cut placement will end.  Note if the spacing is set to CustomDefined, 
                            you won't notice the end trim getting used, unless you try to place too many cuts between along the guide (including any trim objects and 
                            offsets added by the Start and End positions on the guide). 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::GeometricUtilities::OnPathDimensionBuilder * EndPositionOnGuide
                (
                );
                /**Returns  the sketch block.
                             <br> 
                            Users can specify the hole shape using a single sketch. The sketch type and its parameters
                            are controlled by the @link Features::ShipDesign::SteelFeatureSpreadsheetBuilder Features::ShipDesign::SteelFeatureSpreadsheetBuilder@endlink .
                             <br> 
                        
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::ShipDesign::SteelFeatureSpreadsheetBuilder * SketchBlock
                (
                );
                /**Returns  the manufacturing stock builder that holds the manufacturing data. 
                 <br>  Created in NX8.5.1.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::ShipDesign::ManufacturingStockBuilder * ManufacturingInformation
                (
                );
            };
        }
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