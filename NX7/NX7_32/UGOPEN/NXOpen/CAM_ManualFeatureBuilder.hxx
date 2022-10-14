#ifndef NXOpen_CAM_MANUALFEATUREBUILDER_HXX_INCLUDED
#define NXOpen_CAM_MANUALFEATUREBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_ManualFeatureBuilder.ja
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
#include <NXOpen/Builder.hxx>
#include <NXOpen/CAM_ManualFeatureBuilder.hxx>
#include <NXOpen/ScCollector.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAM
    {
        class ManualFeatureBuilder;
    }
    class Builder;
    class ScCollector;
    namespace CAM
    {
        class _ManualFeatureBuilderBuilder;
        /**
            Represents a @link CAM::ManualFeatureBuilder CAM::ManualFeatureBuilder@endlink 
             <br> This is an abstract class, and cannot be instantiated. <br> */
        class NXOPENCPPEXPORT ManualFeatureBuilder : public Builder
        {
            private: friend class  _ManualFeatureBuilderBuilder;
            protected: ManualFeatureBuilder();
            /**Returns  the manual feature name  <br> License requirements : None */
            public: NXString Name
            (
            );
            /**Sets  the manual feature name  <br> License requirements : None */
            public: void SetName
            (
                const NXString & name /** name */ 
            );
            /**Returns  the manual feature floor faces  <br> License requirements : None */
            public: NXOpen::ScCollector * FloorFaces
            (
            );
            /**Sets  the manual feature floor faces  <br> License requirements : None */
            public: void SetFloorFaces
            (
                NXOpen::ScCollector * floorFaces /** floor faces */ 
            );
            /**Returns  the manual feature wall faces  <br> License requirements : None */
            public: NXOpen::ScCollector * WallFaces
            (
            );
            /**Sets  the manual feature wall faces  <br> License requirements : None */
            public: void SetWallFaces
            (
                NXOpen::ScCollector * wallFaces /** wall faces */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif