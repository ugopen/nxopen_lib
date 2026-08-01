/*******************************************************************************

                    Copyright (c) 1996-2003 Unigraphics Solutions Corporation
                             Unpublished - All rights reserved
*****************************************************************************



File Description:

Open API interface to boundaries.  The boundary routines in this file enable
you to:
 . Get boundary data
 . Create boundary data
******************************************************************************/
#ifndef UF_BOUND_H_INCLUDED
#define UF_BOUND_H_INCLUDED


/***************************************************************************

  ***************************************************************************/


#include <uf_defs.h>
#include <libufun_exports.h>


#ifdef __cplusplus
extern "C" {
#endif

/*
   **************************************************************************
   ***************************     Definitions    ***************************
   **************************************************************************
*/

#define UF_BOUND_ON  0
#define UF_BOUND_TANGENT_TO 1

#define UF_BOUND_NOT_SPECIFIED 0
#define UF_BOUND_SPECIFIED 1

#define UF_BOUND_CLOSED 0
#define UF_BOUND_OPEN 1

#define UF_BOUND_NOT_CONTIGUOUS 0
#define UF_BOUND_CONTIGUOUS 1

/*
   **************************************************************************
   ***************************     Structures     ***************************
   **************************************************************************
*/

struct UF_BOUND_tolerance_s{
    int tol_specified;                /* Tolerance specified flag:
                                         UF_BOUND_NOT_SPECIFIED - not specified
                                         UF_BOUND_SPECIFIED - specified
                                      */
    double into_tolerance;            /* The maximum allowed tolerance that
                                         the boundary may deviate from the
                                         defining curves into the part.
                                      */
    double out_tolerance;             /* The maximum allowed tolerance that
                                         the boundary may deviate from
                                         the defining curves away from the
                                         part.
                                      */
};

typedef struct UF_BOUND_tolerance_s UF_BOUND_tolerance_t,
               *UF_BOUND_tolerance_p_t;

struct UF_BOUND_object_s{
    tag_t object_tag;                 /* Curve that establishes the boundary.
                                      */
    int on_tangent_to_flag;           /* A parameter that describes the
                                         relationship of the cutter to the
                                         boundary for machining operation.
                                         UF_BOUND_ON: This indicates that
                                                the center line of the cutter
                                                is to remain on the specified
                                                curve during the machining
                                                operation.
                                         UF_BOUND_TANGENT_TO:  This indicates
                                                that the side of the cutter is
                                                to remain tangent to the
                                                specified curve during the
                                                machining operation.
                                       */
};

typedef struct UF_BOUND_object_s UF_BOUND_object_t, *UF_BOUND_object_p_t;

struct UF_BOUND_member_data_s{
    tag_t member_tag;    /* Tag of boundary member */
    int                  on_tangent_to_flag;/* On/Tangent to Flag
                                               UF_BOUND_ON or
                                               UF_BOUND_TANGENT_TO.
                                            */
    int                  contiguity_flag;   /* Contiguity Flag
                                               UF_BOUND_CONTIGUOUS or
                                               UF_BOUND_NOT_CONTIGUOUS.
                                            */
    double               parameter_range[2];/* Parameter Range */
    double               midpoint[2];       /* Midpoint */
    double               direction_vec[2];  /* Direction Vector */
};

typedef struct UF_BOUND_member_data_s UF_BOUND_member_data_t,
*UF_BOUND_member_data_p_t;

struct UF_BOUND_all_data_s{
    int                  num_members;       /* number of boundary members */
    int                  open_closed_flag;  /* flag to indicate if the
                                               boundary is open or closed
                                               UF_BOUND_OPEN or UF_BOUND_CLOSED
                                            */
    tag_t                plane_matrix;      /* tag of matrix of plane */
    double               minimum_distance;  /* distance from model space
                                               origin to plane */
    double               maxmin_box[4];     /* maximum and minimum box of
                                               the boundary */
    double               tolerance[2];      /* boundary tolerances
                                               tolerance[0]: The maximum allowed
                                               tolerance that the boundary may
                                               deviate from the defining
                                               curves into the part
                                               tolerance[1]: The maximum allowed
                                               tolerance that the boundary may
                                               deviate from the defining
                                               curves away from the part.
                                             */
    UF_BOUND_member_data_p_t  members_data;  /* <len:num_members> data of boundary members */
};

typedef struct UF_BOUND_all_data_s UF_BOUND_all_data_t, *UF_BOUND_all_data_p_t;

/*
   **************************************************************************
   ******************     Functions Relating to Boundary    *****************
   **************************************************************************
*/

/* ********************     Boundary Creation     ******************** */

/***************************************************************************
 *
 * Create a boundary object
 *
 *
 * Environment: Internal  and  External
 *
 * See Also:  UF_BOUND_object_s
 *            
 * History:
 ***************************************************************************/
extern UFUNEXPORT int UF_BOUND_create_boundary(
             int   open_closed_flag, /* <I> the boundary is a open
                                        or closed boundary.
                                        UF_BOUND_OPEN: the boundary is open.
                                        UF_BOUND_CLOSED: the boundary is closed.
                                     */
              tag_t view_tag,       /* <I> view tag for mapping on a drawing.
                                              NULL_TAG -- No particular view
                                                 to be specified
                                    */
              UF_BOUND_tolerance_t tol,    /* <I> specified boundary
                                              tolerance
                                           */
              unsigned int num_members,    /* <I> number of objects in the
                                              object list to construct the
                                              boundary
                                           */
              UF_BOUND_object_t object_list[], /* <I,len:num_members> object list to construct
                                              the boundary
                                           */
              tag_t     *bound_tag         /* <O> tag of created boundary
                                                object
                                           */
);


/***************************************************************************
*
*  Gets all data of a boundary.
*
*  Environment: Internal  and  External
*
*  See Also:  UF_BOUND_all_data_s
*              
*  History:
********************************************************************** */
extern UFUNEXPORT int UF_BOUND_ask_boundary_data(
    tag_t               boundary_tag,        /* <I>  the tag for the boundary
                                             */
    UF_BOUND_all_data_t *boundary_data       /* <OF> all of the data
                                                     associated with the
                                                     boundary. The function
                                                     will allocate memory for
                                                     members_data. This
                                                     memory should be freed
                                                     when no longer needed
                                                     by UF_free()
                                             */
);


/**********************************************************************
*
*  Queries the number of boundaries that a given object is in.
*
*  Environment: Internal  and  External
*
*  See Also:
*  History: Released in V16.0
************************************************************************/
extern UFUNEXPORT int UF_BOUND_ask_number_of_boundaries(
tag_t object,         /*<I> The object identifier to be queried.
                      */
int *no_of_members   /*<O> The number of boundaries that this object
                           is in.
                     */
);


#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif /* UF_BOUND_H_INCLUDED */
