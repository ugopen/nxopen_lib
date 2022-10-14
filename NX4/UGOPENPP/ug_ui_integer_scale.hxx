/*
===============================================================================

            Copyright (c) 1999-2000 Unigraphics Solutions, Incorporated
                      Unpublished - All rights reserved
===============================================================================

File Description:
    This file declares the interface for UIStyler integer scales.

Classes Declared:
    UgUIIntegerScale

================================================================================



*/

#ifndef UG_UI_INTEGER_SCALE_INCLUDED
#define UG_UI_INTEGER_SCALE_INCLUDED

#include <ug_ui_control.hxx>
#include <libopenintpp_exports.hxx>

///////////////////////////////////////////////////////////////////////////////
// This class provides an interface to UIStyler integer scale controls.
///////////////////////////////////////////////////////////////////////////////
class OPENINTPPEXPORT UgUIIntegerScale : public UgUIControl
{
    public:
        // Constructor
        UgUIIntegerScale
        (
            const std::string  &control_id, // Identifying name of the control
            const UgUIDialog   *dialog      // Dialog associated with the
                                            // control
        );

        // Destructor
        virtual ~UgUIIntegerScale ( );

        // Retrieves the scale value
        int getValue ( ) const;

        // Sets the scale labels
        void setLabels
        (
            const std::vector< std::string > &labels   // <I>
                                                       // Array of two scale labels
        );

        // Sets the scale limits
        void setLimits
        (
            const std::vector< int > &limits    // <I>
                                                // Array of two scale limits
        );

        // Sets the scale value
        void setValue
        (
            int value                           // <I>
                                                // Scale value
        );
};

#undef EXPORTLIBRARY

#endif // UG_UI_INTEGER_SCALE_INCLUDED
