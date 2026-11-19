/*******************************************************************************

           Copyright (c) 1996-2003 Unigraphics Solutions Inc.
                        Unpublished - All rights reserved

********************************************************************************



File description:

These subroutines provide access to Clearance Analysis data within NX.
All Clearance Analysis data is maintained in an object called a Clearance
Analysis data set. The data set consists of two types of information, setup
data and analysis results. The setup data includes items such as the list of
objects available for analysis, the clearance zones for those objects, rules
used to exclude some object pairs from analysis, and analysis preferences. The
results are a list of interferences. The routines in this section allow you to:
      . manipulate clearance analysis data sets.
      . establish the lists of objects to be subject to clearance analysis.
      . define clearance zones around objects. These clearance
        zones define a volume in which no other objects can penetrate.
      . defines rules that exclude certain pairs from analysis.
      . create and query analysis results.
      . specify clearance analysis preferences.

Refer to the Assemblies User Manual for details on Clearance Analysis.

Note in routines where a user is expected to provide a valid pointer,
UF_CLEAR_err_null_pointer will be returned when a null pointer is detected.


*******************************************************************************/
#ifndef UF_CLEAR_H_INCLUDED
#define UF_CLEAR_H_INCLUDED

/***************************************************************************

  ***************************************************************************/

/*******************************************************************************
                                 ** Includes **
 ******************************************************************************/

#define ERROR_CLEAR_base       1185000
#include <uf_defs.h>                    /* For MAX_LINE_SIZE, TRUE/FALSE, etc.*/
#include <libufun_exports.h>

#ifdef __cplusplus
extern "C" {
#endif


/*******************************************************************************
                                  ** Macros **
 ******************************************************************************/

#define UF_CLEAR_BIT(n)                 ( 1 << ((n) - 1) )


/*******************************************************************************
                                ** Constants **
 ******************************************************************************/

/*******************************************************************************
                                  Error codes

The following module specific failure codes can be returned by the
UF_CLEAR routines.

*******************************************************************************/
#define UF_CLEAR_ERROR_BASE             ERROR_CLEAR_base

/* An attempt has been made to create a data set
      with the name of an existing data set. */
#define UF_CLEAR_err_name_exists        ( UF_CLEAR_ERROR_BASE + 1 )
/* The named data set cannot be found. */
#define UF_CLEAR_err_cant_find_dataset  ( UF_CLEAR_ERROR_BASE + 2 )
#define UF_CLEAR_err_not_clranl_obj     ( UF_CLEAR_ERROR_BASE + 3 )
/* An invalid object list number has been supplied.
   The list number must be 1 or 2. */
#define UF_CLEAR_err_bad_list_num       ( UF_CLEAR_ERROR_BASE + 4 )
#define UF_CLEAR_err_no_work_part       ( UF_CLEAR_ERROR_BASE + 5 )
#define UF_CLEAR_err_cant_find_point    ( UF_CLEAR_ERROR_BASE + 6 )
/* The tag (or tags) specified does not define a valid interference. */
#define UF_CLEAR_err_bad_interf         ( UF_CLEAR_ERROR_BASE + 7 )
/* The two object tags do not define a valid pair. */
#define UF_CLEAR_err_bad_pair           ( UF_CLEAR_ERROR_BASE + 8 )
#define UF_CLEAR_err_bad_num_zones      ( UF_CLEAR_ERROR_BASE + 9 )
/* The tag specified was not a valid part. */
#define UF_CLEAR_err_bad_part           ( UF_CLEAR_ERROR_BASE + 10 )
#define UF_CLEAR_err_sheet_intersect    ( UF_CLEAR_ERROR_BASE + 11 )
/* An error occurred during analysis. */
#define UF_CLEAR_err_analysis_error     ( UF_CLEAR_ERROR_BASE + 12 )
/* A faceting error occurred during analysis. */
#define UF_CLEAR_err_facet_err          ( UF_CLEAR_ERROR_BASE + 13 )
#define UF_CLEAR_err_obj_not_avail      ( UF_CLEAR_ERROR_BASE + 14 )
/* The tag specified was not a valid clearance analysis data set. */
#define UF_CLEAR_err_bad_dataset        ( UF_CLEAR_ERROR_BASE + 15 )
/* An invalid copy mode parameter was supplied to a routine. */
#define UF_CLEAR_err_bad_copy_mode      ( UF_CLEAR_ERROR_BASE + 16 )
/* The text supplied is invalid (either too long or zero length). */
#define UF_CLEAR_err_bad_string         ( UF_CLEAR_ERROR_BASE + 17 )
/* A null pointer has been passed to a routine. */
#define UF_CLEAR_err_null_pointer       ( UF_CLEAR_ERROR_BASE + 18 )
/* The object list type parameter is nvalid. */
#define UF_CLEAR_err_bad_list_type      ( UF_CLEAR_ERROR_BASE + 19 )
/* The analysis mode supplied to a routine is invalid. */
#define UF_CLEAR_err_bad_analysis_mode  ( UF_CLEAR_ERROR_BASE + 20 )
/* The tag specified does not refer to a valid expression. */
#define UF_CLEAR_err_bad_expression     ( UF_CLEAR_ERROR_BASE + 21 )
/* The data in an object list is invalid. */
#define UF_CLEAR_err_bad_list_data      ( UF_CLEAR_ERROR_BASE + 22 )
/* The exclusion rule supplied to a routine is invalid. */
#define UF_CLEAR_err_bad_exclude_rules  ( UF_CLEAR_ERROR_BASE + 23 )
/* The message filter supplied to a routine is invalid. */
#define UF_CLEAR_err_bad_msg_filter     ( UF_CLEAR_ERROR_BASE + 24 )
/* The layer number supplied to a routine is invalid. */
#define UF_CLEAR_err_bad_layer          ( UF_CLEAR_ERROR_BASE + 25 )
/* The color index supplied to a routine is invalid. */
#define UF_CLEAR_err_bad_color          ( UF_CLEAR_ERROR_BASE + 26 )
/* The data set in question does not contain any analysis results. */
#define UF_CLEAR_err_no_results         ( UF_CLEAR_ERROR_BASE + 27 )

/*
  These constants are used as masks for the interactive_msg_filter field.
  They are also used in the UF_CLEAR_interfere structure for the type field.
*/
#define UF_CLEAR_NO_INTERFERENCE                0
#define UF_CLEAR_SOFT_INTERFERENCE              UF_CLEAR_BIT(1)
#define UF_CLEAR_TOUCH_INTERFERENCE             UF_CLEAR_BIT(2)
#define UF_CLEAR_HARD_INTERFERENCE              UF_CLEAR_BIT(4)
#define UF_CLEAR_CONT_1_IN_2_INTERFERENCE       UF_CLEAR_BIT(5)
#define UF_CLEAR_CONT_2_IN_1_INTERFERENCE       UF_CLEAR_BIT(6)
#define UF_CLEAR_NEW_INTERFERENCE               UF_CLEAR_BIT(8)

/*
  These constants are used to define the analysis mode.  Note do not
  use the first four (UF_CLEAR_SOLID_BASED, UF_CLEAR_FACET_BASED,
  UF_CLEAR_EXHAUSTIVE_FACET_MODE, or UF_CLEAR_BEST_AVAILABLE_BASED).
  They are used to define the next five (described below)
  which are to be used by users.
*/
#define UF_CLEAR_SOLID_BASED            UF_CLEAR_BIT(1)
#define UF_CLEAR_FACET_BASED            UF_CLEAR_BIT(2)
#define UF_CLEAR_EXHAUSTIVE_FACET_MODE  UF_CLEAR_BIT(3)
#define UF_CLEAR_BEST_AVAILABLE_BASED   UF_CLEAR_BIT(4)

/*
  UF_CLEAR_QUICK_FACET is the fastest clearance analysis mode.  It uses
      existing facetted representations where possible, and generates
      temporary facetted representations of solid bodies that don?t have
      a facetted representation loaded.  It maps into the interactive mode
      Facet Based.
*/
#define UF_CLEAR_QUICK_FACET            UF_CLEAR_FACET_BASED
/*
  UF_CLEAR_FULL_FACET use of this mode is generally discouraged.  It is a
      legacy analysis mode that had a special meaning in the pre-V18
      clearance analysis application which has been largely lost in the
      re-implemented functionality.  In the current system, it will perform
      a slightly more exhaustive analysis than the quick facet mode (and
      therefore will be a little more resource intensive), but in most if
      not all cases will yield the same results as UF_CLEAR_QUICK_FACET.
      It also maps into the interactive mode Facet Based.
*/
#define UF_CLEAR_FULL_FACET             ( UF_CLEAR_FACET_BASED | \
                                          UF_CLEAR_EXHAUSTIVE_FACET_MODE )
