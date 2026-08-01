/*
===============================================================================

            Copyright (c) 1999-2000 Unigraphics Solutions, Incorporated
                      Unpublished - All rights reserved
===============================================================================

File Description:
    This file declares an abstract base class for UIStyler containers. UIStyler
    controls that contain other UIStyler controls (e.g. button layout, radio
    box) qualify as containers. This class provides functionality for
    manipulating the child controls.

Classes Declared:
    UgUIContainer

================================================================================



*/

#ifndef UG_UI_CONTAINER_INCLUDED
#define UG_UI_CONTAINER_INCLUDED

#include <stddef.h>
#include <ug_ui_control.hxx>
#include <libopenintpp_exports.hxx>

///////////////////////////////////////////////////////////////////////////////
// This is an abstract base class for UIStyler container controls. UIStyler
// controls that contain other UIStyler controls (e.g. button layout, radio
// box) qualify as containers. This class provides functionality for
// manipulating the child controls.
///////////////////////////////////////////////////////////////////////////////
class OPENINTPPEXPORT UgUIContainer : public UgUIControl
{
    public:
        // Sets the sensitivity
        virtual void setSensitive
        (
            bool sensitive  // <I>
                            // Sensitivity status of the container
        );

        // Sets the subitem sensitivity
        virtual void setSubitemSensitive
        (
            int  index,     // <I>
                            // Zero-based index of the subitem
            bool sensitive  // <I>
                            // Sensitivity status of the subitem
        );

    protected:
        // Constructor
        UgUIContainer
        (
            const std::string  &control_id, // Identifying name of the control
            const UgUIDialog   *dialog      // Dialog associated with the
                                            // control
        );

        // Destructor
        virtual ~UgUIContainer ( );
};

#undef EXPORTLIBRARY

#endif // UG_UI_CONTAINER_INCLUDED
