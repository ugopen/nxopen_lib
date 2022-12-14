#ifndef NXOpen_PREFERENCES_SESSIONVISUALIZATIONVISUAL_HXX_INCLUDED
#define NXOpen_PREFERENCES_SESSIONVISUALIZATIONVISUAL_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Preferences_SessionVisualizationVisual.ja
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
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/ugmath.hxx>
#include <NXOpen/libnxopenuicpp_exports.hxx>

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
        class SessionVisualizationVisual;
    }
    class UI;
    class View;
    namespace Preferences
    {
        class SessionVisualizationVisualImpl;
        /** Represents all UI based session Visualization visual preferences  <br> To obtain an instance of this class, refer to @link NXOpen::UI  NXOpen::UI @endlink  <br> 
         <br>  Created in NX3.0.0.  <br>  
        */
        class NXOPENUICPPEXPORT  SessionVisualizationVisual
        {
            private: SessionVisualizationVisualImpl * m_sessionvisualizationvisual_impl;
            private: NXOpen::UI* m_owner;
            /// \cond NX_NO_DOC 
            public: explicit SessionVisualizationVisual(NXOpen::UI *owner);


            /// \endcond 
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~SessionVisualizationVisual();
            /**Returns  the translucency flag. True value specifies that each shaded object is drawn with the translucency setting 
                specified with Edit-\>Object Display. False value specify that all objects in Fully Shaded or Partially Shaded 
                views appear opaque, regardless of their individual translucency settings.  
             <br>  Created in NX3.0.0.  <br>  
             <br> License requirements : None */
            public: bool Translucency
            (
            );
            /**Sets  the translucency flag. True value specifies that each shaded object is drawn with the translucency setting 
                specified with Edit-\>Object Display. False value specify that all objects in Fully Shaded or Partially Shaded 
                views appear opaque, regardless of their individual translucency settings.  
             <br>  Created in NX3.0.0.  <br>  
             <br> License requirements : None */
            public: void SetTranslucency
            (
                bool translucency /** translucency */ 
            );
            /**Returns  the line antialiasing flag. True value specifies that lines, curves, and edges are drawn more smoothly 
             <br>  Created in NX3.0.0.  <br>  
             <br> License requirements : None */
            public: bool LineAntialiasing
            (
            );
            /**Sets  the line antialiasing flag. True value specifies that lines, curves, and edges are drawn more smoothly 
             <br>  Created in NX3.0.0.  <br>  
             <br> License requirements : None */
            public: void SetLineAntialiasing
            (
                bool lineAntialiasing /** line antialiasing */ 
            );
            /**Returns  the scene antialiasing flag. 
             <br>  Created in NX3.0.0.  <br>  
             <br> License requirements : None */
            public: bool FullSceneAntialiasing
            (
            );
            /**Sets  the scene antialiasing flag. 
             <br>  Created in NX3.0.0.  <br>  
             <br> License requirements : None */
            public: void SetFullSceneAntialiasing
            (
                bool fullSceneAntialiasing /** full scene antialiasing */ 
            );
            /**Returns  the reduce edge bleed-through flag.
                    True indicates that Show Line Widths, Edge Emphasis, and Line Antialising settings
                    are overriden so as to minimize the effects of edges bleeding through surfaces. 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: bool ReduceEdgeBleedThrough
            (
            );
            /**Sets  the reduce edge bleed-through flag.
                    True indicates that Show Line Widths, Edge Emphasis, and Line Antialising settings
                    are overriden so as to minimize the effects of edges bleeding through surfaces. 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: void SetReduceEdgeBleedThrough
            (
                bool reduceEdgeBleedThrough /** reduce edge bleed through */ 
            );

            /// \cond NX_NO_DOC 
            /** If specified screen coordinates are contained in a displayed view,
                    returns the view and the corresponding view coordinates. Otherwise,
                    returns NULL. Supported for Windows systems only. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: void GetViewFromPoint
            (
                int screenX /** screenx */ ,
                int screenY /** screeny */ ,
                NXOpen::View ** view /** view */ ,
                NXOpen::Point3d* viewPoint /** viewpoint */ 
            );

            /// \endcond 
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
