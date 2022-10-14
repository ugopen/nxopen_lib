/*****************************************************************************
             Copyright (c) 1997-2000 Unigraphics Solutions, Inc.
                       Unpublished - All Rights Reserved



File Description:

 This file contains User functions for Model Checker's - element check.

List of User functions:

  1. UF_SF_mc_aspect_ratio
  2. UF_SF_mc_warp
  3. UF_SF_mc_skew
  4. UF_SF_mc_taper
  5. UF_SF_mc_twist
  6. UF_SF_mc_jacobian_ratio
  7. UF_SF_mc_jacobian_zero
  8. UF_SF_mc_tetra_angle
  9. UF_SF_mc_2d_angle
 10. UF_SF_mc_element_check
 11. UF_SF_mc_tet_collapse



******************************************************************************/

#ifndef  UF_SF_ELEMENT_CHECK__H_INCLUDED
#define  UF_SF_ELEMENT_CHECK__H_INCLUDED

#include <uf_defs.h>
#include <uf_disp.h>
#include <uf_sf_types.h>
#include <libufun_cae_exports.h>

#ifdef __cplusplus
extern "C" {
#endif

/* element check tolerance definition */
#ifndef CAET_ELEMENT_CHECK_TOL
#define CAET_ELEMENT_CHECK_TOL   0.05
#endif

#define CAET_MAX_ELEM_NODES        20

/* Model Checker related enums*/

enum UF_SF_mc_result_format_e
{
    UF_SF_mc_do_not_normalize_result,
    UF_SF_mc_normalize_result
} ;
typedef enum UF_SF_mc_result_format_e  UF_SF_mc_result_format_t,
                                      *UF_SF_mc_result_format_p_t ;

/* This enum is used for element check reporting */
enum UF_SFMC_result_e {
      SFMC_passed_check,                 /* check passed */
      SFMC_failed_check,                 /* at least one check failed */
      SFMC_error_with_check,             /* error occurred in operation */
      SFMC_check_does_not_apply          /* not applicable for given element */
};
typedef enum UF_SFMC_result_e  UF_SFMC_result_t;

/* The struct is for overall test reporting */
struct sCAET_mesh_test_case_s
{
    char  part_file[UF_SF_LANG_MAX_NAME_BUFSIZE];   /*  part file name  */
    char  solver[UF_SF_LANG_MAX_NAME_BUFSIZE];      /*  solver name     */
    UF_SF_atm_mesh_parameters_data_t test_param;   /*  mesh parameters */
};
typedef struct sCAET_mesh_test_case_s sCAET_mesh_test_case_t;

/* This struct is for the criteria used in elemet check */
struct sCAET_mesh_check_result_s
{
  int  elem_type;                  /* element type    */
  int  fail_count_aspect;          /* failed aspect ratio */
  int  fail_count_warp;            /* failed warp  */
  int  fail_count_taper;           /* failed taper */
  int  fail_count_skew;            /* failed skew  */
  int  fail_count_jacob_ratio;     /* failed Jacobian ratio */
  int  fail_count_jacob_zero;      /* failed Jacobian zero  */
  int  fail_count_min_angle;       /* failed mininum angle  */
  int  fail_count_max_angle;       /* failed maximum angle  */
  int  total_fail_count;           /* total failed elements */
};
typedef struct sCAET_mesh_check_result_s sCAET_mesh_check_result_t;

/**********************************************************************
 UF_SF_mc_aspect_ratio :

This function will check an element's aspect ratio value against
threshold value

Note: result_format is a dummy input on NX85

Environment: Internal & External

See Also:

History: released in v18.0
******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_mc_aspect_ratio (
UF_SF_element_type_t element_type ,/* <I> element type.  */
double abspos[3] ,/* <I> pointer to the node location in absolute
                coordinates.
                */
int node_count ,/* <I> number of nodes.  */
UF_SF_mc_result_format_t  result_format ,/* <I> format of results */
double  threshold , /* <I> threshold value */
double* aspect_ratio , /* <O> aspect ratio for the element.  */
UF_SFMC_result_t*  status_ptr /* <O> result status */
);


