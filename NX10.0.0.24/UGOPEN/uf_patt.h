/*******************************************************************************

             Copyright (c) 1998-2001 Unigraphics Solutions, Inc.
                       Unpublished - All Rights Reserved



File Description:

This file contains the subroutines that offer access to the NX
database.  Using the subroutines in this file, you can:
  . read current setting of pattern and shaded data archiving switches
  . set pattern and shaded data archiving switches
  . read pattern data
  . read pattern data as one pattern object
  . cycle pattern errors
  . create pattern point

CAUTION:
Open C API no longer supports saving pattern data in external mode. All of the
pattern routines are for internal Open C API. If you save a part containing
pattern data in external mode, the pattern data in that part is lost. To
regenerate the pattern data, save the part again with the "Save Pattern Data"
switch on. This switch is only supported in internal Open C API, interactive
NX, and GRIP.
 ****************************************************************************/

#ifndef UF_PATT_INCLUDED
#define UF_PATT_INCLUDED


/***************************************************************************

  ***************************************************************************/

#include <uf_defs.h>
#include <uf_cfi_types.h>
#include <uf_obj_types.h>
#include <libufun_exports.h>


#ifdef __cplusplus
extern "C" {
#endif

enum UF_PATT_switch_e {
    UF_PATT_off = 0,
    UF_PATT_on
};

typedef enum UF_PATT_switch_e UF_PATT_switch_t;
/****************************************************************************
Reads the pattern's data archiving switch.

Environment: Internal  and  External
See Also: UF_PATT_set_archiving
History: Original release was in V14.0.
*****************************************************************************/
extern UFUNEXPORT int UF_PATT_is_archiving_on(
logical * on  /* <O>
              Curent setting of the pattern data archiving switch
                 TRUE = switch is on
                 FALSE = switch is off
              */
);

/****************************************************************************
Sets the pattern's data archiving switch.
NOTE: Setting the pattern's data archiving switch to UF_PATT_off
also sets the Shaded Data Archiving switch to UF_PATT_off since
shaded data cannot be filed unless pattern data is filed. This is
consistent with the interactive functionality.

Environment: Internal  and  External
See Also: 
History: Original release was in V14.0.
*****************************************************************************/
extern UFUNEXPORT int UF_PATT_set_archiving(
UF_PATT_switch_t setting  /* <I>
                          Set the pattern's data archiving switch.
                            UF_PATT_on = set switch on
                            UF_PATT_off = set switch off
                          */
);

/**************************************************************************n
Reads the pattern's shaded data archiving switch.

Environment: Internal  and  External
See Also: 
History: Original release was in V14.0.
*****************************************************************************/
extern UFUNEXPORT int UF_PATT_is_shading_on(
logical * on  /* <O>
              Read the pattern's shaded data archiving switch
                   TRUE = switch is on
                   FALSE = switch is off
              */
);

/****************************************************************************
Set the pattern's shaded data archiving switch.
NOTE: Setting the pattern's shaded data archiving switch to
UF_PATT_on also sets the pattern's data archiving switch to
UF_PATT_on since shaded data cannot be filed unless pattern data is
filed. This is consistent with the interactive functionality.

Environment: Internal  and  External
See Also: 
History: Original release was in V14.0.
*****************************************************************************/
extern UFUNEXPORT int UF_PATT_set_shading(
UF_PATT_switch_t setting  /* <I>
                          Set the pattern's shaded data archiving switch.
                           UF_PATT_on = set switch on
                           UF_PATT_off = set switch off
                          */
);

/****************************************************************************
Creates a pattern point entity at the specified coordinates.

Environment: Internal  and  External
See Also: 
History: Original release was in V14.0.
 *****************************************************************************/
extern UFUNEXPORT int UF_PATT_create_point(
double coordinates[3] ,/* <I>
                       Coordinates of pattern point in model space
                       */
tag_t * tag  /* <O>
             Tag of newly created pattern point entity
             */
);

/****************************************************************************
Reads the pattern's display parameters.

Environment: Internal  and  External
See Also: 
History: Original release was in V14.0.
*****************************************************************************/
extern UFUNEXPORT int UF_PATT_ask_params(
tag_t tag ,/* <I>
           Tag of pattern entity (or NULL_TAG for global setting)
           */
UF_PATT_switch_t * origin_display ,/* <O>
                                   Origin marker display status
                                       UF_PATT_on = display status is on
                                       UF_PATT_off = display status is off
                                   */
UF_PATT_switch_t * max_min_display ,/* <O>
                                    Max/Min box display status
                                       UF_PATT_on = display status is on
                                       UF_PATT_off = display status  is off
                                    */
UF_PATT_switch_t * control_pt_display  /* <O>
                                       Control point display status
                                           UF_PATT_on = display status is on
                                           UF_PATT_off = display status is off
                                       */
);

/****************************************************************************
Set the pattern's display parameters.

Environment: Internal  and  External
See Also: 
History: Original release was in V14.0.
*****************************************************************************/
extern UFUNEXPORT int UF_PATT_set_params(
tag_t tag ,/* <I>
           Tag of pattern entity (or NULL_TAG for global setting)
           */
UF_PATT_switch_t origin_status ,/* <I>
                                Origin marker display status
                                  UF_PATT_on = display status is on
                                  UF_PATT_off = display status is off
                                */
UF_PATT_switch_t max_min_status ,/* <I>
                                 Max/Min box display status
                                   UF_PATT_on = display status is on
                                   UF_PATT_off = display status  is off
                                 */
UF_PATT_switch_t control_pt_status  /* <I>
                                    Control point display status
                                      UF_PATT_on = display status is on
                                      UF_PATT_off = display status is off
                                    */
);

/****************************************************************************
Read Pattern Data.  Returns pattern data.

Return:
       1 = np1 is not a pattern object

Environment: Internal  and  External
See Also:
History:
 ***************************************************************************/
extern UFUNEXPORT int uc5822(
tag_t  object,/* <I>
            Pattern Object Identifier
            */
char  name[ UF_OBJ_NAME_BUFSIZE ],/* <O>
            Pattern Name
            */
char  file_name[MAX_FSPEC_BUFSIZE],/* <O>
            Corresponding Archive Part File Name
            In NX Manager mode this will be an encoded part filename.
            */
int * view_dependent_status,/* <O>
           View Dependent Status
             0 = Model Object
             1 = View Dependent Entity
           */
int *  layer,/* <O>
            Layer
            */
int *  retrieval_status,/* <O>
            Retrieval Status
              0 = Good, Pattern Data is in Dynamic
                  Memory
              1 = Error Occurred During Pattern Data
                  Retrieval
            */
double transform_data[13]  /* <O>
              Pattern Information, rr7 is a 13 element array
              rr7[13]
              [0] - [8]       - Pattern Orientation Matrix
              [9]-[11]        - Pattern Origin
              [12]            - Pattern Scale
              */
); /* <WRAPAS:UF_PATT_ask_data> */

/*****************************************************************************
Retrieve pattern data as a single pattern object and return its identifier.

Return:
         Error Status
        < 0 =  Error
        0 = No Error
        1 = Part File Not Found
        3 = Part In Checkpoint Format
        5 = Part Failed Revision Check
        6 = No Pattern Data In Part
        14= Pattern data must be recreated
        20= Invalid Pattern Name
        21= Matrix Is Not Orthogonal
        22= Scale Must Be Positive

Environment: Internal  and  External
See Also:
History:
****************************************************************************/
extern UFUNEXPORT int uc5823(
char *  file_name,/* <I>
             Pattern File Specification
             */
char *  pattern_name,/* <I>
             Pattern Name
             " " = Part Name
             */
int  autoscale_option,/* <I>
          Autoscale Option
            1 = Yes - Autoscale If Metric/English
                          Conflict
            2 = No - Continue if Metric/English Conflict
          */
double transform_data[13] ,/* <I>
               Pattern Real Data, rp4[13]
                [0] - [8] Pattern Orientation Matrix
                [9] - [11] Pattern Origin
                [12]    Pattern Scale
               */
tag_t * pattern  /* <O>
             Pattern object identifier
             */
); /* <WRAPAS:UF_PATT_import> */

/*****************************************************************************
Cycles pattern errors.

Environment: Internal  and  External
See Also:
History:
****************************************************************************/
extern UFUNEXPORT int uc5824(
int * ia1 ,/* <I/O>
           On input the error found by the last call to this routine.
           If this routine has not been called yet, then set ia1 to 0
           to start cycling.  On output this will be the next error.
           The cycling is complete when a 0 is returned.
           */
char  cr2[ MAX_FSPEC_BUFSIZE ]  /* <O>
            Part Name Where Error Occurred
            */
); /* <WRAPAS:UF_PATT_cycle_errors> */

/* uf5891 read/set pattern display parameters - Internal and External
   Please replace calls to uc5891 with UF_PATT_ask_params and
   UF_PATT_set_params */
extern UFUNEXPORT void FTN(uf5891)(tag_t *np1, int *ip2, int *ia3);


#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY


#endif   /* END UF_PATT_INCLUDED */
