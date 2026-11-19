/*
===============================================================================

            Copyright (c) 1999-2000 Unigraphics Solutions, Incorporated
                      Unpublished - All rights reserved
===============================================================================

File Description:
    This file declares the interface for UIStyler real scales.

Classes Declared:
    UgUIRealScale

================================================================================



*/

#ifndef UG_UI_REAL_SCALE_INCLUDED
#define UG_UI_REAL_SCALE_INCLUDED

#include <ug_ui_control.hxx>
#include <libopenintpp_exports.hxx>

///////////////////////////////////////////////////////////////////////////////
// This class provides an interface to UIStyler real scale controls.
///////////////////////////////////////////////////////////////////////////////
class OPENINTPPEXPORT UgUIRealScale : public UgUIControl
{
    public:
        // Constructor
        UgUIRealScale
        (
            const std::string  &control_id, // Identifying name of the control
            const UgUIDialog   *dialog      // Dialog associated with the
                                            // control
        );

        // Destructor
        virtual ~UgUIRealScale ( );

        // Retrieves the scale value
        double getValue ( ) const;

        // Sets the scale precision
        void setPrecision
        (
            int precision                       // <I>
                                                // Decimal precision
        );

        // Sets the scale labels
        void setLabels
        (
            const std::vector< std::string > &labels   // <I>
                                                       // Array of two scale labels
        );

        // Sets the scale limits
        void setLimits
        (
            const std::vector< double > &limits   // <I>
                                                  // Array of two scale limits
        );

        // Sets the scale value
        void setValue
        (
            double value                        // <I>
                                                // Scale value
        );
};

#undef EXPORTLIBRARY

#endif // UG_UI_REAL_SCALE_INCLUDED
