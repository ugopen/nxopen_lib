#ifndef NXOpen_DIE_DECKPARENTBUILDER_HXX_INCLUDED
#define NXOpen_DIE_DECKPARENTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Die_DeckParentBuilder.ja
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
#include <NXOpen/Die.hxx>
#include <NXOpen/Features_FeatureBuilder.hxx>
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
        class DeckParentBuilder;
    }
    class Body;
    namespace Features
    {
        class FeatureBuilder;
    }
    class IProfile;
    class ISurface;
    namespace Die
    {
        class _DeckParentBuilderBuilder;
        class DeckParentBuilderImpl;
        /** Represents a Die Deck Feature sub feature. Used by the Upper Draw Die
         and Draw Die Punch to capture the deck definition. Unless specified, the
         attributes and methods are generic and can be applied to any type of deck.  <br> This sub feature is created via the main feature builder.  <br> 
         <br>  Created in NX4.0.0.  <br>  
        */
        class NXOPENCPP_DIEEXPORT  DeckParentBuilder : public NXOpen::Features::FeatureBuilder
        {
            private: DeckParentBuilderImpl * m_deckparentbuilder_impl;
            private: friend class  _DeckParentBuilderBuilder;
            protected: DeckParentBuilder();
            public: ~DeckParentBuilder();
            /**Sets  the inner deck sheet of deck. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetInnerDeckSheet
            (
                NXOpen::Body * innerDeckSheet /** inner deck sheet */ 
            );
            /**Returns  the inner deck sheet of deck. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: NXOpen::Body * InnerDeckSheet
            (
            );
            /** Sets the main deck profile of the upper draw die deck. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetMainDeck
            (
                NXOpen::Die::DirectionOption direction /** Profile direction. */,
                const std::vector<NXOpen::IProfile *> & profileEntries /** The profile entries, can be curves, edges, faces, sketches or curve features. */
            );
            /** Gets the main deck profile of the upper draw die deck.  @return  The profile entries, will be curves, edges, faces, sketches or curve features. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: std::vector<NXOpen::IProfile *> GetMainDeck
            (
                NXOpen::Die::DirectionOption* direction /** Profile direction. */
            );
            /** Sets the binder edge profile of the upper draw die deck. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetBinderEdge
            (
                NXOpen::Die::DirectionOption direction /** Profile direction. */,
                const std::vector<NXOpen::IProfile *> & profileEntries /** The profile entries, can be curves, edges, faces, sketches or curve features. */
            );
            /** Gets the binder edge profile of the upper draw die deck.  @return  The profile entries, will be curves, edges, faces, sketches or curve features. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: std::vector<NXOpen::IProfile *> GetBinderEdge
            (
                NXOpen::Die::DirectionOption* direction /** Profile direction. */
            );
            /** Sets the main wall centerline profile of the draw die punch.
                Knowledge Fusion: Main Deck of Upper Draw Die.
                 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetMainWallCenterline
            (
                NXOpen::Die::DirectionOption direction /** Profile direction. */,
                const std::vector<NXOpen::IProfile *> & profileEntries /** The profile entries, can be curves, edges, faces, sketches or curve features. */
            );
            /** Gets the main wall centerline profile of the draw die punch.
                  Knowledge Fusion: Main Deck of Upper Draw Die.
                  @return  The profile entries, will be curves, edges, faces, sketches or curve features. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: std::vector<NXOpen::IProfile *> GetMainWallCenterline
            (
                NXOpen::Die::DirectionOption* direction /** Profile direction. */
            );
            /** Sets the base flange profile of the draw die punch.
                Knowledge Fusion: Binder Edge of Upper Draw Die.
                 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetBaseFlange
            (
                NXOpen::Die::DirectionOption direction /** Profile direction. */,
                const std::vector<NXOpen::IProfile *> & profileEntries /** The profile entries, can be curves, edges, faces, sketches or curve features. */
            );
            /** Gets the base flange profile of the draw die punch.
                Knowledge Fusion: Binder Edge of Upper Draw Die.
                  @return  The profile entries, will be curves, edges, faces, sketches or curve features. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: std::vector<NXOpen::IProfile *> GetBaseFlange
            (
                NXOpen::Die::DirectionOption* direction /** Profile direction. */
            );
            /** Sets the intermediate deck profile of the deck. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetIntermediateDeck
            (
                NXOpen::Die::DirectionOption direction /** Profile direction. */,
                const std::vector<NXOpen::IProfile *> & profileEntries /** The profile entries, can be curves, edges, faces, sketches or curve features. */
            );
            /** Gets the intermediate deck profile of the deck.  @return  The profile entries, will be curves, edges, faces, sketches or curve features. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: std::vector<NXOpen::IProfile *> GetIntermediateDeck
            (
                NXOpen::Die::DirectionOption* direction /** Profile direction. */
            );
            /**Sets  the intermediate deck orientation of the deck. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetIntermediateDeckOrientation
            (
                NXOpen::ISurface * intermediateDeckOrientation /** intermediate deck orientation */ 
            );
            /**Returns  the intermediate deck orientation of the deck. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: NXOpen::ISurface * IntermediateDeckOrientation
            (
            );
            /**Sets  the design status of deck, if true the deck will be built into the model, if false it will not. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetDesignStatus
            (
                bool designStatus /** design status */ 
            );
            /**Returns  the design status of deck, if true the deck will be built into the model, if false it will not. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: bool DesignStatus
            (
            );
            /**Returns  the build status of deck. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: NXOpen::Die::DieBuildStatusOption BuildStatus
            (
            );
            /**Sets  the display status of deck, if true input data to the deck will be displayed, if false the input data will not be displayed. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetDisplayStatus
            (
                bool displayStatus /** display status */ 
            );
            /**Returns  the display status of deck, if true input data to the deck will be displayed, if false the input data will not be displayed. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: bool DisplayStatus
            (
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
