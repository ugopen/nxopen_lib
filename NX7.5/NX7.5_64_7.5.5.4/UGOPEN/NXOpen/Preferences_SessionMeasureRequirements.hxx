#ifndef NXOpen_PREFERENCES_SESSIONMEASUREREQUIREMENTS_HXX_INCLUDED
#define NXOpen_PREFERENCES_SESSIONMEASUREREQUIREMENTS_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Preferences_SessionMeasureRequirements.ja
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
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Preferences
    {
        class SessionMeasureRequirements;
    }
    namespace Preferences
    {
        class SessionPreferences;
    }
    namespace Preferences
    {
        class SessionMeasureRequirementsImpl;
        /** Represents the two options available on the Measure Requirements toolbar and applicable to the entire session  <br> To obtain an instance of this class, refer to @link Preferences::SessionPreferences Preferences::SessionPreferences@endlink  <br> */
        class NXOPENCPPEXPORT  SessionMeasureRequirements
        {
            /** Values for the action to take when a requirement error is generated for a measure with a displayed
                annotation in Assembly Sequencing.
            */
            public: enum ActionOnViolation
            {
                ActionOnViolationHightlightMeasure/** Highlight (color) measure for requirements violations */,
                ActionOnViolationStopPlayback/** Suspend playback and wait for acknowledgement for requirements violations */
            };

            private: SessionMeasureRequirementsImpl * m_sessionmeasurerequirements_impl;
            private: NXOpen::Preferences::SessionPreferences* m_owner;
            /** Constructor */
            public: explicit SessionMeasureRequirements(NXOpen::Preferences::SessionPreferences *owner);
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~SessionMeasureRequirements();
            /**Returns  the frame rate.  The frame rate specifies how frequently a displayed measure annotation is updated in Assembly Sequencing.
            So a rate of 1 specifies that the annotation will update every frame during playback.
            A rate of 5 specifies that the annotation will update every fifth frame during playback.  <br> License requirements : None */
            public: int UpdateFrameRate
            (
            );
            /**Sets  the frame rate.  The frame rate specifies how frequently a displayed measure annotation is updated in Assembly Sequencing.
            So a rate of 1 specifies that the annotation will update every frame during playback.
            A rate of 5 specifies that the annotation will update every fifth frame during playback.  <br> License requirements : None */
            public: void SetUpdateFrameRate
            (
                int frameRate /** an integer \> 0 */
            );
            /**Returns  the violation action.  The violation action is one of the enumerated type values.  <br> License requirements : None */
            public: NXOpen::Preferences::SessionMeasureRequirements::ActionOnViolation ViolationAction
            (
            );
            /**Sets  the violation action.  The violation action is one of the enumerated type values.  <br> License requirements : None */
            public: void SetViolationAction
            (
                NXOpen::Preferences::SessionMeasureRequirements::ActionOnViolation violationAction /** violation action */ 
            );
        }; //lint !e1712 default constructor not defined for class  

    }
}
#undef EXPORTLIBRARY
#endif