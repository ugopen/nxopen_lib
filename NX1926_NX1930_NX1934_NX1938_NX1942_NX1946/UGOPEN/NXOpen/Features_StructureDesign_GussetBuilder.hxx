#ifndef NXOpen_FEATURES_STRUCTUREDESIGN_GUSSETBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_STRUCTUREDESIGN_GUSSETBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_StructureDesign_GussetBuilder.ja
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
#include <NXOpen/Features_StructureDesign_FeatureSpreadsheetBuilder.hxx>
#include <NXOpen/Features_FeatureBuilder.hxx>
#include <NXOpen/ScCollector.hxx>
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
        namespace StructureDesign
        {
            class GussetBuilder;
        }
    }
    class Direction;
    class Expression;
    namespace Features
    {
        class FeatureBuilder;
    }
    namespace Features
    {
        namespace StructureDesign
        {
            class FeatureSpreadsheetBuilder;
        }
    }
    class ScCollector;
    namespace Features
    {
        namespace StructureDesign
        {
            class _GussetBuilderBuilder;
            class GussetBuilderImpl;
            /**
                    Represents a builder which is used to create or edit a Structure Design Gusset feature.
                     <br> To create a new instance of this class, use @link NXOpen::Features::StructureDesignCollection::CreateStructureDesignGussetBuilder  NXOpen::Features::StructureDesignCollection::CreateStructureDesignGussetBuilder @endlink  <br> 
            Default values.
            <list type="table"> 
             
            <listheader><term> 
            Property</term>  <description> 
            Value</description> </listheader>
            <item><term> 
             
            ThicknessType </term> <description> 
             
            BothSides </description> </item> 

            </list> 

             <br>  Created in NX1926.0.0.  <br>  
            */
            class NXOPENCPP_FEATURESEXPORT  GussetBuilder : public NXOpen::Features::FeatureBuilder
            {
                /**
                            the thickness type 
                            */
                public: enum ThicknessTypes
                {
                    ThicknessTypesBothSides/** both sides */ ,
                    ThicknessTypesInnerSide/** inner side */ ,
                    ThicknessTypesOuterSide/** outer side */ 
                };

                private: GussetBuilderImpl * m_gussetbuilder_impl;
                private: friend class  _GussetBuilderBuilder;
                protected: GussetBuilder();
                public: ~GussetBuilder();
                /**Returns  the stock data used to define the stock information of the gusset.
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::StructureDesign::FeatureSpreadsheetBuilder * FlangeData
                (
                );
                /**Returns  the firstface to be used at locate gusset
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::ScCollector * FirstFaceSelect
                (
                );
                /**Returns   the second face to be used at locate gusset
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::ScCollector * SecondFaceSelect
                (
                );
                /**Returns  the direction to be used at thicken sketch 
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::StructureDesign::GussetBuilder::ThicknessTypes ThicknessType
                (
                );
                /**Sets  the direction to be used at thicken sketch 
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : nx_structure_design ("Structure Designer") */
                public: void SetThicknessType
                (
                    NXOpen::Features::StructureDesign::GussetBuilder::ThicknessTypes thicknessType /** thicknesstype */ 
                );
                /**Returns   @brief  the offset to the alignment plane .  

                 
                            
                                If offset is zero, the bracket molding face is aligned to the alignment plane or attachment stiffener molding face.
                             
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * OffsetDistance
                (
                );
                /**Returns   @brief  the distance tolerance (part units)  

                 
                            
                                The distance tolerance is used for:
                                <ul>
                                    <li>gusset placement orign and orientation evaluation</li>
                                    <li>gusset geometry construction</li>
                                </ul>
                            
                            
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : None */
                public: double DistanceTolerance
                (
                );
                /**Sets   @brief  the distance tolerance (part units)  

                 
                            
                                The distance tolerance is used for:
                                <ul>
                                    <li>gusset placement orign and orientation evaluation</li>
                                    <li>gusset geometry construction</li>
                                </ul>
                            
                            
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : nx_structure_design ("Structure Designer") */
                public: void SetDistanceTolerance
                (
                    double distanceTolerance /** distancetolerance */ 
                );
                /**Returns   @brief  the angular tolerance (degrees)  

                 
                            
                                The angular tolerance is used for:
                                <ul>
                                    <li>gusset placement orign and orientation evaluation</li>
                                    <li>gusset geometry construction</li>
                                </ul>
                            
                            
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : None */
                public: double AngularTolerance
                (
                );
                /**Sets   @brief  the angular tolerance (degrees)  

                 
                            
                                The angular tolerance is used for:
                                <ul>
                                    <li>gusset placement orign and orientation evaluation</li>
                                    <li>gusset geometry construction</li>
                                </ul>
                            
                            
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : nx_structure_design ("Structure Designer") */
                public: void SetAngularTolerance
                (
                    double angularTolerance /** angulartolerance */ 
                );
                /**Returns  the flag to specify whether the gusset offset distance direction is reversed or not. 
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : None */
                public: bool ReverseFlange
                (
                );
                /**Sets  the flag to specify whether the gusset offset distance direction is reversed or not. 
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : nx_structure_design ("Structure Designer") */
                public: void SetReverseFlange
                (
                    bool reverseFlange /** reverseflange */ 
                );
                /**Returns  the flag to specify whether the gusset first face is reversed or not. 
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : None */
                public: bool ReverseFirstFace
                (
                );
                /**Sets  the flag to specify whether the gusset first face is reversed or not. 
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : nx_structure_design ("Structure Designer") */
                public: void SetReverseFirstFace
                (
                    bool reverseFirstFace /** reversefirstface */ 
                );
                /**Returns  the flag to specify whether the gusset second face is reversed or not. 
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : None */
                public: bool ReverseSecondFace
                (
                );
                /**Sets  the flag to specify whether the gusset second face is reversed or not. 
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : nx_structure_design ("Structure Designer") */
                public: void SetReverseSecondFace
                (
                    bool reverseSecondFace /** reversesecondface */ 
                );
                /**Returns  the specify line to help locate gusset when one face is curved surface and the other is plane. 
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Direction * OrientVector
                (
                );
                /**Sets  the specify line to help locate gusset when one face is curved surface and the other is plane. 
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : nx_structure_design ("Structure Designer") */
                public: void SetOrientVector
                (
                    NXOpen::Direction * orientVector /** orientvector */ 
                );
                /**Returns   @brief  the pick point on reinforcement face.  

                 
                        
                            When the reinforcement face is curved (such as a cylindrical face), the bracket can
                            be placed at multiple locations, then the pick point is used.
                            The location which is closest to the pick point is used.
                             <br>  It is optional. If there are multiple candidate locations and this is not set, a random location is chosen. <br> 
                         
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Point3d PickPointOnReinforcement
                (
                );
                /**Sets   @brief  the pick point on reinforcement face.  

                 
                        
                            When the reinforcement face is curved (such as a cylindrical face), the bracket can
                            be placed at multiple locations, then the pick point is used.
                            The location which is closest to the pick point is used.
                             <br>  It is optional. If there are multiple candidate locations and this is not set, a random location is chosen. <br> 
                         
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : nx_structure_design ("Structure Designer") */
                public: void SetPickPointOnReinforcement
                (
                    const NXOpen::Point3d & pickPoint /** Pick Point type */
                );
                /**Returns   @brief  the pick point on attachment face.  

                 
                        
                            When the attachment face is curved (such as a cylindrical face), the bracket can
                            be placed at multiple locations, then the pick point is used.
                            The position which is closest to the pick point is used.
                             <br>  It is optional. If there are multiple candidate locations and this is not set, a random location is chosen. <br> 
                             <br> 
                            It is only used when @link NXOpen::Features::ShipDesign::BracketBuilder::AlignmentType NXOpen::Features::ShipDesign::BracketBuilder::AlignmentType @endlink and @link NXOpen::Features::ShipDesign::BracketBuilder::SetAlignmentType NXOpen::Features::ShipDesign::BracketBuilder::SetAlignmentType @endlink 
                            is set to @link Features::ShipDesign::BracketBuilder::AlignmentTypesDatumPlaneAlignment Features::ShipDesign::BracketBuilder::AlignmentTypesDatumPlaneAlignment@endlink .  <br> 
                         
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Point3d PickPointOnAttachment
                (
                );
                /**Sets   @brief  the pick point on attachment face.  

                 
                        
                            When the attachment face is curved (such as a cylindrical face), the bracket can
                            be placed at multiple locations, then the pick point is used.
                            The position which is closest to the pick point is used.
                             <br>  It is optional. If there are multiple candidate locations and this is not set, a random location is chosen. <br> 
                             <br> 
                            It is only used when @link NXOpen::Features::ShipDesign::BracketBuilder::AlignmentType NXOpen::Features::ShipDesign::BracketBuilder::AlignmentType @endlink and @link NXOpen::Features::ShipDesign::BracketBuilder::SetAlignmentType NXOpen::Features::ShipDesign::BracketBuilder::SetAlignmentType @endlink 
                            is set to @link Features::ShipDesign::BracketBuilder::AlignmentTypesDatumPlaneAlignment Features::ShipDesign::BracketBuilder::AlignmentTypesDatumPlaneAlignment@endlink .  <br> 
                         
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : nx_structure_design ("Structure Designer") */
                public: void SetPickPointOnAttachment
                (
                    const NXOpen::Point3d & pickPoint /** pickpoint */ 
                );
                /**Returns  the pick point normal on reinforcement face. 
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Vector3d ReinforcementPointNormal
                (
                );
                /**Sets  the pick point normal on reinforcement face. 
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : nx_structure_design ("Structure Designer") */
                public: void SetReinforcementPointNormal
                (
                    const NXOpen::Vector3d & pickPoint /** pickpoint */ 
                );
                /**Returns  the pick point normal on attachment face. 
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Vector3d AttachmentPointNormal
                (
                );
                /**Sets  the pick point normal on attachment face. 
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : nx_structure_design ("Structure Designer") */
                public: void SetAttachmentPointNormal
                (
                    const NXOpen::Vector3d & pickPoint /** pickpoint */ 
                );
                /**Returns  the gusset name 
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : None */
                public: NXString GussetName
                (
                );
                /**Sets  the gusset name 
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : nx_structure_design ("Structure Designer") */
                public: void SetGussetName
                (
                    const NXString & gussetName /** gussetname */ 
                );
                /**Sets  the gusset name 
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : nx_structure_design ("Structure Designer") */
                void SetGussetName
                (
                    const char * gussetName /** gussetname */ 
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
