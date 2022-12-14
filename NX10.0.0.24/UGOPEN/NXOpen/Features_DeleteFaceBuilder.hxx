#ifndef NXOpen_FEATURES_DELETEFACEBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_DELETEFACEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_DeleteFaceBuilder.ja
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
#include <NXOpen/Features_DeleteFaceBuilder.hxx>
#include <NXOpen/Features_FeatureBuilder.hxx>
#include <NXOpen/ScCollector.hxx>
#include <NXOpen/SelectObject.hxx>
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
        class DeleteFaceBuilder;
    }
    class Expression;
    namespace Features
    {
        class FeatureBuilder;
    }
    class Plane;
    class ScCollector;
    class SelectISurface;
    namespace Features
    {
        class _DeleteFaceBuilderBuilder;
        class DeleteFaceBuilderImpl;
        /**
            Represents a builder for a delete face feature, don't use it until nx502.
             <br> To create a new instance of this class, use @link NXOpen::Features::FeatureCollection::CreateDeleteFaceBuilder  NXOpen::Features::FeatureCollection::CreateDeleteFaceBuilder @endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        CapOption </td> <td> 
         
        FaceOrPlane </td> </tr> 

        <tr><td> 
         
        DeletePartialBlend </td> <td> 
         
        False </td> </tr> 

        <tr><td> 
         
        FaceEdgeBlendPreference </td> <td> 
         
        Cliff </td> </tr> 

        <tr><td> 
         
        Heal </td> <td> 
         
        True </td> </tr> 

        <tr><td> 
         
        HealPlanar </td> <td> 
         
        False </td> </tr> 

        <tr><td> 
         
        MaxBlendRadius.Value </td> <td> 
         
        5.0 (millimeters part), 0.2 (inches part) </td> </tr> 

        <tr><td> 
         
        MaxHoleDiameter.Value </td> <td> 
         
        5.0 (millimeters part), 0.2 (inches part) </td> </tr> 

        <tr><td> 
         
        Setback </td> <td> 
         
        SelectedBlend </td> </tr> 

        <tr><td> 
         
        SpecifyBlend </td> <td> 
         
        False </td> </tr> 

        <tr><td> 
         
        UseHoleDiameter </td> <td> 
         
        True </td> </tr> 

        </table>  

         <br>  Created in NX5.0.2.  <br>  
        */
        class NXOPENCPP_FEATURESEXPORT  DeleteFaceBuilder : public NXOpen::Features::FeatureBuilder
        {
            /** Enumeration of select type, don't use it until nx502 
             <br>  Created in NX5.0.2.  <br>  
            */
            public: enum SelectTypes
            {
                SelectTypesFace/** This stands for delete face type. */,
                SelectTypesHole/** This stands for delete hole type. */,
                SelectTypesBlend/** This stands for delete blend type. */,
                SelectTypesFaceEdgeBlend/** This stands for delete notch blend type. */
            };

            /** Represents the cap option values. */
            public: enum CapOptionValues
            {
                CapOptionValuesFaceOrPlane/** face or plane. */,
                CapOptionValuesNewPlane/** new plane. */
            };

            /** Represents the set back options. */
            public: enum SetbackOptions
            {
                SetbackOptionsSelectedBlend/** Cap by setback along the selected blend.*/,
                SetbackOptionsNeighborBlend/** Cap by setback along the neighbor of the selected blend. */
            };

            /** Represents the face edge blend preference options. */
            public: enum FaceEdgeBlendPreferenceOptions
            {
                FaceEdgeBlendPreferenceOptionsNotch/** Delete as notch blend. */,
                FaceEdgeBlendPreferenceOptionsCliff/** Delete as cliff blend. */
            };

            private: DeleteFaceBuilderImpl * m_deletefacebuilder_impl;
            private: friend class  _DeleteFaceBuilderBuilder;
            protected: DeleteFaceBuilder();
            public: ~DeleteFaceBuilder();
            /**Returns  the delete face type, don't use it until nx502 
             <br>  Created in NX5.0.2.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::DeleteFaceBuilder::SelectTypes Type
            (
            );
            /**Sets  the delete face type, don't use it until nx502 
             <br>  Created in NX5.0.2.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR cam_base ("CAM BASE") */
            public: void SetType
            (
                NXOpen::Features::DeleteFaceBuilder::SelectTypes selectType /** the delete face type */
            );
            /**Returns  the face collector holding the faces to delete, don't use it until nx502 
             <br>  Created in NX5.0.2.  <br>  
             <br> License requirements : None */
            public: NXOpen::ScCollector * FaceCollector
            (
            );
            /**Returns  the flag of using hole diameter to filter hole or not, only for delete hole type and the max hole diameter should be
                        set if it is true, don't use it until nx502 
             <br>  Created in NX5.0.2.  <br>  
             <br> License requirements : None */
            public: bool UseHoleDiameter
            (
            );
            /**Sets  the flag of using hole diameter to filter hole or not, only for delete hole type and the max hole diameter should be
                        set if it is true, don't use it until nx502 
             <br>  Created in NX5.0.2.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR cam_base ("CAM BASE") */
            public: void SetUseHoleDiameter
            (
                bool useHoleDiameter /** the flag of use hole diameter */
            );
            /**Returns  the maximal diameter of deleted holes, only for delete hole type and only working when use_hole_diameter is true,
                        don't use it until nx502 
             <br>  Created in NX5.0.2.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * MaxHoleDiameter
            (
            );
            /**Returns  the flag of treating all input faces as blend, don't use it until further notification 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: bool SpecifyBlend
            (
            );
            /**Sets  the flag of treating all input faces as blend, don't use it until further notification 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR cam_base ("CAM BASE") */
            public: void SetSpecifyBlend
            (
                bool specifyBlend /** specify blend */ 
            );
            /**Returns  the flag of finding a plane in which all edges of a hole lie and attach this to a face covering the hole during heal hole process,
                        don't use it until further notification 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: bool HealPlanar
            (
            );
            /**Sets  the flag of finding a plane in which all edges of a hole lie and attach this to a face covering the hole during heal hole process,
                        don't use it until further notification 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR cam_base ("CAM BASE") */
            public: void SetHealPlanar
            (
                bool healPlanar /** heal planar */ 
            );
            /**Returns  the flag specifying whether to heal the body while deleting its face. If True, body is healed, else it is not. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: bool Heal
            (
            );
            /**Sets  the flag specifying whether to heal the body while deleting its face. If True, body is healed, else it is not. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR cam_base ("CAM BASE") */
            public: void SetHeal
            (
                bool heal /** heal */ 
            );
            /**Returns  the cap option. 
             <br>  Created in NX8.0.1.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::DeleteFaceBuilder::CapOptionValues CapOption
            (
            );
            /**Sets  the cap option. 
             <br>  Created in NX8.0.1.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR cam_base ("CAM BASE") */
            public: void SetCapOption
            (
                NXOpen::Features::DeleteFaceBuilder::CapOptionValues capOption /** capoption */ 
            );
            /**Returns  the face or plane to be used as cap face. 
             <br>  Created in NX8.0.1.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectISurface * CapFace
            (
            );
            /**Returns  the new plane to be used as cap face. 
             <br>  Created in NX8.0.1.  <br>  
             <br> License requirements : None */
            public: NXOpen::Plane * CapPlane
            (
            );
            /**Sets  the new plane to be used as cap face. 
             <br>  Created in NX8.0.1.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR cam_base ("CAM BASE") */
            public: void SetCapPlane
            (
                NXOpen::Plane * capPlane /** capplane */ 
            );
            /**Returns  the flag indicating whether to delete the partial blend or not. 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: bool DeletePartialBlend
            (
            );
            /**Sets  the flag indicating whether to delete the partial blend or not. 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR cam_base ("CAM BASE") */
            public: void SetDeletePartialBlend
            (
                bool deletePartialBlend /** deletepartialblend */ 
            );
            /**Returns  the set back options. 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::DeleteFaceBuilder::SetbackOptions Setback
            (
            );
            /**Sets  the set back options. 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR cam_base ("CAM BASE") */
            public: void SetSetback
            (
                NXOpen::Features::DeleteFaceBuilder::SetbackOptions setback /** setback */ 
            );
            /**Returns  the maximal radius of deleted blends, only for delete blend type 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * MaxBlendRadius
            (
            );
            /**Returns  the blend collector holding the blends to delete 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::ScCollector * BlendCollector
            (
            );
            /**Returns  the preference option indicating wether to delete undetermined blend chain as notch chain or as cliff chain 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::DeleteFaceBuilder::FaceEdgeBlendPreferenceOptions FaceEdgeBlendPreference
            (
            );
            /**Sets  the preference option indicating wether to delete undetermined blend chain as notch chain or as cliff chain 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR cam_base ("CAM BASE") */
            public: void SetFaceEdgeBlendPreference
            (
                NXOpen::Features::DeleteFaceBuilder::FaceEdgeBlendPreferenceOptions faceEdgeBlendPreference /** faceedgeblendpreference */ 
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
