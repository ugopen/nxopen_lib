#ifndef NXOpen_GEOMETRICUTILITIES_POINTFACEPLANESELECTIONBUILDER_HXX_INCLUDED
#define NXOpen_GEOMETRICUTILITIES_POINTFACEPLANESELECTIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     GeometricUtilities_PointFacePlaneSelectionBuilder.ja
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
#include <NXOpen/Expression.hxx>
#include <NXOpen/GeometricUtilities_FaceSetData.hxx>
#include <NXOpen/GeometricUtilities_LengthLimitPointBuilder.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/ScCollector.hxx>
#include <NXOpen/libnxopencpp_geometricutilities_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace GeometricUtilities
    {
        class PointFacePlaneSelectionBuilder;
    }
    class Builder;
    class Expression;
    namespace GeometricUtilities
    {
        class FaceSetData;
    }
    namespace GeometricUtilities
    {
        class LengthLimitPointBuilder;
    }
    namespace GeometricUtilities
    {
        class OnPathDimensionBuilder;
    }
    class Plane;
    class Point;
    class ScCollector;
    namespace GeometricUtilities
    {
        class _PointFacePlaneSelectionBuilderBuilder;
        class PointFacePlaneSelectionBuilderImpl;
        /**
            Represents a @link NXOpen::GeometricUtilities::PointFacePlaneSelectionBuilder NXOpen::GeometricUtilities::PointFacePlaneSelectionBuilder@endlink 
             <br> To create a new instance of this class, use @link NXOpen::GeometricUtilities::LengthLimitsListBuilder::CreatePointFacePlaneSelectionBuilder  NXOpen::GeometricUtilities::LengthLimitsListBuilder::CreatePointFacePlaneSelectionBuilder @endlink  <br> 
        Default values.
        <list type="table"> 
         
        <listheader><term> 
        Property</term>  <description> 
        Value</description> </listheader>
        <item><term> 
         
        TrimObject </term> <description> 
         
        Point </description> </item> 

        <item><term> 
         
        UseFaceCapBlend </term> <description> 
         
        1 </description> </item> 

        <item><term> 
         
        UsePlaneCapBlend </term> <description> 
         
        0 </description> </item> 

        </list> 

         <br>  Created in NX1899.0.0.  <br>  
        */
        class NXOPENCPP_GEOMETRICUTILITIESEXPORT  PointFacePlaneSelectionBuilder : public NXOpen::Builder
        {
            /** Specifies the object type for length limit */
            public: enum TrimObjectType
            {
                TrimObjectTypePoint/** length limit point */,
                TrimObjectTypePlane/** plane end cap*/,
                TrimObjectTypeFace/** face end cap*/,
                TrimObjectTypeEdge/** edge limit cap */
            };

            private: PointFacePlaneSelectionBuilderImpl * m_pointfaceplaneselectionbuilder_impl;
            private: friend class  _PointFacePlaneSelectionBuilderBuilder;
            protected: PointFacePlaneSelectionBuilder();
            public: ~PointFacePlaneSelectionBuilder();
            /**Returns  the object type for length limit object 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricUtilities::PointFacePlaneSelectionBuilder::TrimObjectType TrimObject
            (
            );
            /**Sets  the object type for length limit object 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetTrimObject
            (
                NXOpen::GeometricUtilities::PointFacePlaneSelectionBuilder::TrimObjectType trimObject /** trimobject */ 
            );
            /**Returns  the select face as length limit object
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricUtilities::FaceSetData * SelectFace
            (
            );
            /**Returns  the select plane as length limit object
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Plane * SelectPlane
            (
            );
            /**Sets  the select plane as length limit object
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetSelectPlane
            (
                NXOpen::Plane * selectPlane /** selectplane */ 
            );
            /**Returns  the use plane cap blend 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: bool UsePlaneCapBlend
            (
            );
            /**Sets  the use plane cap blend 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetUsePlaneCapBlend
            (
                bool usePlaneCapBlend /** useplanecapblend */ 
            );
            /**Returns the user plane cap help point 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Point * PlaneHelpPoint
            (
            );
            /**Sets the user plane cap help point 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetPlaneHelpPoint
            (
                NXOpen::Point * helpPoint /** helppoint */ 
            );
            /**Sets the length limit object data OK flag 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetOk
            (
                bool isOk /** isok */ 
            );
            /**Returns the length limit object data OK flag 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: bool IsOk
            (
            );
            /**Returns the select edge as length limit object
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::ScCollector * SelectEdge
            (
            );
            /**Returns  the limit edge switch fin flag 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: bool LimitTopolSwitchFinFlag
            (
            );
            /**Sets  the limit edge switch fin flag 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetLimitTopolSwitchFinFlag
            (
                bool switchFlag /** switchflag */ 
            );
            /**Returns  the use face cap blend flag 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: bool UseFaceCapBlend
            (
            );
            /**Sets  the use face cap blend flag 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetUseFaceCapBlend
            (
                bool useFaceCapBlend /** usefacecapblend */ 
            );
            /**Returns the select point as length limit object
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricUtilities::LengthLimitPointBuilder * LengthLimitPoint
            (
            );
            /** Creates a FacePlaneSelectionBuilder @return LengthLimitPointBuilder object 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : features_modeling ("FEATURES MODELING"), solid_modeling ("SOLIDS MODELING") */
            public: NXOpen::GeometricUtilities::LengthLimitPointBuilder * CreateLengthLimitPointBuilder
            (
                NXOpen::Expression * mOnPathExp /** monpathexp */ ,
                NXOpen::GeometricUtilities::OnPathDimensionBuilder * mOnPath /** monpath */ ,
                bool mIsFlipped /** misflipped */ ,
                NXOpen::Point * mThruPoint /** mthrupoint */ 
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