#ifndef NXOpen_VISUALREPORTING_GROUPLABEL_HXX_INCLUDED
#define NXOpen_VISUALREPORTING_GROUPLABEL_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     VisualReporting_GroupLabel.ja
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
#include <NXOpen/NXColor.hxx>
#include <NXOpen/NXObject.hxx>
#include <NXOpen/VisualReporting_GroupLabel.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace VisualReporting
    {
        class GroupLabel;
    }
    class NXObject;
    namespace VisualReporting
    {
        class _GroupLabelBuilder;
        class GroupLabelImpl;
        /**
                A group label corresponds to a group of objects in the results of an applied 
                @link VisualReporting::VisualReport VisualReporting::VisualReport@endlink .
            */
        class NXOPENCPPEXPORT  GroupLabel : public NXObject
        {
            /** Represents the possible DisplayStyle options.
                        for a group label.
                    */
            public: enum DisplayStyleOption
            {
                DisplayStyleOptionDeEmphasis/** Matching objects will be de-emphasized */,
                DisplayStyleOptionSpecifiedColor/** Matching objects will be shown using @link VisualReporting::GroupLabel::Color VisualReporting::GroupLabel::Color@endlink  */,
                DisplayStyleOptionOriginalColor/** Matching objects will be shown using their original color */,
                DisplayStyleOptionAutomaticColor/** Matching objects will be shown using @link VisualReporting::GroupLabel::Color VisualReporting::GroupLabel::Color@endlink  which is system determined */
            };

            private: GroupLabelImpl * m_grouplabel_impl;
            private: friend class  _GroupLabelBuilder;
            protected: GroupLabel();
            public: ~GroupLabel();
            /**Returns  whether the group label is manual. It is manual if it either has a user-specified
                        @link NXObject::Name NXObject::Name@endlink  or if its @link VisualReporting::GroupLabel::DisplayStyle VisualReporting::GroupLabel::DisplayStyle@endlink  is
                        not @link VisualReporting::GroupLabel::DisplayStyleOptionAutomaticColor VisualReporting::GroupLabel::DisplayStyleOptionAutomaticColor@endlink .
                     <br> License requirements : nx_visual_reporting ("Visual Reporting") */
            public: bool IsManual
            (
            );
            /**Returns  whether the group label has a user-specified @link NXObject::Name NXObject::Name@endlink . If it isn't
                        user-specified, then the system will generate its name automatically.
                     <br> License requirements : nx_visual_reporting ("Visual Reporting") */
            public: bool IsNameUserSpecified
            (
            );
            /**Returns  the lower-bound of the group label (if it is being grouped by range)  <br> License requirements : nx_visual_reporting ("Visual Reporting") */
            public: double LowerBound
            (
            );
            /**Returns  the upper-bound value of the group label (if it is being grouped by range)  <br> License requirements : nx_visual_reporting ("Visual Reporting") */
            public: double UpperBound
            (
            );
            /**Returns  the value of the group label (if it is being grouped by value)  <br> License requirements : nx_visual_reporting ("Visual Reporting") */
            public: NXString Value
            (
            );
            /**Returns  the @link VisualReporting::GroupLabel::DisplayStyleOption VisualReporting::GroupLabel::DisplayStyleOption@endlink  of the group label  <br> License requirements : nx_visual_reporting ("Visual Reporting") */
            public: NXOpen::VisualReporting::GroupLabel::DisplayStyleOption DisplayStyle
            (
            );
            /**Sets  the @link VisualReporting::GroupLabel::DisplayStyleOption VisualReporting::GroupLabel::DisplayStyleOption@endlink  of the group label  <br> License requirements : nx_visual_reporting ("Visual Reporting") */
            public: void SetDisplayStyle
            (
                NXOpen::VisualReporting::GroupLabel::DisplayStyleOption displayStyle /** displaystyle */ 
            );
            /**Returns  the color of the group label  <br> License requirements : nx_visual_reporting ("Visual Reporting") */
            public: NXOpen::NXColor::Rgb Color
            (
            );
            /**Sets  the color of the group label  <br> License requirements : nx_visual_reporting ("Visual Reporting") */
            public: void SetColor
            (
                const NXOpen::NXColor::Rgb & color /** color */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
