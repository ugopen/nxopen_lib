#ifndef NXOpen_FEATURES_ADMMOVEFACEBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_ADMMOVEFACEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_AdmMoveFaceBuilder.ja
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
#include <NXOpen/Features_FaceRecognitionBuilder.hxx>
#include <NXOpen/GeometricUtilities_FaceChangeOverflowBehavior.hxx>
#include <NXOpen/GeometricUtilities_ModlMotion.hxx>
#include <NXOpen/GeometricUtilities_StepOptionBehavior.hxx>
#include <NXOpen/Features_AdmBaseBuilder.hxx>
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
        class AdmMoveFaceBuilder;
    }
    namespace Features
    {
        class AdmBaseBuilder;
    }
    namespace Features
    {
        class FaceRecognitionBuilder;
    }
    namespace GeometricUtilities
    {
        class FaceChangeOverflowBehavior;
    }
    namespace GeometricUtilities
    {
        class ModlMotion;
    }
    namespace GeometricUtilities
    {
        class StepOptionBehavior;
    }
    namespace Features
    {
        class _AdmMoveFaceBuilderBuilder;
        class AdmMoveFaceBuilderImpl;
        /**
            Represents a @link NXOpen::Features::AdmMoveFace NXOpen::Features::AdmMoveFace@endlink  builder
             <br> To create a new instance of this class, use @link NXOpen::Features::FeatureCollection::CreateAdmMoveFaceBuilder  NXOpen::Features::FeatureCollection::CreateAdmMoveFaceBuilder @endlink  <br> 
        Default values.
        <list type="table"> 
         
        <listheader><term> 
        Property</term>  <description> 
        Value</description> </listheader>
        <item><term> 
         
        FaceToMove.CoaxialEnabled </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        FaceToMove.CoplanarAxesEnabled </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        FaceToMove.CoplanarEnabled </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        FaceToMove.EqualDiameterEnabled </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        FaceToMove.OffsetEnabled </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        FaceToMove.ParallelEnabled </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        FaceToMove.PerpendicularEnabled </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        FaceToMove.SameOrbitEnabled </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        FaceToMove.SymmetricEnabled </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        FaceToMove.TangentEnabled </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        FaceToMove.ThicknessChainEnabled </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        FaceToMove.UseFaceBrowse </term> <description> 
         
        1 </description> </item> 

        <item><term> 
         
        HealOption </term> <description> 
         
        True </description> </item> 

        <item><term> 
         
        Motion.DeltaEnum </term> <description> 
         
        ReferenceWcsWorkPart </description> </item> 

        <item><term> 
         
        Motion.DeltaXc.Value </term> <description> 
         
        0.0 </description> </item> 

        <item><term> 
         
        Motion.DeltaYc.Value </term> <description> 
         
        0.0 </description> </item> 

        <item><term> 
         
        Motion.DeltaZc.Value </term> <description> 
         
        0.0 </description> </item> 

        <item><term> 
         
        Motion.Option </term> <description> 
         
        DistanceAngle </description> </item> 

        <item><term> 
         
        StepOption.StepOption </term> <description> 
         
        None </description> </item> 

        </list> 

         <br>  Created in NX6.0.0.  <br>  
        */
        class NXOPENCPP_FEATURESEXPORT  AdmMoveFaceBuilder : public NXOpen::Features::AdmBaseBuilder
        {
            /** Represents the move option. */
            public: enum MoveOptionType
            {
                MoveOptionTypeMoveAndAdapt/** Option equates to standard Move Face. */,
                MoveOptionTypeCutAndPaste/** Option equates to enhanced Move Face with Cut or Copy Face with Paste Face and Delete Face without heal. */
            };

            private: AdmMoveFaceBuilderImpl * m_admmovefacebuilder_impl;
            private: friend class  _AdmMoveFaceBuilderBuilder;
            protected: AdmMoveFaceBuilder();
            public: ~AdmMoveFaceBuilder();
            /**Returns  the face to move. Please refer @link NXOpen::Features::FaceRecognitionBuilder NXOpen::Features::FaceRecognitionBuilder@endlink  for details. 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::FaceRecognitionBuilder * FaceToMove
            (
            );
            /**Returns  the motion. The motion block provides a suite of linear and angular transform methods. Please refer @link NXOpen::GeometricUtilities::ModlMotion NXOpen::GeometricUtilities::ModlMotion@endlink  for details. 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricUtilities::ModlMotion * Motion
            (
            );
            /**Returns  the face change overflow behavior. Please refer @link NXOpen::GeometricUtilities::FaceChangeOverflowBehavior NXOpen::GeometricUtilities::FaceChangeOverflowBehavior@endlink  for details. 
             <br>  Created in NX6.0.2.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricUtilities::FaceChangeOverflowBehavior * FaceChangeOverflowBehavior
            (
            );
            /**Returns  the step option behavior. Please refer @link NXOpen::GeometricUtilities::StepOptionBehavior NXOpen::GeometricUtilities::StepOptionBehavior@endlink  for details. 
             <br>  Created in NX8.0.1.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricUtilities::StepOptionBehavior * StepOption
            (
            );
            /**Returns  the move option. 
             <br>  Created in NX8.0.1.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::AdmMoveFaceBuilder::MoveOptionType MoveOption
            (
            );
            /**Sets  the move option. 
             <br>  Created in NX8.0.1.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR cam_base ("CAM BASE") OR insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetMoveOption
            (
                NXOpen::Features::AdmMoveFaceBuilder::MoveOptionType moveOption /** moveoption */ 
            );
            /**Returns  the paste option. If true, the copied or cut faces will be pasted on the target body, else those faces will not be pasted.
             <br>  Created in NX8.0.1.  <br>  
             <br> License requirements : None */
            public: bool PasteOption
            (
            );
            /**Sets  the paste option. If true, the copied or cut faces will be pasted on the target body, else those faces will not be pasted.
             <br>  Created in NX8.0.1.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR cam_base ("CAM BASE") OR insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetPasteOption
            (
                bool pasteOption /** pasteoption */ 
            );
            /**Returns  the heal option. If true, Cut Face will be used to move the faces, and the wound will be healed automatically, else Copy Face will be 
                    used to move the faces and the original faces will be deleted without heal. 
             <br>  Created in NX8.0.1.  <br>  
             <br> License requirements : None */
            public: bool HealOption
            (
            );
            /**Sets  the heal option. If true, Cut Face will be used to move the faces, and the wound will be healed automatically, else Copy Face will be 
                    used to move the faces and the original faces will be deleted without heal. 
             <br>  Created in NX8.0.1.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR cam_base ("CAM BASE") OR insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetHealOption
            (
                bool healOption /** healoption */ 
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
