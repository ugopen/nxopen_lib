/*
===============================================================================

            Copyright (c) 1999-2000 Unigraphics Solutions, Incorporated
                      Unpublished - All rights reserved
===============================================================================

File Description:
    This file declares the interface for UIStyler radio boxes.

Classes Declared:
    UgUIRadioBox

================================================================================



*/

#ifndef UG_UI_RADIO_BOX_INCLUDED
#define UG_UI_RADIO_BOX_INCLUDED

#include <ug_ui_container.hxx>
#include <libopenintpp_exports.hxx>

///////////////////////////////////////////////////////////////////////////////
// This class provides an interface to UIStyler radio box controls.
///////////////////////////////////////////////////////////////////////////////
class OPENINTPPEXPORT UgUIRadioBox : public UgUIContainer
{
    public:
        // Constructor
        UgUIRadioBox
        (
            const std::string  &control_id, // Identifying name of the control
            const UgUIDialog   *dialog      // Dialog associated with the
                                            // control
        );

        // Destructor
        virtual ~UgUIRadioBox ( );

        // Retrieves the currently selected option
        int getValue ( ) const;

        // Sets the default action to this button
        void setDefaultAction ( );

        // Sets the label
        void setLabel
        (
            const std::string &label    // <I>
                                        // Label of the control
        );

        // Sets the selected radio option
        void setValue
        (
            int value                   // <I>
                                        // Selected option
        );
};

#undef EXPORTLIBRARY

#endif // UG_UI_RADIO_BOX_INCLUDED