/*
  UF_CLEAR_FACET_SOLID will perform analysis based on loaded solids where
      possible, but will fall back on analyzing facetted representations
      where they are loaded instead of solids.  Solid analysis is slower,
      so depending on the mix of facets and solids that are loaded in the
      session, the performance of UF_CLEAR_FACET_SOLID will fall somewhere
      between the performance of UF_CLEAR_QUICK_FACET and UF_CLEAR_SOLID.
      This mode maps into the interactive mode Use Solids Where Available.
*/
#define UF_CLEAR_FACET_SOLID            ( UF_CLEAR_FACET_BASED | \
                                          UF_CLEAR_SOLID_BASED )
/*
  UF_CLEAR_SOLID is the most accurate and slowest analysis mode.  It does
      analysis based on solid bodies exclusively.  In cases where solid
      data is not loaded, demand loading will occur so that the analysis
      can be performed.  This maps to the interactive mode Use Solids.
*/
#define UF_CLEAR_SOLID                  UF_CLEAR_SOLID_BASED
#define UF_CLEAR_BEST_AVAILABLE         ( UF_CLEAR_FACET_SOLID | \
                                          UF_CLEAR_BEST_AVAILABLE_BASED )

/*
  These constants are used to define the types of object lists.
  A negative value is used for list2 if it is not used.
*/
#define UF_CLEAR_ALL_OBJECTS            1
#define UF_CLEAR_ALL_BUT                2
#define UF_CLEAR_FIXED_LIST             4
#define UF_CLEAR_ALL_VISIBLE_OBJECTS    5
#define UF_CLEAR_LIST2_NOT_USED         ( -1 )

/*
  These constants are used to define the source of a clearance zone.
*/
#define UF_CLEAR_USING_DEFAULT_CZ       0
#define UF_CLEAR_USING_DEFINED_CZ       1
#define UF_CLEAR_USING_OBJ1_CZ          2
#define UF_CLEAR_USING_OBJ2_CZ          3
#define UF_CLEAR_USING_PAIR_CZ          4

/*
  These constants are used to define the exclusion rules.
*/
#define UF_CLEAR_EXCLUDE_MATING_PAIRS   UF_CLEAR_BIT(1)
#define UF_CLEAR_EXCLUDE_WITHIN_COMP    UF_CLEAR_BIT(2)
#define UF_CLEAR_EXCLUDE_WITHIN_GROUP   UF_CLEAR_BIT(3)
#define UF_CLEAR_EXCLUDE_WITHIN_PART    UF_CLEAR_BIT(4)

/*
  These constants specify why a job was aborted.
*/
#define UF_CLEAR_NOT_ABORTED            0
#define UF_CLEAR_ABORTED_BY_USER        1
#define UF_CLEAR_ABORTED_ON_ERROR       2

/*
  These constants specify the reason for inclusion/exclusion.
*/
#define UF_CLEAR_EXCL_NO_REASON         0
#define UF_CLEAR_EXCL_USER_DEF          UF_CLEAR_BIT(1)
#define UF_CLEAR_EXCL_SAME_COMP         UF_CLEAR_BIT(2)
#define UF_CLEAR_EXCL_SAME_GROUP        UF_CLEAR_BIT(3)
#define UF_CLEAR_EXCL_MATED_COMP        UF_CLEAR_BIT(4)
#define UF_CLEAR_EXCL_SAME_PART         UF_CLEAR_BIT(5)

/*
  These constants specify how results should be handled when copying a dataset.
*/
#define UF_CLEAR_COPY_NO_RESULTS        0
#define UF_CLEAR_COPY_RESULTS           1
#define UF_CLEAR_COPY_INTERF_BODIES     2


/**************************
 ** Structures and Types **
 **************************/
/************************************************************************
Contains the summary of the most recent analysis results.
************************************************************************/
struct UF_CLEAR_summary_s {
        int     start_time;             /* The starting time of the last
                                           analysis run (in seconds since
                                           00:00:00 1/1/1970.
                                        */
        int     end_time;               /* The ending time of the last
                                           analysis run (in seconds since
                                           00:00:00 1/1/1970.
                                        */
        int     run_time;               /* the total analysis time (in secs.) */
        int     version;                /* The version of this analysis run.
                                           This is a positive number.
                                        */
        int     analysis_mode;          /* The analysis mode.  One of
                                           UF_CLEAR_QUICK_FACET,
                                           UF_CLEAR_FULL_FACET,
                                           UF_CLEAR_BEST_AVAILABLE,
                                           UF_CLEAR_FACET_SOLID and
                                           UF_CLEAR_SOLID.
                                        */
        int     num_lists;              /* Number of object lists analyzed.
                                           Can be either 1 or 2.
                                        */
        int     n_list1;                /* The number of objects in list 1.   */
        int     n_list2;                /* The number of objects in list 2.   */
        int     n_pairs;                /* The number of pairs built from
                                           the object lists.
                                        */
        int     excluded_pairs;         /* The number of pairs that were
                                           excluded from analysis, either
                                           due to exclusion rules or
                                           explicit pair exclusion.
                                        */
        int     changed_pairs;          /* The number of pairs that had
                                           changed since the previous
                                           clearance analysis.
                                        */
        int     changed_objs;           /* The number of objects that had
                                           changed since the previous
                                           clearance analysis.
                                        */
        int     checked_pairs;          /* The total number of pairs that
                                           underwent analysis.
                                        */
        int     new_n_hard;             /* The total number of new hard
                                           interferences.
                                        */
        int     new_n_soft;             /* The total number of new soft
                                           interferences.
                                        */
        int     new_n_touching;         /* The total number of new touching
                                           interferences.
                                        */
        int     new_n_containment;      /* The total number of new containment
                                           interferences.
                                        */
        int     new_n_all_interf;       /* The total number of new
                                           interferences.
                                        */
        int     n_hard;                 /* The total number of hard
                                           interferences.
                                        */
        int     n_soft;                 /* The total number of soft
                                           interferences.
                                        */
        int     n_touching;             /* The total number of touching
                                           interferences.
                                        */
        int     n_containment;          /* The total number of containment
                                           interferences.
                                        */
        int     n_all_interf;           /* The total number of interferences. */
        int     job_aborted;            /* Indicates if the analysis was
                                           aborted.  Valid values are
                                           UF_CLEAR_NOT_ABORTED,
                                           UF_CLEAR_ABORTED_BY_USER and
                                           UF_CLEAR_ABORTED_ON_ERROR.
                                        */
        int     num_zones;              /* The number of assembly zones used
                                           by the analysis (batch only).
                                        */
};

typedef struct UF_CLEAR_summary_s UF_CLEAR_summary_t, *UF_CLEAR_summary_p_t;

/*************************************************************************
Contains data associated with an interference.
*************************************************************************/
struct UF_CLEAR_interf_data_s {
        int     type;                   /* The type of interference.  One of
                                           UF_CLEAR_SOFT_INTERFERENCE,
                                           UF_CLEAR_TOUCH_INTERFERENCE,
                                           UF_CLEAR_HARD_INTERFERENCE,
                                           UF_CLEAR_CONT_1_IN_2_INTERFERENCE
                                           or UF_CLEAR_CONT_2_IN_1_INTERFERENCE.
                                        */
        logical new_interference;       /* Is this a new interference?        */
        int     n_bodies;               /* The number of interference bodies. */
        tag_t   *interf_bodies;         /* <len:n_bodies> The array of interference body
                                           tags.  This array must be freed
                                           when no longer needed by the user,
                                           provided n_bodies > 0.
                                        */
        double  point1[3];              /* A point on object 1.               */
        double  point2[3];              /* A point on object 2.               */
        char    text[MAX_LINE_SIZE + 1];/* The text associated with this
                                           interference.
                                        */
        int     interf_num;             /* A unique number for the
                                           interference.
                                        */
};

typedef struct UF_CLEAR_interf_data_s UF_CLEAR_interf_data_t,
                                     *UF_CLEAR_interf_data_p_t;

/*************************************************************************
Contains the clearance analysis module preference settings.
*************************************************************************/
struct UF_CLEAR_pref_s {
        int     interactive_msg_filter; /* The mode of the interactive message
                                           filter, composed of one or more of
                                           the following bits:
                                           UF_CLEAR_NO_INTERFERENCE,
                                           UF_CLEAR_SOFT_INTERFERENCE,
                                           UF_CLEAR_TOUCH_INTERFERENCE,
                                           UF_CLEAR_HARD_INTERFERENCE,
                                           UF_CLEAR_CONT_1_IN_2_INTERFERENCE,
                                           UF_CLEAR_CONT_2_IN_1_INTERFERENCE,
                                           and UF_CLEAR_NEW_INTERFERENCE.
                                        */
        logical save_interference;      /* Should interference bodies be
                                           saved?
                                        */
        int     interference_layer;     /* The layer on which to put
                                           interference bodies.
                                        */
        int     interference_color;     /* The color to assign to all
                                           interference bodies.
                                        */
        int     interf_attn_color;      /* The color used in interactive
                                           review to highlight interference
                                           bodies.
                                        */
        int     parent_attn_color;      /* The color used in interactive
                                           review to highlight parent bodies.
                                        */
};

