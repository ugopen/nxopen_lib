/*****************************************************************************
             Copyright (c) 1998-2003 Unigraphics Solutions Inc.
                       Unpublished - All Rights Reserved                       



File description: 
    Open API modeling routines to create, edit and inquire about tapers.

*****************************************************************************/

#ifndef UF_MODL_TAPER_H_INCLUDED
#define UF_MODL_TAPER_H_INCLUDED


/***************************************************************************

  ***************************************************************************/

#include <uf_defs.h>
#include <uf_modl_types.h>
#include <libufun_exports.h>

#ifdef __cplusplus
extern "C" {
#endif

/****************************************************************************
Creates a face taper feature using a location, direction, angle, and a
list of faces to taper. The output of this function is the object identifier
associated to the face taper.

Environment: Internal  and  External
See Also:
 UF_MODL_create_taper_from_faces
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_create_face_taper(
double  location[3] ,/* <I>
                     Taper location.
                     */
double  direction[3] ,/* <I>
                      Taper direction.
                      */
const char * angle ,/* <I>
              Taper angle.
              */
uf_list_p_t faces ,/* <I>
                   List of faces to taper.
                   */
tag_t * feature_obj_id  /* <O>
                        Feature object identifier of created face taper
                        */
);

/********************************************************************
Gets taper parameters.

Environment: Internal  and  External
See Also:
History:
********************************************************************/
extern UFUNEXPORT int UF_MODL_ask_taper_parms(
tag_t feature_obj_id ,/* <I>
                      A feature object identifier
                      */
int  edit ,/* <I>
           This is an unused flag. It was used to determine
           whether to return the right-hand side or both sides
           of an expression. Currently, both sides of an
           expression are returned.
           */
char ** angle  /* <OF>
               Taper angle.  This must be freed by calling UF_free.
               */
);

/****************************************************************************
Creates a taper on a specified feature.

Environment: Internal  and  External
See Also:
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_create_feature_taper(
double location[3] ,/* <I>
                    Location of the taper
                    */
double direction[3] ,/* <I>
                     Direction of the taper
                     */
const char * angle ,/* <I>
              Angle of taper
              */
tag_t original_feature ,/* <I>
                        Identifier for the feature to be tapered.
                        */
tag_t * taper_feature  /* <O>
                       Identifier for the tapered feature
                       */
);

/****************************************************************************
Create a taper feature from the input edges.

Environment: Internal  and  External

You can input individual edges or an edge collector as the first element
of array edges[].

See Also:
History: NX2.0 added the edge collector functionality
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_create_taper_from_edges(
    tag_t direction_tag,   /* <I>
                           taper direction
                           */
    const char *angle_str,       /* <I>
                           taper angle
                           */
    logical taper_all_instances, /* <I>
                                 all instances or else just this one
                                 */
    int num_edges,         /* <I>
                           number of edges in array
                           */
    tag_t edges[],         /* <I,len:num_edges>
                           array of edges to taper
                           */
    tag_t *feature_tag   /* <O>
                         feature eid of created feature taper
                         */
);

/****************************************************************************
Create a split line taper.  A regular taper will create multiple faces,
based on the edges supplied to the function.  A split line taper will
create a single face, but the face may not meet the edges specified.
In this case sweep faces are created perpendicular to the reference
direction to accomodate the mismatch.

You can input individual edges or an edge collector as the first element
of array edges[].


Environment: Internal  and  External
See Also:
History: Originally released in V16.0
         NX2.0 added the edge collector functionality
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_create_taper_split_line(
    tag_t    point_tag,    /* <I> taper reference point */
    tag_t direction_tag,   /* <I> taper direction */
    const char *angle_str,       /* <I> taper angle */
    logical taper_all_instances, /* <I>
                                 If TRUE, all instances will be tapered.  If
                                 FALSE, then just this instance is tapered.
                                 */
    int num_edges,         /* <I> number of edges in array */
    tag_t edges[],         /* <I,len:num_edges> array of edges to taper */
    double dist_tol,       /* <I> distance tolerances */
    double angle_tol,      /* <I> angle tolerances */
    tag_t *feature_tag /* <O> feature eid of created feature taper */
);

/****************************************************************************
Create a true taper from edges

Environment: Internal  and  External

You can input individual edges or an edge collector as the first element
of array edges[].

See Also:
History: Originally released in V17.0
         NX2.0 added the edge collector functionality
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_create_true_taper_from_edges
(
    tag_t direction_tag,   /* <I> taper direction */
    const char *angle_str,       /* <I> taper angle */
    logical taper_all_instances, /* <I>
                                 If TRUE, all instances will be tapered.  If
                                 FALSE, then just this instance is tapered.
                                 */
    int num_edges,         /* <I> number of edges in array */
    tag_t edges[],         /* <I,len:num_edges> array of edges to taper */
    double dist_tol,       /* <I> distance tolerances */
    double angle_tol,      /* <I> angle tolerances */
    tag_t *feature_eid     /* <O> feature eid of created feature taper */
);

