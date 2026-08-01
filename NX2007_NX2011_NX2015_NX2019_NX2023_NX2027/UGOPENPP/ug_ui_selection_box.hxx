/*
===============================================================================

            Copyright (c) 1999-2000 Unigraphics Solutions, Incorporated
                      Unpublished - All rights reserved
===============================================================================

File Description:
    This file declares the interface for UIStyler selection boxes.

Classes Declared:
    UgUISelectionBox

================================================================================



*/

#ifndef UG_UI_SELECTION_BOX_INCLUDED
#define UG_UI_SELECTION_BOX_INCLUDED

#include <ug_ui_list.hxx>
#include <libopenintpp_exports.hxx>

///////////////////////////////////////////////////////////////////////////////
// This class provides an interface to UIStyler selection box controls.
///////////////////////////////////////////////////////////////////////////////
class OPENINTPPEXPORT UgUISelectionBox : public UgUIList
{
    public:
        // Constructor
        UgUISelectionBox
        (
            const std::string  &control_id, // Identifying name of the control
            const UgUIDialog   *dialog      // Dialog associated with the
                                            // control
        );

        // Destructor
        virtual ~UgUISelectionBox ( );

        // Sets the focus to this control
        void setFocus ( );

        // Sets the label
        void setLabel
        (
            const std::string &label    // <I>
                                        // Label of the control
        );
};

#undef EXPORTLIBRARY

#endif // UG_UI_SELECTION_BOX_INCLUDED
