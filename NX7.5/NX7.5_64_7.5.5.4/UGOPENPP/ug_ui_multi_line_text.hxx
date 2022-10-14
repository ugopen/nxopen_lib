/*
===============================================================================

            Copyright (c) 1999-2000 Unigraphics Solutions, Incorporated
                      Unpublished - All rights reserved
===============================================================================

File Description:
    This file declares the interface for UIStyler multi-line text controls.

Classes Declared:
    UgUIMultiLineText

================================================================================



*/

#ifndef UG_UI_MULTI_LINE_TEXT_INCLUDED
#define UG_UI_MULTI_LINE_TEXT_INCLUDED

#include <ug_ui_control.hxx>
#include <libopenintpp_exports.hxx>

///////////////////////////////////////////////////////////////////////////////
// This class provides an interface to UIStyler multi-line text controls.
///////////////////////////////////////////////////////////////////////////////
class OPENINTPPEXPORT UgUIMultiLineText : public UgUIControl
{
    public:
        // Constructor
        UgUIMultiLineText
        (
            const std::string  &control_id, // Identifying name of the control
            const UgUIDialog   *dialog      // Dialog associated with the
                                            // control
        );

        // Destructor
        virtual ~UgUIMultiLineText ( );

        // Retrieves the value
        const std::vector< std::string > getValue ( ) const;

        // Sets the focus to this control
        void setFocus ( );

        // Sets the label
        void setLabel
        (
            const std::string  &label       // <I>
                                            // Label of the control
        );

        // Sets the value
        void setValue
        (
            const std::vector< std::string > &value    // <I>
                                                       // Array of text strings
        );
};

#undef EXPORTLIBRARY

#endif // UG_UI_MULTI_LINE_TEXT_INCLUDED
