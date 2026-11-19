/*******************************************************************************

             Copyright (c) 1998-2004 Unigraphics Solutions, Inc.
                       Unpublished - All Rights Reserved



File Description:
The subroutines in this file describes parts list functions.
These include functions to:
  . Get the tag of a parts list.
  . Define the fields of a parts list.
  . Remove a field from a parts list.
  . Set priorities for parts list fit rules.
  . Set the display modes of a parts list.
  . Set the character sizes for the parts list fit rules and then put
    the character sizes in the data base.
  . Add a list of objects to the parts list.
  . Remove a list of objects from the parts list.
  . List a parts list to the current listing device.
  . Create a parts list note.
  . Get the object identifier of a parts list note
*******************************************************************************/


#ifndef UF_PLIST_H_INCLUDED
#define UF_PLIST_H_INCLUDED

#include <uf_defs.h>
#include <libufun_exports.h>
#include <uf_plist_types.h>
#include <uf_tabnot_types.h>
#include <uf_retiring.h>

/***************************************************************************

  ***************************************************************************/


#ifdef __cplusplus
extern "C" {
#endif

/*****************************************************************************
                        Parts List C Interface
****************************************************************************/

/****************************************************************************
Lists the parts list to the current listing device. This takes into
consideration any additions or removals from the parts list, any
changes to: the member attributes, the parts list format, or the output
modes like sorting and callouts.

Return:
         Error code:
        0       = Success
        1       = No parts list members
        2       = No key or quantity field defined
      > 2        = Some other output error

Environment: Internal  and  External
See Also:
History:
*****************************************************************************/
extern UFUNEXPORT int UF_PLIST_list(
tag_t obj_id  /* <I>
              The object identifier of the parts list.
              */
);
/****************************************************************************
Lists the parts list to the specified output file. This takes into
consideration any additions or removals from the parts list, any
changes to: the member attributes, the parts list format, or the output
modes like sorting and callouts.

Parameters:
   tag_t obj_id        <I>  The object identifier of the parts list.
   char *out_filename  <I>  Filename of output file.
   int   new_file      <I>  Boolean where
                               0 -> append to existing out_filename
                               1 -> write to new out_filename
   char *plist_level   <I>  Parts list level string
Return:
   Error code:
      0       = Success
      1       = No parts list members
      2       = No key or quantity field defined
      > 2     = Some other output error

Environment: Internal  and  External
See Also:
History:
*****************************************************************************/
extern UFUNEXPORT int UF_PLIST_list_to_file(
   tag_t obj_id,                /* <I>  The object identifier of the parts list */
   const char *out_filename,    /* <I>  Filename of output file */
   int new_file,                /* <I>  Boolean for output */
   const char *plist_level      /* <I>  Parts list level string */
);

/*********************************************************************************
 *
 * Create a generic parts list (one with three columns: a callout column,
 *                              a general column with a $PART_NAME attribute
 *                              and a quantity column)
 *
 * See also:
 *
 * History:
 *
 ********************************************************************************/

extern UFUNEXPORT int UF_PLIST_create(
    UF_PLIST_prefs_p_t prefs,           /* <I> Parts list preferences */
    double origin[3],                   /* <I> Origin */
    tag_t *parts_list                   /* <O> New parts list */
);

/*********************************************************************************
 *
 * Create a parts list from a template
 *
 * See also:
 *
 * History:
 *
 ********************************************************************************/

extern UFUNEXPORT int UF_PLIST_create_from_template(
    const char *template_name,          /* <I> Name of template part */
    double origin[3],                   /* <I> Origin */
    tag_t *parts_list                   /* <O> New parts list */
);

/*********************************************************************************
 *
 * Get the parts list preferences of a parts list
 *
 * See also:
 *
 * History:
 *
 ********************************************************************************/

extern UFUNEXPORT int UF_PLIST_ask_prefs(
    tag_t parts_list,                   /* <I> Parts list */
    UF_PLIST_prefs_p_t prefs            /* <O> Parts list preferences */
);

/*********************************************************************************
 *
 * Set the parts list preferences of a parts list
 *
 * See also:
 *
 * History:
 *
 ********************************************************************************/

extern UFUNEXPORT int UF_PLIST_set_prefs(
    tag_t parts_list,                   /* <I> Parts list */
    UF_PLIST_prefs_p_t prefs            /* <I> Parts list preferences */
);

/*********************************************************************************
 *
 * Create a manual parts list row.  The row can later be added to a parts list
 * using UF_TABNOT_add_row.
 *
 * See also:
 *
 * History:
 *
 ********************************************************************************/

extern UFUNEXPORT int UF_PLIST_create_manual_row(
    double height,                      /* <I> Row height */
    tag_t *row                          /* <O> New row */
);

/*********************************************************************************
 *
 * Create a parts list column.  The column can later be added to a parts list
 * using UF_TABNOT_add_column.
 *
 * See also:
 *
 * History:
 *
 ********************************************************************************/

extern UFUNEXPORT int UF_PLIST_create_column(
    double width,                       /* <I> Column width */
    UF_PLIST_col_prefs_p_t col_prefs,   /* <I> Column preferences */
    UF_PLIST_column_type_t column_type, /* <I> Column type */
    tag_t *column                       /* <O> New column */
);

/*********************************************************************************
 *
 * Add an object to a parts list.  The following describes the behaviors for
 * each type of object added:
 *
 *  Component                        Add the component as a parts list member.  If
 *                                   add_components_as_subassemblies is TRUE, then
 *                                   the components will be added as subassemblies
 *                                   to the parts list.  This will cause all of the
 *                                   components that are descendents of the added
 *                                   component to be added to the parts list.
 *  Solid body                       Add the solid body as a parts list member.
 *  Curve (line, circle or spline)   Add the curve as a parts list member.
 *  Member view                      Associate the parts list with the given member
 *                                   view.  This will cause the view to be automatically
 *                                   populated with callout symbols if the related
 *                                   parts list preferences are set.
 *
 * See also:
 *
 * History:
 *
 ********************************************************************************/

extern UFUNEXPORT int UF_PLIST_add_object(
    tag_t parts_list,                   /* <I> Parts list */
    logical add_components_as_subassemblies, /* <I> If TRUE, components are added as
                                               subassemblies */
    tag_t object                        /* <I> Object to add */
);

/*********************************************************************************
 *
 * Remove an object to a parts list.  See the documentation for UF_PLIST_add_object for
 * information on the types of objects that can be added or removed.
 *
 * See also:
 *
 * History:
 *
 ********************************************************************************/

extern UFUNEXPORT int UF_PLIST_remove_object(
    tag_t parts_list,                   /* <I> Parts list */
    logical remove_components_as_subassemblies, /* <I> If TRUE, components are removed as
                                                   subassemblies */
    tag_t object                        /* <I> Object to remove */
);

/*********************************************************************************
 *
 * List objects associated to a parts list.  This includes all members and member views.
 *
 * See also:
 *
 * History: Initially released in NX2.0.0.
 *
 ********************************************************************************/

extern UFUNEXPORT int UF_PLIST_ask_objects(
    tag_t parts_list,                   /* <I> Parts list */
    int *nm_objects,                    /* <O> Number of objects */
    tag_t **objects                      /* <OF,len:nm_objects Objects> */
);

/*********************************************************************************
 *
 * Get the traversal settings of a parts list
 *
 * See also:
 *
 * History:
 *
 ********************************************************************************/

extern UFUNEXPORT int UF_PLIST_ask_traversal_settings(
    tag_t parts_list,                   /* <I> Parts list */
    UF_PLIST_traversal_settings_p_t traversal_settings  /* <O> Traversal settings */
);

/*********************************************************************************
 *
 * Set the traversal settings of a parts list
 *
 * See also:
 *
 * History:
 *
 ********************************************************************************/

extern UFUNEXPORT int UF_PLIST_set_traversal_settings(
    tag_t parts_list,                   /* <I> Parts list */
    UF_PLIST_traversal_settings_p_t traversal_settings  /* <I> Traversal settings */
);

/*********************************************************************************
 *
 * Get the lock state of a parts list row
 *
 * See also:
 *
 * History:
 *
 ********************************************************************************/

extern UFUNEXPORT int UF_PLIST_ask_row_lock(
    tag_t row,                          /* <I> Parts list row */
    logical *lock_state                 /* <O> Lock state */
);

/*********************************************************************************
 *
 * Set the lock state of a parts list row
 *
 * See also:
 *
 * History:
 *
 ********************************************************************************/

extern UFUNEXPORT int UF_PLIST_set_row_lock(
    tag_t row,                          /* <I> Parts list row */
    logical lock_state                  /* <I> Lock state */
);

/*********************************************************************************
 *
 * Attach or detach parts list rows
 *
 * See also:
 *
 * History:
 *
 ********************************************************************************/

extern UFUNEXPORT int UF_PLIST_attach_rows(
    tag_t parent_row,                   /* <I> Parts list row that will become the parent.
                                         If equal to NULL_TAG, attach to the bottom
                                         of the parts list. */
    int nm_rows,                        /* <I> Number of children_rows. If set to zero,
                                         any rows previously attached will become
                                         unattached */
    tag_t *children_rows                /* <I,len:nm_rows> Rows that will become the children rows */
);

/*********************************************************************************
 *
 * Get the attached parts list rows that are children of the specified
 * parts list or row
 *
 * See also:
 *
 * History:
 *
 ********************************************************************************/

extern UFUNEXPORT int UF_PLIST_ask_attached_rows(
    tag_t parent,                   /* <I> Parts list or parts list row */
    int *nm_rows,                   /* <O> Number of children_rows */
    tag_t **children_rows           /* <OF,len:nm_rows> Children rows */
);

/*********************************************************************************
 *
 * Retrieves the default parts list preferences
 *
 * See also:
 *
 * History:
 *
 ********************************************************************************/
extern UFUNEXPORT int UF_PLIST_ask_default_prefs(
    UF_PLIST_prefs_p_t plist_prefs    /* <O> The default parts list preferences */
);

/*********************************************************************************
 *
 * Sets the default parts list preferences
 *
 * See also:
 *
 * History:
 *
 ********************************************************************************/
extern UFUNEXPORT int UF_PLIST_set_default_prefs(
    UF_PLIST_prefs_p_t plist_prefs      /* <I> The parts list preferences to set */
);

/*********************************************************************************
 *
 * Retrieves the default column preferences
 *
 * See also:
 *
 * History:
 *
 ********************************************************************************/
extern UFUNEXPORT int UF_PLIST_ask_default_col_prefs(
    UF_PLIST_col_prefs_p_t col_prefs     /* <O> The default column preferences */
);

/*********************************************************************************
 *
 * Ask the preferences for a column
 *
 * See also:
 *
 * History:
 *
 ********************************************************************************/
extern UFUNEXPORT int UF_PLIST_ask_col_prefs(
    tag_t col,                          /* <I> The column we want the preferences for */
    UF_PLIST_col_prefs_p_t col_prefs    /* <O> The preferences for the column */
);

/*********************************************************************************
 *
 * Set the preferences for a column
 * Note: The preferences are only applied to new cells that get added to the column. 
 * Function UF_TABNOT_set_cell_prefs can be used to modify the preferences of 
 * existing cells of a column.
 * 
 * See also:
 *
 * History:
 *
 ********************************************************************************/
extern UFUNEXPORT int UF_PLIST_set_col_prefs(
    tag_t col,                             /* <I> The column which preferences are to be set */
    UF_PLIST_col_prefs_p_t col_prefs       /* <I> The preferences for the column */
);

/*********************************************************************************
 *
 * Get the nested assemblies parent component
 *
 * See also:
 *
 * History:
 *
 ********************************************************************************/
extern UFUNEXPORT int UF_PLIST_ask_nested_assy_parent_comp(
    tag_t column,                          /* <I> Part List column to for nested assy.
                                              This must be a quantity column.         */
    tag_t *component                       /* <O> Parent component */
);

/*********************************************************************************
 *
 * Set the nested assemblies parent component
 *
 * See also:
 *
 * History:  Added in NX4
 *
 ********************************************************************************/
extern UFUNEXPORT int UF_PLIST_set_nested_assy_parent_comp(
    tag_t column,                          /* <I> Part List column to for nested assy.
                                              This must be a quantity column.         */
    tag_t component                        /* <I> Parent component - the component
                                              for which quantities will be counted
                                              in the specified column.  For the row
                                              that represents this component, an X
                                              will display.  Set this to NULL_TAG
                                              to disable nested assemblies for this
                                              column.                               */
);

/*********************************************************************************
 *
 * Update a parts list
 *
 * See also:
 *
 * History:  Added in NX4
 *
 ********************************************************************************/
extern UFUNEXPORT int UF_PLIST_update(
    tag_t parts_list                       /* <I> Parts list */
);

/*********************************************************************************
 *
 * Update all parts list in the work part
 *
 * See also:
 *
 * History:  Added in NX6
 *
 ********************************************************************************/
extern UFUNEXPORT int UF_PLIST_update_all_plists( );

/*********************************************************************************
 *
 * Get the object identifiers of the parts lists. This causes the parts
 * list object to be created if necessary.
 *
 * See also:
 *
 * History: Added in NX602
 *
 ********************************************************************************/
extern UFUNEXPORT int UF_PLIST_ask_tags( 
    tag_p_t *parts_list,                       /* <OF> Tags of Parts Lists. This array 
                                                must be freed by calling UF_free */
     int *num                                  /* <O> Number of Parts Lists */
);

/*********************************************************************************
 *
 * Get the method for displaying the locked deleted row of the parts list
 *
 * Parameters :
 *       tag_t row        <I> The object identifier for the row
 *       int *ldr_method  <O> The display method used for locked deleted row
 *                              = 1  -> Strike thru
 *                              = 2  -> Blanked
 *                              = 3  -> Hidden
 *                              = 4  -> Ordinary
 *                              = -1 -> The row is not locked and deleted
 *
 * Return code :
 *           = 0 : successful
 *           > 0 : failing error number
 *           < 0 : failing error number
 *
 * See also:
 *
 * History: Added in NX602
 *
 ********************************************************************************/
extern UFUNEXPORT int UF_PLIST_ask_ldr_method(
    tag_t row,          /* <I> Parts list row */
    int *ldr_method     /* <O> Display method */
    );

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif
