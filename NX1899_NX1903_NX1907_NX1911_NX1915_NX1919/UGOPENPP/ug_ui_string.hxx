/*
===============================================================================

            Copyright (c) 1999-2000 Unigraphics Solutions, Incorporated
                      Unpublished - All rights reserved
===============================================================================

File Description:
    This file declares the interface for UIStyler string controls.

Classes Declared:
    UgUIString

================================================================================



*/

#ifndef UG_UI_STRING_INCLUDED
#define UG_UI_STRING_INCLUDED

#include <ug_ui_control.hxx>
#include <libopenintpp_exports.hxx>

///////////////////////////////////////////////////////////////////////////////
// This class provides an interface to UIStyler string controls.
///////////////////////////////////////////////////////////////////////////////
class OPENINTPPEXPORT UgUIString : public UgUIControl
{
    public:
        // Constructor
        UgUIString
        (
            const std::string  &control_id, // Identifying name of the control
            const UgUIDialog   *dialog      // Dialog associated with the
                                            // control
        );

        // Destructor
        virtual ~UgUIString ( );

        // Retrieves the value
        const std::string getValue ( ) const;

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
            const std::string &value    // <I>
                                        // Value of the control
        );


        // Sets the value
        void setValue
        (
            bool value                  // <I>
                                        // Boolean to be converted to a string
        );

        // Sets the value
        void setValue
        (
            int value                   // <I>
                                        // Integer to be converted to a string
        );

        // Sets the value
        void setValue
        (
            double value                // <I>
                                        // Double to be converted to a string
        );
};

#undef EXPORTLIBRARY

#endif // UG_UI_STRING_INCLUDED
