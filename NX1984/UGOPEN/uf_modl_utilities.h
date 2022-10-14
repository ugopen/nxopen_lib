/*****************************************************************************
                  Copyright (c) 1999-2007 UGS Corp.
                       All Rights Reserved



File description:

    Open API modeling utility functions.

*****************************************************************************/

#ifndef UF_MODL_UTILITIES_H_INCLUDED
#define UF_MODL_UTILITIES_H_INCLUDED


/***************************************************************************

  ***************************************************************************/

#include <uf_defs.h>
#include <uf_modl_types.h>
#include <libufun_exports.h>

#ifdef __cplusplus
extern "C" {
#endif

/****************************************************************************
This function cycles the database for the first, or next, available object
that matches both the type, and subtype, for the values entered.
When searching for the first object, just input a NULL_TAG for the
value of object identifier.  Then, when you need the next object, just
input the previous value, and the next matching object is returned to the
user.  When the final object has been returned to the user, the next call
to UF_MODL_ask_object() returns a NULL_TAG value for obj_id and an integer
return code that corresponds to "Invalid object type" when input into
UF_get_fail_message.

Environment: Internal  and  External
See Also:
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_object(
int ug_type ,/* <I>
             Object Type
             */
int ug_subtype ,/* <I>
                Object subtype
                */
tag_t * object  /* <I/O>
                Object's object identifier within a file
                */
);

/****************************************************************************
Retrieves the count from a linked list of objects. A list of objects may
contain identifiers for bodies, features, faces, and edges.
 If one of the nodes in the list contains an object identifier
that is a NULL_TAG, it is possible to receive an incorrect count.

Environment: Internal  and  External
See Also:
 UF_MODL_ask_list_item
 UF_MODL_create_list
 UF_MODL_delete_list
 UF_MODL_put_list_item
 UF_MODL_delete_list_item
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_list_count(
uf_list_p_t list ,/* <I>
                  List of object identifiers.
                  */
int * count  /* <O>
             Count of items in linked list.
             */
);

/****************************************************************************
Retrieves an object from a linked list of objects. A list of objects may
contain identifiers for bodies, features, faces, and edges. Normal C
indexing is used; i.e., the list begins at zero.

Environment: Internal  and  External
See Also:
 UF_MODL_create_list
 UF_MODL_delete_list
 UF_MODL_ask_list_count
 UF_MODL_put_list_item
 UF_MODL_delete_list_item
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_list_item(
uf_list_p_t list ,/* <I>
                  List of object identifiers.
                  */
int index ,/* <I>
           Count into the list.
           */
tag_t * object  /* <O>
                Object to be located.
                */
);

/****************************************************************************
Adds the input object identifier to the end of the list that you input.
NOTE: Duplicate tags added to the list are ignored.

Environment: Internal  and  External
See Also:
 UF_MODL_ask_list_item
 UF_MODL_create_list
 UF_MODL_delete_list
 UF_MODL_ask_list_count
 UF_MODL_delete_list_item
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_put_list_item(
uf_list_p_t list ,/* <I>
                  List of object identifiers.
                  */
tag_t obj_id  /* <I>
              Object identifier to put into list
              */
);

/****************************************************************************
Creates a linked list of objects. A list of objects may contain
identifiers for bodies, features, faces and edges. You use this routine
to create a list for those modeling routines that require a list as an
input; please do not use this for ask routines that return lists.

Environment: Internal  and  External
See Also:
 UF_MODL_ask_list_item
 UF_MODL_delete_list
 UF_MODL_ask_list_count
 UF_MODL_put_list_item
 UF_MODL_delete_list_item
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_create_list(
uf_list_p_t * list  /* <OF>
                    List of object identifiers.
                    */
);

/****************************************************************************
Deallocates the memory for a linked list of objects, the objects
themselves are not deleted. A list of objects may contain identifiers
for bodies, features, faces and edges.

Environment: Internal  and  External
See Also:
 UF_MODL_ask_list_item
 UF_MODL_create_list
 UF_MODL_ask_list_count
 UF_MODL_put_list_item
 UF_MODL_delete_list_item
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_delete_list(
uf_list_p_t * list  /* <I>
                    List of object identifiers
                    */
); /* <NON_NXOPEN> */

/****************************************************************************
Delete object identifier from a linked list of object identifiers.
NOTE: Deleting all the items in a list also causes the list to be
deleted.

Environment: Internal  and  External
See Also:
 UF_MODL_ask_list_item
 UF_MODL_create_list
 UF_MODL_delete_list
 UF_MODL_ask_list_count
 UF_MODL_put_list_item
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_delete_list_item(
uf_list_p_t * list ,/* <I>
                    list of object identifiers
                    */
tag_t object  /* <I>
              object to be deleted from list.
              */
); /* <NON_NXOPEN> */

