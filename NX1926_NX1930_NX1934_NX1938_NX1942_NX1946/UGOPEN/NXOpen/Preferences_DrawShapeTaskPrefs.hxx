#ifndef NXOpen_PREFERENCES_DRAWSHAPETASKPREFS_HXX_INCLUDED
#define NXOpen_PREFERENCES_DRAWSHAPETASKPREFS_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Preferences_DrawShapeTaskPrefs.ja
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
#include <NXOpen/DisplayableObject.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_preferences_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Preferences
    {
        class DrawShapeTaskPrefs;
    }
    namespace Preferences
    {
        class SessionPreferences;
    }
    class NXColor;
    namespace Preferences
    {
        class DrawShapeTaskPrefsImpl;
        /** Represents the set of Draw Shape preferences applicable to entire session <br> To obtain an instance of this class, refer to @link NXOpen::Preferences::SessionPreferences  NXOpen::Preferences::SessionPreferences @endlink  <br> 
         <br>  Created in NX1926.0.0.  <br>  
        */
        class NXOPENCPP_PREFERENCESEXPORT  DrawShapeTaskPrefs
        {
            private: DrawShapeTaskPrefsImpl * m_drawshapetaskprefs_impl;
            private: NXOpen::Preferences::SessionPreferences* m_owner;
            /// \cond NX_NO_DOC 
            public: explicit DrawShapeTaskPrefs(NXOpen::Preferences::SessionPreferences *owner);


            /// \endcond 
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~DrawShapeTaskPrefs();
            /**Returns  the Stroke thickness. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::DisplayableObject::ObjectWidth StrokeThickness
            (
            );
            /**Sets  the Stroke thickness. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_draw_shape (" NX Draw Shape Functionality") */
            public: void SetStrokeThickness
            (
                NXOpen::DisplayableObject::ObjectWidth thickenss /** thickenss */ 
            );
            /**Returns  the Stroke color. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::NXColor * StrokeColor
            (
            );
            /**Sets  the Stroke color. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_draw_shape (" NX Draw Shape Functionality") */
            public: void SetStrokeColor
            (
                NXOpen::NXColor * color /** color */ 
            );
            /**Returns  the Curve thickness. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::DisplayableObject::ObjectWidth CurveThickness
            (
            );
            /**Sets  the Curve thickness. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_draw_shape (" NX Draw Shape Functionality") */
            public: void SetCurveThickness
            (
                NXOpen::DisplayableObject::ObjectWidth thickenss /** thickenss */ 
            );
            /**Returns  the Curve color. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::NXColor * CurveColor
            (
            );
            /**Sets  the Curve color. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_draw_shape (" NX Draw Shape Functionality") */
            public: void SetCurveColor
            (
                NXOpen::NXColor * color /** color */ 
            );
            /**Returns  the Mirror Curve font. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::DisplayableObject::ObjectFont SymmetryCurveFont
            (
            );
            /**Sets  the Mirror Curve font. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_draw_shape (" NX Draw Shape Functionality") */
            public: void SetSymmetryCurveFont
            (
                NXOpen::DisplayableObject::ObjectFont font /** font */ 
            );
        }; //lint !e1712 default constructor not defined for class  

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