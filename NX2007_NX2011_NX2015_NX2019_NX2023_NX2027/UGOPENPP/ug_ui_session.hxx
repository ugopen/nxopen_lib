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

///////////////////////////////////////////////////////////////////////////////
// This class provides an interface to the Unigraphics user interface.
///////////////////////////////////////////////////////////////////////////////
class OPENINTPPEXPORT UgUISession  
{
    public:
        // Constructor
        UgUISession ( );

        // Destructor
        virtual ~UgUISession ( );

        // Display a message in the prompt area of the user interface
        void setPromptMessage
        (
            const std::string &message   // <I>
                                         // Prompt message
        );

        // Display a message in the status area of the user interface
        void setStatusMessage
        (
            const std::string &message   // <I>
                                         // Status message
        );

        // Refresh the display
        void refresh ( ) const;
};

#undef EXPORTLIBRARY

#endif // UG_UI_SESSION_INCLUDED
