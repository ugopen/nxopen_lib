#ifndef NXOpen_FEATURES_INTERCEPTIONBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_INTERCEPTIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_InterceptionBuilder.ja
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
#include <NXOpen/Features_InterceptionCameraListItemBuilder.hxx>
#include <NXOpen/Features_InterceptionMirrorListItemBuilder.hxx>
#include <NXOpen/Features_FeatureBuilder.hxx>
#include <NXOpen/ObjectList.hxx>
#include <NXOpen/ScCollector.hxx>
#include <NXOpen/SelectObject.hxx>
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
        class InterceptionBuilder;
    }
    class Direction;
    namespace Features
    {
        class FeatureBuilder;
    }
    namespace Features
    {
        class InterceptionCameraListItemBuilder;
    }
    namespace Features
    {
        class InterceptionCameraListItemBuilderList;
    }
    namespace Features
    {
        class InterceptionMirrorListItemBuilder;
    }
    namespace Features
    {
        class InterceptionMirrorListItemBuilderList;
    }
    namespace Features
    {
        class SelectFeature;
    }
    namespace Features
    {
        class SelectFeatureList;
    }
    class NXColor;
    class Point;
    class ScCollector;
    namespace Features
    {
        class _InterceptionBuilderBuilder;
        class InterceptionBuilderImpl;

        /// \cond NX_NO_DOC 
        /**
            Represents a @link Features::Interception Features::Interception@endlink  builder
             <br> To create a new instance of this class, use @link NXOpen::Features::AVDACollection::CreateInterceptionBuilder  NXOpen::Features::AVDACollection::CreateInterceptionBuilder @endlink  <br> 
        Default values.
        <list type="table"> 
         
        <listheader><term> 
        Property</term>  <description> 
        Value</description> </listheader>
        <item><term> 
         
        AllowDirectVisibility </term> <description> 
         
        1 </description> </item> 

        <item><term> 
         
        BlindspotColor </term> <description> 
         
        216 </description> </item> 

        <item><term> 
         
        DistanceThreshold </term> <description> 
         
        5.00 (millimeters part), 0.2 (inches part) </description> </item> 

        <item><term> 
         
        DistanceTolerance </term> <description> 
         
        0.025 (millimeters part), 0.001 (inches part) </description> </item> 

        <item><term> 
         
        InterceptionStandard </term> <description> 
         
        Iso5006 </description> </item> 

        <item><term> 
         
        InterceptionType </term> <description> 
         
        Ground </description> </item> 

        <item><term> 
         
        UseViewDirection </term> <description> 
         
        1 </description> </item> 

        <item><term> 
         
        ViewDirectionMethod </term> <description> 
         
        Forward </description> </item> 

        </list> 

         <br>  Created in NX1953.0.0.  <br>  
        */
        class NXOPENCPP_FEATURESEXPORT  InterceptionBuilder : public NXOpen::Features::FeatureBuilder
        {
            /**
                    Used to indicate the type of interception
                    */
            public: enum InterceptionTypes
            {
                InterceptionTypesGround/** ground */ ,
                InterceptionTypesWall/** wall */ 
            };

            /**
                    Used to indicate the Interception standard
                    */
            public: enum InterceptionStandards
            {
                InterceptionStandardsIso5006/** iso5006 */ ,
                InterceptionStandardsUserDefined/** user defined */ 
            };

            /**
                    Used to indicate the View Direction Method
                    */
            public: enum ViewDirectionMethods
            {
                ViewDirectionMethodsForward/** forward */ ,
                ViewDirectionMethodsTargetPoint/** target point */ ,
                ViewDirectionMethodsUserdefinedDirection/** userdefined direction */ 
            };

            private: InterceptionBuilderImpl * m_interceptionbuilder_impl;
            private: friend class  _InterceptionBuilderBuilder;
            protected: InterceptionBuilder();
            public: ~InterceptionBuilder();

            /// \cond NX_NO_DOC 
            /**Returns  the interception type 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::InterceptionBuilder::InterceptionTypes InterceptionType
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the interception type 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : vehicle_des_val (" Vehicle Design and Validation") */
            public: void SetInterceptionType
            (
                NXOpen::Features::InterceptionBuilder::InterceptionTypes interceptionType /** interceptiontype */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the interception standard 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::InterceptionBuilder::InterceptionStandards InterceptionStandard
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the interception standard 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : vehicle_des_val (" Vehicle Design and Validation") */
            public: void SetInterceptionStandard
            (
                NXOpen::Features::InterceptionBuilder::InterceptionStandards interceptionStandard /** interceptionstandard */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the direct vision 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::SelectFeature * DirectVision
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the allow direct visibility 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: bool AllowDirectVisibility
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the allow direct visibility 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : vehicle_des_val (" Vehicle Design and Validation") */
            public: void SetAllowDirectVisibility
            (
                bool allowDirectVisibility /** allowdirectvisibility */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the use view direction 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: bool UseViewDirection
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the use view direction 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : vehicle_des_val (" Vehicle Design and Validation") */
            public: void SetUseViewDirection
            (
                bool useViewDirection /** useviewdirection */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the view direction method 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::InterceptionBuilder::ViewDirectionMethods ViewDirectionMethod
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the view direction method 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : vehicle_des_val (" Vehicle Design and Validation") */
            public: void SetViewDirectionMethod
            (
                NXOpen::Features::InterceptionBuilder::ViewDirectionMethods viewDirectionMethod /** viewdirectionmethod */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the view direction vector 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Direction * ViewDirectionVector
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the view direction vector 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : vehicle_des_val (" Vehicle Design and Validation") */
            public: void SetViewDirectionVector
            (
                NXOpen::Direction * viewDirectionVector /** viewdirectionvector */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the target point 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Point * TargetPoint
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the target point 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : vehicle_des_val (" Vehicle Design and Validation") */
            public: void SetTargetPoint
            (
                NXOpen::Point * targetPoint /** targetpoint */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**This button pops up dialog to set display properties to direct vision output data 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : vehicle_des_val (" Vehicle Design and Validation") */
            public: void ButtonDisplayProperties
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Creates a @link NXOpen::Features::InterceptionMirrorListItemBuilder NXOpen::Features::InterceptionMirrorListItemBuilder@endlink  
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : vehicle_des_val (" Vehicle Design and Validation") */
            public: NXOpen::Features::InterceptionMirrorListItemBuilder * CreateInterceptionMirrorListItemBuilder
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the list of @link NXOpen::Features::InterceptionMirrorListItemBuilder NXOpen::Features::InterceptionMirrorListItemBuilder@endlink  defining the mirror parameters. 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::InterceptionMirrorListItemBuilderList * MirrorList
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Creates a @link NXOpen::Features::InterceptionCameraListItemBuilder NXOpen::Features::InterceptionCameraListItemBuilder@endlink  
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : vehicle_des_val (" Vehicle Design and Validation") */
            public: NXOpen::Features::InterceptionCameraListItemBuilder * CreateInterceptionCameraListItemBuilder
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the camera list 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::InterceptionCameraListItemBuilderList * CameraList
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the grid target 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::ScCollector * GridTarget
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the obstruction 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::SelectFeatureList * Obstructions
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the blindspot color 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::NXColor * BlindspotColor
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the blindspot color 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : vehicle_des_val (" Vehicle Design and Validation") */
            public: void SetBlindspotColor
            (
                NXOpen::NXColor * blindspotColor /** blindspotcolor */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the distance tolerance 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: double DistanceTolerance
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the distance tolerance 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : vehicle_des_val (" Vehicle Design and Validation") */
            public: void SetDistanceTolerance
            (
                double distanceTolerance /** distancetolerance */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the distance threshold 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: double DistanceThreshold
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the distance threshold 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : vehicle_des_val (" Vehicle Design and Validation") */
            public: void SetDistanceThreshold
            (
                double distanceThreshold /** distancethreshold */ 
            );

            /// \endcond 
        };

        /// \endcond 
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