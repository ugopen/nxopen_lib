/****************************************************************************

           Copyright (c) 2013 Siemens Co.
                         Unpublished - All rights reserved

===========================================================================

 

File description:

This the Open API interface to units specifications used by e.g. expressions and user attributes.

In NX a units specification consists of two parts, the measure and the unit types.
The measure defines what type of value is being considered.
Examples of measures are:

    Measure              Measure Type
    ---------------------------------
    Length               UF_MEASURE_LENGTH
    Area                 UF_MEASURE_AREA
    Thermal Energy       UF_MEASURE_THERMAL_ENERGY

For each measure, NX supports a number of unit types. The unit type is the actual units
that are used to express the given value. 
Examples of unit types are:

     Units               Unit Type Name
     ----------------------------------
    'millimeters'        UF_UNIT_LENGTH_mm
    'inches squared'     UF_UNIT_AREA_in2
    'Btu'                UF_UNIT_ENERGY_btu

Using the UF_UNIT subroutines, you can:

    . Find the tag of a unit type using the unit name.
    . Find the name of a unit specification using the unit type tag.
    . Convert a value from one unit type to another.
*/
#ifndef UF_UNIT_INCLUDED
#define UF_UNIT_INCLUDED

/******************************************************************************

  ***************************************************************************/

#include <uf_defs.h>
#include <uf_error_bases.h>
#include <uf_unit_types.h>
#include <libufun_exports.h>
#ifdef __cplusplus
extern "C" {
#endif

/*****************************************************************************
 * UF_UNIT_ask_unit_tag_from_unit_name
 *
 * Given a unit type name and the associated measure type, return the tag of the unit type
 *
 * The given name is the name of the units as defined in uf_unit_types.h
 * To properly select the units, an object in the part as well as the measure type
 * must be provided.
 *
 * For example, the name for millimeters is "MilliMeter", defined in uf_unit_types.h as 'UF_UNIT_LENGTH_mm
 *
 * Environment: Internal and External
 * History: NX8.5.3
 *****************************************************************************/
extern UFUNEXPORT int UF_UNIT_ask_unit_tag_from_unit_name
(
    tag_t object,                             /* <I> The units context (an object in the part where the units are used) */
    UF_UNIT_MEASURE_TYPE_t unit_measure_type, /* <I> The measure type of the units (see uf_unit_types.h) */
    const char * name,                        /* <I> The name of the unit type (see uf_unit_types.h) */
    tag_t *unit                               /* <O> The tag of the unit type */
);

/*****************************************************************************
 * UF_UNIT_ask_system_unit_tag_from_measure
 *
 * Given a unit type name and the associated measure type, return the tag of the system unit type.
 * The system units is that used to store values in the part file (as opposed to display units).
 *
 * To properly select the units, an object in the part as well as the measure type
 * must be provided.
 *
 * Environment: Internal and External
 * History: NX8.5.3
 *****************************************************************************/
extern UFUNEXPORT int UF_UNIT_ask_system_unit_tag_from_measure
(
    tag_t object,                             /* <I> The units context (an object in the part where the units are used) */
    UF_UNIT_MEASURE_TYPE_t unit_measure_type, /* <I> The measure type of the units (see uf_unit_types.h) */
    tag_t *unit                               /* <O> The tag of the unit type */
);

/******************************************************************************
 * UF_UNIT_ask_unit_name_from_unit_tag
 *
 * Given a unit tag, return the unit name of the units
 *
 * For example, the name for millimeters is "MilliMeter", defined in uf_unit_types.h as 'UF_UNIT_LENGTH_mm
 * The returned string must be freed after use.
 *
 * Environment: Internal and External
 * History: NX8.5.3
 *****************************************************************************/
extern UFUNEXPORT int UF_UNIT_ask_unit_name_from_unit_tag
(
    tag_t unit,            /* <I>  The tag of the unit type */
    char ** name           /* <OF> The unit name of the units (see uf_unit_types.h) */
);

/******************************************************************************
 * UF_UNIT_ask_measure_type_from_unit_tag
 *
 * Given a unit tag, return the measure type
 *
 * Environment: Internal and External
 * History: NX8.5.3
 ******************************************************************************/
extern UFUNEXPORT int UF_UNIT_ask_measure_type_from_unit_tag
(
    tag_t unit,                                 /* <I> The tag of the unit type */
    UF_UNIT_MEASURE_TYPE_p_t measure_type       /* <O> The measure type associated with the given units (see uf_unit_types.h) */
);

/******************************************************************************
 * UF_UNIT_convert_value
 *
 * Given a value with a given unit type, convert it to a value in a new unit type.
 *
 * The measure type of the new units must be the same as that of the initial units
 *
 * Environment: Internal and External
 * History: NX8.5.3
 ******************************************************************************/
extern UFUNEXPORT int UF_UNIT_convert_value
(
    double initial_value,    /* <I> The value to be converted */
    tag_t initial_units,     /* <I> The tag of the unit type of the initial value */
    tag_t new_units,         /* <I> The tag of the unit type of the new units */
    double *converted_value  /* <O> The value expressed in the new units */
);

#ifdef __cplusplus
}
#endif


#undef EXPORTLIBRARY
#endif
