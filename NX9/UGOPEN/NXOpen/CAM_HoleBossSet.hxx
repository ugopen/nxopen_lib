#ifndef NXOpen_CAM_HOLEBOSSSET_HXX_INCLUDED
#define NXOpen_CAM_HOLEBOSSSET_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_HoleBossSet.ja
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
#include <NXOpen/CAM_HoleBossSet.hxx>
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
        class HoleBossSet;
    }
    namespace CAM
    {
        class CAMAttribute;
    }
    namespace CAM
    {
        class CAMFeature;
    }
    namespace CAM
    {
        namespace FBM
        {
            class Feature;
        }
    }
    namespace CAM
    {
        class InferredDouble;
    }
    class NXObject;
    namespace CAM
    {
        class _HoleBossSetBuilder;
        class HoleBossSetImpl;
        /** Represents a Cut Area Geometry builder  <br> To create a new instance of this class, use @link CAM::HoleBossGeom::CreateHoleBossBuilder  CAM::HoleBossGeom::CreateHoleBossBuilder @endlink  <br> 
         <br>  Created in NX7.5.0.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  HoleBossSet : public TaggedObject
        {
            /** the depth limit types 
             <br>  Created in NX8.0.0.  <br>  
            */
            public: enum DepthLimitTypes
            {
                DepthLimitTypesThrough/** Depth Limit: Through */,
                DepthLimitTypesBlind/** Depth Limit: Blind */
            };

            private: HoleBossSetImpl * m_holebossset_impl;
            private: friend class  _HoleBossSetBuilder;
            protected: HoleBossSet();
            public: ~HoleBossSet();
            /**Returns  the Depth 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: double Depth
            (
            );
            /**Sets  the Depth 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetDepth
            (
                double depthValue /** the Depth */
            );
            /**Returns  the Tool Axis 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::NXObject * ToolAxis
            (
            );
            /**Sets  the Tool Axis 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetToolAxis
            (
                NXOpen::NXObject * toolAxis /** the tool axis */
            );
            /**Returns  the Diameter 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: double Diameter
            (
            );
            /**Sets  the Diameter 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetDiameter
            (
                double holeBossValue /** the Diameter */
            );
            /**Returns  the Major Diameter 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: double MajorDiameter
            (
            );
            /**Sets  the Major Diameter 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetMajorDiameter
            (
                double holeBossValue /** the Major Diameter */
            );
            /**Returns  the Minor Diameter 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: double MinorDiameter
            (
            );
            /**Sets  the Minor Diameter 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetMinorDiameter
            (
                double holeBossValue /** the Minor Diameter */
            );
            /**Returns  the Length 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: double Length
            (
            );
            /**Sets  the Length 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetLength
            (
                double holeBossValue /** the Length */
            );
            /**Returns  the Size 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXString Size
            (
            );
            /**Sets  the Size 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetSize
            (
                const NXString & holeBossValue /** the Size */
            );
            /**Sets  the Size 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            void SetSize
            (
                const char * holeBossValue /** the Size */
            );
            /**Returns  the depth builder 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InferredDouble * DepthBuilder
            (
            );
            /**Returns  the diameter builder 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InferredDouble * DiameterBuilder
            (
            );
            /**Returns  the length builder 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InferredDouble * LengthBuilder
            (
            );
            /** Save the infer logic information of the input entity, such as the orientation, pitch, diameter and height etc. into the feature
             <br>  Created in NX7.5.2.  <br>  
             <br> License requirements : None */
            public: void InferLogic
            (
                NXOpen::NXObject * entity /** the geometry*/
            );
            /**Returns  the Depth Limit types 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::HoleBossSet::DepthLimitTypes DepthLimit
            (
            );
            /**Sets  the Depth Limit types 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetDepthLimit
            (
                NXOpen::CAM::HoleBossSet::DepthLimitTypes type /** the Depth Limit type*/
            );
            /** Reverses the direction of the feature
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: void ReverseDirection
            (
            );
            /**Returns  the start diameter
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::CAMAttribute * StartDiameter
            (
            );
            /** Returns the in process feature  @return  
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::FBM::Feature * GetFeature
            (
            );
            /** Returns the machining feature  @return  
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::CAMFeature * GetMachiningFeature
            (
            );
            /**Returns  the tip angle
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::CAMAttribute * TipAngle
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