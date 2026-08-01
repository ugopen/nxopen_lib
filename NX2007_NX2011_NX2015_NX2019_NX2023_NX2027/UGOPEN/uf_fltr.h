/*******************************************************************************
            Copyright(c) 1995-2007 UGS Inc.
                      Unpublished - All rights reserved
*****************************************************************************




File description:

The Open API interface to the creation and manipulation of
zone and filter objects.

Zone objects are used to isolate regions of interest in a part.
Currently, they are used exclusively as part of component filters and
allow manipulation of assemblies and components by region.  Zones
can be created in two forms:  box and plane.

Box zones are specified by a centroid and corner vector.  The centroid
is given in Absolute coordinates and represents the center-point of
the box.  The corner vector is  the vector which represents the
most-positive corner of the box from the centroid (see diagram in
UF_FLTR_create_box_zone).

Plane zones are specified in the same way that ordinary planes are
specified in NX, with an origin and orientation.

Filter objects are used to inquire as to whether an object specifies
certain conditions.

A name must be specified when creating zones.  For this reason, name arguments
are also provided for "edit" and "ask" routines which concern zones.  Note
that the User function methods for naming and renaming objects will also work.

To delete a zone object, use the User Function routine which deletes an object.

Filters are specified with a name and a condition.  For instance, a
filter could be named "FLT1" and its condition could be
"Within(0,ZONE1)" which means any part occurrence which falls
within 0 units of ZONE1 satisfies the filter FLT1.

These functions enable you to:
   .  output the parameters of the box zone specified by box_zone.
   .  return the name and condition of a given filter.
   .  outputs the parameters of the plane zone referred to by plane_zone.
   .  automatically generates box zones along all 3 axes of the WCS in a part.
   .  automatically generate plane zones along the Z axis of the WCS in a part.
   .  create a box zone and obtain its tag.
   .  create a filter object given the name and condition.
   .  create a plane zone given the origin and orientation.
   .  modify the box zone referred to by zone to have the values 
      passed in by name, centroid, corner, and matrix.
   .  Give filter a new name and condition.
   .  modify the plane zone referred to by zone to have the values
      passed in by name, origin and matrix.
   .  evaluate whether object matches the given filter.
   .  test whether an object is within some distance of a zone.
   .  test whether an object is further than some distance of a zone.
   .  test whether a part occurrence is above a planar zone.

Errors:
-------
   Errors that can be encountered when using UF_FLTR are:
   .  UF_FLTR_ERR_NULL_PART - A null part tag has been passed into the routine
   .  UF_FLTR_ERR_NULL_FLTR_TAG - A null filter tag has been passed into 
      the routine.
   .  UF_FLTR_ERR_NULL_ZONE_TAG - A null zone tag has been passed into
      the routine.
   .  UF_FLTR_ERR_AUTO_NAME_CLASH - When an auto-create option attempts to
      create a zone whose name conflicts with other zone names in the part,
      this error occurs.
   .  UF_FLTR_ERR_NULL_CHAR - A null character string has been passed into
      the function.
   .  UF_FLTR_ERR_NULL_OBJ_TAG - A null object tag has been passed into
      the function.  This would be encountered during any of the comparison
      functions.
   .  UF_FLTR_ERR_INVALID_FILTER - When an invalid filter is encountered
       (usually this means the condition of the filter is erroneous), 
      this value is returned.   

*******************************************************************************/

#ifndef UF_FLTR_H_INCLUDED
#define UF_FLTR_H_INCLUDED


/***************************************************************************

  ***************************************************************************/

/******************************************************************************
 * The #include section 
 */

#include <uf_defs.h> 
#include <uf_obj_types.h>
#include <libufun_exports.h>

