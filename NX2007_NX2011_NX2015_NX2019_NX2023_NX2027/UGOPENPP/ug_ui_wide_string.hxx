/*
===============================================================================

            Copyright (c) 1999-2000 Unigraphics Solutions, Incorporated
                      Unpublished - All rights reserved
===============================================================================

File Description:
    This file declares the interface for UIStyler wide string controls.

Classes Declared:
    UgUIWideString

================================================================================



*/

#ifndef UG_UI_WIDE_STRING_INCLUDED
#define UG_UI_WIDE_STRING_INCLUDED

#include <ug_ui_control.hxx>
#include <libopenintpp_exports.hxx>

///////////////////////////////////////////////////////////////////////////////
// This class provides an interface to UIStyler wide string controls.
///////////////////////////////////////////////////////////////////////////////
class OPENINTPPEXPORT UgUIWideString : public UgUIControl
{
    public:
        // Constructor
        UgUIWideString
        (
            const std::string  &control_id, // Identifying name of the control
            const UgUIDialog   *dialog      // Dialog associated with the
                                            // control
        );

        // Destructor
        virtual ~UgUIWideString ( );

        // Retrieves the value
        const std::string getValue ( ) const;

        // Sets the focus to this control
        void setFocus ( );

        // Sets the label
        void setLabel
        (
            const std::string  &label   // <I>
                                        // Label of the control
        );

        // Sets the value
        void setValue
        (
            const std::string  &value   // <I>
                                        // Value of the control
        );
};

#undef EXPORTLIBRARY

#endif // UG_UI_WIDE_STRING_INCLUDED
