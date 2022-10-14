/*
================================================================================

          Copyright (c) 1998-2000 Unigraphics Solutions Inc.
                    Unpublished - All rights reserved

================================================================================
  File description:

    Header file for Geometric Conics C++ class definitions.

================================================================================

*/

#ifndef UG_CONIC_INCLUDED
#define UG_CONIC_INCLUDED

// ****************************************************************************
// Include files for base classes and other needed types
// ****************************************************************************

#include <ug_orientable.hxx>
#include <ug_curve.hxx>
#include <libopenpp_exports.hxx>

// This class defines the interface for the creation and manipulation of
// NX conic objects.  It is foreseen that this class will contain the 
// create methods for loft conics.
class OPENPPEXPORT UgConicObject : public UgCurveObject, 
                                        public UgOrientableObject
{

    public:

        // Edit the center point of the invoking object.
        virtual void setCenterPoint
        (
            const Point3    &center_point   // <I>
                                            // The new center point in Absolute
                                            // Coordinate System coordinates of the conic
        ) = 0;
        
    protected:

        // Construct a UgConicObject object
        UgConicObject
        (
            tag_t tag = NULL_TAG            // The tag of the NX database conic that the
                                            // UgConicObject object corresponds to.
        );

        // Destroy a UgConicObject object
        virtual ~UgConicObject ( );

};

#undef EXPORTLIBRARY

#endif  // UG_CONIC_INCLUDED
