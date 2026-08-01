/*
================================================================================

          Copyright (c) 1998-2000 Unigraphics Solutions Inc.
                    Unpublished - All rights reserved

================================================================================
  File description:

    Header file for Interval C++ class definitions.

================================================================================

*/

#ifndef INTERVAL_INCLUDED
#define INTERVAL_INCLUDED

// ****************************************************************************
// Include files for base classes and other needed types
// ****************************************************************************

#include <ug_openpp.hxx>
#include <libopenpp_exports.hxx>

// This class defines the data and the interface for the creation and
// manipulation of Interval objects.  An instance of this class represents
// a parameter interval, containing both the start and the end parameter.
// If an Interval object is returned via a UGOpen++ call, the start parameter
// is guaranteed to be less than the end parameter.  However, there are no
// such retrictions on a User created Interval object.
class OPENPPEXPORT Interval { 

    public:

        // Construct the Interval object [ 0.0, 1.0 ].
        Interval ( );

        // Construct the Interval object [ start, end ].
        Interval
        (
            double start,           // The start parameter of the Interval object.
            double end              // The end parameter of the Interval object.
        );

        // Destroy an Interval object.
        virtual ~Interval ( );

        // Return the length of the invoking object.
        double askLength ( ) const;

        // Return the start parameter of the invoking object.
        double getStart ( ) const;

        // Return the end parameter of the invoking object.
        double getEnd ( ) const;

        // Edit the start parameter of the invoking object.
        void setStart
        (
            double start            // <I>
                                    // The new start parameter of the invoking object.
        );

        // Edit the end parameter of the invoking object.
        void setEnd
        (
            double end              // <I>
                                    // The new end parameter of the invoking object.
        );

    private:

        // The start parameter of the Interval object.
        double m_start;

        // The end parameter of the Interval object.
        double m_end;
};

#undef EXPORTLIBRARY

#endif  // INTERVAL_INCLUDED