/****************************************************************************
Retrieves an object from a linked list of objects. A list of objects may
contain identifiers for bodies, features, faces and edges.
Loop type for a face is Peripheral only for a non-periodic (topologically flat)
face.  Loops on a periodic face are either Holes or "Other".

Environment: Internal  and  External
See Also:
 UF_MODL_ask_face_topology
 UF_MODL_delete_loop_list
 UF_MODL_ask_loop_list_count
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_loop_list_item(
uf_loop_p_t loop_list ,/* <I>
                       List of object identifiers
                       */
int index ,/* <I>
           Count into the list
           */
int * type ,/* <O>
            Peripheral=1, Hole=2, Other=3
            */
uf_list_p_t * list  /* <OF,free:UF_MODL_delete_loop_list>
                    Pointer to the list of edge object identifiers.  This
                    should not be freed, as it will be freed when the entire
                    loop list is freed by calling UF_MODL_delete_loop_list.
                    */
);

/****************************************************************************
The input is a single pointer to a loop list, which frees each edge list
within the loop list.

Environment: Internal  and  External
See Also:
 UF_MODL_ask_loop_list_item
 UF_MODL_ask_loop_list_count
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_delete_loop_list(
uf_loop_p_t * list  /* <I>
                    Pointer to a loop list
                    */
); /* <NON_NXOPEN> */

/****************************************************************************
This routine returns the count of elements within a loop list  specified
by the user.

Environment: Internal  and  External
See Also:
 UF_MODL_ask_loop_list_item
 UF_MODL_delete_loop_list
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_loop_list_count(
uf_loop_p_t list ,/* <I>
                  Pointer to a loop list
                  */
int * count  /* <O>
             Pointer to an int for the loop count
             */
);

/*****************************************************************************
Compute the direction flag for a curve or edge

The direction flag is computed base on the input point and
the input curve or edge.  We assign UF_MODL_CURVE_START_FROM_BEGIN ,
if the input point is closer to the starting point than the end
point of the curve, and UF_MODL_CURVE_START_FROM_END, otherwise.

If the curve or edge is closed and the point is on both end points, we
assign UF_MODL_CURVE_START_FROM_END.

Return: error code
Environment: Internal  and  External
See Also: 
History:
 ****************************************************************************/
extern UFUNEXPORT int UF_MODL_get_curve_edge_direction
(
    double    end_point[3] ,      /* <I> : The input endpoint */
    tag_t      curve_edge_eid , /* <I> : The input curve or edge */
    int      * direction        /* <O> : Ouput direction */
) ;



/*****************************************************************************
Assign the direction flags in a string list structure.

The direction flags are computed base on the input points and the input
string list structure. The number of points must be the same as the number
of profiles in the string list structure.

For each profile, we use the  first curve or edge.

We assign UF_MODL_CURVE_START_FROM_BEGIN ,
if the input point is closer to the starting point than the end point of the curve, and
UF_MODL_CURVE_START_FROM_END, otherwise, to the direction of the corresponding profile
in the string list structure.

If the curve or edge is closed and the point is on both end points, we
assign UF_MODL_CURVE_START_FROM_END to the direction of this profile
in the string list structure.

Return: error code.
Environment: Internal  and  External
See Also: 
History:
 ****************************************************************************/
extern UFUNEXPORT int UF_MODL_assign_string_directions
(
    double        * end_points , /* <I> An array of 3*string_list->num doubles.  */
    UF_STRING_p_t   string_list1  /* <IOF> A string list structure. */
) ;


/*****************************************************************************
Creates a string list structure. The output of this function is a pointer
to the string list structure.

Example:
UF_MODL_create_string_list call setup
UF_STRING_t     guide;
UF_STRING_p_t   gu = &guide;
UF_MODL_create_string_list( 3, 50, gu );
 Creates 3 guides containing 50 entities

Return: void
Environment: Internal  and  External
See Also: 
History:
 ****************************************************************************/
extern UFUNEXPORT void UF_MODL_create_string_list(
int  num_string ,/* <I>
                 Number of strings
                 */
int  num_object ,/* <I>
                 Number of object
                 */
UF_STRING_p_t string_list1  /* <IOF>
                           The caller passes in a pointer to an already
                           allocated UF_STRING_t structure, and this
                           routine allocates space for the arrays in the
                           structure.  The arrays allocated inside of this
                           structure must be freed by calling
                           UF_MODL_free_string_list.
                           */
);

/*****************************************************************************
Frees a string list structure.

Environment: Internal  and  External
See Also:
History:
 ****************************************************************************/
extern UFUNEXPORT void UF_MODL_free_string_list(
UF_STRING_p_t string_list  /* <I>
                           Pointer to string list structure
                           */
);

/*****************************************************************************
Initializes a string list structure.

Return: void
Environment: Internal  and  External
See Also:
History:
 ****************************************************************************/
