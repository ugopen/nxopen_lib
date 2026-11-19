/****************************************************************************

           Copyright (c) 1999-2023 Siemens
           Unpublished - All rights reserved

 File description:
          These routines are in the process of being removed from the Open API
          product.  Customers should use the designated replacement routines
          instead of the routines listed here.  Once a routine is placed
          here, it is eligible to be removed in the next release of Unigraphics.

****************************************************************************/

/*


*/

#ifndef UF_MODL_EXPRESSION_TYPES
#define UF_MODL_EXPRESSION_TYPES

/*  */
#define AT_MAX_TITLE_LEN 50
/*  */
#include <uf_defs.h>
#include <uf_curve.h>

/***************************************************************************

  ***************************************************************************/

#ifdef __cplusplus
extern "C" {
#endif

/*****************************************************************************/

/* The structure UF_MODL_dimension_data_s stores the data to create drafting
   dimension data for feature expressions.  The structure is filled by the
   function UF_MODL_get_dimension_data (see below ). */
struct UF_MODL_dimension_data_s
{
    int type;         /* Type of dimension  - 0 - Parallel
                                               1 - Diameter
                                               2- angular
                                               3- Radial
                                               4 - RPO
                                               */
    tag_t feature_tag;        /* The tag of the feature associated with the
                                 dimension */
    double value;             /* The value of the expression from which we
                                 create the dimension. */
    double first_point[3];    /* The absolute coordinates of objects used to
                                 create the dimension.  For a parallel
                                 dimension this is the first point necessary
                                 to create the dimension.  For a diameter or
                                 radial dimension this is the center of the
                                 arc from which we create the dimension. For
                                 an angular or RPO dimension????*/

    double second_point[3];   /* The second point necessary to create the
                                 parallel dimension. This is unused for the
                                 other types of dimensions. */
    double origin[3];         /* Origin for the dimension placement in
                                 absolute coordinates. */
    double start_angle;       /* Start angle for arc of radial dimensions in radians */
    double end_angle;         /* End angle for arc of radial dimensions in radians */
    tag_t csys_tag;           /* This is the coordinate system which defines
                                 the XY plane on which the dimension is
                                 created. */
    char* drf_txt;            /* Dimension text associated with the dimension.
                              */
    tag_t* top_array;         /* <len:num_top_array> Topological information associated with the
                                 feature (such as faces or edges) which should
                                 be used to customize the dimension creation by
                                 the user.  This array must be freed by the
                                 user by calling UF_free. */
    int num_top_array;        /* Number of topological entities returned */
    UF_CURVE_line_t first_line; /* Used only when the dimension is angular,
                                   this is the first line to be created for
                                   the angular dimension. */
    UF_CURVE_line_t second_line;  /* Used only when the dimension is angular,
                                     this is the Second line to be created for
                                     the angular dimension. */
};
typedef struct UF_MODL_dimension_data_s UF_MODL_dimension_data_t, *UF_MODL_dimension_data_p_t;

#ifdef __cplusplus
}
#endif

#endif /* UF_MODL_EXPRESSION_TYPES */
