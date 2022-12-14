#ifndef NXOpen_BLOCKSTYLER_CURVECOLLECTOR_HXX_INCLUDED
#define NXOpen_BLOCKSTYLER_CURVECOLLECTOR_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     BlockStyler_CurveCollector.ja
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
#include <NXOpen/BlockStyler_CurveCollector.hxx>
#include <NXOpen/BlockStyler_UIBlock.hxx>
#include <NXOpen/libnxopenuicpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace BlockStyler
    {
        class CurveCollector;
    }
    namespace BlockStyler
    {
        class UIBlock;
    }
    class TaggedObject;
    namespace BlockStyler
    {
        class _CurveCollectorBuilder;
        class CurveCollectorImpl;
        /** Represents a Curve Collector
         <br>  Created in NX8.5.0.  <br>  
        */
        class NXOPENUICPPEXPORT  CurveCollector : public NXOpen::BlockStyler::UIBlock
        {
            private: CurveCollectorImpl * m_curvecollector_impl;
            private: friend class  _CurveCollectorBuilder;
            protected: CurveCollector();
            public: ~CurveCollector();
            /**Returns  the AutomaticProgression
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: bool AutomaticProgression
            (
            );
            /**Sets  the AutomaticProgression
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetAutomaticProgression
            (
                bool automaticProgression /** automaticprogression */ 
            );
            /**Returns  the BalloonTooltipImage
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXString BalloonTooltipImage
            (
            );
            /**Sets  the BalloonTooltipImage
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetBalloonTooltipImage
            (
                const NXString & imageString /** image string */ 
            );
            /**Sets  the BalloonTooltipImage
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            void SetBalloonTooltipImage
            (
                const char * imageString /** image string */ 
            );
            /**Returns  the BalloonTooltipLayout as string
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXString BalloonTooltipLayoutAsString
            (
            );
            /**Sets  the BalloonTooltipLayout as string
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetBalloonTooltipLayoutAsString
            (
                const NXString & enumString /** enumstring */ 
            );
            /**Sets  the BalloonTooltipLayout as string
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            void SetBalloonTooltipLayoutAsString
            (
                const char * enumString /** enumstring */ 
            );
            /** Gets the BalloonTooltipLayout members  @return Value to get from the property. 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXString> GetBalloonTooltipLayoutMembers
            (
            );
            /**Returns  the BalloonTooltipText
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXString BalloonTooltipText
            (
            );
            /**Sets  the BalloonTooltipText
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetBalloonTooltipText
            (
                const NXString & balloonTooltipText /** balloon tooltip text */ 
            );
            /**Sets  the BalloonTooltipText
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            void SetBalloonTooltipText
            (
                const char * balloonTooltipText /** balloon tooltip text */ 
            );
            /**Returns  the Bitmap
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXString Bitmap
            (
            );
            /**Sets  the Bitmap
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetBitmap
            (
                const NXString & bitmapString /** bitmap string */ 
            );
            /**Sets  the Bitmap
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            void SetBitmap
            (
                const char * bitmapString /** bitmap string */ 
            );
            /**Returns  the BlendVirtualCurveOverlay
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: bool BlendVirtualCurveOverlay
            (
            );
            /**Sets  the BlendVirtualCurveOverlay
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetBlendVirtualCurveOverlay
            (
                bool blendCurve /** blendcurve */ 
            );
            /**Returns  the CurveRules
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: int CurveRules
            (
            );
            /**Sets  the CurveRules
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetCurveRules
            (
                int curveRules /** curverules */ 
            );
            /**Returns  the CreateInterpartLink
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: bool CreateInterpartLink
            (
            );
            /**Sets  the CreateInterpartLink
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetCreateInterpartLink
            (
                bool createLink /** createlink */ 
            );
            /**Returns  the Cue
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXString Cue
            (
            );
            /**Sets  the Cue
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetCue
            (
                const NXString & cue /** cue */ 
            );
            /**Sets  the Cue
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            void SetCue
            (
                const char * cue /** cue */ 
            );
            /**Returns  the InterpartSelection as string
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXString InterpartSelectionAsString
            (
            );
            /**Sets  the InterpartSelection as string
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetInterpartSelectionAsString
            (
                const NXString & enumString /** enumstring */ 
            );
            /**Sets  the InterpartSelection as string
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            void SetInterpartSelectionAsString
            (
                const char * enumString /** enumstring */ 
            );
            /** Gets the InterpartSelection members @return Value to get from the property
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXString> GetInterpartSelectionMembers
            (
            );
            /** Gets the SelectedObjects @return Value to get from the property
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXOpen::TaggedObject *> GetSelectedObjects
            (
            );
            /** Sets the SelectedObjects
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetSelectedObjects
            (
                const std::vector<NXOpen::TaggedObject *> & objectVector /**Value to set for the property*/
            );
            /**Returns  the SelectMode as string
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXString SelectModeAsString
            (
            );
            /**Sets  the SelectMode as string
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetSelectModeAsString
            (
                const NXString & enumString /** enumstring */ 
            );
            /**Sets  the SelectMode as string
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            void SetSelectModeAsString
            (
                const char * enumString /** enumstring */ 
            );
            /** Gets the SelectMode members @return Value to get from the property
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXString> GetSelectModeMembers
            (
            );
            /**Returns  the StepStatus as string
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXString StepStatusAsString
            (
            );
            /**Sets  the StepStatus as string
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetStepStatusAsString
            (
                const NXString & enumString /** enumstring */ 
            );
            /**Sets  the StepStatus as string
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            void SetStepStatusAsString
            (
                const char * enumString /** enumstring */ 
            );
            /** Gets the StepStatus members @return Value to get from the property
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXString> GetStepStatusMembers
            (
            );
            /**Returns  the ToolTip
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXString ToolTip
            (
            );
            /**Sets  the ToolTip
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetToolTip
            (
                const NXString & toolTip /** tooltip */ 
            );
            /**Sets  the ToolTip
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            void SetToolTip
            (
                const char * toolTip /** tooltip */ 
            );
            /**Returns  the DefaultCurveRules as string
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXString DefaultCurveRulesAsString
            (
            );
            /**Sets  the DefaultCurveRules as string
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetDefaultCurveRulesAsString
            (
                const NXString & enumString /** enumstring */ 
            );
            /**Sets  the DefaultCurveRules as string
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            void SetDefaultCurveRulesAsString
            (
                const char * enumString /** enumstring */ 
            );
            /** Gets the DefaultCurveRules members @return Value to get from the property
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXString> GetDefaultCurveRulesMembers
            (
            );
            /**Returns  the EntityType
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: int EntityType
            (
            );
            /**Sets  the EntityType
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetEntityType
            (
                int entityType /** entitytype */ 
            );
            /**Returns  the PopupMenuEnabled
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: bool PopupMenuEnabled
            (
            );
            /**Sets  the PopupMenuEnabled
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetPopupMenuEnabled
            (
                bool enabled /** enabled */ 
            );
            /**Returns  the AllowInferredCurveSelection
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: bool AllowInferredCurveSelection
            (
            );
            /**Sets  the AllowInferredCurveSelection
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetAllowInferredCurveSelection
            (
                bool allow /** allow */ 
            );
            /**Returns  the InferredCurveSelection
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: bool InferredCurveSelection
            (
            );
            /**Sets  the InferredCurveSelection
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetInferredCurveSelection
            (
                bool selectInferredCurve /** selectinferredcurve */ 
            );
            /**Returns  the LabelString
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXString LabelString
            (
            );
            /**Sets  the LabelString
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetLabelString
            (
                const NXString & labelString /** labelstring */ 
            );
            /**Sets  the LabelString
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            void SetLabelString
            (
                const char * labelString /** labelstring */ 
            );
            /**Returns  the AllowConvergentObject
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: bool AllowConvergentObject
            (
            );
            /**Sets  the AllowConvergentObject
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: void SetAllowConvergentObject
            (
                bool allowConvergentObject /** allowconvergentobject */ 
            );
            /**Returns  the MaximumScope
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: NXString MaximumScopeAsString
            (
            );
            /**Sets  the MaximumScope
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: void SetMaximumScopeAsString
            (
                const NXString & enumString /** enumstring */ 
            );
            /**Sets  the MaximumScope
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            void SetMaximumScopeAsString
            (
                const char * enumString /** enumstring */ 
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
