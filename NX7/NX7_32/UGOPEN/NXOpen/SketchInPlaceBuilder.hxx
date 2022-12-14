#ifndef NXOpen_SKETCHINPLACEBUILDER_HXX_INCLUDED
#define NXOpen_SKETCHINPLACEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     SketchInPlaceBuilder.ja
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
#include <NXOpen/SelectObject.hxx>
#include <NXOpen/Sketch.hxx>
#include <NXOpen/SketchInPlaceBuilder.hxx>
#include <NXOpen/type.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    class SketchInPlaceBuilder;
    class Builder;
    class Plane;
    class SelectIReferenceAxis;
    class SelectISurface;
    class _SketchInPlaceBuilderBuilder;
    /**
        Use the @link SketchInPlaceBuilder SketchInPlaceBuilder@endlink  to create or reattach a @link Sketch Sketch@endlink  on a @link DatumPlane DatumPlane@endlink  or planar @link Face Face@endlink .
         <br> To create a new instance of this class, use @link SketchCollection::CreateSketchInPlaceBuilder SketchCollection::CreateSketchInPlaceBuilder@endlink  <br> */
    class NXOPENCPPEXPORT SketchInPlaceBuilder : public Builder
    {
        private: friend class  _SketchInPlaceBuilderBuilder;
        protected: SketchInPlaceBuilder();
        /**Returns  the specified sketch plane    <br> License requirements : None */
        public: NXOpen::SelectISurface * PlaneOrFace
        (
        );
        /**Returns  the specified datum plane    <br> License requirements : None */
        public: NXOpen::Plane * Plane
        (
        );
        /**Returns  the flag to indicate the normal direction of the sketch plane is reversed.  This is not applicable when the plane is a Face.  <br> License requirements : None */
        public: bool ReversePlaneNormal
        (
        );
        /**Sets  the flag to indicate the normal direction of the sketch plane is reversed.  This is not applicable when the plane is a Face.  <br> License requirements : None */
        public: void SetReversePlaneNormal
        (
            bool reversePlaneNormal /** reverseplanenormal */ 
        );
        /**Returns  the attachment plane option (existing plane, new plane, new csys)  <br> License requirements : None */
        public: NXOpen::Sketch::PlaneOption PlaneOption
        (
        );
        /**Sets  the attachment plane option (existing plane, new plane, new csys)  <br> License requirements : None */
        public: void SetPlaneOption
        (
            NXOpen::Sketch::PlaneOption planeOption /** planeoption */ 
        );
        /**Returns  the reference axis orientation (horizontal or vertical)  <br> License requirements : None */
        public: NXOpen::AxisOrientation AxisOrientation
        (
        );
        /**Sets  the reference axis orientation (horizontal or vertical)  <br> License requirements : None */
        public: void SetAxisOrientation
        (
            NXOpen::AxisOrientation axisOrientation /** axisorientation */ 
        );
        /**Returns  the reference axis  <br> License requirements : None */
        public: NXOpen::SelectIReferenceAxis * Axis
        (
        );
        /**Returns  the flag to indicate the reference axis is reversed  <br> License requirements : None */
        public: bool ReverseAxis
        (
        );
        /**Sets  the flag to indicate the reference axis is reversed  <br> License requirements : None */
        public: void SetReverseAxis
        (
            bool reverseAxis /** reverseaxis */ 
        );
    };
}
#undef EXPORTLIBRARY
#endif
