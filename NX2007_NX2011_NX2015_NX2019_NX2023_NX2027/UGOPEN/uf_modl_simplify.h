/*****************************************************************************
             Copyright (c) 1998-2000 Unigraphics Solutions Inc.
                       Unpublished - All Rights Reserved                       



File description: 
    Open API modeling routines to create, edit and inquire about simplify feature and
    imprint.

*****************************************************************************/

#ifndef UF_MODL_SIMPLIFY_H_INCLUDED
#define UF_MODL_SIMPLIFY_H_INCLUDED


/***************************************************************************

  ***************************************************************************/

#include <uf_defs.h>
#include <uf_modl_types.h>
#include <libufun_exports.h>

#ifdef __cplusplus
extern "C" {
#endif

/******************************************************************************
Create a simplify feature according to the specified data.  The part
containing the body on which the feature is being applied will be fully
loaded if necessary.  <n_retained_faces> gives the number of faces on the
body after the simplify has been applied, <n_removed_faces> gives the
number of faces on the body removed when the simplify is applied.  If the
feature cannot be created because one or more faces could not be removed,
the ifail UF_MODL_SIMPL_HEAL_FAILED is returned, and the array
<failing_wound_edges> will contain the tags of the edges which could not be
healed.  UF_MODL_SIMPL_HEAL_FAILED is also returned if the simplified body
would have been invalid, in which case <n_failing_wound_edges> will be 0.  If
this or another ifail is returned, the feature is not created, and
<feature_tag> will be NULL_TAG.

Environment: Internal  and  External
See Also:
History:
*******************************************************************************/
extern UFUNEXPORT int UF_MODL_create_simplify
(
  UF_MODL_simpl_data_p_t simpl_parms,  /* <I>
                                       Parameters of the new simplify feature
                                       */
  tag_t    *feature_tag,        /* <O>
                                The feature created
                                */
  int   *n_failing_wound_edges, /* <O>
                                Number of edges of failing wounds
                                */
  tag_t **failing_wound_edges,  /* <OF,len:n_failing_wound_edges>
                                Array of edges of failing wounds.  This must
                                be freed by calling UF_free.
                                */
  int   *n_retained_faces,      /* <O>
                                Number of faces retained on the body
                                */
  int   *n_removed_faces        /* <O>
                                Number of faces removed from the body
                                */
);

/******************************************************************************
Edit an existing simplify feature according to the specified data, which
must have been created at an earlier timestamp than the feature.  Faces and
edges which are already parameters of the simplify feature, but which have
no associated geometry at present, are retained as its parameters after the
edit.  If the feature cannot be edited to the specified parameters because
one or more faces could not be removed, the ifail UF_MODL_SIMPL_HEAL_FAILED
is returned, and the array <failing_wound_edges> will contain the tags of
the edges which could not be healed (and must be freed using UF_free()).  It
is not possible to edit a simplify feature to be on a different body.

If the expression passed in as <max_hole_dia_expression> is different from
the previous expression used, and the old expression is an unused system
expression, the old expression will be deleted.  The expression's value can
be changed by the normal expression editing routines.

Environment: Internal and External
See Also:
History: This function was originally released in V15.0.
*******************************************************************************/
extern UFUNEXPORT int UF_MODL_edit_simplify_parms
(
  tag_t   feature_tag,    /* <I>
                          The simplify feature
                          */
  UF_MODL_simpl_data_p_t simpl_parms, /* <I>
                                      New parameters of the simplify feature
                                      */
  int *n_failing_wound_edges,  /* <O>
                               The number of failing wound edges
                               */
  tag_t **failing_wound_edges  /* <OF,len:n_failing_wound_edges>
                               Array of failing wound edges.  This must be
                               freed by calling UF_free.
                               */
);

/******************************************************************************
Returns the current parameters of the simplify feature.  Faces and edges
which are currently parameters of the simplify feature, but which have no
associated geometry at present, are not listed.

Environment: Internal and External
See Also: UF_MODL_create_simplify
          UF_MODL_edit_simplify_parms
          UF_MODL_preview_simplify
          UF_MODL_simpl_data_t
History: This function was originally released in V15.0.
******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_simplify_parms
(
  tag_t feature_tag, /* <I>
                     The simplify feature
                     */
  UF_MODL_simpl_data_p_t simpl_parms  /* <OF>
                                      The parameters of the simplify feature.
NEEDS A FREE ROUTINE
                                      */
);
/******************************************************************************
Preview a simplification feature.  This returns lists of the faces that
will be retained and removed if the feature is applied.  The arrays
retained_faces> and <removed_faces> are allocated, and should be freed
afterwards by the caller with UF_free().

If a path can be traced from any retained face to any removed face without
crossing the boundary, the ifail UF_MODL_SIMPL_FACE_NOT_REMOVED is returned.
In this case, for each such removed face an array of faces is returned.
This array gives a path between the removed face and an explicitly retained
face which does not cross any boundaries.  These arrays must be freed by
the caller with UF_free().  The retained and removed faces are still
returned.

If there are no leaks, <n_leaks> is 0, and <n_leak_faces> and <leak_faces>
are NULL.  Note that the preview cannot detect possible heal failures
which may show up when the simplify is applied.

If the simplification feature already exists, but is suppressed, this
routine will still give the correct results.  If it already exists and
is not suppressed, the removed faces will not be present in the solid,
and the result is unlikely to be useful.

Environment: Internal and External.
See Also: UF_MODL_create_simplify
          UF_MODL_edit_simplify_parms
          UF_MODL_ask_simplify_parms

          UF_MODL_simpl_data_t
History: This function was originally released in V15.0
*******************************************************************************/
extern UFUNEXPORT int UF_MODL_preview_simplify
(
  UF_MODL_simpl_data_p_t simpl_parms, /* <I>
                                      Parameters of the potential simplify
                                      feature
                                      */
  int *n_retained_faces, /* <O>
                         Number of faces that will be retained
                         */
  tag_t **retained_faces, /* <OF,len:n_retained_faces>
                          Faces that will be retained.  This array must be
                          freed by calling UF_free.
                          */
  int *n_removed_faces,  /* <O>
                         Number of faces that will be removed
                         */
  tag_t **removed_faces, /* <OF,len:n_removed_faces>
                         Faces that will be removed.  This array must be
                         freed by calling UF_free.
                         */
  int *n_leaks,  /* <O>
                 The number of leaks
                 */
  int **n_leak_faces, /* <OF,len:n_leaks>
                      The number of faces in the path of each leak.  This
                      array must be freed by calling UF_free.
                      */
  tag_t ***leak_faces /* <OF,len:n_leak_faces>
                      The faces in the path of each leak.  This array must be
                      freed by calling UF_free.
                      */
);

