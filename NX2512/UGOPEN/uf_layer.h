/*******************************************************************************

             Copyright 1998 Siemens Product Lifecycle Management Software Inc.
                               All Rights Reserved                       


   
File Description:

This file contains the subroutines that offer access to the NX
database.  Using the subroutines in this file, you can:

 . Read the work layer
 . Read the category name, member layers, and description.
 . Read the layer status.
 . Cycle by layer.
 . Edit a category description.
 . Edit a category layer.
 . Edit a category name.
 . Set the layer status.
 . Create, read, or edit a layer category.

NX6 onwards supports creation of mixed case category names along with spaces. 
Always use NX functions to determine the existence of categories with given name.
String comparison is not recommended for verifying the existence of category.
The following is the general guideline for checking for the existence of a category.

Always use the function UF_LAYER_ask_category_tag to get the tag of a category 
corresponding to name. The following is an example of a function that would check 
if a category has been created or not.
  static tag_t ask_category_tag(char *name)
  {
      tag_t  object;
      UF_CALL(UF_LAYER_ask_category_tag(name, &object));
      return object;
  }
A non null tag (NULL_TAG) returned from the above function indicates that the 
category is present. All other category related functions such as UF_LAYER_ask_category_info,
UF_LAYER_edit_category_name, UF_LAYER_edit_category_layer, UF_LAYER_edit_category_descr can 
make use of the tag obtained. The advantage of using this approach is that this function 
returns the tag of a category similar to the passed name. We consider 2 names to be similar 
if they pass case insensitive comparison. This way, even though a category is created using 
upper case, it's existence could be still queried using mixed case strings.

****************************************************************************/

#ifndef UF_LAYER_INCLUDED 
#define UF_LAYER_INCLUDED 


/***************************************************************************

***************************************************************************/


#include <uf_defs.h>
#include <uf_obj_types.h>
#include <libufun_exports.h>

#define UF_LAYER_WORK_LAYER           1
#define UF_LAYER_ACTIVE_LAYER         2
#define UF_LAYER_REFERENCE_LAYER      3
#define UF_LAYER_INACTIVE_LAYER       4

/****************************************************************************
 *
 *  UF_LAYER_CAT_DESC_LEN is being deprecated because NX is moving to support
 *  multibyte characters.  User written programs should start using the
 *  new definitions for object names defined in uf_obj_types.h instead:
 *    UF_OBJ_NAME_BUFSIZE should be used for buffer allocations and memory
 *                      allocations, e.g. char my_description[UF_OBJ_NAME_BUFSIZE];
 *    UF_OBJ_NAME_NCHARS  should be used to limit the number of characters in
 *                      a buffer.  NX code will enforce these limits.
 *  New routines have been added which will help in this transition:
 *     UF_TEXT_count_characters() will count the number of characters in a
 *     buffer.
 *     UF_TEXT_terminate_chars() will terminate a C string after the given
 *     number of characters.
 */
/*  */
#define UF_LAYER_CAT_DESC_LEN        (UF_OBJ_NAME_BUFSIZE-1)
/*  */

/*  The minimum and maximum layer numbers available.  */

#define UF_LAYER_MIN_LAYER  (1)
#define UF_LAYER_MAX_LAYER  (256)

struct UF_LAYER_category_info_s {
    char name[ UF_OBJ_NAME_BUFSIZE ];      /* The name of this category. */
    logical layer_mask[UF_LAYER_MAX_LAYER]; /* A logical for each layer, does
                                              it belong to this category or not.
                                              layer_mask[0] is TRUE if layer 1
                                              belongs to the category, otherwise
                                              it is false.  layer_mask[1] applies
                                              to layer 2, and so on.
                                            */
    char descr[ UF_OBJ_NAME_BUFSIZE ];  /* This is the description of this
                                             layer category. */
};

typedef struct UF_LAYER_category_info_s UF_LAYER_category_info_t, 
                                       *UF_LAYER_category_info_p_t;

