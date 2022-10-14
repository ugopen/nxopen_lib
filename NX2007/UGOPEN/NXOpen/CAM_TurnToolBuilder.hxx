#ifndef NXOpen_CAM_TURNTOOLBUILDER_HXX_INCLUDED
#define NXOpen_CAM_TURNTOOLBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_TurnToolBuilder.ja
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
#include <NXOpen/CAM_TurningToolBuilder.hxx>
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
        class TurnToolBuilder;
    }
    namespace CAM
    {
        class InheritableDoubleBuilder;
    }
    namespace CAM
    {
        class TurningToolBuilder;
    }
    namespace CAM
    {
        class _TurnToolBuilderBuilder;
        class TurnToolBuilderImpl;
        /** Represents a Turn tool builder  <br> To create a new instance of this class, use @link NXOpen::CAM::NCGroupCollection::CreateTurnToolBuilder  NXOpen::CAM::NCGroupCollection::CreateTurnToolBuilder @endlink  <br> 
         <br>  Created in NX5.0.0.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  TurnToolBuilder : public NXOpen::CAM::TurningToolBuilder
        {
            /** the available insert shapes */
            public: enum InsertShapes
            {
                InsertShapesParallelogram85/**  Insert shape: Parallelogram 85 */,
                InsertShapesParallelogram82/**  Insert shape: Parallelogram 82 */,
                InsertShapesDiamond80/**  Insert shape: Diamond 80 */,
                InsertShapesDiamond100/**  Insert shape: Diamond 100 */,
                InsertShapesDiamond55/**  Insert shape: Diamond 55 */,
                InsertShapesDiamond75/**  Insert shape: Diamond 75 */,
                InsertShapesHexagon/**  Insert shape: Hexagon */,
                InsertShapesParallelogram55/**  Insert shape: Parallelogram 55 */,
                InsertShapesRectangle/**  Insert shape: Rectangle */,
                InsertShapesDiamond86/**  Insert shape: Diamond 86 */,
                InsertShapesOctagon/**  Insert shape: Octagon */,
                InsertShapesPentagon/**  Insert shape: Pentagon */,
                InsertShapesRound/**  Insert shape: Round */,
                InsertShapesSquare/**  Insert shape: Square */,
                InsertShapesTriangle/**  Insert shape: Triangle */,
                InsertShapesDiamond35/**  Insert shape: Diamond 35 */,
                InsertShapesTrigon/**  Insert shape: Trigon */,
                InsertShapesUser/**  Insert shape: User defined */,
                InsertShapesPrimeA/**  Insert shape: Prime A */,
                InsertShapesPrimeB/**  Insert shape: Prime B */
            };

            /** the available size options */
            public: enum SizeOptions
            {
                SizeOptionsCutEdgeLength/** Size option: Cut Edge length */,
                SizeOptionsInscribedCircle/** Size option: Inscribed_circle */,
                SizeOptionsInscribedCircleAnsi/** Size option: Inscribed_circle ANSI */
            };

            /** the available relief angle types */
            public: enum ReliefAngleTypes
            {
                ReliefAngleTypesA3/** Relief angle type: A (3) */,
                ReliefAngleTypesB5/** Relief angle type: B (5) */,
                ReliefAngleTypesC7/** Relief angle type: C (7) */,
                ReliefAngleTypesD15/** Relief angle type: D (15) */,
                ReliefAngleTypesE20/** Relief angle type: E (20) */,
                ReliefAngleTypesF25/** Relief angle type: F (25) */,
                ReliefAngleTypesG30/** Relief angle type: G (30) */,
                ReliefAngleTypesN0/** Relief angle type: N (0) */,
                ReliefAngleTypesP11/** Relief angle type: P (11) */,
                ReliefAngleTypesOOther/** Relief angle type: O (other) */
            };

            /** the available thickness types */
            public: enum ThicknessTypes
            {
                ThicknessTypesThickness01/** Thickness: 01 */,
                ThicknessTypesThicknessT1/** Thickness: T1 */,
                ThicknessTypesThickness02/** Thickness: 02 */,
                ThicknessTypesThicknessT2/** Thickness: T2 */,
                ThicknessTypesThickness03/** Thickness: 03 */,
                ThicknessTypesThicknessT3/** Thickness: T3 */,
                ThicknessTypesThickness04/** Thickness: 04 */,
                ThicknessTypesThickness05/** Thickness: 05 */,
                ThicknessTypesThickness06/** Thickness: 06 */,
                ThicknessTypesThickness07/** Thickness: 07 */,
                ThicknessTypesThickness09/** Thickness: 09 */,
                ThicknessTypesThickness11/** Thickness: 11 */,
                ThicknessTypesThickness12/** Thickness: 12 */,
                ThicknessTypesThicknessUserDefined/** Thickness: User defined */
            };

            /** the available turn holder style options */
            public: enum HolderStyles
            {
                HolderStylesA/** A-Style */,
                HolderStylesB/** B-Style */,
                HolderStylesC/** C-Style */,
                HolderStylesD/** D-Style */,
                HolderStylesE/** E-Style */,
                HolderStylesF/** F-Style */,
                HolderStylesG/** G-Style */,
                HolderStylesH/** H-Style */,
                HolderStylesI/** I-Style */,
                HolderStylesJ/** J-Style */,
                HolderStylesK/** K-Style */,
                HolderStylesL/** L-Style */,
                HolderStylesM/** M-Style */,
                HolderStylesN/** N-Style */,
                HolderStylesP/** P-Style */,
                HolderStylesQ/** Q-Style */,
                HolderStylesR/** R-Style */,
                HolderStylesS/** S-Style */,
                HolderStylesT/** T-Style */,
                HolderStylesU/** U-Style */,
                HolderStylesV/** V-Style */,
                HolderStylesUd/** User-Defined-Style */
            };

            /** the available turn holder hand options */
            public: enum HolderHands
            {
                HolderHandsLeft/** Hand: Left */,
                HolderHandsNeutral/** Hand: Neutral */,
                HolderHandsRight/** Hand: Right */
            };

            /** the available turn holder shank definition modes */
            public: enum HolderShankDefinitionModes
            {
                HolderShankDefinitionModesInsertAndHolder/** insert and holder mode */,
                HolderShankDefinitionModesCuttingEdgeAngle/** cutting edge angle mode */
            };

            private: TurnToolBuilderImpl * m_turntoolbuilder_impl;
            private: friend class  _TurnToolBuilderBuilder;
            protected: TurnToolBuilder();
            public: ~TurnToolBuilder();
            /**Returns  the insert shape 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::TurnToolBuilder::InsertShapes InsertShape
            (
            );
            /**Sets  the insert shape 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void SetInsertShape
            (
                NXOpen::CAM::TurnToolBuilder::InsertShapes insertShape /** insertshape */ 
            );
            /**Returns  the nose angle builder (inheritable double) 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::InheritableDoubleBuilder * NoseAngleBuilder
            (
            );
            /**Returns  the size option 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::TurnToolBuilder::SizeOptions SizeOption
            (
            );
            /**Sets  the size option 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void SetSizeOption
            (
                NXOpen::CAM::TurnToolBuilder::SizeOptions sizeOption /** sizeoption */ 
            );
            /**Returns  the size builder (inheritable double) 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::InheritableDoubleBuilder * SizeBuilder
            (
            );
            /**Returns  the button diameter builder (inheritable double) 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::InheritableDoubleBuilder * ButtonDiameterBuilder
            (
            );
            /**Returns  the holder control width (inheritable double) 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::InheritableDoubleBuilder * HolderControlWidthBuilder
            (
            );
            /**Returns  the holder control angle (inheritable double) 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::InheritableDoubleBuilder * HolderControlAngleBuilder
            (
            );
            /**Returns  the relief angle type 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::TurnToolBuilder::ReliefAngleTypes ReliefAngleType
            (
            );
            /**Sets  the relief angle type 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void SetReliefAngleType
            (
                NXOpen::CAM::TurnToolBuilder::ReliefAngleTypes reliefAngleType /** reliefangletype */ 
            );
            /**Returns  the relief angle (inheritable double) 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::InheritableDoubleBuilder * ReliefAngleBuilder
            (
            );
            /**Returns  the thickness type 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::TurnToolBuilder::ThicknessTypes ThicknessType
            (
            );
            /**Sets  the thickness type 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void SetThicknessType
            (
                NXOpen::CAM::TurnToolBuilder::ThicknessTypes thicknessType /** thicknesstype */ 
            );
            /**Returns  the turn holder style 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::TurnToolBuilder::HolderStyles HolderStyle
            (
            );
            /**Sets  the turn holder style 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void SetHolderStyle
            (
                NXOpen::CAM::TurnToolBuilder::HolderStyles holderStyle /** holderstyle */ 
            );
            /**Returns  the turn holder hand 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::TurnToolBuilder::HolderHands HolderHand
            (
            );
            /**Sets  the turn holder hand 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void SetHolderHand
            (
                NXOpen::CAM::TurnToolBuilder::HolderHands holderHand /** holderhand */ 
            );
            /**Returns  the holder shank definition mode 
             <br>  Created in NX11.0.2.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::TurnToolBuilder::HolderShankDefinitionModes HolderShankDefinitionMode
            (
            );
            /**Sets  the holder shank definition mode 
             <br>  Created in NX11.0.2.  <br>  
             <br> License requirements : None */
            public: void SetHolderShankDefinitionMode
            (
                NXOpen::CAM::TurnToolBuilder::HolderShankDefinitionModes holderShankDefinitionMode /** holdershankdefinitionmode */ 
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