/******************************************************************************
  UF_SF_mc_warp:

  This function will check an element's warp against the threshold value

  Note: result_format is a dummy input on NX85

Environment: Internal

See Also:

History: released in v18.0
******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_mc_warp(
UF_SF_element_type_t element_type ,/* <I> element type.  */
double abspos[3] ,/* <I> pointer to the node location in absolute
                coordinates.
                */
int node_count ,/* <I> number of nodes.  */
UF_SF_mc_result_format_t  result_format ,/* <I> format of results */
double  threshold , /* <I> threshold value */
double* warp, /* <O> warp for the element.  */
UF_SFMC_result_t* status_ptr/* <O> result status */
);

/******************************************************************************
  UF_SF_mc_skew:

  This function will check an element's skew against the threshold value

  Note: result_format is a dummy input on NX85

 Environment: Internal  and  External

See Also:

History: released in v18.0
******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_mc_skew (
UF_SF_element_type_t element_type ,/* <I> element type.  */
double abspos[3] ,/* <I> pointer to the node location in absolute
                coordinates.
                */
int node_count ,/* <I> number of nodes.  */
UF_SF_mc_result_format_t  result_format ,/* <I> format of results */
double  threshold , /* <I> threshold value */
double* skew , /* <O> skew for the element.  */
UF_SFMC_result_t* status_ptr/* <O> result status */
);

/*****************************************************************************
  UF_SF_mc_taper:

  This function will check an element's taper against the threshold value

  Note: result_format is a dummy input on NX85

 Environment: Internal  and  External

See Also:

History: released in v18.0
******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_mc_taper (
UF_SF_element_type_t element_type ,/* <I> element type.  */
double abspos[3] ,/* <I>
                pointer to the node location in absolute
                coordinates.
                */
int node_count ,/* <I> number of nodes.  */
UF_SF_mc_result_format_t  result_format ,/* <I> format of results */
double  threshold , /* <I> threshold value */
double* taper, /* <O> taper for the element.  */
UF_SFMC_result_t* status_ptr /* <O> result status */
);

/*****************************************************************************

  UF_SF_mc_twist:

  This function will check an element's twist against the threshold value

  Note: result_format is a dummy input on NX85

 Environment: Internal  and  External

See Also:

History: released in v18.0
******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_mc_twist (
UF_SF_element_type_t element_type ,/* <I> element type.  */
double abspos[3] ,/* <I>
                pointer to the node location in absolute
                coordinates.
                */
int node_count ,/* <I> number of nodes.  */
UF_SF_mc_result_format_t  result_format ,/* <I> format of results */
double  threshold , /* <I>
                       threshold value
                    */
double* twist, /* <O>
               twist for the element.
               */
UF_SFMC_result_t* status_ptr /* <O>
                          result status
                          */
);

/****************************************************************************
  UF_SF_mc_jacobian_ratio:

  This function will check an element's jacobian ratio against the threshold
  value

  Note: result_format is a dummy input on NX85

 Environment: Internal  and  External

See Also:

History: released in v18.0
******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_mc_jacobian_ratio (
UF_SF_element_type_t     element_type,/* <I>
                element type.
                */
double abspos[3] ,/* <I>
                pointer to the node location in absolute
                coordinates.
                */
int node_count ,/* <I>
              number of nodes.
              */
UF_SF_mc_result_format_t results_format, /* <I>
                                      format of result
                                    */
double  threshold , /* <I>
                       threshold value
                   */
double* jacobian_ratio, /* <O>
                        The Elements jacobian ratio.
                        */
UF_SFMC_result_t*  status_ptr/* <O>
                          result status
                          */
);

/****************************************************************************
  UF_SF_mc_jacobian_zero:

  This function will check an element's jacobian zero against the
  threshold value

  Note: result_format is a dummy input on NX85

 Environment: Internal  and  External

See Also:

History: released in v18.0
******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_mc_jacobian_zero (
UF_SF_element_type_t     element_type,/* <I>
                element type.
                */
double abspos[3] ,/* <I>
                pointer to the node location in absolute
                coordinates.
                */
int node_count ,/* <I>
              number of nodes.
              */
