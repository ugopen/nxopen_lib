#ifndef NXOpen_FEATURES_WAVEPOINTBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_WAVEPOINTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_WavePointBuilder.ja
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
#include <NXOpen/SelectObjectList.hxx>
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
        class WavePointBuilder;
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
    class SelectPointList;
    class TaggedObject;
    namespace Features
    {
        class _WavePointBuilderBuilder;
        class WavePointBuilderImpl;
        /**
            Represents a @link Features::Feature Features::Feature@endlink  builder
             <br> To create a new instance of this class, use @link NXOpen::Features::FeatureCollection::CreateWavePointBuilder  NXOpen::Features::FeatureCollection::CreateWavePointBuilder @endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        Associative </td> <td> 
         
        True </td> </tr> 

        <tr><td> 
         
        DrawLineBetweenPoints </td> <td> 
         
        False </td> </tr> 

        <tr><td> 
         
        InheritDisplayProperties </td> <td> 
         
        False </td> </tr> 

        <tr><td> 
         
        ParentPart </td> <td> 
         
        OtherPart </td> </tr> 

        </table>  

         <br>  Created in NX5.0.0.  <br>  
        */
        class NXOPENCPP_FEATURESEXPORT  WavePointBuilder : public NXOpen::Features::FeatureBuilder
        {
            /** enum for scope of part*/
            public: enum ParentPartType
            {
                ParentPartTypeWorkPart/** intra part mode */,
                ParentPartTypeOtherPart/** inter part mode */
            };

            private: WavePointBuilderImpl * m_wavepointbuilder_impl;
            private: friend class  _WavePointBuilderBuilder;
            protected: WavePointBuilder();
            public: ~WavePointBuilder();
            /**Returns  the point to link 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectPointList * Points
            (
            );
            /**Returns  the draw line 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: bool DrawLineBetweenPoints
            (
            );
            /**Sets  the draw line 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR cam_base ("CAM BASE") OR insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetDrawLineBetweenPoints
            (
                bool drawLine /** drawline */ 
            );
            /**Returns  the fix at timestamp 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: bool FixAtCurrentTimestamp
            (
            );
            /**Sets  the fix at timestamp 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR cam_base ("CAM BASE") OR insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetFixAtCurrentTimestamp
            (
                bool timestamp /** timestamp */ 
            );
            /**Returns  the associative 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: bool Associative
            (
            );
            /**Sets  the associative 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR cam_base ("CAM BASE") OR insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetAssociative
            (
                bool associative /** associative */ 
            );
            /**Returns  the makepositionindependent 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: bool MakePositionIndependent
            (
            );
            /**Sets  the makepositionindependent 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR cam_base ("CAM BASE") OR insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetMakePositionIndependent
            (
                bool makePositionIndependent /** makepositionindependent */ 
            );
            /**Returns  the inherit display property option 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: bool InheritDisplayProperties
            (
            );
            /**Sets  the inherit display property option 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR cam_base ("CAM BASE") OR insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetInheritDisplayProperties
            (
                bool inheritDisplayProperties /** inheritdisplayproperties */ 
            );
            /** Commits the feature and set create on the fly flag  @return  
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR cam_base ("CAM BASE") OR insp_programming ("INSPECTION PROGRAMMING") */
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
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR cam_base ("CAM BASE") OR insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetFrecAtTimeStamp
            (
                NXOpen::Features::Feature * terminalFrec /** terminal frec */ 
            );
            /**Returns  the source part type 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::WavePointBuilder::ParentPartType ParentPart
            (
            );
            /**Sets  the source part type 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR cam_base ("CAM BASE") OR insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetParentPart
            (
                NXOpen::Features::WavePointBuilder::ParentPartType parentPart /** parentpart */ 
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
