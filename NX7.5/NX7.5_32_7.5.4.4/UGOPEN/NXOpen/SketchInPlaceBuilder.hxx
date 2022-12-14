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
#ifdef _MSC_VER
#pragma once
#endif

#include <NXOpen/NXDeprecation.hxx>
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
    class Point;
    class SelectIReferenceAxis;
    class SelectISurface;
    class _SketchInPlaceBuilderBuilder;
    class SketchInPlaceBuilderImpl;
    /**
        Use the @link SketchInPlaceBuilder SketchInPlaceBuilder@endlink  to create or reattach a @link Sketch Sketch@endlink  on a @link DatumPlane DatumPlane@endlink  or planar @link Face Face@endlink .
         <br> To create a new instance of this class, use @link SketchCollection::CreateNewSketchInPlaceBuilder SketchCollection::CreateNewSketchInPlaceBuilder@endlink  <br> 
    Default values.
    <table border="1"> 
     
    <tr><th> 
    Property</th>  <th> 
    Value</th> </tr>
    <tr><td> 
     
    CreateIntermediateDatumCsys </td> <td> 
     
    1 </td> </tr> 

    <tr><td> 
     
    MakeOriginAssociative </td> <td> 
     
    1 </td> </tr> 

    <tr><td> 
     
    PlaneOption </td> <td> 
     
    Inferred </td> </tr> 

    </table>  
    */
    class NXOPENCPPEXPORT  SketchInPlaceBuilder : public Builder
    {
        private: SketchInPlaceBuilderImpl * m_sketchinplacebuilder_impl;
        private: friend class  _SketchInPlaceBuilderBuilder;
        protected: SketchInPlaceBuilder();
        public: ~SketchInPlaceBuilder();
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
        /**Returns  the origin point for sketch  <br> License requirements : None */
        public: NXOpen::Point * SketchOrigin
        (
        );
        /**Sets  the origin point for sketch  <br> License requirements : None */
        public: void SetSketchOrigin
        (
            NXOpen::Point * origin /** origin */ 
        );
        /**Returns  the create intermediate datum csys toggle. <br> License requirements : None */
        public: bool CreateIntermediateDatumCsys
        (
        );
        /**Sets  the create intermediate datum csys toggle. <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: void SetCreateIntermediateDatumCsys
        (
            bool intermediateDatumCsys /** intermediatedatumcsys */ 
        );
        /**Returns  the associative origin toggle. <br> License requirements : None */
        public: bool MakeOriginAssociative
        (
        );
        /**Sets  the associative origin toggle. <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: void SetMakeOriginAssociative
        (
            bool associativeOrigin /** associativeorigin */ 
        );
        /**Returns  the create project work part origin toggle. <br> License requirements : None */
        public: bool ProjectWorkPartOrigin
        (
        );
        /**Sets  the create project work part origin toggle. <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: void SetProjectWorkPartOrigin
        (
            bool projectWorkPartOrigin /** projectworkpartorigin */ 
        );
    };
}
#undef EXPORTLIBRARY
#endif
