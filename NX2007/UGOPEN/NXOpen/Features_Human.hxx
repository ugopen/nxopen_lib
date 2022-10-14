#ifndef NXOpen_FEATURES_HUMAN_HXX_INCLUDED
#define NXOpen_FEATURES_HUMAN_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_Human.ja
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
#include <NXOpen/HumanReachZone.hxx>
#include <NXOpen/Features_Feature.hxx>
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
        class Human;
    }
    namespace Features
    {
        class Feature;
    }
    class HumanReachZone;
    class NXObject;
    namespace Features
    {
        class _HumanBuilder;
        class HumanImpl;
        /** Represents a human feature.  <br> To create or edit an instance of this class, use @link NXOpen::Features::HumanBuilder  NXOpen::Features::HumanBuilder @endlink  <br> 
         <br>  Created in NX4.0.0.  <br>  
        */
        class NXOPENCPP_FEATURESEXPORT  Human : public NXOpen::Features::Feature
        {
            private: HumanImpl * m_human_impl;
            private: friend class  _HumanBuilder;
            protected: Human();
            public: ~Human();
            /** Create a new @link NXOpen::HumanReachZone NXOpen::HumanReachZone@endlink  for human feature 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING"), ug_human ("Human Modelling") */
            public: void CreateReachZone
            (
                int* index /** index of the reach zone */,
                NXOpen::HumanReachZone ** reachZone /** reach zone */
            );
            /** Find the selected @link NXOpen::HumanReachZone NXOpen::HumanReachZone@endlink  for human feature  @return  reach zone 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING"), ug_human ("Human Modelling") */
            public: NXOpen::HumanReachZone * FindSelectedReachZone
            (
                NXOpen::NXObject * reachZoneGeom /** reach zone geom  */
            );
            /** Delete a @link NXOpen::HumanReachZone NXOpen::HumanReachZone@endlink  from human feature 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING"), ug_human ("Human Modelling") */
            public: void DeleteNthReachZone
            (
                int index /** index of the reach zone */
            );
            /** Get a @link NXOpen::HumanReachZone NXOpen::HumanReachZone@endlink  from human feature  @return  reach zone 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING"), ug_human ("Human Modelling") */
            public: NXOpen::HumanReachZone * GetNthReachZone
            (
                int index /** index of the reach zone */
            );
            /** Get the number of reach zones of the human feature  @return  numbers of reach zones 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING"), ug_human ("Human Modelling") */
            public: int GetNumReachZones
            (
            );
            /** Find @link NXOpen::HumanReachZone NXOpen::HumanReachZone@endlink  in a human feature by reach zone name  @return  reach zone 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING"), ug_human ("Human Modelling") */
            public: NXOpen::HumanReachZone * FindNamedReachZone
            (
                const NXString & reachZoneName /** reach zone name */
            );
            /** Find @link NXOpen::HumanReachZone NXOpen::HumanReachZone@endlink  in a human feature by reach zone name  @return  reach zone 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING"), ug_human ("Human Modelling") */
            NXOpen::HumanReachZone * FindNamedReachZone
            (
                const char * reachZoneName /** reach zone name */
            );
            /** Check whether human is correct compared with user defined base human 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING"), ug_human ("Human Modelling") */
            public: void CheckHuman
            (
                NXOpen::Features::Human * baseHuman /** User defined base human used for check */,
                bool checkHumanData /** Flag of check human data */,
                bool checkSegment /** Flag of check human segment position */,
                bool checkExpression /** Flag of check human expression */,
                bool checkReachZone /** Flag of check human reach zone */
            );
            /** Create a new  HumanHands  for human feature 
             <br>  Created in NX12.0.2.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING"), ug_human ("Human Modelling") */
            public: void CreateHumanHands
            (
            );
            /** Set Human Hands options 
             <br>  Created in NX12.0.2.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING"), ug_human ("Human Modelling") */
            public: void SetHandsData
            (
                bool create /** create */ ,
                int database /** database */ ,
                int gender /** gender */ ,
                bool glovesOn /** gloveson */ ,
                int side /** side */ ,
                double length /** length */ ,
                double breadth /** breadth */ ,
                double gloveT /** glovet */ ,
                bool forearmOn /** forearmon */ ,
                const NXString & posture /** posture */ 
            );
            /** Set Human Hands options 
             <br>  Created in NX12.0.2.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING"), ug_human ("Human Modelling") */
            void SetHandsData
            (
                bool create /** create */ ,
                int database /** database */ ,
                int gender /** gender */ ,
                bool glovesOn /** gloveson */ ,
                int side /** side */ ,
                double length /** length */ ,
                double breadth /** breadth */ ,
                double gloveT /** glovet */ ,
                bool forearmOn /** forearmon */ ,
                const char * posture /** posture */ 
            );
            /** Posture Human Hands 
             <br>  Created in NX12.0.2.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING"), ug_human ("Human Modelling") */
            public: void PostureHands
            (
                double app /** app */ ,
                const NXString & shapeName /** shapename */ ,
                bool postureOnly /** postureonly */ 
            );
            /** Posture Human Hands 
             <br>  Created in NX12.0.2.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING"), ug_human ("Human Modelling") */
            void PostureHands
            (
                double app /** app */ ,
                const char * shapeName /** shapename */ ,
                bool postureOnly /** postureonly */ 
            );
            /**  Set/modify additional v10 scaling data that has not been added to hm_params. 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING"), ug_human ("Human Modelling") */
            public: void SetV10Data
            (
                int chestMeasureType /** chestmeasuretype */ ,
                double shoulderCircum /** shouldercircum */ ,
                double chestCircum /** chestcircum */ ,
                double elbowToWrist /** elbowtowrist */ ,
                double waistCircum /** waistcircum */ ,
                int hipMeasureType /** hipmeasuretype */ ,
                double hipCircum /** hipcircum */ ,
                double kneeHeight /** kneeheight */ ,
                double sittingHeight /** sittingheight */ ,
                double handLength /** handlength */ ,
                double handBreadth /** handbreadth */ ,
                double handDepth /** handdepth */ ,
                double footLength /** footlength */ ,
                double footBreadth /** footbreadth */ ,
                int statureOpt /** stature opt */ ,
                int weightOpt /** weight opt */ ,
                int age /** age */ ,
                double shoeSoleHeight /** shoesoleheight */ ,
                double customStatureCM /** customstaturecm */ ,
                double customWeightKG /** customweightkg */ 
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