#ifndef NXOpen_DIE_DRAWDIEPUNCHSECTIONBUILDER_HXX_INCLUDED
#define NXOpen_DIE_DRAWDIEPUNCHSECTIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Die_DrawDiePunchSectionBuilder.ja
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
#include <NXOpen/Die.hxx>
#include <NXOpen/Features_FeatureBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Die
    {
        class DrawDiePunchSectionBuilder;
    }
    class Expression;
    namespace Features
    {
        class FeatureBuilder;
    }
    namespace Die
    {
        class _DrawDiePunchSectionBuilderBuilder;
        class DrawDiePunchSectionBuilderImpl;
        /** Represents a Draw Die Punch Section sub feature.  <br> This sub feature is created via the main feature builder. <br> */
        class NXOPENCPPEXPORT  DrawDiePunchSectionBuilder : public Features::FeatureBuilder
        {
            private: DrawDiePunchSectionBuilderImpl * m_drawdiepunchsectionbuilder_impl;
            private: friend class  _DrawDiePunchSectionBuilderBuilder;
            protected: DrawDiePunchSectionBuilder();
            public: ~DrawDiePunchSectionBuilder();
            /**  <br> License requirements : ug_die_design ("Die Design") */
            public: void SetReliefDistance
            (
                double reliefDistance /** relief distance */ 
            );
            /**Returns  the relief distance of the draw die punch casting.  <br> License requirements : ug_die_design ("Die Design") */
            public: double ReliefDistance
            (
            );
            /**  <br> License requirements : ug_die_design ("Die Design") */
            public: void SetDeckThickness
            (
                double deckThickness /** deck thickness */ 
            );
            /**Returns  the deck thickness of the draw die punch casting.  <br> License requirements : ug_die_design ("Die Design") */
            public: double DeckThickness
            (
            );
            /**  <br> License requirements : ug_die_design ("Die Design") */
            public: void SetWallThickness
            (
                double wallThickness /** wall thickness */ 
            );
            /**Returns  the wall thickness of the draw die punch casting.  <br> License requirements : ug_die_design ("Die Design") */
            public: double WallThickness
            (
            );
            /**  <br> License requirements : ug_die_design ("Die Design") */
            public: void SetBaseThickness
            (
                double baseThickness /** base thickness */ 
            );
            /**Returns  the base thickness of the draw die punch casting.  <br> License requirements : ug_die_design ("Die Design") */
            public: double BaseThickness
            (
            );
            /**  <br> License requirements : ug_die_design ("Die Design") */
            public: void SetBaseWidth
            (
                double baseWidth /** base width */ 
            );
            /**Returns  the base width of the draw die punch casting.  <br> License requirements : ug_die_design ("Die Design") */
            public: double BaseWidth
            (
            );
            /**  <br> License requirements : ug_die_design ("Die Design") */
            public: void SetPartialRibHeight
            (
                double partialRibHeight /** partial rib height */ 
            );
            /**Returns  the partial rib height of the draw die punch casting.  <br> License requirements : ug_die_design ("Die Design") */
            public: double PartialRibHeight
            (
            );
            /**  <br> License requirements : ug_die_design ("Die Design") */
            public: void SetOffsetProfileToTop
            (
                double offsetProfileToTop /** offset profile to top */ 
            );
            /**Returns  the offset profile to top distance of the draw die punch casting.  <br> License requirements : ug_die_design ("Die Design") */
            public: double OffsetProfileToTop
            (
            );
            /**  <br> License requirements : ug_die_design ("Die Design") */
            public: void SetReliefAngle
            (
                double reliefAngle /** relief angle */ 
            );
            /**Returns  the relief angle of the draw die punch casting.  <br> License requirements : ug_die_design ("Die Design") */
            public: double ReliefAngle
            (
            );
            /**  <br> License requirements : ug_die_design ("Die Design") */
            public: void SetBeltThickness
            (
                const NXString & beltThickness /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /**Returns  the belt thickness of the draw die punch casting.  <br> License requirements : ug_die_design ("Die Design") */
            public: NXOpen::Expression * BeltThickness
            (
            );
            /**  <br> License requirements : ug_die_design ("Die Design") */
            public: void SetDesignStatus
            (
                bool designStatus /** design status */ 
            );
            /**Returns  the design status of the draw die punch casting, if true the casting will be built into the model, if false it will not.  <br> License requirements : ug_die_design ("Die Design") */
            public: bool DesignStatus
            (
            );
            /**Returns  the build status of the draw die punch casting.  <br> License requirements : ug_die_design ("Die Design") */
            public: NXOpen::Die::DieBuildStatusOption BuildStatus
            (
            );
            /**  <br> License requirements : ug_die_design ("Die Design") */
            public: void SetDisplayStatus
            (
                bool displayStatus /** display status */ 
            );
            /**Returns  the display status of the draw die punch casting, if true input data to the draw die punch casting will be displayed, 
                    if false the input data will not be displayed.  <br> License requirements : ug_die_design ("Die Design") */
            public: bool DisplayStatus
            (
            );
            /** Gets the forming faces attributes.  <br> License requirements : ug_die_design ("Die Design") */
            public: void GetFormingAttributes
            (
                NXString* title /** Title for attribute. */,
                NXString* value /** Value of attribute. */,
                int* color /** Color of forming faces. */
            );
            /** Sets the forming faces attributes.  <br> License requirements : ug_die_design ("Die Design") */
            public: void SetFormingAttributes
            (
                const NXString & title /** Title for attribute.   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                const NXString & value /** Value of attribute.   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                int color /** Color of forming faces. */
            );
            /** Gets the belt wall faces attributes.  <br> License requirements : ug_die_design ("Die Design") */
            public: void GetBeltWallAttributes
            (
                NXString* title /** Title for attribute. */,
                NXString* value /** Value of attribute. */,
                int* color /** Color of belt wall faces. */
            );
            /** Sets the belt wall faces attributes.  <br> License requirements : ug_die_design ("Die Design") */
            public: void SetBeltWallAttributes
            (
                const NXString & title /** Title for attribute.   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                const NXString & value /** Value of attribute.   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                int color /** Color of belt wall faces. */
            );
            /** Gets the base faces attributes.  <br> License requirements : ug_die_design ("Die Design") */
            public: void GetBaseAttributes
            (
                NXString* title /** Title for attribute. */,
                NXString* value /** Value of attribute. */,
                int* color /** Color of base faces. */
            );
            /** Sets the base faces attributes.  <br> License requirements : ug_die_design ("Die Design") */
            public: void SetBaseAttributes
            (
                const NXString & title /** Title for attribute.   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                const NXString & value /** Value of attribute.   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                int color /** Color of base faces. */
            );
            /** Gets the punch profile edges attributes.  <br> License requirements : ug_die_design ("Die Design") */
            public: void GetPunchProfileAttributes
            (
                NXString* title /** Title for attribute. */,
                NXString* value /** Value of attribute. */
            );
            /** Sets the punch profile edges attributes.  <br> License requirements : ug_die_design ("Die Design") */
            public: void SetPunchProfileAttributes
            (
                const NXString & title /** Title for attribute.   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                const NXString & value /** Value of attribute.   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
