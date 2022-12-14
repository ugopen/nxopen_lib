#ifndef NXOpen_LIGHT_HXX_INCLUDED
#define NXOpen_LIGHT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Light.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/NXObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    class Light;
    class NXObject;
    class View;
    class _LightBuilder;
    /**
     Represents a light source.
     <br> Creation of lights is not supported yet. <br> */
    class NXOPENCPPEXPORT Light : public NXObject
    {
        /**
             The type of a light.  For now, you can only modify lights of type
             JA_LIGHT_light_type_scene via automation languages.
            */
        public: enum LightType
        {
            LightTypeAmbient/** An ambient light provides global illumination
                                                     for the scene.  It does not cause shadows, and illuminates
                                                     all objects equally regardless of the orientation. You can
                                                     control the intensity and color. */,
            LightTypeDistant/** A distant light can be thought of as being
                                                     located for all practical purposes infinitely far away,
                                                     such as the sun.  You can control the intensity, color,
                                                     and a vector that defines the direction of the light.
                                                     A distant light can cast shadows in High Quality Images
                                                     and requires the computation to determine shadowing. */,
            LightTypeEye/** An eye light is Located at the viewpoint or directly
                                                     on the Z axis of the screen. You can control
                                                     the color and intensity.  An eye light cannot cause
                                                     shadows in your scene. */,
            LightTypePoint/** A point light emits light equally in all directions.
                                                     You can specify the location, intensity, and color.
                                                     You can also set it to generate shadows in
                                                     High Quality Images. The default position for
                                                     point lights is in the right-hand corner
                                                     of the view. */,
            LightTypeSpot/** A spot light is the same as a point light,
                                                     except that it is constrained by a cone shape.
                                                     You can specify the location, intensity, and color.
                                                     You can also set it to generate shadows in High Quality
                                                     Images.  The default light source position for spot lights
                                                     is in the upper right corner of the view.  The
                                                     default target position is the center of the view. */,
            LightTypeScene = 6/** A scene lights is a light whose parameters, except for
                                                     intensity, are fixed.  Interactively, these lights
                                                     may be modified only in the Basic Lights dialog,
                                                     while the other light types may be modified only
                                                     in the Advanced Lights dialog. */
        };

        /**
             The predefined scene lights used in Basic Lights.  These are subtypes of
             JA_LIGHT_light_type_scene.  Except for ambient light, all of the other lights
             are on the same side of the model as the observer.
            */
        public: enum SceneType
        {
            SceneTypeNotASceneLight = -1/** The light is not a scene light */,
            SceneTypeAmbient/** Light from all around the model */,
            SceneTypeLeftTop/** Light from the top left of the view */,
            SceneTypeTop/** Light from the top center of the view */,
            SceneTypeRightTop/** Light from the top right of the view */,
            SceneTypeFront/** Light from the front of the view (at
                                                          the observer's location */,
            SceneTypeLeftBottom/** Light from the bottom left of the view */,
            SceneTypeBottom/** Light from the bottom center of the view */,
            SceneTypeRightBottom/** Light from the bottom right of the view */
        };

        private: friend class  _LightBuilder;
        protected: Light();
        /** Whether a light is enabled in a given view.  true means the light is on, 
                false means the light is off.  @return  true: the light is on, false: off  <br> License requirements : None */
        public: bool GetEnabledInView
        (
            NXOpen::View * view /** The view to check */
        );
        /** Whether a light is to be enabled in a given view.  true means
                to turn the light on, false is to turn it off.  For now, the light must be
                of type JA_LIGHT_light_type_scene.  <br> License requirements : None */
        public: void SetEnabledInView
        (
            NXOpen::View * view /** The view to turn the light on or off in */,
            bool on_or_off /** true for on, false for off */
        );
        /**Returns  the intensity of a light.  Intensity is normally in the range of
                0.0 (fully off) to 1.0 (fully on), except that for lights other than
                scene lights, the intensity may be greater than 1.0.
                 <br>  Note that even if the light is not displayed in any view, the
                intensity may still be greater than 0.0, as this intensity will be used
                the next time the light is turned on.  <br> 
                 <br>  For now, JA_LIGHT_set_intensity may only be used for
                a scene light.  <br>  <br> License requirements : None */
        public: double Intensity
        (
        );
        /**Sets  the intensity of a light.  Intensity is normally in the range of
                0.0 (fully off) to 1.0 (fully on), except that for lights other than
                scene lights, the intensity may be greater than 1.0.
                 <br>  Note that even if the light is not displayed in any view, the
                intensity may still be greater than 0.0, as this intensity will be used
                the next time the light is turned on.  <br> 
                 <br>  For now, JA_LIGHT_set_intensity may only be used for
                a scene light.  <br>  <br> License requirements : None */
        public: void SetIntensity
        (
            double intensity /** */
        );
        /** Get the type of a light.  If the light is a scene light, the specific type
                of scene light is also returned.  It the light is not a scene light, the
                scene_light_type output is undefined.  <br> License requirements : None */
        public: void GetLightType
        (
            NXOpen::Light::LightType* light_type /** the type of light */,
            NXOpen::Light::SceneType* scene_light_type /** is light_type is ...scene,
                                                                    this is the specific type of
                                                                    scene light */
        );
    };
}
#undef EXPORTLIBRARY
#endif
