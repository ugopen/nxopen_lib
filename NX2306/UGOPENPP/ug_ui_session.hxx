/*
===============================================================================

            Copyright (c) 1999-2000 Unigraphics Solutions, Incorporated
                      Unpublished - All rights reserved
===============================================================================

File Description:
    This file declares a class for handling user interface sessions.

Classes Declared:
    UgUISession

================================================================================



*/

#ifndef UG_UI_SESSION_INCLUDED
#define UG_UI_SESSION_INCLUDED

#include <stddef.h>
#include <ug_string.hxx>
#include <libopenintpp_exports.hxx>
#include <UGOpenCPP_NXDeprecation.hxx>

///////////////////////////////////////////////////////////////////////////////
// This class provides an interface to the Unigraphics user interface.
///////////////////////////////////////////////////////////////////////////////
class UGOPENCPP_DEPRECATED("Replacement functionality exists in NXOpen API. Consider replacing usage with NXOpen::UI.") OPENINTPPEXPORT UgUISession
{
    public:
        // Constructor
        UGOPENCPP_DEPRECATED("Replacement functionality exists in NXOpen API. Consider replacing usage with NXOpen::UI.") UgUISession ( );

        // Destructor
        UGOPENCPP_DEPRECATED("Replacement functionality exists in NXOpen API. Consider replacing usage with NXOpen::UI.") virtual ~UgUISession ( );

        // Display a message in the prompt area of the user interface
        UGOPENCPP_DEPRECATED("Replacement functionality exists in NXOpen API. Consider replacing usage with NXOpen::UI.") void setPromptMessage
        (
            const std::string &message   // <I>
                                         // Prompt message
        );

        // Display a message in the status area of the user interface
        UGOPENCPP_DEPRECATED("Replacement functionality exists in NXOpen API. Consider replacing usage with NXOpen::UI.") void setStatusMessage
        (
            const std::string &message   // <I>
                                         // Status message
        );

        // Refresh the display
        UGOPENCPP_DEPRECATED("Replacement functionality exists in NXOpen API. Consider replacing usage with NXOpen::UI.") void refresh ( ) const;
};

#undef EXPORTLIBRARY

#endif // UG_UI_SESSION_INCLUDED
