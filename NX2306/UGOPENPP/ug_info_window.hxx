/*
================================================================================

          Copyright (c) 1998-2000 Unigraphics Solutions Inc.
                    Unpublished - All rights reserved

================================================================================
  File description:

    Header file for NX Information Window C++ class definitions

================================================================================

*/

#ifndef UG_INFO_WINDOW_INCLUDED
#define UG_INFO_WINDOW_INCLUDED

// ****************************************************************************
// Include files for base classes and other needed types
// ****************************************************************************

#include <ug_openpp.hxx>
#include <ug_string.hxx>
#include <libopenpp_exports.hxx>
#include <UGOpenCPP_NXDeprecation.hxx>

// This class defines the interface for the creation and manipulation of NX information
// windows.  The information window is the device used to output textual information
// about any aspect of an NX session.
class UGOPENCPP_DEPRECATED("Replacement functionality exists in NXOpen API. Consider replacing usage with NXOpen::ListingWindow.") OPENPPEXPORT UgInfoWindow
{

    public:

        // Construct a UgInfoWindow object
        UGOPENCPP_DEPRECATED("Replacement functionality exists in NXOpen API. Consider replacing usage with NXOpen::ListingWindow.") UgInfoWindow ( );

        // Destroy a UgInfoWindow object
        UGOPENCPP_DEPRECATED("Replacement functionality exists in NXOpen API. Consider replacing usage with NXOpen::ListingWindow.") virtual ~UgInfoWindow ( );

        // Open the information window in NX.  In an external Open++ application,
        // this method has no effect, but it is benign.
        UGOPENCPP_DEPRECATED("Replacement functionality exists in NXOpen API. Consider replacing usage with NXOpen::ListingWindow.") static void open ( );

        // Write information to the information window in NX.  In an external Open++
        // applications this is equivalent to using 'cout'.
        UGOPENCPP_DEPRECATED("Replacement functionality exists in NXOpen API. Consider replacing usage with NXOpen::ListingWindow.") static void write
        (
            const std::string &buffer               // <I>
                                                    // The data that is to be written
                                                    // to the information window.
        );

        // Save the contents of the information window to a file.
        UGOPENCPP_DEPRECATED("Replacement functionality exists in NXOpen API. Consider replacing usage with NXOpen::ListingWindow.") static void save
        (
            const std::string &file_name            // <I>
                                                    // The file name to save the
                                                    // information window contents to
        );

        // Close the information window in NX.    In an external Open++ application,
        // this method has no effect, but it is benign.
        UGOPENCPP_DEPRECATED("Replacement functionality exists in NXOpen API. Consider replacing usage with NXOpen::ListingWindow.") static void close ( );

};

#undef EXPORTLIBRARY

#endif  // UG_INFO_WINDOW_INCLUDED
