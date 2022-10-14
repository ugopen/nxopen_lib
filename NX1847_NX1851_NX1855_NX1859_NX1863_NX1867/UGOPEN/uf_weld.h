/****************************************************************************

       Copyright (c) 1999-2000 Unigraphics Solutions Inc.
                 Unpublished - All rights reserved

******************************************************************************
 

File Description :

This is the Open API interface to the Weld Assistant application. This
allows the programmer access to the weld information contained in a part file.

 ***************************************************************************/


#ifndef UF_WELD_H_INCLUDED
#define UF_WELD_H_INCLUDED

/****************************************************************************

*****************************************************************************/

#include <uf_weld_types.h>
#include <uf_retiring.h>
#include <libufun_weld_exports.h>

#ifdef __cplusplus
extern "C" {
#endif

/*****************************************************************************
 To fetch an array of all weld objects in the specified assembly.
Optionally, filter the weld objects by weld type.
The weld_array must be freed using UF_free.
This replaces UF_WELD_locate_welds, which only returns legacy welds.

Environment : Internal and External
See Also :

History : Originally released in NX 5.0
*****************************************************************************/
extern UFUN_WELDEXPORT int UF_WELD_locate_welds2(
tag_t           work_part,   /* <I>
                                The specified assembly to query
                             */
UF_WELD_feature_types_array  types_array,   /* <I>
                                An array of logicals to indicate which
                                weld types to return. Use
                                UF_WELD_INIT_TYPES_ARRAY(types_array,false)
                                to initialize all to off. Use
                                UF_WELD_INIT_TYPES_ARRAY(types_array,true)
                                to get all weld types. To get a specific
                                weld feature, use UF_WELD_feature_types_e
                                to turn on a specific weld feature.

                             */
int             *count,      /* <O>
                                Pointer to the number of weld object which
                                answer the query. This may be 0.

                                This storage is not allocated by the
                                function. Pass in a valid integer location

                                If the count is not desired, pass in a NULL
                                instead of a pointer
                             */
tag_p_t         *weld_array  /* <OF,len:count>
                                The pointer in which to return the array
                                containing the tags of the found
                                weld_objects. 

                                If NULL is passed in instead of a pointer,
                                then the array is not returned.
                                Such an option might be used to simply
                                obtain a count of the objects.

                                If the pointer is returned as non_NULL,
                                then the array must be freed by UF_free
                              */
); /* <NON_NXOPEN> */

/******************************************************************************
Returns the number of welds in a weld feature set.

Environment: Internal  and  External

See Also:   UF_WELD_locate_welds2

History: Original release was in V16.0.1
******************************************************************************/
extern UFUN_WELDEXPORT int UF_WELD_ask_number_of_welds (
tag_t feature_set_tag,   /* <I>
                         Feature set tag of weld
                         */
int   *num_of_welds      /* <O>
                         Number of welds present in the weld feature set.
                         */
);

/******************************************************************************
Returns the spacing between welds in a weld feature set. If the weld is a
single or continuous weld then the spacing returned is zero.

Environment: Internal  and  External

See Also:   UF_WELD_locate_welds2

History: Original release was in V16.0.1
******************************************************************************/
extern UFUN_WELDEXPORT int UF_WELD_ask_spacing_of_welds (
tag_t  feature_set_tag,  /* <I>
                         Feature set tag of weld
                         */
double *spacing          /* <O>
                         Spacing between welds.
                         */
);

/******************************************************************************
Returns the segment length of weld in a weld feature set. If the weld is a
continuous weld then the total length of weld is returned.

Environment: Internal  and  External

See Also:   UF_WELD_locate_welds2

History: Original release was in V16.0.1
******************************************************************************/
extern UFUN_WELDEXPORT int UF_WELD_ask_segment_len_of_welds (
tag_t  feature_set_tag,  /* <I>
                         Feature set tag of weld
                         */
double *seg_len          /* <O>
                         Segment length of weld
                         */
);

/******************************************************************************
Gets the body tags of the connected parts for a weld feature set.

Environment: Internal  and  External
See Also:   UF_WELD_locate_welds2

History: Original release was in V16.0.1
******************************************************************************/
extern UFUN_WELDEXPORT int UF_WELD_ask_connected_parts (
tag_t feature_set_tag, /* <I>
                       Feature set tag of the weld
                       */
UF_WELD_conn_parts_info_p_t conn_info
                       /* <O>
                        UF_WELD_conn_parts_info_p_t. Must free ithe body tags using UF_free.
                       Info of connected parts
                       */
); /* <NON_NXOPEN> */

/******************************************************************************
Gets the attribute titles of weld belonging to a weld feature_set_tag.

Environment: Internal  and  External

See Also:   UF_WELD_locate_welds2

History: Original release was in V16.0.1
******************************************************************************/
extern UFUN_WELDEXPORT int UF_WELD_populate_attr_list (
tag_t feature_set_tag,    /* <I>
                          Feature set tag of the weld
                          */
char  ***attribute_title, /* <OF,len:count>
                          Attibute titles of the weld.
                          This must be freed by calling UF_free_string_array.
                          */
int   *count              /* <O>
                          Number of attributes of the weld.
                          */
);

/******************************************************************************
Gets all body tags of welds in a weld feature set.

Environment: Internal  and  External

See Also:   UF_WELD_locate_welds2

History: Original release was in V16.0.1
******************************************************************************/
extern UFUN_WELDEXPORT int UF_WELD_ask_body_id (
tag_t   feature_set_tag,    /* <I>
                            Feature set tag of the weld
                            */
tag_p_t *body_id,           /* <OF,len:num_objects>
                            Array of body tags of welds.
                            This must be freed by calling UF_free.
                            */
int     *num_objects        /* <O>
                            Number of welds in the weld feature set.
                            */
);

/******************************************************************************
Returns whether the input object is weld.

Environment: Internal  and  External

See Also:   UF_WELD_ask_body_id

History: Original release was in V16.0.1
******************************************************************************/
extern UFUN_WELDEXPORT int UF_WELD_is_object_weld (
tag_t object,      /* <I>
                   Tag of weld body
                   */
logical *is_weld,  /* <O>
                   TRUE if the body is weld otherwise returns FALSE
                   */
tag_p_t feature_set_tag   /* <O>
                          Feature set tag of the weld body
                          */
);

/******************************************************************************
Given a Linked or Extract feature returns the source occurrence or parent
object

Environment: Internal  and  External

See Also:   UF_WAVE_ask_link_source

History: Original release was in V16.0.1
******************************************************************************/
extern UFUN_WELDEXPORT int UF_WELD_ask_linked_feat_source(
tag_t linked_feat_tag, /* <I>
                       Tag of the linked or extract feature
                       */
tag_p_t source_obj     /* <O>
                       Tag of the source object for the feature
                       */
);

/******************************************************************************
Given a face from a Linked or Extract feature returns the source occurrence
or parent object

Environment: Internal  and  External

See Also:   UF_WAVE_ask_link_source

History: Original release was in V16.0.1
******************************************************************************/
extern UFUN_WELDEXPORT int UF_WELD_ask_linked_face_parent(
tag_t face_tag, /* <I>
                       face tag of the LINKED_FACE feature
                       */
tag_p_t source_obj     /* <O>
                       Tag of the source object for the feature
                       */
);

/******************************************************************************
Given the spot feature set tag, this function returns the tags of the spot
points and the faces involved in the weld.

Environment : Internal and External

See Also :

History : Originally Released in v16.0.1
******************************************************************************/
extern UFUN_WELDEXPORT int UF_WELD_ask_spot_weld_info(
tag_t       spot_feature_set,   /* <I>
                            tag of the spot feature set
                                */
tag_p_t     top_body,           /* <O>
                            tag of the top body
                                */
int         *spot_count,        /* <O>
                            number of spots in the feature set
                                */
tag_p_t     *spot_points,       /* <OF,len:spot_count>
                            feature tags of the spot points in the feature set.
                            Use UF_free to free this variable
                                */
int         *num_sets,          /* <O>
                            number of sets of faces
                                */
int         **n_faces_in_each_set,      /* <OF,len:num_sets>
                            number of faces in each set. Must free using
                            UF_free_string_array
                                */
tag_p_t     **set_of_faces      /*<OF,len:n_faces_in_each_set>
                            tags of the faces involved in the weld.
                            Use UF_free_string_array to free the array
                                */
);

/*****************************************************************************
Given the spot ( or clinch ) feature set tag, this function will return the
information regarding the weld.  This function will work for resistance spot,
arc spot and clinch.

Environment : Internal and External

See Also :  UF_WELD_spot_info_t
            UF_WELD_free_spot_data

History : Originally released in v16.0.1
******************************************************************************/
extern UFUN_WELDEXPORT int UF_WELD_ask_spot_face_data(
tag_t spot_feature_set,           /* <I>
                              tag of the spot feature set
                                  */
int   *num_sets,                  /* <O>
                              number of sets of faces in the spot weld
                                  */
int   *spot_count,                /* <O>
                              number of spots in the feature set
                                  */
UF_WELD_spot_info_p_t *spot_info  /* <OF,len:spot_count,free:UF_WELD_free_spot_data>
                              pointer to the data structure which contains
                              the spot weld information ( see uf_weld_types.h )
                              for the given feature set tag.  Use
                              UF_WELD_free_spot_data to free this pointer.
                                  */
);

/*****************************************************************************
Given the spot ( or clinch ) feature set tag, this function will return the
information regarding the weld.  This function will work for resistance spot,
arc spot and clinch.

Environment : Internal and External

See Also :  UF_WELD_spot_data_t
            UF_WELD_free_spot_info

History : Originally released in v18.0.4. Will be made obsolete in V20
******************************************************************************/
extern UFUN_WELDEXPORT int UF_WELD_ask_spot_face_info(
tag_t spot_feature_set,           /* <I>
                              tag of the spot feature set
                                  */
int   *num_sets,                  /* <O>
                              number of sets of faces in the spot weld
                                  */
int   *spot_count,                /* <O>
                              number of spots in the feature set
                                  */
UF_WELD_spot_data_p_t *spot_info  /* <OF,len:spot_count,free:UF_WELD_free_spot_info>
                              pointer to the data structure which contains
                              the spot weld information ( see uf_weld_types.h )
                              for the given feature set tag.  Use
                              UF_WELD_free_spot_info to free this pointer.
                                  */
);

/*****************************************************************************
Frees the memory used for storing spot weld information

Environment : Internal and External.

See Also :  UF_WELD_spot_info_t
            UF_WELD_ask_spot_face_data

History : Originally released in v16.0.1
******************************************************************************/
extern UFUN_WELDEXPORT int UF_WELD_free_spot_data(
int spot_count,                  /* <I>
                          number of spots in the spot feature set
                                 */
UF_WELD_spot_info_p_t *spot_info  /* <I,len:spot_count>
                          pointer to the data structure which contains
                          the spot weld information
                                  */
);/* <NON_NXOPEN> */

/*****************************************************************************
Frees the memory used for storing spot weld information

Environment : Internal and External.

See Also :  UF_WELD_spot_data_t
            UF_WELD_ask_spot_face_info

History : Originally released in v18.0.4 . Will be made obsolete in V20
******************************************************************************/
extern UFUN_WELDEXPORT int UF_WELD_free_spot_info (
int spot_count,                  /* <I>
                          number of spots in the spot feature set
                                 */
UF_WELD_spot_data_p_t *spot_info  /* <I>
                          pointer to the data structure which contains
                          the spot weld information
                                  */
);/* <NON_NXOPEN> */

/******************************************************************************
Given the feature set tag, this function returns the tags of the seams in the
feature set and the faces involved in the seam.  Please note that this function
works for seam weld and bead.

Environment : Internal and External.

See Also :

History : Originally released in v16.0.1
******************************************************************************/
extern UFUN_WELDEXPORT int UF_WELD_ask_seam_weld_info(
tag_t       seam_feature_set, /* <I>
                                  tag of the seam feature set
                              */
int         *seam_count,      /* <O>
                                  count of the seams in the feature set
                              */
tag_p_t     *seam_id,         /* <OF,len:seam_count>
                                  tags of the seams in the feature set. Use
                                  UF_free to free this variable.
                              */
int         *num_sets,        /* <O>
                                  number of sets of faces involved in the
                                  weld
                              */
int         **n_faces_in_each_set,      /* <OF,len:num_sets>
                            number of faces in each set. Must free using
                            UF_free_string_array
                                */
tag_p_t     **set_of_faces    /* <OF,len:n_faces_in_each_set>
                                  tags of the faces involved in the weld.
                                  Use UF_free_string_array to free the array
                              */
);

/******************************************************************************
Given the feature set tag, this function returns the guide curves for all
weld types except Groove and Edge welds. Note that guide curves are not
returned if the input tag is a Plug or Slot weld.

Environment : Internal and External.

See Also :  UF_WELD_ask_groove_or_edge_guide

History : Originally released in v16.0.1
******************************************************************************/
extern UFUN_WELDEXPORT int UF_WELD_ask_guide_curves (
tag_t weld_feat_tag,            /* <I>
                                   tag of the weld feature, can be either
                                   Fillet, Arc Spot, Resistance Spot,
                                   Resistance Seam, Bead, Tape,
                                   Dollop or Clinch
                                */
int *guide_crv_cnt,             /* <O>
                                   Number of guide curves
                                */
tag_t **guide_curves            /* <OF,len:guide_crv_cnt>
                                   tag of guide curves
                                */
);
/******************************************************************************
Given a Groove or Edge weld tag, this function returns the guide curves for
the weld. For all other types of welds refer to UF_WELD_ask_guide_curves.

Environment : Internal and External.

See Also :  UF_WELD_ask_guide_curves

History : Originally released in v16.0.1
******************************************************************************/
extern UFUN_WELDEXPORT int UF_WELD_ask_groove_or_edge_guide (
tag_t weld_feat_tag,            /* <I>
                                   tag of the weld feature, can be only
                                   Groove or Edge weld feature
                                */
uf_list_p_t *guide_crv_cnt,     /* <OF,free:UF_MODL_delete_list>
                                   tags of the first set of guide strings
                                   use UF_MODL_delete_list to free
                                */
uf_list_p_t *guide_curves       /* <OF,free:UF_MODL_delete_list>
                                   tags of the second set of guide strings
                                   use UF_MODL_delete_list to free
                                */
);

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif /* UF_WELD_H_INCLUDED */