/****************************************************************************
Require defining data of a taper from edges

Environment: Internal  and  External
See Also:
History: Originally released in V17.0
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_taper_from_edges
(
    tag_t    feature_eid,          /* <I> feature eid of created taper */
    int      *type,                /* <O> taper type */
    tag_t    *direction_tag,       /* <O> taper direction */
    char     angle_str[ UF_MAX_EXP_BUFSIZE ],           /* <O> taper angle */
    logical  *taper_all_instances, /* <O> tapering all instances */
    int      *num_edges,           /* <O> number of edges */
    tag_t    **edges,              /* <OF,len:num_edges> array of edges, 
                                           this must be freed by calling UF_free 
                                   */
    double   *dist_tol,            /* <O> tolerance of distance */
    double   *angle_tol            /* <O> tolerance of angle */
);

/******************* 
Returns the defining data for a collector enabled Taper from edges feature. 
To be used in place of UF_MODL_ask_taper_from_edges() when collection objects are desired.
Environment: Internal  and  External 
See Also: 
 UF_MODL_create_taper_from_edges
 UF_MODL_ask_taper_from_edges
History: This function was originally released in NX2.0.
********************/
extern UFUNEXPORT int UF_MODL_ask_taper_from_edges1
(
    tag_t    feature_obj_id,       /* <I> Feature object identifier for the Taper feature*/
    int     *taper_type,           /* <O> Taper type */
    tag_t   *direction_tag,        /* <O> Taper direction */
    char     angle_str[ UF_MAX_EXP_BUFSIZE ],            /* <O> Taper angle */
    logical *taper_all_instances,  /* <O> Tapering all instances */
    tag_t   *edge_collection,      /* <O> Collection of edges to be tapered */
    double  *distance_tolerance,   /* <O> Distance tolerance */
    double  *angle_tolerance       /* <O> Angle tolerance */
) ;

/****************************************************************************
Edit a taper from edges

Environment: Internal  and  External
See Also:
History: Originally released in V17.0
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_edit_taper_from_edges
(
    tag_t           feature_eid,           /* <I> feature eid of created taper */
    int             type,                  /* <I> taper type */
    tag_t           direction_tag,         /* <I> taper direction */
    const char *    angle_str,             /* <I> taper angle */
    logical         taper_all_instances,   /* <I> tapering all instances */
    int             num_edges,             /* <I> number of edges */
    tag_t           edges[],               /* <I,len:num_edges> array of edges */
    double          dist_tol,              /* <I> tolerance of distance */
    double          angle_tol              /* <I> tolerance of angle */
);

/****************************************************************************
Creates a face taper feature using a location, direction, angle, and a
list of faces to taper. The output of this function is the object identifier
associated to the face taper.

You can input individual faces or a face collector as the first element
of array faces[].

Environment: Internal and External
See Also:
 UF_MODL_create_face_taper
History: NX2.0 added the face collector functionality
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_create_taper_from_faces(
    tag_t           point_tag,              /* <I>
                                                taper location
                                            */
    tag_t           direction_tag,          /* <I>
                                                taper direction
                                            */
    const char *    angle_str,              /* <I>
                                                taper angle
                                            */
    logical         taper_all_instances,    /* <I>
                                                all instances or else just this one
                                            */
    int             num_faces,              /* <I>
                                                number of faces in array
                                            */
    tag_t           faces[],                /* <I,len:num_faces>
                                                array of faces to taper
                                            */
    tag_t *         feature_tag             /* <O>
                                                feature eid of created feature taper
                                            */
);

/****************************************************************************
Create a taper feature from tangent faces.

You can input individual faces or a face collector as the first element
of array faces[].

Environment: Internal and External
See Also:
History: NX2.0 added the face collector functionality
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_create_taper_from_tangent_faces(
    tag_t direction_tag,            /* <I>
                                        taper direction
                                    */
    const char *angle_str,          /* <I>
                                        taper angle
                                    */
    logical taper_all_instances,    /* <I>
                                        all instances or else just this one
                                    */
    int num_faces,                  /* <I>
                                        number of faces in array
                                    */
    tag_t faces[],                  /* <I,len:num_faces>
                                        array of faces to taper
                                    */
    tag_t *feature_eid              /* <O>
                                        feature eid of created feature taper
                                    */
);

/****************************************************************************
Create a variable angle taper feature from the input edges. This function is
the same as UF_MODL_create_taper_from_edges if the input num_points=0.

You can input individual edges or an edge collector as the first element
of array edges[].

Environment: Internal  and  External
See Also:
History: Originally released in V16.0
         NX2.0 added the edge collector functionality
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_create_variable_taper_from_edges (
    tag_t direction_tag,            /* <I>
                                        taper direction
                                    */
    const char *angle_str,          /* <I>
                                        taper angle
                                    */
    logical taper_all_instances,    /* <I>
                                        all instances or else just this one
                                    */
    int num_edges,                  /* <I>
                                        number of edges in array
                                    */
    tag_t edges[],                  /* <I,len:num_edges>
                                        array of edges to taper
                                    */
    int num_points,                 /* <I>
                                        number of points where angles are specified
                                    */
    double points[],                /* <I,len:3*num_points>
                                        coordinates of the points (size is 3*num_points)
                                    */
    char **angles,                  /* <I,len:num_points>
                                        angle values or expressions at the points
                                    */
    double dist_tol,                /* <I>
                                        distance tolerances
                                    */
    double angle_tol,               /* <I>
                                        angle tolerances
                                    */
    tag_t *feature_tag              /* <O>
                                        feature eid of created feature taper
                                    */
);

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif     /* UF_MODL_TAPER_H_INCLUDED */
