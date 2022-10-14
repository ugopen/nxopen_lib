/*******************************************************************************
            Copyright (c) 1999-2000 Unigraphics Solutions, Inc.
                     Unpublished - All rights reserved
 *****************************************************************************
 *
 * 
 *
 *
 * File description:
 *
 *    This file contains documentation for the UF_CUTTER module. This module
 *    allows the Open API programmer to interface with the cutting tools that NX
 *    uses in its CAM operations. The programmer can perform functions
 *    such as retrieving a cutter into NX from an external library and creating
 *    a cutter based upon a template object.
 *
 ******************************************************************************/
#ifndef UF_CUTTER_H_INCLUDED
#define UF_CUTTER_H_INCLUDED

/***************************** Include Files **********************************/
#include <uf_defs.h>
#include <uf_cam.h>
#include <libufun_cam_exports.h>
#include <uf_obj_types.h>

#ifdef __cplusplus
extern "C" {
#endif

/******************************** Defines *************************************/

/**** CUTTER types *************/
#define UF_CUTTER_TYPE_MILL       1
#define UF_CUTTER_TYPE_DRILL      2
#define UF_CUTTER_TYPE_TURN       3
#define UF_CUTTER_TYPE_GROOVE     4
#define UF_CUTTER_TYPE_THREAD     5
#define UF_CUTTER_TYPE_BARREL     7
#define UF_CUTTER_TYPE_T          8
#define UF_CUTTER_TYPE_FORM       9
#define UF_CUTTER_TYPE_SOLID     11
#define UF_CUTTER_TYPE_LASER     12
#define UF_CUTTER_TYPE_SOFT      UF_CUTTER_TYPE_LASER

/**** Cutter subtypes *********/

/*** Subtypes valid for type UF_CUTTER_TYPE_MILL ****/
#define UF_CUTTER_SUBTYPE_MILL_5            1
#define UF_CUTTER_SUBTYPE_MILL_7            2
#define UF_CUTTER_SUBTYPE_MILL_10           3
#define UF_CUTTER_SUBTYPE_MILL_BALL         4
#define UF_CUTTER_SUBTYPE_MILL_CHAMFER      5
#define UF_CUTTER_SUBTYPE_MILL_SPHERICAL    6
/*** Subtypes valid for type UF_CUTTER_TYPE_DRILL ****/
#define UF_CUTTER_SUBTYPE_DRILL_STD         0
#define UF_CUTTER_SUBTYPE_DRILL_CENTER_BELL 1
#define UF_CUTTER_SUBTYPE_DRILL_COUNTERSINK 2
#define UF_CUTTER_SUBTYPE_DRILL_SPOT_FACE   3
#define UF_CUTTER_SUBTYPE_DRILL_SPOT_DRILL  4
#define UF_CUTTER_SUBTYPE_DRILL_BORE        5
#define UF_CUTTER_SUBTYPE_DRILL_REAM        6
#define UF_CUTTER_SUBTYPE_DRILL_COUNTERBORE 7
#define UF_CUTTER_SUBTYPE_DRILL_TAP         8
#define UF_CUTTER_SUBTYPE_DRILL_THREAD_MILL 10
#define UF_CUTTER_SUBTYPE_DRILL_STEP        12
/*** Subtypes valid for type UF_CUTTER_TYPE_TURN ****/
#define UF_CUTTER_SUBTYPE_TURN_STD          1
#define UF_CUTTER_SUBTYPE_TURN_BUTTON       2
#define UF_CUTTER_SUBTYPE_TURN_BORING_BAR   3
/*** Subtypes valid for type UF_CUTTER_TYPE_GROOVE ****/
#define UF_CUTTER_SUBTYPE_GROOVE_STD        1
#define UF_CUTTER_SUBTYPE_GROOVE_RING       2
#define UF_CUTTER_SUBTYPE_GROOVE_FNR        3
#define UF_CUTTER_SUBTYPE_GROOVE_USER       4
/*** Subtypes valid for type UF_CUTTER_TYPE_THREAD ****/
#define UF_CUTTER_SUBTYPE_THREAD_STD        1
#define UF_CUTTER_SUBTYPE_THREAD_TRAP       4

/*** Subtypes valid for type UF_CUTTER_TYPE_SOLID ****/
#define UF_CUTTER_SUBTYPE_GENERIC           0
#define UF_CUTTER_SUBTYPE_PROBE             1

/*** Subtypes valid for type UF_CUTTER_TYPE_SOFT ****/
#define UF_CUTTER_SUBTYPE_STD_LASER         0
#define UF_CUTTER_SUBTYPE_COAXIAL_LASER     1
#define UF_CUTTER_SUBTYPE_LASER             UF_CUTTER_SUBTYPE_STD_LASER

/* Defines for TURN CUTTER inserttypes */
#define UF_TURN_INSERTTYPE_PARALLEL_85 0  /* ISO A              */
#define UF_TURN_INSERTTYPE_PARALLEL_82 1  /* ISO B              */
#define UF_TURN_INSERTTYPE_DIAMOND_80  2  /* ISO C              */
#define UF_TURN_INSERTTYPE_DIAMOND_100 3  /* ISO C turned 90deg */
#define UF_TURN_INSERTTYPE_DIAMOND_55  4  /* ISO D              */
#define UF_TURN_INSERTTYPE_DIAMOND_75  5  /* ISO E              */
#define UF_TURN_INSERTTYPE_HEXAGON     6  /* ISO H              */
#define UF_TURN_INSERTTYPE_PARALLEL_55 7  /* ISO K              */
#define UF_TURN_INSERTTYPE_RECTANGLE   8  /* ISO L              */
#define UF_TURN_INSERTTYPE_DIAMOND_86  9  /* ISO M              */
#define UF_TURN_INSERTTYPE_OCTAGON     10 /* ISO O              */
#define UF_TURN_INSERTTYPE_PENTAGON    11 /* ISO P              */
#define UF_TURN_INSERTTYPE_ROUND       12 /* ISO R              */
#define UF_TURN_INSERTTYPE_SQUARE      13 /* ISO S              */
#define UF_TURN_INSERTTYPE_TRIANGLE    14 /* ISO T              */
#define UF_TURN_INSERTTYPE_DIAMOND_35  15 /* ISO V              */
#define UF_TURN_INSERTTYPE_TRIGON      16 /* ISO W              */
#define UF_TURN_INSERTTYPE_USER        17 /* User defined       */

#define UF_TURN_INSERTTYPE_GRV_STD      0 /* Standard grooving tool */
#define UF_TURN_INSERTTYPE_GRV_FNR      1 /* Full nose radius grooving tool */
#define UF_TURN_INSERTTYPE_GRV_RTJ      2 /* Ring type joint grooving tool */
#define UF_TURN_INSERTTYPE_GRV_USER     3 /* User defined grooving tool */

#define UF_TURN_INSERTTYPE_THREAD_STD   0 /* Standard threading tool */
#define UF_TURN_INSERTTYPE_THREAD_TRAP  1 /* Trapezoidal threading tool */

/* Defines for TURN CUTTER thickness types */
#define UF_TURN_THICKNESS_TYPE_01    0
#define UF_TURN_THICKNESS_TYPE_T1    1
#define UF_TURN_THICKNESS_TYPE_02    2
#define UF_TURN_THICKNESS_TYPE_T2    3
#define UF_TURN_THICKNESS_TYPE_03    4
#define UF_TURN_THICKNESS_TYPE_T3    5
#define UF_TURN_THICKNESS_TYPE_04    6
#define UF_TURN_THICKNESS_TYPE_05    7
#define UF_TURN_THICKNESS_TYPE_06    8
#define UF_TURN_THICKNESS_TYPE_07    9
#define UF_TURN_THICKNESS_TYPE_09   10
#define UF_TURN_THICKNESS_TYPE_11   11
#define UF_TURN_THICKNESS_TYPE_12   12
#define UF_TURN_THICKNESS_TYPE_USER 13

/* Defines for TURN CUTTER relief angle types */
#define UF_TURN_RELIEF_ANGLE_TYPE_A 0    /* A (3)     */
#define UF_TURN_RELIEF_ANGLE_TYPE_B 1    /* B (5)     */
#define UF_TURN_RELIEF_ANGLE_TYPE_C 2    /* C (7)     */
#define UF_TURN_RELIEF_ANGLE_TYPE_D 3    /* D (15)    */
#define UF_TURN_RELIEF_ANGLE_TYPE_E 4    /* E (20)    */
#define UF_TURN_RELIEF_ANGLE_TYPE_F 5    /* F (25)    */
#define UF_TURN_RELIEF_ANGLE_TYPE_G 6    /* G (30)    */
#define UF_TURN_RELIEF_ANGLE_TYPE_N 7    /* N (0)     */
#define UF_TURN_RELIEF_ANGLE_TYPE_P 8    /* P (11)    */
#define UF_TURN_RELIEF_ANGLE_TYPE_O 9    /* O (other) */


/* Defines for TURN CUTTER insert position types */

/* If the insert position is topside,
   the spindle have to rotate in clockwise direction,
   if the tool works above the centerline */
#define UF_TURN_INSERT_POSITION_TYPE_TOPSIDE   1

/* If the insert position is underside,
   the spindle have to rotate in counterclockwise direction,
   if the tool works above the centerline */
#define UF_TURN_INSERT_POSITION_TYPE_UNDERSIDE 2

/*
| Integral constants for tracking point location on a turning cutter
|
|                           Y
|                           ^
|                           |
|                           |
|              TL 2      TM 6         1 TR
|                  x--------x--------x
|                  |        |        |
|                  |        |        |
|              ML 7|     MM 9        |5 MR
|                  x--------x--------x--------->X
|                  |        |        |
|                  |        |        |
|                  |        |        |
|                  x--------x--------x
|              BL 3      BM 8         4 BR
|
| Abbreviations: T = Top, M = Middle, B = Bottom, L = Left, R = Right
*/

#define UF_TURN_CUTTER_TRACKING_POINT_TL  2
#define UF_TURN_CUTTER_TRACKING_POINT_TM  6
#define UF_TURN_CUTTER_TRACKING_POINT_TR  1
#define UF_TURN_CUTTER_TRACKING_POINT_ML  7
#define UF_TURN_CUTTER_TRACKING_POINT_MM  9
#define UF_TURN_CUTTER_TRACKING_POINT_MR  5
#define UF_TURN_CUTTER_TRACKING_POINT_BL  3
#define UF_TURN_CUTTER_TRACKING_POINT_BM  8
#define UF_TURN_CUTTER_TRACKING_POINT_BR  4


/***************************** Public Typedefs ********************************/

/*  tracking point data structure for a Milling Cutter tracking point         */
struct UF_CUTTER_tracking_point_data_s
{
    double diameter;            /* The output diameter of the point */
    double distance;            /* The distance of the point along the tool axis */
    double zoff;                /* The postprocessor Z offset of the point */
    int adjust;                 /* The adjust register to use with this point */
    int cutcom;                 /* The cutcom register to use with this point */
    int zoff_status;            /* The active/inactive status of the Z offset */
    int adjust_status;          /* The active/inactive status of the adjust register */
    int cutcom_status;          /* The active/inactive status of the cutcom register */
    char name[ UF_OBJ_NAME_BUFSIZE ];  /* The name of the tracking point */
};
typedef struct UF_CUTTER_tracking_point_data_s
               UF_CUTTER_tracking_point_data_t, *UF_CUTTER_tracking_point_data_p_t;

/*  tracking point data structure for a Turning Cutter tracking point         */
struct UF_CUTTER_turn_tracking_point_data_s
{
    double tlangl;              /* The tool angle of the point */
    double radius;              /* The radius value of the point */
    double xoff;                /* The postprocessor X offset of the point */
    double yoff;                /* The postprocessor Y offset of the point */
    int adjust;                 /* The adjust register to use with this point */
    int cutcom;                 /* The cutcom register to use with this point */
    int radiusid;               /* The radius id of this point */
    int cluster;                /* The P value of this point */
    char name[ UF_OBJ_NAME_BUFSIZE ];  /* The name of the tracking point */
};
typedef struct UF_CUTTER_turn_tracking_point_data_s
               UF_CUTTER_turn_tracking_point_data_t, *UF_CUTTER_turn_tracking_point_data_p_t;

/*
  Data structure to hold parameters for a holder section

*/
struct UF_CUTTER_holder_section_s
{
    double diameter;  /*  diameter of the cylindrical section  */
    double length;    /*  height of the cylindrical section  */
    double taper;     /*  taper angle of the cylindrical section in radians  */
    double corner;    /*  corner radius at bottom of section  */
};
typedef struct UF_CUTTER_holder_section_s
               UF_CUTTER_holder_section_t, *UF_CUTTER_holder_section_p_t;

/************************* Public Function Definitions ************************/


/*****************************************************************************
 * This function retrieves a Cutter from the current Cutter Library (as
 * defined in cam_config.dat) and creates a NX Cutter Object based upon
 * the values received from the library.
 *
 * Environment : Internal  and  External
 * See Also:
 * History : Released in V16.0
 ****************************************************************************/
extern UFUN_CAMEXPORT int UF_CUTTER_retrieve
(
   const char   *libref,    /* <I> - the library reference of the desired
                             *     cutter. Can be gotten from a record
                             *     set or an existing NX object
                             */
   tag_t        *tool_tag   /* <O> - the NX object created as a result of the
                             *     retrieval
                             */
);

/*****************************************************************************
 * This function updates the data of an already existing Cutter from the current
 * Cutter Library (as defined in cam_config.dat).
 *
 * Environment : Internal  and  External
 * See Also:
 * History : Released in V18.0
 ****************************************************************************/
extern UFUN_CAMEXPORT int UF_CUTTER_update_from_lib
(
   tag_t        tool_tag   /* <I> - the NX object which shall be updated
                            *
                            */
);

/*****************************************************************************
 * This function creates a Cutter based upon the Cutter template object
 * specified. All parameters of the newly created Cutter are derived from
 * the specified Cutter template object.
 *
 * Environment : Internal  and  External
 * See Also:
 * History : Released in V16.0
 ****************************************************************************/
extern UFUN_CAMEXPORT int UF_CUTTER_create
(
   char    *type_name, /* <I> - the template type name of the desired Cutter
                        *       template object.
                        */
   char    *subtype_name, /* <I> - the template subtype name of the desired
                           *       Cutter template object.
                           */
   tag_t   *new_object /* <O> - the tag of the newly created Cutter object */
);
extern UFUN_CAMEXPORT int UF_CUTTER_ask_type_and_subtype(
tag_t object_id ,/* <I>
                 Object identifier of CUTTER
                 */
int * type ,     /* <O>
                 CUTTER Type
                 */
int * subtype    /* <O>
                 CUTTER Subtype
                */
);

/***************************************************************
 *   Create a new tracking point and add it to the input Cutter.
 *
 * Return :
 * UF_CAM_ERROR_TAG_NOT_CORRECT_TYPE
 *  The input tag is not a cutter
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * History: Released in NX2.0
 *************************************************************/
 extern UFUN_CAMEXPORT int UF_CUTTER_create_tracking_point
(
    tag_t      object_tag,                  /* <I> the parent of the point */
    UF_CUTTER_tracking_point_data_t  *data  /* <I> the data of the point */
);

/***************************************************************
 *   Create a new turn tracking point and add it to the input Cutter.
 *
 * Return :
 * UF_CAM_ERROR_TAG_NOT_CORRECT_TYPE
 *  The input tag is not a cutter
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * History: Released in NX5.0
 *************************************************************/
 extern UFUN_CAMEXPORT int UF_CUTTER_create_turn_tracking_point
(
    tag_t      object_tag,                  /* <I> the parent of the point */
    UF_CUTTER_turn_tracking_point_data_t  *data  /* <I> the data of the point */
);

/***************************************************************
 *   Query the number of tracking points in the Cutter.
 *
 *  Return :
 * UF_CAM_ERROR_TAG_NOT_CORRECT_TYPE
 *  The input tag is not a cutter
 *
 * Environment: Internal  and  External
 *
 * See Also:
 *    UF_CUTTER_ask_tracking_point_data
 *
 * History: Released in NX2.0
 *************************************************************/
extern UFUN_CAMEXPORT int UF_CUTTER_ask_tracking_point_count
(
    tag_t  object_tag,  /* <I> the parent object of the points  */
    int *count          /* <O> the number of tracking points */
);

/***************************************************************
 *   Query the tracking point data for a cutter.
 *
 * Return :
 * UF_CAM_ERROR_TAG_NOT_CORRECT_TYPE
 *  The input tag is not a cutter
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * History: Released in NX2.0
 *************************************************************/
extern UFUN_CAMEXPORT int UF_CUTTER_ask_tracking_point_data
(
    tag_t  object_tag,              /*  <I> the parent of the point */
    int  *count,                    /*  <O> number of tracking points  */
    UF_CUTTER_tracking_point_data_t  ***data  /* <OF,len:count> count
                                              the data for the points */
);

/***************************************************************
 *   Query the turn tracking point data for a cutter.
 *
 * Return :
 * UF_CAM_ERROR_TAG_NOT_CORRECT_TYPE
 *  The input tag is not a cutter
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * History: Released in NX5.0
 *************************************************************/
extern UFUN_CAMEXPORT int UF_CUTTER_ask_turn_tracking_point_data
(
    tag_t  object_tag,              /*  <I> the parent of the point */
    int  *count,                    /*  <O> number of tracking points  */
    UF_CUTTER_turn_tracking_point_data_t  ***data  /* <OF,len:count> count
                                              the data for the points */
);

/***************************************************************
 *   Modify the tracking point data for a specified point.
 *
 * Return :
 * UF_CAM_ERROR_TAG_NOT_CORRECT_TYPE
 *  The input tag is not a cutter
 * UF_CAM_ERROR_INVALID_INDEX
 *  No tracking point with this index exists in the cutter.
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * History: Released in NX2.0
 *************************************************************/
extern UFUN_CAMEXPORT int UF_CUTTER_set_tracking_point_data
(
    tag_t  object_tag,          /* <I> the parent object of the point */
    int  index,                 /* <I> index of tracking point in parent (from 0 to
                                        the number of tracking points - 1)  */
    UF_CUTTER_tracking_point_data_t *data /* <I> the modified data of the point */
);

/***************************************************************
 *   Modify the turn tracking point data for a specified point.
 *
 * Return :
 * UF_CAM_ERROR_TAG_NOT_CORRECT_TYPE
 *  The input tag is not a cutter
 * UF_CAM_ERROR_INVALID_INDEX
 *  No turn tracking point with this index exists in the cutter.
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * History: Released in NX2.0
 *************************************************************/
extern UFUN_CAMEXPORT int UF_CUTTER_set_turn_tracking_point_data
(
    tag_t  object_tag,          /* <I> the parent object of the point */
    int  index,                 /* <I> index of tracking point in parent (from 0 to
                                        the number of tracking points - 1)  */
    UF_CUTTER_turn_tracking_point_data_t *data /* <I> the modified data of the point */
);

/***************************************************************
 *   Delete a specified tracking point from the specified cutter.
 *
 * Return :
 * UF_CAM_ERROR_TAG_NOT_CORRECT_TYPE
 *  The input tag is not a cutter
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * History: Released in NX2.0
 *************************************************************/
extern UFUN_CAMEXPORT int UF_CUTTER_delete_tracking_point
(
    tag_t  cutter_tag,  /*  <I> the parent cutter of the point */
    int  index          /*  <I> index of tracking point in parent (from 0 to the
                                number of tracking points -1)  */
);

/***************************************************************
 *   Create a new holder section and append it to the holder definition
 *
 * Return :
 * UF_CAM_ERROR_TAG_NOT_CORRECT_TYPE
 *  The input tag is not a cutter
 *    UF_CAM_ERROR_INVALID_RADIUS
 *    UF_CAM_ERROR_INVALID_DIAMETER
 *    UF_CAM_ERROR_INVALID_LENGTH
 *    UF_CAM_ERROR_INVALID_TAPER
 *          The input structure contains invalid data
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * History: Released in NX2.0
 *************************************************************/
 extern UFUN_CAMEXPORT int UF_CUTTER_create_holder_section
(
    tag_t  object_tag,                  /* <I> the tag of the cutter */
    UF_CUTTER_holder_section_t  *data   /* <I> the data of the section */
);

/***************************************************************
 *   Query a cutter for the number of cylindrical sections defining the holder
 *
 * Return :
 * UF_CAM_ERROR_TAG_NOT_CORRECT_TYPE
 *  The input tag is not a cutter
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * History: Released in NX2.0
 *************************************************************/
extern UFUN_CAMEXPORT int UF_CUTTER_ask_section_count
(
    tag_t  object_tag,  /* <I> the tag of the cutter  */
    int *count          /* <O> the number of cylindrical sections */
);

/***************************************************************
 *   Query a cutter for the data of a tool cylindrical section holder
 *
 * Return :
 * UF_CAM_ERROR_TAG_NOT_CORRECT_TYPE
 *  The input tag is not a cutter
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * History: Released in NX2.0
 *************************************************************/
extern UFUN_CAMEXPORT int UF_CUTTER_ask_holder_data
(
    tag_t  object_tag,    /*  <I> the tag of the cutter  */
    int  *count,          /*  <O> number of holder sections  */
    UF_CUTTER_holder_section_t  ***data  /*  <OF,len:count> count
                                            array of structure pointers
                                            for each cylindrical section  */
);

/***************************************************************
 *   Modify the data for a specific tool cylindrical section
 *
 * Return :
 * UF_CAM_ERROR_TAG_NOT_CORRECT_TYPE
 *  The input tag is not a cutter
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * History: Released in NX2.0
 *************************************************************/
extern UFUN_CAMEXPORT int UF_CUTTER_edit_holder_section
(
    tag_t  object_tag,  /*  <I> the tag of the cutter  */
    int  index,         /*  <I> index to desired section to modify  */
    UF_CUTTER_holder_section_t *data  /* <I>  modified section data  */
);

/***************************************************************
 *   Delete a specific tool cylindrical section
 *
 * Return :
 * UF_CAM_ERROR_TAG_NOT_CORRECT_TYPE
 *  The input tag is not a cutter
 * UF_CAM_ERROR_INVALID_INDEX
 *  No holder section with this index exists in the cutter.
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * History: Released in NX2.0
 *************************************************************/
extern UFUN_CAMEXPORT int UF_CUTTER_delete_holder_section
(
    tag_t  object_tag,  /*  <I> the tag of the cutter  */
    int  index          /*  <I> index to desired section to delete  */
);

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif /* UF_CUTTER_H_INCLUDED */
