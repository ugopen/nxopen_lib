#ifndef NXOpen_PREFERENCES_PARTPREFERENCES_HXX_INCLUDED
#define NXOpen_PREFERENCES_PARTPREFERENCES_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Preferences_PartPreferences.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Preferences
    {
        class PartPreferences;
    }
    class BasePart;
    namespace Preferences
    {
        class DraftingPreferenceManager;
    }
    namespace Preferences
    {
        class PartAeroSheetmetal;
    }
    namespace Preferences
    {
        class PartDrafting;
    }
    namespace Preferences
    {
        class PartFlexiblePrintedCircuitDesign;
    }
    namespace Preferences
    {
        class PartModeling;
    }
    namespace Preferences
    {
        class PartObject;
    }
    namespace Preferences
    {
        class PartSheetmetal;
    }
    namespace Preferences
    {
        class PartSketch;
    }
    namespace Preferences
    {
        class PartUserInterface;
    }
    namespace Preferences
    {
        class PartVisualizationColorSetting;
    }
    namespace Preferences
    {
        class PartVisualizationLine;
    }
    namespace Preferences
    {
        class PartVisualizationNamesBorders;
    }
    namespace Preferences
    {
        class PartVisualizationShade;
    }
    namespace Preferences
    {
        class PartVisualizationVisual;
    }
    namespace Preferences
    {
        class WorkPlane;
    }
    namespace Preferences
    {
        /** Represents set of preferences applicable to displayed part.  <br> To obtain an instance of this class, refer to @link BasePart BasePart@endlink  <br> */
        class NXOPENCPPEXPORT PartPreferences
        {
            private: NXOpen::BasePart* m_owner;
            public: explicit PartPreferences(NXOpen::BasePart *owner): m_owner(owner)
            {
            }
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            /**Returns  the workplane preferences.  <br> License requirements : None */
            public: NXOpen::Preferences::WorkPlane * Workplane
            (
            );


            private: NXOpen::Preferences::PartModeling *modeling;
            /** Returns object for doing Modeling preferences settings applicable to displayed part */
            public: NXOpen::Preferences::PartModeling *Modeling()
            {
                return modeling;
            }
            private: NXOpen::Preferences::PartDrafting *drafting;
            /** Returns object for doing Drafting preferences settings applicable to displayed part */
            public: NXOpen::Preferences::PartDrafting *Drafting()
            {
                return drafting;
            }
            private: NXOpen::Preferences::PartObject *objectPreferences;
            /** Returns object for doing object preferences settings applicable to displayed part */
            public: NXOpen::Preferences::PartObject *ObjectPreferences()
            {
                return objectPreferences;
            }
            private: NXOpen::Preferences::PartUserInterface *userInterface;
            /** Returns object for doing User Interface preferences settings applicable to displayed part */
            public: NXOpen::Preferences::PartUserInterface *UserInterface()
            {
                return userInterface;
            }
            private: NXOpen::Preferences::PartVisualizationVisual *visualVisualization;
            /** Returns object for doing Visualization preferences settings for Visual tab applicable to displayed part */
            public: NXOpen::Preferences::PartVisualizationVisual *VisualVisualization()
            {
                return visualVisualization;
            }
            private: NXOpen::Preferences::PartVisualizationLine *lineVisualization;
            /** Returns object for doing Visualization preferences settings for Line tab applicable to displayed part */
            public: NXOpen::Preferences::PartVisualizationLine *LineVisualization()
            {
                return lineVisualization;
            }
            private: NXOpen::Preferences::PartVisualizationNamesBorders *namesBorderVisualization;
            /** Returns object for doing Visualization preferences settings for Names/Border tab applicable to displayed part */
            public: NXOpen::Preferences::PartVisualizationNamesBorders *NamesBorderVisualization()
            {
                return namesBorderVisualization;
            }
            private: NXOpen::Preferences::PartVisualizationColorSetting *colorSettingVisualization;
            /** Returns object for doing Visualization preferences settings for color setting tab applicable to displayed part */
            public: NXOpen::Preferences::PartVisualizationColorSetting *ColorSettingVisualization()
            {
                return colorSettingVisualization;
            }
            private: NXOpen::Preferences::PartVisualizationShade *shadeVisualization;
            /** Returns object for doing Visualization preferences settings for shade tab applicable to displayed part */
            public: NXOpen::Preferences::PartVisualizationShade *ShadeVisualization()
            {
                return shadeVisualization;
            }
            private: NXOpen::Preferences::PartSheetmetal *partSheetmetal;
            /** Returns object to modify the Preference settings for NX Sheetmetal application */
            public: NXOpen::Preferences::PartSheetmetal *PartSheetmetal()
            {
                return partSheetmetal;
            }
            private: NXOpen::Preferences::PartFlexiblePrintedCircuitDesign *partFlexiblePrintedCircuitDesign;
            /** Returns object to modify the Preference settings for Flexible Printed Circuit Design application */
            public: NXOpen::Preferences::PartFlexiblePrintedCircuitDesign *PartFlexiblePrintedCircuitDesign()
            {
                return partFlexiblePrintedCircuitDesign;
            }
            private: NXOpen::Preferences::PartAeroSheetmetal *partAeroSheetmetal;
            /** Returns object to modify the Preference settings for Aerospace Sheetmetal application */
            public: NXOpen::Preferences::PartAeroSheetmetal *PartAeroSheetmetal()
            {
                return partAeroSheetmetal;
            }
            private: NXOpen::Preferences::PartSketch *partSketch;
            /** Returns object to modify the Preference settings for Sketcher application */
            public: NXOpen::Preferences::PartSketch *PartSketch()
            {
                return partSketch;
            }
            private: NXOpen::Preferences::DraftingPreferenceManager *draftingPreference;
            /** Returns object to modify the Preference settings for PMI/drafting application */
            public: NXOpen::Preferences::DraftingPreferenceManager *DraftingPreference()
            {
                return draftingPreference;
            }
            public: virtual void initialize();
        };
    }
}
#undef EXPORTLIBRARY
#endif
