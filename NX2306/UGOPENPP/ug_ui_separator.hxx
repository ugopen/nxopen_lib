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
#include <UGOpenCPP_NXDeprecation.hxx>

///////////////////////////////////////////////////////////////////////////////
// This class provides an interface to UIStyler separator controls.
///////////////////////////////////////////////////////////////////////////////
class UGOPENCPP_DEPRECATED("Replacement functionality exists in NXOpen API. Consider replacing usage with NXOpen::BlockStyler namespace.") OPENINTPPEXPORT UgUISeparator : public UgUIControl
{
    public:
        // Constructor
        UGOPENCPP_DEPRECATED("Replacement functionality exists in NXOpen API. Consider replacing usage with NXOpen::BlockStyler namespace.") UgUISeparator
        (
            const std::string  &control_id, // Identifying name of the control
            const UgUIDialog   *dialog      // Dialog associated with the
                                            // control
        );

        // Destructor
        UGOPENCPP_DEPRECATED("Replacement functionality exists in NXOpen API. Consider replacing usage with NXOpen::BlockStyler namespace.") virtual ~UgUISeparator ( );

        // Determines if the control is sensitive (always returns false
        // because separators are never sensitive)
        UGOPENCPP_DEPRECATED("Replacement functionality exists in NXOpen API. Consider replacing usage with NXOpen::BlockStyler namespace.") bool isSensitive ( ) const;

        // Sets the sensitivity (overridden to do nothing because separator
        // sensitivity cannot be set)
        UGOPENCPP_DEPRECATED("Replacement functionality exists in NXOpen API. Consider replacing usage with NXOpen::BlockStyler namespace.") void setSensitive
        (
            bool sensitive  // <I>
                            // Sensitivity status of the control
        );
};

#undef EXPORTLIBRARY

#endif // UG_UI_SEPARATOR_INCLUDED
