#ifndef NXOpen_TOOLING_LAYOUTREPOSITIONBUILDER_HXX_INCLUDED
#define NXOpen_TOOLING_LAYOUTREPOSITIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Tooling_LayoutRepositionBuilder.ja
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
#include <NXOpen/Builder.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/libnxopencpp_tooling_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Tooling
    {
        class LayoutRepositionBuilder;
    }
    class Builder;
    class Expression;
    class NXObject;
    class Point;
    class SelectNXObjectList;
    namespace Tooling
    {
        class _LayoutRepositionBuilderBuilder;
        class LayoutRepositionBuilderImpl;
        /** Represents a Tooling::LayoutRepositionBuilder builder  <br> To create a new instance of this class, use @link NXOpen::Tooling::MWLayoutCollection::CreateLayoutRepositionBuilder  NXOpen::Tooling::MWLayoutCollection::CreateLayoutRepositionBuilder @endlink  <br> 
        Default values.
        <list type="table"> 
         
        <listheader><term> 
        Property</term>  <description> 
        Value</description> </listheader>
        <item><term> 
         
        DimX.Value </term> <description> 
         
        0 (millimeters part), 0 (inches part) </description> </item> 

        <item><term> 
         
        DimY.Value </term> <description> 
         
        0 (millimeters part), 0 (inches part) </description> </item> 

        <item><term> 
         
        RepositionType </term> <description> 
         
        Move </description> </item> 

        <item><term> 
         
        RotateAngle.Value </term> <description> 
         
        180 </description> </item> 

        </list> 

         <br>  Created in NX6.0.0.  <br>  
        */
        class NXOPENCPP_TOOLINGEXPORT  LayoutRepositionBuilder : public NXOpen::Builder
        {
            /** Represents the type of layout transform. */
            public: enum Method
            {
                MethodRotate/** Rotate method */,
                MethodTransform/** Transform method */,
                MethodPointToPoint/** Point to Point method */
            };

            /** Represents the method of layout transform. */
            public: enum Type
            {
                TypeMove/** Move type */,
                TypeCopy/** Copy type */
            };

            private: LayoutRepositionBuilderImpl * m_layoutrepositionbuilder_impl;
            private: friend class  _LayoutRepositionBuilderBuilder;
            protected: LayoutRepositionBuilder();
            public: ~LayoutRepositionBuilder();
            /**Returns  the select instance 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectNXObjectList * SelectInstance
            (
            );
            /**Returns  the reposition method 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Tooling::LayoutRepositionBuilder::Method RepositionMethod
            (
            );
            /**Sets  the reposition method 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: void SetRepositionMethod
            (
                NXOpen::Tooling::LayoutRepositionBuilder::Method enumRepositionmethod /** enumrepositionmethod */ 
            );
            /**Returns  the reposition type 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Tooling::LayoutRepositionBuilder::Type RepositionType
            (
            );
            /**Sets  the reposition type 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: void SetRepositionType
            (
                NXOpen::Tooling::LayoutRepositionBuilder::Type enumRepositiontype /** enumrepositiontype */ 
            );
            /**Returns  the rotate point 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Point * RotatePoint
            (
            );
            /**Sets  the rotate point 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: void SetRotatePoint
            (
                NXOpen::Point * rotatePoint /** rotatepoint */ 
            );
            /**Returns  the rotate angle 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * RotateAngle
            (
            );
            /**Returns  the distance dimension in X-axis 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * DimX
            (
            );
            /**Returns  the distance dimension in Y-axis 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * DimY
            (
            );
            /**Returns  the transform start point 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Point * PointFrom
            (
            );
            /**Sets  the transform start point 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: void SetPointFrom
            (
                NXOpen::Point * pointFrom /** pointfrom */ 
            );
            /**Returns  the transform end point 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Point * PointTo
            (
            );
            /**Sets  the transform end point 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: void SetPointTo
            (
                NXOpen::Point * pointTo /** pointto */ 
            );
            /** Generates a new cavity according to the given cavity occ
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void AddCavity
            (
                NXOpen::NXObject * selectedCavity /** selectedcavity */ 
            );
            /** Transforms cavity with x y distance
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void RepositionMove
            (
                int copyOption /** copyoption */ 
            );
            /** Rotates cavity
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void RepositionRotate
            (
                int type /** type */ ,
                int copyOption /** copyoption */ 
            );
            /** Transforms cavity  from point to point
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void RepositionPointToPoint
            (
                int copyOption /** copyoption */ 
            );
            /** Reposition to original place
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void RepositionToOriginal
            (
            );
            /** Removes components from the current assembly
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void RemoveOperation
            (
            );
            /** Adds a cavity to move cavities
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void AddACavityToMoveCavities
            (
                NXOpen::NXObject * cavityComponent /** cavitycomponent */ 
            );
            /** Clears all cavities in move cavities
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void ClearMoveCavities
            (
            );
            /** Adds a cavity to copy cavities
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void AddACavityToCopyCavities
            (
                NXOpen::NXObject * cavityComponent /** cavitycomponent */ 
            );
            /** Clears all cavities in copy cavities
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void ClearCopyCavities
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
