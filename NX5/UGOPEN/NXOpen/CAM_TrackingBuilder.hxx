#ifndef NXOpen_CAM_TRACKINGBUILDER_HXX_INCLUDED
#define NXOpen_CAM_TRACKINGBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_TrackingBuilder.ja
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
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAM
    {
        class TrackingBuilder;
    }
    class Builder;
    class NXObject;
    namespace CAM
    {
        class _TrackingBuilderBuilder;
        /** Represents a Tracking Builder  <br> This is an abstract class, and cannot be instantiated. <br> */
        class NXOPENCPPEXPORT TrackingBuilder : public Builder
        {
            private: friend class  _TrackingBuilderBuilder;
            protected: TrackingBuilder();
            /** Create a new track point  @return   <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::NXObject * Create
            (
                const NXString & name /** the name   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                int radiusId /** the radius ID */,
                int tpNumber /** the track point number */,
                double angle /** the angle */,
                double radius /** the radius */,
                double xOffset /** the xoffset */,
                double yOffset /** the yoffset */,
                int adjustReg /** the adjust register */,
                int cutcomReg /** the cutcom register */
            );
            /** Modify an existing track point  <br> License requirements : cam_base ("CAM BASE") */
            public: void Modify
            (
                NXOpen::NXObject * pointTag /** the current selected entry */,
                const NXString & name /** the name   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                int radiusId /** the radius ID */,
                int tpNumber /** the track point number */,
                double angle /** the angle */,
                double radius /** the radius */,
                double xOffset /** the xoffset */,
                double yOffset /** the yoffset */,
                int adjustReg /** the adjust register */,
                int cutcomReg /** the cutcom register */
            );
            /** Delete an existing track point  <br> License requirements : cam_base ("CAM BASE") */
            public: void Delete
            (
                NXOpen::NXObject * pointTag /** the deleted track point */
            );
            /** Get the values of an existing track point  <br> License requirements : cam_base ("CAM BASE") */
            public: void Get
            (
                NXOpen::NXObject * pointTag /** the track point */,
                NXString* name /** the name */,
                int* radiusId /** the radius ID */,
                int* tpNumber /** the track point number */,
                double* angle /** the angle */,
                double* radius /** the radius */,
                double* xOffset /** the xoffset */,
                double* yOffset /** the yoffset */,
                int* adjustReg /** the adjust register */,
                int* cutcomReg /** the cutcom register */
            );
            /**Returns  the number of track points  <br> License requirements : cam_base ("CAM BASE") */
            public: int NumberOfTrackPoints
            (
            );
            /** Get a specific track point  @return  the track point  <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::NXObject * GetTrackPoint
            (
                int position /** the position of track point */
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif