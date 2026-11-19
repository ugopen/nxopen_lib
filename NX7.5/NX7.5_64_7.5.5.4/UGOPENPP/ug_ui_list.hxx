/*
===============================================================================

            Copyright (c) 1999-2000 Unigraphics Solutions, Incorporated
                      Unpublished - All rights reserved
===============================================================================

File Description:
    This file declares the interface for UIStyler lists.

Classes Declared:
    UgUIList

================================================================================



*/

#ifndef UG_UI_LIST_INCLUDED
#define UG_UI_LIST_INCLUDED

#include <ug_ui_control.hxx>
#include <libopenintpp_exports.hxx>

///////////////////////////////////////////////////////////////////////////////
// This is an abstract base class for UIStyler list controls. It provides
// basic list functionality.
///////////////////////////////////////////////////////////////////////////////
class OPENINTPPEXPORT UgUIList : public UgUIControl
{
    public:
        // Retrieves the list
        virtual const std::vector< std::string > getList ( ) const;

        // Retrieves the currently selected item
        virtual int askSelectedIndex ( ) const;

        // Deselects an item in the list
        virtual void deselect
        (
            int index               // <I>
                                    // Zero-based index of the item
        );

        // Deletes an item in the list
        virtual void erase
        (
            int index               // <I>
                                    // Zero-based index of the item
        );

        // Inserts an item into the list
        virtual void insert
        (
            const std::string   &item,   // <I>
                                         // Item to insert
            int                  index   // <I>
                                         // Zero-based index in list to
                                         // insert before
        );

        // Inserts multiple items into the list
        virtual void insert
        (
            const std::vector< std::string >  &items,  // <I>
                                                       // Items to insert
            int                                index   // <I>
                                                       // Zero-based index in
                                                       // list to insert before
        );

        // Selects an item in the list
        virtual void select
        (
            int index               // <I>
                                    // Zero-based index of the item
        );

        // Sets the list
        virtual void setList
        (
            const std::vector< std::string >  &list  // <I>
                                                     // Item list
        );

        // Scrolls the list so that the specified item is visible at the top
        virtual void show
        (
            int index               // <I>
                                    // Zero-based index of the item
        );

    protected:
        // Constructor
        UgUIList
        (
            const std::string  &control_id, // Identifying name of the control
            const UgUIDialog   *dialog      // Dialog associated with the
                                            // control
        );

        // Destructor
        virtual ~UgUIList ( );
};

#undef EXPORTLIBRARY

#endif // UG_UI_LIST_INCLUDED
