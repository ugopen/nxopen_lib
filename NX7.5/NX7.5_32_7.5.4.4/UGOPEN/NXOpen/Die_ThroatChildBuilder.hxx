#ifndef NXOpen_DIE_THROATCHILDBUILDER_HXX_INCLUDED
#define NXOpen_DIE_THROATCHILDBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Die_ThroatChildBuilder.ja
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
        class ThroatChildBuilder;
    }
    class Expression;
    namespace Features
    {
        class FeatureBuilder;
    }
    namespace Die
    {
        class _ThroatChildBuilderBuilder;
        class ThroatChildBuilderImpl;
        /** Represents a Die Throat Child sub feature.  <br> This sub feature is created via the main feature builder. <br> */
        class NXOPENCPPEXPORT  ThroatChildBuilder : public Features::FeatureBuilder
        {
            /** Settings for the type of the throat section. */
            public: enum TypeOption
            {
                TypeOptionWipe/** Throat section is built for a wipe operation. */,
                TypeOptionRestrike/** Throat section is built for a restrike operation. */
            };

            private: ThroatChildBuilderImpl * m_throatchildbuilder_impl;
            private: friend class  _ThroatChildBuilderBuilder;
            protected: ThroatChildBuilder();
            public: ~ThroatChildBuilder();
            /**  <br> License requirements : ug_die_design ("Die Design") */
            public: void SetSectionPlacement
            (
                const NXString & sectionPlacement /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /**Returns  the throat section placement along the center line, an expression containg the length along the centerline for placement  <br> License requirements : ug_die_design ("Die Design") */
            public: NXOpen::Expression * SectionPlacement
            (
            );
            /**Sets  the radius to be applied at the back of the throat, top and bottom  <br> License requirements : ug_die_design ("Die Design") */
            public: void SetRadius
            (
                double radius /** radius */ 
            );
            /**Returns  the radius to be applied at the back of the throat, top and bottom  <br> License requirements : ug_die_design ("Die Design") */
            public: double Radius
            (
            );
            /**Sets  the step to be applied at the end of the tangent extension of the flange  <br> License requirements : ug_die_design ("Die Design") */
            public: void SetStep
            (
                double step /** step */ 
            );
            /**Returns  the step to be applied at the end of the tangent extension of the flange  <br> License requirements : ug_die_design ("Die Design") */
            public: double Step
            (
            );
            /** Gets the extension attributes, note existance of attributes depends on usage in
                    main feature.  <br> License requirements : ug_die_design ("Die Design") */
            public: void GetExtensionAttributes
            (
                NXString* title /** Title for attribute. */,
                NXString* value /** Value of attribute. */,
                int* color /** Color of extension faces. */
            );
            /** Sets the extension attributes, note existance of attributes depends on usage in
                    main feature.  <br> License requirements : ug_die_design ("Die Design") */
            public: void SetExtensionAttributes
            (
                const NXString & title /** Title for attribute.   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                const NXString & value /** Value of attribute.   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                int color /** Color of extension faces. */
            );
            /** Gets the cavity attributes, note existance of attributes depends on usage in
                    main feature.  <br> License requirements : ug_die_design ("Die Design") */
            public: void GetCavityAttributes
            (
                NXString* title /** Title for attribute. */,
                NXString* value /** Value of attribute. */,
                int* color /** Color of cavity faces. */
            );
            /** Sets the cavity attributes, note existance of attributes depends on usage in
                    main feature.  <br> License requirements : ug_die_design ("Die Design") */
            public: void SetCavityAttributes
            (
                const NXString & title /** Title for attribute.   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                const NXString & value /** Value of attribute.   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                int color /** Color of cavity faces. */
            );
            /**Sets  the design status of the throat section, if true the throat section will be built into the model, if false it will not.  <br> License requirements : ug_die_design ("Die Design") */
            public: void SetDesignStatus
            (
                bool designStatus /** design status */ 
            );
            /**Returns  the design status of the throat section, if true the throat section will be built into the model, if false it will not.  <br> License requirements : ug_die_design ("Die Design") */
            public: bool DesignStatus
            (
            );
            /**Returns  the build status of the throat section.  <br> License requirements : ug_die_design ("Die Design") */
            public: NXOpen::Die::DieBuildStatusOption BuildStatus
            (
            );
            /**Sets  the display status of the throat section, if true input data to the throat section will be displayed,
                    if false the input data will not be displayed.  <br> License requirements : ug_die_design ("Die Design") */
            public: void SetDisplayStatus
            (
                bool displayStatus /** display status */ 
            );
            /**Returns  the display status of the throat section, if true input data to the throat section will be displayed,
                    if false the input data will not be displayed.  <br> License requirements : ug_die_design ("Die Design") */
            public: bool DisplayStatus
            (
            );
            /**  <br> License requirements : ug_die_design ("Die Design") */
            public: void SetExtensionLength
            (
                const NXString & extensionLength /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /**Returns  the tangent distance to add to the end of the flange.
                    An expression containg the length along the tangent.
                    Value is used in both the Wipe and Restrike Flange.  <br> License requirements : ug_die_design ("Die Design") */
            public: NXOpen::Expression * ExtensionLength
            (
            );
            /**  <br> License requirements : ug_die_design ("Die Design") */
            public: void SetStepDistance
            (
                const NXString & stepDistance /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /**Returns  the step distance to add at the end of the tangent extension. The
                    step is at a right angle and only applies to the Wipe Flange. An
                    expression containg the step distance.  <br> License requirements : ug_die_design ("Die Design") */
            public: NXOpen::Expression * StepDistance
            (
            );
            /**  <br> License requirements : ug_die_design ("Die Design") */
            public: void SetUpperRadius
            (
                const NXString & upperRadius /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /**Returns  the radius to apply to the upper corner of the throat cavity.
                    An expression containg the value.
                    Value is used in both the Wipe and Restrike Flange.  <br> License requirements : ug_die_design ("Die Design") */
            public: NXOpen::Expression * UpperRadius
            (
            );
            /**  <br> License requirements : ug_die_design ("Die Design") */
            public: void SetLowerRadius
            (
                const NXString & lowerRadius /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /**Returns  the radius to apply to the lower corner of the throat cavity.
                    Typically, both the lower and the upper radius will be the
                    same. An expression containg the value.
                    Value is used in both the Wipe and Restrike Flange.  <br> License requirements : ug_die_design ("Die Design") */
            public: NXOpen::Expression * LowerRadius
            (
            );
            /**  <br> License requirements : ug_die_design ("Die Design") */
            public: void SetCavityOffset
            (
                const NXString & cavityOffset /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /**Returns  the offset distance measured from the Throat CSYS to the back
                    cavity area of the throat. Both positive and negative values may
                    given to adjust the cavity to the proper location.
                    An expression containg the value.
                    Value is used in both the Wipe and Restrike Flange.  <br> License requirements : ug_die_design ("Die Design") */
            public: NXOpen::Expression * CavityOffset
            (
            );
            /**  <br> License requirements : ug_die_design ("Die Design") */
            public: void SetCavityDepth
            (
                const NXString & cavityDepth /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /**Returns  the distance measured from the bend profile of the flange to the
                    base of the throat. The base of the throat is considered to be
                    the surface the wear plates are mounted on for guiding and aliging
                    the flange steels. The value given must be larger than the
                    minimum cavity depth. An expression containg the value.
                    Value is used in both the Wipe and Restrike Flange.  <br> License requirements : ug_die_design ("Die Design") */
            public: NXOpen::Expression * CavityDepth
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif