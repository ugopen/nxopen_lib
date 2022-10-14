#ifndef NXOpen_PREFERENCES_SESSIONSKETCH_HXX_INCLUDED
#define NXOpen_PREFERENCES_SESSIONSKETCH_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Preferences_SessionSketch.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/Preferences_SketchPreferences.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Preferences
    {
        class SessionSketch;
    }
    namespace Preferences
    {
        class SessionPreferences;
    }
    namespace Preferences
    {
        /** Represents the set of sketch preferences applicable to entire session  <br> To obtain an instance of this class, refer to @link Preferences::SessionPreferences Preferences::SessionPreferences@endlink  <br> */
        class NXOPENCPPEXPORT SessionSketch
        {
            /** Describes the available sketch origin types. */
            public: enum OriginType
            {
                OriginTypeInferFromPlaneSelection/** Sketch origin is inferred from placement face */,
                OriginTypeProjectWorkPartOrigin/** Sketch origin is the projection of the work part origin */
            };

            /** Describes the available sketch background types. */
            public: enum BackgroundType
            {
                BackgroundTypeInherit/** Sketch background color is inherited from the parent application */,
                BackgroundTypePlain/** Sketch background color is forced to the plain background color */
            };

            private: NXOpen::Preferences::SessionPreferences* m_owner;
            public: explicit SessionSketch(NXOpen::Preferences::SessionPreferences *owner): m_owner(owner)
            {
            }
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            /**Returns  the snap angle.  This is snap angle tolerance for vertical, horizontal, parallel, and perpendicular 
                lines.The default value is 3 and maximum value is 20  <br> License requirements : None */
            public: double SnapAngle
            (
            );
            /** <b>Deprecated</b>:<br>
            &nbsp;&nbsp;&nbsp;Use @link SnapAngle() SnapAngle@endlink instead.
            @deprecated
            */
            public: double GetSnapAngle
            (
            ) { return this->SnapAngle(); }
            /**Sets  the snap angle.  This is snap angle tolerance for vertical, horizontal, parallel, and perpendicular 
                lines.The default value is 3 and maximum value is 20  <br> License requirements : None */
            public: void SetSnapAngle
            (
                double snap_angle /** snap angle */ 
            );
            /**Returns  the change view orientation flag.  If true, when a sketch is activated, the view will be changed to 
                align with the sketch  <br> License requirements : None */
            public: bool ChangeViewOrientation
            (
            );
            /** <b>Deprecated</b>:<br>
            &nbsp;&nbsp;&nbsp;Use @link ChangeViewOrientation() ChangeViewOrientation@endlink instead.
            @deprecated
            */
            public: bool GetChangeViewOrientation
            (
            ) { return this->ChangeViewOrientation(); }
            /**Sets  the change view orientation flag.  If true, when a sketch is activated, the view will be changed to 
                align with the sketch  <br> License requirements : None */
            public: void SetChangeViewOrientation
            (
                bool change_view_orientation /** change view orientation */ 
            );
            /**Returns  the maintain layer status flag. Controls whether the work layer remains the same or returns to its previous 
                value when a sketch is deactivated.  <br> License requirements : None */
            public: bool MaintainLayerStatus
            (
            );
            /** <b>Deprecated</b>:<br>
            &nbsp;&nbsp;&nbsp;Use @link MaintainLayerStatus() MaintainLayerStatus@endlink instead.
            @deprecated
            */
            public: bool GetMaintainLayerStatus
            (
            ) { return this->MaintainLayerStatus(); }
            /**Sets  the maintain layer status flag. Controls whether the work layer remains the same or returns to its previous 
                value when a sketch is deactivated.  <br> License requirements : None */
            public: void SetMaintainLayerStatus
            (
                bool maintain_layer_status /** maintain layer status */ 
            );
            /**Returns  the displays DOF arrows flag. Controls the display of the degree of freedom arrows. When this flag is set as
                False, the display of the arrows is turned OFF.  <br> License requirements : None */
            public: bool DisplayDOFArrows
            (
            );
            /** <b>Deprecated</b>:<br>
            &nbsp;&nbsp;&nbsp;Use @link DisplayDOFArrows() DisplayDOFArrows@endlink instead.
            @deprecated
            */
            public: bool GetDisplayDOFArrows
            (
            ) { return this->DisplayDOFArrows(); }
            /**Sets  the displays DOF arrows flag. Controls the display of the degree of freedom arrows. When this flag is set as
                False, the display of the arrows is turned OFF.  <br> License requirements : None */
            public: void SetDisplayDOFArrows
            (
                bool display_d_o_f_arrows /** display d o f arrows */ 
            );
            /**Returns  the dynamic constraints display flag. If it is True, constraint symbols do not display if the associated 
                geometry is very small.  <br> License requirements : None */
            public: bool DynamicConstraintDisplay
            (
            );
            /** <b>Deprecated</b>:<br>
            &nbsp;&nbsp;&nbsp;Use @link DynamicConstraintDisplay() DynamicConstraintDisplay@endlink instead.
            @deprecated
            */
            public: bool GetDynamicConstraintDisplay
            (
            ) { return this->DynamicConstraintDisplay(); }
            /**Sets  the dynamic constraints display flag. If it is True, constraint symbols do not display if the associated 
                geometry is very small.  <br> License requirements : None */
            public: void SetDynamicConstraintDisplay
            (
                bool dynamic_constraint_display /** dynamic constraint display */ 
            );
            /**Returns  the retain dimensions flag. If it is True, text size absolute value will not change when zooming in or out.  <br> License requirements : None */
            public: bool TextSizeFixed
            (
            );
            /**Sets  the retain dimensions flag. If it is True, text size absolute value will not change when zooming in or out.  <br> License requirements : None */
            public: void SetTextSizeFixed
            (
                bool text_size_fixed /** text size fixed */ 
            );
            /**Returns  the retain dimensions flag. If it is True, sketch dimensions continue to display after a sketch is deactivated.  <br> License requirements : None */
            public: bool RetainDimensions
            (
            );
            /** <b>Deprecated</b>:<br>
            &nbsp;&nbsp;&nbsp;Use @link RetainDimensions() RetainDimensions@endlink instead.
            @deprecated
            */
            public: bool GetRetainDimensions
            (
            ) { return this->RetainDimensions(); }
            /**Sets  the retain dimensions flag. If it is True, sketch dimensions continue to display after a sketch is deactivated.  <br> License requirements : None */
            public: void SetRetainDimensions
            (
                bool retain_dimensions /** retain dimensions */ 
            );
            /**Returns  the origin option  <br> License requirements : None */
            public: NXOpen::Preferences::SessionSketch::OriginType OriginOption
            (
            );
            /**Sets  the origin option  <br> License requirements : None */
            public: void SetOriginOption
            (
                NXOpen::Preferences::SessionSketch::OriginType origin_type /** origin type */ 
            );
            /**Returns  the background option  <br> License requirements : None */
            public: NXOpen::Preferences::SessionSketch::BackgroundType BackgroundOption
            (
            );
            /**Sets  the background option  <br> License requirements : None */
            public: void SetBackgroundOption
            (
                NXOpen::Preferences::SessionSketch::BackgroundType background_type /** background type */ 
            );
            /**Returns  the default sketch name prefix   <br> License requirements : None */
            public: NXString DefaultSketchNamePrefix
            (
            );
            /** <b>Deprecated</b>:<br>
            &nbsp;&nbsp;&nbsp;Use @link DefaultSketchNamePrefix() DefaultSketchNamePrefix@endlink instead.
            @deprecated
            */
            public: NXString GetDefaultSketchNamePrefix
            (
            ) { return this->DefaultSketchNamePrefix(); }
            /**Sets  the default sketch name prefix   <br> License requirements : None */
            public: void SetDefaultSketchNamePrefix
            (
                const NXString & default_sketch_name_prefix /** default sketch name prefix */ 
            );
            /**Returns  the default vertex name prefix  <br> License requirements : None */
            public: NXString DefaultVertexNamePrefix
            (
            );
            /** <b>Deprecated</b>:<br>
            &nbsp;&nbsp;&nbsp;Use @link DefaultVertexNamePrefix() DefaultVertexNamePrefix@endlink instead.
            @deprecated
            */
            public: NXString GetDefaultVertexNamePrefix
            (
            ) { return this->DefaultVertexNamePrefix(); }
            /**Sets  the default vertex name prefix  <br> License requirements : None */
            public: void SetDefaultVertexNamePrefix
            (
                const NXString & default_vertex_name_prefix /** default vertex name prefix */ 
            );
            /**Returns  the default line name prefix  <br> License requirements : None */
            public: NXString DefaultLineNamePrefix
            (
            );
            /** <b>Deprecated</b>:<br>
            &nbsp;&nbsp;&nbsp;Use @link DefaultLineNamePrefix() DefaultLineNamePrefix@endlink instead.
            @deprecated
            */
            public: NXString GetDefaultLineNamePrefix
            (
            ) { return this->DefaultLineNamePrefix(); }
            /**Sets  the default line name prefix  <br> License requirements : None */
            public: void SetDefaultLineNamePrefix
            (
                const NXString & default_line_name_prefix /** default line name prefix */ 
            );
            /**Returns  the default arc name prefix  <br> License requirements : None */
            public: NXString DefaultArcNamePrefix
            (
            );
            /** <b>Deprecated</b>:<br>
            &nbsp;&nbsp;&nbsp;Use @link DefaultArcNamePrefix() DefaultArcNamePrefix@endlink instead.
            @deprecated
            */
            public: NXString GetDefaultArcNamePrefix
            (
            ) { return this->DefaultArcNamePrefix(); }
            /**Sets  the default arc name prefix  <br> License requirements : None */
            public: void SetDefaultArcNamePrefix
            (
                const NXString & default_arc_name_prefix /** default arc name prefix */ 
            );
            /**Returns  the default conic name prefix  <br> License requirements : None */
            public: NXString DefaultConicNamePrefix
            (
            );
            /** <b>Deprecated</b>:<br>
            &nbsp;&nbsp;&nbsp;Use @link DefaultConicNamePrefix() DefaultConicNamePrefix@endlink instead.
            @deprecated
            */
            public: NXString GetDefaultConicNamePrefix
            (
            ) { return this->DefaultConicNamePrefix(); }
            /**Sets  the default conic name prefix  <br> License requirements : None */
            public: void SetDefaultConicNamePrefix
            (
                const NXString & default_conic_name_prefix /** default conic name prefix */ 
            );
            /**Returns  the default spline name prefix  <br> License requirements : None */
            public: NXString DefaultSplineNamePrefix
            (
            );
            /** <b>Deprecated</b>:<br>
            &nbsp;&nbsp;&nbsp;Use @link DefaultSplineNamePrefix() DefaultSplineNamePrefix@endlink instead.
            @deprecated
            */
            public: NXString GetDefaultSplineNamePrefix
            (
            ) { return this->DefaultSplineNamePrefix(); }
            /**Sets  the default spline name prefix  <br> License requirements : None */
            public: void SetDefaultSplineNamePrefix
            (
                const NXString & default_spline_name_prefix /** default spline name prefix */ 
            );
            /**Returns  the decimal places  <br> License requirements : None */
            public: int DecimalPlaces
            (
            );
            /** <b>Deprecated</b>:<br>
            &nbsp;&nbsp;&nbsp;Use @link DecimalPlaces() DecimalPlaces@endlink instead.
            @deprecated
            */
            public: int GetDecimalPlaces
            (
            ) { return this->DecimalPlaces(); }
            /**Sets  the decimal places  <br> License requirements : None */
            public: void SetDecimalPlaces
            (
                int decimal_places /** decimal places */ 
            );
            /**Returns  the text height  <br> License requirements : None */
            public: double TextHeight
            (
            );
            /** <b>Deprecated</b>:<br>
            &nbsp;&nbsp;&nbsp;Use @link TextHeight() TextHeight@endlink instead.
            @deprecated
            */
            public: double GetTextHeight
            (
            ) { return this->TextHeight(); }
            /**Sets  the text height  <br> License requirements : None */
            public: void SetTextHeight
            (
                double text_height /** text height */ 
            );
            /**Returns  the dimension label  <br> License requirements : None */
            public: NXOpen::Preferences::SketchPreferences::DimensionLabelType DimensionLabel
            (
            );
            /** <b>Deprecated</b>:<br>
            &nbsp;&nbsp;&nbsp;Use @link DimensionLabel() DimensionLabel@endlink instead.
            @deprecated
            */
            public: NXOpen::Preferences::SketchPreferences::DimensionLabelType GetDimensionLabel
            (
            ) { return this->DimensionLabel(); }
            /**Sets  the dimension label  <br> License requirements : None */
            public: void SetDimensionLabel
            (
                NXOpen::Preferences::SketchPreferences::DimensionLabelType dimension_label /** dimension label */ 
            );
            /**Returns  the delay evaluation preference.  This preference is used in the UI to indicate 
                whether the sketch should be evaluated when a constraint is
                added to the sketch.  <br> License requirements : None */
            public: bool DelayEvaluation
            (
            );
            /** <b>Deprecated</b>:<br>
            &nbsp;&nbsp;&nbsp;Use @link DelayEvaluation() DelayEvaluation@endlink instead.
            @deprecated
            */
            public: bool GetDelayEvaluation
            (
            ) { return this->DelayEvaluation(); }
            /**Sets  the delay evaluation preference.  This preference is used in the UI to indicate 
                whether the sketch should be evaluated when a constraint is
                added to the sketch.  <br> License requirements : solid_modeling ("SOLIDS MODELING") OR drafting ("DRAFTING") */
            public: void SetDelayEvaluation
            (
                bool delay_evaluation /** delay evaluation */ 
            );
            public: virtual void initialize();
        };
    }
}
#undef EXPORTLIBRARY
#endif