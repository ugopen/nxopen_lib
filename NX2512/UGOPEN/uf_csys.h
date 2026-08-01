/****************************************************************************

      Copyright (c) 1993-2002 Electronic Data Systems Corporation
                    Unpublished - All rights reserved

****************************************************************************



File description :

   This include file contains routines that enable you to manipulate matrices
   and coordinate systems. Using the routines you can:

     .  map a point from one coordinate system to a point in
        another coordinate system.

     .  create, read, and edit matrices

     .  create, edit, and change the WCS pointer

     .  create or read the CSYS origin

*****************************************************************************/

#ifndef UF_CSYS_INCLUDED
#define UF_CSYS_INCLUDED


/***************************************************************************

  ***************************************************************************/

#define ERROR_UF_CSYS_base     1100000

/****************************************************************************/

/* Constants for coordinate systems */

/* coordinate space of the root part which is
   the whole part being displayed */
#define UF_CSYS_ROOT_COORDS     1
/* coordinate space of the work part */
#define UF_CSYS_WORK_COORDS     2
/* work coordinate space of the root part */
#define UF_CSYS_ROOT_WCS_COORDS 3


/* Constants for error codes */
#define UF_CSYS_ERR_INVALID_COORDS (ERROR_UF_CSYS_base + 0)
        /* : The input coordinate system is invalid */

#include <uf_defs.h>
#include <libufun_exports.h>


