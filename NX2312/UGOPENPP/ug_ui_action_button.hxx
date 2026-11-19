/*
===============================================================================

            Copyright (c) 1999-2000 Unigraphics Solutions, Incorporated
                      Unpublished - All rights reserved
===============================================================================

File Description:
    This file declares the interface for UIStyler action buttons.

Classes Declared:
    UgUIActionButton

================================================================================



*/

#ifndef UG_UI_ACTION_BUTTON_INCLUDED
#define UG_UI_ACTION_BUTTON_INCLUDED

#include <ug_ui_control.hxx>
#include <libopenintpp_exports.hxx>
#include <UGOpenCPP_NXDeprecation.hxx>

///////////////////////////////////////////////////////////////////////////////
// This class provides an interface to UIStyler action button controls.
///////////////////////////////////////////////////////////////////////////////
class UGOPENCPP_DEPRECATED("Replacement functionality exists in NXOpen API. Consider replacing usage with NXOpen::BlockStyler namespace.") OPENINTPPEXPORT UgUIActionButton : public UgUIControl
{
    public:
        // Constructor
        UGOPENCPP_DEPRECATED("Replacement functionality exists in NXOpen API. Consider replacing usage with NXOpen::BlockStyler namespace.") UgUIActionButton
        (
            const std::string  &control_id, // Identifying name of the control
            const UgUIDialog   *dialog        // Dialog associated with the
                                            // control
        );

        // Destructor
        UGOPENCPP_DEPRECATED("Replacement functionality exists in NXOpen API. Consider replacing usage with NXOpen::BlockStyler namespace.") virtual ~UgUIActionButton ( );

        // Sets the button bitmap
        UGOPENCPP_DEPRECATED("Replacement functionality exists in NXOpen API. Consider replacing usage with NXOpen::BlockStyler namespace.") void setBitmap
        (
            const std::string &file        // <I>
                                        // Name of the bitmap file
        );

        // Sets the default action to this button
        UGOPENCPP_DEPRECATED("Replacement functionality exists in NXOpen API. Consider replacing usage with NXOpen::BlockStyler namespace.") void setDefaultAction ( );

        // Sets the focus to this button
        UGOPENCPP_DEPRECATED("Replacement functionality exists in NXOpen API. Consider replacing usage with NXOpen::BlockStyler namespace.") void setFocus ( );

        // Sets the button label
        UGOPENCPP_DEPRECATED("Replacement functionality exists in NXOpen API. Consider replacing usage with NXOpen::BlockStyler namespace.") void setLabel
        (
            const std::string &label    // <I>
                                        // Button label
        );
};

#undef EXPORTLIBRARY

#endif // UG_UI_ACTION_BUTTON_INCLUDED