typedef struct UF_CLEAR_pref_s UF_CLEAR_pref_t, *UF_CLEAR_pref_p_t;

/*******************************************************************************
                         ** Function Prototypes **

 ******************************************************************************/

/*******************************************************************************
                        ** Begin dataset routines.
*******************************************************************************/

/*******************************************************************************
*  Gets the name of a clearance analysis dataset.
*  The name must be allocated to at least MAX_LINE_SIZE+1 characters.
*
*  Return:
*        Return code:
*               0 = No error
*           not 0 = Error code, which includes
*                               UF_CLEAR_err_bad_dataset.
*
*  Environment: Internal  and  External
*
*  See Also:
*   UF_CLEAR_ask_dataset_version
*   UF_CLEAR_ask_next_dataset
*   UF_CLEAR_copy_dataset
*   UF_CLEAR_count_datasets
*   UF_CLEAR_create_dataset
*   UF_CLEAR_delete_dataset
*   UF_CLEAR_find_dataset
*   UF_CLEAR_rename_dataset
*  History:
*******************************************************************************/
extern UFUNEXPORT int UF_CLEAR_ask_dataset_name (
tag_t dataset ,/* <I>
               The dataset tag.
               */
char * name  /* <O>
             The name of the dataset. Must be allocated to
             MAX_LINE_SIZE+1 characters.
             */
);

/*******************************************************************************
*
*  Gets the version of a clearance analysis dataset. The version indicates
*  how many times clearance analysis has been run on a data set. If the
*  version is zero, then the analysis has never been run.
*
*  Return:
*        Return code:
*               0 = No error
*           not 0 = Error code, which includes
*                               UF_CLEAR_err_bad_dataset.
*
*
*  Environment: Internal  and  External
*
*  See Also:
*   UF_CLEAR_ask_next_dataset
*   UF_CLEAR_copy_dataset
*   UF_CLEAR_count_datasets
*   UF_CLEAR_create_dataset
*   UF_CLEAR_delete_dataset
*   UF_CLEAR_find_dataset
*   UF_CLEAR_rename_dataset
*  History:
*******************************************************************************/
extern UFUNEXPORT int UF_CLEAR_ask_dataset_version (
        tag_t   dataset,        /* <I> The dataset tag.                       */
        int     *version        /* <O> The version of dataset.                */
);

/*******************************************************************************
*  Cycles all clearance analysis datasets in a part, beginning with NULL_TAG
*  as the the input set.  NULL_TAG will be passed back to signify the end of
*  cycling.
*  Note: The dataset tag may only be used as a parameter to other UF_CLEAR
*        functions.
*  Note: Do not delete a dataset while it is being cycled.
*
*  Return:
*        Return code:
*               0 = No error
*           not 0 = Error code, which includes
*                               UF_CLEAR_err_bad_dataset.
*
*  Environment: Internal  and  External
*  See Also:
*   UF_CLEAR_ask_dataset_version
*   UF_CLEAR_ask_dataset_name
*   UF_CLEAR_copy_dataset
*   UF_CLEAR_count_datasets
*   UF_CLEAR_create_dataset
*   UF_CLEAR_delete_dataset
*   UF_CLEAR_find_dataset
*   UF_CLEAR_rename_dataset
*  History:
*******************************************************************************/
extern UFUNEXPORT int UF_CLEAR_ask_next_dataset (
tag_t part_tag ,/* <I>
                The part in which to find the dataset.
                */
tag_t * dataset  /* <I/O>
                 On input, the current dataset.
                 On output, the next dataset.
                */
 );


/*******************************************************************************
*
*  Makes a copy of a dataset.  You must supply a unique name.  There are three
*  modes in which to copy the dataset: UF_CLEAR_COPY_NO_RESULTS only copies
*  the setup data.  The version of the new dataset is set to zero (meaning
*  clearance analysis has not been run);  UF_CLEAR_COPY_RESULTS makes a copy of
*  the current analysis results, but not the interference bodies;
*  UF_CLEAR_COPY_INTERF_BODIES makes a complete copy of the results. The name
*  must  be less than MAX_LINE_SIZE characters long.
*  NOTE: The new data set tag may only be used as a parameter to
*  other UF_CLEAR functions.
*
*  Return:
*        Return code:
*               0 = No error
*           not 0 = Error code, which includes
*                               UF_CLEAR_err_bad_dataset
*                               UF_CLEAR_err_name_exists
*                               UF_CLEAR_err_bad_string
*                               UF_CLEAR_err_bad_copy_mode.
*
*  Environment: Internal  and  External
*
*  See Also:
*   UF_CLEAR_ask_dataset_version
*   UF_CLEAR_ask_dataset_name
*   UF_CLEAR_count_datasets
*   UF_CLEAR_create_dataset
*   UF_CLEAR_delete_dataset
*   UF_CLEAR_find_dataset
*   UF_CLEAR_rename_dataset
*  History:
*******************************************************************************/
extern UFUNEXPORT int UF_CLEAR_copy_dataset (
        tag_t   dataset,        /* <I>
                                The dataset to copy.
                                */
        char    *name,          /* <I>
                                The name of the new dataset.
                                */
        int     mode,           /* <I>
                                Copy mode, see above.
                                */
        tag_t   *new_dataset    /* <O>
                                The dataset that is copied.
                                */
);

/*******************************************************************************
*
*  Determines the number of clearance analysis datasets in the specified part.
*  Return:
*        Return code:
*               0 = No error
*           not 0 = Error code, which includes
*                               UF_CLEAR_err_bad_part.
*
*  Environment :Internal & External
*
*  See Also:
*   UF_CLEAR_ask_dataset_version
*   UF_CLEAR_ask_dataset_name
*   UF_CLEAR_copy_dataset
*   UF_CLEAR_create_dataset
*   UF_CLEAR_delete_dataset
*   UF_CLEAR_find_dataset
*   UF_CLEAR_rename_dataset
*
*  History:
*******************************************************************************/
extern UFUNEXPORT int UF_CLEAR_count_datasets (
        tag_t   part_tag,       /* <I>
                                   The part in which to count.
                                */
        int     *num            /* <O>
                                   The number of datasets.
                                */
);

/*******************************************************************************
*  Creates a new clearance analysis data set, initialized to default values.
*  If successful, this routine returns the tag of the new dataset. If a
*  dataset of the given name already exists, an error is returned. The
*  name must be less than MAX_LINE_SIZE characters long.
*  NOTE: The new data set tag may only be used as a parameter to
*  other UF_CLEAR functions.

* Return:
*       Return code:
*              0 = No error
*          not 0 = Error code, which includes
*                              UF_CLEAR_bad_part
*                              UF_CLEAR_err_name_exists
*                              UF_CLEAR_err_bad_string.
*
* Environment: Internal  and  External
*
*  See Also:
*   UF_CLEAR_ask_dataset_version
*   UF_CLEAR_ask_dataset_name
*   UF_CLEAR_copy_dataset
*   UF_CLEAR_count_datasets
*   UF_CLEAR_delete_dataset
*   UF_CLEAR_find_dataset
*   UF_CLEAR_rename_dataset
* History:
*******************************************************************************/
extern UFUNEXPORT int UF_CLEAR_create_dataset(
tag_t part_tag ,/* <I>
                The part in which the new dataset belongs.
                */
char * name ,/* <I>
             The name of the new dataset.
             */
tag_t * dataset  /* <O>
                 The new dataset tag.
                 */
);

/*******************************************************************************
*
*  Delete the given clearance analysis data set.
*  NOTE: Do not delete data sets while they are being cycled.
*
*  Return:
*        Return code:
*               0 = No error
*           not 0 = Error code, which includes
*                               UF_CLEAR_err_bad_dataset.
*
*  Environment: Internal  and  External
*
*  See Also:
*   UF_CLEAR_ask_dataset_version
*   UF_CLEAR_ask_dataset_name
*   UF_CLEAR_copy_dataset
*   UF_CLEAR_count_datasets
*   UF_CLEAR_create_dataset
*   UF_CLEAR_find_dataset
*   UF_CLEAR_rename_dataset
*
*  History:
*******************************************************************************/
extern UFUNEXPORT int UF_CLEAR_delete_dataset(
tag_t dataset  /* <I>
               The dataset to delete.
               */
);

