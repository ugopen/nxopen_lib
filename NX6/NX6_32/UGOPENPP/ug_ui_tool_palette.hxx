/*
===============================================================================

            Copyright (c) 1999-2000 Unigraphics Solutions, Incorporated
                      Unpublished - All rights reserved
===============================================================================

File Description:
    This file declares the interface for UIStyler tool palettes.

Classes Declared:
    UgUIToolPalette

================================================================================



*/

#ifndef UG_UI_TOOL_PALETTE_INCLUDED
#define UG_UI_TOOL_PALETTE_INCLUDED

#include <ug_ui_container.hxx>
#include <libopenintpp_exports.hxx>

///////////////////////////////////////////////////////////////////////////////
// This class provides an interface to UIStyler tool palette controls.
///////////////////////////////////////////////////////////////////////////////
class OPENINTPPEXPORT UgUIToolPalette : public UgUIContainer
{
    public:
        // Constructor
        UgUIToolPalette
        (
            const std::string  &control_id, // Identifying name of the control
            const UgUIDialog   *dialog      // Dialog associated with the
                                            // control
        );

        // Destructor
        virtual ~UgUIToolPalette ( );

        // Retrieves the currently selected palette item
        int getValue ( ) const;

        // Sets the default action to this button
        void setDefaultAction ( );

        // Sets the label
        void setLabel
        (
            const std::string &label    // <I>
                                        // Label of the control
        );

        // Sets the selected palette item
        void setValue
        (
            int value                   // <I>
                                        // Zero-based index of item to
                                        // select
        );
};

#undef EXPORTLIBRARY

#endif // UG_UI_TOOL_PALETTE_INCLUDED
