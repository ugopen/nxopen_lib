/******************************************************************************
  
             Copyright (c) 1995-2003 Unigraphics Solutions, Inc.
                       Unpublished - All Rights Reserved                       

  
 ******************************************************************************
 *


File description:

      UF_DPUD provides the required functions and type definitions for 
      the creation of drive paths for Surface Contouring

      UF_DPUD is used when an operation uses the User Defined drive path
      method.  When setting up a User Defined drive path, the user must
      enter the name of an environment variable which points to a usable
      shared library.  The Surface Contouring processor expects a single
      entry point, dpud(), in this shared library to service
      all requests related to drive path generation.  The particular
      request type is identified by a 'purpose' variable.

      The UF program with the name dpud() must identify the
      purpose of the request and, accordingly, branch to the proper
      service routine.  

      The entry point function has the following typedef:

          extern int dpud ( char *param, int *status, int parm_len);

      The string 'param' contains the data which is communicated back and
      forth. To get access to this data, first cast the param to
      to UF_CAM_exit_id_t, then get the DPUD specific data using the
      function UF_DPUD_ask_dpud.

      With this data available, the UF program can service the requests.

      The following services are expected:
         1. Specify user parameters
            This request is made during operation editing through a
            dialog button.  Any parameters entered through this request
            must be maintained by the UF program.  To aid this maintenance,
            UF_DPUD provides access to the name of the calling operation.
                Available objects:
                     purpose
                     operation
         
         2. Specify tool axis parameters
            This request is also made during operation editing through a
            dialog button, when USER_DEFINED tool axis is selected (this
            option is only available when USER_DEFINED drive method has
            been selected previously.  Any parameters entered through this
            request must be maintained by the UF program.  To aid this
            maintenance, UF_DPUD provides access to the name of the
            calling operation.
                Available objects:
                     purpose
                     operation

         3. Specify projection vector parameters
            This request is also made during operation editing through a
            dialog button, when USER_DEFINED projection vector is selected
            (this option is only available when the USER_DEFINED drive method
            has been selected previously.  Any parameters entered through
            this request must be maintained by the UF program.  To aid this
            maintenance, UF_DPUD provides access to the name of the
            calling operation.
                Available objects:
                     purpose
                     operation

         4. Initialize the processor
            This request is made to allow the UF program to start up and
            initialize internal data as required.
                Available objects:
                     purpose
                     operation
                     tool axis option
                     tool axis
                     projection vector option
                     projection vector

         5. Set user data size
            Surface Contouring maintains several positions during processing.
            Each position has an associated drive position, the structure of
            which has been split into two parts, a system portion and a
            user portion.  These objects are allocated by the Surface 
            Contouring processor.  While the size system portion is known to 
            the processor, the user portion, of course, is not known.  The
            set user data size service is used to provide this size.  
            Please specify the size in number of bytes.
            For purposes of allignment, it is important that the user
            data does not contain any elements greater than double, which is
            currently the largest size used in the system portion.  
                Available objects:
                     purpose
                     operation
                     user data size

         6. Get next drive position
            This request is for the next available drive position along the
            drive path.  The UF program is responsible for generating 
            sufficiently many drive positions to satisfy any drive-path
            related tolerances.
                Available objects:
                     purpose
                     operation
                     tool axis option
                     tool axis
                     projection vector option
                     projection vector
                     drive position 0

         7. Get intermediate drive position
            This request is used when the direct path between two projected
            drive positions does not fall within the tolerance bands of the
            part geometry.  The UF program must supply a drive position at
            a given ratio (between 0.0 and 1.0) between the two specified
            drive positions.
                Available objects:
                     purpose
                     operation
                     tool axis option
                     tool axis
                     projection vector option
                     projection vector
                     ratio
                     drive position 0
                     drive position 1
                     drive position 2

         8. Rewind
            This request is used to reset the drive path processor back to
            the beginning.  In other words, after a rewind request, the next
            drive position generated with be the first drive position in the
            drive path.
                Available objects:
                     purpose
                     operation

         9. Stop the processor
            When tool path generation is completed, or when the system 
            otherwise is interrupted (such as if a user abort is generated),
            this request is generated to allow the UF program to free any
            allocated internal memory and perform any other required
            cleanup activities.
                Available objects:
                     purpose
                     operation
            

 *****************************************************************************/

