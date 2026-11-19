/*
===============================================================================

            Copyright (c) 1999-2000 Unigraphics Solutions, Incorporated
                      Unpublished - All rights reserved
===============================================================================

File Description:
    This file declares the interface for UIStyler labels.

Classes Declared:
    UgUILabel

================================================================================



*/

#ifndef UG_UI_LABEL_INCLUDED
#define UG_UI_LABEL_INCLUDED

#include <ug_ui_control.hxx>
#include <libopenintpp_exports.hxx>

///////////////////////////////////////////////////////////////////////////////
// This class provides an interface to UIStyler label controls.
///////////////////////////////////////////////////////////////////////////////
class OPENINTPPEXPORT UgUILabel : public UgUIControl
{
    public:
        // Constructor
        UgUILabel
        (
            const std::string  &control_id, // Identifying name of the control
            const UgUIDialog   *dialog      // Dialog associated with the
                                            // control
        );

        // Destructor
        virtual ~UgUILabel ( );

        // Sets the bitmap
        void setBitmap
        (
            const std::string &file     // <I>
                                        // Name of the bitmap file
        );

        // Sets the label
        void setLabel
        (
            const std::string &label    // <I>
                                        // Label of the control
        );
};

#undef EXPORTLIBRARY

#endif // UG_UI_LABEL_INCLUDED
