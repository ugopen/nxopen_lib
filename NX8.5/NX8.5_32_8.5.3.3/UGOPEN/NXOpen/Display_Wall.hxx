#ifndef NXOpen_DISPLAY_WALL_HXX_INCLUDED
#define NXOpen_DISPLAY_WALL_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Display_Wall.ja
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
#include <NXOpen/Builder.hxx>
#include <NXOpen/Display_Image.hxx>
#include <NXOpen/Display_Wall.hxx>
#include <NXOpen/libnxopencpp_display_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Display
    {
        class Wall;
    }
    class Builder;
    namespace Display
    {
        class Image;
    }
    namespace Display
    {
        class _WallBuilder;
        class WallImpl;
        /**
            Represents a @link Display::Wall Display::Wall@endlink 
             <br> This class is restricted to being called from a program running during an 
            Interactive NX session.  If run from a non-interactive session it will 
            return NULL. <br> 
             <br> To create a new instance of this class, use @link ViewCollection::CreateWall  ViewCollection::CreateWall @endlink  <br> 
         <br>  Created in NX5.0.0.  <br>  
        */
        class NXOPENCPP_DISPLAYEXPORT  Wall : public Builder
        {
            /** Defines the material characteristics of a stage wall.
                    */
            public: enum MaterialType
            {
                MaterialTypeShadowCatcher/** The wall is transparent, and is used to display
                                                                              shadows.  Use this to cast shadows onto a "virtual"
                                                                              background image of an environment. */,
                MaterialTypeReflective/** The wall is reflective.  For example, use this on
                                                                              a "bottom" wall to display a shiny floor. */,
                MaterialTypeInvisible/** The wall is not displayed.  For example, use this
                                                                              on all the walls except the "bottom" if you only
                                                                              need to display a floor. */
            };

            private: WallImpl * m_wall_impl;
            private: friend class  _WallBuilder;
            protected: Wall();
            public: ~Wall();
            /**Returns  the wall material type - either shadow_catcher, reflective, or invisible 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Display::Wall::MaterialType WallMaterialType
            (
            );
            /**Sets  the wall material type - either shadow_catcher, reflective, or invisible 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void SetWallMaterialType
            (
                NXOpen::Display::Wall::MaterialType wallMaterialType /** wallmaterialtype */ 
            );
            /**Returns  the pattern repeat factor - the number of times the image repeats 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: double PatternRepeatFactor
            (
            );
            /**Sets  the pattern repeat factor - the number of times the image repeats 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void SetPatternRepeatFactor
            (
                double patternRepeatFactor /** patternrepeatfactor */ 
            );
            /**Returns  the reflectivity of a wall - the percentage of the environment reflected off of the wall 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: double Reflectivity
            (
            );
            /**Sets  the reflectivity of a wall - the percentage of the environment reflected off of the wall 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void SetReflectivity
            (
                double reflectivity /** reflectivity */ 
            );
            /**Returns  the walls's image builder 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Display::Image * Image
            (
            );
            /**Sets  the walls's image builder 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void SetImage
            (
                NXOpen::Display::Image * imageBuilder /** image builder */ 
            );
            /**Returns  the stage wall's image filename 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXString ImageFilename
            (
            );
            /**Sets  the stage wall's image filename 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void SetImageFilename
            (
                const NXString & newImageFileName /** new image file name */ 
            );
            /**Sets  the stage wall's image filename 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            void SetImageFilename
            (
                const char * newImageFileName /** new image file name */ 
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
