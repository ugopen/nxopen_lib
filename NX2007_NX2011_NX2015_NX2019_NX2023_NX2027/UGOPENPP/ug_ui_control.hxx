/*
===============================================================================

            Copyright (c) 1999-2000 Unigraphics Solutions, Incorporated
                      Unpublished - All rights reserved
===============================================================================

File Description:
    This file declares an abstract base class for UIStyler controls.

Classes Declared:
    UgUIControl

================================================================================



*/

#ifndef UG_UI_CONTROL_INCLUDED
#define UG_UI_CONTROL_INCLUDED

#include <stddef.h>
#include <ug_string.hxx>
#include <ug_vector.hxx>
#include <uf_styler.h>
#include <libopenintpp_exports.hxx>

class UgUIDialog;

///////////////////////////////////////////////////////////////////////////////
// This is an abstract base class for UIStyler controls. It provides basic
// control functionality.
///////////////////////////////////////////////////////////////////////////////
class OPENINTPPEXPORT UgUIControl  
{
    public:
        // This enum defines the navigation buttons that are available on a
        // dialog.
        enum ControlType
        {
            ActionButton        = UF_STYLER_ACTION_BUTTON_TYPE,     // Defines an action button control
            Bitmap              = UF_STYLER_BITMAP_TYPE,            // Defines a bitmap control
            ButtonLayout        = UF_STYLER_BUTTON_LAYOUT_TYPE,     // Defines a button layout control
            Dialog              = UF_STYLER_DIALOG_TYPE,            // Defines a dialog control
            Integer             = UF_STYLER_INTEGER_TYPE,           // Defines an integer control
            IntegerScale        = UF_STYLER_SCALE_INTEGER_TYPE,     // Defines an integer scale control
            Label               = UF_STYLER_LABEL_TYPE,             // Defines a label control
            MultiLineText       = UF_STYLER_MULTI_LINE_TEXT_TYPE,   // Defines a multi-line text control
            MultiSelectList     = UF_STYLER_MULTI_LIST_TYPE,        // Defines a multi-select list control
            OptionMenu          = UF_STYLER_OPTION_MENU_TYPE,       // Defines an option menu control
            RadioBox            = UF_STYLER_RADIO_BOX_TYPE,         // Defines a radio box control
            Real                = UF_STYLER_REAL_TYPE,              // Defines a real control
            RealScale           = UF_STYLER_SCALE_REAL_TYPE,        // Defines a real scale control
            ScrolledWindow      = UF_STYLER_SCROLLED_WINDOW_TYPE,   // Defines a scrolled window control
            SelectionBox        = UF_STYLER_SELECTION_BOX_TYPE,     // Defines a selection box control
            Separator           = UF_STYLER_SEPARATOR_TYPE,         // Defines a separator control
            SingleSelectList    = UF_STYLER_SINGLE_LIST_TYPE,       // Defines a single select list control
            String              = UF_STYLER_STRING_TYPE,            // Defines a string control
            ToggleButton        = UF_STYLER_TOGGLE_TYPE,            // Defines a toggle button control
            ToolPalette         = UF_STYLER_TOOL_PALETTE_TYPE,      // Defines a tool palette control
            WideString          = UF_STYLER_WIDE_STRING_TYPE,       // Defines a wide string control
            Invalid             = UF_STYLER_INVALID_TYPE            // Defines an invalid control
        };

        // Retrieves the ID of the associated dialog
        int askDialogID ( ) const;

        // Retrieves the control type
        virtual UgUIControl::ControlType askType ( ) const;

        // Retrieves the associated dialog
        const UgUIDialog * getDialog ( ) const;

        // Determines if the control is visible
        virtual bool isVisible ( ) const;

        // Determines if the control is sensitive
        virtual bool isSensitive ( ) const;

        // Sets the visibility
        virtual void setVisible
        (
            bool visible    // <I>
                            // Visibility status of the control
        );

        // Sets the sensitivity
        virtual void setSensitive
        (
            bool sensitive  // <I>
                            // Sensitivity status of the control
        );

    protected:
        // Retrieves the control ID
        const char* askControlID ( ) const;

        // Retrieves a boolean property
        bool getBool
        (
            int property    // <I>
                            // ID of property to retrieve
        ) const;

        // Retrieves an integer property
        int getInt
        (
            int property    // <I>
                            // ID of property to retrieve
        ) const;

        // Retrieves an array of integer properties
        const std::vector< int > getInts
        (
            int property    // <I>
                            // ID of property to retrieve
        ) const;

        // Retrieves a double property
        double getDouble
        (
            int property    // <I>
                            // ID of property to retrieve
        ) const;

        // Retrieves an array of double properties
        const std::vector< double > getDoubles
        (
            int property    // <I>
                            // ID of property to retrieve
        ) const;

        // Retrieves a string property
        std::string getString
        (
            int property    // <I>
                            // ID of property to retrieve
        ) const;

        // Retrieves an array of string properties
        const std::vector< std::string > getStrings
        (
            int property    // <I>
                            // ID of property to retrieve
        ) const;

        // Sets the dialog associated with the control
        void setDialog
        (
            const UgUIDialog *dialog    // <I>
                                        // Dialog associated with the
                                        // control
        );

        // Sets a property
        void setProperty
        (
            int property    // <I>
                            // ID of property to set
        );

        // Sets a property subitem
        void setPropertySubitem
        (
            int property,   // <I>
                            // ID of property to set
            int subitem     // <I>
                            // Subitem to set
        );

        // Sets a boolean property
        void setBool
        (
            int   property, // <I>
                            // ID of property to set
            bool  value     // <I>
                            // Value of the boolean
        );

        // Sets an integer property
        void setInt
        (
            int   property, // <I>
                            // ID of property to set
            int   value     // <I>
                            // Value of the integer
        );

        // Sets an array of integer properties
        void setInts
        (
            int                        property, // <I>
                                                 // ID of property to set
            const std::vector< int >  &values    // <I>
                                                 // Array of integer values
        );

        // Sets a double property
        void setDouble
        (
            int     property,  // <I>
                               // ID of property to set
            double  value      // <I>
                               // Value of the double
        );

        // Sets an array of double properties
        void setDoubles
        (
            int                           property, // <I>
                                                    // ID of property to set
            const std::vector< double >  &values    // <I>
                                                    // Array of double values
        );

        // Sets a string property
        void setString
        (
            int                 property,   // <I>
                                            // ID of property to set
            const std::string  &value,      // <I>
                                            // Value of the string
            int                 index = 0   // <I>
                                            // Zero-based index of insertion
                                            // position (when inserting into list)
        );

        // Sets an array of string properties
        void setStrings
        (
            int                                property,  // <I>
                                                          // ID of property to set
            const std::vector< std::string >  &values,    // <I>
                                                          // Array of string values
            int                                index = 0  // <I>
                                                          // Zero-based index of
                                                          // insertion position (when
                                                          // inserting into list)
        );

        // Constructor
        UgUIControl
        (
            const std::string &control_id, // Identifying name of the control
            const UgUIDialog  *dialog      // Dialog associated with the
                                           // control
        );

        // Destructor
        virtual ~UgUIControl ( );

    private:
        // Identifying name of the control
        std::string    m_control_id;

        // Dialog associated with the control
        UgUIDialog    *m_dialog;

};

#undef EXPORTLIBRARY

#endif // UG_UI_CONTROL_INCLUDED
