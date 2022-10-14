#ifndef NXOpen_FEATURES_SHIPDESIGN_SHIPSECTIONBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_SHIPDESIGN_SHIPSECTIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_ShipDesign_ShipSectionBuilder.ja
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
#include <NXOpen/Features_ShipDesign_ReadDataSetBuilder.hxx>
#include <NXOpen/Features_ShipDesign_ShipSectionBuilder.hxx>
#include <NXOpen/Features_FeatureBuilder.hxx>
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
            class ShipSectionBuilder;
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
            class ReadDataSetBuilder;
        }
    }
    class SelectBody;
    class SelectDisplayableObjectList;
    namespace Features
    {
        namespace ShipDesign
        {
            class _ShipSectionBuilderBuilder;
            class ShipSectionBuilderImpl;
            /**
                    Represents a @link NXOpen::Features::ShipDesign::ShipSection NXOpen::Features::ShipDesign::ShipSection@endlink  builder
                     <br> To create a new instance of this class, use @link NXOpen::Features::ShipCollection::CreateShipSectionBuilder  NXOpen::Features::ShipCollection::CreateShipSectionBuilder @endlink  <br> 
            Default values.
            <table border="1"> 
             
            <tr><th> 
            Property</th>  <th> 
            Value</th> </tr>
            <tr><td> 
             
            ReadDataSet.CreateDataSetToggle </td> <td> 
             
            0 </td> </tr> 

            <tr><td> 
             
            ReadDataSet.NativeToggle </td> <td> 
             
            0 </td> </tr> 

            <tr><td> 
             
            XDatumFilter </td> <td> 
             
            All </td> </tr> 

            <tr><td> 
             
            XMaxOffset.Value </td> <td> 
             
            0 (millimeters part), 0 (inches part) </td> </tr> 

            <tr><td> 
             
            XMinOffset.Value </td> <td> 
             
            0 (millimeters part), 0 (inches part) </td> </tr> 

            <tr><td> 
             
            YMaxOffset.Value </td> <td> 
             
            0 (millimeters part), 0 (inches part) </td> </tr> 

            <tr><td> 
             
            YMinOffset.Value </td> <td> 
             
            0 (millimeters part), 0 (inches part) </td> </tr> 

            <tr><td> 
             
            ZDatumFilter </td> <td> 
             
            All </td> </tr> 

            <tr><td> 
             
            ZMaxOffset.Value </td> <td> 
             
            0 (millimeters part), 0 (inches part) </td> </tr> 

            <tr><td> 
             
            ZMinOffset.Value </td> <td> 
             
            0 (millimeters part), 0 (inches part) </td> </tr> 

            </table>  

             <br>  Created in NX7.5.0.  <br>  
            */
            class NXOPENCPP_FEATURESEXPORT  ShipSectionBuilder : public NXOpen::Features::FeatureBuilder
            {
                /** Define the creation type */
                public: enum Type
                {
                    TypeManual/** manual */ ,
                    TypeSpreadsheet/** spreadsheet */ 
                };

                /** Define the output option for each of the frame type */
                public: enum XFilter
                {
                    XFilterAll/** all */ ,
                    XFilterTransverseFrames/** transverse frames */ ,
                    XFilterBulkheads/** bulkheads */ 
                };

                /** Define the output option for each of the frame type */
                public: enum ZFilter
                {
                    ZFilterAll/** all */ ,
                    ZFilterDeckFrames/** deck frames */ ,
                    ZFilterLongitudinalFrames/** longitudinal frames */ 
                };

                private: ShipSectionBuilderImpl * m_shipsectionbuilder_impl;
                private: friend class  _ShipSectionBuilderBuilder;
                protected: ShipSectionBuilder();
                public: ~ShipSectionBuilder();
                /**Returns  the creation method 
                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::ShipDesign::ShipSectionBuilder::Type SectionType
                (
                );
                /**Sets  the creation method 
                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : nx_ship_concept ("Ship Concept") OR nx_ship_detail ("Ship Detail Design") */
                public: void SetSectionType
                (
                    NXOpen::Features::ShipDesign::ShipSectionBuilder::Type type /** type */ 
                );
                /**Returns  the assembly part 
                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : None */
                public: NXString AssemblyPart
                (
                );
                /**Sets  the assembly part 
                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : nx_ship_concept ("Ship Concept") OR nx_ship_detail ("Ship Detail Design") */
                public: void SetAssemblyPart
                (
                    const NXString & filename /** filename */ 
                );
                /**Sets  the assembly part 
                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : nx_ship_concept ("Ship Concept") OR nx_ship_detail ("Ship Detail Design") */
                void SetAssemblyPart
                (
                    const char * filename /** filename */ 
                );
                /**Returns  the section part 
                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : None */
                public: NXString SectionPart
                (
                );
                /**Sets  the section part 
                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : nx_ship_concept ("Ship Concept") OR nx_ship_detail ("Ship Detail Design") */
                public: void SetSectionPart
                (
                    const NXString & filename /** filename */ 
                );
                /**Sets  the section part 
                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : nx_ship_concept ("Ship Concept") OR nx_ship_detail ("Ship Detail Design") */
                void SetSectionPart
                (
                    const char * filename /** filename */ 
                );
                /**Returns  the section name 
                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : None */
                public: NXString SectionName
                (
                );
                /**Sets  the section name 
                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : nx_ship_concept ("Ship Concept") OR nx_ship_detail ("Ship Detail Design") */
                public: void SetSectionName
                (
                    const NXString & sectionName /** sectionname */ 
                );
                /**Sets  the section name 
                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : nx_ship_concept ("Ship Concept") OR nx_ship_detail ("Ship Detail Design") */
                void SetSectionName
                (
                    const char * sectionName /** sectionname */ 
                );
                /**Returns  the ship body 
                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::SelectBody * ShipBody
                (
                );
                /**Returns  the x datum filter 
                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::ShipDesign::ShipSectionBuilder::XFilter XDatumFilter
                (
                );
                /**Sets  the x datum filter 
                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : nx_ship_concept ("Ship Concept") OR nx_ship_detail ("Ship Detail Design") */
                public: void SetXDatumFilter
                (
                    NXOpen::Features::ShipDesign::ShipSectionBuilder::XFilter xDatumFilter /** xdatumfilter */ 
                );
                /**Returns  the x min datum filter 
                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : None */
                public: int XMinDatumFilter
                (
                );
                /**Sets  the x min datum filter 
                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : nx_ship_concept ("Ship Concept") OR nx_ship_detail ("Ship Detail Design") */
                public: void SetXMinDatumFilter
                (
                    int xMinDatumFilter /** xmindatumfilter */ 
                );
                /**Returns  the x max datum filter 
                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : None */
                public: int XMaxDatumFilter
                (
                );
                /**Sets  the x max datum filter 
                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : nx_ship_concept ("Ship Concept") OR nx_ship_detail ("Ship Detail Design") */
                public: void SetXMaxDatumFilter
                (
                    int xMaxDatumFilter /** xmaxdatumfilter */ 
                );
                /**Returns  the section xmin 
                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : None */
                public: int SectionXMin
                (
                );
                /**Sets  the section xmin 
                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : nx_ship_concept ("Ship Concept") OR nx_ship_detail ("Ship Detail Design") */
                public: void SetSectionXMin
                (
                    int sectionXMin /** sectionxmin */ 
                );
                /**Returns  the x min offset 
                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * XMinOffset
                (
                );
                /**Returns  the section xmax 
                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : None */
                public: int SectionXMax
                (
                );
                /**Sets  the section xmax 
                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : nx_ship_concept ("Ship Concept") OR nx_ship_detail ("Ship Detail Design") */
                public: void SetSectionXMax
                (
                    int sectionXMax /** sectionxmax */ 
                );
                /**Returns  the x max offset 
                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * XMaxOffset
                (
                );
                /**Returns  the y datum filter 
                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : None */
                public: int YDatumFilter
                (
                );
                /**Sets  the y datum filter 
                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : nx_ship_concept ("Ship Concept") OR nx_ship_detail ("Ship Detail Design") */
                public: void SetYDatumFilter
                (
                    int yDatumFilter /** ydatumfilter */ 
                );
                /**Returns  the y min datum filter 
                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : None */
                public: int YMinDatumFilter
                (
                );
                /**Sets  the y min datum filter 
                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : nx_ship_concept ("Ship Concept") OR nx_ship_detail ("Ship Detail Design") */
                public: void SetYMinDatumFilter
                (
                    int yMinDatumFilter /** ymindatumfilter */ 
                );
                /**Returns  the y max datum filter 
                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : None */
                public: int YMaxDatumFilter
                (
                );
                /**Sets  the y max datum filter 
                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : nx_ship_concept ("Ship Concept") OR nx_ship_detail ("Ship Detail Design") */
                public: void SetYMaxDatumFilter
                (
                    int yMaxDatumFilter /** ymaxdatumfilter */ 
                );
                /**Returns  the section ymin 
                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : None */
                public: int SectionYMin
                (
                );
                /**Sets  the section ymin 
                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : nx_ship_concept ("Ship Concept") OR nx_ship_detail ("Ship Detail Design") */
                public: void SetSectionYMin
                (
                    int sectionYMin /** sectionymin */ 
                );
                /**Returns  the y min offset 
                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * YMinOffset
                (
                );
                /**Returns  the section ymax 
                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : None */
                public: int SectionYMax
                (
                );
                /**Sets  the section ymax 
                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : nx_ship_concept ("Ship Concept") OR nx_ship_detail ("Ship Detail Design") */
                public: void SetSectionYMax
                (
                    int sectionYMax /** sectionymax */ 
                );
                /**Returns  the y max offset 
                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * YMaxOffset
                (
                );
                /**Returns  the z datum filter 
                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::ShipDesign::ShipSectionBuilder::ZFilter ZDatumFilter
                (
                );
                /**Sets  the z datum filter 
                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : nx_ship_concept ("Ship Concept") OR nx_ship_detail ("Ship Detail Design") */
                public: void SetZDatumFilter
                (
                    NXOpen::Features::ShipDesign::ShipSectionBuilder::ZFilter zDatumFilter /** zdatumfilter */ 
                );
                /**Returns  the z min datum filter 
                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : None */
                public: int ZMinDatumFilter
                (
                );
                /**Sets  the z min datum filter 
                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : nx_ship_concept ("Ship Concept") OR nx_ship_detail ("Ship Detail Design") */
                public: void SetZMinDatumFilter
                (
                    int zMinDatumFilter /** zmindatumfilter */ 
                );
                /**Returns  the z max datum filter 
                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : None */
                public: int ZMaxDatumFilter
                (
                );
                /**Sets  the z max datum filter 
                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : nx_ship_concept ("Ship Concept") OR nx_ship_detail ("Ship Detail Design") */
                public: void SetZMaxDatumFilter
                (
                    int zMaxDatumFilter /** zmaxdatumfilter */ 
                );
                /**Returns  the section zmin 
                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : None */
                public: int SectionZMin
                (
                );
                /**Sets  the section zmin 
                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : nx_ship_concept ("Ship Concept") OR nx_ship_detail ("Ship Detail Design") */
                public: void SetSectionZMin
                (
                    int sectionZMin /** sectionzmin */ 
                );
                /**Returns  the z min offset 
                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * ZMinOffset
                (
                );
                /**Returns  the section zmax 
                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : None */
                public: int SectionZMax
                (
                );
                /**Sets  the section zmax 
                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : nx_ship_concept ("Ship Concept") OR nx_ship_detail ("Ship Detail Design") */
                public: void SetSectionZMax
                (
                    int sectionZMax /** sectionzmax */ 
                );
                /**Returns  the z max offset 
                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * ZMaxOffset
                (
                );
                /**Returns  the Data Set Builder for reading data sets from Team Center  
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::ShipDesign::ReadDataSetBuilder * ReadDataSet
                (
                );
                /**Returns  the reference geometry 
                 <br>  Created in NX10.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::SelectDisplayableObjectList * ReferenceGeometry
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