#ifndef NXOpen_UI_HXX_INCLUDED
#define NXOpen_UI_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     UI.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopenuicpp_exports.hxx>
namespace NXOpen
{
    class UI;
    namespace Preferences
    {
        class ObjectPreferences;
    }
    namespace Preferences
    {
        class SessionUserInterfaceUI;
    }
    namespace Preferences
    {
        class SessionVisualizationShade;
    }
    namespace Preferences
    {
        class SessionVisualizationVisual;
    }
    namespace Preferences
    {
        class VisualizationLine;
    }
    class Selection;
    class _UIBuilder;
    /** This class contains the various elements that represent the NX User Interface. There is
        a single instance of this class per session. To obtain a reference to the current UI, 
        call the static method @link GetUI GetUI@endlink .
     <br> Use the static method in this class to obtain an instance. <br> */
    class NXOPENUICPPEXPORT UI : public TaggedObject
    {
        private: static UI *theUI;
        public: static UI *GetUI();
        private: friend class  _UIBuilder;
        protected: UI();
        /** Locks access to the NX User Interface. This method may be used for a custom dialog
                that requires the session to remain in a known state. When this method is called,
                all menu items that would allow the user to edit the model are grayed out.
                 <br> 
                Note that until @link UnlockAccess UnlockAccess@endlink  is called, the user will not
                be able to interact with the session. You must ensure that the UI is unlocked when
                the custom dialog terminates.
                 <br> 
                 <br> 
                This method will throw an exception if the UI cannot be locked. Note that if the UI has already been 
                locked, then it is safe to call this method again.
                 <br> 
                 <br> License requirements : None */
        public: void LockAccess
        (
        );
        /** Unlocks access for a UI that has been locked by a call to @link LockAccess LockAccess@endlink . If the UI
                is already unlocked, this method has no effect.
              <br> License requirements : None */
        public: void UnlockAccess
        (
        );
        /** Pauses execution of a journal.  <br> License requirements : None */
        public: void JournalPause
        (
        );


        private: NXOpen::Selection *selectionManager;
        /** the SelectionManager for the current session. */
        public: NXOpen::Selection *SelectionManager()
        {
            return selectionManager;
        }
        /** <b>Deprecated</b>:<br>
        &nbsp;&nbsp;&nbsp;Use @link SelectionManager() SelectionManager@endlink instead.
        @deprecated
        */
        public: NXOpen::Selection *GetSelectionManager() { return SelectionManager(); }
        private: NXOpen::Preferences::ObjectPreferences *objectPreferences;
        /** the UI based Object Preferences in the current session.*/
        public: NXOpen::Preferences::ObjectPreferences *ObjectPreferences()
        {
            return objectPreferences;
        }
        /** <b>Deprecated</b>:<br>
        &nbsp;&nbsp;&nbsp;Use @link ObjectPreferences() ObjectPreferences@endlink instead.
        @deprecated
        */
        public: NXOpen::Preferences::ObjectPreferences *GetObjectPreferences() { return ObjectPreferences(); }
        private: NXOpen::Preferences::SessionUserInterfaceUI *userInterfacePreferences;
        /** the UI based User Interface Preferences in the current session */
        public: NXOpen::Preferences::SessionUserInterfaceUI *UserInterfacePreferences()
        {
            return userInterfacePreferences;
        }
        /** <b>Deprecated</b>:<br>
        &nbsp;&nbsp;&nbsp;Use @link UserInterfacePreferences() UserInterfacePreferences@endlink instead.
        @deprecated
        */
        public: NXOpen::Preferences::SessionUserInterfaceUI *GetUserInterfacePreferences() { return UserInterfacePreferences(); }
        private: NXOpen::Preferences::SessionVisualizationVisual *visualizationVisualPreferences;
        /** the UI based Visualization Preferences under Visual Tab in the current session */
        public: NXOpen::Preferences::SessionVisualizationVisual *VisualizationVisualPreferences()
        {
            return visualizationVisualPreferences;
        }
        /** <b>Deprecated</b>:<br>
        &nbsp;&nbsp;&nbsp;Use @link VisualizationVisualPreferences() VisualizationVisualPreferences@endlink instead.
        @deprecated
        */
        public: NXOpen::Preferences::SessionVisualizationVisual *GetVisualizationVisualPreferences() { return VisualizationVisualPreferences(); }
        private: NXOpen::Preferences::VisualizationLine *visualizationLinePreferences;
        /** the UI based Visualization Preferences under Line Tab in the current session */
        public: NXOpen::Preferences::VisualizationLine *VisualizationLinePreferences()
        {
            return visualizationLinePreferences;
        }
        /** <b>Deprecated</b>:<br>
        &nbsp;&nbsp;&nbsp;Use @link VisualizationLinePreferences() VisualizationLinePreferences@endlink instead.
        @deprecated
        */
        public: NXOpen::Preferences::VisualizationLine *GetVisualizationLinePreferences() { return VisualizationLinePreferences(); }
        private: NXOpen::Preferences::SessionVisualizationShade *visualizationShadingPreferences;
        /** the UI based Visualization Preferences under Shading Tab in the current session  */
        public: NXOpen::Preferences::SessionVisualizationShade *VisualizationShadingPreferences()
        {
            return visualizationShadingPreferences;
        }
        /** <b>Deprecated</b>:<br>
        &nbsp;&nbsp;&nbsp;Use @link VisualizationShadingPreferences() VisualizationShadingPreferences@endlink instead.
        @deprecated
        */
        public: NXOpen::Preferences::SessionVisualizationShade *GetVisualizationShadingPreferences() { return VisualizationShadingPreferences(); }
        public: virtual void initialize();
    };
}
#undef EXPORTLIBRARY
#endif
