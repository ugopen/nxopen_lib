/*
===============================================================================

            Copyright (c) 1999-2000 Unigraphics Solutions, Incorporated
                      Unpublished - All rights reserved
===============================================================================

File Description:
    This file declares the interface for UIStyler dialogs. When using UgUI
    classes for controls, an instance of UgUIDialog must be instantiated for
    each dialog.

Classes Declared:
    UgUIDialog

================================================================================



*/

#ifndef UG_UI_DIALOG_INCLUDED
#define UG_UI_DIALOG_INCLUDED

#include <ug_ui_control.hxx>
#include <uf_styler.h>
#include <libopenintpp_exports.hxx>

///////////////////////////////////////////////////////////////////////////////
// This class provides an interface to UIStyler dialogs. A UgUIDialog object
// must be created for each styler dialog in order to use UgUI controls. The
// ID of the dialog changes each time it is displayed on the screen
// (constructed). Consequently, it is important that the ID be set
// appropriately each time using the setDialogID method.
///////////////////////////////////////////////////////////////////////////////
class OPENINTPPEXPORT UgUIDialog : public UgUIControl
{
    public:
        // This enum defines the navigation buttons that are available on a
        // dialog.
        enum NavigationButton
        {
            OKButton        = UF_STYLER_OK_INDEX,       // The OK button
            ApplyButton     = UF_STYLER_APPLY_INDEX,    // The Apply button
            BackButton      = UF_STYLER_BACK_INDEX,     // The Back button
            CancelButton    = UF_STYLER_CANCEL_INDEX    // The Cancel button
        };

        // Constructor
        UgUIDialog( void );

        // Destructor
        virtual ~UgUIDialog( void );

        // Retrieves the selection type
        UF_UI_selection_p_t askSelectionType( void );

        // Retrieves the control type
        UgUIControl::ControlType askType( void ) const;

        // Retrieves the dialog ID
        int getDialogID( void );

        // Determines if the control is sensitive
        bool isSensitive( void ) const;

        // Determines if the control is visible
        bool isVisible( void ) const;

        // Initializes the dialog
        void initialize
        (
            int dialogID            // <I>
                                    // Dialog ID
        );

        // Performs custom initialization of a dialog, it is called
        // from the initialize method. This method must be defined
        // in derived classes.
        virtual void initializeThis( void ) = 0;

        // Sets the dialog ID
        void setDialogID
        (
            int dialogID            // <I>
                                    // Dialog ID
        );

        // Sets the dialog label
        void setLabel
        (
            const std::string &label   // <I>
                                       // Dialog label
        );

        // Sets the dialog resizeability
        void setResizeable
        (
            bool resizeable         // <I>
                                    // Resizeability status
        );

        // Sets navigation button sensitivity
        void setNavigationButtonSensitive
        (
            NavigationButton  button,    // <I>
                                         // Navigation button
            bool              sensitive  // <I>
                                         // Sensitivity of the button
        );

        // Sets the visibility
        void setVisible
        (
            bool visible    // <I>
                            // Visibility status of the control
        );

        // Sets the dialog width
        void setWidth
        (
            int width               // <I>
                                    // Dialog width
        );

        // Invalidate the dialog ID
        void invalidate( void );

    private:
        // Dialog ID
        int m_dialog_id;
};

#undef EXPORTLIBRARY

#endif // UG_UI_DIALOG_INCLUDED