UF_SF_mc_result_format_t results_format, /* <I>
                                      format of result
                                    */
double  threshold , /* <I>
                       threshold value
                   */
double* jacobian_zero, /* <O>
                      The Elements jacobian zero
                               */
UF_SFMC_result_t*  status_ptr/* <O>
                     result status
                      */
);



/****************************************************************************
  UF_SF_mc_tetra_angle:

  This function will calculate an element's tet angle

  Note: result_format is a dummy input on NX85

 Environment: Internal  and  External

See Also:

History: released in v18.0
******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_mc_tetra_angle(
double abspos[3] ,/* <I>
                pointer to the node location in absolute
                coordinates.
                */
int node_count ,/* <I>
              number of nodes.
              */
UF_SF_mc_result_format_t results_format, /* <I>
                                      format of result
                                    */
double  min_threshold , /* <I>
                       minimum threshold value
                   */
double  max_threshold , /* <I>
                       maximum threshold value
                   */
double* min_angle, /* <O>
                      The Elements minimim angle
                   */
double* max_angle, /* <O>
                      The Elements maximum angle
                   */
UF_SFMC_result_t*  min_status_ptr ,/* <O>
                                   minimum result status
                                 */
UF_SFMC_result_t*  max_status_ptr/* <O>
                                 maximum result status
                              */
);


/****************************************************************************
  UF_SF_mc_2d_angle :

  This function will calculate an element's  angle between sides

  Note: result_format is a dummy input on NX85

 Environment: Internal  and  External

See Also:

History: released in v18.0
******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_mc_2d_angle(
UF_SF_element_type_t     element_type,/* <I>
                element type.
                */
double abspos[3] ,/* <I>
                pointer to the node location in absolute
                coordinates.
                */
int node_count ,/* <I>
              number of nodes.
              */
UF_SF_mc_result_format_t results_format, /* <I>
                                      format of result
                                    */
double  min_threshold , /* <I>
                       minimum threshold value
                   */
double  max_threshold , /* <I>
                       maximum threshold value
                   */
double* min_angle, /* <O>
                      The Elements minimim angle
                   */
double* max_angle, /* <O>
                      The Elements maximum angle
                   */
UF_SFMC_result_t*  min_status_ptr ,/* <O>
                                   minimum result status
                                 */
UF_SFMC_result_t*  max_status_ptr/* <O>
                                 maximum result status
                              */
);

/****************************************************************************
  UF_SF_mc_element_check :

  This function will check an element's all qualities, such as warp, taper,
  skew, aspect ratio, jacobian ratio, against the threshold values .

 Environment: Internal & External

 See Also:

 History: released in v18.0
******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_mc_element_check( tag_t mesh_tag, /* <I>
                   tag of mesh which needs to be checked */
int *failed_elm_count /* <O> */
);

/******************************************************************************
  UF_SF_mc_tet_collapse

  This function will check elements' tet collapse. An element tet collapse is
  defined as the ratio of its longest edge to its shortest altitude. This
  check only applies to the Tet elements.

  Note: result_format is a dummy input on NX85

  Input:
      element_type             element type
      abs_node_coordinates[]   Array of  PNT3_t which contain absolute
                               node coordinates.

      node_cnt                 The number of nodes in an array.

      results_format           Indicates whether how results are to be
                               presented. (i.e normalized or not)

      threshold                threshold aspect_ratio value.

  Output:
      tet_collapse             The Elements tet collapse

      status_ptr               status whether passed or failed check.

  returns:
        int               = 0  - successful completion
                          > 0  - error
******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_mc_tet_collapse
(
    UF_SF_element_type_t      element_type,     /*<I>*/
    double                    abspos[3] ,          /*<I>*/
    int                       node_count ,      /*<I>*/
    UF_SF_mc_result_format_t  result_format ,   /*<I>*/
    double                    threshold,        /*<I>*/
    double                   *tet_collapse,     /*<O>*/
    UF_SFMC_result_t         *status_ptr        /*<O>*/
);


#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif  /*  UF_SF_ELEMENT_CHECK__H_INCLUDED */
