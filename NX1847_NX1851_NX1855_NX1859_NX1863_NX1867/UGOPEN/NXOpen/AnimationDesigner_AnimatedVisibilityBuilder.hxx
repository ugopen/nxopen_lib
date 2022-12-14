#ifndef NXOpen_ANIMATIONDESIGNER_ANIMATEDVISIBILITYBUILDER_HXX_INCLUDED
#define NXOpen_ANIMATIONDESIGNER_ANIMATEDVISIBILITYBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     AnimationDesigner_AnimatedVisibilityBuilder.ja
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
#include <NXOpen/Builder.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/libanimationdesigneropencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace AnimationDesigner
    {
        class AnimatedVisibilityBuilder;
    }
    class Builder;
    class NXColor;
    class SelectNXObjectList;
    namespace AnimationDesigner
    {
        class _AnimatedVisibilityBuilderBuilder;
        class AnimatedVisibilityBuilderImpl;
        /** Represents a @link NXOpen::AnimationDesigner::AnimatedVisibilityBuilder NXOpen::AnimationDesigner::AnimatedVisibilityBuilder@endlink .  <br> To create a new instance of this class, use @link NXOpen::AnimationDesigner::AnimatedVisibilityCollection::CreateAnimatedVisibilityBuilder  NXOpen::AnimationDesigner::AnimatedVisibilityCollection::CreateAnimatedVisibilityBuilder @endlink  <br> 
         <br>  Created in NX1847.0.0.  <br>  
        */
        class ANIMATIONDESIGNEROPENCPPEXPORT  AnimatedVisibilityBuilder : public NXOpen::Builder
        {
            /** the creation types. */
            public: enum CreationTypes
            {
                CreationTypesCombine/** Combine selections into one animated visibility */,
                CreationTypesSeparate/** Create an animated visibility for each selection */
            };

            /** the color options. */
            public: enum ColorOptions
            {
                ColorOptionsSpecifyColor/** Assigns a color to the visibility */,
                ColorOptionsAutomaticColor/** Auto-assigns a color to each visibility */,
                ColorOptionsNoColor/** Assigns no color to the visibility */
            };

            private: AnimatedVisibilityBuilderImpl * m_animatedvisibilitybuilder_impl;
            private: friend class  _AnimatedVisibilityBuilderBuilder;
            protected: AnimatedVisibilityBuilder();
            public: ~AnimatedVisibilityBuilder();
            /**Returns  the rigid group to display translucency. This can be a @link NXOpen::AnimationDesigner::RigidGroup NXOpen::AnimationDesigner::RigidGroup@endlink . 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_animationdesigner (" NX Animation Designer") */
            public: NXOpen::SelectNXObjectList * RigidGroup
            (
            );
            /**Returns  the creation type. 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_animationdesigner (" NX Animation Designer") */
            public: NXOpen::AnimationDesigner::AnimatedVisibilityBuilder::CreationTypes CreationType
            (
            );
            /**Sets  the creation type. 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_animationdesigner (" NX Animation Designer") */
            public: void SetCreationType
            (
                NXOpen::AnimationDesigner::AnimatedVisibilityBuilder::CreationTypes creationType /** creationtype */ 
            );
            /**Returns  the translucency. 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_animationdesigner (" NX Animation Designer") */
            public: int Translucency
            (
            );
            /**Sets  the translucency. 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_animationdesigner (" NX Animation Designer") */
            public: void SetTranslucency
            (
                int translucency /** translucency */ 
            );
            /** Creates a new bar. 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_animationdesigner (" NX Animation Designer") */
            public: void CreateBar
            (
                int index /** index */ 
            );
            /** Deletes the bars. 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_animationdesigner (" NX Animation Designer") */
            public: void DeleteBars
            (
                const std::vector<int> & bars /** bars */ 
            );
            /** Mirrors the bars. 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_animationdesigner (" NX Animation Designer") */
            public: void MirrorBars
            (
                const std::vector<int> & bars /** bars */ ,
                double mirrorTime /** mirror time */ 
            );
            /** Splits the bar with the split time. 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_animationdesigner (" NX Animation Designer") */
            public: void SplitBar
            (
                int index /** index */ ,
                double splitTime /** split time */ 
            );
            /** Sets the bar name. 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_animationdesigner (" NX Animation Designer") */
            public: void SetBarName
            (
                int index /** index */ ,
                const NXString & name /** name */ 
            );
            /** Sets the bar name. 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_animationdesigner (" NX Animation Designer") */
            void SetBarName
            (
                int index /** index */ ,
                const char * name /** name */ 
            );
            /** Sets the bar start time. 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_animationdesigner (" NX Animation Designer") */
            public: void SetBarStartTime
            (
                int index /** index */ ,
                double startTime /** start time */ 
            );
            /** Sets the bar end time. 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_animationdesigner (" NX Animation Designer") */
            public: void SetBarEndTime
            (
                int index /** index */ ,
                double endTime /** end time */ 
            );
            /** Sets the bar start translucency. 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_animationdesigner (" NX Animation Designer") */
            public: void SetBarStartTranslucency
            (
                int index /** index */ ,
                int translucency /** translucency */ 
            );
            /** Sets the bar end translucency. 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_animationdesigner (" NX Animation Designer") */
            public: void SetBarEndTranslucency
            (
                int index /** index */ ,
                int translucency /** translucency */ 
            );
            /**Returns  the color option. 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_animationdesigner (" NX Animation Designer") */
            public: NXOpen::AnimationDesigner::AnimatedVisibilityBuilder::ColorOptions ColorOption
            (
            );
            /**Sets  the color option. 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_animationdesigner (" NX Animation Designer") */
            public: void SetColorOption
            (
                NXOpen::AnimationDesigner::AnimatedVisibilityBuilder::ColorOptions colorOption /** coloroption */ 
            );
            /**Returns  the color. 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_animationdesigner (" NX Animation Designer") */
            public: NXOpen::NXColor * Color
            (
            );
            /**Sets  the color. 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_animationdesigner (" NX Animation Designer") */
            public: void SetColor
            (
                NXOpen::NXColor * color /** color */ 
            );
            /**Returns  the name. 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_animationdesigner (" NX Animation Designer") */
            public: NXString Name
            (
            );
            /**Sets  the name. 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_animationdesigner (" NX Animation Designer") */
            public: void SetName
            (
                const NXString & name /** name */ 
            );
            /**Sets  the name. 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_animationdesigner (" NX Animation Designer") */
            void SetName
            (
                const char * name /** name */ 
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
