/*
================================================================================

          Copyright (c) 1998 Unigraphics Solutions Inc.
                    Unpublished - All rights reserved

================================================================================
  File description:

    This file contains the declaration for the MidCurve object, and is
    part of an example that demonstrates how to extend an NX object.
    There are two source files that are used with this file:
    ufx_midcurve.cxx and ufx_midcurve_internal.cxx.
   
    Before discussing the functionality of the example, the udo, startup and
    application directories must be created in a location pointed to by
    one of the following environment variables -- UGII_SITE_DIR,
    UGII_VENDOR_DIR, and UGII_USER_DIR.
  
    For example, if UGII_USER_DIR=/my_custom_code, the directory 
    structure for my_custom_code would contain udo/, application/, and 
    startup/ as the three subdirectories.
                   
    The "udo/" directory contains the shared image obtained by compiling and
    linking ufx_midcurve.cxx. Neither the "application/" nor the
    "startup/" directories are used in this example.  ufx_midcurve_internal.cxx
    contains the normal internal user function ufusr(), and the shared image
    obtained by comiling and linking this source can be placed anywhere.
  
    The .ugii_env file needs to be customized with the following line:
  
        UGII_USER_DIR=<the parent directory of the udo, application, 
                       and startup directories>
  
    The user should refer to the documentation in the UDO chapter 
    of the Open C API (User Function) Reference Manual which describes the 
    use of the above directories in detail.
  
    The Unigraphics image executes all shared images found in udo/
    directory once during Unigraphics startup. Thus the shared 
    image corresponding to ufx_midcurve.cxx is executed 
    and registers the UDO methods that are used to extend an NX spline
    object to become a MidCurve object.  
  
    ******************************************************************
    ******************************************************************
    INSTRUCTIONS FOR WINDOWS/NT:
      1)  The file ufx_midcurve.cxx needs to be compiled and linked as
          a DLL. It needs to link against libopenpp.lib and
          libvmathpp.lib.  In addition, the preprocessor symbol
          IMPL_MIDCURVE needs to be defined so the the MidCurve class
          will be exported from the DLL.
      2)  The file ufx_midcurve_internal.cxx needs to be compiled and
          linked as a DLL. It needs to link against libugopenint.lib, 
          libopenpp.lib, AND the lib file created in the link of
          ufx_midcurve.dll above.
    ******************************************************************
    ******************************************************************
  
================================================================================

*/

#ifndef MIDCURVE_INCLUDED
#define MIDCURVE_INCLUDED

#if defined ( WIN32 )

#   if defined ( IMPL_MIDCURVE )
        // export Open++ classes from their implementation
#       define CLASS_DECL_MIDCURVE __declspec ( dllexport )
        // define templates at the implementation
#       define TEMPLATE_DECL_MIDCURVE
#   else
        // import Open++ classes from their implementation
#       define CLASS_DECL_MIDCURVE __declspec ( dllimport )
        // use templates from the implementation
#       define TEMPLATE_DECL_MIDCURVE extern
#   endif

#else

#   define CLASS_DECL_MIDCURVE
#   define TEMPLATE_DECL_MIDCURVE

#endif

// ****************************************************************************
// Include files for base classes and other needed types
// ****************************************************************************

#include <ug_extension.hxx>
#include <ug_spline.hxx>

// This class defines the interface for the creation and manipulation of
// MidCurve objects.  The MidCurve object is derived from the base 
// Unigraphics class UgSpline.  It is a cubic spline object that is constrained
// to contain the points in space that are exactly midway between
// corresponding points on two UgEvaluatableObject objects, considered generating
// objects.  E.g., A MidCurve object exists for two UgEvaluatableObject
// objects.  For any normalized parameter t0 of the two objects, the MidCurve 
// object will contain the point that is halfway between the point on
// the first generating object evaluated at t0 and the point on the
// second generating object evaluated at t0.
// NOTE: Use of any UgExtensionObject will cause NX to reserve a user function
// execute license for the entire NX session.  NX will crash if there is no user 
// function execute license available when the library which uses the 
// UgExtensionObject is loaded.
class CLASS_DECL_MIDCURVE MidCurve : public UgSpline, public UgExtensionObject {

