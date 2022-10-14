#ifndef NXOpen_PREFERENCES_PARTVISUALIZATIONSHADE_HXX_INCLUDED
#define NXOpen_PREFERENCES_PARTVISUALIZATIONSHADE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Preferences_PartVisualizationShade.ja
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
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Preferences
    {
        class PartVisualizationShade;
    }
    namespace Preferences
    {
        class PartPreferences;
    }
    namespace Preferences
    {
        /** Represents the set of shade visualization preferences applicable to entire part <br> To obtain an instance of this class, refer to @link Preferences::PartPreferences Preferences::PartPreferences@endlink  <br> */
        class NXOPENCPPEXPORT PartVisualizationShade
        {
            /** Describes the available tolerance types for Shaded View. Each of these options maps tolerance values to 
             three specific faceting operations: Facet Edge Tolerance, Facet Chord Tolerance, and Angular Tolerance.  */
            public: enum ShadedViewToleranceType
            {
                ShadedViewToleranceTypeCoarse/** For Coarse: Facet Edge Tolerance is 0.01, Facet 
                                                                                            Chord Tolerance is 0.01, and Angular Tolerance is 0.0  */,
                ShadedViewToleranceTypeStandard/** For Standard: Facet Edge Tolerance is 0.005, Facet 
                                                                                            Chord Tolerance is 0.005 , and Angular Tolerance is 15 */,
                ShadedViewToleranceTypeFine/** For Fine: Facet Edge Tolerance is 0.0005, Facet 
                                                                                            Chord Tolerance is 0.0025, and Angular Tolerance is 6 */,
                ShadedViewToleranceTypeExtrafine/** For Extrafine: Facet Edge Tolerance is 0.005, Facet 
                                                                                            Chord Tolerance is 0.001, and Angular Tolerance is 6 */,
                ShadedViewToleranceTypeUltrafine/** For Ultrafine: Facet Edge Tolerance is 0.0005, Facet 
                                                                                            Chord Tolerance is 0.0005, and Angular Tolerance is 3 */,
                ShadedViewToleranceTypeCustomize/** Customize. User can specify the Edge Tolerance,
                                                                                            Face Tolerance and Angle Tolerance specifically. */
            };

            /** Describes the available tolerance types for Advanced View. Each of these options maps tolerance values to 
               for specific operations : Curve Edge Chord Distance, Surface Chord Distance, Angular Tolerance, Facet Width 
               Tolerance */
            public: enum AdvViewToleranceType
            {
                AdvViewToleranceTypeCoarse/** Coarse  */,
                AdvViewToleranceTypeStandard/** Standard*/,
                AdvViewToleranceTypeFine/** Fine  */,
                AdvViewToleranceTypeExtrafine/** Extrafine */,
                AdvViewToleranceTypeSuperfine/** Superfine */,
                AdvViewToleranceTypeUltrafine/** Ultrafine  */,
                AdvViewToleranceTypeCustomize/** Custamize. User can specify the Edge Tolerance,
                                                                                            Face Tolerance and Angle Tolerance, Width Tolerance
                                                                                            specifically.  */
            };

            /** Describes whether the applied changes are applicable to visible object or all object or no object */
            public: enum ViewUpdateModeType
            {
                ViewUpdateModeTypeVisibleObject/** Applicable only to visible object */,
                ViewUpdateModeTypeAllObject/** Applicable to all object */,
                ViewUpdateModeTypeNone/** No object */
            };

            /** Describes whether the shaded face edges are having no color or body color or user defined color. */
            public: enum ShadedFaceEdge
            {
                ShadedFaceEdgeOff/** Option is off */,
                ShadedFaceEdgeBodyColor/** Body Color  */,
                ShadedFaceEdgeSpecifyColor/** Specified Color */
            };

            /** Describes whether the shaded face edges are invisible or dashed visible or with a color to depict the hidden geometry */
            public: enum HiddenShadedFaceEdges
            {
                HiddenShadedFaceEdgesInvisible/** If selected, shaded face edges that are 
                                                                                           hidden are not displayed  */,
                HiddenShadedFaceEdgesDashed/** If selected, hidden shaded face edges are 
                                                                                           displayed in the body color with a dashed line 
                                                                                           font. */,
                HiddenShadedFaceEdgesHiddenColor/** If any color is selected, hidden shaded face 
                                                                                            edges are displayed in that color.*/
            };

            private: NXOpen::Preferences::PartPreferences* m_owner;
            public: explicit PartVisualizationShade(NXOpen::Preferences::PartPreferences *owner): m_owner(owner)
            {
            }
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            /**Returns  the tolerance for shaded view.  <br> License requirements : None */
            public: NXOpen::Preferences::PartVisualizationShade::ShadedViewToleranceType ShadedViewTolerance
            (
            );
            /**Sets  the tolerance for shaded view.  <br> License requirements : None */
            public: void SetShadedViewTolerance
            (
                NXOpen::Preferences::PartVisualizationShade::ShadedViewToleranceType shadedViewTolerance /** shaded view tolerance */ 
            );
            /**Returns  the edge tolerance for shaded view.  <br> License requirements : None */
            public: double ShadedViewEdgeTolerance
            (
            );
            /**Sets  the edge tolerance for shaded view.  <br> License requirements : None */
            public: void SetShadedViewEdgeTolerance
            (
                double shadedViewEdgeTolerance /** shaded view edge tolerance */ 
            );
            /**Returns  the face tolerance for shaded view.  <br> License requirements : None */
            public: double ShadedViewFaceTolerance
            (
            );
            /**Sets  the face tolerance for shaded view.  <br> License requirements : None */
            public: void SetShadedViewFaceTolerance
            (
                double shadedViewFaceTolerance /** shaded view face tolerance */ 
            );
            /**Returns  the angle tolerance for shaded view.  <br> License requirements : None */
            public: double ShadedViewAngleTolerance
            (
            );
            /**Sets  the angle tolerance for shaded view.  <br> License requirements : None */
            public: void SetShadedViewAngleTolerance
            (
                double shadedViewAngleTolerance /** shaded view angle tolerance */ 
            );
            /**Returns  the update mode for shaded view.  <br> License requirements : None */
            public: NXOpen::Preferences::PartVisualizationShade::ViewUpdateModeType ShadedViewUpdateMode
            (
            );
            /**Sets  the update mode for shaded view.  <br> License requirements : None */
            public: void SetShadedViewUpdateMode
            (
                NXOpen::Preferences::PartVisualizationShade::ViewUpdateModeType shadedViewUpdateMode /** shaded view update mode */ 
            );
            /**Returns  the tolerance for advanced visualization views.  <br> License requirements : None */
            public: NXOpen::Preferences::PartVisualizationShade::AdvViewToleranceType AdvancedVisViewTolerance
            (
            );
            /**Sets  the tolerance for advanced visualization views.  <br> License requirements : None */
            public: void SetAdvancedVisViewTolerance
            (
                NXOpen::Preferences::PartVisualizationShade::AdvViewToleranceType advancedVisViewTolerance /** advanced vis view tolerance */ 
            );
            /**Returns  the edge tolerance for advanced visualization views.   <br> License requirements : None */
            public: double AdvancedVisViewEdgeTolerance
            (
            );
            /**Sets  the edge tolerance for advanced visualization views.   <br> License requirements : None */
            public: void SetAdvancedVisViewEdgeTolerance
            (
                double advancedVisViewEdgeTolerance /** advanced vis view edge tolerance */ 
            );
            /**Returns  the face tolerance for advanced visualization views.   <br> License requirements : None */
            public: double AdvancedVisViewFaceTolerance
            (
            );
            /**Sets  the face tolerance for advanced visualization views.   <br> License requirements : None */
            public: void SetAdvancedVisViewFaceTolerance
            (
                double advancedVisViewFaceTolerance /** advanced vis view face tolerance */ 
            );
            /**Returns  the angle tolerance for advanced visualization views.  <br> License requirements : None */
            public: double AdvancedVisViewAngleTolerance
            (
            );
            /**Sets  the angle tolerance for advanced visualization views.  <br> License requirements : None */
            public: void SetAdvancedVisViewAngleTolerance
            (
                double advancedVisViewAngleTolerance /** advanced vis view angle tolerance */ 
            );
            /**Returns  the width tolerance for advanced Visualization Views.   <br> License requirements : None */
            public: double AdvancedVisViewWidthTolerance
            (
            );
            /**Sets  the width tolerance for advanced Visualization Views.   <br> License requirements : None */
            public: void SetAdvancedVisViewWidthTolerance
            (
                double advancedVisViewWidthTolerance /** advanced vis view width tolerance */ 
            );
            /**Returns  the update mode for advanced visualization views.  <br> License requirements : None */
            public: NXOpen::Preferences::PartVisualizationShade::ViewUpdateModeType AdvancedVisViewUpdateMode
            (
            );
            /**Sets  the update mode for advanced visualization views.  <br> License requirements : None */
            public: void SetAdvancedVisViewUpdateMode
            (
                NXOpen::Preferences::PartVisualizationShade::ViewUpdateModeType advancedVisViewUpdateMode /** advanced vis view update mode */ 
            );
            /**Returns  the shade hidden geometry color.   <br> License requirements : None */
            public: int HiddenGeometryColor
            (
            );
            /**Sets  the shade hidden geometry color.   <br> License requirements : None */
            public: void SetHiddenGeometryColor
            (
                int hiddenGeomColor /** hidden geom color */ 
            );
            /**Returns  the shaded face edges option.
             <br> This property is deprecated. Use @link NXOpen::Preferences::ViewVisualizationVisual::ShadedEdgeStyle NXOpen::Preferences::ViewVisualizationVisual::ShadedEdgeStyle @endlink and @link NXOpen::Preferences::ViewVisualizationVisual::SetShadedEdgeStyle NXOpen::Preferences::ViewVisualizationVisual::SetShadedEdgeStyle @endlink  instead.
             <br>  
             @deprecated Deprecated in NX4 <br> 
             <br> License requirements : None */
            public: NXOpen::Preferences::PartVisualizationShade::ShadedFaceEdge ShadedFaceEdgeOption
            (
            );
            /**Sets  the shaded face edges option.
             <br> This property is deprecated. Use @link NXOpen::Preferences::ViewVisualizationVisual::ShadedEdgeStyle NXOpen::Preferences::ViewVisualizationVisual::ShadedEdgeStyle @endlink and @link NXOpen::Preferences::ViewVisualizationVisual::SetShadedEdgeStyle NXOpen::Preferences::ViewVisualizationVisual::SetShadedEdgeStyle @endlink  instead.
             <br>  
             @deprecated Deprecated in NX4 <br> 
             <br> License requirements : None */
            public: void SetShadedFaceEdgeOption
            (
                NXOpen::Preferences::PartVisualizationShade::ShadedFaceEdge shadedFaceEdgeOption /** shaded face edge option */ 
            );
            /**Returns  the shaded edge faces color.
             <br> This property is deprecated. Use @link NXOpen::Preferences::ViewVisualizationVisual::ShadedEdgeColor NXOpen::Preferences::ViewVisualizationVisual::ShadedEdgeColor @endlink and @link NXOpen::Preferences::ViewVisualizationVisual::SetShadedEdgeColor NXOpen::Preferences::ViewVisualizationVisual::SetShadedEdgeColor @endlink  instead.
             <br>  
             @deprecated Deprecated in NX4 <br> 
             <br> License requirements : None */
            public: int ShadedFaceEdgesColor
            (
            );
            /**Sets  the shaded edge faces color.
             <br> This property is deprecated. Use @link NXOpen::Preferences::ViewVisualizationVisual::ShadedEdgeColor NXOpen::Preferences::ViewVisualizationVisual::ShadedEdgeColor @endlink and @link NXOpen::Preferences::ViewVisualizationVisual::SetShadedEdgeColor NXOpen::Preferences::ViewVisualizationVisual::SetShadedEdgeColor @endlink  instead.
             <br>  
             @deprecated Deprecated in NX4 <br> 
             <br> License requirements : None */
            public: void SetShadedFaceEdgesColor
            (
                int shadedFaceEdgesColor /** shaded face edges color */ 
            );
            /**Returns  the shaded hidden shaded face edges option.
             <br> This property is deprecated. Use @link NXOpen::Preferences::ViewVisualizationVisual::HiddenEdgeStyle NXOpen::Preferences::ViewVisualizationVisual::HiddenEdgeStyle @endlink and @link NXOpen::Preferences::ViewVisualizationVisual::SetHiddenEdgeStyle NXOpen::Preferences::ViewVisualizationVisual::SetHiddenEdgeStyle @endlink  instead.
             <br>  
             @deprecated Deprecated in NX4 <br> 
             <br> License requirements : None */
            public: NXOpen::Preferences::PartVisualizationShade::HiddenShadedFaceEdges HiddenShadedFaceEdgesOption
            (
            );
            /**Sets  the shaded hidden shaded face edges option.
             <br> This property is deprecated. Use @link NXOpen::Preferences::ViewVisualizationVisual::HiddenEdgeStyle NXOpen::Preferences::ViewVisualizationVisual::HiddenEdgeStyle @endlink and @link NXOpen::Preferences::ViewVisualizationVisual::SetHiddenEdgeStyle NXOpen::Preferences::ViewVisualizationVisual::SetHiddenEdgeStyle @endlink  instead.
             <br>  
             @deprecated Deprecated in NX4 <br> 
             <br> License requirements : None */
            public: void SetHiddenShadedFaceEdgesOption
            (
                NXOpen::Preferences::PartVisualizationShade::HiddenShadedFaceEdges hiddenShadedFaceEdgesChoice /** hidden shaded face edges choice */ 
            );
            public: virtual void initialize();
        };
    }
}
#undef EXPORTLIBRARY
#endif