#ifdef __cplusplus
extern "C" {
#endif

/******************************************************************************
 * The #define section 
 */

#define ERROR_FLTR_base        1415000
#define UF_FLTR_OK                      0

#define UF_FLTR_ERR_NULL_PART               (ERROR_FLTR_base+11)
#define UF_FLTR_ERR_NULL_FLTR_TAG           (ERROR_FLTR_base+12)
#define UF_FLTR_ERR_NULL_ZONE_TAG           (ERROR_FLTR_base+13)
#define UF_FLTR_ERR_AUTO_NAME_CLASH         (ERROR_FLTR_base+14)
#define UF_FLTR_ERR_NULL_CHAR               (ERROR_FLTR_base+15)
#define UF_FLTR_ERR_NULL_OBJ_TAG            (ERROR_FLTR_base+16)
#define UF_FLTR_ERR_INVALID_FILTER          (ERROR_FLTR_base+17)


/******************************************************************************
Creates a box zone and returns its tag. The centroid is the center
point of the box zone (in Absolute coordinates).  The corner is a
vector describing the most positive corner of the box relative to the
centroid. The orientation is the orientation of the zone to be created.


Environment: Internal  and  External
See Also: 
History:
 *****************************************************************************/
extern UFUNEXPORT int UF_FLTR_create_box_zone(
tag_t  part_tag ,/* <I>
                 Part in which zone is to be created.
                 */
char *  name ,/* <I>
              Name of zone to be created.
              */
double  centroid[3] ,/* <I>
                     Centroid of zone (in Absolute Coordinates.)
                     */
double  corner[3] ,/* <I>
                   Corner vector (points to most positive box corner)
                   */
double orientation[9] ,/* <I>
                       Orientation of zone with respect to absolute.
                       */
tag_t * zone_tag  /* <I/O>
                  Tag of zone created.
                  */
);

/****************************************************************************
Creates a plane zone given the origin and orientation. Origin and
Creates a plane zone given the origin and orientation. Origin and

Environment: Internal  and  External
See Also: 
History:
 ****************************************************************************/
extern UFUNEXPORT int UF_FLTR_create_plane_zone(
tag_t  part_tag ,/* <I>
                 Part in which zone is to be created.
                 */
char *  name ,/* <I>
              Name of zone to be created.
              */
double  origin[3] ,/* <I>
                   Origin of zone (in Absolute Coordinates.)
                   */
double orientation[9] ,/* <I>
                       Orientation of plane zone.
                       */
tag_t * zone_tag  /* <I/O>
                  Tag of zone created.
                  */
);

/******************************************************************************
Outputs the parameters of the box zone specified by a tag.

The corner value represents an offset position which can be 
subtracted from the centroid position to give the minimum corner, 
or added to the centroid position to give the maximum corner. 
The corner value is always positive in value.

Say the bounding box has a minimum corner of 0,0,0 and 
maximum corner of 100,100,100. The centroid is at 
((0,0,0)+(100,100,100))/2 = (50,50,50) whilst the 
corner calculation is ((100,100,100)-(0,0,0))/2 = (50,50,50).

Environment: Internal  and  External
See Also: 
History:
******************************************************************************/
extern UFUNEXPORT int UF_FLTR_ask_box_zone(
tag_t box_zone ,/* <I>
                Tag of zone being queried
                */
char* name ,/* <O>
            Name of zone being queried (30 chars max)
            */
double  centroid[3] ,/* <O>
                     Centroid of zone (in Absolute Coordinates.)
                     */
double  corner[3] ,/* <O>
                   Corner vector
                   */
double matrix[9]  /* <O>
                  Orientation of zone.
                  */
);

/******************************************************************************
Outputs the parameters of the plane zone referred to by a tag.

Environment: Internal  and  External
See Also: 

History:
******************************************************************************/

extern UFUNEXPORT int UF_FLTR_ask_plane_zone(
tag_t plane_zone ,/* <I>
                  tag of zone being queried.
                  */
char name[ UF_OBJ_NAME_BUFSIZE ] ,/* <O>
               The output should be declared as char *buffer[ UF_OBJ_NAME_BUFSIZE ]
               Name of zone being queried
               */
double  origin[3] ,/* <O>
                   Origin of zone (in Absolute Coordinates.)
                   */
double matrix[9]  /* <O>
                  Orientation of plane.
                  */
);

/******************************************************************************
Modifies the box zone referred to by a tag to have the values passed
in by name, centroid, corner and matrix.

Environment: Internal  and  External
See Also: 
History:
******************************************************************************/
extern UFUNEXPORT int UF_FLTR_edit_box_zone(
tag_t zone ,/* <I>
            Tag of zone to be edited.
            */
char * name ,/* <I>
             New name of zone.
             */
double  centroid[3] ,/* <I>
                     New centroid of zone (in Absolute Coordinates.)
                     */
double  corner[3] ,/* <I>
                   New corner vector
                   */
double matrix[9]  /* <I>
                  New orientation of zone.
                  */
);

/******************************************************************************
Modifies the plane zone referred to by a tag to have the values passed
in by name, origin and matrix.

Environment: Internal  and  External
See Also: 
History:
******************************************************************************/
extern UFUNEXPORT int UF_FLTR_edit_plane_zone(
tag_t zone ,/* <I>
            tag of zone to be modified.
            */
char * name ,/* <I>
             New name of zone.
             */
double  origin[3] ,/* <I>
                   New origin of zone (in Absolute Coordinates.)
                   */
double matrix[9]  /* <I>
                  New orientation of plane.
                  */
);

/******************************************************************************
Automatically generates box zones along all 3 axes of the WCS in a
part. If use_part_volume is TRUE, the zones are created to divide up
the entire volume occupied by the part.

Environment: Internal  and  External
See Also:
History:
******************************************************************************/
extern UFUNEXPORT int UF_FLTR_auto_create_box_zones(
tag_t  part_tag ,/* <I>
                 part in which zones are to be created.
                 */
char * prefix_text ,/* <I>
                    Name to be used as prefix of auto-generated
                    zones. (e.g. "ZONE" makes ZONE1, ZONE2 etc.)
                    */
int  num_in_dir[3] ,/* <I>
                    Number of zones to be created in each direction of
                    the WCS.
                      num_in_dir[0] = number of zones in X direction
                      num_in_dir[1] = number of zones in Y direction
                      num_in_dir[2] = number of zones in Z direction
                    */
logical use_part_volume ,/* <I>
                         Flag which indicates region to be zoned.  if TRUE,
                         part extents are used. If FALSE, user_spec_vol and
                         user_spec_origin are used (See below).
                         */
double  user_spec_vol[3] ,/* <I>
                          User specified volume to be zoned.  If
                          use_part_volume is TRUE, user_spec_vol is
                          ignored.
                          user_spec_vol[0] extent of volume in X direction
                          user_spec_vol[1] extent of volume in Y direction
                          user_spec_vol[2] extent of volume in Z direction
                          */
double  user_spec_origin[3] ,/* <I>
                             User specified origin of volume to be zoned.  If
                             use_part_volume is TRUE, user_spec_origin is
                             ignored.
                             user_spec_origin[0] X coordinate of origin
                             user_spec_origin[1] Y coordinate of origin
                             user_spec_origin[2] Z coordinate of origin.
                             */
tag_t **  zone_list ,/* <OF,len:num_zones_created>
                     List of resulting zone tags.  Must be freed by the 
                     caller using UF_free.
                     */
int * num_zones_created  /* <O>
                         Number of zones in zone_list.
                         */
);

/******************************************************************************
Automatically generates plane zones along the Z axis of the WCS in a
part.  If use_part_disp is TRUE, the zones are created to cover the
entire Z displacement of the part.

Environment: Internal  and  External
See Also: 
History:
******************************************************************************/
extern UFUNEXPORT int UF_FLTR_auto_create_plane_zones(
tag_t  part_tag ,/* <I>
                 part in which zones are to be created.
                 */
char * prefix_text ,/* <I>
                    Name to be used as prefix of auto-generated
                    zones. (e.g. "ZONE" makes ZONE1, ZONE2 etc.)
                    */
int  num_in_dir ,/* <I>
                 Number of zones to be created in the Z direction of
                 the WCS.
                 */
logical use_part_disp ,/* <I>
                       Flag which indicates region to be zoned.  if TRUE,
                       part extents along the Z axis of WCS are used. If
                       FALSE, user_spec_z_disp and user_spec_origin are
                       used (See below).
                       */
double  user_spec_z_disp ,/* <I>
                          User specified Z displacement to be zoned.  If
                          use_part_disp is TRUE, this argument is ignored.
                          */
double  user_spec_origin[3] ,/* <I>
                             User specified origin of volume to be zoned.  If
                             use_part_disp is TRUE, user_spec_origin is
                             ignored.
                             user_spec_origin[0] X coordinate of origin
                             user_spec_origin[1] Y coordinate of origin
                             user_spec_origin[2] Z coordinate of origin.
                             */
tag_t **  zone_list ,/* <OF,len:num_zones_created>
                     List of resulting zone tags.  Must be freed by the
                     caller using UF_free.
                     */
int * num_zones_created  /* <O>
                         Number of zones in zone_list.
                         */
);

/*******************************************************************************
Tests whether an object is within some distance of a zone. Currently
the object can only be a part occurrence. The zone can be either a box
or a plane zone.

Environment: Internal  and  External
See Also:
History:
******************************************************************************/
extern UFUNEXPORT int UF_FLTR_is_obj_intsct_zone(
double distance ,/* <I>
                 Distance between zone and part occurrence (in part
                 units).
                 */
tag_t  zone ,/* <I>
             Tag of zone.
             */
tag_t  object ,/* <I>
                tag of object.  Currently only part occurrences are
                supported.
                */
logical *  result  /* <O>
                   Result of comparison.
                   result = TRUE if some portion of object is within
                            distance of zone.
                   result = FALSE if no portion of object is within
                            distance of zone.
                   */
);

/******************************************************************************
Tests whether an object is further than some distance of a zone.

Environment: Internal  and  External
See Also:
History:
*****************************************************************************/ 
extern UFUNEXPORT int UF_FLTR_is_obj_inside_box_zone(
double distance ,/* <I>
                 Distance between zone and part occurrence (in part units).
                 */
tag_t  zone ,/* <I>
             Tag of zone. (Must be box zone)
             */
tag_t object ,/* <I>
              Tag of object. Currently only part occurrences are supported.
              */
logical *  result  /* <O>
                   Result of comparison.
                   result = TRUE if no portion of object is further
                            than distance from zone.
                   result = FALSE if any portion of object is further
                            than distance from zone.
                   */
);

/******************************************************************************
Tests whether a part occurrence is above a planar zone. Note that this
function can only be used with a plane zone.

Environment: Internal  and  External
See Also:
History:
*****************************************************************************/
extern UFUNEXPORT int UF_FLTR_is_obj_above_plane_zone(
tag_t  zone ,/* <I>
             Tag of zone. Must be a plane zone.
             */
tag_t  object ,/* <I>
                tag of object.  Currently only part occurrences are
                supported.
                */
logical *  result  /* <O>
                   Result of comparison:
                    TRUE = if any portion of object is above the plane
                           specified by zone.
                    FALSE = if no portion of object is above the plane
                    i       specified by zone.
                   */
);

/******************************************************************************
Creates a filter object given the name and condition.

Environment: Internal  and  External
See Also:
History:
*****************************************************************************/
extern UFUNEXPORT int UF_FLTR_create_filter(
tag_t  part_tag ,/* <I>
                 part in which filter is to be created.
                 */
char *  name ,/* <I>
              Name of filter to be created.
              */
char *  condition ,/* <I>
                   Condition of filter to be created. For example,
                   "Within(0,ZONE_PLANE_P1)"
                   */
tag_t * zone_tag  /* <I/O>
                  Tag of filter created.
                  */
);

/******************************************************************************
Returns name and condition of a given filter.

Environment: Internal  and  External
See Also:
History:
******************************************************************************/
extern UFUNEXPORT int UF_FLTR_ask_filter(
tag_t  filter_tag ,/* <I>
                   Filter which is being queried
                   */
char  name[ UF_OBJ_NAME_BUFSIZE ] ,/* <O>
              Name of filter (30 chars max).
              */
char condition[132]  /* <O>
                   Condition of filter (132 chars max).
                   */
);

/******************************************************************************
Gives filter new name and condition.

Environment: Internal  and  External
See Also:
History:
******************************************************************************/
extern UFUNEXPORT int UF_FLTR_edit_filter(
tag_t  filter_tag ,/* <I>
                   Filter which is being edited
                   */
char *  name ,/* <I>
              New name of filter (30 chars max).
              */
char *  condition  /* <I>
                   New condition of filter (132 chars max).
                   */
);

/******************************************************************************
Evaluate whether object matches the given filter.

Environment: Internal  and  External
See Also:
History:
*****************************************************************************/
extern UFUNEXPORT int UF_FLTR_evaluate_filter(
tag_t  input_object ,/* <I>
                     Object to test against filter.  Currently only part
                     occurrences are supported.
                     */
tag_t  filter_tag ,/* <I>
                   Tag of filter in question.
                   */
logical * result  /* <O>
                  Result of filter evaluation.  TRUE if object matches
                  the given filter. Otherwise FALSE.
                  */
);

/******************************************************************************
Returns the bounding box information for an assembly and all of the
components in it, or for a particular component. The edges of the box
are parallel to the axis of the absolute coordinate system.

Environment: Internal  and  External
See Also:
History:This function was originally released in V13.0.4.
******************************************************************************/
extern UFUNEXPORT int UF_FLTR_ask_box_of_assy(
tag_t   assy, /* <I>
              Tag of the assembly, component, or subassembly to box.
              */ 
double  centroid[3], /* <O>
                     Center of box
                     */ 
double  corner[3], /* <O>
                   Corner vector (diagonal corner coordinates of the box can be 
                   calculated by adding and subtracting this vector from the
                   centroid location)
                   */
double  orientation[9] /* <O>
                       Orientation of box with respect to absolute 
                       coordinate system.
                       */
);

/******************************************************************************
Returns if the given NX object has a bounding box recorded for it.

Environment: Internal  and  External
See Also:
History:This function was originally released in V18.0.5.2
******************************************************************************/
extern UFUNEXPORT int UF_FLTR_object_has_box(
tag_t   object, /* <I>
              Tag of the object to question.
              */ 
logical  *has_box /* <O>
                    True if the object has a box, false otherwise
                   */ 
);


/******************************************************************************
Updates the assembly structure of the given part.
The interactively equivalent is found on the assembly node in the 
Assembly Navitagor (ANT) as Update Structure.
It uses file time stamps to see which parts have been modified since
the assembly was last saved, these parts are then loaded to get the
assembly structure, and component attributes, up to date, and are
then unloaded.

Environment: Internal  and  External
See Also:
History:This function was originally released in V15.0.
*****************************************************************************/
extern UFUNEXPORT int UF_FLTR_update_structure(
tag_t part /* <I>
           part to update assembly structure of
           */
);

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif /* UF_FLTR_H_INCLUDED */