/*******************************************************************************
*
*  Finds the tag of a named clearance analysis data set. If the name
*  doesn't exist, UF_CLEAR_err_cant_find_dataset is returned. The
*  name must be equal to or less than MAX_LINE_SIZE characters long.
*  NOTE: The data set tag may only be used as a parameter to other
*  UF_CLEAR functions.
*
*  Return:
*        Return code:
*               0 = No error
*           not 0 = Error code, which includes
*                               UF_CLEAR_err_bad_part
*                               UF_CLEAR_err_bad_string
*                               UF_CLEAR_err_cant_find_dataset.
*
*  Environment: Internal  and  External
*
*  See Also:
*   UF_CLEAR_ask_dataset_version
*   UF_CLEAR_ask_dataset_name
*   UF_CLEAR_copy_dataset
*   UF_CLEAR_count_datasets
*   UF_CLEAR_create_dataset
*   UF_CLEAR_delete_dataset
*   UF_CLEAR_rename_dataset
*
*  History:
*******************************************************************************/
extern UFUNEXPORT int UF_CLEAR_find_dataset(
tag_t part_tag ,/* <I>
                The part in which to search.
                */
char * name ,/* <I>
             The name of the dataset to search for.
             */
tag_t * dataset  /* <O>
                 The tag of the found dataset.
                 */
);


/*******************************************************************************
*
*  Changes the name of the given data set. If a dataset of the given name
*  already exists, an error is returned. The name must be equal to or less
*  than MAX_LINE_SIZE characters long.
*
*  Return:
*        Return code:
*               0 = No error
*           not 0 = Error code, which includes
*                               UF_CLEAR_err_bad_dataset
*                               UF_CLEAR_err_name_exists
*                               UF_CLEAR_err_bad_string.
*
*  Environment: Internal  and  External
*
*  See Also:
*   UF_CLEAR_ask_dataset_version
*   UF_CLEAR_ask_dataset_name
*   UF_CLEAR_copy_dataset
*   UF_CLEAR_count_datasets
*   UF_CLEAR_create_dataset
*   UF_CLEAR_delete_dataset
*   UF_CLEAR_find_dataset
*   UF_CLEAR_find_dataset
*   UF_CLEAR_create_dataset
*
*  History:
*******************************************************************************/
extern UFUNEXPORT int UF_CLEAR_rename_dataset(
tag_t dataset ,/* <I>
               The dataset to rename.
               */
char * name  /* <I>
             The new name.
             */
);



/*****************************************************************************
                       Begin the object list routines.
******************************************************************************/

/*****************************************************************************
*
*  Inquire the number of object lists used by the given clearance analysis
*  data set. The number of lists can either be 1 or 2.
*
*  Return:
*        Return code:
*               0 = No error
*           not 0 = Error code, which includes
*                               UF_CLEAR_err_bad_dataset.
*
*  Environment: Internal  and  External
*
*  See Also:
*   UF_CLEAR_ask_obj_list
*   UF_CLEAR_set_obj_list
*
*  History:
******************************************************************************/
extern UFUNEXPORT int UF_CLEAR_ask_num_lists(
tag_t dataset ,/* <I>
               The dataset tag.
               */
int * num_lists  /* <O>
                 The number of lists used (1 or 2).
                 */
);


/*******************************************************************************
*
*  Inquires data associated with one of the clearance analysis object lists,
*  specified by which_list. The list_type corresponds to the ways the
*  object lists can be defined in the interactive application by using one
*  of these values: UF_CLEAR_ALL_OBJECTS, UF_CLEAR_ALL_VISIBLE_OBJECTS,
*  UF_CLEAR_ALL_BUT, or UF_CLEAR_FIXED_LIST.
*  If the data set only uses one list and which_list is 2, then list_type is
*  set to UF_CLEAR_LIST2_NOT_USED. The list is evaluated when
*  necessary and the number of objects in the list is returned in list_size.
*  A pointer to a tag_array is returned.
*  If list_size is greater than zero, you must call UF_free when you no
*  longer need this array. The tag_array stores either solid body or facet
*  model tags depending on which objects are currently loaded. If both
*  are loaded, the solid body tags are returned. If neither object is
*  loaded, then NULL_TAG is placed in the array.
*
*  Return:
*        Return code:
*               0 = No error
*           not 0 = Error code, which includes
*                               UF_CLEAR_err_bad_dataset
*                               UF_CLEAR_err_bad_list_num.
*
*  Environment: Internal  and  External
*
*  See Also:
*   UF_CLEAR_ask_num_lists
*   UF_CLEAR_set_obj_list
*
*  History:
*******************************************************************************/
extern UFUNEXPORT int UF_CLEAR_ask_obj_list(
tag_t dataset ,/* <I>
                 The dataset tag.
                 */
int which_list ,/* <I>
                Is this for list 1 or list 2?
                Acceptable values are 1 and 2.
                */
int * list_type ,/* <O>
                 The type of list (UF_CLEAR_ALL_OBJECTS,
                 UF_CLEAR_ALL_VISIBLE_OBJECTS,
                 UF_CLEAR_ALL_BUT,
                 UF_CLEAR_FIXED_LIST, or
                 UF_CLEAR_LIST2_NOT_USED).
                 */
int * list_size ,/* <O>
                 The number of objects in list.
                 */
tag_t ** tag_array  /* <OF,len:list_size>
                    The pointer to an array of objects (solids or facets)
                    on the list.  This should be freed by calling UF_free.
                    */
);



/*******************************************************************************
*  Returns a list of objects that was last selected to be excluded from
*  which_list, regardless of the current list type. If an object on the list  is
*  currently not loaded, a NULL_TAG is put in its place in the
*  tag_array. You need to free the tag_array when no longer needed.
*
*  Return:
*        Return code:
*               0 = No error
*           not 0 = Error code, which includes
*                               UF_CLEAR_err_bad_dataset and
*                               UF_CLEAR_err_bad_list_num.
*
*  Environment: Internal  and  External
*  See Also:
*   UF_CLEAR_ask_obj_list
*   UF_CLEAR_set_obj_list
*
*  History:
*******************************************************************************/
extern UFUNEXPORT int UF_CLEAR_ask_obj_all_but_list (
tag_t dataset ,/* <I>
               The dataset tag
               */
int which_list ,/* <I>
                Determines which list to use:
                1 = List 1
                2 = List 2
                */
int * list_size ,/* <O>
                 The number of objects in the list
                 */
tag_t ** tag_array  /* <OF,len:list_size>
                    The array of objects (solid or facet) on the list.
                    This should be freed by calling UF_free.
                    */
);


/*******************************************************************************
*  Fully defines a clearance analysis object list, specified by which_list.
*  The list type corresponds to the ways an object list can be defined in
*  the interactive application by using one of these values:
*  UF_CLEAR_ALL_OBJECTS, UF_CLEAR_ALL_VISIBLE_OBJECTS, UF_CLEAR_ALL_BUT, or
*  UF_CLEAR_FIXED_LIST.
*  To specify a one list data set, set which_list to 2 and list_type to
*  UF_CLEAR_LIST2_NOT_USED. No tag_array is necessary.
*  For a UF_CLEAR_ALL_OBJECTS or UF_CLEAR_ALL_VISIBLE_OBJECTS list, you do
*  not need to supply a tag_array -- the list is automatically evaluated
*  when necessary.
*  For a UF_CLEAR_ALL_BUT list, you must specify the tags of those
*  solid bodies and/or facet models you want to explicitly exclude from
*  the list. The list of included objects is reevaluated when necessary.
*  For a UF_CLEAR_FIXED_LIST, you must specify an array of objects
*  to be members of the list. These objects must be solid bodies or facet
*  models. This list is not further evaluated. Note that you may need to
*  call this routine twice, once for each list.
*
*  Return:
*        Return code:
*               0 = No error
*           not 0 = Error code, which includes
*                               UF_CLEAR_err_bad_dataset
*                               UF_CLEAR_err_bad_list_num
*                               UF_CLEAR_err_bad_list_type
*                               UF_CLEAR_err_bad_list_data.
*
*  Environment: Internal  and  External
*  See Also:
*   UF_CLEAR_ask_num_lists
*   UF_CLEAR_ask_obj_list
*  History:
*******************************************************************************/
extern UFUNEXPORT int UF_CLEAR_set_obj_list(
tag_t dataset ,/* <I>
               The dataset tag.
               */
int which_list ,/* <I>
                Is this for list 1 or list 2? Acceptable values are 1
                and 2.
                */
int list_type ,/* <I>
               The new type of list
                (UF_CLEAR_ALL_OBJECTS,
                UF_CLEAR_ALL_VISIBLE_OBJECTS,
                UF_CLEAR_ALL_BUT,
                UF_CLEAR_FIXED_LIST, or
                UF_CLEAR_LIST2_NOT_USED).
               */
int list_size ,/* <I>
               The size of tag_array.
               */
tag_t * tag_array  /* <I,len:list_size> list_size
                   The object tags (solids or facets) to be applied to
                   the list.
                   */
);


