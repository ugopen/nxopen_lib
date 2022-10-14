#ifndef NXOpen_PREFERENCES_VIRTUALINTERSECTIONSVIEWPREFERENCES_HXX_INCLUDED
#define NXOpen_PREFERENCES_VIRTUALINTERSECTIONSVIEWPREFERENCES_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Preferences_VirtualIntersectionsViewPreferences.ja
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
#include <NXOpen/Preferences_IVirtualIntersectionsViewPreferences.hxx>
#include <NXOpen/Preferences_ViewStylePreferencesData.hxx>
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
        class VirtualIntersectionsViewPreferences;
    }
    namespace Preferences
    {
        class ViewPreferences;
    }
    namespace Preferences
    {
        class IVirtualIntersectionsViewPreferences;
    }
    namespace Preferences
    {
        class VirtualIntersectionsViewPreferencesImpl;
        /** Represents set of Virtual Intersections View Preferences applicable to drafting views. 
                Allows to display imaginary intersection curves.
              <br> To obtain an instance of this class use @link Preferences::ViewPreferences::VirtualIntersections Preferences::ViewPreferences::VirtualIntersections@endlink   <br> 
         <br>  Created in NX5.0.0.  <br>  
        */
        class NXOPENCPP_PREFERENCESEXPORT  VirtualIntersectionsViewPreferences: public virtual Preferences::IVirtualIntersectionsViewPreferences
        {
            private: VirtualIntersectionsViewPreferencesImpl * m_virtualintersectionsviewpreferences_impl;
            private: NXOpen::Preferences::ViewPreferences* m_owner;
            /// \cond NX_NO_DOC 
            public: explicit VirtualIntersectionsViewPreferences(NXOpen::Preferences::ViewPreferences *owner);


            /// \endcond 
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~VirtualIntersectionsViewPreferences();
            /**Sets  the status of virtual intersection.
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetVirtualIntersection
            (
                bool virtualIntersection /** virtual intersection */ 
            );
            /**Returns  the status of virtual intersection.
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: bool VirtualIntersection
            (
            );
            /**Sets  the status of adjacent blends.
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetAdjacentBlends
            (
                bool adjacentBlends /** adjacent blends */ 
            );
            /**Returns  the status of adjacent blends.
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: bool AdjacentBlends
            (
            );
            /**Sets  the color of adjacent blends. The value should be between 1 and 216.
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetAdjacentBlendsColor
            (
                int adjacentBlendsColor /** adjacent blends color */ 
            );
            /**Returns  the color of adjacent blends. The value should be between 1 and 216.
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: int AdjacentBlendsColor
            (
            );
            /**Sets  the font of adjacent blends.
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetAdjacentBlendsFont
            (
                NXOpen::Preferences::Font adjacentBlendsFont /** adjacent blends font */ 
            );
            /**Returns  the font of adjacent blends.
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Preferences::Font AdjacentBlendsFont
            (
            );
            /**Sets  the width of adjacent blends.
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetAdjacentBlendsWidth
            (
                NXOpen::Preferences::Width adjacentBlendsWidth /** adjacent blends width */ 
            );
            /**Returns  the width of adjacent blends.
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Preferences::Width AdjacentBlendsWidth
            (
            );
            /**Sets  the status of adjacent blends end gaps. It controls the display of visible ends. If True, the 
                        visible ends are suppressed from the display. The length of the suppressed end is in drawing 
                        units and is controlled by the value set in the End Gap field. If False, the visible ends are 
                        not suppressed from the display.
                     
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetAdjacentBlendsEndGaps
            (
                bool adjacentBlendsEndGaps /** adjacent blends end gaps */ 
            );
            /**Returns  the status of adjacent blends end gaps. It controls the display of visible ends. If True, the 
                        visible ends are suppressed from the display. The length of the suppressed end is in drawing 
                        units and is controlled by the value set in the End Gap field. If False, the visible ends are 
                        not suppressed from the display.
                     
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: bool AdjacentBlendsEndGaps
            (
            );
            /**Sets  the value of adjacent blends end gaps.
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetAdjacentBlendsEndGapsData
            (
                double adjacentBlendsEndGapsData /** adjacent blends end gaps data */ 
            );
            /**Returns  the value of adjacent blends end gaps.
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: double AdjacentBlendsEndGapsData
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