/*
===============================================================================

            Copyright (c) 1999-2000 Unigraphics Solutions, Incorporated
                      Unpublished - All rights reserved
===============================================================================

File Description:
    This file declares the interface for UIStyler real controls.

Classes Declared:
    UgUIReal

================================================================================



*/

#ifndef UG_UI_REAL_INCLUDED
#define UG_UI_REAL_INCLUDED

#include <ug_ui_control.hxx>
#include <libopenintpp_exports.hxx>

///////////////////////////////////////////////////////////////////////////////
// This class provides an interface to UIStyler real controls.
///////////////////////////////////////////////////////////////////////////////
class OPENINTPPEXPORT UgUIReal : public UgUIControl
{
    public:
        // Constructor
        UgUIReal
        (
            const std::string  &control_id, // Identifying name of the control
            const UgUIDialog   *dialog      // Dialog associated with the
                                            // control
        );

        // Destructor
        virtual ~UgUIReal ( );

        // Retrieves the value
        double getValue ( ) const;

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
            double value                // <I>
                                        // Value of the control
        );
};

#undef EXPORTLIBRARY

#endif // UG_UI_REAL_INCLUDED
