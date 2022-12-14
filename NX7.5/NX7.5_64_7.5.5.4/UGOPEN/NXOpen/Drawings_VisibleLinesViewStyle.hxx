#ifndef NXOpen_DRAWINGS_VISIBLELINESVIEWSTYLE_HXX_INCLUDED
#define NXOpen_DRAWINGS_VISIBLELINESVIEWSTYLE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Drawings_VisibleLinesViewStyle.ja
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
#include <NXOpen/Preferences_IVisibleLinesViewPreferences.hxx>
#include <NXOpen/Preferences_ViewStylePreferencesData.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Drawings
    {
        class VisibleLinesViewStyle;
    }
    namespace Drawings
    {
        class ViewStyle;
    }
    namespace Preferences
    {
        class IVisibleLinesViewPreferences;
    }
    namespace Drawings
    {
        class VisibleLinesViewStyleImpl;
        /** Represents set of Visible Lines View Style Preferences applicable to drafting views.  <br> To obtain an instance of this class use @link Drawings::ViewStyle::VisibleLines Drawings::ViewStyle::VisibleLines@endlink  <br> */
        class NXOPENCPPEXPORT  VisibleLinesViewStyle: public virtual Preferences::IVisibleLinesViewPreferences
        {
            private: VisibleLinesViewStyleImpl * m_visiblelinesviewstyle_impl;
            private: NXOpen::Drawings::ViewStyle* m_owner;
            /** Constructor */
            public: explicit VisibleLinesViewStyle(NXOpen::Drawings::ViewStyle *owner);
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~VisibleLinesViewStyle();
            /**Returns  the visible color. The value should be between 1 and 216.  <br> License requirements : None */
            public: int VisibleColor
            (
            );
            /**Sets  the visible color. The value should be between 1 and 216.  <br> License requirements : drafting ("DRAFTING") */
            public: void SetVisibleColor
            (
                int visibleColor /** visible color */ 
            );
            /**Returns  the visible font. <br> License requirements : None */
            public: NXOpen::Preferences::Font VisibleFont
            (
            );
            /**Sets  the visible font. <br> License requirements : drafting ("DRAFTING") */
            public: void SetVisibleFont
            (
                NXOpen::Preferences::Font visibleFont /** visible font */ 
            );
            /**Returns  the visible width. <br> License requirements : None */
            public: NXOpen::Preferences::Width VisibleWidth
            (
            );
            /**Sets  the visible width. <br> License requirements : drafting ("DRAFTING") */
            public: void SetVisibleWidth
            (
                NXOpen::Preferences::Width visibleWidth /** visible width */ 
            );
        }; //lint !e1712 default constructor not defined for class  

    }
}
#undef EXPORTLIBRARY
#endif