struct UF_LAYER_status_info_s {
    int  layer_number;       /* The layer number that this status is for. 
                                Valid layers are UF_LAYER_MIN_LAYER to
                                UF_LAYER_MAX_LAYER inclusive. */
    int  layer_status;       /* The layer status.  One of the values:
                                  UF_LAYER_WORK_LAYER
                                  UF_LAYER_ACTIVE_LAYER 
                                  UF_LAYER_REFERENCE_LAYER  
                                  UF_LAYER_INACTIVE_LAYER
                             */
};

typedef struct UF_LAYER_status_info_s UF_LAYER_status_info_t, 
                                     *UF_LAYER_status_info_p_t;

#ifdef __cplusplus
extern "C" {
#endif

/******************************************************************************
Reads work layer.

Environment: Internal  and  External

See Also:

History:  New in V16.0
*******************************************************************************/
extern UFUNEXPORT int UF_LAYER_ask_work_layer(
int * layer_number  /* <O>
                    Layer number
                     */
);

/******************************************************************************
Reads layer status.

Environment: Internal  and  External

See Also:

History:
*******************************************************************************/
extern UFUNEXPORT int UF_LAYER_ask_status(
const int  layer_number ,/* <I>
                         Layer number
                         */
int * layer_status  /* <O>
                    Layer status
                      UF_LAYER_WORK_LAYER
                      UF_LAYER_ACTIVE_LAYER 
                      UF_LAYER_REFERENCE_LAYER  
                      UF_LAYER_INACTIVE_LAYER
                    */
);
/******************************************************************************
Sets the layer status to either: work layer, active layer, reference layer,
or inactive layer.

The status of the current work layer may not be changed.  You must first
set another layer to be the work layer, then change the status of
the prior work layer.

Environment: Internal  and  External

See Also:

History:  V18.0  Disallow changing the status of the current work layer
 ******************************************************************************/
extern UFUNEXPORT int UF_LAYER_set_status(
const int  layer_number ,/* <I>
                   Layer number
                   */
const int layer_status  /* <I>
                  Layer status
                      UF_LAYER_WORK_LAYER
                      UF_LAYER_ACTIVE_LAYER 
                      UF_LAYER_REFERENCE_LAYER  
                      UF_LAYER_INACTIVE_LAYER
                  */
);
/*******************************************************************************
Sets the status of all layers, except the work layer, as specified.

Environment: Internal  and  External

See Also:

History:
 *****************************************************************************/
extern UFUNEXPORT int UF_LAYER_set_all_but_work (
const int layer_status  /* <I>
                        Layer status
                            UF_LAYER_WORK_LAYER
                            UF_LAYER_ACTIVE_LAYER 
                            UF_LAYER_REFERENCE_LAYER  
                            UF_LAYER_INACTIVE_LAYER
                  */
);
/*******************************************************************************
Sets the specified layers to the corresponding specified status. The
work layer is not made reference or inactive.  Only one layer can be
the work layer. If any error occurs, then none of the layers status is
modified.

Environment: Internal  and  External
        
See Also:  UF_LAYER_status_info_p_t
        
History:
 ******************************************************************************/
extern UFUNEXPORT int UF_LAYER_set_many_layers_status (
const int count_of_layers ,/* <I>
                           Count of layers specified
                           */
UF_LAYER_status_info_p_t changes  /* <I>
                                  An array of structures where each element
                                  in the array is a structure that contains a
                                  layer number and status.
                                  */
);                                                          

/****************************************************************************
Cycles the work part by layer.

First call:     Returns first object in first enabled layer.
Next call:      Returns next object in next enabled layer.
Last call:      When all objects have been exhausted,
                *object_tag = NULL_TAG is returned.

Do not attempt to delete objects when cycling the database in a loop.  Problems
can occur when trying to read the next object when the current object has been
deleted.  To delete objects, save an array with the objects in it, and then 
when you have completed cycling, use UF_OBJ_delete_array_of_objects to delete
the saved array of objects.

UF_LAYER_cycle_by_layer returns all objects on the given layer.  This includes
objects which are not counted as objects on the layer by the "Layer Settings"
dialog.

Environment: Internal  and  External

See Also:

History:
 ****************************************************************************/
extern UFUNEXPORT int UF_LAYER_cycle_by_layer(
int  layer_number ,/* <I>
                   Layer number to cycle, pass in a layer number of 0 to
                   cycle all enabled layers.
                   */
tag_t * object_tag  /* <I/O>
                    On input the object found by the last call to this routine.
                    Begin the cycle by passing in object = NULL_TAG
                    On output, the next object on the specified layer or layers.
                    Outputs a NULL_TAG when the cycle is finished.
                    */
);


/****************************************************************************
Reads category name, member layers, and description.

Environment: Internal  and  External

See Also:  UF_LAYER_category_info_p_t

History:
 ***************************************************************************/
extern UFUNEXPORT int UF_LAYER_ask_category_info(
tag_t category ,/* <I>
                Category object identifier
                */
UF_LAYER_category_info_p_t category_info  /* <O>
                                          Pointer to category information for
                                          the given category.
                                          */
);

/****************************************************************************
Finds the tag of a category given the category name

Environment: Internal  and  External

History:  New in V18.0
 ***************************************************************************/
extern UFUNEXPORT int UF_LAYER_ask_category_tag(
const char  *category_name ,/* <I>
                      Name of the category
                      */
tag_t *category  /* <O>
                 Category object identifier.  If the category name does not
                 exist, *category will be NULL_TAG (but no error code
                 will be returned).
                 */

);

/****************************************************************************
Edit a category name.

Environment: Internal  and  External

See Also:

History:
 ****************************************************************************/
extern UFUNEXPORT int UF_LAYER_edit_category_name(
tag_t category ,/* <I>
                Category object identifier
                */
const char * cat_name  /* <I>
                 New category name
                 */
);

/****************************************************************************
Edit the layers associated with a category.

Environment: Internal  and  External

See Also:

History:
 ***************************************************************************/
extern UFUNEXPORT int UF_LAYER_edit_category_layer(
tag_t category ,/* <I>
                Category object identifier
                */
logical layer_mask[UF_LAYER_MAX_LAYER] /* <I>
                                       A logical for each layer, does
                                       it belong to this category or not.
                                       layer_mask[0] is TRUE if layer 1
                                       belongs to the category, otherwise
                                       it is false.  layer_mask[1] applies
                                       to layer 2, and so on.
                                       */
);

/****************************************************************************
Edit a category description.

Environment: Internal  and  External

See Also:

History:
 ***************************************************************************/
extern UFUNEXPORT int UF_LAYER_edit_category_descr(
tag_t category ,/* <I>
                Category object identifier
                */
const char * cat_descr  /* <I>
                  New description for this category.
                  */
);

/****************************************************************************
Create a category name, member layers, and description.

Environment: Internal  and  External

See Also:
See Also:  UF_LAYER_category_info_p_t


History:
 ***************************************************************************/
extern UFUNEXPORT int UF_LAYER_create_category(
UF_LAYER_category_info_p_t category_info ,/* <I>
                                          Pointer to category info structure
                                          */
tag_t *category  /* <O>
                 Category object identifier
                 */
);


/*
 ******************************************************************************
 ******************************************************************************
 *****     WARNING:  The routines that follow will be obsoleted soon.     *****
 *****     Do not use them!  Use their indicated replacements.            *****
 ******************************************************************************
 ******************************************************************************
*/

/* uc5007 create layer category -- replaced by UF_LAYER_create_category */
extern UFUNEXPORT int uc5007(int *ip1, const char *cp2 /* <I> */, int ip3);

/* uc5008 read category layer -- replaced by UF_LAYER_ask_category_info */
extern UFUNEXPORT int uc5008(const char *cp1 /* <I> */, int ip2, int *ir3);

/* uc5009 edit layer category -- replaced UF_LAYER_edit_category_layer */
extern UFUNEXPORT int uc5009(int *ip1, const char *cp2 /* <I> */, int ip3);


#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif   /*  END  UF_LAYER_INCLUDED  */
