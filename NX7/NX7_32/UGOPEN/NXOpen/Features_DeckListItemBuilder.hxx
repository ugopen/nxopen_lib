#ifndef NXOpen_FEATURES_DECKLISTITEMBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_DECKLISTITEMBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_DeckListItemBuilder.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/Features_DeckListItemBuilder.hxx>
#include <NXOpen/NXObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Features
    {
        class DeckListItemBuilder;
    }
    class NXObject;
    namespace Features
    {
        class _DeckListItemBuilderBuilder;
        /**
            Represents a DeckListItemBuilder 
            */
        class NXOPENCPPEXPORT DeckListItemBuilder : public NXObject
        {
            /**Represents the thickening direction */
            public: enum DatumDir
            {
                DatumDirPlus/** plus */ ,
                DatumDirMinus/** minus */ ,
                DatumDirNuetral/** nuetral */ 
            };

            private: friend class  _DeckListItemBuilderBuilder;
            protected: DeckListItemBuilder();
            /**Returns  the deck name  <br> License requirements : None */
            public: NXString DeckName
            (
            );
            /**Sets  the deck name  <br> License requirements : nx_ship_concept ("Ship Concept") */
            public: void SetDeckName
            (
                const NXString & deckName /** deckname */ 
            );
            /**Returns  the deck coord  <br> License requirements : None */
            public: double DeckCoord
            (
            );
            /**Sets  the deck coord  <br> License requirements : nx_ship_concept ("Ship Concept") */
            public: void SetDeckCoord
            (
                double deckCoord /** deckcoord */ 
            );
            /**Returns  the normal dir  <br> License requirements : None */
            public: NXOpen::Features::DeckListItemBuilder::DatumDir NormalDir
            (
            );
            /**Sets  the normal dir  <br> License requirements : nx_ship_concept ("Ship Concept") */
            public: void SetNormalDir
            (
                NXOpen::Features::DeckListItemBuilder::DatumDir normalDir /** normaldir */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif