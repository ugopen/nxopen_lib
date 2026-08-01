/*
===============================================================================

            Copyright (c) 1999-2000 Unigraphics Solutions, Incorporated
                      Unpublished - All rights reserved
===============================================================================

File Description:
    This file declares the interface for UIStyler scrolled windows.

Classes Declared:
    UgUIScrolledWindow

================================================================================



*/

#ifndef UG_UI_SCROLLED_WINDOW_INCLUDED
#define UG_UI_SCROLLED_WINDOW_INCLUDED

#include <ug_ui_control.hxx>
#include <libopenintpp_exports.hxx>

///////////////////////////////////////////////////////////////////////////////
// This class provides an interface to UIStyler scrolled window controls.
///////////////////////////////////////////////////////////////////////////////
class OPENINTPPEXPORT UgUIScrolledWindow : public UgUIControl
{
    public:
        // Constructor
        UgUIScrolledWindow
        (
            const std::string  &control_id, // Identifying name of the control
            const UgUIDialog   *dialog      // Dialog associated with the
                                            // control
        );

        // Destructor
        virtual ~UgUIScrolledWindow ( );
};

#undef EXPORTLIBRARY

#endif // UG_UI_SCROLLED_WINDOW_INCLUDED
