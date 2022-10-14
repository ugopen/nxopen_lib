/*
===============================================================================

            Copyright (c) 1999-2000 Unigraphics Solutions, Incorporated
                      Unpublished - All rights reserved
===============================================================================

File Description:
    This file declares the interface for UIStyler button layouts.

Classes Declared:
    UgUIButtonLayout

================================================================================



*/

#ifndef UG_UI_BUTTON_LAYOUT_INCLUDED
#define UG_UI_BUTTON_LAYOUT_INCLUDED

#include <ug_ui_container.hxx>
#include <libopenintpp_exports.hxx>

///////////////////////////////////////////////////////////////////////////////
// This class provides an interface to UIStyler button layout controls.
///////////////////////////////////////////////////////////////////////////////
class OPENINTPPEXPORT UgUIButtonLayout : public UgUIContainer
{
    public:
        // Constructor
        UgUIButtonLayout
        (
            const std::string  &control_id, // Identifying name of the control
            const UgUIDialog   *dialog      // Dialog associated with the
                                            // control
        );

        // Destructor
        virtual ~UgUIButtonLayout ( );

        // Sets the default action to this button layout
        void setDefaultAction ( );
};

#undef EXPORTLIBRARY

#endif // UG_UI_BUTTON_LAYOUT_INCLUDED