/* Do not process this file again if already included */
#ifndef UF_DPUD_H_INCLUDED
#define UF_DPUD_H_INCLUDED


/***************************************************************************

  ***************************************************************************/


/**************************************************************************
 *
 *   Include files necessary for UF_DPUD definition
 *
 **************************************************************************/

#include <uf_defs.h>
#include <uf_cam.h>
#include <uf_oper.h>
#include <uf_drpos.h>
#include <libufun_cam_exports.h>

/****************************************************************************

  *************************************************************************/
#define ERROR_UF_DPUD_base     1375000

#ifdef __cplusplus
extern "C" {
#endif

/**************************************************************************
 *
 *    UF_DPUD data definitions (#defines, enums, typedefs, etc.)
 *
 **************************************************************************/
 
/* UF_DPUD_id_t is the identifier for referring to a UF_DPUD */
typedef void   *UF_DPUD_id_t;


/* UF_DPUD error codes */

/* This function is not available for the current request */
#define UF_DPUD_FUN_NOT_AVAIL           ERROR_UF_DPUD_base+0  

/* A tool axis is provided in the DPUD object only if it is constant */
#define UF_DPUD_TAXIS_NOT_CONSTANT      ERROR_UF_DPUD_base+1

/* A projection vector is provided in the DPUD object only if it is constant */
#define UF_DPUD_PROJ_NOT_CONSTANT       ERROR_UF_DPUD_base+2


/* UF_DPUD_purpose indicates the purpose for which the user function
   request is being made from the Surface Contouring Drive Path Processor */
enum UF_DPUD_purpose_e
    {
    UF_DPUD_USER_PARAMS,       /* Specify user parameters */
    UF_DPUD_TAXIS_PARAMS,      /* Specify tool axis parameters */
    UF_DPUD_PROJ_PARAMS,       /* Specify projection vector parameters */
    UF_DPUD_INIT_PROCESSOR,    /* Initialize the UFUNC processor */
    UF_DPUD_GET_USER_DATA_SIZE,/* Get size of user data for drive positions */
    UF_DPUD_GET_NEXT,          /* Get the next drive position */
    UF_DPUD_GET_INTERMEDIATE,  /* Get an intermediate drive position */
    UF_DPUD_REWIND,            /* Rewind the drive path */
    UF_DPUD_STOP_PROCESSOR     /* Deallocate memory used by processor */
    } ;
typedef enum UF_DPUD_purpose_e UF_DPUD_purpose_t;

/* UF_DPUD_taxis_option indicates how the tool axis is to be calculated.
   Note: use UF-specified tool axis only if variable */
enum UF_DPUD_taxis_option_e
    {
    UF_DPUD_TAXIS_CONSTANT,     /* Tool axis is constant and NX-specified */
    UF_DPUD_TAXIS_VARIABLE,     /* Tool axis is variable and NX-specified */
    UF_DPUD_TAXIS_USER_DEFINED  /* Tool axis is variable and UF-specified */
    } ;
typedef enum UF_DPUD_taxis_option_e UF_DPUD_taxis_option_t;

/* UF_DPUD_proj_option indicates how the projection vector is to be calculated.
   Note: use UF-specified projection vector only if variable */
enum UF_DPUD_proj_option_e
    {
    UF_DPUD_PROJ_CONSTANT,      /* Projection vector is constant and 
                                   NX-specified */
    UF_DPUD_PROJ_VARIABLE,      /* Projection vector is variable and 
                                   NX-specified */
    UF_DPUD_PROJ_USER_DEFINED   /* Projection vector is variable and 
                                   UF-specified */
    } ;
typedef enum UF_DPUD_proj_option_e UF_DPUD_proj_option_t;

/* UF_DPUD_drtype indicates the type of drive position which is being 
   generated.  Cut and stepover drive positions differ only in the 
   feedrate used for the projected motions.  The first drive position output 
   must be of type cut.  When a local lift is output, the processor will 
   generate a local retract/transfer/engage sequence based on the non-cutting 
   parameters of the requesting operation.  This sequence of non-cutting 
   motions will start at the previously projected drive position and ending at 
   the following projected drive position.  A local lift therefore must be
   bracketed by either cut or stepover positions, and there should be at least
   two cut or stepover positions between any two lifts.  Note that because the 
   tool is engaging to this position, the feedrate of the drive position 
   following a local lift will be ignored.  The stepover drive position type 
   acts just like a cut, but is assigned the stepover feedrate.
   The last drive position must be of type final lift.  This signals the
   Surface Contouring processor to stop and to generate a final retract
   sequence from the previously output cut or stepover position. 
*/
enum UF_DPUD_drtype_e
    {
    UF_DPUD_DRTYPE_NONE = 0,        /* Undefined drive position type */
    UF_DPUD_DRTYPE_CUT  = 1,        /* Normal cut position */
    UF_DPUD_DRTYPE_STEPOVER = 10,   /* Stepover cut position */
    UF_DPUD_DRTYPE_LOCAL_LIFT = 50, /* Output retract/engage sequence */
    UF_DPUD_DRTYPE_FINAL_LIFT = 51  /* Output final retract sequence */
    } ;
typedef enum UF_DPUD_drtype_e UF_DPUD_drtype_t;


/************************************************************************
 *
 *    UF_DPUD public function interface
 *
 ************************************************************************/


/*****************************************************************************
Return the UF_DPUD_id_t identifier which corresponds to the UF_CAM_exit_id_t 
that was passed to the User Exit from NX.

Environment: Internal  and  External
See Also:
History:
 *****************************************************************************/
extern UFUN_CAMEXPORT int UF_DPUD_ask_dpud(
UF_CAM_exit_id_t exit_id ,/* <I>
                          Identifier passed to User Exit from NX
                          */
UF_DPUD_id_t * dpud_id  /* <O>
                        Identifier of corresponding DPUD
                        */
);

/*************************************************************************
Return the identifier for the operation requesting the service.

Environment: Internal  and  External
See Also:
History:
 **************************************************************************/
extern UFUN_CAMEXPORT int UF_DPUD_ask_oper(
UF_DPUD_id_t dpud ,/* <I>
                   Identifier for a DPUD object
                   */
UF_OPER_id_t * oper  /* <O>
                     Identifier for an OPER object
                     */
);

/***************************************************************************
Return the purpose of this request.

Environment: Internal  and  External
See Also:
History:
 **************************************************************************/
extern UFUN_CAMEXPORT int UF_DPUD_ask_purpose(
UF_DPUD_id_t dpud ,/* <I>
                   Identifier for a DPUD object
                   */
UF_DPUD_purpose_t * purpose  /* <O>
                             The purpose of this request
                             */
);

/**************************************************************************
Determine the tool axis option chosen by the user in the NX dialog.

Environment: Internal  and  External
See Also:
History:
 **************************************************************************/
extern UFUN_CAMEXPORT int UF_DPUD_ask_taxis_option(
UF_DPUD_id_t dpud ,/* <I>
                   Identifier for a DPUD object
                   */
UF_DPUD_taxis_option_t * taxis_option  /* <O>
                                       The tool axis option chosen
                                       */
);
/**************************************************************************
Determine the tool axis chosen by the user in the NX dialog, if the
tool axis option is UF_DPUD_taxis_constant. For other options the
result of this call is undetermined.

Since the drive position tool axis in this case is automatically set by
the NX processor, there is no need to do it in the Open C API
program. This function is included only for the information it
provides.

Environment: Internal  and  External
See Also:
History:
 **************************************************************************/
extern UFUN_CAMEXPORT int UF_DPUD_ask_tool_axis(
UF_DPUD_id_t dpud ,/* <I>
                   Identifier for a DPUD object
                   */
double tool_axis[3]  /* <O>
                     The constant tool axis
                     */
);
/**************************************************************************
Determine the projection vector option chosen by the user in the NX
dialog.

Environment: Internal  and  External
See Also:
History:
 **************************************************************************/
extern UFUN_CAMEXPORT int UF_DPUD_ask_proj_option(
UF_DPUD_id_t dpud ,/* <I>
                   Identifier for a DPUD object
                   */
UF_DPUD_proj_option_t * proj_option  /* <O>
                                     the projection vector option chosen
                                     */
);
/**************************************************************************
Determine the projection vector chosen by the user in the NX dialog,
if the projection vector option is UF_DPUD_proj_constant. For other
options the result of this call is undetermined.

Since the drive position projection vector in this case is automatically
set by the NX processor, there is no need to do it in the Open C
API program.  This function is included only for the information it
provides.

Environment: Internal  and  External
See Also:
History:
 **************************************************************************/
extern UFUN_CAMEXPORT int UF_DPUD_ask_proj_vec(
UF_DPUD_id_t dpud ,/* <I>
                   Identifier for a DPUD object
                   */
double proj_vec[3]  /* <O>
                    The constant projection vector
                    */
);
/**************************************************************************
Set the size of the user data portion to be used for all drive postions.
This function is available only when the purpose of the request is
UF_DPUD_GET_USER_DATA_SIZE.

Environment: Internal  and  External
See Also:
History:
 **************************************************************************/
extern UFUN_CAMEXPORT int UF_DPUD_set_user_data_size(
UF_DPUD_id_t dpud ,/* <I>
                   Identifier for a DPUD object
                   */
int size  /* <I>
          Size of User data drive positions (bytes)
          */
);
/**************************************************************************
Returns the identifier of the requested drive position of this request.
This drive position is available only when the purpose of the request is
UF_DPUD_GET_NEXT or UF_DPUD_GET_INTERMEDIATE.

Environment: Internal  and  External
See Also:
History:
 **************************************************************************/
extern UFUN_CAMEXPORT int UF_DPUD_ask_drpos0(
UF_DPUD_id_t dpud ,/* <I>
                   Identifier for a DPUD object
                   */
UF_DRPOS_id_t * drpos  /* <O>
                       The drive postion of this request
                       */
);
/**************************************************************************
Return the identifier of the first input drive position of this request.
This drive position is available only when the purpose of the request is
UF_DPUD_GET_INTERMEDIATE.

Environment: Internal  and  External
See Also:
History:
 **************************************************************************/
extern UFUN_CAMEXPORT int UF_DPUD_ask_drpos1(
UF_DPUD_id_t dpud ,/* <I>
                   Identifier for a DPUD object
                   */
UF_DRPOS_id_t * drpos  /* <O>
                       First input drive position of this request
                       */
);
/**************************************************************************
Return the identifier of the second input drive position of this request.
This drive position is available only when the purpose of the request is
UF_DPUD_GET_INTERMEDIATE.

Environment: Internal  and  External
See Also:
History:
 **************************************************************************/
extern UFUN_CAMEXPORT int UF_DPUD_ask_drpos2(
UF_DPUD_id_t dpud ,/* <I>
                   Identifier for a DPUD object
                   */
UF_DRPOS_id_t * drpos  /* <O>
                       2nd input drive position of this request
                       */
);
/**************************************************************************
Returns the ratio at which an intermediate drive position must be
generated. The value of this ratio is between 0.0 and 1.0.  If ratio=
0.0, the Open C API program must return a copy of drpos2. Note:
while the parameterization of the drive path (used to associate the
ratio with a drive position) is not expected to equal the actual curve
length, it must be strictly monotonous and a continuous function of
the curve length.

This function is only available when the purpose of the request is
UF_DPUD_GET_INTERMEDIATE.

Environment: Internal  and  External
See Also:
History:
 **************************************************************************/
extern UFUN_CAMEXPORT int UF_DPUD_ask_ratio(
UF_DPUD_id_t dpud ,/* <I>
                   Identifier for a DPUD object
                   */
double* ratio  /* <O>
               The ratio for the intermediate point
               */
);

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif
