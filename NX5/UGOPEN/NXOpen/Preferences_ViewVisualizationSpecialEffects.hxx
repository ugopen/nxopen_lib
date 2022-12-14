#ifndef NXOpen_PREFERENCES_VIEWVISUALIZATIONSPECIALEFFECTS_HXX_INCLUDED
#define NXOpen_PREFERENCES_VIEWVISUALIZATIONSPECIALEFFECTS_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Preferences_ViewVisualizationSpecialEffects.ja
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
        class ViewVisualizationSpecialEffects;
    }
    class View;
    namespace Preferences
    {
        /** Represents the set of visualization special effect preferences applicable to entire session. 
        Mainly sets fog preferences. Fog is the ability to display close objects in shades that are different 
        than those of distant objects resulting in a display that shows which geometry is closest to the 
        viewer and which is furthest.
         <br> To obtain an instance of this class, refer to @link View View@endlink  <br> */
        class NXOPENCPPEXPORT ViewVisualizationSpecialEffects
        {
            /** Describes whether the fog type is selected as linear or light or heavy. */
            public: enum FogType
            {
                FogTypeLinear/** Linear Fog  */,
                FogTypeLight/** Non linear Fog. Light fog produces a fog effect less pervasive than Heavy fog */,
                FogTypeHeavy/** Non linear Fog */
            };

             /** Represents three constituents of a RGB color pattern */
            public:
            struct ColorRGB
            {
                public: /** Red in RGB pattern */double RedColor;
                public: /** Green in RGB pattern */double GreenColor;
                public: /** Blue in RGB pattern */double BlueColor;
                public: ColorRGB() :
                    RedColor(),
                    GreenColor(),
                    BlueColor()
                {
                }
                /** Constructor for the ColorRGB struct. */ 
                public: ColorRGB(double INIT_red_color /** Red in RGB pattern */, double INIT_green_color /** Green in RGB pattern */, double INIT_blue_color /** Blue in RGB pattern */) :
                    RedColor(INIT_red_color),
                    GreenColor(INIT_green_color),
                    BlueColor(INIT_blue_color)
                {
                }
            };

             /** Represents the constituents of fog data */
            public:
            struct FogData
            {
                public: /** Fog mode  */int FogMode;
                public: /** If true fog color is applied to the view */bool FogColorFlag;
                public: /** Fog Color  */NXOpen::Preferences::ViewVisualizationSpecialEffects::ColorRGB FogColor;
                public: /** Start of fog  */double FogStart;
                public: /** End of fog  */double FogEnd;
                public: /** Density of fog  */double FogDensity;
                public: FogData() :
                    FogMode(),
                    FogColorFlag(),
                    FogColor(),
                    FogStart(),
                    FogEnd(),
                    FogDensity()
                {
                }
                /** Constructor for the FogData struct. */ 
                public: FogData(int INIT_fog_mode /** Fog mode  */, bool INIT_fog_color_flag /** If true fog color is applied to the view */, NXOpen::Preferences::ViewVisualizationSpecialEffects::ColorRGB INIT_fog_color /** Fog Color  */, double INIT_fog_start /** Start of fog  */, double INIT_fog_end /** End of fog  */, double INIT_fog_density /** Density of fog  */) :
                    FogMode(INIT_fog_mode),
                    FogColorFlag(INIT_fog_color_flag),
                    FogColor(INIT_fog_color),
                    FogStart(INIT_fog_start),
                    FogEnd(INIT_fog_end),
                    FogDensity(INIT_fog_density)
                {
                }
            };

             /** Represents three constituents of a HSV color pattern */
            public:
            struct ColorHSV
            {
                public: /** Hue in HSV pattern is the color  type (such as red, blue, or yellow) Ranges from 0-360  */double Hue;
                public: /** Saturation in HSV pattern is the "vibrancy" of the color Ranges from 0-255 */double Saturation;
                public: /** Value in HSV pattern is the brightness of the color Ranges from 0-255 */double Value;
                public: ColorHSV() :
                    Hue(),
                    Saturation(),
                    Value()
                {
                }
                /** Constructor for the ColorHSV struct. */ 
                public: ColorHSV(double INIT_hue /** Hue in HSV pattern is the color  type (such as red, blue, or yellow) Ranges from 0-360  */, double INIT_saturation /** Saturation in HSV pattern is the "vibrancy" of the color Ranges from 0-255 */, double INIT_value /** Value in HSV pattern is the brightness of the color Ranges from 0-255 */) :
                    Hue(INIT_hue),
                    Saturation(INIT_saturation),
                    Value(INIT_value)
                {
                }
            };

             /** Represents three constituents of a HLS color pattern */
            public:
            struct ColorHLS
            {
                public: /** Hue in HSV pattern is the color type (such as red, blue, or yellow) Ranges from 0-360 */double Hue;
                public: /** Lightness in HLS pattern Ranges from 0-255 */double Lightness;
                public: /** Saturation in HSV pattern is the "vibrancy" of the color Ranges from 0-255 */double Saturation;
                public: ColorHLS() :
                    Hue(),
                    Lightness(),
                    Saturation()
                {
                }
                /** Constructor for the ColorHLS struct. */ 
                public: ColorHLS(double INIT_hue /** Hue in HSV pattern is the color type (such as red, blue, or yellow) Ranges from 0-360 */, double INIT_lightness /** Lightness in HLS pattern Ranges from 0-255 */, double INIT_saturation /** Saturation in HSV pattern is the "vibrancy" of the color Ranges from 0-255 */) :
                    Hue(INIT_hue),
                    Lightness(INIT_lightness),
                    Saturation(INIT_saturation)
                {
                }
            };

            private: NXOpen::View* m_owner;
            public: explicit ViewVisualizationSpecialEffects(NXOpen::View *owner): m_owner(owner)
            {
            }
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            /**Returns  the fog option. If true fog settings are available and applied to display  <br> License requirements : None */
            public: bool FogSettingOption
            (
            );
            /** <b>Deprecated</b>:<br>
            &nbsp;&nbsp;&nbsp;Use @link FogSettingOption() FogSettingOption@endlink instead.
            @deprecated
            */
            public: bool GetFogSettingOption
            (
            ) { return this->FogSettingOption(); }
            /**Sets  the fog option. If true fog settings are available and applied to display  <br> License requirements : None */
            public: void SetFogSettingOption
            (
                bool fog_setting_option /** fog setting option */ 
            );
            /**Returns  the fog setting type  <br> License requirements : None */
            public: NXOpen::Preferences::ViewVisualizationSpecialEffects::FogType FogSetting
            (
            );
            /** <b>Deprecated</b>:<br>
            &nbsp;&nbsp;&nbsp;Use @link FogSetting() FogSetting@endlink instead.
            @deprecated
            */
            public: NXOpen::Preferences::ViewVisualizationSpecialEffects::FogType GetFogSetting
            (
            ) { return this->FogSetting(); }
            /**Sets  the fog setting type  <br> License requirements : None */
            public: void SetFogSetting
            (
                NXOpen::Preferences::ViewVisualizationSpecialEffects::FogType fog_setting /** fog setting */ 
            );
            /**Returns  the use background color flag. If true background color is used as fog color  <br> License requirements : None */
            public: bool FogBackgroundColor
            (
            );
            /** <b>Deprecated</b>:<br>
            &nbsp;&nbsp;&nbsp;Use @link FogBackgroundColor() FogBackgroundColor@endlink instead.
            @deprecated
            */
            public: bool GetFogBackgroundColor
            (
            ) { return this->FogBackgroundColor(); }
            /**Sets  the use background color flag. If true background color is used as fog color  <br> License requirements : None */
            public: void SetFogBackgroundColor
            (
                bool fog_background_color /** fog background color */ 
            );
            /**Returns  the value of RGB color pattern <br> License requirements : None */
            public: NXOpen::Preferences::ViewVisualizationSpecialEffects::ColorRGB FogColorRGBValue
            (
            );
            /** <b>Deprecated</b>:<br>
            &nbsp;&nbsp;&nbsp;Use @link FogColorRGBValue() FogColorRGBValue@endlink instead.
            @deprecated
            */
            public: NXOpen::Preferences::ViewVisualizationSpecialEffects::ColorRGB GetFogColorRGBValue
            (
            ) { return this->FogColorRGBValue(); }
            /**Sets  the value of RGB color pattern <br> License requirements : None */
            public: void SetFogColorRGBValue
            (
                const NXOpen::Preferences::ViewVisualizationSpecialEffects::ColorRGB & fog_color_rgb_value /** fog color rgb value */ 
            );
            /**Returns  the value of HSV color pattern <br> License requirements : None */
            public: NXOpen::Preferences::ViewVisualizationSpecialEffects::ColorHSV FogColorHSVValue
            (
            );
            /** <b>Deprecated</b>:<br>
            &nbsp;&nbsp;&nbsp;Use @link FogColorHSVValue() FogColorHSVValue@endlink instead.
            @deprecated
            */
            public: NXOpen::Preferences::ViewVisualizationSpecialEffects::ColorHSV GetFogColorHSVValue
            (
            ) { return this->FogColorHSVValue(); }
            /**Sets  the value of HSV color pattern <br> License requirements : None */
            public: void SetFogColorHSVValue
            (
                const NXOpen::Preferences::ViewVisualizationSpecialEffects::ColorHSV & fog_color_hsv_value /** fog color hsv value */ 
            );
            /**Returns  the value of HLS color pattern <br> License requirements : None */
            public: NXOpen::Preferences::ViewVisualizationSpecialEffects::ColorHLS FogColorHLSValue
            (
            );
            /** <b>Deprecated</b>:<br>
            &nbsp;&nbsp;&nbsp;Use @link FogColorHLSValue() FogColorHLSValue@endlink instead.
            @deprecated
            */
            public: NXOpen::Preferences::ViewVisualizationSpecialEffects::ColorHLS GetFogColorHLSValue
            (
            ) { return this->FogColorHLSValue(); }
            /**Sets  the value of HLS color pattern <br> License requirements : None */
            public: void SetFogColorHLSValue
            (
                const NXOpen::Preferences::ViewVisualizationSpecialEffects::ColorHLS & fog_color_hls_value /** fog color hls value */ 
            );
            /**Returns  the fog front scale value. The front scale defines the beginning of fog.  <br> License requirements : None */
            public: int FogFrontValue
            (
            );
            /** <b>Deprecated</b>:<br>
            &nbsp;&nbsp;&nbsp;Use @link FogFrontValue() FogFrontValue@endlink instead.
            @deprecated
            */
            public: int GetFogFrontValue
            (
            ) { return this->FogFrontValue(); }
            /**Sets  the fog front scale value. The front scale defines the beginning of fog.  <br> License requirements : None */
            public: void SetFogFrontValue
            (
                int fog_front_value /** fog front value */ 
            );
            /**Returns  the fog back scale value. The Back scale defines the point at which fog reaches its maximum.  <br> License requirements : None */
            public: int FogBackValue
            (
            );
            /** <b>Deprecated</b>:<br>
            &nbsp;&nbsp;&nbsp;Use @link FogBackValue() FogBackValue@endlink instead.
            @deprecated
            */
            public: int GetFogBackValue
            (
            ) { return this->FogBackValue(); }
            /**Sets  the fog back scale value. The Back scale defines the point at which fog reaches its maximum.  <br> License requirements : None */
            public: void SetFogBackValue
            (
                int fog_back_value /** fog back value */ 
            );
            /**Returns  the fog rate value. Specifies the rate at which an object fades as the distance in the view increases.  <br> License requirements : None */
            public: int FogRateValue
            (
            );
            /** <b>Deprecated</b>:<br>
            &nbsp;&nbsp;&nbsp;Use @link FogRateValue() FogRateValue@endlink instead.
            @deprecated
            */
            public: int GetFogRateValue
            (
            ) { return this->FogRateValue(); }
            /**Sets  the fog rate value. Specifies the rate at which an object fades as the distance in the view increases.  <br> License requirements : None */
            public: void SetFogRateValue
            (
                int fog_rate_value /** fog rate value */ 
            );
            /** Applies current fog settings to display  <br> License requirements : None */
            public: void UpdateFogDisplay
            (
                const NXOpen::Preferences::ViewVisualizationSpecialEffects::FogData & fog_data /** fog data */ 
            );
            public: virtual void initialize();
        };
    }
}
#undef EXPORTLIBRARY
#endif
