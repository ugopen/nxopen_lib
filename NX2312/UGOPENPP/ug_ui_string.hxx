/*
===============================================================================

            Copyright (c) 1999-2000 Unigraphics Solutions, Incorporated
                      Unpublished - All rights reserved
===============================================================================

File Description:
    This file declares the interface for UIStyler string controls.

Classes Declared:
    UgUIString

================================================================================



*/

#ifndef UG_UI_STRING_INCLUDED
#define UG_UI_STRING_INCLUDED

#include <ug_ui_control.hxx>
#include <libopenintpp_exports.hxx>
#include <UGOpenCPP_NXDeprecation.hxx>

///////////////////////////////////////////////////////////////////////////////
// This class provides an interface to UIStyler string controls.
///////////////////////////////////////////////////////////////////////////////
class UGOPENCPP_DEPRECATED("Replacement functionality exists in NXOpen API. Consider replacing usage with NXOpen::BlockStyler namespace.") OPENINTPPEXPORT UgUIString : public UgUIControl
{
    public:
        // Constructor
        UGOPENCPP_DEPRECATED("Replacement functionality exists in NXOpen API. Consider replacing usage with NXOpen::BlockStyler namespace.") UgUIString
        (
            const std::string  &control_id, // Identifying name of the control
            const UgUIDialog   *dialog      // Dialog associated with the
                                            // control
        );

        // Destructor
        UGOPENCPP_DEPRECATED("Replacement functionality exists in NXOpen API. Consider replacing usage with NXOpen::BlockStyler namespace.") virtual ~UgUIString ( );

        // Retrieves the value
        UGOPENCPP_DEPRECATED("Replacement functionality exists in NXOpen API. Consider replacing usage with NXOpen::BlockStyler namespace.") const std::string getValue ( ) const;

        // Sets the bitmap
        UGOPENCPP_DEPRECATED("Replacement functionality exists in NXOpen API. Consider replacing usage with NXOpen::BlockStyler namespace.") void setBitmap
        (
            const std::string &file     // <I>
                                        // Name of the bitmap file
        );

        // Sets the focus to this control
        UGOPENCPP_DEPRECATED("Replacement functionality exists in NXOpen API. Consider replacing usage with NXOpen::BlockStyler namespace.") void setFocus ( );

        // Sets the label
        UGOPENCPP_DEPRECATED("Replacement functionality exists in NXOpen API. Consider replacing usage with NXOpen::BlockStyler namespace.") void setLabel
        (
            const std::string &label    // <I>
                                        // Label of the control
        );

        // Sets the value
        UGOPENCPP_DEPRECATED("Replacement functionality exists in NXOpen API. Consider replacing usage with NXOpen::BlockStyler namespace.") void setValue
        (
            const std::string &value    // <I>
                                        // Value of the control
        );


        // Sets the value
        UGOPENCPP_DEPRECATED("Replacement functionality exists in NXOpen API. Consider replacing usage with NXOpen::BlockStyler namespace.") void setValue
        (
            bool value                  // <I>
                                        // Boolean to be converted to a string
        );

        // Sets the value
        UGOPENCPP_DEPRECATED("Replacement functionality exists in NXOpen API. Consider replacing usage with NXOpen::BlockStyler namespace.") void setValue
        (
            int value                   // <I>
                                        // Integer to be converted to a string
        );

        // Sets the value
        UGOPENCPP_DEPRECATED("Replacement functionality exists in NXOpen API. Consider replacing usage with NXOpen::BlockStyler namespace.") void setValue
        (
            double value                // <I>
                                        // Double to be converted to a string
        );
};

#undef EXPORTLIBRARY

#endif // UG_UI_STRING_INCLUDED
