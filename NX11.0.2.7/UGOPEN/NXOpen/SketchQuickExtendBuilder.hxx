#ifndef NXOpen_SKETCHQUICKEXTENDBUILDER_HXX_INCLUDED
#define NXOpen_SKETCHQUICKEXTENDBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     SketchQuickExtendBuilder.ja
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
#include <NXOpen/SketchQuickExtendBuilder.hxx>
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
    class SketchQuickExtendBuilder;
    class Builder;
    class SelectCurveList;
    class SelectNXObjectList;
    class _SketchQuickExtendBuilderBuilder;
    class SketchQuickExtendBuilderImpl;
    /**
        Represents a @link NXOpen::SketchQuickExtendBuilder NXOpen::SketchQuickExtendBuilder@endlink 
         <br> To create a new instance of this class, use @link NXOpen::SketchCollection::CreateQuickExtendBuilder  NXOpen::SketchCollection::CreateQuickExtendBuilder @endlink  <br> 
    Default values.
    <table border="1"> 
     
    <tr><th> 
    Property</th>  <th> 
    Value</th> </tr>
    <tr><td> 
     
    ExtendBound </td> <td> 
     
    True </td> </tr> 

    </table>  

     <br>  Created in NX5.0.0.  <br>  
    */
    class NXOPENCPPEXPORT  SketchQuickExtendBuilder : public NXOpen::Builder
    {
        private: SketchQuickExtendBuilderImpl * m_sketchquickextendbuilder_impl;
        private: friend class  _SketchQuickExtendBuilderBuilder;
        protected: SketchQuickExtendBuilder();
        public: ~SketchQuickExtendBuilder();
        /**Returns  the extended curves 
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::SelectCurveList * ExtendedCurves
        (
        );
        /**Returns  the boundary curves 
         <br>  @deprecated Deprecated in NX9.0.0.  Use @link NXOpen::SketchQuickExtendBuilder::BoundaryObjects NXOpen::SketchQuickExtendBuilder::BoundaryObjects@endlink  instead. <br>  

         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : None */
        public:  NX_DEPRECATED("Deprecated in NX9.0.0.  Use NXOpen::SketchQuickExtendBuilder::BoundaryObjects instead.") NXOpen::SelectCurveList * BoundaryCurves
        (
        );
        /**Returns  the boundary objects 
         <br>  Created in NX9.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::SelectNXObjectList * BoundaryObjects
        (
        );
        /**Returns  the flag to control the ability to extend to extension of the boundary 
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        public: bool ExtendBound
        (
        );
        /**Sets  the flag to control the ability to extend to extension of the boundary 
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        public: void SetExtendBound
        (
            bool extendBound /** extendbound */ 
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