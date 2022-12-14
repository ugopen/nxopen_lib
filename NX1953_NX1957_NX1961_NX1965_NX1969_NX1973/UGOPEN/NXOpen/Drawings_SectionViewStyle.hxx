#ifndef NXOpen_DRAWINGS_SECTIONVIEWSTYLE_HXX_INCLUDED
#define NXOpen_DRAWINGS_SECTIONVIEWSTYLE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Drawings_SectionViewStyle.ja
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
#include <NXOpen/Preferences_ISectionViewPreferences.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_drawings_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Drawings
    {
        class SectionViewStyle;
    }
    namespace Drawings
    {
        class ViewStyle;
    }
    namespace Preferences
    {
        class ISectionViewPreferences;
    }
    namespace Drawings
    {
        class SectionViewStyleImpl;
        /** Represents set of Section View Style Preferences applicable to drafting views.  <br> To obtain an instance of this class use @link Drawings::ViewStyle::Section Drawings::ViewStyle::Section@endlink   <br> 
         <br>  Created in NX5.0.0.  <br>  
        */
        class NXOPENCPP_DRAWINGSEXPORT  SectionViewStyle: public virtual NXOpen::Preferences::ISectionViewPreferences
        {
            private: SectionViewStyleImpl * m_sectionviewstyle_impl;
            private: NXOpen::Drawings::ViewStyle* m_owner;
            /// \cond NX_NO_DOC 
            public: explicit SectionViewStyle(NXOpen::Drawings::ViewStyle *owner);


            /// \endcond 
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~SectionViewStyle();
            /**Sets  the status of background. Suppress or display the background curves for a section view. If True,
                        not only the curves and crosshatching generated by cutting the solid are displayed, 
                        but the curves behind the cutting plane are displayed as well. If False, only the curves and 
                        crosshatching generated by cutting the solid are displayed in the view.
                     
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetBackground
            (
                bool background /** background */ 
            );
            /**Returns  the status of background. Suppress or display the background curves for a section view. If True,
                        not only the curves and crosshatching generated by cutting the solid are displayed, 
                        but the curves behind the cutting plane are displayed as well. If False, only the curves and 
                        crosshatching generated by cutting the solid are displayed in the view.
                     
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: bool Background
            (
            );
            /**Sets  the status of foreground 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetForeground
            (
                bool foreground /** foreground */ 
            );
            /**Returns  the status of foreground 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: bool Foreground
            (
            );
            /**Sets  the status of bendlines 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetBendlines
            (
                bool bendlines /** bendlines */ 
            );
            /**Returns  the status of bendlines 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: bool Bendlines
            (
            );
            /**Sets  the status of section sheet bodies. Allows sectioning of sheet bodies in a Section view. 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetSectionSheetBodies
            (
                bool sectionSheetBodies /** section sheet bodies */ 
            );
            /**Returns  the status of section sheet bodies. Allows sectioning of sheet bodies in a Section view. 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: bool SectionSheetBodies
            (
            );
            /**Sets  the status of cross hatch. Allows to control whether or not crosshatching is generated in 
                        a given section view. If True, crosshatching is displayed for a section view on the drawing, 
                        else crosshatching is not generated for a section view on the drawing, and a performance 
                        increase is gained.
                     
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetCrossHatch
            (
                bool crossHatch /** cross hatch */ 
            );
            /**Returns  the status of cross hatch. Allows to control whether or not crosshatching is generated in 
                        a given section view. If True, crosshatching is displayed for a section view on the drawing, 
                        else crosshatching is not generated for a section view on the drawing, and a performance 
                        increase is gained.
                     
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: bool CrossHatch
            (
            );
            /**Sets  the status of hidden line hatching. Controls whether hatching for a Break-Out
                        or Pictorial Section view participates in hidden line processing. When it is True for a break-out section view, 
                        the only hatch style available is iron (equally spaced solid lines).  <br> 
                        Works when @link Drawings::SectionViewStyle::CrossHatch Drawings::SectionViewStyle::CrossHatch@endlink  is True.  <br> 
                     
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetHiddenLineHatching
            (
                bool hiddenLineHatching /** hidden line hatching */ 
            );
            /**Returns  the status of hidden line hatching. Controls whether hatching for a Break-Out
                        or Pictorial Section view participates in hidden line processing. When it is True for a break-out section view, 
                        the only hatch style available is iron (equally spaced solid lines).  <br> 
                        Works when @link Drawings::SectionViewStyle::CrossHatch Drawings::SectionViewStyle::CrossHatch@endlink  is True.  <br> 
                     
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: bool HiddenLineHatching
            (
            );
            /**Sets  the status of assembly cross hatching. Controls the crosshatching angle
                        of adjacent solids in an assembly section view. <br> 
                        Works when @link Drawings::SectionViewStyle::CrossHatch Drawings::SectionViewStyle::CrossHatch@endlink  is True. <br> 
                     
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetAssemblyCrossHatching
            (
                bool assemblyCrossHatching /** assembly cross hatching */ 
            );
            /**Returns  the status of assembly cross hatching. Controls the crosshatching angle
                        of adjacent solids in an assembly section view. <br> 
                        Works when @link Drawings::SectionViewStyle::CrossHatch Drawings::SectionViewStyle::CrossHatch@endlink  is True. <br> 
                     
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: bool AssemblyCrossHatching
            (
            );
            /**Sets   
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetRestrictCrosshatchAngle
            (
                bool restrictCrosshatchAngle /** restrict crosshatch angle */ 
            );
            /**Returns   
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: bool RestrictCrosshatchAngle
            (
            );
            /**Sets  the value of crosshatch adjacency tolarance. Controls the crosshatching angle of adjacent 
                        solids in an assembly section view. <br> 
                        Works when @link Drawings::SectionViewStyle::AssemblyCrossHatching Drawings::SectionViewStyle::AssemblyCrossHatching@endlink  is True. <br> 
                     
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetCrosshatchAdjacencyTolarance
            (
                double crosshatchAdjacencyTolarance /** crosshatch adjacency tolarance */ 
            );
            /**Returns  the value of crosshatch adjacency tolarance. Controls the crosshatching angle of adjacent 
                        solids in an assembly section view. <br> 
                        Works when @link Drawings::SectionViewStyle::AssemblyCrossHatching Drawings::SectionViewStyle::AssemblyCrossHatching@endlink  is True. <br> 
                     
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: double CrosshatchAdjacencyTolarance
            (
            );
            /**Sets  the status of display section line. Suppress or display the sectio line in a section view.
                     
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetDisplaySectionLine
            (
                bool displaySectionLine /** display section line */ 
            );
            /**Returns  the status of display section line. Suppress or display the sectio line in a section view.
                     
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: bool DisplaySectionLine
            (
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
