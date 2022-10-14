#ifndef NXOpen_BLOCKSTYLER_SELECTOBJECT_HXX_INCLUDED
#define NXOpen_BLOCKSTYLER_SELECTOBJECT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     BlockStyler_SelectObject.ja
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
#include <NXOpen/BlockStyler_UIBlock.hxx>
#include <NXOpen/Selection.hxx>
#include <NXOpen/ugmath.hxx>
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
        class SelectObject;
    }
    namespace BlockStyler
    {
        class UIBlock;
    }
    class TaggedObject;
    namespace BlockStyler
    {
        class _SelectObjectBuilder;
        class SelectObjectImpl;
        /** Represents a Select Object block
         <br>  Created in NX8.5.0.  <br>  
        */
        class NXOPENUICPPEXPORT  SelectObject : public NXOpen::BlockStyler::UIBlock
        {
            /**Indicates the general filter type for selection. */
            public: enum FilterType
            {
                FilterTypeFeatures/** Filter to select all feature types */ = 1,
                FilterTypeFaces/** Filter to select all face types */,
                FilterTypeEdges/** Filter to select all edge types */ = 4,
                FilterTypeCurvesAndEdges/** Filter to select all curve and edge types */ = 8,
                FilterTypeComponents/** Filter to select all components */ = 16,
                FilterTypeSolidBodies/** Filter to select all solid bodies */ = 32,
                FilterTypeSheetBodies/** Filter to select all sheet bodies */ = 64
            };

            private: SelectObjectImpl * m_selectobject_impl;
            private: friend class  _SelectObjectBuilder;
            protected: SelectObject();
            public: ~SelectObject();
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
            /**Returns  the BlendVirtualCurveOverlay. If true, virtual curve is displayed during preselection.
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: bool BlendVirtualCurveOverlay
            (
            );
            /**Sets  the BlendVirtualCurveOverlay. If true, virtual curve is displayed during preselection.
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetBlendVirtualCurveOverlay
            (
                bool blendCurve /** blendcurve */ 
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
            /** Gets the LastDeselectedObjects @return Value to get from the property
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXOpen::TaggedObject *> GetLastDeselectedObjects
            (
            );
            /** Gets the LastSelectedObjects @return Value to get from the property
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXOpen::TaggedObject *> GetLastSelectedObjects
            (
            );
            /**Returns  the MaximumScope as string
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXString MaximumScopeAsString
            (
            );
            /**Sets  the MaximumScope as string
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetMaximumScopeAsString
            (
                const NXString & enumString /** enumstring */ 
            );
            /**Sets  the MaximumScope as string
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            void SetMaximumScopeAsString
            (
                const char * enumString /** enumstring */ 
            );
            /** Gets the MaximumScope members  @return Value to get from the property. 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXString> GetMaximumScopeMembers
            (
            );
            /**Returns  the PickPoint
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Point3d PickPoint
            (
            );
            /**Returns  the PointOverlay. If true,on the fly point creation is allowed.
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: bool PointOverlay
            (
            );
            /**Sets  the PointOverlay. If true,on the fly point creation is allowed.
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetPointOverlay
            (
                bool pointOverlay /** pointoverlay */ 
            );
            /** Sets the SelectionFilter
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetSelectionFilter
            (
                NXOpen::Selection::SelectionAction maskAction /** Mask action */,
                const std::vector<NXOpen::Selection::MaskTriple> & maskTriples /** Mask triples */
            );
            /**Returns  the SnapPointTypesEnabled
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: int SnapPointTypesEnabled
            (
            );
            /**Sets  the SnapPointTypesEnabled
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetSnapPointTypesEnabled
            (
                int typesEnabled /** typesenabled */ 
            );
            /**Returns  the SnapPointTypesOnByDefault
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: int SnapPointTypesOnByDefault
            (
            );
            /**Sets  the SnapPointTypesOnByDefault
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetSnapPointTypesOnByDefault
            (
                int typesByDefault /** typesbydefault */ 
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
            /**
                     @brief 
                    Adds the filters for select object block
                     

             
                    
                    This method takes the integer value of the desired enum values from 
                    @link NXOpen::BlockStyler::SelectObject::FilterType NXOpen::BlockStyler::SelectObject::FilterType@endlink .
                    
                     
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void AddFilter
            (
                int filterTypes /**Values from @link SelectObject::FilterType SelectObject::FilterType@endlink  for specifying filters */
            );
            /**
                     @brief 
                    Adds the filters for select object block 
                     

             
                    
                    This method takes the desired enumeration value from
                    @link NXOpen::BlockStyler::SelectObject::FilterType NXOpen::BlockStyler::SelectObject::FilterType@endlink .
                    
                    
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: void AddFilter
            (
                NXOpen::BlockStyler::SelectObject::FilterType filterTypes /**Values from @link SelectObject::FilterType SelectObject::FilterType@endlink  for specifying filters */
            );
            /**Adds the filter for select object block using type, subtype and solidBodyType 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void AddFilter
            (
                int type /** Object type. This can be one of the object types that are listed in 
                                                        uf_object_types.h. For example, for point, 
                                                        use UF_point_type in C++ and
                                                        NXOpen.UF.UFConstants.UF_point_type in .NET. */,
                int subType /** Object subtype. This can either be -1 (UF_all_subtype) for any subtype, or a
                                                        subtype of the selected type.
                                                        The subtypes are listed in uf_object_types.h. */,
                int solidBodyType /** Solid body subtype. This is only meaningful when the type is 
                                                         UF_solid_type.  In that case, this should be set to
                                                         one of the solid type constants listed in uf_ui_types.h 
                                                         under "Constants for selection solid_type". 
                                                         When this is used, subtype does not matter.
                                                         For example, to select any face, use UF_UI_SEL_FEATURE_ANY_FACE in C++ and 
                                                         NXOpen.UF.UFConstants.UF_UI_SEL_FEATURE_ANY_FACE in .NET */
            );
            /**Resets the filter for select object block 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void ResetFilter
            (
            );
            /**Returns  the update option for points created by the point overlay.
                     <br> 
                    Acceptable values are:
                    <ul>
                    <li> <b>Within Modeling</b> The smart object updates within Modeling in time stamp order. For example, if the smart object is referenced by Feature(i), the smart object will update after Feature (i-1) and right before Feature(i).</li>
                    <li> <b>After Modeling</b> The smart object updates after Modeling. Use for Drafting dimensions and other objects outside Modeling.</li>
                    <li> <b>After Parent Body</b> The smart object will always update after the last feature on the parent body.</li>
                    <li> <b>Mixed</b> The smart object will update after the last feature on the parent body when the parent body is in a different part; updates within Modeling in time-stamp order for parents in the same part.</li>
                    </ul>
                     <br> 
                    
             <br>  Created in NX8.5.1.  <br>  
             <br> License requirements : None */
            public: NXString SmartUpdateOptionAsString
            (
            );
            /**Sets  the update option for points created by the point overlay.
                     <br> 
                    Acceptable values are:
                    <ul>
                    <li> <b>Within Modeling</b> The smart object updates within Modeling in time stamp order. For example, if the smart object is referenced by Feature(i), the smart object will update after Feature (i-1) and right before Feature(i).</li>
                    <li> <b>After Modeling</b> The smart object updates after Modeling. Use for Drafting dimensions and other objects outside Modeling.</li>
                    <li> <b>After Parent Body</b> The smart object will always update after the last feature on the parent body.</li>
                    <li> <b>Mixed</b> The smart object will update after the last feature on the parent body when the parent body is in a different part; updates within Modeling in time-stamp order for parents in the same part.</li>
                    </ul>
                     <br> 
                    
             <br>  Created in NX8.5.1.  <br>  
             <br> License requirements : None */
            public: void SetSmartUpdateOptionAsString
            (
                const NXString & enumString /** enumstring */ 
            );
            /**Sets  the update option for points created by the point overlay.
                     <br> 
                    Acceptable values are:
                    <ul>
                    <li> <b>Within Modeling</b> The smart object updates within Modeling in time stamp order. For example, if the smart object is referenced by Feature(i), the smart object will update after Feature (i-1) and right before Feature(i).</li>
                    <li> <b>After Modeling</b> The smart object updates after Modeling. Use for Drafting dimensions and other objects outside Modeling.</li>
                    <li> <b>After Parent Body</b> The smart object will always update after the last feature on the parent body.</li>
                    <li> <b>Mixed</b> The smart object will update after the last feature on the parent body when the parent body is in a different part; updates within Modeling in time-stamp order for parents in the same part.</li>
                    </ul>
                     <br> 
                    
             <br>  Created in NX8.5.1.  <br>  
             <br> License requirements : None */
            void SetSmartUpdateOptionAsString
            (
                const char * enumString /** enumstring */ 
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
            /**Returns  the AllowConvergentObjectWithMixedGeometries
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: bool AllowConvergentObjectWithMixedGeometries
            (
            );
            /**Sets  the AllowConvergentObjectWithMixedGeometries
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: void SetAllowConvergentObjectWithMixedGeometries
            (
                bool allowConvergentObjectWithMixedGeometries /** allowconvergentobjectwithmixedgeometries */ 
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