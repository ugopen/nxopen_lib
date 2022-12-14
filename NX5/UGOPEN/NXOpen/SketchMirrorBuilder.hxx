#ifndef NXOpen_SKETCHMIRRORBUILDER_HXX_INCLUDED
#define NXOpen_SKETCHMIRRORBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     SketchMirrorBuilder.ja
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
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/SketchMirrorBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    class SketchMirrorBuilder;
    class Builder;
    class SelectNXObject;
    class SelectNXObjectList;
    class _SketchMirrorBuilderBuilder;
    /**
        This class is used to create a set of mirrored curves from a
        @link SketchMirrorBuilder SketchMirrorBuilder@endlink .
         <br> 
        Note that the implementation of the @link Builder::Commit Builder::Commit@endlink 
        for this class only returns the first mirror constraint created.
         <br> 
         <br> To create a new instance of this class, use @link SketchCollection::CreateSketchMirrorBuilder SketchCollection::CreateSketchMirrorBuilder@endlink  <br> */
    class NXOPENCPPEXPORT SketchMirrorBuilder : public Builder
    {
        private: friend class  _SketchMirrorBuilderBuilder;
        protected: SketchMirrorBuilder();
        /**Returns  the center line. This must be a straight line, straight edge, datum axis or a datum plane
                that is not parallel to the plane of the sketch. If an entity is selected that is not part of sketch,
                it will be projected on the sketch plane and the projection will be used as the center line for mirror.  <br> License requirements : None */
        public: NXOpen::SelectNXObject * CenterLine
        (
        );
        /**Returns  the input curves. These curves must be a part of the active sketch. Sketch curves and points can
                be mirrored using the operation. The line being used as center line can not be a part of the input curves.  <br> License requirements : None */
        public: NXOpen::SelectNXObjectList * InputCurves
        (
        );
        /**Returns  the flag to indicate if the centerline needs to be converted to reference  <br> License requirements : None */
        public: bool ConvertToReference
        (
        );
        /**Sets  the flag to indicate if the centerline needs to be converted to reference  <br> License requirements : None */
        public: void SetConvertToReference
        (
            bool reference /** reference */ 
        );
    };
}
#undef EXPORTLIBRARY
#endif
