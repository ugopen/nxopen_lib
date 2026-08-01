/*****************************************************************************
 *            Copyright (c) 2003,2004 Unigraphics Solutions, Inc.
 *                      Unpublished - All Rights Reserved
 * File Name: uf_scop.h
 *
 * 
 *
 * File description:
 *    This file contains the Open C interface for accessing drive data
 *    for Surface Contouring operations
 *
 ******************************************************************************/
#ifndef UF_SCOP_H_INCLUDED
#define UF_SCOP_H_INCLUDED

/***************************** Include Files **********************************/
#include <uf.h>
#include <uf_defs.h>
#include <uf_cam_spec.h>
#include <uf_cam_errors.h>
#include <uf_drpos.h>
#include <libufun_cam_exports.h>

#include <uf_modl_types.h>

/******************************** Defines *************************/

#ifdef __cplusplus
extern "C" {
#endif

/***************************** Public Typedefs *******************************/

/*UF_SCOP_tx_data_type_t enumerates the different date types of given vectors*/
typedef enum
{
    UF_SCOP_TX_INTP_DATYPE_VECTOR = 0, /* used for surface or curve interpolation */
    UF_SCOP_TX_INTP_DATYPE_ANGLE_PS = 1, /* used for surface or curve interpolation */
    UF_SCOP_TX_INTP_DATYPE_ANGLE_DS = 2 /* used for surface interpolation */
} UF_SCOP_tx_intp_data_type_t;

/* UF_SCOP_tx_intp_type_t enumerates the different interpolation types of
 * given vectors */
typedef enum
{
    UF_SCOP_TX_INTP_LINEAR_METHOD = 0,
    UF_SCOP_TX_INTP_CUBIC_SPLINE_METHOD = 1,
    UF_SCOP_TX_INTP_SMOOTH_METHOD = 2
} UF_SCOP_tx_intp_method_t;

/* The application data for vector data */
struct UF_SCOP_vector_data_s
{
    double xyz[3]; /* the vector location */
    double ijk[3]; /* the vector direction, if data type is
    UF_SCOP_TX_INTP_DATYPE_VECTOR */
    double lead_tilt[2]; /* the vector lead angle and tilt angle,
                            if data type is
                            UF_SCOP_TX_INTP_DATYPE_ANGLE_DS or
                            UF_SCOP_TX_INTP_DATYPE_ANGLE_PS */

    logical is_corner_vector; /* If TRUE, this vector can not be deleted.
                                 The users must set a vector on each
                                 corner of the Drive surface. (Therefore,
                                 four vectors must be set to the Drive
                                 surface, one for each corner. Two vectors
                                 must be set to Curve/Point method.) The
                                 flags "is_corner_vector" of these vectors
                                 must be set to TRUE. */

    /* Notice: when set a new vector to Drive surface,
       if the geven vector location xyz is not exactly on the
       surface, the location xyz will be moved to the closest
       point along the given vector direction ijk, regardless
       which data type is used. If the user does not define
       valid vector direction ijk, a default vector (0,0,1)
       will be used. */
};

typedef struct UF_SCOP_vector_data_s UF_SCOP_vector_data_t,
                                   *UF_SCOP_vector_data_p_t;

/************************* Public Function Definitions ***********************/

/*****************************************************************************
 * This function asks the data type of the given interpolation vectors
 * for a Surface Contouring operation using the Surface Area drive
 * method and Interpolation tool axis. This function also returns the error
 * code. If return is not zero, error happens.
 *
 * Environment : Internal  and  External
 * See Also:
 * History : Released in NX3.0
 ****************************************************************************/
extern UFUN_CAMEXPORT int UF_SCOP_ask_tx_intp_data_type
(
    tag_t    object_tag,   /*  <I> The operation object  */
    UF_SCOP_tx_intp_data_type_t      *tx_intp_data_type
                           /*  <O> Data type of the given vector  */
);

/*****************************************************************************
 * This function sets the data type of the given interpolation vectors
 * for a Surface Contouring operation using the Surface Area drive
 * method and Interpolation tool axis. This function also returns the error
 * code. If return is not zero, error happens.
 *
 * Environment : Internal  and  External
 * See Also:
 * History : Released in NX3.0
 ****************************************************************************/
extern UFUN_CAMEXPORT int UF_SCOP_set_tx_intp_data_type
(
    tag_t    object_tag,   /*  <I> The operation object  */
    UF_SCOP_tx_intp_data_type_t      tx_intp_data_type
                           /*  <I> Data type of the given vector  */
);

/*****************************************************************************
 * This function asks the interpolation method of the given vectors
 * for a Surface Contouring operation using the Surface Area drive
 * method and Interpolation tool axis. This function also returns the error
 * code. If return is not zero, error happens.
 *
 * Environment : Internal  and  External
 * See Also:
 * History : Released in NX3.0
 ****************************************************************************/
extern UFUN_CAMEXPORT int UF_SCOP_ask_tx_intp_method
(
    tag_t    object_tag,   /*  <I> The operation object  */
    UF_SCOP_tx_intp_method_t      *tx_intp_method
                       /*  <O> Interpolation method of the given vectors */
);

/*****************************************************************************
 * This function sets the interpolation method of the given vectors
 * for a Surface Contouring operation using the Surface Area drive
 * method and Interpolation tool axis. This function also returns the error
 * code. If return is not zero, error happens.
 *
 * Environment : Internal  and  External
 * See Also:
 * History : Released in NX3.0
 ****************************************************************************/
extern UFUN_CAMEXPORT int UF_SCOP_set_tx_intp_method
(
    tag_t    object_tag,   /*  <I> The operation object  */
    UF_SCOP_tx_intp_method_t      tx_intp_method
                       /*  <I> Interpolation method of the given vectors */
);

/*****************************************************************************
 * This function asks the vector data for a Surface Contouring operation
 * using the Surface Area drive method and Interpolation tool axis.
 * This function also returns the error code.
 * If return is not zero, error happens.
 *
 * Environment : Internal  and  External
 * See Also:
 * History : Released in NX3.0
 ****************************************************************************/
extern UFUN_CAMEXPORT int UF_SCOP_ask_tx_intp_vector_data
(
    tag_t    object_tag,   /*  <I> The operation object  */
    int      *count,       /*  <O> The number of the vector data set */
    UF_SCOP_vector_data_t  **vector_data   /* <OF,len:count> the vector data list
                                            The data list must be freed
                                              by the user using UF_free() */
);

/*****************************************************************************
 * This function sets (add, modify, delete) the vector data for a Surface
 * Contouring operation using the Surface Area drive method and Interpolation
 * tool axis. This function also returns the error code. If return is not zero,
 * error happens. Please notice each corner on the Drive surface must be set
 * a vector. Otherwise, this function returns error.
 *
 * Environment : Internal  and  External
 * See Also:
 * History : Released in NX3.0
 ****************************************************************************/
extern UFUN_CAMEXPORT int UF_SCOP_set_tx_intp_vector_data
(
    tag_t    object_tag,   /*  <I> The operation object  */
    int      count,        /*  <I> Number of vector data set */
    UF_SCOP_vector_data_t  *vector_data,    /* <I> The vector data list */
    logical  *all_on_surface   /* <O> Flag to indicate whether all the
                                      locations (xyz) of the input vectors
                                      are on the surface. If it returns
                                      FALSE, some vectors are moved to the
                                      closest points on the surface. */
);

/*****************************************************************************
 * This function returns the number of rows and columns in the drive surface
 * grid for a Surface Contouring operation using the Surface Area drive
 * method.
 *
 * Environment : Internal  and  External
 * See Also:
 * History : Released in NX3.0
 ****************************************************************************/
extern UFUN_CAMEXPORT int UF_SCOP_ask_row_column_count
(
    tag_t    object_tag,   /*  <I> The operation object  */
    int      *num_row,     /*  <O> Number of rows in the drive surface grid  */
    int      *num_col      /*  <O> Number of columns in the grid  */
);

/*****************************************************************************
 * This function reads through the file of drive points in a Surface
 * Contouring operation using the Surface Area drive method and returns the
 * next position.  The data for the drive point is returned with respect to
 * the absolute coordinate system.
 *
 * Environment : Internal  and  External
 * See Also:
 * History : Released in NX3.0
 ****************************************************************************/
extern UFUN_CAMEXPORT int UF_SCOP_get_next_drive_point
(
    tag_t          object_tag,   /*  <I> The operation object  */
    UF_DRPOS_id_t  *drpos,       /*  <O> The next drive point  */
    int            *point_count  /*  <O> Number of points returned so far */
);

/*****************************************************************************
 * This function rewind the Drive Points of a Surface
 * Contouring operation to the beginning, such that the next call to
 * UF_SCOP_get_next_drive_point will output the very first Drive Point.
 * There is no need to call this function if UF_SCOP_get_next_drive_point
 * hasn't been called on the Surface Contouring operation.
 *
 * Environment : Internal  and  External
 * See Also: UF_SCOP_get_next_drive_point
 * History : Released in NX3.0
 ****************************************************************************/
extern UFUN_CAMEXPORT int UF_SCOP_rewind_drive_point
(
    tag_t          object_tag   /*  <I> The operation object  */
);

/***************************************************************************
 *
 * Displays UV grid directions on a surface.
 *
 * Environment: Internal Only
 *
 * See Also:
 * History: Released in NX3.0
********************************************************************** */
extern UFUN_CAMEXPORT int UF_SCOP_display_uv_dirs
(
    tag_t                 object_tag       /* <I> the parent object */
);

/***************************************************************************
 *
 * Evaluates a grid of surfaces at a input parameter position.
 * This function takes an optional entity to evaluate.  This will only be
 * used in the case where the parameter position is on a boundary point
 * between two surfaces and the tag is one of the two surfaces to evaluate.
 * If the parameter position is not on a boundary the entity will be ignored.
 * If the parameter position is on a boundary and the tag is not one of the
 * surfaces that contains the parameter position an error will be given.
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * History: Released in NX3.0
********************************************************************** */
extern UFUN_CAMEXPORT int UF_SCOP_eval_grid
(
    tag_t                 object_tag,      /* <I> */
    double                *uv,             /* <I> u,v parameter position */
    tag_t                 entity,          /* <I> entity to evaluate */
    UF_MODL_SRF_VALUE_p_t srf_value        /* <O> evaluation data structure */
);



#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif /* UF_SCOP_H_INCLUDED */

/***************************************************************************/


