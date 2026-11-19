/*
================================================================================

          Copyright (c) 1998-1999 Unigraphics Solutions Inc.
                    Unpublished - All rights reserved

================================================================================
  File description:

    This file contains the definition for the Midcurve example class.

================================================================================

*/

/*  */

// ****************************************************************************
// Include files for needed types
// ****************************************************************************

#include <uf_exit.h>

#include <ufx_midcurve.hxx>

#include <ug_info_window.hxx>
#include <ug_exception.hxx>

#include <ug_vector.hxx>

#include <evaluator.hxx>

#include <point3.hxx>

#if !defined(__sgi) && ! (defined(__hpux) && !defined(_HP_NAMESPACE_STD)) || defined(__GNUG__)
#   include <strstream>
    using std::ostrstream;
    using std::endl;    
    using std::ends;
#else
#   include <strstream.h>
#endif

// The startup user exit that allows the MidCurve object to
// be registered when Unigraphics is invoked.
extern void ufsta 
(
    char *param,            // <I>
                            // Parameters -- unused
    int *retcod,            // <O>
                            // Return code.  Not used by Internal
                            // UG/Open API.
    int param_len           // <I>
                            // Length of param argument.  Unigraphics
                            // handles this input for you.
)
{
}


// ****************************************************************************
// Class implementation for MidCurve
// ****************************************************************************

UG_IMPLEMENT_FEATURE_CLASS ( MidCurve )

MidCurve::MidCurve ( )
{
}

MidCurve::~MidCurve ( )
{
}

// Return an array of equally spaced points evaluated on a UgEvaluatableObject object.
static const std::vector < Point3 > computeSamplePoints
(
    int                        n_points,    // <I>
                                            // The number of points to return
    const UgEvaluatableObject *curve        // <I>
                                            // The object to evaluate the points on
)
{
    // Get the evaluator object of the input object
    Evaluator evaluator = curve->askEvaluator ( );

    // Construct an output array to hold the points
    std::vector < Point3 > points ( n_points );

    // Get the limits of the evaluator to determine the delta parameter,
    // and to inquire the parameter at which to start the iteration
    Interval interval = evaluator.askLimits ( );
    double   delta = interval.askLength ( ) / ( n_points - 1 );

    // Iterate to get all the points
    int      indx;
    double   param;
    for ( indx = 0, param = interval.getStart ( );
          indx < n_points;
          indx++, param += delta )
    {
        // Evaluate the point at the parameter and store the point in the output array.
        points [ indx ] = evaluator.evaluatePoint ( param );
    }

    return points;
}

// Return an array of points through which the MidCurve object will pass.
static const std::vector < Point3 > computeThruPoints
(
    int                        n_points,    // <I>
                                            // The number of points to return
    const UgEvaluatableObject *curve1,      // <I>
                                            // The first generating object
    const UgEvaluatableObject *curve2       // <I>
                                            // The second generating object
)
{
    // Get an array of sample points from each generating object
    std::vector < Point3 > sample_points1 = computeSamplePoints ( n_points, curve1 );
    std::vector < Point3 > sample_points2 = computeSamplePoints ( n_points, curve2 );

    // Construct an output array to hold the points
    std::vector < Point3 > thru_points ( n_points );

    // Iterate to get all the points
    for ( int indx = 0; indx < n_points; indx++ )
    {
        // Calculate the mid-point between corresponding points in the sample arrays
        // and store the point in the output array.
        const Point3 pt1 = sample_points1 [ indx ];
        const Point3 pt2 = sample_points2 [ indx ];

        thru_points [ indx ] = pt1 + 0.5 * ( pt2 - pt1 );
    }

    return thru_points;
}

// Create a MidCurve object that passes through the midpoints between the given  
// generating objects.
MidCurve *MidCurve::create 
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
)
{
    // Allocate new memory to hold the MidCurve object
    MidCurve *midcurve = new MidCurve ( );

    // Initialize the MidCurve object within a try block
    try
    {
        midcurve->initialize ( n_points, curve1, curve2, part_or_object );
    }

    // If an exception was thrown from MidCurve::initialize ( ), delete the 
    // MidCurve object and re-throw
    catch ( const UgException & )
    {
        delete midcurve;

        throw;
    }

    return midcurve;
}

