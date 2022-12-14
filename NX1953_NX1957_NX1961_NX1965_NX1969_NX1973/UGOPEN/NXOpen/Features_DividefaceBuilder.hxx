#ifndef NXOpen_FEATURES_DIVIDEFACEBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_DIVIDEFACEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_DividefaceBuilder.ja
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
#include <NXOpen/GeometricUtilities_SelectDividingObjectBuilder.hxx>
#include <NXOpen/Features_FeatureBuilder.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/libnxopencpp_features_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Features
    {
        class DividefaceBuilder;
    }
    namespace Features
    {
        class FeatureBuilder;
    }
    namespace GeometricUtilities
    {
        class ProjectionOptions;
    }
    namespace GeometricUtilities
    {
        class SelectDividingObjectBuilder;
    }
    class ScCollector;
    class SelectDisplayableObjectList;
    namespace Features
    {
        class _DividefaceBuilderBuilder;
        class DividefaceBuilderImpl;
        /** Represents a divide face builder. Inputs to this class can be convergent objects.  <br> To create a new instance of this class, use @link NXOpen::Features::FeatureCollection::CreateDividefaceBuilder  NXOpen::Features::FeatureCollection::CreateDividefaceBuilder @endlink  <br> 
        Default values.
        <list type="table"> 
         
        <listheader><term> 
        Property</term>  <description> 
        Value</description> </listheader>
        <item><term> 
         
        SelectDividingObject.OffsetDistance.Value </term> <description> 
         
        5 (millimeters part), 0.2 (inches part) </description> </item> 

        <item><term> 
         
        SelectDividingObject.ToolOption </term> <description> 
         
        Object </description> </item> 

        </list> 

         <br>  Created in NX4.0.0.  <br>  
        */
        class NXOPENCPP_FEATURESEXPORT  DividefaceBuilder : public NXOpen::Features::FeatureBuilder
        {
            private: DividefaceBuilderImpl * m_dividefacebuilder_impl;
            private: friend class  _DividefaceBuilderBuilder;
            protected: DividefaceBuilder();
            public: ~DividefaceBuilder();
            /**Sets  the Faces to Divide 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR cam_base ("CAM BASE") OR insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetFacesToDivide
            (
                NXOpen::ScCollector * facesToDivide /** Smart collector for faces to divide */
            );
            /**Returns  the Faces to Divide 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::ScCollector * FacesToDivide
            (
            );
            /**Returns  the Projection Options data 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricUtilities::ProjectionOptions * ProjectionOption
            (
            );
            /**Sets  the tolerance 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR cam_base ("CAM BASE") OR insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetTolerance
            (
                double tolerance /** Tolerance */
            );
            /**Returns  the tolerance 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: double Tolerance
            (
            );
            /**Sets  the curve blanking option 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR cam_base ("CAM BASE") OR insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetBlankOption
            (
                bool blank /** false: maintain curves; true: blank curves */
            );
            /**Returns  the curve blanking option 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: bool BlankOption
            (
            );
            /**Sets  the Extend resulting edges to boundary 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR cam_base ("CAM BASE") OR insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetExtendOption
            (
                bool extend /** false: do not extend curves; true: extend curves */
            );
            /**Returns  the Extend resulting edges to boundary 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: bool ExtendOption
            (
            );
            /**Sets  the Do not project curves that lie on face 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR cam_base ("CAM BASE") OR insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetProjectCurvesThatLieOnFaceOption
            (
                bool projectCurvesThatLieOnFace /** false: project curves that lie on face option; true: Do not project curves that lie on face option */
            );
            /**Returns  the Do not project curves that lie on face 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: bool ProjectCurvesThatLieOnFaceOption
            (
            );
            /**Returns  the Dividing Objects 
             <br>  @deprecated Deprecated in NX9.0.0.  This is for pre NX9 usage, do not use this method.  Instead use @link NXOpen::Features::DividefaceBuilder::SelectDividingObject NXOpen::Features::DividefaceBuilder::SelectDividingObject@endlink  instead. <br>  

             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX9.0.0.  This is for pre NX9 usage, do not use this method.  Instead use NXOpen::Features::DividefaceBuilder::SelectDividingObject instead.") NXOpen::SelectDisplayableObjectList * DividingObjectsList
            (
            );
            /**Returns  the Select Dividing Objects 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricUtilities::SelectDividingObjectBuilder * SelectDividingObject
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
