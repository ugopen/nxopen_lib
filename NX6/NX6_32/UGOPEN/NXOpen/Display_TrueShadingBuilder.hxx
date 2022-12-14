#ifndef NXOpen_DISPLAY_TRUESHADINGBUILDER_HXX_INCLUDED
#define NXOpen_DISPLAY_TRUESHADINGBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Display_TrueShadingBuilder.ja
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
#include <NXOpen/Builder.hxx>
#include <NXOpen/Display_TrueShadingBuilder.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Display
    {
        class TrueShadingBuilder;
    }
    class Builder;
    class Plane;
    class SelectNXObjectList;
    namespace Display
    {
        class _TrueShadingBuilderBuilder;
        /** Represents a @link Display::TrueShading Display::TrueShading@endlink  builder  <br> To create a new instance of this class, use @link Display::TrueShadingCollection::CreateTrueShadingBuilder Display::TrueShadingCollection::CreateTrueShadingBuilder@endlink  <br> */
        class NXOPENCPPEXPORT TrueShadingBuilder : public Builder
        {
            /** Global material and per object overriding material types */
            public: enum MaterialType
            {
                MaterialTypeGlobalWashShinyMetal/** Shiny Metal Wash */,
                MaterialTypeGlobalWashBrushedMetal/** Brushed Metal Wash */,
                MaterialTypeGlobalWashShinyPlastic/** Shiny Plastic Wash */,
                MaterialTypeGlobalWashAnalysis/** Surface Analysis Wash */,
                MaterialTypeGlobalWashFlat/** Low Sheen Plastic Wash */,
                MaterialTypeGlobalRedGlossyPlastic/** Red Glossy Plastic */,
                MaterialTypeGlobalBlueGlossyPlastic/** Blue Glossy Plastic */,
                MaterialTypeGlobalGreenGlossyPlastic/** Green Glossy Plastic */,
                MaterialTypeGlobalGrayGlossyPlastic/** Gray Glossy Plastic */,
                MaterialTypeGlobalBlackGlossyPlastic/** Black Glossy Plastic */,
                MaterialTypeGlobalBrownGlossyPlastic/** Brown Glossy Plastic */,
                MaterialTypeGlobalYellowGlossyPlastic/** Yellow Glossy Plastic */,
                MaterialTypeGlobalTealGlossyPlastic/** Teal Glossy Plastic */,
                MaterialTypeGlobalWhiteGlossyPlastic/** White Glossy Plastic */,
                MaterialTypeGlobalClearPlastic/** Clear Plastic */,
                MaterialTypeGlobalChrome/** Chrome */,
                MaterialTypeGlobalCopper/** Copper */,
                MaterialTypeGlobalGold/** Gold */,
                MaterialTypeGlobalBrass/** Brass */,
                MaterialTypeGlobalSteel/** Steel */,
                MaterialTypeGlobalBrushedChrome/** Brushed Chrome */,
                MaterialTypeGlobalBrushedAluminum/** Brushed Aluminum */,
                MaterialTypeGlobalBrushedTitanium/** Brushed Titanium */,
                MaterialTypeGlobalGlassClear/** Clear Glass */,
                MaterialTypeGlobalGlassSmokey/** Smokey Glass */,
                MaterialTypeGlobalMetallicPaintRed/** Red Metallic Paint */,
                MaterialTypeGlobalMetallicPaintGray/** Gray Metallic Paint */,
                MaterialTypeGlobalMetallicPaintBlack/** Black Metallic Paint */,
                MaterialTypeGlobalMetallicPaintBlue/** Blue Metallic Paint */,
                MaterialTypeGlobalRubber/** Black Rubber */,
                MaterialTypeOverrideRedGlossyPlastic/** Red Glossy Plastic */,
                MaterialTypeOverrideBlueGlossyPlastic/** Blue Glossy Plastic */,
                MaterialTypeOverrideGreenGlossyPlastic/** Green Glossy Plastic */,
                MaterialTypeOverrideGrayGlossyPlastic/** Gray Glossy Plastic */,
                MaterialTypeOverrideBlackGlossyPlastic/** Black Glossy Plastic */,
                MaterialTypeOverrideBrownGlossyPlastic/** Brown Glossy Plastic */,
                MaterialTypeOverrideYellowGlossyPlastic/** Yellow Glossy Plastic */,
                MaterialTypeOverrideTealGlossyPlastic/** Teal Glossy Plastic */,
                MaterialTypeOverrideWhiteGlossyPlastic/** White Glossy Plastic */,
                MaterialTypeOverrideClearPlastic/** Clear Plastic */,
                MaterialTypeOverrideChrome/** Chrome */,
                MaterialTypeOverrideCopper/** Copper */,
                MaterialTypeOverrideGold/** Gold */,
                MaterialTypeOverrideBrass/** Brass */,
                MaterialTypeOverrideSteel/** Steel */,
                MaterialTypeOverrideBrushedChrome/** Brushed Chrome */,
                MaterialTypeOverrideBrushedAluminum/** Brushed Aluminum */,
                MaterialTypeOverrideBrushedTitanium/** Brushed Titanium */,
                MaterialTypeOverrideGlassClear/** Clear Glass */,
                MaterialTypeOverrideGlassSmokey/** Smokey Glass */,
                MaterialTypeOverrideMetallicPaintRed/** Red Metallic Paint */,
                MaterialTypeOverrideMetallicPaintGray/** Gray Metallic Paint */,
                MaterialTypeOverrideMetallicPaintBlack/** Black Metallic Paint */,
                MaterialTypeOverrideMetallicPaintBlue/** Blue Metallic Paint */,
                MaterialTypeOverrideRubber/** Black Rubber */,
                MaterialTypeOverrideRoughMetalMedGray/** Medium Grey Texture */,
                MaterialTypeOverrideRoughMetalDkGray/** Dark Grey Texture */,
                MaterialTypeOverrideRoughPlasticBlueGray/** Blue Grey Texture */,
                MaterialTypeOverrideRoughPlasticTan/** Tan Texture */
            };

            /** Global environment reflection map types */
            public: enum EnvironmentMapType
            {
                EnvironmentMapTypeDefault/** No reflection map */,
                EnvironmentMapTypeMetalShiny1/** Shiny Metal Reflection 1 */,
                EnvironmentMapTypeMetalShiny2/** Shiny Metal Reflection 2 */,
                EnvironmentMapTypeMetalBrushed1/** Brushed Metal Reflection 1 */,
                EnvironmentMapTypeMetalBrushed2/** Brushed Metal Reflection 2 */,
                EnvironmentMapTypeGlossy1/** Glossy Reflection 1 */,
                EnvironmentMapTypeGlossy2/** Glossy Reflection 2 */,
                EnvironmentMapTypeSurfaceAnalysisLines/** Surface Analysis Lines Reflection */,
                EnvironmentMapTypeSurfaceAnalysisHorizon/** Surface Analysis Horizontal Lines Reflection */,
                EnvironmentMapTypeAutoPhotoStudio/** Automotive Lighting Reflection */,
                EnvironmentMapTypeCustomImage/** Custom Image Reflection */
            };

            /** Background colors and image types */
            public: enum BgdType
            {
                BgdTypeDarkGraduated/** Graduated dark colored background */,
                BgdTypeLightGraduated/** Graduated light colored background */,
                BgdTypeBlack/** Plain dark Colored background */,
                BgdTypeWhite/** Plain light Colored background */,
                BgdTypeCustomPlain/** Customized plain colored background */,
                BgdTypeCustomGraduated/** Customized graduated colored background */,
                BgdTypeInheritShadedBackground/** Use same background color as in shaded display mode */,
                BgdTypeImageBackground/** Use one of the predefined images as background */
            };

            /** Background image types */
            public: enum BgdImageType
            {
                BgdImageTypeImage1/** Predefined image 1 background */,
                BgdImageTypeImage2/** Predefined image 2 background */,
                BgdImageTypeImage3/** Predefined image 3 background */,
                BgdImageTypeImage4/** Predefined image 4 background */,
                BgdImageTypeImage5/** Predefined image 5 background */,
                BgdImageTypeImage6/** Predefined image 6 background */,
                BgdImageTypeCustomImage/** Custom image background */
            };

            /** Shadow plane projection orientation types */
            public: enum SurfaceOrientType
            {
                SurfaceOrientTypeNone/** Do not project shadows */,
                SurfaceOrientTypeBottom/** Project shadows onto the floor */,
                SurfaceOrientTypeBack/** Project shadows onto the back wall */
            };

            /** Scene lighting collection types */
            public: enum SHEDLightCollectionType
            {
                SHEDLightCollectionTypeDefaultLights/** Scene lighting collection 1 */,
                SHEDLightCollectionTypeLighting1/** Scene lighting collection 2 */,
                SHEDLightCollectionTypeLighting2/** Scene lighting collection 3 */,
                SHEDLightCollectionTypeLighting3/** Scene lighting collection 4 */,
                SHEDLightCollectionTypeLighting4/** Scene lighting collection 5 */,
                SHEDLightCollectionTypeCustom/** Custom lighting configuration */
            };

            private: friend class  _TrueShadingBuilderBuilder;
            protected: TrueShadingBuilder();
            /**Returns  the True Shading display toggle state  <br> License requirements : None */
            public: bool ShedModeToggle
            (
            );
            /**Sets  the True Shading display toggle state  <br> License requirements : None */
            public: void SetShedModeToggle
            (
                bool shedModeToggle /** shedmodetoggle */ 
            );
            /**Returns  the globalMaterialType  <br> License requirements : None */
            public: NXOpen::Display::TrueShadingBuilder::MaterialType GlobalMaterialType
            (
            );
            /**Sets  the globalMaterialType  <br> License requirements : None */
            public: void SetGlobalMaterialType
            (
                NXOpen::Display::TrueShadingBuilder::MaterialType globalMaterialType /** globalmaterialtype */ 
            );
            /** Assigns an overriding material type to one or more selected objects  <br> License requirements : None */
            public: void AssignOverrideMaterial
            (
                NXOpen::Display::TrueShadingBuilder::MaterialType overrideMaterialType /** New material type */
            );
            /** Global material button 1  <br> License requirements : None */
            public: void GButton0
            (
            );
            /** Global material button 2  <br> License requirements : None */
            public: void GButton1
            (
            );
            /** Global material button 3  <br> License requirements : None */
            public: void GButton2
            (
            );
            /** Global material button 4  <br> License requirements : None */
            public: void GButton3
            (
            );
            /** Global material button 5  <br> License requirements : None */
            public: void GButton4
            (
            );
            /** Global material button 6  <br> License requirements : None */
            public: void GButton5
            (
            );
            /** Global material button 7  <br> License requirements : None */
            public: void GButton6
            (
            );
            /** Global material button 8  <br> License requirements : None */
            public: void GButton7
            (
            );
            /** Global material button 9  <br> License requirements : None */
            public: void GButton8
            (
            );
            /** Global material button 10  <br> License requirements : None */
            public: void GButton9
            (
            );
            /** Global material button 11  <br> License requirements : None */
            public: void GButton10
            (
            );
            /** Global material button 12  <br> License requirements : None */
            public: void GButton11
            (
            );
            /** Global material button 13  <br> License requirements : None */
            public: void GButton12
            (
            );
            /** Global material button 14  <br> License requirements : None */
            public: void GButton13
            (
            );
            /** Global material button 15  <br> License requirements : None */
            public: void GButton14
            (
            );
            /** Global material button 16  <br> License requirements : None */
            public: void GButton15
            (
            );
            /** Global material button 17  <br> License requirements : None */
            public: void GButton16
            (
            );
            /** Global material button 18  <br> License requirements : None */
            public: void GButton17
            (
            );
            /** Global material button 19  <br> License requirements : None */
            public: void GButton18
            (
            );
            /** Global material button 20  <br> License requirements : None */
            public: void GButton19
            (
            );
            /** Global material button 21  <br> License requirements : None */
            public: void GButton20
            (
            );
            /** Global material button 22  <br> License requirements : None */
            public: void GButton21
            (
            );
            /** Global material button 23  <br> License requirements : None */
            public: void GButton22
            (
            );
            /** Global material button 24  <br> License requirements : None */
            public: void GButton23
            (
            );
            /** Global material button 25  <br> License requirements : None */
            public: void GButton24
            (
            );
            /** Global material button 26  <br> License requirements : None */
            public: void GButton25
            (
            );
            /** Global material button 27  <br> License requirements : None */
            public: void GButton26
            (
            );
            /** Global material button 28  <br> License requirements : None */
            public: void GButton27
            (
            );
            /** Global material button 29  <br> License requirements : None */
            public: void GButton28
            (
            );
            /** Global material button 30  <br> License requirements : None */
            public: void GButton29
            (
            );
            /** Per Object override material button 1  <br> License requirements : None */
            public: void OButton0
            (
            );
            /** Per Object override material button 2  <br> License requirements : None */
            public: void OButton1
            (
            );
            /** Per Object override material button 3  <br> License requirements : None */
            public: void OButton2
            (
            );
            /** Per Object override material button 4  <br> License requirements : None */
            public: void OButton3
            (
            );
            /** Per Object override material button 5  <br> License requirements : None */
            public: void OButton4
            (
            );
            /** Per Object override material button 6  <br> License requirements : None */
            public: void OButton5
            (
            );
            /** Per Object override material button 7  <br> License requirements : None */
            public: void OButton6
            (
            );
            /** Per Object override material button 8  <br> License requirements : None */
            public: void OButton7
            (
            );
            /** Per Object override material button 9  <br> License requirements : None */
            public: void OButton8
            (
            );
            /** Per Object override material button 10  <br> License requirements : None */
            public: void OButton9
            (
            );
            /** Per Object override material button 11  <br> License requirements : None */
            public: void OButton10
            (
            );
            /** Per Object override material button 12  <br> License requirements : None */
            public: void OButton11
            (
            );
            /** Per Object override material button 13  <br> License requirements : None */
            public: void OButton12
            (
            );
            /** Per Object override material button 14  <br> License requirements : None */
            public: void OButton13
            (
            );
            /** Per Object override material button 15  <br> License requirements : None */
            public: void OButton14
            (
            );
            /** Per Object override material button 16  <br> License requirements : None */
            public: void OButton15
            (
            );
            /** Per Object override material button 17  <br> License requirements : None */
            public: void OButton16
            (
            );
            /** Per Object override material button 18  <br> License requirements : None */
            public: void OButton17
            (
            );
            /** Per Object override material button 19  <br> License requirements : None */
            public: void OButton18
            (
            );
            /** Per Object override material button 20  <br> License requirements : None */
            public: void OButton19
            (
            );
            /** Per Object override material button 21  <br> License requirements : None */
            public: void OButton20
            (
            );
            /** Per Object override material button 22  <br> License requirements : None */
            public: void OButton21
            (
            );
            /** Per Object override material button 23  <br> License requirements : None */
            public: void OButton22
            (
            );
            /** Per Object override material button 24  <br> License requirements : None */
            public: void OButton23
            (
            );
            /** Per Object override material button 25  <br> License requirements : None */
            public: void OButton24
            (
            );
            /** Per Object override material button 26  <br> License requirements : None */
            public: void OButton25
            (
            );
            /** Per Object override material button 27  <br> License requirements : None */
            public: void OButton26
            (
            );
            /** Per Object override material button 28  <br> License requirements : None */
            public: void OButton27
            (
            );
            /** Per Object override material button 29  <br> License requirements : None */
            public: void OButton28
            (
            );
            /** Removes override material from selected object(s)  <br> License requirements : None */
            public: void ORemoveButton
            (
            );
            /**Returns  the selected object(s) list   <br> License requirements : None */
            public: NXOpen::SelectNXObjectList * ObjSpecificSelection
            (
            );
            /**Returns  the reflection environment map enum type  <br> License requirements : None */
            public: NXOpen::Display::TrueShadingBuilder::EnvironmentMapType EnvironmentMapEnum
            (
            );
            /**Sets  the reflection environment map enum type  <br> License requirements : None */
            public: void SetEnvironmentMapEnum
            (
                NXOpen::Display::TrueShadingBuilder::EnvironmentMapType environmentMapEnum /** environmentmapenum */ 
            );
            /**Returns  the reflection environment map filename  <br> License requirements : None */
            public: NXString EnvironmentMapFileBrowser
            (
            );
            /**Sets  the reflection environment map filename  <br> License requirements : None */
            public: void SetEnvironmentMapFileBrowser
            (
                const NXString & filename /** filename */ 
            );
            /**Returns  the background color or background image type enum  <br> License requirements : None */
            public: NXOpen::Display::TrueShadingBuilder::BgdType BgdTypeEnum
            (
            );
            /**Sets  the background color or background image type enum  <br> License requirements : None */
            public: void SetBgdTypeEnum
            (
                NXOpen::Display::TrueShadingBuilder::BgdType bgdTypeEnum /** bgdtypeenum */ 
            );
            /** Returns the RGB values of background top color picker  @return  Array of 3 RGB values, each between 0 and 1  <br> License requirements : None */
            public: std::vector<double> GetBgdTopRgbcolorPicker
            (
            );
            /** Sets the RGB values of background top color picker  <br> License requirements : None */
            public: void SetBgdTopRgbcolorPicker
            (
                const std::vector<double> & bgdTopRGBColorPicker /** Array of 3 RGB values, each between 0 and 1 */
            );
            /** Returns the RGB values of background bottom color picker  @return  Array of 3 RGB values, each between 0 and 1  <br> License requirements : None */
            public: std::vector<double> GetBgdBottomRgbcolorPicker
            (
            );
            /** Sets the RGB values of background bottom color picker  <br> License requirements : None */
            public: void SetBgdBottomRgbcolorPicker
            (
                const std::vector<double> & bgdBottomRGBColorPicker /** Array of 3 RGB values, each between 0 and 1 */
            );
            /**Returns  the background image list enum  <br> License requirements : None */
            public: NXOpen::Display::TrueShadingBuilder::BgdImageType BgdImageEnum
            (
            );
            /**Sets  the background image list enum  <br> License requirements : None */
            public: void SetBgdImageEnum
            (
                NXOpen::Display::TrueShadingBuilder::BgdImageType bgdImageEnum /** bgdimageenum */ 
            );
            /**Returns  the background image filename  <br> License requirements : None */
            public: NXString BgdImageFileBrowser
            (
            );
            /**Sets  the background image filename  <br> License requirements : None */
            public: void SetBgdImageFileBrowser
            (
                const NXString & filename /** filename */ 
            );
            /**Returns  the shadow plane surface orientation enum  <br> License requirements : None */
            public: NXOpen::Display::TrueShadingBuilder::SurfaceOrientType SurfaceOrientEnum
            (
            );
            /**Sets  the shadow plane surface orientation enum  <br> License requirements : None */
            public: void SetSurfaceOrientEnum
            (
                NXOpen::Display::TrueShadingBuilder::SurfaceOrientType surfaceOrientEnum /** surfaceorientenum */ 
            );
            /**Returns  the custom plane definition for the shadow projection  <br> License requirements : None */
            public: NXOpen::Plane * SpecifyPlane
            (
            );
            /**Sets  the custom plane definition for the shadow projection  <br> License requirements : None */
            public: void SetSpecifyPlane
            (
                NXOpen::Plane * specifyPlane /** specifyplane */ 
            );
            /**Returns  the offset distance between the shadow plane and the nearest vertex of the displayed object  <br> License requirements : None */
            public: double PlaneOffsetValue
            (
            );
            /**Sets  the offset distance between the shadow plane and the nearest vertex of the displayed object  <br> License requirements : None */
            public: void SetPlaneOffsetValue
            (
                double planeOffsetValue /** planeoffsetvalue */ 
            );
            /**Returns  the shadow plane grid visibility toggle  <br> License requirements : None */
            public: bool PlaneGridToggle
            (
            );
            /**Sets  the shadow plane grid visibility toggle  <br> License requirements : None */
            public: void SetPlaneGridToggle
            (
                bool planeGridToggle /** planegridtoggle */ 
            );
            /** Returns the grid RGB color values picker  @return  Array of 3 RGB values, each between 0 and 1  <br> License requirements : None */
            public: std::vector<double> GetGridRgbcolorPicker
            (
            );
            /** Sets the grid RGB color picker  <br> License requirements : None */
            public: void SetGridRgbcolorPicker
            (
                const std::vector<double> & gridRGBColorPicker /** Array of 3 RGB values, each between 0 and 1 */
            );
            /**Returns  the toggle forces the shadow plane to snap to the nearest object vertex  <br> License requirements : None */
            public: bool SnapFloorToggle
            (
            );
            /**Sets  the toggle forces the shadow plane to snap to the nearest object vertex  <br> License requirements : None */
            public: void SetSnapFloorToggle
            (
                bool snapFloorToggle /** snapfloortoggle */ 
            );
            /**Returns  the planar shadow visibility toggle  <br> License requirements : None */
            public: bool PlanarShadowToggle
            (
            );
            /**Sets  the planar shadow visibility toggle  <br> License requirements : None */
            public: void SetPlanarShadowToggle
            (
                bool planarShadowToggle /** planarshadowtoggle */ 
            );
            /**Returns  the soft shadows toggle  <br> License requirements : None */
            public: bool SoftShadowsToggle
            (
            );
            /**Sets  the soft shadows toggle  <br> License requirements : None */
            public: void SetSoftShadowsToggle
            (
                bool softShadowsToggle /** softshadowstoggle */ 
            );
            /**Returns  the planar reflection visibility toggle  <br> License requirements : None */
            public: bool PlanarReflectionToggle
            (
            );
            /**Sets  the planar reflection visibility toggle  <br> License requirements : None */
            public: void SetPlanarReflectionToggle
            (
                bool planarReflectionToggle /** planarreflectiontoggle */ 
            );
            /**Returns  the reflectivity value  <br> License requirements : None */
            public: double ReflectivityValue
            (
            );
            /**Sets  the reflectivity value  <br> License requirements : None */
            public: void SetReflectivityValue
            (
                double reflectivityValue /** reflectivityvalue */ 
            );
            /**Returns  the light collection enum  <br> License requirements : None */
            public: NXOpen::Display::TrueShadingBuilder::SHEDLightCollectionType LightCollectionEnum
            (
            );
            /**Sets  the light collection enum  <br> License requirements : None */
            public: void SetLightCollectionEnum
            (
                NXOpen::Display::TrueShadingBuilder::SHEDLightCollectionType lightCollectionEnum /** lightcollectionenum */ 
            );
            /**Returns  the light dimmer value  <br> License requirements : None */
            public: double LightDimmerValue
            (
            );
            /**Sets  the light dimmer value  <br> License requirements : None */
            public: void SetLightDimmerValue
            (
                double lightDimmerValue /** lightdimmervalue */ 
            );
            /** the function to protect update  <br> License requirements : None */
            public: void ProtectUpdate
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
