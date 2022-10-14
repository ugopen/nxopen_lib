/*
===============================================================================

            Copyright (c) 1999-2000 Unigraphics Solutions, Incorporated
                      Unpublished - All rights reserved
===============================================================================

File Description:
    This file declares the interface for UIStyler multi-select lists.

Classes Declared:
    UgUIMultiSelectList

================================================================================



*/

#ifndef UG_UI_MULTI_SELECT_LIST_INCLUDED
#define UG_UI_MULTI_SELECT_LIST_INCLUDED

#include <ug_ui_list.hxx>
#include <libopenintpp_exports.hxx>

///////////////////////////////////////////////////////////////////////////////
// This class provides an interface to UIStyler multi-select list controls.
///////////////////////////////////////////////////////////////////////////////
class OPENINTPPEXPORT UgUIMultiSelectList : public UgUIList
{
    public:
        // Constructor
        UgUIMultiSelectList
        (
            const std::string  &control_id, // Identifying name of the control
            const UgUIDialog   *dialog      // Dialog associated with the
                                            // control
        );

        // Destructor
        virtual ~UgUIMultiSelectList ( );

        // Retrieves the index of the first selected item
        int askSelectedIndex ( ) const;

        // Retrieves the indices of all selected items
        const std::vector< int > askSelectedIndices ( ) const;

        // Retrieves the names of the currently selected items
        const std::vector< std::string > askSelectedNames ( ) const;

        // Sets the focus to this control
        void setFocus ( );
};

#undef EXPORTLIBRARY

#endif // UG_UI_MULTI_SELECT_LIST_INCLUDED