    // The MidCurve will have the update behavior of a feature.
    UG_DECLARE_FEATURE_CLASS ( MidCurve )

    public:

        // Create a MidCurve object that passes through the 
        // midpoints between the given generating objects.
        static MidCurve *create 
        ( 
            int                        n_points, // <I>
                                                 // The number of points to sample 
                                                 // along the given generating
                                                 // objects.  These points are used
                                                 // to determine the midpoints that
                                                 // the MidCurve object will pass through.
            const UgEvaluatableObject *curve1,   // <I>
                                                 // The first generating object.
            const UgEvaluatableObject *curve2,   // <I>
                                                 // The second generating object.
            const UgObject            *part_or_object
                                                 // <I>
                                                 // This argument defines the owning part of
                                                 // the new object.  If the argument is a
                                                 // UgPart object, the argument is the owning
                                                 // part of the new object.  If the argument
                                                 // is not a UgPart object, the part that owns
                                                 // the argument is the owning part of the new
                                                 // object.
        );

        //  

        // This macro generates the 'int getNPoints ( ) const;' 
        // and 'void setNPoints ( int n_points )' methods.
        // 'getNPoints' returns the number of sample points of the invoking object.
        // 'setNPoints' edits the number of sample points of the invoking object.
        UG_INT_PROPERTY ( NPoints, 0 );

        // This macro generates the 'UgEvaluatableObject *getCurve1 ( ) const;' 
        // and 'void setCurve1 ( const UgEvaluatableObject *curve1 )' methods.
        // 'getCurve1' returns the first generating object of the invoking object.
        // 'setCurve1' edits the first generating object of the invoking object.
        UG_LINK1_PROPERTY ( UgEvaluatableObject, Curve1, 0 );

        // This macro generates the 'UgEvaluatableObject *getCurve2 ( ) const;' 
        // and 'void setCurve2 ( const UgEvaluatableObject *curve2 )' methods.
        // 'getCurve2' returns the second generating object of the invoking object.
        // 'setCurve2' edits the second generating object of the invoking object.
        UG_LINK1_PROPERTY ( UgEvaluatableObject, Curve2, 1 );

        //  

        // This method provides information about the invoking object.
        void infoObject ( );

        // This method updates the invoking object.  This method will be
        // invoked whenever one or both of the linked curves of the
        // MidCurve object is changed.
        void update
        (
            UgTypedObject *updated_object        // <I>
                                                 // The linked object that has
                                                 // been changed
        );

    protected:

        // Initialize a MidCurve object by actually creating an NX database
        // spline and an NX database UDO that corresponds to a MidCurve object
        // that passes through the midpoints between the given generating 
        // objects.
        void initialize
        ( 
            int                        n_points, // <I>
                                                 // The number of points to sample 
                                                 // along the given generating
                                                 // objects.  These points are used
                                                 // to determine the midpoints that
                                                 // the MidCurve object will pass through.
            const UgEvaluatableObject *curve1,   // <I>
                                                 // The first generating object.
            const UgEvaluatableObject *curve2,   // <I>
                                                 // The second generating object.
            const UgObject            *part_or_object
                                                 // <I>
                                                 // This argument defines the owning part of
                                                 // the new object.  If the argument is a
                                                 // UgPart object, the argument is the owning
                                                 // part of the new object.  If the argument
                                                 // is not a UgPart object, the part that owns
                                                 // the argument is the owning part of the new
                                                 // object.
        );

        // Construct a MidCurve object
        MidCurve ( );

        // Destroy a MidCurve object
        virtual ~MidCurve ( );

};

#endif  // MIDCURVE_INCLUDED
