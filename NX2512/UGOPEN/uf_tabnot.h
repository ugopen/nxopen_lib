/****************************************************************************

                           Copyright 2003 UGS Corp.
                           All rights reserved

******************************************************************************


File Description:

    Open C API interface for tabular notes

****************************************************************************/

#ifndef UF_TABNOT_H_INCLUDED
#define UF_TABNOT_H_INCLUDED

/***************************************************************************

  ***************************************************************************/

#include <uf_defs.h>
#include <libufun_exports.h>
#include <uf_tabnot_types.h>

#ifdef __cplusplus
extern "C" {
#endif

/********************************************************************************
    Note on Tabular Notes:
    (a)A Tabular Note and Parts List is composed of one or more Tabular Note Sections. 
    (b)A tabular note section is an annotation. Functions such as UF_DRF_ask_origin and UF_DRF_ask_associative_origin 
       that expect an annotation as input need to input a tabular note section.


Note on Selection:
    (a) Selection function UF_UI_select_with_single_dialog returns a
    tabular note section in all cases. Please use the function
    UF_TABNOT_ask_tabular_note_of_section to get the tabular note from the section.
    (b) Selection of tabular note rows and columns is not currently supported.
********************************************************************************/


/*********************************************************************************
 *
 * Create a tabular note
 *
 * Note: Use the functions UF_DRF_ask_origin and UF_DRF_ask_associative_origin
 *       to retrieve the origin of a tabular note section.  Use the functions
 *       UF_DRF_set_origin and UF_DRF_set_associative_origin to set the origin
 *       of a tabular note section.
 *
 * Return :
 *           Return code :
 *           = 0 : successful
 *           > 0 : failing error number
 *           < 0 : failing error number
 *
 * Environment : Internal and External
 *
 * See also:
 *
 * History:
 *
 ********************************************************************************/

extern UFUNEXPORT int UF_TABNOT_create(
    UF_TABNOT_section_prefs_p_t prefs,  /* <I> Tabular note section preferences */
    double origin[3],                   /* <I> Origin */
    tag_t *tabular_note                 /* <O> New tabular note */
);

/*********************************************************************************
 *
 * Create a tabular note from a template
 *
 * Note: Use the functions UF_DRF_ask_origin and UF_DRF_ask_associative_origin
 *       to retrieve the origin of a tabular note section.  Use the functions
 *       UF_DRF_set_origin and UF_DRF_set_associative_origin to set the origin
 *       of a tabular note section.
 *
 * Return :
 *           Return code :
 *           = 0 : successful
 *           > 0 : failing error number
 *           < 0 : failing error number
 *
 * Environment : Internal and External
 *
 * See also:
 *
 * History:
 *
 ********************************************************************************/
extern UFUNEXPORT int UF_TABNOT_create_from_template(
    char *template_name,                /* <I> Name of template part */
    double origin[3],                   /* <I> Origin of the tabular note to create */
    tag_t *tabular_note                 /* <O> New tabular note */
);

/*********************************************************************************
 *
 * Ask the sort data of a column
 *
 * Return :
 *           Return code :
 *           = 0 : successful
 *           > 0 : failing error number
 *           < 0 : failing error number
 *
 * Environment : Internal and External
 *
 * See also:
 *
 * History:
 *
 ********************************************************************************/

extern UFUNEXPORT int UF_TABNOT_ask_column_sort_data(
    tag_t column,                       /* <I> Column */
    UF_TABNOT_sort_data_p_t sort_data   /* <O> Sort data */
);

/*********************************************************************************
 *
 * Set the sort data of a column. A subsequent call to UF_TABNOT_sort
 * will apply the sort data.
 *
 * Return :
 *           Return code :
 *           = 0 : successful
 *           > 0 : failing error number
 *           < 0 : failing error number
 *
 * Environment : Internal and External
 *
 * See also:
 *
 * History:
 *
 ********************************************************************************/

extern UFUNEXPORT int UF_TABNOT_set_column_sort_data(
    tag_t column,                       /* <I> Column */
    UF_TABNOT_sort_data_p_t sort_data   /* <I> Sort data */
);

/*********************************************************************************
 *
 * Sort the tabular note or parts list after the sort data is set
 * (using UF_TABNOT_set_column_sort_data) on all the columns.
 *
 * Return :
 *           Return code :
 *           = 0 : successful
 *           > 0 : failing error number
 *           < 0 : failing error number
 *
 * Environment : Internal and External
 *
 * See also:
 *
 * History:
 *
 ********************************************************************************/

extern UFUNEXPORT int UF_TABNOT_sort(
   tag_t tabnote_tag
);

/*********************************************************************************
 *
 * Create a tabular note row
 *
 * Return :
 *           Return code :
 *           = 0 : successful
 *           > 0 : failing error number
 *           < 0 : failing error number
 *
 * Environment : Internal and External
 *
 * See also:
 *
 * History:
 *
 ********************************************************************************/

extern UFUNEXPORT int UF_TABNOT_create_row(
    double height,                      /* <I> Row height */
    tag_t *row                          /* <O> New row */
);

/*********************************************************************************
 *
 * Create a tabular note column
 *
 * Return :
 *           Return code :
 *           = 0 : successful
 *           > 0 : failing error number
 *           < 0 : failing error number
 *
 * Environment : Internal and External
 *
 * See also:
 *
 * History:
 *
 ********************************************************************************/

extern UFUNEXPORT int UF_TABNOT_create_column(
    double width,                       /* <I> Column width */
    tag_t *column                       /* <O> New column */
);

/*********************************************************************************
 *
 * Add a row to a tabular note
 *
 * Return :
 *           Return code :
 *           = 0 : successful
 *           > 0 : failing error number
 *           < 0 : failing error number
 *
 * Environment : Internal and External
 *
 * See also:
 *
 * History:
 *
 ********************************************************************************/

extern UFUNEXPORT int UF_TABNOT_add_row(
    tag_t tabular_note,                 /* <I> Tabular note */
    tag_t row,                          /* <I> Row */
    int index                           /* <I> Index of position for row or
                                           UF_TABNOT_APPEND to append to the end */
);

/*********************************************************************************
 *
 * Add a column to a tabular note
 *
 * Return :
 *           Return code :
 *           = 0 : successful
 *           > 0 : failing error number
 *           < 0 : failing error number
 *
 * Environment : Internal and External
 *
 * See also:
 *
 * History:
 *
 ********************************************************************************/

extern UFUNEXPORT int UF_TABNOT_add_column(
    tag_t tabular_note,                 /* <I> Tabular note */
    tag_t column,                       /* <I> Column */
    int index                           /* <I> Index of position for column or
                                           UF_TABNOT_APPEND to append to the end */
);

/*********************************************************************************
 *
 * Add a header row to a tabular note
 *
 * Return :
 *           Return code :
 *           = 0 : successful
 *           > 0 : failing error number
 *           < 0 : failing error number
 *
 * Environment : Internal and External
 *
 * See also:
 *
 * History:
 *
 ********************************************************************************/

extern UFUNEXPORT int UF_TABNOT_add_header_row(
    tag_t tabular_note,                 /* <I> Tabular note */
    tag_t row,                          /* <I> Row */
    int index                           /* <I> Index of position for row */
);

/*********************************************************************************
 *
 * Remove a row from a tabular note.  Note that this does not delete the row.  To
 * delete the row, use UF_OBJ_delete_object.
 *
 * Return :
 *           Return code :
 *           = 0 : successful
 *           > 0 : failing error number
 *           < 0 : failing error number
 *
 * Environment : Internal and External
 *
 * See also:
 *
 * History:
 *
*********************************************************************************/

extern UFUNEXPORT int UF_TABNOT_remove_row(
    tag_t row                           /* <I> Row to remove */
);

/*********************************************************************************
 *
 * Remove a column from a tabular note.  Note that this does not delete the column.  To
 * delete the column, use UF_OBJ_delete_object.
 *
 * Return :
 *           Return code :
 *           = 0 : successful
 *           > 0 : failing error number
 *           < 0 : failing error number
 *
 * Environment : Internal and External
 *
 * See also:
 *
 * History:
 *
*********************************************************************************/

extern UFUNEXPORT int UF_TABNOT_remove_column(
    tag_t column                        /* <I> Column to remove */
);

/*********************************************************************************
 *
 * Get the number of rows in a tabular note
 *
 * Return :
 *           Return code :
 *           = 0 : successful
 *           > 0 : failing error number
 *           < 0 : failing error number
 *
 * Environment : Internal and External
 *
 * See also:
 *
 * History:
 *
 ********************************************************************************/

extern UFUNEXPORT int UF_TABNOT_ask_nm_rows(
    tag_t tabnote,                      /* <I> Tabular note */
    int *nm_rows                        /* <O> Number of rows */
);


/*********************************************************************************
 *
 * Get the number of rows in a section
 *
 * Return :
 *           Return code :
 *           = 0 : successful
 *           > 0 : failing error number
 *           < 0 : failing error number
 *
 * Environment : Internal and External
 *
 * See also:
 *
 * History:
 *
 ********************************************************************************/

extern UFUNEXPORT int UF_TABNOT_ask_nm_rows_in_section(
    tag_t section,                      /* <I> Tabular note section */
    int *nm_rows                        /* <O> Number of rows */
);

/*********************************************************************************
 *
 * Get the number of columns in a tabular note
 *
 * Return :
 *           Return code :
 *           = 0 : successful
 *           > 0 : failing error number
 *           < 0 : failing error number
 *
 * Environment : Internal and External
 *
 * See also:
 *
 * History:
 *
 ********************************************************************************/

extern UFUNEXPORT int UF_TABNOT_ask_nm_columns(
    tag_t tabnote,                      /* <I> Tabular note */
    int *nm_columns                     /* <O> Number of columns */
);

/*********************************************************************************
 *
 * Get the number of sections in a tabular note
 *
 * Return :
 *           Return code :
 *           = 0 : successful
 *           > 0 : failing error number
 *           < 0 : failing error number
 *
 * Environment : Internal and External
 *
 * See also:
 *
 * History:
 *
 ********************************************************************************/

extern UFUNEXPORT int UF_TABNOT_ask_nm_sections(
    tag_t tabnote,                      /* <I> Tabular note */
    int *nm_sections                    /* <O> Number of sections */
);

/*********************************************************************************
 *
 * Get the number of header rows in a tabular note
 *
 * Return :
 *           Return code :
 *           = 0 : successful
 *           > 0 : failing error number
 *           < 0 : failing error number
 *
 * Environment : Internal and External
 *
 * See also:
 *
 * History:
 *
 ********************************************************************************/

extern UFUNEXPORT int UF_TABNOT_ask_nm_header_rows(
    tag_t tabnote,                      /* <I> Tabular note */
    int *nm_header_rows                 /* <O> Number of header rows */
);

/*********************************************************************************
 *
 * Get the nth row in a tabular note
 *
 * Return :
 *           Return code :
 *           = 0 : successful
 *           > 0 : failing error number
 *           < 0 : failing error number
 *
 * Environment : Internal and External
 *
 * See also:
 *
 * History:
 *
 ********************************************************************************/

extern UFUNEXPORT int UF_TABNOT_ask_nth_row(
    tag_t tabnote,                      /* <I> Tabular note */
    int index,                          /* <I> Index of row to retrieve */
    tag_t *row                          /* <O> Row */
);

/*********************************************************************************
 *
 * Get the nth row in a section
 *
 * Return :
 *           Return code :
 *           = 0 : successful
 *           > 0 : failing error number
 *           < 0 : failing error number
 *
 * Environment : Internal and External
 *
 * See also:
 *
 * History:
 *
 ********************************************************************************/

extern UFUNEXPORT int UF_TABNOT_ask_nth_row_in_section(
    tag_t section,                      /* <I> Tabular note section */
    int index,                          /* <I> Index of row to retrieve */
    tag_t *row                          /* <O> Row */
);

/*********************************************************************************
 *
 * Get the nth column in a tabular note
 *
 * Return :
 *           Return code :
 *           = 0 : successful
 *           > 0 : failing error number
 *           < 0 : failing error number
 *
 * Environment : Internal and External
 *
 * See also:
 *
 * History:
 *
 ********************************************************************************/

extern UFUNEXPORT int UF_TABNOT_ask_nth_column(
    tag_t tabnote,                      /* <I> Tabular note */
    int index,                          /* <I> Index of column to retrieve */
    tag_t *column                       /* <O> Column */
);

/*********************************************************************************
 *
 * Get the nth section in a tabular note
 *
 * Return :
 *           Return code :
 *           = 0 : successful
 *           > 0 : failing error number
 *           < 0 : failing error number
 *
 * Environment : Internal and External
 *
 * See also:
 *
 * History:
 *
 ********************************************************************************/

extern UFUNEXPORT int UF_TABNOT_ask_nth_section(
    tag_t tabnote,                      /* <I> Tabular note */
    int index,                          /* <I> Index of section to retrieve */
    tag_t *section                      /* <O> Section */
);

/*********************************************************************************
 *
 * Get a row at a position relative to the given row
 *
 * Return :
 *           Return code :
 *           = 0 : successful
 *           > 0 : failing error number
 *           < 0 : failing error number
 *
 * Environment : Internal and External
 *
 * See also:
 *
 * History:
 *
 ********************************************************************************/

extern UFUNEXPORT int UF_TABNOT_ask_relative_row(
    tag_t row,                          /* <I> Row */
    int position,                       /* <I> Relative position.  If position is
                                           less than zero, the row retrieved will be
                                           above the given row; if position is
                                           greater than zero, the row retrieved
                                           will be below the given row. */
    tag_t *relative_row                 /* <O> Relative row */
);

/*********************************************************************************
 *
 * Get a column at a position relative to the given column
 *
 * Return :
 *           Return code :
 *           = 0 : successful
 *           > 0 : failing error number
 *           < 0 : failing error number
 *
 * Environment : Internal and External
 *
 * See also:
 *
 * History:
 *
 ********************************************************************************/

extern UFUNEXPORT int UF_TABNOT_ask_relative_column(
    tag_t column,                       /* <I> Column */
    int position,                       /* <I> Relative position.  If position is
                                           less than zero, the column retrieved will
                                           be to the left of given column; if position
                                           is greater than zero, the column retrieved
                                           will be to the right of the given column. */
    tag_t *relative_column              /* <O> Relative column */
);

/*********************************************************************************
 *
 * Get a cell at the intersection of a row and column
 *
 * Return :
 *           Return code :
 *           = 0 : successful
 *           > 0 : failing error number
 *           < 0 : failing error number
 *
 * Environment : Internal and External
 *
 * See also:
 *
 * History:
 *
 ********************************************************************************/

extern UFUNEXPORT int UF_TABNOT_ask_cell_at_row_col(
    tag_t row,                          /* <I> Row */
    tag_t column,                       /* <I> Column */
    tag_t *cell                         /* <O> Cell */
);

/*********************************************************************************
 *
 * Get the tabular note of a section
 *
 * Return :
 *           Return code :
 *           = 0 : successful
 *           > 0 : failing error number
 *           < 0 : failing error number
 *
 * Environment : Internal and External
 *
 * See also:
 *
 * History:
 *
 ********************************************************************************/

extern UFUNEXPORT int UF_TABNOT_ask_tabular_note_of_section(
    tag_t section,                      /* <I> Section */
    tag_t *tabular_note                 /* <O> Tabular note */
);


/*********************************************************************************
 *
 * Get the section of a row
 *
 * Return :
 *           Return code :
 *           = 0 : successful
 *           > 0 : failing error number
 *           < 0 : failing error number
 *
 * Environment : Internal and External
 *
 * See also:
 *
 * History:
 *
 ********************************************************************************/

extern UFUNEXPORT int UF_TABNOT_ask_section_of_row(
    tag_t row,                          /* <I> Row */
    tag_t *section                      /* <O> Section */
);

/*********************************************************************************
 *
 * Get the tabular note of a column
 *
 * Return :
 *           Return code :
 *           = 0 : successful
 *           > 0 : failing error number
 *           < 0 : failing error number
 *
 * Environment : Internal and External
 *
 * See also:
 *
 * History:
 *
 ********************************************************************************/

extern UFUNEXPORT int UF_TABNOT_ask_tabular_note_of_column(
    tag_t column,                       /* <I> Column */
    tag_t *tabular_note                 /* <O> Tabular note */
);

/*********************************************************************************
 *
 * Get the row of a cell
 *
 * Return :
 *           Return code :
 *           = 0 : successful
 *           > 0 : failing error number
 *           < 0 : failing error number
 *
 * Environment : Internal and External
 *
 * See also:
 *
 * History:
 *
 ********************************************************************************/

extern UFUNEXPORT int UF_TABNOT_ask_row_of_cell(
    tag_t cell ,                        /* <I> Cell */
    tag_t *row                          /* <O> Row */
);

/*********************************************************************************
 *
 * Get the column of a cell
 *
 * Return :
 *           Return code :
 *           = 0 : successful
 *           > 0 : failing error number
 *           < 0 : failing error number
 *
 * Environment : Internal and External
 *
 * See also:
 *
 * History:
 *
 ********************************************************************************/

extern UFUNEXPORT int UF_TABNOT_ask_column_of_cell(
    tag_t cell ,                        /* <I> Cell */
    tag_t *column                       /* <O> Column */
);

/*********************************************************************************
 *
 * Get the height of a row
 *
 * Return :
 *           Return code :
 *           = 0 : successful
 *           > 0 : failing error number
 *           < 0 : failing error number
 *
 * Environment : Internal and External
 *
 * See also:
 *
 * History:
 *
 ********************************************************************************/

extern UFUNEXPORT int UF_TABNOT_ask_row_height(
    tag_t row,                          /* <I> Row */
    double *height                      /* <O> Height */
);

/*********************************************************************************
 *
 * Set the height of a row
 * Note: Fit methods auto size row and auto size text must be disabled
 * in order for the row height to be reflected on the row.
 * Return :
 *           Return code :
 *           = 0 : successful
 *           > 0 : failing error number
 *           < 0 : failing error number
 *
 * Environment : Internal and External
 *
 * See also:
 *
 * History:
 *
 ********************************************************************************/

extern UFUNEXPORT int UF_TABNOT_set_row_height(
    tag_t row,                          /* <I> Row */
    double height                       /* <I> Height */
);

/*********************************************************************************
 *
 * Get the color/font/width settings for the line at the row head
 *
 * Return :
 *           Return code :
 *           = 0 : successful
 *           > 0 : failing error number
 *           < 0 : failing error number
 *
 * Environment : Internal and External
 *
 * See also:
 *
 * History:
 *
 ********************************************************************************/

extern UFUNEXPORT int UF_TABNOT_ask_row_head_cfw(
    tag_t row,                          /* <I> Row */
    int cfw[3]                          /* <O> Color/font/width of row head */
);

/*********************************************************************************
 *
 * Set the color/font/width settings for the line at the row head
 *
 * Return :
 *           Return code :
 *           = 0 : successful
 *           > 0 : failing error number
 *           < 0 : failing error number
 *
 * Environment : Internal and External
 *
 * See also:
 *
 * History:
 *
 ********************************************************************************/

extern UFUNEXPORT int UF_TABNOT_set_row_head_cfw(
    tag_t row,                          /* <I> Row */
    int cfw[3]                          /* <I> Color/font/width of row head */
);

/*********************************************************************************
 *
 * Get the width of a column
 *
 * Return :
 *           Return code :
 *           = 0 : successful
 *           > 0 : failing error number
 *           < 0 : failing error number
 *
 * Environment : Internal and External
 *
 * See also:
 *
 * History:
 *
 ********************************************************************************/

extern UFUNEXPORT int UF_TABNOT_ask_column_width(
    tag_t column,                       /* <I> Column */
    double *width                       /* <O> Width */
);

/*********************************************************************************
 *
 * Set the width of a column
 *
 * Return :
 *           Return code :
 *           = 0 : successful
 *           > 0 : failing error number
 *           < 0 : failing error number
 *
 * Environment : Internal and External
 *
 * See also:
 *
 * History:
 *
 ********************************************************************************/

extern UFUNEXPORT int UF_TABNOT_set_column_width(
    tag_t column,                       /* <I> Column */
    double width                        /* <I> Width */
);

/*********************************************************************************
 *
 * Get the color/font/width settings for the line at the column head
 *
 * Return :
 *           Return code :
 *           = 0 : successful
 *           > 0 : failing error number
 *           < 0 : failing error number
 *
 * Environment : Internal and External
 *
 * See also:
 *
 * History:
 *
 ********************************************************************************/

extern UFUNEXPORT int UF_TABNOT_ask_column_head_cfw(
    tag_t column,                       /* <I> Column */
    tag_t section,                      /* <I> Section */
    int cfw[3]                          /* <O> Color/font/width of column head */
);

/*********************************************************************************
 *
 * Set the color/font/width settings for the line at the column head
 *
 * Return :
 *           Return code :
 *           = 0 : successful
 *           > 0 : failing error number
 *           < 0 : failing error number
 *
 * Environment : Internal and External
 *
 * See also:
 *
 * History:
 *
 ********************************************************************************/

extern UFUNEXPORT int UF_TABNOT_set_column_head_cfw(
    tag_t column,                       /* <I> Column */
    tag_t section,                      /* <I> Section */
    int cfw[3]                          /* <I> Color/font/width of column head */
);

/*********************************************************************************
 *
 * Get the defining text of a cell
 *
 * Return :
 *           Return code :
 *           = 0 : successful
 *           > 0 : failing error number
 *           < 0 : failing error number
 *
 * Environment : Internal and External
 *
 * See also:
 *
 * History:
 *
 ********************************************************************************/

extern UFUNEXPORT int UF_TABNOT_ask_cell_text(
    tag_t cell,                         /* <I> Cell */
    char **cell_text                    /* <OF> Cell text */
);

/*********************************************************************************
 *
 * Set the defining text of a cell
 *
 * Return :
 *           Return code :
 *           = 0 : successful
 *           > 0 : failing error number
 *           < 0 : failing error number
 *
 * Environment : Internal and External
 *
 * See also:
 *
 * History:
 *
 ********************************************************************************/

extern UFUNEXPORT int UF_TABNOT_set_cell_text(
    tag_t cell,                         /* <I> Cell */
    const char *cell_text               /* <I> Cell text */
);

/*********************************************************************************
 *
 * Get the evaluated text from a tabular note cell
 *
 * Return :
 *           Return code :
 *           = 0 : successful
 *           > 0 : failing error number
 *           < 0 : failing error number
 *
 * Environment : Internal and External
 *
 * See also:
 *
 * History:
 *
 ********************************************************************************/

extern UFUNEXPORT int UF_TABNOT_ask_evaluated_cell_text(
    tag_t cell,                         /* <I> Tabular note cell */
    char **evaluated_text               /* <OF> Evaluated cell text */
);

/*********************************************************************************
 *
 * Get the cell preferences of a cell
 *
 * Return :
 *           Return code :
 *           = 0 : successful
 *           > 0 : failing error number
 *           < 0 : failing error number
 *
 * Environment : Internal and External
 *
 * See also:
 *
 * History:
 *
 ********************************************************************************/

extern UFUNEXPORT int UF_TABNOT_ask_cell_prefs(
    tag_t cell,                         /* <I> Cell */
    UF_TABNOT_cell_prefs_p_t cell_prefs /* <O> Cell preferences */
);

/*********************************************************************************
 *
 * Set the cell preferences of a cell
 *
 * Return :
 *           Return code :
 *           = 0 : successful
 *           > 0 : failing error number
 *           < 0 : failing error number
 *
 * Environment : Internal and External
 *
 * See also:
 *
 * History:
 *
 ********************************************************************************/

extern UFUNEXPORT int UF_TABNOT_set_cell_prefs(
    tag_t cell,                         /* <I> Cell */
    UF_TABNOT_cell_prefs_p_t cell_prefs /* <I> Cell preferences */
);

/*********************************************************************************
 *
 * Get the position of text in a cell relative to the upper left
 * corner of the tabular note section in the space of the section
 *
 * Return :
 *           Return code :
 *           = 0 : successful
 *           > 0 : failing error number
 *           < 0 : failing error number
 *
 * Environment : Internal and External
 *
 * See also:
 *
 * History:
 *
 ********************************************************************************/

UFUNEXPORT int UF_TABNOT_ask_cell_text_position(
    tag_t cell,                         /* <I> Cell */
    double text_position[2]             /* <O> Cell text position */
);

/*********************************************************************************
 *
 * Merge tabular note cells
 *
 * Return :
 *           Return code :
 *           = 0 : successful
 *           > 0 : failing error number
 *           < 0 : failing error number
 *
 * Environment : Internal and External
 *
 * See also:
 *
 * History:
 *
 ********************************************************************************/

extern UFUNEXPORT int UF_TABNOT_merge_cells(
    tag_t start_cell,                   /* <I> Cell at start of range to merge */
    tag_t end_cell                      /* <I> Cell at end of range to merge */
);

/*********************************************************************************
 *
 * Unmerge tabular note cells
 *
 * Return :
 *           Return code :
 *           = 0 : successful
 *           > 0 : failing error number
 *           < 0 : failing error number
 *
 * Environment : Internal and External
 *
 * See also:
 *
 * History:
 *
 ********************************************************************************/

extern UFUNEXPORT int UF_TABNOT_unmerge_cells(
    tag_t cell                          /* <I> Merged cell */
);

/*********************************************************************************
 *
 * Get information about merged cells.  If the specified cell is a merge
 * parent (meaning it is the cell in the range of merged cells that contains
 * the text), returns the start and end rows and columns of the range.
 *
 * Return :
 *           Return code :
 *           = 0 : successful
 *           > 0 : failing error number
 *           < 0 : failing error number
 *
 * Environment : Internal and External
 *
 * See also:
 *
 * History:
 *
 ********************************************************************************/

extern UFUNEXPORT int UF_TABNOT_ask_merge_info(
    tag_t cell,          /* <I> Cell */
    tag_t *start_row,    /* <O> Start row or NULL_TAG if cell is not merged */
    tag_t *start_column, /* <O> Start column or NULL_TAG if cell is not merged */
    tag_t *end_row,      /* <O> End row or NULL_TAG if cell is not merged */
    tag_t *end_column    /* <O> End column or NULL_TAG if cell is not merged */
);

/*********************************************************************************
 *
 * Get the section preferences of a tabular note section
 *
 * Return :
 *           Return code :
 *           = 0 : successful
 *           > 0 : failing error number
 *           < 0 : failing error number
 *
 * Environment : Internal and External
 *
 * See also:
 *
 * History:
 *
 ********************************************************************************/

extern UFUNEXPORT int UF_TABNOT_ask_section_prefs(
    tag_t section,                      /* <I> Tabular note section */
    UF_TABNOT_section_prefs_p_t section_prefs /* <O> Section preferences */
);

/*********************************************************************************
 *
 * Set the section preferences of a tabular note section
 *
 * Return :
 *           Return code :
 *           = 0 : successful
 *           > 0 : failing error number
 *           < 0 : failing error number
 *
 * Environment : Internal and External
 *
 * See also:
 *
 * History:
 *
 ********************************************************************************/

extern UFUNEXPORT int UF_TABNOT_set_section_prefs(
    tag_t section,                      /* <I> Tabular note section */
    UF_TABNOT_section_prefs_p_t section_prefs /* <I> Section preferences */
);

/*********************************************************************************
 *
 * Import a spreadsheet cell into a tabular note cell.
 *
 * Note: This method will change the tag of a tabular note cell object in which
 * spreadsheet data is imported. The new tag of the tabular note cell can be
 * queried using the method UF_TABNOT_ask_cell_at_row_col()
 *
 * Return :
 *           Return code :
 *           = 0 : successful
 *           > 0 : failing error number
 *           < 0 : failing error number
 *
 * Environment : Internal and External
 *
 * See also:
 *
 * History:
 *
 ********************************************************************************/

extern UFUNEXPORT int UF_TABNOT_import_spreadsheet_cell(
    tag_t spreadsheet,                  /* <I> Tag of NX spreadsheet object */
    int sheet_number,                   /* <I> Sheet number in spreadsheet */
    int row_number,                     /* <I> Row number in spreadsheet */
    int column_number,                  /* <I> Column number in spreadsheet */
    tag_t cell                          /* <I> Cell in a tabular to import into */
);

/*********************************************************************************
 *
 * Retrieves the nth header row
 *
 * Return :
 *           Return code :
 *           = 0 : successful
 *           > 0 : failing error number
 *           < 0 : failing error number
 *
 * Environment : Internal and External
 *
 * See also:
 *
 * History:
 *
 ********************************************************************************/
extern UFUNEXPORT int UF_TABNOT_ask_nth_header_row(
    tag_t tabnote,    /* <I> The tabular note which has the row */
    int index,        /* <I> The index of the row */
    tag_t *row        /* <O> The nth row */
);

/*********************************************************************************
 *
 * Retrieves the default section preferences
 *
 * Return :
 *           Return code :
 *           = 0 : successful
 *           > 0 : failing error number
 *           < 0 : failing error number
 *
 * Environment : Internal and External
 *
 * See also:
 *
 * History:
 *
 ********************************************************************************/
extern UFUNEXPORT int UF_TABNOT_ask_default_section_prefs(
    UF_TABNOT_section_prefs_p_t section_prefs    /* <O> The default section preferences */
);

/*********************************************************************************
 *
 * Sets the default section preferences
 *
 * Return :
 *           Return code :
 *           = 0 : successful
 *           > 0 : failing error number
 *           < 0 : failing error number
 *
 * Environment : Internal and External
 *
 * See also:
 *
 * History:
 *
 ********************************************************************************/
extern UFUNEXPORT int UF_TABNOT_set_default_section_prefs(
    UF_TABNOT_section_prefs_p_t section_prefs   /* <I> The section preferences */
);

/*********************************************************************************
 *
 * Retrieves the default cell preferences
 *
 * Return :
 *           Return code :
 *           = 0 : successful
 *           > 0 : failing error number
 *           < 0 : failing error number
 *
 * Environment : Internal and External
 *
 * See also:
 *
 * History:
 *
 ********************************************************************************/
extern UFUNEXPORT int UF_TABNOT_ask_default_cell_prefs(
    UF_TABNOT_cell_prefs_p_t cell_prefs    /* <O> The cell preferences */
);

/*********************************************************************************
 *
 * Sets the default cell preferences
 *
 * Return :
 *           Return code :
 *           = 0 : successful
 *           > 0 : failing error number
 *           < 0 : failing error number
 *
 * Environment : Internal and External
 *
 * See also:
 *
 * History:
 *
 ********************************************************************************/
extern UFUNEXPORT int UF_TABNOT_set_default_cell_prefs(
    UF_TABNOT_cell_prefs_p_t cell_prefs    /* <I> The cell preferences */
);

/*********************************************************************************
 *
 * Enable or disable the automatic update of tabular notes
 *
 * Return :
 *           Return code :
 *           = 0 : successful
 *           > 0 : failing error number
 *           < 0 : failing error number
 *
 * Environment : Internal and External
 *
 * See also:
 *
 * History:
 *
 ********************************************************************************/
extern UFUNEXPORT int UF_TABNOT_enable_automatic_update(
    logical allow_automatic_update     /* <I> Allow automatic update? */
);

/*********************************************************************************
 *
 * Force a tabular note to update
 *
 * Return :
 *           Return code :
 *           = 0 : successful
 *           > 0 : failing error number
 *           < 0 : failing error number
 *
 * Environment : Internal and External
 *
 * See also:
 *
 * History:
 *
 ********************************************************************************/
extern UFUNEXPORT int UF_TABNOT_update(
    tag_t tabular_note       /* <I> The tabular note to update */
);

/*********************************************************************************
 *
 * Convert a tabular note that references a spreadsheet to
 * one for which every cell is an ordinary cell.
 *
 * Return :
 *           Return code :
 *           = 0 : successful
 *           > 0 : failing error number
 *           < 0 : failing error number
 *
 * Environment : Internal and External
 *
 * See also:
 *
 * History:
 *
 ********************************************************************************/
extern UFUNEXPORT int UF_TABNOT_convert_to_non_spreadsheet_tabnote(
    tag_t tabular_note      /* <I> The tabular note */
);

/*********************************************************************************
 *
 * Find and fix out-of-synch spreadsheet linked tabular notes from input part
 *
 * Note: The out-of-synch tabular note will be fixed by considering tabular note data as master.
 * 
 * Input :
 *     partTag         : Part tag 
 *     fixTabnotes     : Flag to fix out-of-synch tabular notes,
 *                       when false, then this method will only find out-of-synch spreadsheet linked tabular notes from input part.
 *                       when true, then this method will find and fix out-of-synch spreadsheet linked tabular notes from input part.
 *
 * Output :
 *      numTabnotes    : Number of out-of-synch tabular notes.
 *      tabnotes       : List of out-of-synch tabular notes. Use UF_free to free this memory.
 *
 * Return :
 *           Return code :
 *           = 0 : successful
 *           > 0 : failing error number
 *           < 0 : failing error number
 *
 * Environment : Internal and External
 *
 * See also:
 *
 * History: Released in NX11.0
 *
 ********************************************************************************/
extern UFUNEXPORT int UF_TABNOT_FindAndFixOutOfSynchSpreadsheetTabnotes
(
    tag_t partTag,                   /* <I> Part Tag */
    logical fixTabnotes,             /* <I> flag to fix out-of-synch tabular notes */
    int *numTabnotes,                /* <O> number of out-of-synch tabular notes */
    tag_t **tabnotes                 /* <OF> list of out-of-synch tabular notes. Use UF_free to free this memory. */
);

/*END */

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif /* UF_TABNOT_H_INCLUDED */
