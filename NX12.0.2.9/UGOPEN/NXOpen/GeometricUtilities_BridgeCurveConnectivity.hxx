#ifndef NXOpen_GEOMETRICUTILITIES_BRIDGECURVECONNECTIVITY_HXX_INCLUDED
#define NXOpen_GEOMETRICUTILITIES_BRIDGECURVECONNECTIVITY_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     GeometricUtilities_BridgeCurveConnectivity.ja
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
#include <NXOpen/GeometricUtilities_Continuity.hxx>
#include <NXOpen/GeometricUtilities_OnPathDimensionBuilder.hxx>
#include <NXOpen/GeometricUtilities_IComponentBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/SelectObject.hxx>
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
        class BridgeCurveConnectivity;
    }
    class Direction;
    class Expression;
    namespace GeometricUtilities
    {
        class Continuity;
    }
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    namespace GeometricUtilities
    {
        class OnPathDimensionBuilder;
    }
    class SelectFace;
    namespace GeometricUtilities
    {
        class _BridgeCurveConnectivityBuilder;
        class BridgeCurveConnectivityImpl;
        /** Data offering connectivity controls for @link NXOpen::Features::BridgeCurveBuilderEx NXOpen::Features::BridgeCurveBuilderEx@endlink .
                Use @link NXOpen::GeometricUtilities::BridgeCurveConnectivity NXOpen::GeometricUtilities::BridgeCurveConnectivity@endlink  to define continuity level,
                position and tangency, curvature or flow at the end of a bridge curve. For more details see 
                the NX documentation for Bridge Curves.
            
         <br>  Created in NX8.5.0.  <br>  
        */
        class NXOPENCPP_GEOMETRICUTILITIESEXPORT  BridgeCurveConnectivity : public NXOpen::TaggedObject, public virtual NXOpen::GeometricUtilities::IComponentBuilder
        {
            /** Tangent constraint direction when end is attached to a section */
            public: enum CurveDirectionOptions
            {
                CurveDirectionOptionsTangent/** Tangent to section */,
                CurveDirectionOptionsPerpendicular/** Perpendicular to section using a reference face */
            };

            /** Tangent constraint direction when end is attached to a face */
            public: enum FaceDirectionOptions
            {
                FaceDirectionOptionsSectional/** Sectional direction */,
                FaceDirectionOptionsIsoU/** Along U iso-parameter */,
                FaceDirectionOptionsIsoV/** Along V iso-parameter */
            };

            private: BridgeCurveConnectivityImpl * m_bridgecurveconnectivity_impl;
            private: friend class  _BridgeCurveConnectivityBuilder;
            protected: BridgeCurveConnectivity();
            public: ~BridgeCurveConnectivity();
            /**Returns  the continuity level 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricUtilities::Continuity * Continuity
            (
            );
            /**Returns  the location on section 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricUtilities::OnPathDimensionBuilder * LocationOnSection
            (
            );
            /**Returns  the U coordinate percentage indicating location on the face where bridge curve is connected 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * UPercentage
            (
            );
            /**Returns  the V coordinate percentage indicating location on the face where bridge curve is connected 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * VPercentage
            (
            );
            /**Returns  the curve direction option 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricUtilities::BridgeCurveConnectivity::CurveDirectionOptions CurveDirectionOption
            (
            );
            /**Sets  the curve direction option 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR nx_freeform_1 ("basic freeform modeling") */
            public: void SetCurveDirectionOption
            (
                NXOpen::GeometricUtilities::BridgeCurveConnectivity::CurveDirectionOptions curveDirectionOption /** curvedirectionoption */ 
            );
            /**Returns  the perpendicular face 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectFace * PerpendicularFace
            (
            );
            /**Returns  the face direction option 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricUtilities::BridgeCurveConnectivity::FaceDirectionOptions FaceDirectionOption
            (
            );
            /**Sets  the face direction option 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR nx_freeform_1 ("basic freeform modeling") */
            public: void SetFaceDirectionOption
            (
                NXOpen::GeometricUtilities::BridgeCurveConnectivity::FaceDirectionOptions faceDirectionOption /** facedirectionoption */ 
            );
            /**Returns  the section angle. Positive U direction is used as reference to measure the angle in tangent plane. 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * SectionAngle
            (
            );
            /**Returns  the direction at point 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Direction * DirectionAtPoint
            (
            );
            /**Sets  the direction at point 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR nx_freeform_1 ("basic freeform modeling") */
            public: void SetDirectionAtPoint
            (
                NXOpen::Direction * direction /** direction */ 
            );
            /** Updates the data based on @link  BridgeCurveConnectivity::DirectionAtPoint   BridgeCurveConnectivity::DirectionAtPoint  @endlink and @link  BridgeCurveConnectivity::SetDirectionAtPoint   BridgeCurveConnectivity::SetDirectionAtPoint  @endlink  sense 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR nx_freeform_1 ("basic freeform modeling") */
            public: void UpdateOnDirectionAtPointReversal
            (
            );
            /**Returns  the flag indicating if tangent direction is to be reversed 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: bool CanReverseDirection
            (
            );
            /**Sets  the flag indicating if tangent direction is to be reversed 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR nx_freeform_1 ("basic freeform modeling") */
            public: void SetCanReverseDirection
            (
                bool reverseDirection /** reversedirection */ 
            );
            /** Edits parameter percentage of a representative point on face 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR nx_freeform_1 ("basic freeform modeling") */
            public: void EditUVPercentage
            (
                double uPercent /** upercent */ ,
                double vPercent /** vpercent */ 
            );
            /** Updates the data based on @link NXOpen::GeometricUtilities::BridgeCurveConnectivity::LocationOnSection  NXOpen::GeometricUtilities::BridgeCurveConnectivity::LocationOnSection @endlink 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR nx_freeform_1 ("basic freeform modeling") */
            public: void UpdateBasedOnLocationOnSection
            (
            );
            /** Validate whether the inputs to the component are sufficient for 
                        commit to be called.  If the component is not in a state to commit
                        then an exception is thrown.  For example, if the component requires
                        you to set some property, this method will throw an exception if
                        you haven't set it.  This method throws a not-yet-implemented
                        NXException for some components.
                     @return  Was self validation successful 
             <br>  Created in NX3.0.1.  <br>  
             <br> License requirements : None */
            public: virtual bool Validate
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
