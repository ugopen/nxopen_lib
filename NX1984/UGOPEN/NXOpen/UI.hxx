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
#ifdef _MSC_VER
#pragma once
#endif

#include <NXOpen/NXDeprecation.hxx>
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/BlockStyler_BlockDialog.hxx>
#include <NXOpen/CustomPopupMenuHandler.hxx>
#include <NXOpen/Gateway_ImageExportBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopenuicpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    class UI;
    namespace BlockStyler
    {
        class BlockDialog;
    }
    class CustomPopupMenuHandler;
    namespace Gateway
    {
        class ImageExportBuilder;
    }
    namespace MenuBar
    {
        class MenuBarManager;
    }
    class MovieManager;
    class NXMessageBox;
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
    class ProductDemo;
    class ResourceBarManager;
    class Selection;
    namespace UIStyler
    {
        class Styler;
    }
    class ViewUIManager;
    class _UIBuilder;
    class UIImpl;
    /** This class contains the various elements that represent the NX User Interface. There is
        a single instance of this class per session. To obtain a reference to the current UI, 
        call the static method @link UI::GetUI UI::GetUI@endlink .

        For Java, use  @code SessionFactory::get("UI") @endcode  to obtain the reference of the current UI.

        For language bindings that support remoting, the server must export it for this 
        class to be obtained by a client.

     <br> Use the static method in this class to obtain an instance.  <br> 
     <br>  Created in NX3.0.0.  <br>  
    */
    class NXOPENUICPPEXPORT  UI : public NXOpen::TaggedObject
    {
        /** Indicates the Lock, Unlock status of NX functions. */
        public: enum Status
        {
            StatusLock/** Lock status */,
            StatusUnlock/** Unlock status */
        };

        public: /** User defined method is called whenever an NX utility function state changes.  An
                example of a NX utility function is the Preferences - User Interface dialog.
                
                 <br> 
                The input parameter, visible is true when the function becomes
                visible and false when the function is no longer visible.
                 <br> 
                
                 <br> 
                NX utility functions can be nested. The following scenario describes when this method
                is called for a function call in the middle of another function and
                then exiting both functions:
                 <br> 
                
                 @code 
                First utility function call
                UtilityFunctionVisibilityHandler - visible == true
                
                  Second utility function call while the first utility function is still visible
                  UtilityFunctionVisibilityHandler - visible == true
                  
                  Second utility function exit
                  UtilityFunctionVisibilityHandler - visible == false
                  
                First utility function exit
                UtilityFunctionVisibilityHandler - visible == false
                 @endcode 
                    
                 
         <br>  Created in NX5.0.5.  <br>  
         <br> License requirements : None */
        typedef NXOpen::Callback1<void, bool> UtilityFunctionVisibilityHandler;
        private: UIImpl * m_ui_impl;
        private: static UI *theUI;
        public: static UI *GetUI();
        private: friend class  _UIBuilder;
        protected: UI();
        public: ~UI();
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
                
         <br>  Created in NX3.0.0.  <br>  
         <br> License requirements : None */
        public: void LockAccess
        (
        );
        /** Unlocks access for a UI that has been locked by a call to @link LockAccess LockAccess@endlink . If the UI
                is already unlocked, this method has no effect.
             
         <br>  Created in NX3.0.0.  <br>  
         <br> License requirements : None */
        public: void UnlockAccess
        (
        );
        /** Pauses execution of a journal. 
         <br>  Created in NX4.0.0.  <br>  
         <br> License requirements : None */
        public: void JournalPause
        (
        );
        /** Query NX lock status.
            This function is useful when dismissing a custom dialog and you want
            to determine whether or not a lock has been set. Returns @link NXOpen::UI::StatusLock NXOpen::UI::StatusLock@endlink , 
            when NX is in lock status. Returns @link NXOpen::UI::StatusUnlock NXOpen::UI::StatusUnlock@endlink , 
            when NX is in unlock status.
             @return  
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::UI::Status AskLockStatus
        (
        );
        /** Creates a block dialog. 
            Use  @code #undef CreateDialog @endcode  in C++ programs to avoid confusion with Windows API @return  
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::BlockStyler::BlockDialog * CreateDialog
        (
            const NXString & dialogName /** Dialog name */
        );
        /** Creates a block dialog. 
            Use  @code #undef CreateDialog @endcode  in C++ programs to avoid confusion with Windows API @return  
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        NXOpen::BlockStyler::BlockDialog * CreateDialog
        (
            const char * dialogName /** Dialog name */
        );
        /** Registers a user defined method that is called whenever an utility function state changes.  @return  identifier of registered method (used to unregister the method) 
         <br>  Created in NX5.0.5.  <br>  
         <br> License requirements : None */
        public: int AddUtilityFunctionVisibilityHandler
        (
            const NXOpen::UI::UtilityFunctionVisibilityHandler&  utilityFunctionVisibilityHandler /** utilityfunctionvisibilityhandler */ 
        );
        /** Unregisters a user defined method that is called whenever an utility function state changes. 
         <br>  Created in NX5.0.5.  <br>  
         <br> License requirements : None */
        public: void RemoveUtilityFunctionVisibilityHandler
        (
            int id /** identifier for method to unregister */
        );
        /** Create a custom menu.  @return  
         <br>  Created in NX6.0.4.  <br>  
         <br> License requirements : None */
        public: NXOpen::CustomPopupMenuHandler * CreateCustomPopupMenuHandler
        (
        );
        /** Creates a @link NXOpen::Gateway::ImageExportBuilder NXOpen::Gateway::ImageExportBuilder@endlink  
         <br>  Created in NX12.0.1.  <br>  
         <br> License requirements : None */
        public: NXOpen::Gateway::ImageExportBuilder * CreateImageExportBuilder
        (
        );
        /** Returns a flag indicating whether the NX user interface is in a state
            where opening a part and making it the display part is supported. 
            For example if certain dialogs are displayed or 
            the system is in a task environment it is not supported      
            
         <br>  Created in NX8.5.0.  <br>  
         <br> License requirements : None */
        public: bool CanOpenPart
        (
        );
        /** Display a note to the notification center.  @return  identifier of note (used to delete the note) 
         <br>  Created in NX1980.0.0.  <br>  
         <br> License requirements : None */
        public: int DisplayNotification
        (
            const NXString & title /** Notification title. This title will be displayed in tooltip as well */,
            const NXString & description /** Notification description.  */,
            const NXString & extraText /** Secondary text to be displayed below the description */,
            const NXString & icon /** Bitmap. User can specify a NX bitmap or a new bitmap with path */
        );
        /** Display a note to the notification center.  @return  identifier of note (used to delete the note) 
         <br>  Created in NX1980.0.0.  <br>  
         <br> License requirements : None */
        int DisplayNotification
        (
            const char * title /** Notification title. This title will be displayed in tooltip as well */,
            const char * description /** Notification description.  */,
            const char * extraText /** Secondary text to be displayed below the description */,
            const char * icon /** Bitmap. User can specify a NX bitmap or a new bitmap with path */
        );
        /** Remove a note from the notification center. 
         <br>  Created in NX1980.0.0.  <br>  
         <br> License requirements : None */
        public: void RemoveNotification
        (
            int id /** Notification id */
        );


        /** the Uistyler for the current session. 
         <br>  Created in NX3.0.0.  <br>  
        */
        public: NXOpen::NXMessageBox *NXMessageBox();
        /** the Uistyler for the current session. 
         <br>  Created in NX3.0.0.  <br>  
        */
        public: NXOpen::UIStyler::Styler *Styler();
        /** the SelectionManager for the current session. 
         <br>  Created in NX3.0.0.  <br>  
        */
        public: NXOpen::Selection *SelectionManager();
        /** the UI based Object Preferences in the current session.
         <br>  Created in NX3.0.0.  <br>  
        */
        public: NXOpen::Preferences::ObjectPreferences *ObjectPreferences();
        /** the UI based User Interface Preferences in the current session 
         <br>  Created in NX3.0.0.  <br>  
        */
        public: NXOpen::Preferences::SessionUserInterfaceUI *UserInterfacePreferences();
        /** the UI based Visualization Preferences under Visual Tab in the current session 
         <br>  Created in NX3.0.0.  <br>  
        */
        public: NXOpen::Preferences::SessionVisualizationVisual *VisualizationVisualPreferences();
        /** the UI based Visualization Preferences under Line Tab in the current session 
         <br>  Created in NX3.0.0.  <br>  
        */
        public: NXOpen::Preferences::VisualizationLine *VisualizationLinePreferences();
        /** the UI based Visualization Preferences under Shading Tab in the current session  
         <br>  Created in NX3.0.0.  <br>  
        */
        public: NXOpen::Preferences::SessionVisualizationShade *VisualizationShadingPreferences();
        /** Returns the @link NXOpen::MenuBar::MenuBarManager NXOpen::MenuBar::MenuBarManager@endlink  belonging to the current session 
         <br>  Created in NX3.0.0.  <br>  
        */
        public: NXOpen::MenuBar::MenuBarManager *MenuBarManager();
        /** the Movie Manager class. 
         <br>  Created in NX3.0.0.  <br>  
        */
        public: NXOpen::MovieManager *MovieManager();
        /** Returns the @link ResourceBarManager ResourceBarManager@endlink  for the current session 
         <br>  Created in NX10.0.0.  <br>  
        */
        public: NXOpen::ResourceBarManager *ResourceBarManager();
        /** Returns the @link ViewUIManager ViewUIManager@endlink  
         <br>  Created in NX11.0.1.  <br>  
        */
        public: NXOpen::ViewUIManager *ViewUIManager();
        /** The trial information for the current session. 
         <br>  Created in NX1926.0.0.  <br>  
        */
        public: NXOpen::ProductDemo *ProductDemo();
    };
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