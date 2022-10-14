#ifndef NXOpen_FEATURES_ITFRAMESBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_ITFRAMESBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_ItFramesBuilder.ja
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
#include <NXOpen/Features_FeatureBuilder.hxx>
#include <NXOpen/Features_ItFrameListItemBuilder.hxx>
#include <NXOpen/Features_ItFramesBuilder.hxx>
#include <NXOpen/ObjectList.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Features
    {
        class ItFramesBuilder;
    }
    namespace Features
    {
        class FeatureBuilder;
    }
    namespace Features
    {
        class ItFrameListItemBuilder;
    }
    namespace Features
    {
        class ItFrameListItemBuilderList;
    }
    namespace Features
    {
        class _ItFramesBuilderBuilder;
        /**
            Represents a @link Features::ItFrames Features::ItFrames@endlink  builder
             <br> To create a new instance of this class, use @link Features::FeatureCollection::CreateItFramesBuilder Features::FeatureCollection::CreateItFramesBuilder@endlink  <br> */
        class NXOPENCPPEXPORT ItFramesBuilder : public Features::FeatureBuilder
        {
            private: friend class  _ItFramesBuilderBuilder;
            protected: ItFramesBuilder();
            /**Returns  the itFrame list  <br> License requirements : None */
            public: NXOpen::Features::ItFrameListItemBuilderList * ItFrameList
            (
            );
            /** Create a list containing all required info to generate a single itFrame  @return   <br> License requirements : nx_ship_concept ("Ship Concept") */
            public: NXOpen::Features::ItFrameListItemBuilder * CreateNewItframeListItem
            (
                const NXString & startFrameName /** startframename */ ,
                const NXString & endFrameName /** endframename */ ,
                int nItFrames /** nitframes */ ,
                bool isSeed /** isseed */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif