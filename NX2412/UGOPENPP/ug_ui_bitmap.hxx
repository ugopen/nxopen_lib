/*
===============================================================================

            Copyright (c) 1999-2000 Unigraphics Solutions, Incorporated
                      Unpublished - All rights reserved
===============================================================================

File Description:
    This file declares the interface for UIStyler bitmaps.

Classes Declared:
    UgUIBitmap

================================================================================



*/

#ifndef UG_UI_BITMAP_INCLUDED
#define UG_UI_BITMAP_INCLUDED

#include <ug_ui_control.hxx>
#include <libopenintpp_exports.hxx>
#include <UGOpenCPP_NXDeprecation.hxx>

///////////////////////////////////////////////////////////////////////////////
// This class provides an interface to UIStyler bitmap controls.
///////////////////////////////////////////////////////////////////////////////
class UGOPENCPP_DEPRECATED("Replacement functionality exists in NXOpen API. Consider replacing usage with NXOpen::BlockStyler namespace.") OPENINTPPEXPORT UgUIBitmap : public UgUIControl
{
    public:
        // Constructor
        UGOPENCPP_DEPRECATED("Replacement functionality exists in NXOpen API. Consider replacing usage with NXOpen::BlockStyler namespace.") UgUIBitmap
        (
            const std::string &control_id, // Identifying name of the control
            const UgUIDialog  *dialog      // Dialog associated with the
                                           // control
        );

        // Destructor
        UGOPENCPP_DEPRECATED("Replacement functionality exists in NXOpen API. Consider replacing usage with NXOpen::BlockStyler namespace.") virtual ~UgUIBitmap ( );

        // Determines if the control is visible
        UGOPENCPP_DEPRECATED("Replacement functionality exists in NXOpen API. Consider replacing usage with NXOpen::BlockStyler namespace.") bool isVisible ( ) const;

        // Determines if the control is sensitive
        UGOPENCPP_DEPRECATED("Replacement functionality exists in NXOpen API. Consider replacing usage with NXOpen::BlockStyler namespace.") bool isSensitive ( ) const;

        // Sets the bitmap
        UGOPENCPP_DEPRECATED("Replacement functionality exists in NXOpen API. Consider replacing usage with NXOpen::BlockStyler namespace.") void setBitmap
        (
            const std::string &file   // <I>
                                      // Name of the bitmap file
        );

        // Sets the sensitivity (overridden to do nothing because bitmap
        // sensitivity cannot be set)
        UGOPENCPP_DEPRECATED("Replacement functionality exists in NXOpen API. Consider replacing usage with NXOpen::BlockStyler namespace.") void setSensitive
        (
            bool sensitive            // <I>
                                      // Sensitivity status of the control
        );

        // Sets the visibility (overridden to do nothing because bitmap
        // visibility cannot be set)
        UGOPENCPP_DEPRECATED("Replacement functionality exists in NXOpen API. Consider replacing usage with NXOpen::BlockStyler namespace.") void setVisible
        (
            bool visible              // <I>
                                      // Visibility status of the control
        );
};

#undef EXPORTLIBRARY

#endif // UG_UI_BITMAP_INCLUDED
