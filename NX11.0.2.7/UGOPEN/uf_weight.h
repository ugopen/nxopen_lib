/*******************************************************************************
    Copyright 1997 Siemens Product Lifecycle Management Software Inc.
    All rights reserved

 *

 File Description:
  This is the Open API interface to the Weight Management package

*******************************************************************************/



#ifndef UF_WEIGHT_INCLUDED
#define UF_WEIGHT_INCLUDED


/***************************************************************************

  ***************************************************************************/


#include <uf_defs.h>
#include <uf_weight_errors.h>
#include <libufun_exports.h>

#ifdef __cplusplus
extern "C" {
#endif


/***************************************************************************

    Definitions and Prototypes for the Open API interface routines for
    the Weight Management functionality.

*****************************************************************************/


/*
    Enum for possible units of mass and length for weight properties.
*/
enum UF_WEIGHT_units_type_e
{
    UF_WEIGHT_units_km = 0, /* Kilograms and meters */
    UF_WEIGHT_units_li,     /* Pounds and inches */
    UF_WEIGHT_units_lf,     /* Pounds and feet */
    UF_WEIGHT_units_gm,     /* Grams and millimeters */
    UF_WEIGHT_units_gc,     /* Grams and centimeters */
    UF_WEIGHT_units_custom, /* user selected units - reserved for internal use*/
    UF_WEIGHT_units_kmm     /* Kilograms and millimeters */
};

typedef enum UF_WEIGHT_units_type_e UF_WEIGHT_units_type_t,
                                   *UF_WEIGHT_units_type_p_t;


/*
    Values for weight property states.
*/

enum UF_WEIGHT_state_type_e
{
    UF_WEIGHT_no_cache  = 0, /* no data available */
    UF_WEIGHT_cached    = 1, /* The property or properties are the result of a
                               calculation on geometry. */
    UF_WEIGHT_asserted  = 2, /* The property or properties have been explicitly
                               asserted. */
    UF_WEIGHT_unknown   = 3, /* The property has been asserted to be unknown.*/
    UF_WEIGHT_inherited = 4, /* The properties on a component are an assertion
                               inherited from an assertion on a part. */
    UF_WEIGHT_implied   = 6  /* The property has been derived from other
                               properties. */
};

typedef enum UF_WEIGHT_state_type_e  UF_WEIGHT_state_type_t,
                                    *UF_WEIGHT_state_type_p_t;


/*
    Structure for passing weight management data.

    If the cache_state is UF_WEIGHT_no_cache, the geometric values and their
    errors are all set to 0.0, and the units to UF_WEIGHT_units_km.

    If the cache_state is UF_WEIGHT_asserted or UF_WEIGHT_inherited, then
    density, mass and volume are as follows:
    a) either mass is UF_WEIGHT_asserted and the other two are UF_WEIGHT_unknown
    b) or two of them are UF_WEIGHT_asserted and the third is UF_WEIGHT_implied.
    (This is the only situation in which UF_WEIGHT_implied can be used.)

    If the volume_state is UF_WEIGHT_unknown, then the cofm_state and the
    mofi_state will also be UF_WEIGHT_unknown.  If the cofm_state is
    UF_WEIGHT_unknown, then the mofi_state will be UF_WEIGHT_unknown.
*/

struct UF_WEIGHT_properties_s
{
    UF_WEIGHT_units_type_t units;
                           /* the units in which the rest of the data is
                              returned */
    UF_WEIGHT_state_type_t cache_state;
                           /* the state of the returned data.  This can be
                              UF_WEIGHT_no_cache if the data was not available,
                              UF_WEIGHT_cached if it was calculated from
                              geometry or other properties,
                              UF_WEIGHT_asserted if it was directly asserted,
                              and
                              UF_WEIGHT_inherited if it was data on a component
                              found from an assertion on a part.
                              It cannot be UF_WEIGHT_implied or
                              UF_WEIGHT_unknown. */
    double accuracy;
                           /* the accuracy of the calculated data when the
                              cache_state is UF_WEIGHT_cached, in which case it
                              must be 0.9, 0.99, 0.999, 0.9999, 0.99999 or
                              0.999999.  It is 1.0 if the cache_state is
                              UF_WEIGHT_asserted or UF_WEIGHT_inherited, or if
                              no solids were involved in the calculation. */
    double density;
                           /* the density of the data, equal to mass/volume.
                              This is 0.0 if the density_state is
                              UF_WEIGHT_unknown. */
    UF_WEIGHT_state_type_t density_state;
                           /* the state of the density data.  This is normally
                              the same value as cache_state, but it can be
                              UF_WEIGHT_unknown or UF_WEIGHT_implied if the
                              cache_state is UF_WEIGHT_asserted or
                              UF_WEIGHT_inherited. */
    double volume;
                           /* the volume of the data, equal to mass/density.
                              This is 0.0 is the density_state is
                              UF_WEIGHT_unknown. */
    double volume_error;
                           /* the estimated error range for the volume, in the
                              same units as the volume. */
    UF_WEIGHT_state_type_t volume_state;
                           /* the state of the volume data.  This is normally
                              the same value as cache_state, but it can be
                              UF_WEIGHT_unknown or UF_WEIGHT_implied if the
                              cache_state is UF_WEIGHT_asserted or
                              UF_WEIGHT_inherited. */
    double mass;
                           /* the mass of the data, equal to volume x density.
                              This is 0.0 if the mass_state is
                              UF_WEIGHT_unknown. */
    double mass_error;
                           /* the estimated error range for the mass, in the
                              same units as the mass. */
    UF_WEIGHT_state_type_t mass_state;
                           /* the state of the mass data.  This is normally
                              the same value as cache_state, but it can be
                              UF_WEIGHT_implied if the cache_state is
                              UF_WEIGHT_asserted or UF_WEIGHT_inherited. */
    double area;
                           /* the surface area of the data. */
    double area_error;
                           /* the estimated error range for the surface area,
                              in the same units as the area. */
    UF_WEIGHT_state_type_t area_state;
                           /* the state of the area field.  This is normally
                              the same value as cache_state, but it can be
                              UF_WEIGHT_unknown if the cache_state is
                              UF_WEIGHT_asserted or UF_WEIGHT_inherited. */
    double center_of_mass[3];
                           /* the X, Y and Z co-ordinates of the center of
                              mass, in absolute co-ordinates.  These are set
                              to 0.0 if the cofm_state is UF_WEIGHT_unknown. */
    double cofm_error;
                           /* the estimated error range for the center of mass,
                              in the same length units.  This represents the
                              radius of a sphere of uncertainty drawn around
                              the center of mass. */
    UF_WEIGHT_state_type_t cofm_state;
                           /* the state of the center of mass field.  This is
                              normally the same value as cache_state, but it
                              can be UF_WEIGHT_unknown if the cache_state is
                              UF_WEIGHT_asserted or UF_WEIGHT_inherited. */
    double moments_of_inertia[3];
                           /* the XX, YY and ZZ moments of inertia about the
                              center of mass (in that order), using absolute
                              co-ordinates.  These are set to 0.0 if the
                              mofi_state is UF_WEIGHT_unknown. */
    double products_of_inertia[3];
                           /* the XY, XZ and YZ products of inertia about the
                              center of mass (in that order), using absolute
                              co-ordinates.  These are set to 0.0 if the
                              mofi_state is UF_WEIGHT_unknown.  These values
                              follow the mathematical convention that the
                              products of inertia are usually negative, unlike
                              the convention followed by most engineers. */
    double mofi_error;
                           /* the estimated error range for the moments and
                              products of inertia, in the same units.  This
                              represents the +/- variation in each value. */
    UF_WEIGHT_state_type_t mofi_state;
                           /* the state of the moments and products of inertia
                              field.  This is normally the same value as
                              cache_state, but it can be UF_WEIGHT_unknown if
                              the cache_state is UF_WEIGHT_asserted or
                              UF_WEIGHT_inherited. */
};

typedef struct UF_WEIGHT_properties_s  UF_WEIGHT_properties_t,
                                      *UF_WEIGHT_properties_p_t;
typedef const UF_WEIGHT_properties_t* UF_WEIGHT_properties_pc_t;


/*
    Values for the different exceptions that can be generated while
    calculating weight data.
*/

enum UF_WEIGHT_exception_reason_e
{
    UF_WEIGHT_not_loaded            =  1,
                                  /*  The part or component is unloaded, and
                                      cached properties are not available for
                                      it. */
    UF_WEIGHT_insufficiently_loaded =  2,
                                  /*  The part or component is only partially
                                      loaded, but some necessary data is not
                                      loaded, and cached properties are not
                                      available for it. */
    UF_WEIGHT_ref_set_absent        =  3,
                                  /*  The solids in a part contributing to its
                                      weight properties are defined by a
                                      reference set not currently in the part.*/
    UF_WEIGHT_comp_set_absent       =  4,
                                  /*  The components of a part contributing to
                                      its weight properties are defined by a
                                      component set not currently in the part.*/
    UF_WEIGHT_under_minimum_weight  =  8,
                                  /*  The part or component is below its
                                      minimum weight limit. */
    UF_WEIGHT_over_maximum_weight   =  9,
                                  /*  The part or component is above its
                                      maximum weight limit. */
    UF_WEIGHT_has_assertion         = 11,
                                  /*  The part or component has asserted data
                                      on it. */
    UF_WEIGHT_insufficient_accuracy = 12,
                                  /*  The part or component is unloaded, or
                                      only partially loaded without some
                                      necessary data being loaded.  The only
                                      cache available was of lower accuracy
                                      than asked for. */
    UF_WEIGHT_incomplete_part       = 15,
                                  /*  The part or component is incomplete, 
                                      indicating that the assembly structure
                                      found in the part does not necessarily 
                                      represent the full assembly structure
                                      (for example, as known to TeamCenter). */                                      
                                      
    UF_WEIGHT_comp_group_not_uptodate   = 16,
                                  /*  Indicates that the component group 
                                      update has failed. */
                                      
    UF_WEIGHT_comp_group_updated_successfully = 17,
                                  /*  Indicates that the component group 
                                      has been successfully updated before 
                                      the weight calculation. */
                                      
    UF_WEIGHT_reference_only_component = 18,
                                  /*  The component is a Reference-Only component and
                                      these are excluded from the weight calculation. */

    UF_WEIGHT_excluded_from_spatial_search = 19,
                                  /*  The design element is excluded from spatial search
                                      and should be ignored during weight calculation. */

    UF_WEIGHT_promotion_with_source_suppressed = 20
                                  /*  Source body of a promoted body is in suppressed state. */
};


typedef enum UF_WEIGHT_exception_reason_e  UF_WEIGHT_exception_reason_t,
                                          *UF_WEIGHT_exception_reason_p_t;


/*
    Structure for returning exceptions generated while calculating weight data.

    All the fields except n_exceptions are arrays.
    Each element in turn describes a single exception;
    the nth element of each array describes the same exception.

     The entire exceptions struct must be initialised before use by calling
 UF_WEIGHT_init_exceptions

    The entire exceptions struct can be freed as a whole by calling
 UF_WEIGHT_free_exceptions


*/

struct UF_WEIGHT_exceptions_s
{
    int n_exceptions;
                   /* The total number of exceptions found. */
    UF_WEIGHT_exception_reason_t    *reasons;
                   /* <len:n_exceptions>
                      An array of UF_WEIGHT_exception_reasons_t's, detailing
                      the nature of each exception. */
    char **part_names;
                   /* <OF,len:n_exceptions>
                      Array of the names of the parts generating each exception.
                      Where a component generated the exception, the name of
                      its prototype part is given. */
    char **comp_names;
                   /* <OF,len:n_exceptions>
                      Array of the names of the components generating each
                      exception.  Where a part generated the exception, this
                      is the empty string "". */
    logical *on_part;
                   /* <len:n_exceptions>
                      Array of logicals.  True if a part generated the
                      exception, false if it was a component. */
    int *repeat_counts;
                   /*  The number of times the given exception (defined by the
                      reason and the part and/or component involved) occurred
                      during the traversal.  Because this field is present,
                      no two exceptions should be the same. */
};

typedef struct UF_WEIGHT_exceptions_s  UF_WEIGHT_exceptions_t,
                                      *UF_WEIGHT_exceptions_p_t;



/******************************************************************************
 *          P R O T O T Y P E    D E F I N I T I O N S                        *
 ******************************************************************************/


/*****************************************************************************
Ask the current weight properties of the part, component or solid
passed in.  If properties are not currently present on the part,
UF_WEIGHT_no_cache is returned as the cache state in properties.

This routine does not calculate the weights, this must have already been
done by calling UF_WEIGHT_estab_part_props, UF_WEIGHT_estab_comp_props or
UF_WEIGHT_estab_solid_props.

If object is a part, the properties returned are its own, exclusive of the
properties of any components it may have.  If object is a component,
the properties returned do not allow for the position of the
component in the assembly (use UF_WEIGHT_transform_props if
this is desired), and properties stored on the component's prototype
part will not be returned.  If object is a promotion, its returned cache,
if available, is the delta between the properties of the promotion
geometry and the properties of its base solid.

Like the other UF_WEIGHT routines that can take a solid as an
input argument, this routine requires that the solid is not suppressed,
is not a boolean tool, is not a sheet solid, and is not view dependent.
No solids in these categories can sensibly be given weight properties.

Environment: Internal  and  External

See Also:
 UF_WEIGHT_estab_part_props
 UF_WEIGHT_estab_comp_props
 UF_WEIGHT_estab_solid_props

History:
******************************************************************************/
extern UFUNEXPORT int UF_WEIGHT_ask_props (
const tag_t object ,/* <I>
                    Part, component or solid body whose weight
                    properties are wanted.
                    */
const UF_WEIGHT_units_type_t units ,/* <I>
                                    The units in which the properties are to be
                                    returned.
                                    */
UF_WEIGHT_properties_t * properties  /* <O>
                                     The current properties of object.
                                     */
);

/*****************************************************************************
Add together the elements of properties_array and return the result in
total_properties.  count gives the length of properties_array.  This
summation will combine the properties as if they represented actual
solid bodies of those properties, and returns the properties of those
solids considered as a set.

All the properties must be given in the same units.  If not,
UF_WEIGHT_incompatible_units is returned.

Environment: Internal  and  External

See Also:

History:
******************************************************************************/
extern UFUNEXPORT int UF_WEIGHT_sum_props (
const int count ,/* <I>
                 Number of properties structs in
                 properties_array.
                 */
UF_WEIGHT_properties_t * properties_array ,/* <I,len:count>
                                           The array of properties structs
                                           to be summed.
                                                 */
UF_WEIGHT_properties_t * total_properties  /* <O>
                                           The summed properties.
                                           */
);

/*****************************************************************************
Copy properties to a new struct new_properties with the same values.

Environment: Internal  and  External

See Also:

History:
******************************************************************************/
extern UFUNEXPORT int UF_WEIGHT_copy_props (
const UF_WEIGHT_properties_p_t properties ,/* <I>
                                         The specified properties.
                                         */
UF_WEIGHT_properties_t * new_properties  /* <O>
                                         A copy of properties.
                                         */
);

/*****************************************************************************
Copies the old_properties struct's values to a new struct new_properties,
whose units are given by units, but which is otherwise equivalent to
old_properties.

Environment: Internal  and  External

See Also:

History:
******************************************************************************/
extern UFUNEXPORT int UF_WEIGHT_convert_prop_units (
const UF_WEIGHT_properties_p_t old_properties ,/* <I>
                                             Weight properties to be converted
                                             to other units.
                                             */
const UF_WEIGHT_units_type_t new_units ,/* <I>
                                        The units to which the properties are
                                        to be converted.
                                        */
UF_WEIGHT_properties_t * new_properties  /* <O>
                                         properties, converted to units.
                                         */
);

/*****************************************************************************
Applies a transform to properties.  This routine can be used with
UF_ASSEM_ask_transform_of_occ to get the properties of an
occurrence given those of its prototype (this includes getting the
properties of a component given those of a part).  The caller must
ensure that the units of properties and transform are compatible.

The transform argument must be of the following form:
transform[0][0] to transform[2][2] must be an orthonormal (rotation) matrix.
transform[0][3] to transform[2][3] must be a translation vector.
transform[3][0] to transform[3][2] must be 0.0.
transform[3][3] (the scale factor) must be 1.0.

Environment: Internal  and  External

See Also:
 UF_ASSEM_ask_transform_of_occ

History:
******************************************************************************/
extern UFUNEXPORT int UF_WEIGHT_transform_props (
double transform[4][4] ,/* <I>
                        Transform to be applied to properties.
                        */
const UF_WEIGHT_properties_p_t properties ,/* <I>
                                         The current properties.
                                         */
UF_WEIGHT_properties_t * transformed_properties  /* <O>
                                                 The properties that result
                                                 from the transform.
                                                 */
);

/*****************************************************************************
Initialise an exceptions structure for use when establishing weight properties.
An initialised exceptions structure can be passed into more than one
establish routine, and the exceptions generated by each call will be
accumulated within the exceptions struct.  However, usually an
exceptions structure should be initialised before one call, and freed
immediately after that call and code to check that the exceptions
struct was filled correctly.

Environment: Internal  and  External

See Also:
 UF_WEIGHT_free_exceptions
 UF_WEIGHT_estab_part_props
 UF_WEIGHT_estab_comp_props
 UF_WEIGHT_estab_solid_props

History:
******************************************************************************/
extern UFUNEXPORT int UF_WEIGHT_init_exceptions (
UF_WEIGHT_exceptions_p_t exceptions  /* <I>
                                     The exceptions structure to be initialised.
                                     */
);

/*****************************************************************************
Free an exceptions structure used when establishing weight properties.

Environment: Internal  and  External

See Also:
 UF_WEIGHT_init_exceptions
 UF_WEIGHT_estab_part_props
 UF_WEIGHT_estab_comp_props
 UF_WEIGHT_estab_solid_props

History:
******************************************************************************/
extern UFUNEXPORT int UF_WEIGHT_free_exceptions (
UF_WEIGHT_exceptions_p_t exceptions  /* <I>
                                     The exceptions structure to be freed.
                                     */
);

/*****************************************************************************
Establish the weight properties of part, returning the result in
properties, given in units, and caching the calculated data on the part.
If recurse is true, include contributions from any of its components
present in the part's weight component set (and cache their own
contributions), otherwise include only solids in the part itself.  In
either case, any solids in the part in its weight reference set will
contribute.  This routine will use any assertions applicable.  The part
will be fully loaded.

Calculations of weight properties will be made to an accuracy of at
least accuracy; existing caches of that accuracy or greater will be used
where possible; elsewhere recalculations are made from individual
solids.  accuracy must be 0.9, 0.99, 0.999, 0.9999, 0.99999 or 0.999999.
exceptions must first be initialised by UF_WEIGHT_init_exceptions
and must be freed afterward by UF_WEIGHT_free_exceptions.

Environment: Internal  and  External

See Also:
 UF_WEIGHT_init_exceptions
 UF_WEIGHT_free_exceptions

History:
******************************************************************************/
extern UFUNEXPORT int UF_WEIGHT_estab_part_props (
const tag_t part ,/* <I>
                  The part whose weight properties are to be
                  established.
                  */
const double accuracy ,/* <I>
                       The accuracy to which the part's properties
                       are to be calculated.
                       */
const logical recurse ,/* <I>
                       True if the properties are to include
                       components of the part, false otherwise.
                       */
const UF_WEIGHT_units_type_t units ,/* <I>
                                    The units in which the properties are to be
                                    returned.
                                    */
UF_WEIGHT_properties_t * properties ,/* <O>
                                     The established properties of the part.
                                     */
UF_WEIGHT_exceptions_t * exceptions  /* <OF>
                                     Any exceptions encountered during the
                                     calculation.  This must be freed by
                                     calling UF_WEIGHT_free_exceptions.
                                     */
);

/*****************************************************************************
In order to provide appropriate .NET binding for UF_WEIGHT_estab_part_props, 
UF_WEIGHT_estab_part_props1 is introduced.

Note: C/C++ users can continue to use UF_WEIGHT_estab_part_props.

For docuementation, refer to documentation of UF_WEIGHT_estab_part_props.
*****************************************************************************/
extern UFUNEXPORT int UF_WEIGHT_estab_part_props1 (
const tag_t part ,/* <I>
                  The part whose weight properties are to be
                  established.
                  */
const double accuracy ,/* <I>
                       The accuracy to which the part's properties
                       are to be calculated.
                       */
const logical recurse ,/* <I>
                       True if the properties are to include
                       components of the part, false otherwise.
                       */
const UF_WEIGHT_units_type_t units ,/* <I>
                                    The units in which the properties are to be
                                    returned.
                                    */
UF_WEIGHT_properties_t * properties ,/* <O>
                                     The established properties of the part.
                                     */
UF_WEIGHT_exceptions_t ** exceptions  /* <OF>
                                     Any exceptions encountered during the
                                     calculation.  This must be freed by
                                     calling UF_WEIGHT_free_exceptions.
                                     */
);
/*****************************************************************************
Establish the weight properties of component, returning the result in
properties, given in units, and caching the calculated data on the
component.  The part containing the component will be fully loaded.
If recurse is true, include contributions from any of its children present
in the weight component set of the part containing the component
(and cache their own contributions), otherwise include only solids in
the component's part itself.  In either case, solids must be in the
weight reference set of their part to contribute.  This routine will use
any assertions applicable.

Calculations of weight properties will be made to an accuracy of at
least accuracy; existing caches of that accuracy or greater will be used
where possible; elsewhere recalculations are made from individual
solids.  accuracy must be 0.9, 0.99, 0.999, 0.9999, 0.99999 or 0.999999.
exceptions must first be initialised by UF_WEIGHT_init_exceptions
and must be freed afterward by UF_WEIGHT_free_exceptions.

Environment: Internal  and  External

See Also:
 UF_WEIGHT_init_exceptions
 UF_WEIGHT_free_exceptions

History:
******************************************************************************/
extern UFUNEXPORT int UF_WEIGHT_estab_comp_props (
const tag_t component ,/* <I>
                       The component whose properties are to be
                       calculated.
                       */
const double accuracy ,/* <I>
                       The accuracy to which the component's
                       properties are to be calculated.
                       */
const logical recurse ,/* <I>
                       True if the properties are to include the
                       component's child components, false
                       otherwise.
                       */
const UF_WEIGHT_units_type_t units ,/* <I>
                                    The units in which the properties are to be
                                    returned.
                                    */
UF_WEIGHT_properties_t * properties ,/* <O>
                                     The established properties of the
                                     component.
                                     */
UF_WEIGHT_exceptions_t * exceptions  /* <OF>
                                     Any exceptions encountered during the
                                     calculation.  This structure must be
                                     freed by calling UF_WEIGHT_free_exceptions
                                     */
);
/*****************************************************************************
In order to provide appropriate .NET binding for UF_WEIGHT_estab_comp_props, 
UF_WEIGHT_estab_comp_props1 is introduced.

Note: C/C++ users can continue to use UF_WEIGHT_estab_comp_props.

For docuementation, refer to documentation of UF_WEIGHT_estab_comp_props.
*****************************************************************************/
extern UFUNEXPORT int UF_WEIGHT_estab_comp_props1
(
    const tag_t component ,/* <I>
                       The component whose properties are to be
                       calculated.
                       */
const double accuracy ,/* <I>
                       The accuracy to which the component's
                       properties are to be calculated.
                       */
const logical recurse ,/* <I>
                       True if the properties are to include the
                       component's child components, false
                       otherwise.
                       */
const UF_WEIGHT_units_type_t units ,/* <I>
                                    The units in which the properties are to be
                                    returned.
                                    */
UF_WEIGHT_properties_t * properties ,/* <O>
                                     The established properties of the
                                     component.
                                     */
UF_WEIGHT_exceptions_t **exceptions  /* <OF,free:UF_WEIGHT_free_exceptions>
                                     Any exceptions encountered during the
                                     calculation.  This structure must be
                                     freed by calling UF_WEIGHT_free_exceptions
                                     */
);

/*****************************************************************************
Establish the weight properties of solid, returning the result in
properties, given in units, and caching the calculated data on the solid.
Note that exceptions are not applicable to this lower level routine.

Calculations of weight properties will be made to an accuracy of at
least accuracy; existing caches of that accuracy or greater will be used
where possible; elsewhere recalculations are made from individual
solids.  accuracy must be 0.9, 0.99, 0.999, 0.9999, 0.99999 or 0.999999.

If solid is in the work part, a cache is written on it (if an existing cache
was not available).  Otherwise, the relevant properties are still
returned, but no cache is written.  solid can be a solid occurrence
instead of a solid.  If so, the properties returned are those of the
prototype solid with an appropriate transform applied.  A cache is
written on the prototype solid if it is in the work part, but never on a
solid occurrence.

Like the other UF_WEIGHT routines that can take a solid as an
input argument, this routine requires that the solid is not suppressed,
is not a boolean tool, is not a sheet solid, and is not view dependent.
No solids in these categories can sensibly be given weight properties.
If solid is a promotion, its returned cache is the delta between the
properties of the promotion geometry and the properties of its base
solid.  This ensures that any calculation including both the promotion
and its base returns the correct answer (i.e. the properties of the
promoted geometry).

Environment: Internal  and  External

See Also:

History:
******************************************************************************/
extern UFUNEXPORT int UF_WEIGHT_estab_solid_props (
const tag_t solid ,/* <I>
                   The solid whose properties are to be
                   calculated.
                   */
const  double accuracy ,/* <I>
                        The accuracy to which the solid's properties
                        are to be calculated.
                        */
const UF_WEIGHT_units_type_t units ,/* <I>
                                    The units in which the properties are to be
                                    returned.
                                    */
UF_WEIGHT_properties_t * properties  /* <O>
                                     The established properties of the solid.
                                     */
);

/*****************************************************************************
Assert the properties of part to be those specified by properties.  The
cache_state of properties must be UF_WEIGHT_asserted, and the
other states must be compatible as well, as described in the
description of UF_WEIGHT_properties_t.  The accuracy of the
properties is ignored, and the errors are set to 0.0.  The part will be
fully loaded.

Environment: Internal  and  External

See Also:
 UF_WEIGHT_delete_part_assertion

History:
******************************************************************************/
extern UFUNEXPORT int UF_WEIGHT_assert_part_props (
const tag_t part ,/* <I>
                  The part whose weight properties are to be
                  asserted.
                  */
UF_WEIGHT_properties_pc_t properties  /* <I>
                                           The properties to be asserted on
                                           the part.
                                           */
);

/*****************************************************************************
Assert the properties of component to be those specified by properties.
The cache_state of properties must be UF_WEIGHT_asserted, and
the other states must be compatible as well, as described in the
description of UF_WEIGHT_properties_t.  The accuracy of the
properties is ignored, and the errors are set to 0.0.  The part
containing component will be fully loaded.

Environment: Internal  and  External

See Also:
 UF_WEIGHT_delete_comp_assertion

History:
****************************************************************************/
extern UFUNEXPORT int UF_WEIGHT_assert_comp_props (
const tag_t component ,/* <I>
                       The component whose properties are to be
                       asserted.
                       */
UF_WEIGHT_properties_pc_t properties  /* <I>
                                           The properties to be asserted on the
                                           component.
                                           */
);

/*****************************************************************************
Delete the asserted weight properties on part.  Will return
UF_WEIGHT_has_no_assertion if there are no asserted properties
on the part.  Does not affect the weight reference set or component
set of the part, or any weight limits set on it.  The part will be fully
loaded.

If the part had previously had cached values on it, these will have
been overwritten by the asserted values, and will not be available even
after the assertion is deleted.  However, when the assertion is deleted,
caches on solids and components of the part become available again.

Environment: Internal  and  External

See Also:
 UF_WEIGHT_assert_part_props

History:
******************************************************************************/
extern UFUNEXPORT int UF_WEIGHT_delete_part_assertion (
const tag_t part  /* <I>
                  The part whose asserted properties are to
                  be deleted.
                  */
);

/*****************************************************************************
Delete the asserted weight properties on component.  Will return
UF_WEIGHT_has_no_assertion if there are no asserted properties
on component.  The part containing component will be fully loaded.
If component had previously had cached values on it, these will have
been overwritten by the asserted values, and will not be available even
after the assertion is deleted.  However, when the assertion is deleted,
caches on solids in and children of component become available again.

Environment: Internal  and  External

See Also:
 UF_WEIGHT_assert_comp_props

History:
******************************************************************************/
extern UFUNEXPORT int UF_WEIGHT_delete_comp_assertion (
const tag_t component  /* <I>
                       The component whose asserted properties
                       are to be deleted.
                       */
);


/*****************************************************************************
Set the weight reference set for part to ref_set_name: only solids in the
weight reference set of a part contribute to that part's weight
properties.  The part will be fully loaded.  Use the strings "Entire
Part" and "Empty" respectively to set the weight reference set to be
all solids or none. If the part contains a model reference set then it is 
designated as the initial value before the weight reference set is 
explicitly set. If the model reference set is not defined on the part then 
the weight reference set is "Entire Part".
ref_set_name does not have to be the name of a reference set currently 
in the part (however, using such a weight reference set during a weight
calculation will generate exceptions).  
It is also possible to delete a reference set that is in use
as a weight reference set, causing the same exceptions on following
weight calculations.

Environment: Internal  and  External

See Also:
 UF_WEIGHT_ask_part_ref_set
 UF_ASSEM_create_ref_set

History:
******************************************************************************/
extern UFUNEXPORT int UF_WEIGHT_set_part_ref_set (
const tag_t part ,/* <I>
                  The part whose weight reference set is to
                  be set.
                  */
const char * ref_set_name  /* <I>
                           Name of reference set to be made the
                           part's weight reference set.
                           */
);

/*****************************************************************************
Ask the weight reference set of part, which is returned as a string in
ref_set_name.  Returns "Entire Part" if no reference set is in use,
"Empty" if the empty reference set is in use.  The weight reference set
need not be an actual reference set in the part when this routine is
called.

Environment: Internal  and  External

See Also:
 UF_WEIGHT_set_part_ref_set

History:
******************************************************************************/
extern UFUNEXPORT int UF_WEIGHT_ask_part_ref_set (
const tag_t part ,/* <I>
                  The part whose weight reference set is to
                  be returned.
                  */
char **ref_set_name  /* <OF>
                     The name of part's current weight reference
                     set.  The string must be freed with UF_free.
                     */
);

/*****************************************************************************
Set the weight component set for part to cset_name: only child
components in the weight component set of a part contribute to that's
part's recursive weight properties.  The part will be fully loaded.  Use
the string "AllComponents" to set the weight-component set to be all
components (this is the initial value before the weight component set
is explicitly set). cset_name does not have to be the name of a
component set currently in the part (however, using such a weight
component set during a weight calculation will generate exceptions).
It is also possible to delete a component set that is in use as a weight
component set, causing the same exceptions on following weight calculations.

Environment: Internal  and  External

See Also:
 UF_WEIGHT_ask_part_cset
 UF_ASSEM_create_cset
 UF_ASSEM_add_to_cset

History:
******************************************************************************/
extern UFUNEXPORT int UF_WEIGHT_set_part_cset (
const tag_t part ,/* <I>
                  The part whose weight component set is to
                  be set.
                  */
const char * cset_name  /* <I>
                        Name of component set to be made the
                        part's weight component set.
                        */
);

/*****************************************************************************
Ask the weight component set of part, which is returned as a string in
cset_name.  Returns "AllComponents" if no component set is in use.
The weight component set need not be an actual component set in the
part when this routine is called.

Environment: Internal  and  External

See Also:
 UF_WEIGHT_set_part_cset

History:
******************************************************************************/
extern UFUNEXPORT int UF_WEIGHT_ask_part_cset (
const tag_t part ,/* <I>
                  The part whose weight component set is to
                  be returned.
                  */
char ** cset_name  /* <OF>
                   The name of part's current weight component set.
                   The string must be freed with UF_free.
                   */
);

/*****************************************************************************
Set the update weight properties save option for part.  The part will be
fully loaded.  If update_on_save is true, the weight properties will be
updated for the part every time it is saved thereafter.  If it is false,
weight properties will not be updated on save thereafter (though they
can still be established in response to an explicit user request, of
course).

Environment: Internal  and  External

See Also:
 UF_WEIGHT_ask_part_save_option

History:
******************************************************************************/
extern UFUNEXPORT int UF_WEIGHT_set_part_save_option (
const tag_t part ,/* <I>
                  The part whose update weight properties
                  save option is to be set.
                  */
const logical update_on_save  /* <I>
                              New value of update weight properties save
                              option for the part.
                              */
);

/*****************************************************************************
Ask the state of the update weight properties save option for part:
update_on_save is true if the save option is on, false otherwise.

Environment: Internal  and  External

See Also:
 UF_WEIGHT_set_part_save_option

History:
******************************************************************************/
extern UFUNEXPORT int UF_WEIGHT_ask_part_save_option (
const tag_t part ,/* <I>
                  The part whose update weight properties
                  save option is to be returned.
                  */
logical * update_on_save  /* <O>
                          The current value of part's update weight
                          properties save option.
                          */
);

/*****************************************************************************
Set the minimum permitted weight limit on part to be min_weight,
expressed in units.  min_weight must be greater than zero.  If this limit
is exceeded in future weight property calculations, an exception is
raised.  The part will be fully loaded.

Environment: Internal  and  External

See Also:
 UF_WEIGHT_ask_part_min_weight
 UF_WEIGHT_unset_part_min_weight

History:
******************************************************************************/
extern UFUNEXPORT int UF_WEIGHT_set_part_min_weight (
const tag_t part ,/* <I>
                  The part whose minimum weight limit is to
                  be set.
                  */
const double min_weight ,/* <I>
                         The value of the new minimum weight limit
                         for the part.
                         */
const UF_WEIGHT_units_type_t units  /* <I>
                                    The units in which the minimum weight
                                    limit is expressed.
                                    */
);

/*****************************************************************************
Remove the minimum permitted weight limit on part.  This restores
the initial state of the part, whereby no minimum weight limit
exceptions are given.  The part will be fully loaded.

Environment: Internal  and  External

See Also:
 UF_WEIGHT_ask_part_min_weight
 UF_WEIGHT_set_part_min_weight

History:
******************************************************************************/
extern UFUNEXPORT int UF_WEIGHT_unset_part_min_weight (
const tag_t part  /* <I>
                  The part whose minimum weight limit is to
                  be removed.
                  */
);

/*****************************************************************************
Ask the minimum permitted weight limit for part, expressed in units.
If the limit is not set, is_set is false, and min_weight is 0.0.

Environment: Internal  and  External

See Also:
 UF_WEIGHT_set_part_min_weight
 UF_WEIGHT_unset_part_min_weight

History:
******************************************************************************/
extern UFUNEXPORT int UF_WEIGHT_ask_part_min_weight (
const tag_t part ,/* <I>
                  The part whose minimum weight limit is to
                  be returned.
                  */
const UF_WEIGHT_units_type_t units ,/* <I>
                                    The units in which the minimum weight
                                    limit is to be expressed.
                                    */
double * min_weight ,/* <O>
                     The value of the minimum weight limit of
                     part (0.0 if the limit is not set).
                     */
logical * is_set  /* <O>
                  True if the minimum weight limit of the
                  part is currently set, false if not.
                  */
);

/*****************************************************************************
Set the maximum permitted weight limit on part to be max_weight,
expressed in units.  max_weight must be greater than zero.  If this limit
is exceeded in future weight property calculations, an exception is
raised.  The part will be fully loaded.

Environment: Internal  and  External

See Also:
 UF_WEIGHT_ask_part_max_weight
 UF_WEIGHT_unset_part_max_weight

History:
******************************************************************************/
extern UFUNEXPORT int UF_WEIGHT_set_part_max_weight (
const tag_t part ,/* <I>
                  The part whose maximum weight limit is to
                  be set.
                  */
const double max_weight ,/* <I>
                         The value of the new maximum weight limit
                         for the part.
                         */
const UF_WEIGHT_units_type_t units  /* <I>
                                    The units in which the maximum weight
                                    limit is expressed.
                                    */
);

/*****************************************************************************
Remove the maximum permitted weight limit on part.  This restores
the initial state of the part, whereby no maximum weight limit
exceptions are given.  The part will be fully loaded.

Environment: Internal  and  External

See Also:
 UF_WEIGHT_ask_part_max_weight
 UF_WEIGHT_set_part_max_weight

History:
******************************************************************************/
extern UFUNEXPORT int UF_WEIGHT_unset_part_max_weight (
const tag_t part  /* <I>
                  The part whose maximum weight limit is to
                  be removed.
                  */
);

/*****************************************************************************
Ask the maximum permitted weight limit for part, expressed in units.
If the limit is not set, is_set is false, and max_weight is 0.0.

Environment: Internal  and  External

See Also:
 UF_WEIGHT_set_part_max_weight
 UF_WEIGHT_unset_part_max_weight

History:
******************************************************************************/
extern UFUNEXPORT int UF_WEIGHT_ask_part_max_weight (
const tag_t part ,/* <I>
                  The part whose maximum weight limit is to
                  be returned.
                  */
const UF_WEIGHT_units_type_t units ,/* <I>
                                    The units in which the maximum weight
                                    limit is to be expressed.
                                    */
double * max_weight ,/* <O>
                     The value of the maximum weight limit of
                     part (0.0 if the limit is not set).
                     */
logical * is_set  /* <O>
                  True if the maximum weight limit of the
                  part is currently set, false if not.
                  */
);


#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif /* UF_WEIGHT_INCLUDED */
