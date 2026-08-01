/*
===============================================================================

            Copyright (c) 1999-2000 Unigraphics Solutions, Incorporated
                      Unpublished - All rights reserved
===============================================================================

File Description:
    This file declares the interface for UIStyler separators.

Classes Declared:
    UgUISeparator

================================================================================



*/

#ifndef UG_UI_SEPARATOR_INCLUDED
#define UG_UI_SEPARATOR_INCLUDED

#include <ug_ui_control.hxx>
#include <libopenintpp_exports.hxx>

///////////////////////////////////////////////////////////////////////////////
// This class provides an interface to UIStyler separator controls.
///////////////////////////////////////////////////////////////////////////////
class OPENINTPPEXPORT UgUISeparator : public UgUIControl
{
    public:
        // Constructor
        UgUISeparator
        (
            const std::string  &control_id, // Identifying name of the control
            const UgUIDialog   *dialog      // Dialog associated with the
                                            // control
        );

        // Destructor
        virtual ~UgUISeparator ( );

        // Determines if the control is sensitive (always returns false
        // because separators are never sensitive)
        bool isSensitive ( ) const;

        // Sets the sensitivity (overridden to do nothing because separator
        // sensitivity cannot be set)
        void setSensitive
        (
            bool sensitive  // <I>
                            // Sensitivity status of the control
        );
};

#undef EXPORTLIBRARY

#endif // UG_UI_SEPARATOR_INCLUDED