/****************************************************************************
                         Begin clearance zone routines.
*****************************************************************************/

/****************************************************************************
*
*  Inquire the default clearance zone for the given data set. This routine
*  returns the clearance zone expression tag. If no expression has ever
*  been set, NULL_TAG is returned. Interpret its value as 0.0. For a
*  non-null expression, call UF_MODL_ask_exp_tag_value to get the
*  value of the expression.
*
*  Return:
*        Return code:
*               0 = No error
*           not 0 = Error code, which includes
*                               UF_CLEAR_err_bad_dataset.
*
*  Environment: Internal  and  External
*
*  See Also:
*   UF_CLEAR_ask_object_clear_zone
*   UF_CLEAR_ask_pair_clear_zone
*   UF_CLEAR_set_default_clear_zone
*   UF_CLEAR_set_object_clear_zone
*   UF_CLEAR_set_pair_clear_zone
*
*  History:
*****************************************************************************/
extern UFUNEXPORT int UF_CLEAR_ask_default_clear_zone(
tag_t dataset ,/* <I>
               The dataset tag.
               */
tag_t * def_clr_zone  /* <O>
                      The default clearance zone expression tag.
                      */
);


/*******************************************************************************
*
*  Inquire the clearance zone assigned to a given object.  The object must be
*  a member of the dataset.  The tag of the expression is returned.  If no
*  expression has ever been set, the part of the given object is checked for
*  a clearance zone expression, if none is found, NULL_TAG will be returned
*  for clr_zone. Interpret its value as 0.0 (this is the default value).  For a
*  non-null expression, call UF_MODL_ask_exp_tag_value to get its value.  The
*  source parameter tells where the clearance zone comes from.
*  UF_CLEAR_USING_DEFINED_CZ specifies that the object has its own clearance
*  zone.  UF_CLEAR_USING_DEFAULT_CZ means the default clearance zone is used.
*
*  Return:
*        Return code:
*               0 = No error
*           not 0 = Error code, which includes
*                               UF_CLEAR_err_bad_dataset
*
*  Environment: Internal  and  External
*
*  See Also:
*   UF_CLEAR_ask_default_clear_zone
*   UF_CLEAR_ask_pair_clear_zone
*   UF_CLEAR_set_default_clear_zone
*   UF_CLEAR_set_object_clear_zone
*   UF_CLEAR_set_pair_clear_zone
*
*  History:
*******************************************************************************/
extern UFUNEXPORT int UF_CLEAR_ask_object_clear_zone(
tag_t dataset ,/* <I>
               The dataset tag.
               */
tag_t object ,/* <I>
              The object (solid or facet) whose clearance zone is
              requested.
              */
tag_t * clr_zone ,/* <O>
                    The clearance zone expression.
                  */
int * source  /* <O>
              The source of the clearance zone (one of
              UF_CLEAR_USING_DEFINED_CZ, or
              UF_CLEAR_USING_DEFAULT_CZ).
              */
);

/*******************************************************************************
*  Inquire the clearance zone for a specific pair of objects.  Both objects
*  must be members of the given dataset.  The tag of the expression is
*  returned.  If no expression has ever been set, NULL_TAG will be returned
*  for clr_zone.  Interpret its value as 0.0 (this is the default value).  For
*  a non-null expression, call UF_MODL_ask_exp_tag_value to get its value.
*  The source parameter tells where the clearance zone comes from.  The
*  clearance zone could be the greater of the zones from object 1 or 2
*  (UF_CLEAR_USING_OBJ1_CZ or UF_CLEAR_USING_OBJ2_CZ).
*  UF_CLEAR_USING_PAIR_CZ means this pair has its own explicit clearance zone.
*  UF_CLEAR_USING_DEFAULT_CZ means the default clearance zone is used.
*
*  Return:
*        Return code:
*               0 = No error
*           not 0 = Error code, which includes
*                               UF_CLEAR_err_bad_dataset
*
*  Environment: Internal  and  External
*
*  See Also:
*   UF_CLEAR_ask_default_clear_zone
*   UF_CLEAR_set_default_clear_zone
*   UF_CLEAR_set_object_clear_zone
*   UF_CLEAR_set_pair_clear_zone
*  History:
*******************************************************************************/
extern UFUNEXPORT int UF_CLEAR_ask_pair_clear_zone(
tag_t dataset ,/* <I>
               The dataset tag.
               */
tag_t object1 ,/* <I>
               The first object (solid or facet) in the pair.
               */
tag_t object2 ,/* <I>
               The second object (solid or facet) in the pair.
               */
tag_t * clr_zone ,/* <O>
                  The clearance zone expression.
                  */
int * source  /* <O>
              The source of the clearance zone (one of
              UF_CLEAR_USING_OBJ1_CZ,
              UF_CLEAR_USING_OBJ2_CZ,
              UF_CLEAR_USING_PAIR_CZ, or
              UF_CLEAR_USING_DEFAULT_CZ).
              */
);


/*******************************************************************************
*  Sets the default clearance zone for the given data set. During analysis,
*  any object pair that doesn't have either a zone for one of its objects or
*  for the pair, explicitly uses this default clearance zone. You must
*  supply the tag of a valid expression.
*
*  Return:
*        Return code:
*               0 = No error
*           not 0 = Error code, which includes
*                               UF_CLEAR_err_bad_dataset
*                               UF_CLEAR_err_bad_expression.
*
*  Environment: Internal  and  External
*
*  See Also:
*   UF_CLEAR_ask_default_clear_zone
*   UF_CLEAR_ask_pair_clear_zone
*   UF_CLEAR_ask_object_clear_zone
*   UF_CLEAR_set_object_clear_zone
*   UF_CLEAR_set_pair_clear_zone
*
*  History:
*******************************************************************************/
extern UFUNEXPORT int UF_CLEAR_set_default_clear_zone(
tag_t dataset ,/* <I>
               The dataset tag.
               */
tag_t def_clr_zone  /* <I>
                    The tag of the new default clearance zone
expression.
                    */
);


/*******************************************************************************
*
* Assigns the clearance zone for the given object. The object must be a
* member of the data set. During analysis, any object pair that doesn't
* have a clearance zone explicitly assigned to that pair uses the greater
* of the clearance zones assigned to each object. You must supply the
* tag of a valid expression.
*
* Return:
*       Return code:
*              0 = No error
*          not 0 = Error code, which includes
*                              UF_CLEAR_err_bad_dataset
*                              UF_CLEAR_err_bad_expression.
*
* Environment: Internal  and  External
*
*  See Also:
*   UF_CLEAR_ask_default_clear_zone
*   UF_CLEAR_ask_pair_clear_zone
*   UF_CLEAR_ask_object_clear_zone
*   UF_CLEAR_set_default_clear_zone
*   UF_CLEAR_set_pair_clear_zone
*
* History:
*******************************************************************************/
extern UFUNEXPORT int UF_CLEAR_set_object_clear_zone(
tag_t dataset ,/* <I>
               The dataset tag.
               */
tag_t object ,/* <I>
              The object (solid or facet) whose clearance zone is
              being set.
              */
tag_t clr_zone  /* <I>
                The new clearance zone expression.
                */
);


/*******************************************************************************
*  Assign the clearance zone for the given object pair. Each object must
*  be a member of the data set. During analysis, the pair clearance zones
*  overrides any clearance zones assigned to the individual objects. You
*  must supply the tag of a valid expression.
*
*  Return:
*        Return code:
*               0 = No error
*           not 0 = Error code, which includes
*                               UF_CLEAR_err_bad_dataset
*                               UF_CLEAR_err_bad_expression.
*
*  Environment: Internal  and  External
*
*  See Also:
*   UF_CLEAR_ask_default_clear_zone
*   UF_CLEAR_ask_pair_clear_zone
*   UF_CLEAR_ask_object_clear_zone
*   UF_CLEAR_set_default_clear_zone
*   UF_CLEAR_set_object_clear_zone
*
*  History:
*******************************************************************************/
extern UFUNEXPORT int UF_CLEAR_set_pair_clear_zone(
tag_t dataset ,/* <I>
               The dataset tag.
               */
tag_t object1 ,/* <I>
               The first object (solid or facet) in the pair.
               */
tag_t object2 ,/* <I>
               The second object (solid or facet) in the pair.
               */
tag_t clr_zone  /* <I>
                The new clearance zone expression.
                */

);