extern UFUNEXPORT void UF_MODL_init_string_list(
UF_STRING_p_t string_list1  /* <I>
                           Pointer to string list structure
                           */
);

/*******************************************************************************
Sort features by order of update.  Notice that if feature1 updates before
feature2 then it is legal for feature2 to reference feature1.  This can be used
in a selection filter during edit.

Environment:Internal and External
See Also:
History:
*******************************************************************************/
extern UFUNEXPORT int UF_MODL_sort_features
(
    tag_t  feature1, /* <I>
                     first feature
                     */
    tag_t  feature2, /* <I>
                     second feature
                     */
    int   *result    /* <O>
                     -1 if feature1 updates before feature2
                     0 if feature1 equals feature2
                     1 if feature1 updates after feature2
                     */
);

/*****************************************************************************
Return the next feature in the feature graph based on the time stamp of the
features.

Environment:Internal and External
See Also:
History: Originally released in V16.0
******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_next_feature(
tag_t    feature,      /* <I> Feature to check */
tag_t    *next_feature /* <O>
                       Next feature.  If there is not a next feature,
                       NULL_TAG is returned.
                       */
);

/*****************************************************************************
Return the previous feature in the feature graph based on the time stamp of the
features.

Environment:Internal and External
See Also:
History: Originally released in V16.0
******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_previous_feature(
tag_t   feature,      /* <I> Feature to check */
tag_t   *prev_feature /* <O>
                      Previous feature.  If there is not a previous feature,
                      then NULL_TAG is returned.
                      */
);


/*****************************************************************************
Returns full name (type and time stamp) of feature. The name is the
NX system defined name and will not reflect renaming that the user
may have applied to the feature unless the feature is a UDF.
If the input feature is a user defined feature (UDF) the system feature name
'User Defined Feature' is considered insignificant compared to any name
applied by the user.  UDF features will return the user applied feature name.

In some cases, further refinement of the feature type is neccessary to
distinguish which functions are usable for a given feature. For example,
UF_MODL_ask_feat_type will indicate that a feature is a SWEEP, but further
refinement of the feature is needed to know if UF_MODL_ask_extrusion or
the UF_MODL_ask_sweep... functions can be used to retrieve the parameters
for the given SWEEP.

Environment:Internal and External
See Also:
 UF_MODL_ask_feat_name
 UF_MODL_ask_feat_type
History: Originally released in V19.0
******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_feat_sysname(
    tag_t   feature_eid,  /* <I>
                          Feature to inguire upon
                          */
    char **feature_name   /* <OF>
                          String containing feature name.
                          Must be freed using UF_free
                          */
);

/*****************************************************************************
Returns full name (type and time stamp) of feature. The name is the
NX system defined name and will not reflect renaming that the user
may have applied to the feature.

In some cases, further refinement of the feature type is neccessary to
distinguish which functions are usable for a given feature. For example,
UF_MODL_ask_feat_type will indicate that a feature is a SWEEP, but further
refinement of the feature is needed to know if UF_MODL_ask_extrusion or
the UF_MODL_ask_sweep... functions can be used to retrieve the parameters
for the given SWEEP.

Environment:Internal and External
See Also:
 UF_MODL_ask_feat_name
 UF_MODL_ask_feat_type
History: Originally released in NX6.0.1
******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_feat_or_udf_sysname(
    tag_t   feature_eid,  /* <I>
                          Feature to inguire upon
                          */
    char **feature_name   /* <OF>
                          String containing feature name.
                          Must be freed using UF_free
                          */
);

/******************************************************************************
Returns the bounding box of wireframe and solid type objects.
Wireframe objects include lines, arcs, splines, and conics.  Solid type
objects include bodies, faces, and edges.  Bounding box values are
returned in absolute coordinate values according to where the object
exists in the part file.

If you call this function with an occurrence, the bounding box
of the underlying geometry is transformed into assembly space. This
may cause the bounding box that is returned to be larger than
expected. This happens in cases when the axes of the component part
are transformed such that they don't align with the axes of the
assembly coordinate system.

Note that the box returned favors speed over accuracy. The returned
box will contain the given entity and it will usually be close
to the minimum bounding box but this is not guaranteed.

This function may not return the correct information when the body
has been trimmed or is the result of a boolean operation.  In those
cases UF_MODL_ask_extreme can be used to get the correct bounding box size.

Environment: Internal  and  External
See Also: 
History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_bounding_box(
tag_t  object ,/* <I>
               Object identifier of object to ask bounding box.
               */
double bounding_box[6]  /* <O>
                        Bounding box of object.
                        [0] - minimum x value
                        [1] - minimum y value
                        [2] - minimum z value
                        [3] - maximum x value
                        [4] - maximum y value
                        [5] - maximum z value
                        */
);

