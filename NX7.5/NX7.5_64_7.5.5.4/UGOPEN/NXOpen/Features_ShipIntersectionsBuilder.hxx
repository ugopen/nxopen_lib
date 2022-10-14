#ifndef NXOpen_FEATURES_SHIPINTERSECTIONSBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_SHIPINTERSECTIONSBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_ShipIntersectionsBuilder.ja
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
#include <NXOpen/Features_FeatureBuilder.hxx>
#include <NXOpen/Features_ShipIntersectionsBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Features
    {
        class ShipIntersectionsBuilder;
    }
    namespace Features
    {
        class FeatureBuilder;
    }
    namespace Features
    {
        class _ShipIntersectionsBuilderBuilder;
        class ShipIntersectionsBuilderImpl;
        /**
            Represents a @link Features::ShipIntersections Features::ShipIntersections@endlink  builder
             <br> To create a new instance of this class, use @link Features::FeatureCollection::CreateShipIntersectionsBuilder Features::FeatureCollection::CreateShipIntersectionsBuilder@endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        BulkheadEnum </td> <td> 
         
        None </td> </tr> 

        <tr><td> 
         
        DeckEnum </td> <td> 
         
        None </td> </tr> 

        <tr><td> 
         
        InterTransFrameEnum </td> <td> 
         
        None </td> </tr> 

        <tr><td> 
         
        TransFrameEnum </td> <td> 
         
        None </td> </tr> 

        <tr><td> 
         
        YFrameEnum </td> <td> 
         
        None </td> </tr> 

        <tr><td> 
         
        ZFrameEnum </td> <td> 
         
        None </td> </tr> 

        </table>  
        */
        class NXOPENCPPEXPORT  ShipIntersectionsBuilder : public Features::FeatureBuilder
        {
            /** Define the output option for each of the frame type */
            public: enum Type
            {
                TypeNone/** none */ ,
                TypeSheetBodies/** sheet bodies */ ,
                TypeCurves/** curves */ ,
                TypeAll/** all */ 
            };

            private: ShipIntersectionsBuilderImpl * m_shipintersectionsbuilder_impl;
            private: friend class  _ShipIntersectionsBuilderBuilder;
            protected: ShipIntersectionsBuilder();
            public: ~ShipIntersectionsBuilder();
            /**Returns  Set the output option for the Bulkhead Frames   <br> License requirements : None */
            public: NXOpen::Features::ShipIntersectionsBuilder::Type BulkheadEnum
            (
            );
            /**Sets  Set the output option for the Bulkhead Frames   <br> License requirements : nx_ship_concept ("Ship Concept") */
            public: void SetBulkheadEnum
            (
                NXOpen::Features::ShipIntersectionsBuilder::Type bulkheadEnum /** bulkheadenum */ 
            );
            /**Returns  Set the output option for the Transverse Frames   <br> License requirements : None */
            public: NXOpen::Features::ShipIntersectionsBuilder::Type TransFrameEnum
            (
            );
            /**Sets  Set the output option for the Transverse Frames   <br> License requirements : nx_ship_concept ("Ship Concept") */
            public: void SetTransFrameEnum
            (
                NXOpen::Features::ShipIntersectionsBuilder::Type transFrameEnum /** transframeenum */ 
            );
            /**Returns  Set the output option for the Inter Transverse Frames   <br> License requirements : None */
            public: NXOpen::Features::ShipIntersectionsBuilder::Type InterTransFrameEnum
            (
            );
            /**Sets  Set the output option for the Inter Transverse Frames   <br> License requirements : nx_ship_concept ("Ship Concept") */
            public: void SetInterTransFrameEnum
            (
                NXOpen::Features::ShipIntersectionsBuilder::Type interTransFrameEnum /** intertransframeenum */ 
            );
            /**Returns  Set the output option for the Longitudinal Y Frames   <br> License requirements : None */
            public: NXOpen::Features::ShipIntersectionsBuilder::Type YFrameEnum
            (
            );
            /**Sets  Set the output option for the Longitudinal Y Frames   <br> License requirements : nx_ship_concept ("Ship Concept") */
            public: void SetYFrameEnum
            (
                NXOpen::Features::ShipIntersectionsBuilder::Type yFrameEnum /** yframeenum */ 
            );
            /**Returns  Set the output option for the Longitudinal Z Frames   <br> License requirements : None */
            public: NXOpen::Features::ShipIntersectionsBuilder::Type DeckEnum
            (
            );
            /**Sets  Set the output option for the Longitudinal Z Frames   <br> License requirements : nx_ship_concept ("Ship Concept") */
            public: void SetDeckEnum
            (
                NXOpen::Features::ShipIntersectionsBuilder::Type deckEnum /** deckenum */ 
            );
            /**Returns  Set the output option for the Longitudinal Z Frames   <br> License requirements : None */
            public: NXOpen::Features::ShipIntersectionsBuilder::Type ZFrameEnum
            (
            );
            /**Sets  Set the output option for the Longitudinal Z Frames   <br> License requirements : nx_ship_concept ("Ship Concept") */
            public: void SetZFrameEnum
            (
                NXOpen::Features::ShipIntersectionsBuilder::Type zFrameEnum /** zframeenum */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif