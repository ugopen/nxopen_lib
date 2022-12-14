#ifndef NXOpen_ANNOTATIONS_TARGETPOINTBUILDER_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_TARGETPOINTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_TargetPointBuilder.ja
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
#include <NXOpen/libnxopencpp_annotations_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Annotations
    {
        class TargetPointBuilder;
    }
    class Builder;
    class NXColor;
    class SelectNXObject;
    namespace Annotations
    {
        class _TargetPointBuilderBuilder;
        class TargetPointBuilderImpl;
        /** Represents a @link NXOpen::Annotations::TargetPoint NXOpen::Annotations::TargetPoint@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::Annotations::TargetPointCollection::CreateTargetPointBuilder  NXOpen::Annotations::TargetPointCollection::CreateTargetPointBuilder @endlink  <br> 
        Default values.
        <list type="table"> 
         
        <listheader><term> 
        Property</term>  <description> 
        Value</description> </listheader>
        <item><term> 
         
        Angle </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        Height </term> <description> 
         
        5 </description> </item> 

        <item><term> 
         
        Width </term> <description> 
         
        Thin </description> </item> 

        </list> 

         <br>  Created in NX6.0.0.  <br>  
        */
        class NXOPENCPP_ANNOTATIONSEXPORT  TargetPointBuilder : public NXOpen::Builder
        {
            /** the types of target point thickness */
            public: enum Thickness
            {
                ThicknessThin/** Thin */,
                ThicknessNormal/** Normal */,
                ThicknessThick/** Thick  */,
                ThicknessOne/** Width One */ = 6,
                ThicknessTwo/** Width Two */,
                ThicknessThree/** Width Three */,
                ThicknessFour/** Width Four */,
                ThicknessFive/** Width Five */,
                ThicknessSix/** Width Six */,
                ThicknessSeven/** Width Seven */,
                ThicknessEight/** Width Eight */,
                ThicknessNine/** Width Nine */
            };

            private: TargetPointBuilderImpl * m_targetpointbuilder_impl;
            private: friend class  _TargetPointBuilderBuilder;
            protected: TargetPointBuilder();
            public: ~TargetPointBuilder();
            /**Returns  the location 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectNXObject * Location
            (
            );
            /**Returns  the inherit 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectNXObject * Inherit
            (
            );
            /**Returns  the height 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: double Height
            (
            );
            /**Sets  the height 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetHeight
            (
                double height /** height */ 
            );
            /**Returns  the angle 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: double Angle
            (
            );
            /**Sets  the angle 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetAngle
            (
                double angle /** angle */ 
            );
            /**Returns  the color 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::NXColor * Color
            (
            );
            /**Sets  the color 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetColor
            (
                NXOpen::NXColor * color /** color */ 
            );
            /**Returns  the width 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::TargetPointBuilder::Thickness Width
            (
            );
            /**Sets  the width 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetWidth
            (
                NXOpen::Annotations::TargetPointBuilder::Thickness width /** width */ 
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