/*******************************************************************************
                      ** Begin pair exclusion routines.
*******************************************************************************/

/*******************************************************************************
*  Enquires the global exclusion rules. These settings cause classes of
*  object pairs to be excluded from analysis: pairs composed of two
*  objects that belong to mated components, pairs belonging to the same
*  sub-assembly/component, pairs belonging to the same part and pairs
*  belonging to the same group.
*
*  Return:
*        Return code:
*               0 = No error
*           not 0 = Error code, which includes
*                               UF_CLEAR_err_bad_dataset.
*
*  Environment: Internal  and  External
*
*  See Also:
*
*  History:
*******************************************************************************/
extern UFUNEXPORT int UF_CLEAR_ask_exclude_rules(
tag_t dataset ,/* <I>
               The dataset tag.
               */
int * exclude_rules  /* <O>
                     The exclusion rules that were applied. Any of the
                     following constants can be ORed together:
                     UF_CLEAR_EXCLUDE_MATING_PAIRS
                     UF_CLEAR_EXCLUDE_WITHIN_COMP
                     UF_CLEAR_EXCLUDE_WITHIN_PART
                     UF_CLEAR_EXCLUDE_WITHIN_GROUP
                     */
);

/*******************************************************************************
*  Inquires if an object pair has changed since the last analysis run. Both
*  objects must be solid bodies or facet models that are members of the
*  clearance analysis data set. If either object has changed since the last
*  analysis run, then is_changed is returned as TRUE. If no analysis has
*  been run on either of the objects, TRUE is returned.
*
*  Return:
*        Return code:
*               0 = No error
*           not 0 = Error code, which includes
*                               UF_CLEAR_err_bad_dataset
*
*  Environment: Internal  and  External
*
*  See Also:
*   UF_CLEAR_ask_exclude_rules
*   UF_CLEAR_set_exclude_rules
*   UF_CLEAR_set_pair_exclusion
*   UF_CLEAR_set_pair_inclusion
*
*  History:
*******************************************************************************/
extern UFUNEXPORT int UF_CLEAR_is_pair_changed(
tag_t dataset ,/* <I>
               The dataset tag.
               */
tag_t object1 ,/* <I>
               The first object (solid or facet) in the pair.
               */
tag_t object2 ,/* <I>
               The second object (solid or facet) in the pair.
               */
logical * is_changed  /* <O>
                      Has this pair changed since the last analysis run?
                      */
);


/*******************************************************************************
*  Inquires if an object pair is to be included in the analysis. Both objects
*  must be solid bodies or facet models that are members of the
*  clearance analysis data set. If the pair is to be analyzed, the include_it
*  is returned as TRUE. The reason parameter signifies why the pair is
*  included or excluded. UF_CLEAR_EXCL_NO_REASON is returned
*  when the default behavior is applied.
*  UF_CLEAR_EXCL_USER_DEF means the user has explicitly
*  included or excluded this pair. UF_CLEAR_EXCL_SAME_COMP,
*  UF_CLEAR_EXCL_SAME_PART, UF_CLEAR_EXCL_SAME_GROUP, and
*  UF_CLEAR_EXCL_MATED_COMP are returned if one of the
*  global exclusion rules applied to this pair. Only one such rule is
*  returned, even if several such rules apply to the given pair.
*
*  Return:
*        Return code:
*               0 = No error
*           not 0 = Error code, which includes
*                               UF_CLEAR_err_bad_dataset
*
*  Environment: Internal  and  External
*
*  See Also:
*   UF_CLEAR_ask_exclude_rules
*   UF_CLEAR_is_pair_changed
*   UF_CLEAR_set_exclude_rules
*   UF_CLEAR_set_pair_exclusion
*   UF_CLEAR_set_pair_inclusion
*
*  History:
*******************************************************************************/
extern UFUNEXPORT int UF_CLEAR_is_pair_included(
tag_t dataset ,/* <I>
               The dataset tag.
               */
tag_t object1 ,/* <I>
               The first object (solid or facet) in the pair.
               */
tag_t object2 ,/* <I>
               The second object (solid or facet) in the pair.
               */
logical * include_it ,/* <O>
                      Should this pair be included in the analysis?
                      */
int * reason ,/* <O>
                The reason the pair is included or excluded (one of
                UF_CLEAR_EXCL_NO_REASON,
                UF_CLEAR_EXCL_USER_DEF,
                UF_CLEAR_EXCL_SAME_COMP,
                UF_CLEAR_EXCL_SAME_PART,
                UF_CLEAR_EXCL_SAME_GROUP, or
                UF_CLEAR_EXCL_MATED_COMP).
              */
char ** text  /* <OF>
                The text associated with
                UF_CLEAR_set_pair_inclusion and
                UF_CLEAR_set_pair_exclusion when reason is
                UF_CLEAR_EXCL_USER_DEF, or an empty
                string is returned. Use UF_free((void *) *text) to
                deallocate memory when done.
              */
);


/*******************************************************************************
*  Sets the global exclusion rules. These settings causes classes of object
*  pairs to be excluded from analysis: pairs composed of two objects that
*  belong to mated components; pairs belonging to the same sub-assembly/
*  component; pairs belonging to the same part; and pairs belonging to the
*  same group. The exclude_rules value can be comprised of zero or more of
*  the following constants ORed together: UF_CLEAR_EXCLUDE_MATING_PAIRS,
*  UF_CLEAR_EXCLUDE_WITHIN_COMP, UF_CLEAR_EXCLUDE_WITHIN_PART and
*  UF_CLEAR_EXCLUDE_WITHIN_GROUP.  The default value is to exclude nothing,
*  i.e., exclude_rules = 0.  The customer default file can also be used
*  to change this default value.  See the default values for,
*  Assemblies_ClrAnlExclMatingPairs, Assemblies_ClrAnlExclWithinComp,
*  Assemblies_ClrAnlExclWithinPart and Assemblies_ClrAnlExclWithinGroup.
*
*  Return:
*        Return code:
*               0 = No error
*           not 0 = Error code, which includes
*                               UF_CLEAR_err_bad_dataset
*                               UF_CLEAR_err_bad_exclude_rule.
*
*  Environment: Internal  and  External
*
*  See Also:
*   UF_CLEAR_ask_exclude_rules
*   UF_CLEAR_is_pair_changed
*   UF_CLEAR_is_pair_included
*   UF_CLEAR_set_pair_exclusion
*   UF_CLEAR_set_pair_inclusion
*
*  History:
*******************************************************************************/
extern UFUNEXPORT int UF_CLEAR_set_exclude_rules(
tag_t dataset ,/* <I>
               The data set tag.
               */
int exclude_rules  /* <I>
                        Which rules should be applied? The following
                        constants can be ORed together:
                        UF_CLEAR_EXCLUDE_MATING_PAIRS,
                        UF_CLEAR_EXCLUDE_WITHIN_COMP,
                        UF_CLEAR_EXCLUDE_WITHIN_PART,
                        and UF_CLEAR_EXCLUDE_WITHIN_GROUP.
                  */
);



/*******************************************************************************
*  Explicitly excludes an object pair from analysis. Each object must be a
*  member of the data set. You may associate a text string with the pair.
*  The string must be equal to or less than MAX_LINE_SIZE characters
*  long.
*
*  Return:
*        Return code:
*               0 = No error
*           not 0 = Error code, which includes
*                               UF_CLEAR_err_bad_dataset
*                               UF_CLEAR_err_bad_string.
*
*  Environment: Internal  and  External
*  See Also:
*   UF_CLEAR_ask_exclude_rules
*   UF_CLEAR_is_pair_changed
*   UF_CLEAR_is_pair_included
*   UF_CLEAR_set_exclude_rules
*   UF_CLEAR_set_pair_inclusion
*
*  History:
*******************************************************************************/
extern UFUNEXPORT int UF_CLEAR_set_pair_exclusion(
tag_t dataset ,/* <I>
               The data set tag.
               */
tag_t object1 ,/* <I>
               The first object (solid or facet) in the pair.
               */
tag_t object2 ,/* <I>
               The second object (solid or facet) in the pair.
               */
char * text  /* <I>
             The text to associate with each pair.
             */
);

