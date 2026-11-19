/******************************************************************************
             Copyright (c) 1995-2003 Unigraphics Solutions, Inc.
                       Unpublished - All Rights Reserved

 ******************************************************************************


File Description:
       UF_DRPOS provides the required functions and type definitions for
       the specification of drive positions for Surface Contouring

       UF_DRPOS is used when a CAM Surface Contouring operation uses
       the User Defined drive path method.  Please refer to the module
       UF_DPUD for how to use this drive method.

 *****************************************************************************/

/* Do not process this file again if already included */
#ifndef UF_DRPOS_H_INCLUDED
#define UF_DRPOS_H_INCLUDED


/***************************************************************************

  ***************************************************************************/


/**************************************************************************
 *
 *   Include files necessary for UF_DRPOS definition
 *
 **************************************************************************/
#include <uf_defs.h>
#include <libufun_cam_exports.h>

/***************************************************************************

  ***************************************************************************/
#define ERROR_UF_DRPOS_base    1380000

#ifdef __cplusplus
extern "C" {
#endif

/**************************************************************************
 *
 *    UF_DRPOS data definitions (#defines, enums, typedefs, etc.)
 *
 **************************************************************************/

/* UF_DRPOS_id_t is the identifier for referring to a UF_DRPOS */
typedef void   *UF_DRPOS_id_t;

/* UF_DRPOS_type_t enumerates the different types of UF_DRPOS objects */
enum UF_DRPOS_type_e
        {
        UF_DRPOS_TYPE_NONE = 0, /* This motion type option indicates that no
                                   motion type has yet been specified and
                                   should not be used by an Open API program.
                                */
        UF_DRPOS_TYPE_CUT = 1, /* This motion type option is used to generate
                                  standard cut motions with the cut feedrate. */
        UF_DRPOS_TYPE_FIRST_CUT = 2, /* This motion type option is used to
                                        generate cut motions which are expected
                                        to require a low (first cut) feedrate
                                        because the tool is removing a large
                                        amount of material (the tool is buried).
                                     */
        UF_DRPOS_TYPE_STEPOVER = 10, /* This motion type option is used to
                                        generate cut motions which connect two
                                        passes of a tool path, thus requiring a
                                        lower (stepover) feedrate.
                                     */
        UF_DRPOS_TYPE_LOCAL_LIFT = 50, /* This motion type option is used to
                                          generate a local retract, transfer,
                                          and engege sequence. For this motion
                                          type, no tool position is required.
                                          The previous tool position is used
                                          for the retract and the following cut
                                          position is used for the engage. */

        UF_DRPOS_TYPE_FINAL_LIFT = 51 /* This motion type option must be the
                                         last motion output. No position is
                                         required here (just as with
                                         local_lift). */
        } ;

typedef enum UF_DRPOS_type_e UF_DRPOS_type_t;


/* UF_DRPOS_feed_use_t enumerates the available options for how to
   obtain the feed rate for a UF_DRPOS object */
enum UF_DRPOS_feed_use_e
        {
        UF_DRPOS_FEED_USE_DEFAULT = 0,
        UF_DRPOS_FEED_USE_CUSTOM = 1
        } ;
typedef enum UF_DRPOS_feed_use_e  UF_DRPOS_feed_use_t;


/* UF_DRPOS_feed_unit_t enumerates the available set of units in
   which the feed rate may be expressed */
enum UF_DRPOS_feed_unit_e
        {
        UF_DRPOS_FEED_UNIT_NONE = 0,
        UF_DRPOS_FEED_UNIT_PER_MIN = 1, /* Units per minute */
        UF_DRPOS_FEED_UNIT_PER_REV = 2  /* Revolutions per minute */
        } ;
typedef enum UF_DRPOS_feed_unit_e UF_DRPOS_feed_unit_t;

/* UF_DRPOS_zig_zag_dir_t enumerates the two directions of cut
   when doing zig/zag type cut patterns */
enum UF_DRPOS_zig_zag_dir_e
        {
        UF_DRPOS_ZIG_ZAG_DIR_ZIG = 0,
        UF_DRPOS_ZIG_ZAG_DIR_ZAG = 1
        } ;
typedef enum UF_DRPOS_zig_zag_dir_e UF_DRPOS_zig_zag_dir_t;

/************************************************************************
 *
 *    UF_DRPOS public function interface
 *
 ************************************************************************/

/*************************************************************************
Formats a drive position as a local lift.  Between any two lifts (local or
final), the system should generate at least two cut or stepover positions.

Environment: Internal  and  External

See Also:

History:
 **************************************************************************/
extern UFUN_CAMEXPORT int UF_DRPOS_create_local_lift(
UF_DRPOS_id_t drpos  /* <I>
                     Identifier for a DRPOS object
                     */
);

/*************************************************************************
Formats a drive position as a final lift.  A final lift must be the last drive
position generated by the Open API program, and only one final lift must be
generated, unless a "rewind" request has been received. Between any two lifts
(local or final), the system should generate at least two cut or stepover
positions.

Environment: Internal  and  External

See Also:

History:
 **************************************************************************/
extern UFUN_CAMEXPORT int UF_DRPOS_create_final_lift(
UF_DRPOS_id_t drpos  /* <I>
                     Identifier for a DRPOS object
                     */
);

/*************************************************************************
Formats a drive position as a cut. This formatting must be done before the
Open API program can use the functions which set the position and other data
of a cut drive position.

Environment: Internal  and  External

See Also:

History:
 **************************************************************************/
extern UFUN_CAMEXPORT int UF_DRPOS_create_cut(
UF_DRPOS_id_t drpos ,/* <I>
                     Identifier for a DRPOS object
                     */
double pos[3] ,/* <I>
               Drive position
               */
double dir[3]  /* <I>
               Drive direction
               */
);

/*************************************************************************
Formats a drive position as a first cut drive position. This formatting
must be done before the Open API program can use the functions which set
the positional and other data of a first cut drive position.

Environment: Internal  and  External

See Also:

History:
 **************************************************************************/
extern UFUN_CAMEXPORT int UF_DRPOS_create_first_cut(
UF_DRPOS_id_t drpos ,/* <I>
                     Identifier for a DRPOS object
                     */
double pos[3] ,/* <I>
               Drive position
               */
double dir[3]  /* <I>
               Drive direction
               */

);


/*************************************************************************
Formats a drive position as a stepover cut drive position. This formatting must
be done before the Open API program can use the functions which set the
positional and other data of a stepover drive position.

Environment: Internal  and  External

See Also:

History:
 **************************************************************************/
extern UFUN_CAMEXPORT int UF_DRPOS_create_stepover(
UF_DRPOS_id_t drpos ,/* <I>
                     Identifier for a DRPOS object
                     */
double pos[3] ,/* <I>
               Drive position
               */
double dir[3]  /* <I>
               Drive direction
               */
);

/*************************************************************************
Asks the type of a UF_DRPOS object.

Environment: Internal  and  External

See Also:

History:
 **************************************************************************/
extern UFUN_CAMEXPORT int UF_DRPOS_ask_type(
UF_DRPOS_id_t drpos ,/* <I>
                     Identifier for a DRPOS object
                     */
UF_DRPOS_type_t * type  /* <O>
                        The type of drive position
                        */
);

/*************************************************************************
 Writes positional data to a cut or stepover drive position (the coordinates
used for this must be in relation to the absolute coordinate system).  This
function is available only for cut and stepover drive positions.

Environment: Internal  and  External

See Also:

History:
 **************************************************************************/
extern UFUN_CAMEXPORT int UF_DRPOS_set_position(
UF_DRPOS_id_t drpos ,/* <I>
                     Identifier for a DRPOS object
                     */
double pos[3]  /* <I>
               Coordinates of cut or stepover drive position in
               absolute
               */
);

/*************************************************************************
Asks positional data of a cut or stepover drive position (the coordinates used
for this must be in relation to the absolute coordinate system).  This function
is available only for cut and stepover drive positions.

Environment: Internal  and  External

See Also:

History:
 **************************************************************************/
extern UFUN_CAMEXPORT int UF_DRPOS_ask_position(
UF_DRPOS_id_t drpos ,/* <I>
                     Identifier for a DRPOS object
                     */
double pos[3]  /* <O>
               The location of the drive position
               */
);

/*************************************************************************
Writes tool axis data to a cut or stepover drive position (the coordinates used
for this must be in relation to the absolute coordinate system).

Environment: Internal  and  External

See Also:

History:
 **************************************************************************/
extern UFUN_CAMEXPORT int UF_DRPOS_set_tool_axis(
UF_DRPOS_id_t drpos ,/* <I>
                     Identifier for a DRPOS object
                     */
double tool_axis[3]  /* <I>
                     The tool axis
                     */
);

 /**************************************************************************
Reads tool axis data of a cut or stepover drive position (the coordinates used
for this are in relation to the absolute coordinate system).

Environment: Internal  and  External

See Also:

History:
 *************************************************************************/
extern UFUN_CAMEXPORT int UF_DRPOS_ask_tool_axis(
UF_DRPOS_id_t drpos ,/* <I>
                     Identifier for a DRPOS object
                     */
double tool_axis[3]  /* <O>
                     The tool axis
                     */
);

/**************************************************************************
Writes projection vector data to a cut or stepover drive position (the
coordinates used for this must be in relation to the absolute coordinate
system).  This function is available only for cut and stepover drive positions.

Environment: Internal  and  External

See Also:

History:
 *************************************************************************/
extern UFUN_CAMEXPORT int UF_DRPOS_set_proj_vec(
UF_DRPOS_id_t drpos ,/* <I>
                     Identifier for a DRPOS object
                     */
double proj_vec[3]  /* <I>
                    The projection vector
                    */
);

/**************************************************************************
Reads the projection vector data of a cut or stepover drive position (the
coordinates used for this are in relation to the absolute coordinate system).

Environment: Internal  and  External

See Also:

History:
 *************************************************************************/
extern UFUN_CAMEXPORT int UF_DRPOS_ask_proj_vec(
UF_DRPOS_id_t drpos ,/* <I>
                     Identifier for a DRPOS object
                     */
double proj_vec[3]  /* <O>
                    The projection vector
                    */
);

/**************************************************************************
Writes drive direction data to a cut drive position. This vector is used
when calculating a tool axis that depends on the direction of cut. For
stepovers, the tool axis is interpolated between those of the previous
cut position and the next cut position, and thus does not require a
drive direction vector (the coordinates used for this must be in
relation to the absolute coordinate system).

The drive direction is defined to be the unitized 3D tangent vector of
the drive path:
        drive_dir = dS/ds
where S is the path and s is the curve length.

If the path is not differentiable, which can happen if the path has a
sharp bend, such as in piecewise linear paths, or if the drive position is
next to a lift. In such cases the path should still have either one or two
tangents:
        dS/ds  and/or    -dS/ds

As cut drive position which are preceeded by lifts or stepovers, the
drive direction vector should be the tangent of the previous cut, i.e.,
        drive_dir = -dS/ds
This function is available only for cut drive positions.

Environment: Internal  and  External

See Also:

History:
 **************************************************************************/
extern UFUN_CAMEXPORT int UF_DRPOS_set_drive_direction(
UF_DRPOS_id_t drpos ,/* <I>
                     Identifier for a DRPOS object
                     */
double dir[3]  /* <I>
               The direction vector
               */
);

/**************************************************************************
Asks for drive direction data to cut a drive position.  This function is
available only for cut drive positions.

Environment: Internal  and  External

See Also:

History:
 **************************************************************************/
extern UFUN_CAMEXPORT int UF_DRPOS_ask_drive_direction(
UF_DRPOS_id_t drpos ,/* <I>
                     Identifier for a DRPOS object
                     */
double dir[3]  /* <O>
               The direction vector
               */
);

/**************************************************************************
Writes zig_zag information to a cut drive position. The system allows
the specification of separate tool axis data for zig and zag motions of a
zig/zag cut pattern. The value of the zig_zag_dir determines which of
the two possible tool axis specifications to use. Note: when only a
single tool axis specification is used, this flag has no effect. (This
function need only be called for zag-type cut motions, as the default
direction is zig, which is set by the UF_DRPOS_create_cut).
This function is only available for cut drive positions.

Environment: Internal  and  External

See Also:

History:
 **************************************************************************/
extern UFUN_CAMEXPORT int UF_DRPOS_set_zig_zag_dir(
UF_DRPOS_id_t drpos ,/* <I>
                     Identifier for a DRPOS object
                     */
UF_DRPOS_zig_zag_dir_t zig_zag_dir  /* <I>
                                    The direction of zig/zag cuts
                                    0= the cut is a zig cut (default)
                                    1= the cut is a zag cut
                                    */
);

/*************************************************************************
Asks zig_zag information of a cut drive position.  This function is available
only for cut drive positions.

Environment: Internal  and  External

See Also:

History:
 **************************************************************************/
extern UFUN_CAMEXPORT int UF_DRPOS_ask_zig_zag_dir(
UF_DRPOS_id_t drpos ,/* <I>
                     Identifier for a DRPOS object
                     */
UF_DRPOS_zig_zag_dir_t *zig_zag_dir  /* <O>
                                     Direction of zig/zag cuts
                                     */
);


/*************************************************************************
Writes custom feedrate information to a cut or stepover drive
position. In general it should not be necessary to set the feedrate of a
drive, as this is done by the processor based on the motion types
output. However, in special cases the drive path generator may force a
custom feedrate. In such cases, this function can be used to set the
desired feedrate.  This function is available only for cut and stepover
drive positions.

Environment: Internal  and  External

See Also:

History:
 **************************************************************************/
extern UFUN_CAMEXPORT int UF_DRPOS_set_custom_feed(
UF_DRPOS_id_t drpos ,/* <I>
                     use custom or default feed
                     */
UF_DRPOS_feed_use_t feed_use ,/* <I>
                              custom feed rate units (used only if use custom
                              feed)
                              */
UF_DRPOS_feed_unit_t feed_unit ,/* <I>
                                custom feed value (used only if use custom feed)
                                */
double feed_value  /* <I>
                   The custom feed value (used only if use custom
                   feed)
                   */
);

/*************************************************************************
Asks custom feedrate information of a cut or stepover drive position.
This function is available only for cut and stepover drive positions.

Environment: Internal  and  External

See Also:

History:
 **************************************************************************/
extern UFUN_CAMEXPORT int UF_DRPOS_ask_custom_feed(
UF_DRPOS_id_t drpos ,/* <I>
                     Identifier for a DRPOS object
                     */
UF_DRPOS_feed_use_t * feed_use ,/* <I>
                                Use custom or default feed
                                */
UF_DRPOS_feed_unit_t * feed_unit ,/* <I>
                                  Custom feed rate units (used only if use
                                  custom feed)
                                  */
double * feed_value  /* <O>

                     Custom feed value (used only if use custom feed)
                     */
);

/*************************************************************************
 Asks for the user data area of a drive position. The user data is copied
into a locally supplied variable. User data must point at memory of
size " s " associated by the caller. " s " is the size specified as the
second argument to UF_DPUD_set_user_data_size.

Environment: Internal  and  External

See Also:  UF_DPUD_set_user_data_size

History:
 **************************************************************************/
extern UFUN_CAMEXPORT int UF_DRPOS_ask_user_data(
UF_DRPOS_id_t drpos ,/* <I>
                     Identifier for a DRPOS object
                     */
void * user_data  /* <O>
                  Pointer to user data
                  */
);

/*************************************************************************
Sets the user data area of a drive position.

Environment: Internal  and  External

See Also:

History:
 **************************************************************************/
extern UFUN_CAMEXPORT int UF_DRPOS_set_user_data(
UF_DRPOS_id_t drpos ,/* <I>
                     Identifier for a DRPOS object
                     */
void * user_data  /* <I>
                  Pointer to user data
                  */
);

/*************************************************************************
Returns the u and v parameter position of a drive point with respect to the
surface grid

Environment: Internal  and  External

See Also:

History:  Released in NX3
 *************************************************************************/
extern UFUN_CAMEXPORT int UF_DRPOS_ask_grid_params(
UF_DRPOS_id_t drpos ,   /* <I> Identifier for a DRPOS object  */
double        uv[2]     /* <O>  U,V parameters at the input drive position  */
);

/*************************************************************************
Returns the u and v parameter position of a drive point with respect to the
surface

Environment: Internal  and  External

See Also:

History:  Released in NX3
 *************************************************************************/
extern UFUN_CAMEXPORT int UF_DRPOS_ask_surface_params(
UF_DRPOS_id_t drpos ,   /* <I> Identifier for a DRPOS object  */
double        uv[2]     /* <O>  U,V parameters at the input drive position  */
);

/*************************************************************************
Returns the surface identifier of a drive point

Environment: Internal  and  External

See Also:

History:  Released in NX3
 **************************************************************************/
extern UFUN_CAMEXPORT int UF_DRPOS_ask_surface_identifier (
    UF_DRPOS_id_t drpos,   /*  <I> Identifier for a DRPOS object  */
    tag_t         *eid     /*  <O> Surface identifier  */
);

/*****************************************************************************
 * This function deletes a drive point that is output from UF_SCOP_get_next_drive_point.
 *
 * Environment : Internal  and  External
 * See Also: UF_SCOP_get_next_drive_point
 * History : Released in NX3.0
 ****************************************************************************/
extern UFUN_CAMEXPORT int UF_DRPOS_delete
(
    UF_DRPOS_id_t  drpos /* <I> */
);

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif
