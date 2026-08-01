/*
================================================================================

          Copyright (c) 1998-2000 Unigraphics Solutions Inc.
                    Unpublished - All rights reserved

================================================================================
  File description:

    Header file for NX session C++ class definitions

================================================================================

*/

#ifndef UG_SESSION_INCLUDED
#define UG_SESSION_INCLUDED

// ****************************************************************************
// Include files for base classes and other needed types
// ****************************************************************************

#include <ug_openpp.hxx>
#include <libopenpp_exports.hxx>

// ****************************************************************************
// Forward declarations for classes
// ****************************************************************************

class UgCoordSys;
class UgPart;

// This class defines the interface for the creation and manipulation of
// an object whose purpose is to access and change the environment of 
// an NX session.  Most of the methods are static so that an instance
// of this class is not needed.  However, at least one UgSession needs
// to be created and initialized so that the Open++ classes can
// have access to the Open API environment.
class OPENPPEXPORT UgSession
{
   
    public:

        // Construct a UgSession object.
        explicit UgSession
        (
            bool auto_initialize = false    // If true then auto-initialize
                                            // the Open API environment.
        );

        // Destroy a UgSession object.  If the invoking 
        // object was auto-initialized during construction 
        // then terminate the Open API environment.
        virtual ~UgSession ( ); 

        // Initialize the Open API environment.
        static void initialize ( );

        // Terminate the Open API environment.
        static void terminate ( );

        // Determine if the Open API environment has been initialized.
        static bool isInitialized ( );

        // Return the distance tolerance value in part units.  Any distance that is
        // less than or equal to the distance tolerance is considered by the session
        // to be a zero distance.
        static double getDistanceTolerance ( );

        // Return the angle tolerance value in radians.  Any angle that is less than or
        // equal to the angle tolerance is considered by the session to be a
        // zero angle.
        static double getAngleTolerance ( );

        // Return the Work Coordinate System.
        static UgCoordSys *getWCS ( );

        // Return the part that is currently displayed.
        static UgPart *getDisplayPart ( );

        // Return the part that is currently active as the work part
        static UgPart *getWorkPart ( );

        // Edit the distance tolerance value.  Any distance that is less than or
        // equal to the distance tolerance is considered by the session to be a
        // zero distance.
        static void setDistanceTolerance
        (
            double tolerance                // <I>
                                            // The new distance tolerance value in part units.
        );

        // Edit the angle tolerance value.  Any angle that is less than or
        // equal to the angle tolerance is considered by the session to be a
        // zero angle.
        static void setAngleTolerance
        (
            double tolerance                // <I>
                                            // The new angle tolerance value in radians.
        );

        // Change the Work Coordinate System.
        static void setWCS
        (
            const UgCoordSys *wcs           // <I>
                                            // The new Work Coordinate System.
        );

        // Set the display status of the Work Coordinate System.
        static void setWCSDisplay
        (
            bool display_status = true      // <I>
                                            // If true, the Work Coordinate System
                                            // will be displayed; if false, the
                                            // Work Coordinate System will not be
                                            // displayed.
        );

        // Change the part that is currently displayed.
        static void setDisplayPart
        (
            const UgPart *display_part      // <I>
                                            // The part to be made the new currently displayed
                                            // part.
        );

        // Change the part that is currently active as the work part
        static void setWorkPart
        (
            const UgPart *work_part         // <I>
                                            // The part to be made the new currently active
                                            // work part.
        ); 
         
        // Edit the layer status.
        static void setLayerStatus
        (
            int layer_number,               // <I>
                                            // The layer whose status is to be changed.
            int layer_status                // <I>
                                            // The new layer status value.
        );

        // Refresh the display.
        static void refreshDisplay ( );

        // Trigger an update.
        static void update ( );

        // Close all currently open parts.
        static void closeAllParts ( );

    private:

        // Value to determine if this object initialized the Open API session.
        bool m_auto_initialize;

};

#undef EXPORTLIBRARY

#endif  // UG_SESSION_INCLUDED
