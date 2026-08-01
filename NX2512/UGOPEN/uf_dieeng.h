/****************************************************************************

             Copyright (c) 1999,2002 Unigraphics Solutions Inc.
                             Unpublished - All rights reserved

  ***************************************************************************
  
  ***************************************************************************

   This include file contains the prototypes and descriptions of the
   Die NX Open API functions .

****************************************************************************/

#ifndef UF_DIEENG_H_INCLUDED
#define UF_DIEENG_H_INCLUDED

#include <uf_defs.h>
#include <uf_modl_types.h>
#include <libufun_die_exports.h>

#ifdef __cplusplus
extern "C" {
#endif


/*******************************************************************************
The following structures and enum

UF_DIEENG_opts_t
UF_DIE_binder_wrap_s

are utilized in the functions:

UF_DIE_create_binder_wrap
UF_DIE_edit_binder_wrap
UF_DIE_ask_binder_wrap
UF_DIE_free_binder_wrap

Environment: Internal  and  External

See Also: 

History: Originally released in V16.0
 ***************************************************************************/

typedef enum
{
    UF_DIEENG_BINDER_WRAP_FEATURE = 0,
    UF_DIEENG_ANALYSIS_GEOMETRY,
    UF_DIEENG_POINTS,
    UF_DIEENG_BOUNDARY,
    UF_DIEENG_SHEET
}UF_DIEENG_opts_t;


/*

    */

/* 
 */

/*
  The following structure is the main structure used in the binder wrap functions.
*/
struct UF_DIE_wrap_binder_s
{
    UF_DIEENG_opts_t    input_type;            /*
                                                  Type of data input to the function.
                                                  Can be either UF_DIEENG_POINTS,
                                                  UF_DIEENG_BOUNDARY, or UF_DIEENG_SHEET.
                                               */

    union
    {
        /* use the following structure when input_type == UF_DIEENG_POINTS */
        struct
        {
            int                  num_defining_points;   /*
                                                 Number of points included in points array.
                                                 a spline will be created through the points
                                                 to determine the binder outline.
                                               */
            tag_p_t              defining_points;       /*
                                                 Points used to create the binder outline.
                                               */
        }  points;

        /* use the following structure when input_type == UF_DIEENG_BOUNDARY */
        struct
        {
            UF_STRING_t    defining_string;    /*
                                                  A string of objects defining the binder
                                                  outline.  This structure can contain a
                                                  combination of curves, edges, curve features,
                                                  a single face, and sketches.  If features are
                                                  included then the curves produced by that
                                                  feature are input.  If sketches are included
                                                  then the curves in the sketch are input.  If a
                                                  single face is included then the edges of the
                                                  face are input.
                                               */
        }  string;

        /* use the following structure when input_type == UF_DIEENG_SHEET */
        struct
        {
            tag_t          sheet_body;          /*
                                                   Tag to a sheet body which will be approximated to
                                                   create the DIE_BINDER_WRAP feature.
                                                */
        }  sheet;

    }   defined_by;

    char*                           material_thickness; /*
                                                          Material thickness value as an expression.
                                                          (See "Notes" below.)
                                                        */
    double                          distance_tol; /*
                                                    Modeling distance tolerance.
                                                  */
    double                          angle_tol;  /*
                                                  Modeling angle tolerance.
                                                */
    UF_DIEENG_opts_t                output_sw;  /*
                                                  Switch to indicate what type of feature
                                                  to output.
                                                  UF_DIEENG_BINDER_WRAP_FEATURE - output the
                                                  smooth binder wrap feature.
                                                  UF_DIEENG_ANALYSIS_GEOMETRY - output the
                                                  sheet body containing the triangularization
                                                  of the binder wrap.
                                                */
};
typedef struct UF_DIE_wrap_binder_s
               UF_DIE_binder_wrap_t, *UF_DIE_binder_wrap_p_t;

/*
  NOTES:

  The value character strings in the above structure can be a numeric value (e.g., "25"),
  a fully defined expression (e.g., "p5  = 25"), an existing expression name (e.g., "p5"), or
  an expression string (e.g., "p5+p7"). If the fully defined expression exists then an error
  is returned. If the expression name does not exist an error is returned. In all other cases
  an expression is created. When this value is returned from UF_CURVE_ask_trim, the character
  string is a fully defined expression (e.g., "p5=25").
*/

/*

*/



/****************************************************************************
Create an associative binder wrap feature or a non-associative analysis geometry
sheet body.

Environment: Internal  and  External

See Also: 

History: Originally released in V16.0
 ***************************************************************************/
extern UFUN_DIEEXPORT int UF_DIE_create_binder_wrap
(
    UF_DIE_binder_wrap_p_t  binder_wrap_info,     /* <I>
                                                     Information defining the binder
                                                     wrap.
                                                  */
    tag_t                   *binder_wrap_feature  /* <O>
                                                     DIE_BINDER_WRAP feature if output_sw
                                                     == UF_DIEENG_BINDER_WRAP_FEATURE.
                                                     UNPARAMETERIZED_FEATURE if output_sw
                                                     == UF_DIEENG_ANALYSIS_GEOMETRY
                                                  */
);

/****************************************************************************
Change the parameters of an associative binder wrap feature to the parameters
supplied

Environment: Internal  and  External

See Also: 

History: Originally released in V16.0
***************************************************************************/
extern UFUN_DIEEXPORT int UF_DIE_edit_binder_wrap
(
    tag_t                   binder_wrap_feature,   /* <I>
                                                      DIE_BINDER_WRAP feature whose parameters
                                                      are to be changed.
                                                   */
    UF_DIE_binder_wrap_p_t  uf_binder_wrap_info    /* <I>
                                                      Information defining the binder wrap
                                                      features desired parameters.
                                                   */
);
/****************************************************************************
Retrieve the current parameters of an associative binder wrap feature.

Environment: Internal  and  External

See Also: 

History: Originally released in V16.0
***************************************************************************/
extern UFUN_DIEEXPORT int UF_DIE_ask_binder_wrap
(
    tag_t                   binder_wrap_feature,   /* <I>
                                                      DIE_BINDER_WRAP feature whose parameters
                                                      are to be retrieved.
                                                   */
    UF_DIE_binder_wrap_p_t  uf_binder_wrap_info    /* <OF,free:UF_DIE_free_binder_wrap>
                                                      Information defining the binder wrap
                                                      features current parameters, the caller
                                                      should free allocated memory in this
                                                      structure by calling UF_DIE_free_binder_wrap.
                                                   */
);

/****************************************************************************
Free the memory within the UF_DIE_binder_wrap_p_t structure that was allocated
by a call to UF_DIE_ask_binder_wrap

Environment: Internal  and  External

See Also: 

History: Originally released in V16.0
***************************************************************************/

extern UFUN_DIEEXPORT int UF_DIE_free_binder_wrap
(
    UF_DIE_binder_wrap_p_t  uf_binder_wrap_info     /* <I>
                                                      Information defining the binder wrap
                                                      features current parameters that was
                                                      generated by a call to UF_DIE_ask_binder_wrap.
                                                    */
);

/****************************************************************************
The following function will provide the faces for the various tools.
The faces returned for the binder ring and the punch will be based upon the
last DIE_BINDER_RING feature.  If there is no DIE_BINDER_RING feature in
the part, no faces will be returned.  The faces returned for the die face
will be based upon the DIE_FACE feature within the same operation that
the last DIE_BINDER_RING exists in.  If there is no DIE_FACE feature, the
faces belonging to the DIE_OUTPUT feature that is a child of the
aforementioned DIE_BINDER_RING feature is returned.

Environment: Internal  and  External

See Also: 

History: Originally released in V19.0.1
***************************************************************************/
extern UFUN_DIEEXPORT int UF_DIE_ask_draw_faces
(
    int type_of_tool,      /* <I>    0 = binder ring,
                                1 = punch,
                                2 = die face */
    int *num_faces,    /* <O> number of faces for tool requested */
    tag_t **faces    /* <OF,len:num_faces> array of faces for tool requested */

);

/****************************************************************************
The following function will return the material descriptor tag and the
metal thickness of the part(s) that is being formed.  If no material
properties are connected to the part(s), the material type tag will be
NULL_TAG.  If there are more than one unique material property associated
to the part(s), the function will return one of the properties and the
error code DIE_MULT_MAT_PROPS.  If all the parts do not have the same
metal thickness, this parameter will return 0.

Environment: Internal  and  External

See Also: 

History: Originally released in V19.0.1
***************************************************************************/
extern UFUN_DIEEXPORT int UF_DIE_ask_material_properties
(
    double *metal_thickness,    /* <O> metal thickness of part */
    tag_t *material_type_tag    /* <O> Tag of the Material Descriptor associated to the part
                                   being formed*/
);

/****************************************************************************
This function searches the current work part for the existence of a DIE_LINEUP feature.
If one is found the function generates the DOL report and writes the information out
to the file name provided.  This file must not pre-exist.  If the file pre-exists the
error CFI_err_file_exists is returned.  If there is no DIE_LINEUP feature in the file,
the error DIE_LINEUP_NO_LINEUP is returned.

Environment: Internal  and  External

See Also: 

History: Originally released in NX2.0
***************************************************************************/
extern UFUN_DIEEXPORT int UF_DIEENG_create_dol_report_file
(
    const char   *report_file_name   /* <I> name of file to put report into. An error is
                                        generated if the file you specify already exists.
                                        If you specify a full pathname, then the file is
                                        created there. If you specify
                                        a simple file name, the file is created in the
                                        the TMP directory. */

);

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif /* UF_DIEENG_H_INCLUDED */