/******************************************************************************
Create an imprint feature according to the specified data (using
a face and a datum plane to define a loop of new edges on the solid).
The part containing the solid will be fully loaded if necessary.

Environment: Internal and External.
See Also:
History:
*******************************************************************************/
extern UFUNEXPORT int UF_MODL_create_impr_loop
(
  UF_MODL_imprint_loop_data_p_t    parms, /* <I>
                                          Parameters of the new imprint feature
                                          */
  tag_t *feature_tag /* <O>
                     The feature created
                     */
);
/******************************************************************************
Edit an existing imprint loop feature according to the specified data,
which must have been created at an earlier timestamp than the feature.
It is not possible to edit an imprint feature to be on a different body.
If the <imprint_face> parm or the <imprint_datum_plane> parm is NULL_TAG,
then the corresponding feature parm will be unchanged by the edit.

Environment: Internal and External
See Also:
History: This function was originally released in V15.0.
*******************************************************************************/
extern UFUNEXPORT int UF_MODL_edit_impr_loop_parms
(
  tag_t feature_tag, /* <I>
                     The imprint feature
                     */
  UF_MODL_imprint_loop_data_p_t parms /* <I>
                                      New parameters of the imprint feature
                                      */
);
/******************************************************************************
Returns the current parameters of the imprint loop feature.

Environment: Internal and External
See Also:
History: This function was originally released in V15.0.
*******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_impr_loop_parms
(
  tag_t feature_tag, /* <I>
                     The imprint feature
                     */
  UF_MODL_imprint_loop_data_p_t    parms  /* <O>
                                          The parameters of the imprint feature
                                          */
);

/******************************************************************************
Create an imprint feature according to the specified data (using an
explicit array of faces and a datum plane to define new edges on the
solid).  The part containing the solid will be fully loaded if necessary.

Environment: Internal and External
See Also:
History: 
*******************************************************************************/
extern UFUNEXPORT int UF_MODL_create_impr_faces
(
  UF_MODL_imprint_faces_data_p_t   parms, /* <I>
                                          Parameters of the new imprint feature
                                          */
  tag_t *feature_tag /* <O>
                     The feature created
                     */
);
/******************************************************************************
Edit an existing imprint faces feature according to the specified data,
which must have been created at an earlier timestamp than the feature.
It is not possible to edit an imprint feature to be on a different body.
If the <n_imprint_faces> parm is 0 or the <imprint_datum_plane> parm is
NULL_TAG, then the corresponding feature parm will be unchanged by the edit.

Environment: Internal and External
See Also:
History: This function was originally released in V15.0.
*******************************************************************************/
extern UFUNEXPORT int UF_MODL_edit_impr_faces_parms
(
  tag_t feature_tag,  /* <I>
                      The imprint feature
                      */
  UF_MODL_imprint_faces_data_p_t   parms /* <I>
                                         New parameters of the imprint feature
                                         */
);

/******************************************************************************
Returns the current parameters of the imprint faces feature.  The array
in the returned UF_modl_imprint_faces_data_p_t must be freed by the user
with UF_free().

Environment: Internal and External
See Also:
History: This function was originally released in V15.0.
*******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_impr_faces_parms
(
  tag_t feature_tag, /* <I>
                     The imprint feature
                     */
  UF_MODL_imprint_faces_data_p_t   parms /* <OF>
                                         The parameters of the imprint feature.
                                         */
);
/******************************************************************************
For any imprint feature, return an array containing the edges created
by it.  Only edges with associated geometry will be returned.

Environment: Internal and External
See Also:
History: This function was originally released in V15.0.
*******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_impr_edges
(
  tag_t feature_tag, /* <I>
                     The imprint feature
                     */
  int *n_edges, /* <O>
                The number of edges created by the imprint feature
                */
  tag_t **edges /* <OF, len:n_edges>
                The array of edges created by the imprint feature.  This must
                be freed by calling UF_free.
                */
);


#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif     /* UF_MODL_SIMPLIFY_H_INCLUDED */
