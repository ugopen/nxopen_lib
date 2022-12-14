#ifndef NXOpen_PREFERENCES_SESSIONPREFERENCES_HXX_INCLUDED
#define NXOpen_PREFERENCES_SESSIONPREFERENCES_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Preferences_SessionPreferences.ja
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
        class SessionPreferences;
    }
    class Session;
    namespace Preferences
    {
        class RoutingApplicationView;
    }
    namespace Preferences
    {
        class RulePreferences;
    }
    namespace Preferences
    {
        class SessionAssemblies;
    }
    namespace Preferences
    {
        class SessionDrafting;
    }
    namespace Preferences
    {
        class SessionMeasureRequirements;
    }
    namespace Preferences
    {
        class SessionModeling;
    }
    namespace Preferences
    {
        class SessionNXGateway;
    }
    namespace Preferences
    {
        class SessionPdm;
    }
    namespace Preferences
    {
        class SessionPmi;
    }
    namespace Preferences
    {
        class SessionSketch;
    }
    namespace Preferences
    {
        class SessionUserInterface;
    }
    namespace Preferences
    {
        class SessionVisualizationColorSetting;
    }
    namespace Preferences
    {
        class SessionVisualizationHighQualityImage;
    }
    namespace Preferences
    {
        class SessionVisualizationScreen;
    }
    namespace Preferences
    {
        class SessionWorkPlane;
    }
    namespace Preferences
    {
        /** Represents a collection of session based preferences.  <br> To obtain an instance of this class, refer to @link Session Session@endlink  <br> */
        class NXOPENCPPEXPORT SessionPreferences
        {
            private: NXOpen::Session* m_owner;
            public: explicit SessionPreferences(NXOpen::Session *owner): m_owner(owner)
            {
            }
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 


            private: NXOpen::Preferences::SessionSketch *sketch;
            /** Returns object for doing sketch preferences settings applicable to entire session */
            public: NXOpen::Preferences::SessionSketch *Sketch()
            {
                return sketch;
            }
            private: NXOpen::Preferences::SessionNXGateway *nXGateway;
            /** Returns object for doing NXGateway preferences settings applicable to entire session */
            public: NXOpen::Preferences::SessionNXGateway *NXGateway()
            {
                return nXGateway;
            }
            private: NXOpen::Preferences::SessionAssemblies *assemblies;
            /** Returns object for doing Asseblies preferences settings applicable to entire session */
            public: NXOpen::Preferences::SessionAssemblies *Assemblies()
            {
                return assemblies;
            }
            private: NXOpen::Preferences::SessionWorkPlane *workPlane;
            /** Returns object for doing WorkPlane preferences settings applicable to entire session */
            public: NXOpen::Preferences::SessionWorkPlane *WorkPlane()
            {
                return workPlane;
            }
            private: NXOpen::Preferences::SessionModeling *modeling;
            /** Returns object for doing Modeling preferences settings applicable to entire session */
            public: NXOpen::Preferences::SessionModeling *Modeling()
            {
                return modeling;
            }
            private: NXOpen::Preferences::SessionDrafting *drafting;
            /** Returns object for doing Drafting preferences settings  applicable to entire session */
            public: NXOpen::Preferences::SessionDrafting *Drafting()
            {
                return drafting;
            }
            private: NXOpen::Preferences::SessionPmi *pmi;
            /** Returns object for doing Pmi preferences settings  applicable to entire session */
            public: NXOpen::Preferences::SessionPmi *Pmi()
            {
                return pmi;
            }
            private: NXOpen::Preferences::SessionUserInterface *userInterface;
            /** Returns object for doing Selection preferences settings applicable to entire session */
            public: NXOpen::Preferences::SessionUserInterface *UserInterface()
            {
                return userInterface;
            }
            private: NXOpen::Preferences::SessionVisualizationScreen *screenVisualization;
            /** Returns object for doing Visualization Screen preferences settings applicable to entire session */
            public: NXOpen::Preferences::SessionVisualizationScreen *ScreenVisualization()
            {
                return screenVisualization;
            }
            private: NXOpen::Preferences::SessionVisualizationColorSetting *colorSettingVisualization;
            /** Returns object for doing Visualization preferences settings applicable to entire session */
            public: NXOpen::Preferences::SessionVisualizationColorSetting *ColorSettingVisualization()
            {
                return colorSettingVisualization;
            }
            private: NXOpen::Preferences::SessionVisualizationHighQualityImage *highQualityImageVisualization;
            /** Returns object for doing Visualization High Quality Image preferences settings applicable to entire session */
            public: NXOpen::Preferences::SessionVisualizationHighQualityImage *HighQualityImageVisualization()
            {
                return highQualityImageVisualization;
            }
            private: NXOpen::Preferences::RoutingApplicationView *routingApplicationView;
            /** Returns the Routing Application View preferences. */
            public: NXOpen::Preferences::RoutingApplicationView *RoutingApplicationView()
            {
                return routingApplicationView;
            }
            private: NXOpen::Preferences::RulePreferences *knowledgeFusion;
            /** Returns object for doing Rule preferences settings applicable to entire session */
            public: NXOpen::Preferences::RulePreferences *KnowledgeFusion()
            {
                return knowledgeFusion;
            }
            private: NXOpen::Preferences::SessionPdm *pdm;
            /** Returns object for doing Pdm preference settings applicable to entire session */
            public: NXOpen::Preferences::SessionPdm *Pdm()
            {
                return pdm;
            }
            private: NXOpen::Preferences::SessionMeasureRequirements *sessionMeasureReq;
            /** Returns object for doing Measure Requirements in Assembly Sequencing applicable to the entire session */
            public: NXOpen::Preferences::SessionMeasureRequirements *SessionMeasureReq()
            {
                return sessionMeasureReq;
            }
            public: virtual void initialize();
        };
    }
}
#undef EXPORTLIBRARY
#endif
