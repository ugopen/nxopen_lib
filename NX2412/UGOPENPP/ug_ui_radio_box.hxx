/*
===============================================================================

            Copyright (c) 1999-2000 Unigraphics Solutions, Incorporated
                      Unpublished - All rights reserved
===============================================================================

File Description:
    This file declares the interface for UIStyler radio boxes.

Classes Declared:
    UgUIRadioBox

================================================================================



*/

#ifndef UG_UI_RADIO_BOX_INCLUDED
#define UG_UI_RADIO_BOX_INCLUDED

#include <ug_ui_container.hxx>
#include <libopenintpp_exports.hxx>
#include <UGOpenCPP_NXDeprecation.hxx>

///////////////////////////////////////////////////////////////////////////////
// This class provides an interface to UIStyler radio box controls.
///////////////////////////////////////////////////////////////////////////////
class UGOPENCPP_DEPRECATED("Replacement functionality exists in NXOpen API. Consider replacing usage with NXOpen::BlockStyler namespace.") OPENINTPPEXPORT UgUIRadioBox : public UgUIContainer
{
    public:
        // Constructor
        UGOPENCPP_DEPRECATED("Replacement functionality exists in NXOpen API. Consider replacing usage with NXOpen::BlockStyler namespace.") UgUIRadioBox
        (
            const std::string  &control_id, // Identifying name of the control
            const UgUIDialog   *dialog      // Dialog associated with the
                                            // control
        );

        // Destructor
        UGOPENCPP_DEPRECATED("Replacement functionality exists in NXOpen API. Consider replacing usage with NXOpen::BlockStyler namespace.") virtual ~UgUIRadioBox ( );

        // Retrieves the currently selected option
        UGOPENCPP_DEPRECATED("Replacement functionality exists in NXOpen API. Consider replacing usage with NXOpen::BlockStyler namespace.") int getValue ( ) const;

        // Sets the default action to this button
        UGOPENCPP_DEPRECATED("Replacement functionality exists in NXOpen API. Consider replacing usage with NXOpen::BlockStyler namespace.") void setDefaultAction ( );

        // Sets the label
        UGOPENCPP_DEPRECATED("Replacement functionality exists in NXOpen API. Consider replacing usage with NXOpen::BlockStyler namespace.") void setLabel
        (
            const std::string &label    // <I>
                                        // Label of the control
        );

        // Sets the selected radio option
        UGOPENCPP_DEPRECATED("Replacement functionality exists in NXOpen API. Consider replacing usage with NXOpen::BlockStyler namespace.") void setValue
        (
            int value                   // <I>
                                        // Selected option
        );
};

#undef EXPORTLIBRARY

#endif // UG_UI_RADIO_BOX_INCLUDED
