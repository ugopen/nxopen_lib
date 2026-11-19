/*
===============================================================================

            Copyright (c) 1999-2000 Unigraphics Solutions, Incorporated
                      Unpublished - All rights reserved
===============================================================================

File Description:
    This file declares the interface for UIStyler option menu controls.

Classes Declared:
    UgUIOptionMenu

================================================================================



*/

#ifndef UG_UI_OPTION_MENU_INCLUDED
#define UG_UI_OPTION_MENU_INCLUDED

#include <ug_ui_control.hxx>
#include <libopenintpp_exports.hxx>

///////////////////////////////////////////////////////////////////////////////
// This class provides an interface to UIStyler option menu controls.
///////////////////////////////////////////////////////////////////////////////
class OPENINTPPEXPORT UgUIOptionMenu : public UgUIControl
{
    public:
        // Constructor
        UgUIOptionMenu
        (
            const std::string  &control_id, // Identifying name of the control
            const UgUIDialog   *dialog      // Dialog associated with the
                                            // control
        );

        // Destructor
        virtual ~UgUIOptionMenu ( );

        // Retrieves the list
        const std::vector< std::string > getList ( ) const;

        // Retrieves the currently selected item
        int askSelectedIndex ( ) const;

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

        // Sets the sensitivity of the entire UgUIOptionMenu object
        virtual void setSensitive
        (
            bool sensitive              // <I>
                                        // Sensitivity status of the control
        );

        // Sets the sensitivity of a single item in the list
        virtual void setSensitive
        (
            bool sensitive,             // <I>
                                        // Sensitivity status of the item
            int  index                  // <I>
                                        // Zero-based index of the item
        );

        // Selects an item in the list
        void select
        (
            int index                   // <I>
                                        // Zero-based index of the item
        );

        // Sets the list
        void setList
        (
            const std::vector< std::string > &list   // <I>
                                                     // Item list
        );
};

#undef EXPORTLIBRARY

#endif // UG_UI_OPTION_MENU_INCLUDED
