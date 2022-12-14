#ifndef NXOpen_PREFERENCES_PARTOBJECT_HXX_INCLUDED
#define NXOpen_PREFERENCES_PARTOBJECT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Preferences_PartObject.ja
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
#include <NXOpen/Preferences_ViewVisualizationSpecialEffects.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Preferences
    {
        class PartObject;
    }
    namespace Preferences
    {
        class PartPreferences;
    }
    namespace Preferences
    {
        /** Represents the set of object preferences applicable to entire part. All the preferences available at 
            UG GUI for object can be set by using this class except work layer. Work Layer should be set by using 
            @link Layer::LayerManager Layer::LayerManager@endlink  class which holds a work layer property.  <br> To obtain an instance of this class, refer to @link Preferences::PartPreferences Preferences::PartPreferences@endlink  <br> */
        class NXOPENCPPEXPORT PartObject
        {
            /** Describes whether color of object is not changed or it is default color or it is defined by user */
            public: enum ColorSelection
            {
                ColorSelectionNoChange/** No Change */,
                ColorSelectionDefaultColor/** Default Color */,
                ColorSelectionColor/** User Defined Color */
            };

            /** Describes all available Types for object selection */
            public: enum ObjectType
            {
                ObjectTypeGeneral/** Default Type Value */,
                ObjectTypeLine/** Line */,
                ObjectTypeArc/** Arc */,
                ObjectTypeConic/** Conic */,
                ObjectTypeSpline/** Spline */,
                ObjectTypeSolidbody/** Solid Body */,
                ObjectTypeSheetbody/** Sheet Body */,
                ObjectTypeDatum/** Datum */,
                ObjectTypePoint/** Point */,
                ObjectTypeCoordinateSystem/** Coordinate System */,
                ObjectTypeAllButDefault/** All But Default */,
                ObjectTypeDatumCsys/** Datum CSYS Feature */,
                ObjectTypeTraceline/** Traceline */
            };

            /** Represents the available types for font */
            public: enum LineFontType
            {
                LineFontTypePartDefault = 1/** Default Value from Part*/,
                LineFontTypeSolid/** Solid */,
                LineFontTypeDashed/** Dashed */,
                LineFontTypePhantom/** Phantom */,
                LineFontTypeCenterline/** Centerline */,
                LineFontTypeDotted/** Dotted */,
                LineFontTypeLongDashed/** Long Dashed */,
                LineFontTypeDottedDashed/** Dotted Dashed */
            };

            /** Describes the available types for width */
            public: enum WidthType
            {
                WidthTypePartDefault = 1/** Default Value from Part */,
                WidthTypeThinWidth/** Thin Width */,
                WidthTypeNormalWidth/** Normal Width */,
                WidthTypeThickWidth/** Thick Width */
            };

            private: NXOpen::Preferences::PartPreferences* m_owner;
            public: explicit PartObject(NXOpen::Preferences::PartPreferences *owner): m_owner(owner)
            {
            }
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            /** Returns the current color value for specified type. 
                    The equivalent RGB values can be found by calling 
                    @link ConvertColorNumberToRGBValue ConvertColorNumberToRGBValue@endlink 

                    Red Component is ((((216 - color_number) % 36)/6)* 51)
                    Green component is (((216 - color_number)/36) * 51)
                    Blue is (((216 - color_number) % 6)* 51). 
                    So for example if returned color value is 47 then 
                    Red is ((((216 - 47) % 36)/6)* 51) = (((169 % 36)/6)* 51) = ((25/6)* 51) = 4*51 = 204
                    Green is (((216 - 47)/36) * 51) = ((169/36) * 51) = 4*51 = 204
                    Blue is (((216 - 47) % 6)* 51) = ((169 % 6)* 51) = 1*51 = 51
                     @return    <br> License requirements : None */
            public: int GetColor
            (
                NXOpen::Preferences::PartObject::ObjectType type /** type */ 
            );
            /** Sets the color. For Default color pass -2 as color value and for no change pass -1. 
                    For other color calculate the color in RGB format.  
                    If you pass R value of Red component G value of Green and B value of Blue the color will be:
                    color = (((255-R)/51)*6 + ((255-G)/51)*36 + ((255-B)/51)*1) + 1 ;
                    Where R G and B values are between 0 and 255 . So for Green (0,255,0)we will pass
                    color = (((255-0)/51)*6 + ((255-255)/51)*36 + ((255-0)/51)*1) + 1 = 30+0+5+1 = 36
                    The equivalent color number value can be found by calling 
                    @link ConvertRGBValueToColorNumber ConvertRGBValueToColorNumber@endlink 
                     <br> License requirements : None */
            public: void SetColor
            (
                NXOpen::Preferences::PartObject::ObjectType type /** type */ ,
                int color /** Specified Color */
            );
            /** Returns the current line font for specified object type  @return    <br> License requirements : None */
            public: NXOpen::Preferences::PartObject::LineFontType GetLineFont
            (
                NXOpen::Preferences::PartObject::ObjectType type /** type */ 
            );
            /** Sets line font for specified object type  <br> License requirements : None */
            public: void SetLineFont
            (
                NXOpen::Preferences::PartObject::ObjectType type /** type */ ,
                NXOpen::Preferences::PartObject::LineFontType line_font /** line font */ 
            );
            /** Returns the current width for specified object type  @return    <br> License requirements : None */
            public: NXOpen::Preferences::PartObject::WidthType GetWidth
            (
                NXOpen::Preferences::PartObject::ObjectType type /** type */ 
            );
            /** Sets width for specified object type   <br> License requirements : None */
            public: void SetWidth
            (
                NXOpen::Preferences::PartObject::ObjectType type /** type */ ,
                NXOpen::Preferences::PartObject::WidthType width /** width */ 
            );
            /**Returns  the partially shaded flag for Solid and Sheets  <br> License requirements : None */
            public: bool PartiallyShaded
            (
            );
            /** <b>Deprecated</b>:<br>
            &nbsp;&nbsp;&nbsp;Use @link PartiallyShaded() PartiallyShaded@endlink instead.
            @deprecated
            */
            public: bool GetPartiallyShaded
            (
            ) { return this->PartiallyShaded(); }
            /**Sets  the partially shaded flag for Solid and Sheets  <br> License requirements : None */
            public: void SetPartiallyShaded
            (
                bool partially_shaded /** partially shaded */ 
            );
            /**Returns  the face analysis flag for Solid and Sheets  <br> License requirements : None */
            public: bool FaceAnalysis
            (
            );
            /** <b>Deprecated</b>:<br>
            &nbsp;&nbsp;&nbsp;Use @link FaceAnalysis() FaceAnalysis@endlink instead.
            @deprecated
            */
            public: bool GetFaceAnalysis
            (
            ) { return this->FaceAnalysis(); }
            /**Sets  the face analysis flag for Solid and Sheets  <br> License requirements : None */
            public: void SetFaceAnalysis
            (
                bool face_analysis /** face analysis */ 
            );
            /**Returns  the translucency value  <br> License requirements : None */
            public: int Translucency
            (
            );
            /** <b>Deprecated</b>:<br>
            &nbsp;&nbsp;&nbsp;Use @link Translucency() Translucency@endlink instead.
            @deprecated
            */
            public: int GetTranslucency
            (
            ) { return this->Translucency(); }
            /**Sets  the translucency value  <br> License requirements : None */
            public: void SetTranslucency
            (
                int translucency /** translucency */ 
            );
            /** Converts color number to RGB constituents. The color number passed should be between 1 to 216  @return  Equivalent RGB constituents  <br> License requirements : None */
            public: NXOpen::Preferences::ViewVisualizationSpecialEffects::ColorRGB ConvertColorNumberToRGBValue
            (
                int color_number /** Color value*/
            );
            /** Converts RGB color constituents to color number. The Red, Green and Blue color constituents
                    should be between 0 to 255.  @return  Equivalent color value  <br> License requirements : None */
            public: int ConvertRGBValueToColorNumber
            (
                const NXOpen::Preferences::ViewVisualizationSpecialEffects::ColorRGB & fog_color_rgb_value /** fog color rgb value */ 
            );
            public: virtual void initialize();
        };
    }
}
#undef EXPORTLIBRARY
#endif
