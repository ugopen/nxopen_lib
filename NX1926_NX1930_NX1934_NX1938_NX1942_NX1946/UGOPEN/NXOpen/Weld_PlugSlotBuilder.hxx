#ifndef NXOpen_WELD_PLUGSLOTBUILDER_HXX_INCLUDED
#define NXOpen_WELD_PLUGSLOTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Weld_PlugSlotBuilder.ja
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
#include <NXOpen/ScCollector.hxx>
#include <NXOpen/Section.hxx>
#include <NXOpen/Weld_CharacteristicsBuilder.hxx>
#include <NXOpen/libnxopencpp_weld_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Weld
    {
        class PlugSlotBuilder;
    }
    class Expression;
    class Face;
    namespace Features
    {
        class FeatureBuilder;
    }
    class ScCollector;
    class Section;
    namespace Weld
    {
        class CharacteristicsBuilder;
    }
    namespace Weld
    {
        class _PlugSlotBuilderBuilder;
        class PlugSlotBuilderImpl;
        /** Represents a @link NXOpen::Weld::PlugSlot NXOpen::Weld::PlugSlot@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::Weld::WeldManager::CreatePlugSlotBuilder  NXOpen::Weld::WeldManager::CreatePlugSlotBuilder @endlink  <br> 
        Default values.
        <list type="table"> 
         
        <listheader><term> 
        Property</term>  <description> 
        Value</description> </listheader>
        <item><term> 
         
        AssignWeldPMI </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        ContourDepth.Value </term> <description> 
         
        2.54 (millimeters part), .1 (inches part) </description> </item> 

        <item><term> 
         
        ContourHeight.Value </term> <description> 
         
        2.54 (millimeters part), .1 (inches part) </description> </item> 

        <item><term> 
         
        ContourType </term> <description> 
         
        None </description> </item> 

        <item><term> 
         
        FieldWeld </term> <description> 
         
        0 </description> </item> 

        </list> 

         <br>  Created in NX8.0.0.  <br>  
        */
        class NXOPENCPP_WELDEXPORT  PlugSlotBuilder : public NXOpen::Features::FeatureBuilder
        {
            /** contour type */
            public: enum EnumContour
            {
                EnumContourNone/** none */ ,
                EnumContourConvex/** convex */ ,
                EnumContourFlush/** flush */ ,
                EnumContourConcave/** concave */ 
            };

            /** arc process for the weld feature */
            public: enum ArcProcessEnum
            {
                ArcProcessEnumGmaw/** gmaw */ ,
                ArcProcessEnumGtaw/** gtaw */ ,
                ArcProcessEnumGtac/** gtac */ ,
                ArcProcessEnumSmaw/** smaw */ ,
                ArcProcessEnumPaw/** paw */ 
            };

            private: PlugSlotBuilderImpl * m_plugslotbuilder_impl;
            private: friend class  _PlugSlotBuilderBuilder;
            protected: PlugSlotBuilder();
            public: ~PlugSlotBuilder();
            /**Returns  the face1 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::ScCollector * Face1
            (
            );
            /**Returns  the face2 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::ScCollector * Face2
            (
            );
            /**Returns  the edge of the hole or slot on face1 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Section * Edge1
            (
            );
            /**Returns  the contour type 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Weld::PlugSlotBuilder::EnumContour ContourType
            (
            );
            /**Sets  the contour type 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: void SetContourType
            (
                NXOpen::Weld::PlugSlotBuilder::EnumContour contourType /** contourtype */ 
            );
            /**Returns  the contour height needed for cap
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * ContourHeight
            (
            );
            /**Returns  the contour depth 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * ContourDepth
            (
            );
            /**Returns  the characteristics 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Weld::CharacteristicsBuilder * Characteristics
            (
            );
            /**Returns  the assign weld pmi 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: bool AssignWeldPMI
            (
            );
            /**Sets  the assign weld pmi 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: void SetAssignWeldPMI
            (
                bool assignWeldPMI /** assignweldpmi */ 
            );
            /**Returns  the field weld 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: bool FieldWeld
            (
            );
            /**Sets  the field weld 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: void SetFieldWeld
            (
                bool fieldWeld /** fieldweld */ 
            );
            /**Returns  the top face on face1
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Face * SeedFace1
            (
            );
            /**Sets  the top face on face1
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: void SetSeedFace1
            (
                NXOpen::Face * seedFace1 /** seedface1 */ 
            );
            /**Returns  the bottom face from which the weld will be extruded towards the top
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Face * SeedFace2
            (
            );
            /**Sets  the bottom face from which the weld will be extruded towards the top
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: void SetSeedFace2
            (
                NXOpen::Face * seedFace2 /** seedface2 */ 
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