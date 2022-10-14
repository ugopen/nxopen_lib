#ifndef NXOpen_PREFERENCES_SESSIONMODELING_HXX_INCLUDED
#define NXOpen_PREFERENCES_SESSIONMODELING_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Preferences_SessionModeling.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Preferences
    {
        class SessionModeling;
    }
    namespace Preferences
    {
        class SessionPreferences;
    }
    namespace Preferences
    {
        /** Represents the set of Modeling preferences applicable to entire session <br> To obtain an instance of this class, refer to @link SessionPreferences SessionPreferences@endlink  <br> */
        class NXOPENCPPEXPORT SessionModeling
        {
            /** Describes whether the display of New Face properties inherits from body or part default */
            public: enum NewFacePropertiesInheritance
            {
                NewFacePropertiesInheritanceBody/** Indicates that display of new face properties inherits from body  */,
                NewFacePropertiesInheritancePartDefault/** Indicates that display of new face properties inherits from part default */
            };

            /** Describes whether the display of Boolean Face properties inherits from target body or tool body */
            public: enum BooleanFacePropertiesInheritance
            {
                BooleanFacePropertiesInheritanceTargetBody/** Indicates that display of boolean face properties inherits from target body */,
                BooleanFacePropertiesInheritanceToolBody/** Indicates that display of boolean face properties inherits from tool body */
            };

            /** Describes whether the Dynamic Update type is not selected or selected as incremental or continuous */
            public: enum DynamicUpdateType
            {
                DynamicUpdateTypeNone/** Indicates that Dynamic Update type is not selected */,
                DynamicUpdateTypeIncremental/** Indicates that Dynamic Update type is incremental*/,
                DynamicUpdateTypeContinuous/** Indicates that Dynamic Update type is continuous */
            };

            /** Describes whether the Immediate Children type is selected for first level or for all */
            public: enum ImmediateChildrenType
            {
                ImmediateChildrenTypeFirstLevel/** Indicates that Immediate Children type is at first level */,
                ImmediateChildrenTypeAll/** Indicates that Immediate Children type is at all level  */
            };

            /** Describes whether the body type is solid or sheet */
            public: enum BodyTypeOption
            {
                BodyTypeOptionSolid/** Indicates Body Type is solid  */,
                BodyTypeOptionSheet/** Indicates Body Type is solid */
            };

            /** Describes whether the Free Form Construction Result is plane or B Surface  */
            public: enum FreeFormConstructionResultType
            {
                FreeFormConstructionResultTypePlane/** Indicates the construction result option is plane  */,
                FreeFormConstructionResultTypeBSurface/** Indicates the construction result option is B Surface  */
            };

            /** Describes whether the Curve Fit Method type is selected as cubic or quintic or advanced */
            public: enum CurveFitMethodType
            {
                CurveFitMethodTypeCubic/** Indicates the Curve Fit Method type is cubic */,
                CurveFitMethodTypeQuintic/** Indicates the Curve Fit Method type is quintic */,
                CurveFitMethodTypeAdvanced/** Indicates the Curve Fit Method type is advanced */
            };

            /** Freeform preview resolutions */
            public: enum PreviewResolutionType
            {
                PreviewResolutionTypeNone/** */,
                PreviewResolutionTypeCoarse/** */,
                PreviewResolutionTypeStandard/** */,
                PreviewResolutionTypeFine/** */,
                PreviewResolutionTypeExtraFine/** */,
                PreviewResolutionTypeSuperFine/** */,
                PreviewResolutionTypeUltraFine/** */
            };

            private: NXOpen::Preferences::SessionPreferences* m_owner;
            public: explicit SessionModeling(NXOpen::Preferences::SessionPreferences *owner): m_owner(owner)
            {
            }
            public: tag_t Tag() const;
            /**Returns  the boolean face properties inheritance. Specifies whether the boolean face properties inherit from target body or tool body  <br> License requirements : None */
            public: NXOpen::Preferences::SessionModeling::BooleanFacePropertiesInheritance BooleanFaceProperties
            (
            );
            /** <b>Deprecated</b>:<br>
            &nbsp;&nbsp;&nbsp;Use @link BooleanFaceProperties() BooleanFaceProperties@endlink instead.
            @deprecated
            */
            public: NXOpen::Preferences::SessionModeling::BooleanFacePropertiesInheritance GetBooleanFaceProperties
            (
            ) { return this->BooleanFaceProperties(); }
            /**Sets  the boolean face properties inheritance. Specifies whether the boolean face properties inherit from target body or tool body  <br> License requirements : None */
            public: void SetBooleanFaceProperties
            (
                NXOpen::Preferences::SessionModeling::BooleanFacePropertiesInheritance boolean_face_properties /**  */
            );
            /**Returns  the new face properties inheritance. Specifies whether new face properties inherits from body or part default  <br> License requirements : None */
            public: NXOpen::Preferences::SessionModeling::NewFacePropertiesInheritance NewFaceProperties
            (
            );
            /** <b>Deprecated</b>:<br>
            &nbsp;&nbsp;&nbsp;Use @link NewFaceProperties() NewFaceProperties@endlink instead.
            @deprecated
            */
            public: NXOpen::Preferences::SessionModeling::NewFacePropertiesInheritance GetNewFaceProperties
            (
            ) { return this->NewFaceProperties(); }
            /**Sets  the new face properties inheritance. Specifies whether new face properties inherits from body or part default  <br> License requirements : None */
            public: void SetNewFaceProperties
            (
                NXOpen::Preferences::SessionModeling::NewFacePropertiesInheritance new_face_properties /**  */
            );
            /**Returns  the dynamic update. Specifies that the system dynamically displays in real time with each 
                updation of parent curves, splines, bridge curves, lines or arcs  <br> License requirements : None */
            public: NXOpen::Preferences::SessionModeling::DynamicUpdateType DynamicUpdate
            (
            );
            /** <b>Deprecated</b>:<br>
            &nbsp;&nbsp;&nbsp;Use @link DynamicUpdate() DynamicUpdate@endlink instead.
            @deprecated
            */
            public: NXOpen::Preferences::SessionModeling::DynamicUpdateType GetDynamicUpdate
            (
            ) { return this->DynamicUpdate(); }
            /**Sets  the dynamic update. Specifies that the system dynamically displays in real time with each 
                updation of parent curves, splines, bridge curves, lines or arcs  <br> License requirements : None */
            public: void SetDynamicUpdate
            (
                NXOpen::Preferences::SessionModeling::DynamicUpdateType dynamic_update /**  */
            );
            /**Returns  the immediate children. Specifies to which level the dynamic updation is applicable.  <br> License requirements : None */
            public: NXOpen::Preferences::SessionModeling::ImmediateChildrenType ImmediateChildren
            (
            );
            /** <b>Deprecated</b>:<br>
            &nbsp;&nbsp;&nbsp;Use @link ImmediateChildren() ImmediateChildren@endlink instead.
            @deprecated
            */
            public: NXOpen::Preferences::SessionModeling::ImmediateChildrenType GetImmediateChildren
            (
            ) { return this->ImmediateChildren(); }
            /**Sets  the immediate children. Specifies to which level the dynamic updation is applicable.  <br> License requirements : None */
            public: void SetImmediateChildren
            (
                NXOpen::Preferences::SessionModeling::ImmediateChildrenType immediate_children /**  */
            );
            /**Returns  the features/mark. Controls how often, during feature creation and editing, the system sets internal marks 
                used in updating. A Features/Mark value of 5, for example, means that one mark will be set after five features 
                are created or edited.  <br> License requirements : None */
            public: int PmarkFrequency
            (
            );
            /** <b>Deprecated</b>:<br>
            &nbsp;&nbsp;&nbsp;Use @link PmarkFrequency() PmarkFrequency@endlink instead.
            @deprecated
            */
            public: int GetPmarkFrequency
            (
            ) { return this->PmarkFrequency(); }
            /**Sets  the features/mark. Controls how often, during feature creation and editing, the system sets internal marks 
                used in updating. A Features/Mark value of 5, for example, means that one mark will be set after five features 
                are created or edited.  <br> License requirements : None */
            public: void SetPmarkFrequency
            (
                int pmark_frequency /**  */
            );
            /**Returns  the body type. Toggles between Solid and Sheet. When creating bodies through curves, the Body Type option provides
                 control to the type of body (for example, solid body vs. sheet body) that is created.  <br> License requirements : None */
            public: NXOpen::Preferences::SessionModeling::BodyTypeOption BodyType
            (
            );
            /** <b>Deprecated</b>:<br>
            &nbsp;&nbsp;&nbsp;Use @link BodyType() BodyType@endlink instead.
            @deprecated
            */
            public: NXOpen::Preferences::SessionModeling::BodyTypeOption GetBodyType
            (
            ) { return this->BodyType(); }
            /**Sets  the body type. Toggles between Solid and Sheet. When creating bodies through curves, the Body Type option provides
                 control to the type of body (for example, solid body vs. sheet body) that is created.  <br> License requirements : None */
            public: void SetBodyType
            (
                NXOpen::Preferences::SessionModeling::BodyTypeOption body_type /**  */
            );
            /**Returns  the toggle "Display Legacy Feature names" gives choice, how user wants feature name in "Name" Coulmn in Partnav
                 checked toggled(True) will show old feature names in "Name" column in Partnav, while
                 unchecked toggled(False) will show new translatable feature names in "Name" column in Partnav <br> License requirements : None */
            public: bool DisplayLegacyFeatureName
            (
            );
            /**Sets  the toggle "Display Legacy Feature names" gives choice, how user wants feature name in "Name" Coulmn in Partnav
                 checked toggled(True) will show old feature names in "Name" column in Partnav, while
                 unchecked toggled(False) will show new translatable feature names in "Name" column in Partnav <br> License requirements : None */
            public: void SetDisplayLegacyFeatureName
            (
                bool display_legacy_feature_name /** preference to display_legacy_feature_name */
            );
            /**Returns  the curve fit method. Controls the fitting method used when curves must be approximated by splines.  <br> License requirements : None */
            public: NXOpen::Preferences::SessionModeling::CurveFitMethodType CurveFitMethod
            (
            );
            /** <b>Deprecated</b>:<br>
            &nbsp;&nbsp;&nbsp;Use @link CurveFitMethod() CurveFitMethod@endlink instead.
            @deprecated
            */
            public: NXOpen::Preferences::SessionModeling::CurveFitMethodType GetCurveFitMethod
            (
            ) { return this->CurveFitMethod(); }
            /**Sets  the curve fit method. Controls the fitting method used when curves must be approximated by splines.  <br> License requirements : None */
            public: void SetCurveFitMethod
            (
                NXOpen::Preferences::SessionModeling::CurveFitMethodType body_type /**  */
            );
            /**Returns  the free form construction result. Controls free form feature creation when using the Through Curves, Through 
                Curve Mesh, Swept, and Ruled options.  <br> License requirements : None */
            public: NXOpen::Preferences::SessionModeling::FreeFormConstructionResultType FreeFormConstructionResult
            (
            );
            /** <b>Deprecated</b>:<br>
            &nbsp;&nbsp;&nbsp;Use @link FreeFormConstructionResult() FreeFormConstructionResult@endlink instead.
            @deprecated
            */
            public: NXOpen::Preferences::SessionModeling::FreeFormConstructionResultType GetFreeFormConstructionResult
            (
            ) { return this->FreeFormConstructionResult(); }
            /**Sets  the free form construction result. Controls free form feature creation when using the Through Curves, Through 
                Curve Mesh, Swept, and Ruled options.  <br> License requirements : None */
            public: void SetFreeFormConstructionResult
            (
                NXOpen::Preferences::SessionModeling::FreeFormConstructionResultType free_form_constr_result /**  */
            );
            /**Returns  the associative edit free form option. Specify whether the output of editing certain free form features remain 
                as free form features or as unparameterized features.  <br> License requirements : None */
            public: bool AssociativeEditFreeForm
            (
            );
            /** <b>Deprecated</b>:<br>
            &nbsp;&nbsp;&nbsp;Use @link AssociativeEditFreeForm() AssociativeEditFreeForm@endlink instead.
            @deprecated
            */
            public: bool GetAssociativeEditFreeForm
            (
            ) { return this->AssociativeEditFreeForm(); }
            /**Sets  the associative edit free form option. Specify whether the output of editing certain free form features remain 
                as free form features or as unparameterized features.  <br> License requirements : None */
            public: void SetAssociativeEditFreeForm
            (
                bool associative_edit_free_form /**  */
            );
            /**Returns  the position color  <br> License requirements : None */
            public: int PositionColor
            (
            );
            /** <b>Deprecated</b>:<br>
            &nbsp;&nbsp;&nbsp;Use @link PositionColor() PositionColor@endlink instead.
            @deprecated
            */
            public: int GetPositionColor
            (
            ) { return this->PositionColor(); }
            /**Sets  the position color  <br> License requirements : None */
            public: void SetPositionColor
            (
                int position_color /**  */
            );
            /**Returns  the tangent color  <br> License requirements : None */
            public: int TangentColor
            (
            );
            /** <b>Deprecated</b>:<br>
            &nbsp;&nbsp;&nbsp;Use @link TangentColor() TangentColor@endlink instead.
            @deprecated
            */
            public: int GetTangentColor
            (
            ) { return this->TangentColor(); }
            /**Sets  the tangent color  <br> License requirements : None */
            public: void SetTangentColor
            (
                int tangent_color /**  */
            );
            /**Returns  the curvature color  <br> License requirements : None */
            public: int CurvatureColor
            (
            );
            /** <b>Deprecated</b>:<br>
            &nbsp;&nbsp;&nbsp;Use @link CurvatureColor() CurvatureColor@endlink instead.
            @deprecated
            */
            public: int GetCurvatureColor
            (
            ) { return this->CurvatureColor(); }
            /**Sets  the curvature color  <br> License requirements : None */
            public: void SetCurvatureColor
            (
                int curvature_color /**  */
            );
            /**Returns  the acceleration color  <br> License requirements : None */
            public: int AccelerationColor
            (
            );
            /** <b>Deprecated</b>:<br>
            &nbsp;&nbsp;&nbsp;Use @link AccelerationColor() AccelerationColor@endlink instead.
            @deprecated
            */
            public: int GetAccelerationColor
            (
            ) { return this->AccelerationColor(); }
            /**Sets  the acceleration color  <br> License requirements : None */
            public: void SetAccelerationColor
            (
                int acceleration_color /**  */
            );
            /**Returns  the B curve pole curve color. This is color of the pole control polygons for B-curves  <br> License requirements : None */
            public: int BCurvePoleCurveColor
            (
            );
            /** <b>Deprecated</b>:<br>
            &nbsp;&nbsp;&nbsp;Use @link BCurvePoleCurveColor() BCurvePoleCurveColor@endlink instead.
            @deprecated
            */
            public: int GetBCurvePoleCurveColor
            (
            ) { return this->BCurvePoleCurveColor(); }
            /**Sets  the B curve pole curve color. This is color of the pole control polygons for B-curves  <br> License requirements : None */
            public: void SetBCurvePoleCurveColor
            (
                int b_curve_pole_color /**  */
            );
            /**Returns  the B surface pole face color. This is color of the pole control polygons for B-surface  <br> License requirements : None */
            public: int BSurfacePoleFaceColor
            (
            );
            /** <b>Deprecated</b>:<br>
            &nbsp;&nbsp;&nbsp;Use @link BSurfacePoleFaceColor() BSurfacePoleFaceColor@endlink instead.
            @deprecated
            */
            public: int GetBSurfacePoleFaceColor
            (
            ) { return this->BSurfacePoleFaceColor(); }
            /**Sets  the B surface pole face color. This is color of the pole control polygons for B-surface  <br> License requirements : None */
            public: void SetBSurfacePoleFaceColor
            (
                int b_surface_pole_face_color /**  */
            );
            /**Returns  the curve color option for B Curve. If true the user selected color is applied on curve  <br> License requirements : None */
            public: bool UseCurveColor
            (
            );
            /** <b>Deprecated</b>:<br>
            &nbsp;&nbsp;&nbsp;Use @link UseCurveColor() UseCurveColor@endlink instead.
            @deprecated
            */
            public: bool GetUseCurveColor
            (
            ) { return this->UseCurveColor(); }
            /**Sets  the curve color option for B Curve. If true the user selected color is applied on curve  <br> License requirements : None */
            public: void SetUseCurveColor
            (
                bool use_curve_color /**  */
            );
            /**Returns  the face color option for B Surface. If true the user selected color is applied on face  <br> License requirements : None */
            public: bool UseFaceColor
            (
            );
            /** <b>Deprecated</b>:<br>
            &nbsp;&nbsp;&nbsp;Use @link UseFaceColor() UseFaceColor@endlink instead.
            @deprecated
            */
            public: bool GetUseFaceColor
            (
            ) { return this->UseFaceColor(); }
            /**Sets  the face color option for B Surface. If true the user selected color is applied on face  <br> License requirements : None */
            public: void SetUseFaceColor
            (
                bool use_face_color /**  */
            );
            /**Returns  the update delayed option.  If the option is true, then an edited
                feature does not update until @link Update::DoUpdate Update::DoUpdate@endlink  is
                explicitly called.  If the option is false, then the edited feature
                updates immediately.  The default is false.  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: bool UpdateDelayed
            (
            );
            /** <b>Deprecated</b>:<br>
            &nbsp;&nbsp;&nbsp;Use @link UpdateDelayed() UpdateDelayed@endlink instead.
            @deprecated
            */
            public: bool GetUpdateDelayed
            (
            ) { return this->UpdateDelayed(); }
            /**Sets  the update delayed option.  If the option is true, then an edited
                feature does not update until @link Update::DoUpdate Update::DoUpdate@endlink  is
                explicitly called.  If the option is false, then the edited feature
                updates immediately.  The default is false.  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetUpdateDelayed
            (
                bool option /** */
            );
            /**Sets  the preview resolution setting.  <br> License requirements : None */
            public: void SetPreviewResolution
            (
                NXOpen::Preferences::SessionModeling::PreviewResolutionType resolution /**  */
            );
            /**Returns  the preview resolution setting.  <br> License requirements : None */
            public: NXOpen::Preferences::SessionModeling::PreviewResolutionType PreviewResolution
            (
            );
            /**Sets  the enable trimmed animation setting.  <br> License requirements : None */
            public: void SetEnableTrimmedAnimation
            (
                bool enable /**  */
            );
            /**Returns  the enable trimmed animation setting.  <br> License requirements : None */
            public: bool EnableTrimmedAnimation
            (
            );
            /**Sets  the use triangular mesh setting setting.  <br> License requirements : None */
            public: void SetUseTriangularMesh
            (
                bool use /**  */
            );
            /**Returns  the use triangular mesh setting setting.  <br> License requirements : None */
            public: bool UseTriangularMesh
            (
            );
            /**Returns  the option "Edit with Rollback upon Double-Click" gives choice of what action to 
                be taken on feature upon Double clicking, either in partnavigator or in Graphics widow.
                if the option is true then edit with rollback will be happen upon Double-click.
                if the option is false then the previous default action will be executed  <br> License requirements : None */
            public: bool EditWithRollbackUponDoubleClick
            (
            );
            /**Sets  the option "Edit with Rollback upon Double-Click" gives choice of what action to 
                be taken on feature upon Double clicking, either in partnavigator or in Graphics widow.
                if the option is true then edit with rollback will be happen upon Double-click.
                if the option is false then the previous default action will be executed  <br> License requirements : None */
            public: void SetEditWithRollbackUponDoubleClick
            (
                bool default_edit_option /** preference to Edit with Rollback upon Double-Click */
            );
            /**Returns  the option " Notify on Delete " gives choice, whether the user wants a 
                 notification message when a feature is being deleted will effect other features.
                 if the option is true then it popup a notification message.
                 if the option is true then it will not popup any notification message  <br> License requirements : None */
            public: bool NotifyOnDelete
            (
            );
            /**Sets  the option " Notify on Delete " gives choice, whether the user wants a 
                 notification message when a feature is being deleted will effect other features.
                 if the option is true then it popup a notification message.
                 if the option is true then it will not popup any notification message  <br> License requirements : None */
            public: void SetNotifyOnDelete
            (
                bool notify_on_delete /** preference to Notify on Delete */
            );
            public: virtual void initialize();
        };
    }
}
#undef EXPORTLIBRARY
#endif