/*
===============================================================================

            Copyright (c) 1999-2000 Unigraphics Solutions, Incorporated
                      Unpublished - All rights reserved
===============================================================================

File Description:
    This file declares the interface for UIStyler bitmaps.

Classes Declared:
    UgUIBitmap

================================================================================



*/

#ifndef UG_UI_BITMAP_INCLUDED
#define UG_UI_BITMAP_INCLUDED

#include <ug_ui_control.hxx>
#include <libopenintpp_exports.hxx>

///////////////////////////////////////////////////////////////////////////////
// This class provides an interface to UIStyler bitmap controls.
///////////////////////////////////////////////////////////////////////////////
class OPENINTPPEXPORT UgUIBitmap : public UgUIControl
{
    public:
        // Constructor
        UgUIBitmap
        (
            const std::string &control_id, // Identifying name of the control
            const UgUIDialog  *dialog      // Dialog associated with the
                                           // control
        );

        // Destructor
        virtual ~UgUIBitmap ( );

        // Determines if the control is visible
        bool isVisible ( ) const;

        // Determines if the control is sensitive
        bool isSensitive ( ) const;

        // Sets the bitmap
        void setBitmap
        (
            const std::string &file   // <I>
                                      // Name of the bitmap file
        );

        // Sets the sensitivity (overridden to do nothing because bitmap
        // sensitivity cannot be set)
        void setSensitive
        (
            bool sensitive            // <I>
                                      // Sensitivity status of the control
        );

        // Sets the visibility (overridden to do nothing because bitmap
        // visibility cannot be set)
        void setVisible
        (
            bool visible              // <I>
                                      // Visibility status of the control
        );
};

#undef EXPORTLIBRARY

#endif // UG_UI_BITMAP_INCLUDED
