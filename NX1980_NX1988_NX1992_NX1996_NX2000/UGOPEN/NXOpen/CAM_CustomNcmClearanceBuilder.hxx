#ifndef NXOpen_CAM_CUSTOMNCMCLEARANCEBUILDER_HXX_INCLUDED
#define NXOpen_CAM_CUSTOMNCMCLEARANCEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_CustomNcmClearanceBuilder.ja
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
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_cam_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace CAM
    {
        class CustomNcmClearanceBuilder;
    }
    namespace CAM
    {
        class ExpressionDouble;
    }
    class NXObject;
    class Plane;
    namespace CAM
    {
        class _CustomNcmClearanceBuilderBuilder;
        class CustomNcmClearanceBuilderImpl;

        /// \cond NX_NO_DOC 
        /**  Represents Custom Non-Cutting Move Clearance Builder  
         <br>  Created in NX1980.0.0.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  CustomNcmClearanceBuilder : public NXOpen::TaggedObject
        {
            /** the types available for clearance */

            /// \cond NX_NO_DOC 
            public: enum ClearanceTypes
            {
                ClearanceTypesUseCommon/** inherited from common or parent */,
                ClearanceTypesNone/** clearance turned off */,
                ClearanceTypesAutomatic/** automatic with distance for planar operations */,
                ClearanceTypesPlane/** clearance plane */,
                ClearanceTypesPoint/** clearance point */,
                ClearanceTypesCylinder/** clearance cylinder */,
                ClearanceTypesSphere/** clearance sphere */,
                ClearanceTypesBoundingBox/** clearance box */,
                ClearanceTypesBoundingCylinder/** clearance bounding cylinder */,
                ClearanceTypesBody/** clearance body */
            };


            /// \endcond 
            private: CustomNcmClearanceBuilderImpl * m_customncmclearancebuilder_impl;
            private: friend class  _CustomNcmClearanceBuilderBuilder;
            protected: CustomNcmClearanceBuilder();
            public: ~CustomNcmClearanceBuilder();

            /// \cond NX_NO_DOC 
            /**Returns  the clearance type 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::CustomNcmClearanceBuilder::ClearanceTypes ClearanceType
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the clearance type 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetClearanceType
            (
                NXOpen::CAM::CustomNcmClearanceBuilder::ClearanceTypes clearanceType /** clearancetype */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the safe distance for automatic clearance 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: double SafeDistance
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the safe distance for automatic clearance 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetSafeDistance
            (
                double newValue /** newvalue */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the safe distance builder 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::ExpressionDouble * SafeDistanceBuilder
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the clearance plane,plane entity type covers Xform and Plane 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Plane * PlaneXform
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the clearance plane,plane entity type covers Xform and Plane 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetPlaneXform
            (
                NXOpen::Plane * plane /** entity type can be XFORM or PLANE */
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the point for clearance types point, cylinder and sphere 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::NXObject * Point
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the point for clearance types point, cylinder and sphere 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetPoint
            (
                NXOpen::NXObject * point /** point */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the clearance cylinder axis 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::NXObject * Axis
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the clearance cylinder axis 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetAxis
            (
                NXOpen::NXObject * axis /** axis */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the clearance cylinder and sphere radius 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: double Radius
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the clearance cylinder and sphere radius 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetRadius
            (
                double radius /** radius */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the distance for bounding box clearance 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: double BoundingBoxClearance
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the distance for bounding box clearance 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetBoundingBoxClearance
            (
                double boundingBoxClearance /** boundingboxclearance */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the clearance body 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::NXObject * Body
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the clearance body 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetBody
            (
                NXOpen::NXObject * body /** body */ 
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