/*******************************************************************************
*
*  Explicitly includes an object pair in analysis. Each object must be a
*  member of the data set. You may associate a text string with the pair.
*  The string must be equal to or less than MAX_LINE_SIZE characters
*  long.
*
*  Return:
*        Return code:
*               0 = No error
*           not 0 = Error code, which includes
*                               UF_CLEAR_err_bad_dataset
*                               UF_CLEAR_err_bad_string.
*
*  Environment: Internal  and  External
*
*  See Also:
*   UF_CLEAR_ask_exclude_rules
*   UF_CLEAR_is_pair_changed
*   UF_CLEAR_is_pair_included
*   UF_CLEAR_set_exclude_rules
*   UF_CLEAR_set_pair_exclusion
*
*  History:
*/
extern UFUNEXPORT int UF_CLEAR_set_pair_inclusion(
tag_t dataset ,/* <I>
               The dataset tag.
               */
tag_t object1 ,/* <I>
               The first object (solid or facet) in the pair.
               */
tag_t object2 ,/* <I>
               The second object (solid or facet) in the pair.
               */
char * text  /* <I>
             The text to associate with each pair.
             */
);


/*******************************************************************************
                         ** Begin analysis routines.
*******************************************************************************/

/*******************************************************************************
*  Inquires the current clearance analysis mode. It may have one of the
*  following values: UF_CLEAR_QUICK_FACET, UF_CLEAR_FULL_FACET,
*  UF_CLEAR_BEST_AVAILABLE, UF_CLEAR_FACET_SOLID, or UF_CLEAR_SOLID.
*
*  Return:
*        Return code:
*               0 = No error
*           not 0 = Error code, which includes
*                               UF_CLEAR_err_bad_dataset.
*
*  Environment: Internal  and  External
*
*  See Also:
*   UF_CLEAR_ask_interf_data
*   UF_CLEAR_ask_next_interf
*   UF_CLEAR_ask_results
*   UF_CLEAR_count_interferences
*   UF_CLEAR_delete_interf
*   UF_CLEAR_do_clearance_analysis
*   UF_CLEAR_set_analysis_mode
*   UF_CLEAR_set_interf_text
*
*  History:
*******************************************************************************/
extern UFUNEXPORT int UF_CLEAR_ask_analysis_mode(
tag_t dataset ,/* <I>
               The data set tag.
               */
int * analysis_mode  /* <O>
                     One of the following analysis modes:
                     UF_CLEAR_QUICK_FACET,
                     UF_CLEAR_FULL_FACET,
                     UF_CLEAR_BEST_AVAILABLE,
                     UF_CLEAR_FACET_SOLID, or
                     UF_CLEAR_SOLID.
                     */
);

/*******************************************************************************
*  Inquires the data associated with a given pair of interfering objects.
*  The structure that is returned contains the type of interference. The
*  interference type is one of:
*  UF_CLEAR_SOFT_INTERFERENCE,
*  UF_CLEAR_TOUCH_INTERFERENCE,
*  UF_CLEAR_HARD_INTERFERENCE,
*  UF_CLEAR_CONT_1_IN_2_INTERFERENCE,
*  UF_CLEAR_CONT_2_IN_1_INTERFERENCE, or
*  UF_CLEAR_NO_INTERFERENCE.
*  If the interference was computed during the most recent analysis run,
*  the new_interference will be TRUE. The array of interference bodies
*  that are associated with the interference are passed back in the
*  interf_bodies field. n_bodies indicates the size of this array. This array
*  of tags could refer to points, lines, curves, and/or solid bodies,
*  depending on the analysis mode and the type of interference. If
*  n_bodies is greater than 0, this array must be freed using UF_free by
*  the caller when no longer needed. point1 and point2 indicate points
*  (in assembly coordinates) on both of the interfering objects. The text
*  field contains any text the user has associated with this interference.
*  interf_num is a unique number associated with each interference. You
*  may choose to sort interference based on this value. If the two objects
*  do not have a stored interference, then zero is returned for the
*  interference number, UF_CLEAR_NO_INTERFERENCE is returned as
*  the type, and the size of the interf_bodies array is zero.
*
*  Return:
*        Return code:
*               0 = No error
*           not 0 = Error code, which includes
*                               UF_CLEAR_err_bad_dataset
*                               UF_CLEAR_err_bad_interf.
*
*  Environment: Internal  and  External
*  See Also:
*   UF_CLEAR_ask_analysis_mode
*   UF_CLEAR_ask_next_interf
*   UF_CLEAR_ask_results
*   UF_CLEAR_count_interferences
*   UF_CLEAR_delete_interf
*   UF_CLEAR_do_clearance_analysis
*   UF_CLEAR_set_analysis_mode
*   UF_CLEAR_set_interf_text
*
*  History:
*******************************************************************************/
extern UFUNEXPORT int UF_CLEAR_ask_interf_data(
tag_t dataset ,/* <I>
               The dataset tag.
               */
tag_t  object1 ,/* <I>
                The first object (solid or facet) in the pair.
                */
tag_t  object2 ,/* <I>
                The second object (solid or facet) in the
                pair.
                */
UF_CLEAR_interf_data_t * interf_data  /* <O>
                                      The structure containing data on this
                                      interfering pair.
                                      */
);

/*******************************************************************************
*  Cycles the interference in a clearance analysis data set. Interferences
*  are stored as object pairs. Start the cycling using NULL_TAG as the
*  input values for both object1 and object2. This routine passes back the
*  tags of the objects that define the next interference. NULL_TAG
*  returned for either object indicates the end of the cycling.
*  NOTE: The object tags that are passed back may refer to unloaded
*  objects. One or both of these objects could be object occurrences that
*  refer to unloaded prototypes. Before using these tags for any purpose
*  (other than cycling interferences) you must verify that the objects
*  refer to loaded objects.
*
*  Return:
*        Return code:
*               0 = No error
*           not 0 = Error code, which includes
*                               UF_CLEAR_err_bad_dataset
*                               UF_CLEAR_err_bad_interf.
*
*  Environment: Internal  and  External
*
*  See Also:
*   UF_CLEAR_ask_analysis_mode
*   UF_CLEAR_ask_interf_data
*   UF_CLEAR_ask_results
*   UF_CLEAR_count_interferences
*   UF_CLEAR_delete_interf
*   UF_CLEAR_do_clearance_analysis
*   UF_CLEAR_set_analysis_mode
*   UF_CLEAR_set_interf_text
*  History:
*******************************************************************************/
extern UFUNEXPORT int UF_CLEAR_ask_next_interf(
tag_t dataset ,/* <I>
               The data set tag.
               */
tag_t * object1 ,/* <I/O>
               The first object (solid or facet) in the pair.
                 */
tag_t * object2  /* <I/O>
                 The second object (solid or facet) in the pair.
                 */
);


/*******************************************************************************
*  Inquires a summary of the results of the most recent clearance
*  analysis run. The UF_CLEAR_summary_t structure is filled with
*  analysis statistics, including numbers of objects, number of pairs,
*  number of checked pairs, and number of interferences of each type. If
*  clearance analysis has never been run on the data set, an error is
*  returned.
*
*  Return:
*        Return code:
*               0 = No error
*           not 0 = Error code, which includes
*                               UF_CLEAR_err_bad_dataset
*                               UF_CLEAR_err_no_results.
*
*  Environment: Internal  and  External
*  See Also:
*   UF_CLEAR_ask_analysis_mode
*   UF_CLEAR_ask_interf_data
*   UF_CLEAR_ask_next_interf
*   UF_CLEAR_count_interferences
*   UF_CLEAR_delete_interf
*   UF_CLEAR_do_clearance_analysis
*   UF_CLEAR_set_analysis_mode
*   UF_CLEAR_set_interf_text
*
*  History:
*******************************************************************************/
extern UFUNEXPORT int UF_CLEAR_ask_results(
tag_t dataset ,/* <I>
               The data set tag.
               */
UF_CLEAR_summary_t * summary  /* <O>
                              The summary structure.
                              */
);


/*******************************************************************************
*  Inquires the number of interferences stored in a clearance analysis
*  data set. If clearance analysis has never been run on the data set, an
*  error is returned.
*
*  Return:
*        Return code:
*               0 = No error
*           not 0 = Error code, which includes
*                               UF_CLEAR_err_bad_dataset.
*
*  Environment: Internal  and  External
*  See Also:
*   UF_CLEAR_ask_analysis_mode
*   UF_CLEAR_ask_interf_data
*   UF_CLEAR_ask_next_interf
*   UF_CLEAR_ask_results
*   UF_CLEAR_delete_interf
*   UF_CLEAR_do_clearance_analysis
*   UF_CLEAR_set_analysis_mode
*   UF_CLEAR_set_interf_text
*
*  History:
*******************************************************************************/
extern UFUNEXPORT int UF_CLEAR_count_interferences(
tag_t dataset ,/* <I>
               The data set tag.
               */
int * num_interf  /* <O>
                  The number of interferences associated with the
                  dataset.
                  */
);