#ifdef __cplusplus
extern "C" {
#endif

/****************************************************************************
 * Maps a point from one coordinate system to a point in another
 * coordinate system. The coordinate system can be one of the following
 * constants.
 *
 * UF_CSYS_ROOT_COORDS      is the ABS of the displayed part.
 * UF_CSYS_WORK_COORDS      is the ABS of the work part.
 * UF_CSYS_ROOT_WCS_COORDS  is the WCS of the displayed part.
 * For example:
 * To convert a point from absolute coordinates of the displayed part to
 * the WCS:
 *      input_csys  = UF_CSYS_ROOT_COORDS;
 *      output_csys = UF_CSYS_ROOT_WCS_COORDS;
 * To convert a point from the work part absolute coordinates to the
 * displayed part absolute coordinates:
 *      input_csys  = UF_CSYS_WORK_COORDS;
 *      output_csys = UF_CSYS_ROOT_COORDS;
 *
 * Environment: Internal  and  External
 *
 * See Also:
 *
 * History:
 ****************************************************************************/
extern UFUNEXPORT int UF_CSYS_map_point(
int input_csys ,/* <I>
                   CSYS of point to be mapped which can be:
                   UF_CSYS_ROOT_COORDS
                   ( Coordinate space of the root part which is the whole
                   part being displayed),
                   UF_CSYS_WORK_COORDS ( Coordinate space of the work part),
                   UF_CSYS_ROOT_WCS_COORDS ( Root WCS)
                */
double input_point[3] ,/* <I>
                          The point (xyz) to be mapped.
                       */
int output_csys ,/* <I>
                    CSYS to be mapped to
                 */
double output_point[3]  /* <O>
                           The resultant point (xyz) of the mapping
                        */
);


/****************************************************************************
 * Creates a 3 x 3 matrix.
 *
 * Environment: Internal  and  External
 *
 * See Also:
 *
 * History:
 ****************************************************************************/
extern UFUNEXPORT int UF_CSYS_create_matrix(
const double matrix_values[9] ,/* <I>
                                  Matrix values -- should be normalized and
                                  orthogonal. Use UF_MTX3_initialize to
                                  create a matrix from X and Y vectors.
                               */
tag_t * matrix_id  /* <O>
                      Object identifier of the matrix
                   */
);

/****************************************************************************
 * Gets the matrix values of the specified matrix tag.
 *
 * Environment: Internal  and  External
 *
 * See Also:
 *
 * History:
 ****************************************************************************/
extern UFUNEXPORT int UF_CSYS_ask_matrix_values(
tag_t matrix_id ,/* <I>
                 Object identifier of the matrix
                 */
double matrix_values[9]  /* <O>
                         Matrix values
                         */
);

/****************************************************************************
 * Gets the matrix identifier attached to an object.  An object does not
 * necessarily have an matrix attached to it, and some objects can never have
 * a matrix attached.  This routine will return a NULL_TAG for the matrix
 * identifier if the object does not have a matrix attached to it, even if the
 * object can never have a matrix attached to it.
 *
 *
 * Environment: Internal  and  External
 *
 * See Also:
 *
 * History:
 ****************************************************************************/
extern UFUNEXPORT int UF_CSYS_ask_matrix_of_object(
tag_t object_id ,/* <I>
                    Identifier of object associated with matrix
                 */
tag_t * matrix_id  /* <O>
                      Identifier for the matrix attached to the object.  This
                      may be a NULL_TAG.
                   */
);

/****************************************************************************
 * Creates a CSYS.
 *
 * Environment: Internal  and  External
 *
 * See Also:
 *
 * History:
 ****************************************************************************/
extern UFUNEXPORT int UF_CSYS_create_csys(
const double csys_origin[3] ,/* <I>
                             The origin for the coordinate system
                             */
tag_t matrix_id ,/* <I>
                    Object identifier of the matrix associated with the
                    coordinate system
                 */
tag_t * csys_id  /* <O>
                    Object identifier of the coordinate system
                 */
);

/****************************************************************************
 * Creates a temporary coordinate system.
 *
 * Environment: Internal  and  External
 *
 * See Also:
 *
 * History:
 ****************************************************************************/
extern UFUNEXPORT int UF_CSYS_create_temp_csys (
const double csys_origin[3] ,/* <I>
                                The origin for the coordinate system
                             */
tag_t matrix_id ,/* <I>
                    Object identifier of the matrix associated with the
                    coordinate system
                 */
tag_t * csys_id  /* <O>
                    Object identifier of the coordinate system
                 */
);

/****************************************************************************
 * Sets the work coordinate system to the prototype coordinate system whose
 * tag you specify and then updates the display.  If an occurrence coordinate
 * system is specified, the work coordinate system will not be changed and
 * this function will return an error.  Note that the current WCS can not
 * be deleted, so the tag that is passed in can not then be deleted using
 * UF_OBJ_delete_object.
 *
 * Environment: Internal  and  External
 *
 * See Also:
 *
 * History:
 ****************************************************************************/
extern UFUNEXPORT int UF_CSYS_set_wcs(
tag_t csys_id  /* <I>
               Object identifier of the coordinate system to set the WCS to
               */
);

/****************************************************************************
 * Gets the object identifier of the coordinate system to which the work
 * coordinate system is set.
 *
 * Environment: Internal  and  External
 *
 * See Also:
 *
 * History:
 ****************************************************************************/
extern UFUNEXPORT int UF_CSYS_ask_wcs(
tag_t * wcs_id  /* <O>
                   Object identifier of the coordinate system to which
                   the WCS is set.
                */
);

/****************************************************************************
 * Queries the specified coordinate system and returns the matrix
 * identifier and the x, y, z coordinates of the origin.
 *
 * Environment: Internal  and  External
 *
 * See Also:
 *
 * History:
 ****************************************************************************/
extern UFUNEXPORT int UF_CSYS_ask_csys_info(
tag_t csys_id ,/* <I>
               Object identifier of the coordinate system to query.
               */
tag_t * matrix_id ,/* <O>
                   Pointer to object identifier of the matrix associated
with the coordinate system.
                   */
double csys_origin[3]  /* <O>
                       The origin of the coordinate system
                       */
);

/****************************************************************************
 * Updates the specified coordinate system matrix  with the identifier of
 * the new coordinate system matrix that you specify.
 *
 * This function does not perform an update.  In order for all of the
 * effects of changing the object's matrix to occur, you must call
 * UF_MODL_update at some point after calling this function.
 *
 * Environment: Internal  and  External
 *
 * See Also:
 *
 * History:
 ****************************************************************************/
extern UFUNEXPORT int UF_CSYS_edit_matrix_of_object (
tag_t object_id ,/* <I>
                    Identifier of the object whose matrix is to be updated.
                 */
tag_t matrix_id  /* <I>
                    Object identifier of the new matrix for the object
                 */
);

/****************************************************************************
 * Set origin of coordinate system.
 * Note that this function is not valid on the wcs.
 *
 * Environment: Internal  and  External
 *
 * See Also:
 *
 * History:
 ****************************************************************************/
extern UFUNEXPORT int UF_CSYS_set_origin (
    tag_t  csys_tag, /* <I>
                        tag of coordinate system to modify
                     */
    double origin[3] /* <I>
                        new origin of coordinate system
                     */
);

/****************************************************************************
 * Set display of work coordinate system.
 *
 * Environment: Internal  and  External
 *
 * See Also:
 *
 * History:
 ****************************************************************************/
extern UFUNEXPORT int UF_CSYS_set_wcs_display(
    int display_status /* <I>
                       1 = the wcs should be displayed
                       0 = the wcs should not be displayed
                        */
);



#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif  /* END UF_CSYS_INCLUDED */
