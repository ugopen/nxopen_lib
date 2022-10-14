#ifndef NXOpen_PREFERENCES_SKETCHPREFERENCES_HXX_INCLUDED
#define NXOpen_PREFERENCES_SKETCHPREFERENCES_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Preferences_SketchPreferences.ja
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
        class SketchPreferences;
    }
    class Sketch;
    namespace Preferences
    {
        /** Represents the set of sketch preferences applicable on @link Sketch Sketch@endlink  object <br> To obtain an instance of this class, refer to @link Sketch Sketch@endlink  <br> */
        class NXOPENCPPEXPORT SketchPreferences
        {
            /** Describes the available dimension labels. */
            public: enum DimensionLabelType
            {
                DimensionLabelTypeExpression/** Displays the entire expression such as P2=P3*4 */,
                DimensionLabelTypeName/** Displays only the name of the expression, such as P2 */,
                DimensionLabelTypeValue/** Displays the numerical value of the expression */
            };

            private: NXOpen::Sketch* m_owner;
            public: explicit SketchPreferences(NXOpen::Sketch *owner): m_owner(owner)
            {
            }
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            /**Returns  the decimal places. Defines the number of digits to display after the decimal point on sketch dimensions 
                    (dimensional constraints).  The default value is three. 
                    NX6 - The decimal places preference has been removed from sketches. Each sketch dimension's
                    decimal places will be controlled via its own annotation preferences.
                    get function -  will always return the annotation preferences- dimension- decimal places.  
                    set function -  will apply the preference to each dimension in the sketch.
                    The annotation preference can be asked or set by calling the following functions.
                       JA_ANN_GBL_ask_dimension_preferences
                       JA_ANN_GBL_set_dimension_preferences 
             @deprecated Deprecated in NX6 <br> 
             <br> License requirements : None */
            public: double DecimalPlaces
            (
            );
            /**Sets  the decimal places. Defines the number of digits to display after the decimal point on sketch dimensions 
                    (dimensional constraints).  The default value is three. 
                    NX6 - The decimal places preference has been removed from sketches. Each sketch dimension's
                    decimal places will be controlled via its own annotation preferences.
                    get function -  will always return the annotation preferences- dimension- decimal places.  
                    set function -  will apply the preference to each dimension in the sketch.
                    The annotation preference can be asked or set by calling the following functions.
                       JA_ANN_GBL_ask_dimension_preferences
                       JA_ANN_GBL_set_dimension_preferences 
             @deprecated Deprecated in NX6 <br> 
             <br> License requirements : None */
            public: void SetDecimalPlaces
            (
                double decimalPlaces /** decimal places */ 
            );
            /**Returns  the text height. It is size of text displayed in sketch dimensions. The default is 0.125 
                    NX6 - The text height  preference has been removed from sketches. Each sketch dimension's
                    text height will be controlled via its own annotation preferences.
                    get function -  will always return the annotation preferences- letter prefs- dimension- text height.  
                    set function -  will apply the preference to each dimension in the sketch.
                    The annotation preference can be asked or set by calling the following functions.
                       JA_ANN_GBL_ask_lettering_preferences
                       JA_ANN_GBL_set_lettering_preferences 
             @deprecated Deprecated in NX6 <br> 
             <br> License requirements : None */
            public: double TextHeight
            (
            );
            /**Sets  the text height. It is size of text displayed in sketch dimensions. The default is 0.125 
                    NX6 - The text height  preference has been removed from sketches. Each sketch dimension's
                    text height will be controlled via its own annotation preferences.
                    get function -  will always return the annotation preferences- letter prefs- dimension- text height.  
                    set function -  will apply the preference to each dimension in the sketch.
                    The annotation preference can be asked or set by calling the following functions.
                       JA_ANN_GBL_ask_lettering_preferences
                       JA_ANN_GBL_set_lettering_preferences 
             @deprecated Deprecated in NX6 <br> 
             <br> License requirements : None */
            public: void SetTextHeight
            (
                double textHeight /** text height */ 
            );
            /**Returns  the dimension label. Controls how expressions in sketch dimensions are displayed  <br> License requirements : None */
            public: NXOpen::Preferences::SketchPreferences::DimensionLabelType DimensionLabel
            (
            );
            /**Sets  the dimension label. Controls how expressions in sketch dimensions are displayed  <br> License requirements : None */
            public: void SetDimensionLabel
            (
                NXOpen::Preferences::SketchPreferences::DimensionLabelType dimensionLabel /** dimension label */ 
            );
            /** Applies sketch preferences set by user.  <br> License requirements : None */
            public: void ApplySketchPreferences
            (
                int dimDisplayFlag /** dim display flag */ 
            );
            /**Returns  the toggle that controls whether objects are displayed in their actual color in sketch  <br> License requirements : None */
            public: bool DisplayObjectColor
            (
            );
            /**Sets  the toggle that controls whether objects are displayed in their actual color in sketch  <br> License requirements : solid_modeling ("SOLIDS MODELING") OR drafting ("DRAFTING") */
            public: void SetDisplayObjectColor
            (
                bool displayObjectColor /** display object color */ 
            );
            /**Returns  the create inferred constraints. Controls whether to create inferred constraints <br> License requirements : None */
            public: bool CreateInferredConstraints
            (
            );
            /**Sets  the create inferred constraints. Controls whether to create inferred constraints <br> License requirements : solid_modeling ("SOLIDS MODELING") OR drafting ("DRAFTING") */
            public: void SetCreateInferredConstraints
            (
                bool createInferredConstraints /** create inferred constraints */ 
            );
            /**Returns  the text size fixed. Controls whether to fix text size <br> License requirements : None */
            public: bool TextSizeFixed
            (
            );
            /**Sets  the text size fixed. Controls whether to fix text size <br> License requirements : solid_modeling ("SOLIDS MODELING") OR drafting ("DRAFTING") */
            public: void SetTextSizeFixed
            (
                bool textSizeFixed /** text size fixed */ 
            );
            /**Returns  the fixed text size.  It is the visible dimension size when text size fixed is enabled.  <br> License requirements : None */
            public: double FixedTextSize
            (
            );
            /**Sets  the fixed text size.  It is the visible dimension size when text size fixed is enabled.  <br> License requirements : solid_modeling ("SOLIDS MODELING") OR drafting ("DRAFTING") */
            public: void SetFixedTextSize
            (
                double fixedTextSize /** fixed text size */ 
            );
            public: virtual void initialize();
        };
    }
}
#undef EXPORTLIBRARY
#endif