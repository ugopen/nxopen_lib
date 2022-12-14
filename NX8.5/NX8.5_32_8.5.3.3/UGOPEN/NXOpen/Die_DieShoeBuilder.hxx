#ifndef NXOpen_DIE_DIESHOEBUILDER_HXX_INCLUDED
#define NXOpen_DIE_DIESHOEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Die_DieShoeBuilder.ja
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
#include <NXOpen/Die_DieAttributesBuilder.hxx>
#include <NXOpen/Die_DieDirectionBuilder.hxx>
#include <NXOpen/Die_DiePlaneBuilder.hxx>
#include <NXOpen/Die_DieShoeBuilder.hxx>
#include <NXOpen/Expression.hxx>
#include <NXOpen/Features_FeatureBuilder.hxx>
#include <NXOpen/ObjectList.hxx>
#include <NXOpen/Section.hxx>
#include <NXOpen/libnxopencpp_die_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Die
    {
        class DieShoeBuilder;
    }
    namespace Die
    {
        class DieAttributesBuilder;
    }
    namespace Die
    {
        class DieBooleanBuilderList;
    }
    namespace Die
    {
        class DieDirectionBuilder;
    }
    namespace Die
    {
        class DiePlaneBuilder;
    }
    class Expression;
    namespace Features
    {
        class FeatureBuilder;
    }
    class Section;
    namespace Die
    {
        class _DieShoeBuilderBuilder;
        class DieShoeBuilderImpl;
        /**
            Represents a Die Shoe feature builder.
             <br> To create a new instance of this class, use @link Die::DieCollection::DieShoe  Die::DieCollection::DieShoe @endlink  <br> 
         <br>  Created in NX6.0.0.  <br>  
        */
        class NXOPENCPP_DIEEXPORT  DieShoeBuilder : public Features::FeatureBuilder
        {
            private: DieShoeBuilderImpl * m_dieshoebuilder_impl;
            private: friend class  _DieShoeBuilderBuilder;
            protected: DieShoeBuilder();
            public: ~DieShoeBuilder();
            /**Returns  the base orientation 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Die::DiePlaneBuilder * BaseOrientation
            (
            );
            /**Returns  the base flange section 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Section * BaseFlangeSection
            (
            );
            /**Returns  the main deck section 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Section * MainDeckSection
            (
            );
            /**Returns  the main deck plane 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Die::DiePlaneBuilder * MainDeckPlane
            (
            );
            /**Returns  the offset for the main deck either measured from the main deck specification or the base plane 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * MainDeckOffset
            (
            );
            /**Returns  the cutout sections in the main deck 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Section * DeckCutoutsSection
            (
            );
            /**Returns  the toggle to create the centerline slot 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: bool CenterlineSlotCreate
            (
            );
            /**Sets  the toggle to create the centerline slot 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetCenterlineSlotCreate
            (
                bool centerlineSlotCreate /** centerlineslotcreate */ 
            );
            /**Returns  the centerline slot depth 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * CenterlineSlotDepth
            (
            );
            /**Returns  the centerline slot width 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * CenterlineSlotWidth
            (
            );
            /**Returns  the centerline slot direction 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Die::DieDirectionBuilder * CenterlineSlotDirection
            (
            );
            /**Returns  the centerline slot attributes 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Die::DieAttributesBuilder * CenterlineSlotAttributes
            (
            );
            /**Returns  the die boolean solids list 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Die::DieBooleanBuilderList * DieBooleansList
            (
            );
            /**Returns  the flange thickness 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * FlangeThickness
            (
            );
            /**Returns  the wall thickness 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * WallThickness
            (
            );
            /**Returns  the deck thickness 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * DeckThickness
            (
            );
            /**Returns  the main deck attributes 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Die::DieAttributesBuilder * MainDeckAttributes
            (
            );
            /**Returns  the base attributes 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Die::DieAttributesBuilder * BaseAttributes
            (
            );
            /**Returns  the distance tolerance 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: double DistanceTolerance
            (
            );
            /**Sets  the distance tolerance 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetDistanceTolerance
            (
                double distanceTolerance /** distancetolerance */ 
            );
            /**Returns  the angle tolerance 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: double AngleTolerance
            (
            );
            /**Sets  the angle tolerance 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetAngleTolerance
            (
                double angleTolerance /** angletolerance */ 
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
