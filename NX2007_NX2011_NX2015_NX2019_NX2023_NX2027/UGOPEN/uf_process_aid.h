/***************************************************************************

   Copyright (c) 2001 Unigraphics Solutions, Inc.
                 Unpublished - All rights reserved

****************************************************************************
 

File Description :

This is the Open C API interface to the Manufacturing Process Aid Assistant
application. This allows the programmer access to the Process Aid objects
information contained in a part file.

*****************************************************************************/

#ifndef UF_PROCESS_AID_H_INCLUDED
#define UF_PROCESS_AID_H_INCLUDED

#include <uf_process_aid_types.h>
#include <libufun_weld_exports.h>

#ifdef __cplusplus
extern "C" {
#endif

/*****************************************************************************
    This function retrieves all the linked/extracted objects for the given 
object (prototype/linked/extracted/occurrence). if the objects retrieved 
are further linked/extracted, the function will get all those recursively.

Environment: Internal and External
See Also:
History: V18.0
*****************************************************************************/
extern UFUN_WELDEXPORT int UF_PROCESS_AID_ask_link_objects
(
    tag_t      object,              /* <I> object tag */
    tag_p_t    *linked_objects,     /* <OF,len:linked_object_count>
                                        all the linked/extracted objects 
                                        This must be freed with UF_free. */
    int        *linked_object_count /* <O> number of linked/extracted objects*/
);

/*****************************************************************************
    This function retrieves the source object for the given linked/extracted 
object.  This will give just one level up parent/source if <is_recurse> is 
passed as FALSE. Set <is_recurse> to TRUE, to retrieve the source information 
recursively, ie. in case of the linked/extracted objects being further 
linked/extracted.

    If any of the files are partially open or fully closed, that should be open
to get the required information, and can not be opened by this function due to 
a file opening error, then the function will give the file name with respective 
returned error code. It is the responsibility of the user to open the given 
file before calling the function again.

Environment: Internal and External
See Also:
History: V18.0
*****************************************************************************/
extern UFUN_WELDEXPORT int UF_PROCESS_AID_ask_source_object
(
    tag_t      object,         /* <I> linked/extracted object tag, whose 
                                      source is to be retrieved */
    logical    is_recurse,     /* <I> FALSE if required just one level up
                                            information of the source 
                                      TRUE  if need to search the source
                                            recursively */
    tag_t      *source_object, /* <O> source object tag retrieved,
                                      NULL in case of any error */
    char       **file_to_open  /* <OF>file name, in case of opening error for
                                      this file.
                                      NULL if we were able to get the 
                                      source_object.  This must be freed by
                                      calling UF_free. */
);

/*****************************************************************************
    This function returns all the datum objects of the specified types in the 
part of assembly. This function filters the datum objects by type. 

Environment: Internal and External
See Also:
History: V18.0 
*****************************************************************************/
extern UFUN_WELDEXPORT int UF_PROCESS_AID_ask_datums_in_part
(
    tag_t                  part_tag,     /* <I> The specified part in assembly 
                                              to query */
    UF_PROCESS_AID_types_t feat_type,    /* <I> The datum type filter to apply 
                                              to this query. If no filtering is 
                                              desired, then input 
                                              UF_PROCESS_AID_ALL_TYPES */
    uf_list_p_t            *feature_sets /* <OF,free:UF_MODL_delete_list> The list containing the tags 
                                              of the found process aid objects.
                                              If datum_type is
                                              UF_PROCESS_AID_ALL_TYPES, then 
                                              all of the datum objects in the
                                              part will be returned. If any
                                              other filter option, then only the
                                              objects of the specified types are
                                              returned. returns NULL if no
                                              process aid object found.  This 
                                              parameter must be freed with 
                                              UF_MODL_delete_list */
);

/*****************************************************************************
This function returns all the datum objects of specified types in the part 
of assembly. This function filters the datum objects by type.

Environment: Internal and External
See Also:
History: V18.0
*****************************************************************************/
extern UFUN_WELDEXPORT int UF_PROCESS_AID_is_datum_object(
    tag_t object,            /* <I> tag of the object */
    logical *is_datum,       /* <O> TRUE if the body is a datum otherwise
                                    returns FALSE */
    UF_PROCESS_AID_types_p_t datum_type,
                             /* <O> type of datum object */
    tag_p_t feature_set_tag  /* <O> feature set tag of the datum object */
);

/*****************************************************************************
Given the datum feature set tag, this function returns the tags of the datum
points, datum vectors and the objects involved in the datum

Environment: Internal and External
See Also:
History: V18.0
*****************************************************************************/
extern UFUN_WELDEXPORT int UF_PROCESS_AID_ask_datum_objects(
    tag_t    feature_set,         /* <I> tag of the datum location feature,
                                         datum point, certification point or
                                         measurement point feature */
    int      *num_dat_points,     /* <O> number of datum points in the given
                                         feature set */
    tag_p_t  *datum_point,        /* <OF,len:num_dat_points> 
                                         object tags of the datum point in the
                                         given feature set.  This must be freed
                                         using UF_free. */
    int      *num_dat_vectors,    /* <O> number of datum vectors in the given
                                         feature set */
    tag_p_t  *datum_vector,       /* <OF,len:num_dat_vectors>
                                         object tags of the datum vector in the
                                         given feature set.  This must be freed
                                         using UF_free. */
    int      *num_sets,           /* <O> number of sets of objects */
    int      **n_objects_in_each_set,
                                  /* <OF,len:num_sets>
                                         number of objects in each set. Use
                                         UF_free to free this */
    tag_p_t  *objects             /* <OF> tags of the objects involved in the
                                         datum feature. Use the function
                                         UF_free to free this */
);

/*****************************************************************************
Given the datum feature set tag, this function gives the array of section
planes used to create the datum feature.

Environment: Internal and External
See Also:
History: V18.0
*****************************************************************************/
extern UFUN_WELDEXPORT int UF_PROCESS_AID_ask_section_of_datum
(
    tag_t      datum_feat,      /* <I> Tag of the Datum object Feature.
                                   Possible feature types are DATUM_LOCATION,
                                   MEASUREMENT_LOCATION & HEM_VECTOR */
    int        *num_sections,   /* <O> Number of Section planes */
    tag_p_t    *sec_planes      /* <OF,len:num_sections> 
                                    Array of Section planes. Must free with
                                    UF_free */
);

/*****************************************************************************
This function gives the list of attributes for the process aid object

Environment: Internal and External
See Also:
History: V18.0
*****************************************************************************/
extern UFUN_WELDEXPORT int UF_PROCESS_AID_populate_attr_list
(
    tag_t feature_set,      /* <I> tag of the process aid feature set */
    int   *count,           /* <O> number of attributes */
    char  ***list           /* <OF,len:count>
                                   list of attributes. This array must be
                                   freed by calling UF_free_string_array */
);

/*****************************************************************************
Given a process aid feature set, this function will return its parent feature
set tag.  This means that for a certification point, this function will return
the datum point feature set tag.  For a datum point, this function will return
the datum location feature set tag

Environment: Internal and External
See Also:
History: V18.0
*****************************************************************************/
extern UFUN_WELDEXPORT int UF_PROCESS_AID_ask_parent_feature
(
    tag_t feature_set,      /* <I> tag of the process aid feature set */
    tag_t *parent_datum     /* <O> tag of the feature set of the parent datum*/
);

/*****************************************************************************
Given a process aid feature set, this function will return its children feature
set tags.  This means that for a datum location feature, this function will
return the datum point feature set tag.  For a datum point, this function will
return the certification point feature set tag

Environment: Internal and External
See Also:
History: V18.0
*****************************************************************************/
extern UFUN_WELDEXPORT int UF_PROCESS_AID_ask_children_features
(
    tag_t   feature_set,      /* <I> tag of the process aid feature set */
    int     *num_children,    /* <O> number of children features */
    tag_p_t *children         /* <OF,len:num_children>
                                 tags of the children features. This
                                 array must be freed by calling UF_free */
);

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif /* UF_PROCESS_AID_H_INCLUDED */

