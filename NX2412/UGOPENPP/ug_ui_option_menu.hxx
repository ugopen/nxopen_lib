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
#include <UGOpenCPP_NXDeprecation.hxx>

///////////////////////////////////////////////////////////////////////////////
// This class provides an interface to UIStyler option menu controls.
///////////////////////////////////////////////////////////////////////////////
class UGOPENCPP_DEPRECATED("Replacement functionality exists in NXOpen API. Consider replacing usage with NXOpen::BlockStyler namespace.") OPENINTPPEXPORT UgUIOptionMenu : public UgUIControl
{
    public:
        // Constructor
        UGOPENCPP_DEPRECATED("Replacement functionality exists in NXOpen API. Consider replacing usage with NXOpen::BlockStyler namespace.") UgUIOptionMenu
        (
            const std::string  &control_id, // Identifying name of the control
            const UgUIDialog   *dialog      // Dialog associated with the
                                            // control
        );

        // Destructor
        UGOPENCPP_DEPRECATED("Replacement functionality exists in NXOpen API. Consider replacing usage with NXOpen::BlockStyler namespace.") virtual ~UgUIOptionMenu ( );

        // Retrieves the list
        UGOPENCPP_DEPRECATED("Replacement functionality exists in NXOpen API. Consider replacing usage with NXOpen::BlockStyler namespace.") const std::vector< std::string > getList ( ) const;

        // Retrieves the currently selected item
        UGOPENCPP_DEPRECATED("Replacement functionality exists in NXOpen API. Consider replacing usage with NXOpen::BlockStyler namespace.") int askSelectedIndex ( ) const;

        // Sets the bitmap
        UGOPENCPP_DEPRECATED("Replacement functionality exists in NXOpen API. Consider replacing usage with NXOpen::BlockStyler namespace.") void setBitmap
        (
            const std::string &file     // <I>
                                        // Name of the bitmap file
        );
        
        // Sets the label
        UGOPENCPP_DEPRECATED("Replacement functionality exists in NXOpen API. Consider replacing usage with NXOpen::BlockStyler namespace.") void setLabel
        (
            const std::string &label    // <I>
                                        // Label of the control
        );

        // Sets the sensitivity of the entire UgUIOptionMenu object
        UGOPENCPP_DEPRECATED("Replacement functionality exists in NXOpen API. Consider replacing usage with NXOpen::BlockStyler namespace.") virtual void setSensitive
        (
            bool sensitive              // <I>
                                        // Sensitivity status of the control
        );

        // Sets the sensitivity of a single item in the list
        UGOPENCPP_DEPRECATED("Replacement functionality exists in NXOpen API. Consider replacing usage with NXOpen::BlockStyler namespace.") virtual void setSensitive
        (
            bool sensitive,             // <I>
                                        // Sensitivity status of the item
            int  index                  // <I>
                                        // Zero-based index of the item
        );

        // Selects an item in the list
        UGOPENCPP_DEPRECATED("Replacement functionality exists in NXOpen API. Consider replacing usage with NXOpen::BlockStyler namespace.") void select
        (
            int index                   // <I>
                                        // Zero-based index of the item
        );

        // Sets the list
        UGOPENCPP_DEPRECATED("Replacement functionality exists in NXOpen API. Consider replacing usage with NXOpen::BlockStyler namespace.") void setList
        (
            const std::vector< std::string > &list   // <I>
                                                     // Item list
        );
};

#undef EXPORTLIBRARY

#endif // UG_UI_OPTION_MENU_INCLUDED