/*******************************************************************************
*  Deletes the interference for a given object pair. Both objects must be
*  members of the given data set. If the object pair does not refer to an
*  existing interference, an error is returned. All data associated with the
*  interference is deleted.
*  NOTE: It is acceptable to delete the interference bodies without
*  deleting the interference itself. Use the normal deletion functions to
*  delete the interference points, lines, curve, and/or solid bodies. By
*  doing so, all interference data is retained except for the bodies
*  themselves. This might be desirable in cases where the interference
*  bodies make the part file unnecessarily large.
*  Return:
*        Return code:
*               0 = No error
*           not 0 = Error code, which includes
*                               UF_CLEAR_err_bad_dataset
*                               UF_CLEAR_err_bad_interf.
*
*  Environment: Internal  and  External
*
*  See Also:
*   UF_CLEAR_ask_analysis_mode
*   UF_CLEAR_ask_interf_data
*   UF_CLEAR_ask_next_interf
*   UF_CLEAR_ask_results
*   UF_CLEAR_count_interferences
*   UF_CLEAR_do_clearance_analysis
*   UF_CLEAR_set_analysis_mode
*   UF_CLEAR_set_interf_text
*
*  History:
*******************************************************************************/
extern UFUNEXPORT int UF_CLEAR_delete_interf(
tag_t dataset ,/* <I>
               The data set tag.
               */
tag_t object1 ,/* <I>
               The first object (solid or facet) in the pair.
               */
tag_t object2  /* <I>
               The second object (solid or facet) in the pair.
               */
);


/*******************************************************************************
*  Performs clearance analysis on the given dataset using the previously
*  set options. This function looks at all object pairs from the objects
*  lists. All object pairs that are not excluded and have changed since the
*  last analysis run are analyzed. Facet models are created when
*  necessary if using one of the facet analysis modes. Interference results
*  are created using previously set options. This function can not be
*  gracefully interrupted and interferences are not reported as they are
*  found.
*
*  Return:
*        Return code:
*               0 = No error
*           not 0 = Error code, which includes:
*                               UF_CLEAR_err_bad_dataset
*                               UF_CLEAR_err_analysis_error
*                               UF_CLEAR_err_facet_error
*                               UF_CLEAR_err_obj_not_avail.
*
*  Environment: Internal  and  External
*
*  See Also:
*
*  History:
*******************************************************************************/
extern UFUNEXPORT int UF_CLEAR_do_clearance_analysis(
tag_t dataset  /* <I>
               The dataset tag.
               */
);


/*******************************************************************************
*  Sets the clearance analysis mode. It may have one of the following
*  values: UF_CLEAR_QUICK_FACET, UF_CLEAR_FULL_FACET,
*  UF_CLEAR_BEST_AVAILABLE, UF_CLEAR_FACET_SOLID, or UF_CLEAR_SOLID.
*
*  Return:
*        Return code:
*               0 = No error
*           not 0 = Error code, which includes
*                               UF_CLEAR_err_bad_analysis_mode,
*                               UF_CLEAR_err_bad_dataset.
*
*  Environment: Internal  and  External
*
*  See Also:
*   UF_CLEAR_ask_analysis_mode
*   UF_CLEAR_ask_interf_data
*   UF_CLEAR_ask_next_interf
*   UF_CLEAR_ask_results
*   UF_CLEAR_count_interferences
*   UF_CLEAR_do_clearance_analysis
*   UF_CLEAR_delete_interf
*   UF_CLEAR_set_interf_text
*
*  History:
******************************************************************************/
extern UFUNEXPORT int UF_CLEAR_set_analysis_mode(
tag_t dataset ,/* <I>
               The data set tag.
               */
int analysis_mode  /* <I>
                   One of the following analysis modes:
                   UF_CLEAR_QUICK_FACET,
                   UF_CLEAR_FULL_FACET,
                   UF_CLEAR_BEST_AVAILABLE,
                   UF_CLEAR_FACET_SOLID, or
                   UF_CLEAR_SOLID.
                   */
);


/*******************************************************************************
*  Associates a text string to an interfering object pair. Both objects must
*  be members of the given dataset. If the object pair does not refer to
*  an existing interference, an error is returned.
*
*  Return:
*        Return code:
*               0 = No error
*           not 0 = Error code, which includes
*                               UF_CLEAR_err_bad_dataset,
*                               UF_CLEAR_err_bad_interf.
*
*  Environment: Internal  and  External
*
*  See Also:
*
*  History:
*******************************************************************************/
extern UFUNEXPORT int UF_CLEAR_set_interf_text (
tag_t dataset ,/* <I>
               The dataset tag
               */
tag_t object1 ,/* <I>
               The first object (solid or facet) in the pair
               */
tag_t object2 ,/* <I>
               The second object (solid or facet) in the pair
               */
char * text  /* <I>
             The text to associate with the interference. The
             length of the text cannot be greater than the value
             assigned to the string constant MAX_LINE_SIZE.
             */
);


/*******************************************************************************
                       ** Begin miscellaneous routines.
*******************************************************************************/

/*******************************************************************************
*  Inquire clearance module preferences. The structure contains the
*  current interactive message filter, which indicates the types of
*  interferences that are displayed by the interactive analysis and review
*  functions. Each bit of this integer refers to a specific type of
*  interference (UF_CLEAR_SOFT_INTERFERENCE, etc.). Use the
*  appropriate C bitwise logical operators (&, |, and ^) to interpret this
*  value. The save_interference parameter indicates if the interference
*  bodies are saved during analysis. The current layer and color
*  assignments are returned. The current attention colors for
*  interferences and the parent objects is also given. These colors are
*  used in the interactive review of analysis results.
*
*  Return:
*        Return code:
*               0 = No error
*           not 0 = Error code, which includes
*                               UF_CLEAR_err_bad_dataset.
*
*  Environment: Internal  and  External
*
*  See Also:
*   UF_CLEAR_delete_all
*   UF_CLEAR_set_preferences
*
*  History:
*******************************************************************************/
extern UFUNEXPORT int UF_CLEAR_ask_preferences(
tag_t dataset ,/* <I>
               The dataset tag.
               */
UF_CLEAR_pref_t * preferences  /* <O>
                               The preferences structure.
                               */
);



/*******************************************************************************
*  Deletes all clearance analysis data from the given part, including all
*  clearance analysis data sets, analysis results, and interference bodies.
*
*  Return:
*        Return code:
*               0 = No error
*           not 0 = Error code, which includes:
*                               UF_CLEAR_bad_part.
*
*  Environment: Internal  and  External
*
*  See Also:
*   UF_CLEAR_ask_preferences
*   UF_CLEAR_delete_dataset
*   UF_CLEAR_set_preferences
*
*  History:
*******************************************************************************/
extern UFUNEXPORT int UF_CLEAR_delete_all(
tag_t part_tag  /* <I>
                The part from which all clearance analysis data is to
be deleted.
                */
);


/*******************************************************************************
*  Sets clearance module preferences. The structure contains the current
*  interactive message filter, which indicates the types of interferences
*  that are displayed by the interactive analysis and review functions.
*  Each bit of this integer refers to a specific type of interference
*  (UF_CLEAR_SOFT_INTERFERENCE, etc.). Use the appropriate C
*  bitwise logical operators (&, |, and ^) to set this value. The
*  save_interference parameter indicates if the interference bodies are
*  to be saved during analysis. The layer and color assignments will be
*  given to all new interference bodies. The attention colors for
*  interferences and the parent objects will be used in the interactive
*  review of analysis results. If you want to set just one of the values, you
*  must call UF_CLEAR_ask_preferences to fill the structure. Next, edit
*  those fields you want to change; then call UF_CLEAR_set_preferences.
*  The default values are:
*
*      interactive_msg_filter:   ALL (i.e., display all).
*      save_interference:        TRUE
*      interference_layer:       0 (current)
*      interference_color:       YELLOW
*      interf_attn_color:        RED
*      parent_attn_color:        CYAN
*
*  These defaults are controlled by the customer defaults file.  The default
*  behavior can be changed by editting that file.
*
*  Return:
*        Return code:
*               0 = No error
*           not 0 = Error code, which includes
*                               UF_CLEAR_err_bad_dataset
*                               UF_CLEAR_err_bad_msg_filter
*                               UF_CLEAR_err_bad_layer
*                               UF_CLEAR_err_bad_color.
*
*  Environment: Internal  and  External
*
*  See Also:
*
*  History:
*******************************************************************************/
extern UFUNEXPORT int UF_CLEAR_set_preferences(
tag_t dataset ,/* <I>
               The data set tag.
               */
UF_CLEAR_pref_t preferences  /* <I>
                             The preferences structure.
                             */
);




#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif /* UF_CLEAR_H_INCLUDED */
