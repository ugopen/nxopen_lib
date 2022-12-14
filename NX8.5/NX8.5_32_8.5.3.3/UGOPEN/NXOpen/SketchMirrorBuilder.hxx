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
#ifdef _MSC_VER
#pragma once
#endif

#include <NXOpen/NXDeprecation.hxx>
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/SelectObject.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/SketchMirrorBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    class SketchMirrorBuilder;
    class Builder;
    class SelectNXObject;
    class SelectNXObjectList;
    class _SketchMirrorBuilderBuilder;
    class SketchMirrorBuilderImpl;
    /**
        This class is used to create a set of mirrored curves from a
        @link SketchMirrorBuilder SketchMirrorBuilder@endlink .
         <br> 
        Note that the implementation of the @link Builder::Commit Builder::Commit@endlink 
        for this class only returns the first mirror constraint created.
         <br> 
         <br> To create a new instance of this class, use @link SketchCollection::CreateSketchMirrorBuilder  SketchCollection::CreateSketchMirrorBuilder @endlink  <br> 
    Default values.
    <table border="1"> 
     
    <tr><th> 
    Property</th>  <th> 
    Value</th> </tr>
    <tr><td> 
     
    ConvertToReference </td> <td> 
     
    True </td> </tr> 

    </table>  

     <br>  Created in NX5.0.0.  <br>  
    */
    class NXOPENCPPEXPORT  SketchMirrorBuilder : public Builder
    {
        private: SketchMirrorBuilderImpl * m_sketchmirrorbuilder_impl;
        private: friend class  _SketchMirrorBuilderBuilder;
        protected: SketchMirrorBuilder();
        public: ~SketchMirrorBuilder();
        /**Returns  the center line. This must be a straight line, straight edge, datum axis or a datum plane
                that is not parallel to the plane of the sketch. If an entity is selected that is not part of sketch,
                it will be projected on the sketch plane and the projection will be used as the center line for mirror. 
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::SelectNXObject * CenterLine
        (
        );
        /**Returns  the input curves. These curves must be a part of the active sketch. Sketch curves and points can
                be mirrored using the operation. The line being used as center line can not be a part of the input curves. 
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::SelectNXObjectList * InputCurves
        (
        );
        /**Returns  the flag to indicate if the centerline needs to be converted to reference 
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : None */
        public: bool ConvertToReference
        (
        );
        /**Sets  the flag to indicate if the centerline needs to be converted to reference 
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : None */
        public: void SetConvertToReference
        (
            bool reference /** reference */ 
        );
    };
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
