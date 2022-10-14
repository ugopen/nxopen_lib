/*
===============================================================================

            Copyright (c) 1999-2000 Unigraphics Solutions, Incorporated
                      Unpublished - All rights reserved
===============================================================================

File Description:
    This file declares the interface for UIStyler integer controls.

Classes Declared:
    UgUIInteger

================================================================================



*/

#ifndef UG_UI_INTEGER_INCLUDED
#define UG_UI_INTEGER_INCLUDED

#include <ug_ui_control.hxx>
#include <libopenintpp_exports.hxx>

///////////////////////////////////////////////////////////////////////////////
// This class provides an interface to UIStyler integer controls.
///////////////////////////////////////////////////////////////////////////////
class OPENINTPPEXPORT UgUIInteger : public UgUIControl
{
    public:
        // Constructor
        UgUIInteger
        (
            const std::string  &control_id, // Identifying name of the control
            const UgUIDialog   *dialog      // Dialog associated with the
                                            // control
        );

        // Destructor
        virtual ~UgUIInteger ( );

        // Retrieves the value
        int getValue ( ) const;

        // Sets the bitmap
        void setBitmap
        (
            const std::string &file     // <I>
                                        // Name of the bitmap file
        );

        // Sets the focus to this control
        void setFocus ( );

        // Sets the label
        void setLabel
        (
            const std::string &label    // <I>
                                        // Label of the control
        );

        // Sets the value
        void setValue
        (
            int value                   // <I>
                                        // Value of the control
        );
};

#undef EXPORTLIBRARY

#endif // UG_UI_INTEGER_INCLUDED
