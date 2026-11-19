/*
===============================================================================

            Copyright (c) 1999-2000 Unigraphics Solutions, Incorporated
                      Unpublished - All rights reserved
===============================================================================

File Description:
    This file declares the interface for UIStyler toggle buttons.

Classes Declared:
    UgUIToggleButton

================================================================================



*/

#ifndef UG_UI_TOGGLE_BUTTON_INCLUDED
#define UG_UI_TOGGLE_BUTTON_INCLUDED

#include <ug_ui_control.hxx>
#include <libopenintpp_exports.hxx>

///////////////////////////////////////////////////////////////////////////////
// This class provides an interface to UIStyler toggle button controls.
///////////////////////////////////////////////////////////////////////////////
class OPENINTPPEXPORT UgUIToggleButton : public UgUIControl
{
    public:
        // Constructor
        UgUIToggleButton
        (
            const std::string  &control_id, // Identifying name of the control
            const UgUIDialog   *dialog      // Dialog associated with the
                                            // control
        );

        // Destructor
        virtual ~UgUIToggleButton ( );

        // Retrieves the value
        bool getValue ( ) const;

        // Sets the focus to this control
        void setFocus ( );

        // Sets the default action to this button
        void setDefaultAction ( );

        // Sets the label
        void setLabel
        (
            const std::string &label    // <I>
                                        // Label of the control
        );

        // Sets the value
        void setValue
        (
            bool value                  // <I>
                                        // Value of the control
        );
};

#undef EXPORTLIBRARY

#endif // UG_UI_TOGGLE_BUTTON_INCLUDED
