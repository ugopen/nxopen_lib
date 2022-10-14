/*****************************************************************************
             Copyright (c) 1998-2000 Unigraphics Solutions Inc.
                       Unpublished - All Rights Reserved                       



File description: 
    Open API modeling routines to create, edit and inquire about hollows.
*****************************************************************************/

#ifndef UF_MODL_HOLLOW_H_INCLUDED
#define UF_MODL_HOLLOW_H_INCLUDED


/***************************************************************************

  ***************************************************************************/

#include <uf_defs.h>
#include <uf_modl_types.h>
#include <libufun_exports.h>

#ifdef __cplusplus
extern "C" {
#endif

/*******************************************************************************
Edit a hollow feature.

Environment:Internal and External
See Also:
History: Originally released in V16.0
*******************************************************************************/
extern UFUNEXPORT int UF_MODL_edit_hollow(
tag_t  feature_id,        /* <I> Feature identifier for the hollow feature. */
int    type,              /* <I> Hollow type:
                                  1 = face
                                  2 = region
                                  3 = body
                           */
double tolerance,         /* <I> Tolerance */
char   *thickness,        /* <I> Default hollow thickness */
int    n_pierced_faces,   /* <I> Number of pierced or seed faces */
tag_t  *pierced_faces,    /* <I,len:n_pierced_faces>
                                 Array of pierced face identifiers */
int    n_boundary_faces,  /* <I> Number of boundary faces */
tag_t  *boundary_faces,   /* <I,len:n_boundary_faces>
                                 Array of boundary face identifiers */
int    n_offset_faces,    /* <I> Number of offset faces */
tag_t  *offset_faces,     /* <I,len:n_offset_faces>
                                 Array of offset face identifiers */
char   **offset_thickness /* <I,len:n_offset_faces>
                                 Array of offset thickness expressions */
);

/****************************************************************************
Creates a hollow feature using the input thickness and a list of faces to
hollow. The output of this function is the object identifier associated
to the hollow.

The thickness specified must be larger than the default modeling tolerance.
If a smaller thickness is desired than the modeling tolerance,
UF_MODL_create_variable_hollow may be used.

Environment: Internal  and  External
See Also: UF_MODL_create_variable_hollow
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_create_hollow(
char * thickness ,/* <I>
                  Hollow thickness.
                  */
uf_list_p_t faces ,/* <I>
                   List of faces to be hollow.
                   */
tag_t * feature_obj_id  /* <O>
                        Feature object identifier of created hollow
                        */
);

/********************************************************************
Gets the hollow parameters.

Environment: Internal  and  External
See Also:
History:
********************************************************************/
extern UFUNEXPORT int UF_MODL_ask_hollow_parms(
tag_t feature_obj_id ,/* <I>
                      A feature object identifier
                      */
int edit ,/* <I>
          This is an unused flag. It used to determine whether
          to return the right-hand side or both sides of an
          expression. Currently, both sides of an expression
          are returned.
          */
char ** thickness  /* <OF>
                   The offset from the faces.  This must be
                   freed by calling UF_free.
                   */
);

/*******************************************************************************
Create a variable hollow feature.

Environment:Internal and External
See Also:
History: Originally released in V16.0
*******************************************************************************/
extern UFUNEXPORT int UF_MODL_create_variable_hollow(
double tolerance,          /* <I> Tolerance  */
char   *thickness,         /* <I> Default thickness  */
int    n_pierced_faces,    /* <I> Number of pierced faces */
tag_t  *pierced_faces,     /* <I,len:n_pierced_faces>
                                  Array of pierced face identifiers. */
int    n_boundary_faces,   /* <I> Number of boundary faces */
tag_t  *boundary_faces,    /* <I,len:n_boundary_faces>
                                  Array of boundary face identifiers */
int    n_offset_faces,     /* <I> Number of offset faces */
tag_t  *offset_faces,      /* <I,len:n_offset_faces>
                                  Array of offset face identifiers */
char   **offset_thickness, /* <I,len:n_offset_faces>
                                  Array of offset thickness expressions */
tag_t  *feature_id         /* <O> Feature identifier */
);

/*******************************************************************************
Ask the data for a hollow feature.

Environment:Internal and External
See Also:
History: Originally released in V16.0
*******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_hollow_data(
tag_t   feature_id,       /* <I> Feature identifier             */
int     *type,            /* <I> Hollow type:
                                  1 = face
                                  2 = region
                                  3 = body
                           */
double  *tolerance,       /* <O> Tolerance.  */
char    **thickness,      /* <OF> Default thickness. This must be freed by
                                  calling UF_free.
                          */
int     *n_pierced_faces, /* <O> Number of pierced faces */
tag_t   **pierced_faces,  /* <OF,len:n_pierced_faces> n_pierced_faces
                          Array of pierced face identifiers.  This
                          array must be freed by calling UF_free.
                          */
int     *n_boundary_faces,/* <O> Number of boundary faces       */
tag_t   **boundary_faces, /* <OF,len:n_boundary_faces> n_boundary_faces
                          Array of boundary face identifers.  This
                          array must be freed by calling UF_free.
                          */
int     *n_offset_faces,  /* <O>  Number of offset faces */
tag_t   **offset_faces,   /* <OF,len:n_offset_faces> n_offset_faces
                          Array of offset face ids.  This array must
                          be freed by calling UF_free.
                          */
char    ***offset_thickness /* <OF,len:n_offset_faces> n_offset_faces
                            Array of offset thickness expressions.  This
                            array must be freed by calling UF_free_string_array.
                            */
);

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif     /* UF_MODL_HOLLOW_H_INCLUDED */