// Initialize a MidCurve object by actually creating a UG database
// spline and a UG database UDO that corresponds to a MidCurve object
// that passes through the midpoints between the given generating 
// objects.
void MidCurve::initialize 
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
)
{
    // Construct an array of points through which the MidCurve object will
    // pass through
    std::vector < Point3 > thru_points = computeThruPoints ( n_points, curve1, curve2 );

    // Use the array of points to initialize the cubic UgSpline object via the
    // initialize ( ) method from that class.  The scope operator is required
    // to invoke this method because there is a MidCurve method of the same name.
    // The spline is initialized to be not periodic of order 4, to pass through
    // the required points and to use a default parameterization.
    UgSpline::initialize ( false, 4, thru_points, NoParameters, part_or_object );

    // Initialize the properties of the MidCurve object that distinguishes this
    // object from a normal UgSpline object.  These methods are generated by
    // the macros in the class declaration.
    setNPoints ( n_points );
    setCurve1 ( curve1 );
    setCurve2 ( curve2 );
}

// This method provides information about the invoking object.
void MidCurve::infoObject ( )
{
    // Surround this method in a try block because it is invoked within
    // Unigraphics, and Unigraphics cannot handle C++ exceptions
    try
    {
        // Construct a buffer to hold the text.
        ostrstream buffer;

        // Initialize the buffer with the required text.  The inherited method
        // computeArcLength is invoked in this example.
        buffer << "The arc length of the MidCurve is: ";
        buffer << computeArcLength ( ) << endl << ends;
        
        // Write the text to the UgInfoWindow.  The UgInfoWindow is assumed to
        // be open because this is the infoObject method.  The str method
        // freezes the buffer, so it must be unfrozen afterwards.
        UgInfoWindow::write ( buffer.str ( ) );
        buffer.rdbuf ( )->freeze ( 0 );
    }

    // Catch any exception that occurs so that the exception does not get passed
    // to Unigraphics, and output the error in a UgInfoWindow so that the user
    // can be aware than an exception has occurred.
    catch ( const UgException &exception )
    {
        exception.processError ( );
    }
}

// This method updates the invoking object.  This method will be
// invoked whenever one or both of the linked curves of the
// MidCurve object is changed.
void MidCurve::update
(
    UgTypedObject *updated_object        // <I>
                                         // The linked object that has
                                         // been changed
)
{
    // Surround this method in a try block because it is invoked within
    // Unigraphics, and Unigraphics cannot handle C++ exceptions
    try
    {
        // Get the properties of the MidCurve object that distinguishes this
        // object from a normal UgSpline object.  These methods are generated by
        // the macros in the class declaration.
        const int                        nPoints = getNPoints ( );
        const UgEvaluatableObject       *pCurve1 = getCurve1 ( );
        const UgEvaluatableObject       *pCurve2 = getCurve2 ( );

        // Test to insure that both generating objects are alive at the moment of
        // updating.  This is done because one or both of the objects could be a
        // UgEdge object that may be currently asleep.
        if ( pCurve1->isAlive ( ) && pCurve2->isAlive ( ) )
        {
            // Construct a new array of points through which the MidCurve object will
            // pass through.  If the generating objects have changed, then the points
            // will change.
            std::vector < Point3 > thru_points = computeThruPoints ( nPoints, pCurve1, pCurve2 );

            // Edit the UgSpline object to pass through the new array of points, keeping
            // the periodicity and the order the same, but using the default argument 
            // for parameters.
            setThruPoints ( isClosed ( ), getOrder ( ), thru_points );
        }
    }

    // Catch any exception that occurs so that the exception does not get passed
    // to Unigraphics, and output the error in a UgInfoWindow so that the user
    // can be aware than an exception has occurred.
    catch ( const UgException &exception )
    {
        exception.processError (  );
    }
}