/******************************************************************************
Returns the bounding box information of wireframe and solid type objects
aligned to a CSYS.

Wireframe objects include lines, arcs, splines, and conics.  Solid type
objects include bodies, faces, and edges.  Bounding box values are
returned in absolute coordinate values according to where the object
exists in the part file and aligned to the input CSYS.

If you call this function with an occurrence, the bounding box
of the underlying geometry is transformed into assembly space.

Use occurrence object tags when working in an assembly context and prototype
object tags when working in non-assembly situations. Passing in a prototype
object tag when in an assembly may produce undesired results.

The csys_tag should always be in the context of the current work part.

Due to distance and angle tolerances, the data returned cannot be guaranteed
to be larger than the original object. The expand parameter allows for an
expanded box to be created. The expand option will expand the box in all
directions by a factor of 0.1 of the prototype part units.

To derive the corner points, use the X,Y,X components of the
min_corner  and then add the X,Y,Z components of the directions multiplied
by the X,Y,Z distances. For Example, to derive the 2 corner points:
  corner_pts[2][3]

  corner_pts[0][0] = min_corner[0]
  corner_pts[0][1] = min_corner[1]
  corner_pts[0][2] = min_corner[2]
  for i = 0 -> 2 inclusive
    corner_pts[1][i] = min_corner[i]
    for j = 0 -> 2 inclusive
      corner_pts[1][i] += directions[j][i] * distances[j]

Note that the box returned favors speed over accuracy. The returned
box will contain the given entity and it will usually be close
to the minimum bounding box but this is not guaranteed.

Environment: Internal  and  External
See Also: 
History: Originally released in V19.0
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_bounding_box_aligned(
tag_t   object ,          /* <I>
                             Object identifier of object to ask bounding box.
                          */
tag_t   csys_tag,         /* <I>
                             CSYS to use for box alignment.
                             NULL_TAG - Use Work CSYS
                          */
logical expand,           /* <I>
                             Expand the box to increase enclosure coverage
                             FALSE - Do not expand
                             TRUE  - Expand
                          */
double  min_corner[3],    /* <O>
                             Minimum corner of box of object.
                             [0] - minimum x value
                             [1] - minimum y value
                             [2] - minimum z value
                          */
double  directions[3][3], /* <O>: direction vectors of bounding box
                             [0][] - X Direction
                             [1][] - Y Direction
                             [2][] - Z Direction */
double  distances[3]      /* <O>
                             Distances to move along directions of CSYS
                             to derive all points of the bounding box.
                             [0] - X distance value
                             [1] - Y distance value
                             [2] - Z distance value
                          */
);


/******************************************************************************
Returns the bounding box information of wireframe and solid type objects
aligned to a CSYS.

Wireframe objects include lines, arcs, splines, and conics.  Solid type
objects include bodies, faces, and edges.  Bounding box values are
returned in absolute coordinate values according to where the object
exists in the part file and aligned to the input CSYS.

If you call this function with an occurrence, the bounding box
of the underlying geometry is transformed into assembly space.

Use occurrence object tags when working in an assembly context and prototype
object tags when working in non-assembly situations. Passing in a prototype
object tag when in an assembly may produce undesired results.

The csys_tag should always be in the context of the current work part.

To derive the corner points, use the X,Y,X components of the
min_corner  and then add the X,Y,Z components of the directions multiplied
by the X,Y,Z distances. For Example, to derive the 2 corner points:
  corner_pts[2][3]

  corner_pts[0][0] = min_corner[0]
  corner_pts[0][1] = min_corner[1]
  corner_pts[0][2] = min_corner[2]
  for i = 0 -> 2 inclusive
    corner_pts[1][i] = min_corner[i]
    for j = 0 -> 2 inclusive
      corner_pts[1][i] += directions[j][i] * distances[j]

While a more accurate box is produced, processing time may be increased
significantly.

Environment: Internal  and  External
See Also: 
History: Originally released in NX V4.0
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_bounding_box_exact(
tag_t   object ,          /* <I>
                             Object identifier of object to ask bounding box.
                          */
tag_t   csys_tag,         /* <I>
                             CSYS to use for box alignment.
                             NULL_TAG - Use Work CSYS
                          */
double  min_corner[3],    /* <O>
                             Minimum corner of box of object.
                             [0] - minimum x value
                             [1] - minimum y value
                             [2] - minimum z value
                          */
double  directions[3][3], /* <O>: direction vectors of bounding box
                             [0][] - X Direction
                             [1][] - Y Direction
                             [2][] - Z Direction */
double  distances[3]      /* <O>
                             Distances to move along directions of CSYS
                             to derive all points of the bounding box.
                             [0] - X distance value
                             [1] - Y distance value
                             [2] - Z distance value
                          */
);


#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif     /* UF_MODL_UTILITIES_H_INCLUDED */
