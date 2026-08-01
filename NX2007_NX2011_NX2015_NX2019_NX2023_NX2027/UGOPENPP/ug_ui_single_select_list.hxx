/*
===============================================================================

            Copyright (c) 1999-2000 Unigraphics Solutions, Incorporated
                      Unpublished - All rights reserved
===============================================================================

File Description:
    This file declares the interface for UIStyler single selection lists.

Classes Declared:
    UgUISingleSelectList

================================================================================



*/

#ifndef UG_UI_SINGLE_SELECT_LIST_INCLUDED
#define UG_UI_SINGLE_SELECT_LIST_INCLUDED

#include <ug_ui_list.hxx>
#include <libopenintpp_exports.hxx>

///////////////////////////////////////////////////////////////////////////////
// This class provides an interface to UIStyler single selection list controls.
///////////////////////////////////////////////////////////////////////////////
class OPENINTPPEXPORT UgUISingleSelectList : public UgUIList
{
    public:
        // Constructor
        UgUISingleSelectList
        (
            const std::string  &control_id, // Identifying name of the control
            const UgUIDialog   *dialog      // Dialog associated with the
                                            // control
        );

        // Destructor
        virtual ~UgUISingleSelectList ( );

        // Sets the focus to this control
        void setFocus ( );
};

#undef EXPORTLIBRARY

#endif // UG_UI_SINGLE_SELECT_LIST_INCLUDED
