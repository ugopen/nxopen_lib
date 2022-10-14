/*******************************************************************************
             Copyright (c) 1999-2003,2004 Unigraphics Solutions Inc.
                       Unpublished - All Rights Reserved



File description:
   Open API modeling routines to create, edit and inquire about blends.

*****************************************************************************/

#ifndef UF_MODL_BLENDS_H_INCLUDED
#define UF_MODL_BLENDS_H_INCLUDED


/***************************************************************************

  ***************************************************************************/

#include <uf_defs.h>
#include <uf_modl_types.h>
#include <libufun_exports.h>

struct UF_MODL_blend_point_s
{
    char radius[ UF_MAX_EXP_BUFSIZE ];     /* <len:UF_MAX_EXP_BUFSIZE> variable radius at a point */
    double parameter;                   /* parameter at a point */
};

typedef struct UF_MODL_blend_point_s UF_MODL_blend_point_t,
*UF_MODL_blend_point_p_t;

struct UF_MODL_blend_edge_s
{
    tag_t edge;                         /* an edge eid or an edge collector eid. Collector
                                           cannot be used for cliff edge blend or used
                                           to specify variable or setback data. */
    tag_t cliff_edge;                   /* an cliff-edge eid */
    int number_points;                  /* number of selected points on an edge */
    char start_setback_dis[ UF_MAX_EXP_BUFSIZE ];  /* <len:UF_MAX_EXP_BUFSIZE> setback distance of an edge-start point */
    char end_setback_dis[ UF_MAX_EXP_BUFSIZE ];    /* <len:UF_MAX_EXP_BUFSIZE> setback distance of an edge-end point */
    UF_MODL_blend_point_p_t point_data; /* <len:number_points> point data on an edge */
};

typedef struct UF_MODL_blend_edge_s UF_MODL_blend_edge_t,
*UF_MODL_blend_edge_p_t;

struct UF_MODL_edge_blend_data_s
{
    int blend_type;                   /* type of created blends
                                        0 - regular edge blend
                                        1 - cliff-edge blend
                                      */
    logical blend_instanced;          /* instanced blend */
    logical blend_setback;            /* setback blend */
    double vrb_tolerance;             /* tolerance of a variable blend */
    char blend_radius[ UF_MAX_EXP_BUFSIZE ]; /* <len:UF_MAX_EXP_BUFSIZE> radius of a regular blend */
    logical smooth_overflow;          /* blend smooth overflow */
    logical cliff_overflow;           /* blend cliff overflow */
    logical notch_overflow;           /* blend notch overflow */
    int number_edges;                 /* number of edges to be blended */
    UF_MODL_blend_edge_p_t edge_data; /* <len:number_edges>
                                         Data of an edge to be blended or an edge collector.
                                         If input an edge collector, input it in the first
                                         element array. Extra elements in the array can be
                                         used to input varialbe radius data and/or setback
                                         data. But the edges specified for these data must
                                         be the edges of the collector, otherwise they will
                                         be ignored. */
};

typedef struct UF_MODL_edge_blend_data_s UF_MODL_edge_blend_data_t,
*UF_MODL_edge_blend_data_p_t;

/*********************************************************************************************/
/*                       New Data Structures for Nx3.0 Edge Blend                            */
/*********************************************************************************************/
/* Point Data for Variable Radius Structure */
struct UF_MODL_blend_point_data_s
{
    char radius[ UF_MAX_EXP_BUFSIZE ];     /* <len:UF_MAX_EXP_BUFSIZE> variable radius at a point */
    double parameter;                   /* parameter at a point Its the percentage of paramter value
                                           so can have values ranging from 0.0 to 1.0 */
    tag_t radius_exp ;                  /* Expression TAG will only be set during Edit, User can edit the
                                           radius string to edit the new value*/
    int   status;                       /* When adding Status = 1 and To remove Status = 0 */
};
typedef struct UF_MODL_blend_point_data_s UF_MODL_blend_point_data_t,
*UF_MODL_blend_point_data_p_t;

/* Setback Data Structure */
struct UF_MODL_edge_blend_setback_data_s
{
    tag_t    edge;                 /* The edge on which setback distance has to be specified */
    logical  from_start;           /* if true, then the setback is defined at the start vertex.
                                      Otherwise, it is defined at the end vertex. */
    char     distance[ UF_MAX_EXP_BUFSIZE ];
                                   /* Setback distance */
    tag_t    distance_exp ;        /* Expression TAG will only be set during Edit, User can edit the
                                      distance string to edit the new value*/
    int      status ;              /* When adding Status = 1 and To remove Status = 0 */

};

typedef struct UF_MODL_edge_blend_setback_data_s UF_MODL_edge_blend_setback_data_t,
*UF_MODL_edge_blend_setback_data_p_t;

/* Stopshort Data Structure */
struct UF_MODL_edge_blend_stopshort_data_s
{
    tag_t    edge;                    /* The edge where the stopshort is defined */
    logical  from_start;              /* if true, then the stopshort is defined from the start of edge.
                                         Otherwise, it is defined from the end of edge. */
    char     distance[ UF_MAX_EXP_BUFSIZE ];
                                      /* %Stopshort distance [0 - 100] */
    tag_t    distance_exp ;           /* Expression TAG will only be set during Edit, User can edit the
                                         distance string to edit the new value*/
    int      status ;                 /* When adding Status = 1 and To remove Status = 0 */
};

typedef struct UF_MODL_edge_blend_stopshort_data_s UF_MODL_edge_blend_stopshort_data_t,
*UF_MODL_edge_blend_stopshort_data_p_t;

/* Blend Set(Chainset) Data Structure */
struct UF_MODL_edge_blend_set_s
{
    tag_t  edge_collector;     /* The edge collector, if this is a NULL_TAG, then
                                  the edges will be read from num_edges and edges */

    int    num_edges;          /* The edges with a constant radius. Is honored only
                                  when the edge_collector is NULL_TAG */
    tag_t* edges;              /* <len:num_edges> */


    char   radius[ UF_MAX_EXP_BUFSIZE ];
                                /* Radius associated with these edges */
    tag_t radius_exp ;          /* Expression TAG will only be set during Edit, User can edit the
                                   radius string to edit the new value*/
    int      status ;           /* When adding Status = 1 and To remove Status = 0 */
};

typedef struct UF_MODL_edge_blend_set_s UF_MODL_edge_blend_set_t,
*UF_MODL_edge_blend_set_p_t;

/*
   New Edge Blend Data Structure with Multiple Chainsets, Variable Radius, Setback, Stopshort and
   Options enabled
*/
struct UF_MODL_edge_blend_mult_data_s
{
    logical blend_instanced;          /* instanced blend */
    double  vrb_tolerance;            /* tolerance of a variable blend */
    logical smooth_overflow;          /* blend smooth overflow */
    logical cliff_overflow;           /* blend cliff overflow */
    logical notch_overflow;           /* blend notch overflow */
    logical allow_twist_patches;      /* Allow twist patches to be created.
                                         The corresponding option in interactive NX
                                         is Remove Self Intersections.  When 
                                         allow_twist_patches is TRUE it corresponds 
                                         to Remove Self Intersections being set to OFF */
    logical soften_vertices;          /* Y-Blend */
    int num_sets;                     /* number of blend sets to be blended */
    UF_MODL_edge_blend_set_p_t *edge_data; /* <len:num_sets>
                                           Data of an edges/Blendset to be blended or an edge collector.
                                           */

    int num_var_rad;                  /* Number of points where variable radius is defined */
    tag_t *var_edges;                 /* <len:num_var_rad>
                                         The edge on which the variable radius is defined */
    UF_MODL_blend_point_data_t *var_radius_data;
                                      /* <len:num_var_rad>
                                         Location of the edge and radius value for the variable
                                         radius */

    int num_setback;                  /* Number of edges that have setbacks defined. */
    UF_MODL_edge_blend_setback_data_p_t  *setback_data;
                                      /* <len:num_setback>
                                         Setback data on the edges. */


    int num_stopshort;                /* Number of edges that have stopshorts defined. */
    UF_MODL_edge_blend_stopshort_data_p_t  *stopshort_data;
                                      /* <len:num_stopshort>
                                         Stopshort data on the edges. */

};

typedef struct UF_MODL_edge_blend_mult_data_s UF_MODL_edge_blend_mult_data_t,
*UF_MODL_edge_blend_mult_data_p_t;

/*********************************************************************************************/
/*                       End of Data Structures for Nx3.0 Edge Blend                         */
/*********************************************************************************************/
#ifdef __cplusplus
extern "C" {
#endif

/********************************************************************
Creates a face blend.

An object tag associated to the newly created blend is returned only if
all the following conditions are valid:
  . all faces involved belong to the same body,
  . trim_option = UF_TRIM_AND_ATTACH
  . blend faces can be successfully trimmed and attached to the
  . body. In this case, a parametric feature is created.

If an object tag is not returned and the return code indicates success,
the blend is formed between the faces and/or bodies involved as
separate non-parametric sheet bodies. In this case the tags of newly
created bodies are returned.

Neither set of the faces/bodies can contain:
 . more than one solid body.
 . sheet and solid faces and/or bodies together
 . faces from more than one solid body
 . body and faces from the same body

The caller does not have to know exactly which edges are to be
cliff-edges, all inappropriate edges are ignored.

Tangent hold lines can be used to constrain either constant radius or
law controlled blends. In this case, the smaller of the two implied radii
is the result. Edges and curves can not be used together to constitute
tangent hold lines.

The help point is not taken into account if blend is non-parametric.
Only non-parametric blends can be limited.


This function will be replaced by UF_MODL_create_face_blend.
Please use UF_MODL_create_face_blend which can create all types of
face blends.

Environment: Internal  and  External

See Also:  UF_MODL_create_face_blend

History:
********************************************************************/
extern UFUNEXPORT int UF_MODL_create_blend_faces
(
    UF_MODL_blend_faces_create_data_p_t create_data, /* <I>
                                                     Data describing the blend.
                                                     */
    UF_MODL_blend_faces_limit_data_p_t  limit_data,  /* <I>
                                                     Data describing the blend.
                                                     */

    tag_t           *feature_tag,         /* <O>
                                          The object identifier of the created
                                          blend.
                                          */
    int             *num_bodies_created,  /* <O>
                                          This is unused, and always returns 0.
                                          */
    tag_t          **bodies_created,      /* <OF,len:num_bodies_created> num_bodies_created
                                          This is unused, the pointer is
                                          always set to NULL.
                                          */
    int             *num_blend_faces,     /* <O>
                                          This is unused, and always returns 0.
                                          */
    tag_t          **blend_faces          /* <OF,len:num_blend_faces> num_blend_faces
                                          This is unused, the pointer is
                                          always set to NULL.
                                          */
);

/********************************************************************
Creates a blend feature using the input radius, a list of edges to blend,
the overflow condition flags, and variable radius blend tolerance. To
specify all types of blends, set all of the overlfow flags to 0 (zero). To
allow only one type of blend, for example "smooth", set the
smooth_overflow flag to 0 (zero) and the other two flags to 1 (one).
The output of this function is the object identifier associated to the
blend.

Environment: Internal  and  External
See Also:
History:
********************************************************************/
extern UFUNEXPORT int UF_MODL_create_blend(
const char * radius ,/* <I>
                     Blend radius
                     */
uf_list_p_t edge_list ,/* <I>
                       List of edges to blend
                       */
int smooth_overflow ,/* <I>
                     Smooth overflow/prevent flag:
                        0 = Allow this type of blend
                        1 = Prevent this type of blend
                     */
int cliff_overflow ,/* <I>
                    Cliffedge overflow/prevent flag:
                        0 = Allow this type of blend
                        1 = Prevent this type of blend
                    */
int notch_overflow ,/* <I>
                    Notch overflow/prevent flag:
                        0 = Allow this type of blend
                        1 = Prevent this type of blend
                    */
double vrb_tool ,/* <I>
                 Variable radius blend tolerance
                 */
tag_t * feature_obj_id  /* <O>
                        Feature object identifier of created blend
                        */
);

/********************************************************************
create an edge blend

Environment: Internal  and  External
It can accept individual edges or an edge collector.

See Also:
History: V17 release
         NX2.0 Allow user input edge collector in the edge_data array
********************************************************************/
extern UFUNEXPORT int UF_MODL_create_edge_blend
(
    UF_MODL_edge_blend_data_p_t blend_data, /* <I>
                                               User defining blend data
                                            */
    tag_t *blend_eid                        /* <O>
                                               Feature object identifier of a created blend
                                            */
);

/********************************************************************
Ask an edge blend data

Environment: Internal  and  External
See Also:
History: V17 release
********************************************************************/
extern UFUNEXPORT int UF_MODL_ask_edge_blend
(
    tag_t feature_eid,                     /* <I>
                                              Feature object identifier of a created blend
                                           */
    UF_MODL_edge_blend_data_p_t blend_data /* <OF>
                                              Data describing the created blend
                                           */
);

/*******************
Returns the defining data for a collector enabled Edge Blend feature.
To be used in place of UF_MODL_ask_edge_blend() when collection objects are desired.
Environment: Internal  and  External
See Also:
 UF_MODL_create_edge_blend
 UF_MODL_ask_edge_blend
History: This function was originally released in NX2.0.
********************/
extern UFUNEXPORT int UF_MODL_ask_edge_blend1
(
    tag_t  feature_obj_id,                  /* <I> Feature object identifier for the Edge Blend feature*/
    UF_MODL_edge_blend_data_p_t blend_data  /* <OF>  Data describing the Edge Blend feature */
);

/********************************************************************
Edit an edge blend

Environment: Internal  and  External

It can accept individual edges or an edge collector.

See Also:
History: V17 release
         NX2.0 Allow user input edge collector in the edge_data array
********************************************************************/
extern UFUNEXPORT int UF_MODL_edit_edge_blend
(
    tag_t feature_eid,                     /* <I>
                                              Feature object identifier of a created blend
                                           */
    UF_MODL_edge_blend_data_p_t blend_data /* <I>
                                              User defining blend data
                                           */
);

/********************************************************************
Gets blend parameter.

Environment: Internal  and  External

See Also:

History:
********************************************************************/
extern UFUNEXPORT int UF_MODL_ask_blend_parms(
tag_t feature_obj_id ,/* <I>
                      A feature object identifier
                      */
int  edit ,/* <I>
           This is an unused flag. It used to determine whether
           to return the right-hand side or both sides of an
           expression. Currently, both sides of an expression
           are returned.
           */
char ** radius  /* <OF>
                Blend radius.  This must be freed by calling
                UF_free.
                */
);

/****************************************************************************
Registers a routine for creating a variable radius blend (VRB). This
allows you to register a routine into the Open API environment
so that you can specify the points necessary for the VRB.

Subsequently, every time a blend is created, this registered routine is
called. Note that this routine works in conjunction with
UF_MODL_create_blend. The general procedure for using this
function is to:

   1. Register the vrb_routine with a call to UF_MODL_register_var_blend.
   2. Create the variable blend with a call to UF_MODL_create_blend. Your
      registered routine is called once for each edge on the list that
      was inputted to UF_MODL_create_blend.
   3. Unregister your vrb_routine with a call to UF_MODL_unregister_var_blend.

To register a routine named vrb_routine(), the call is:
    UF_MODL_register_var_blend(vrb_routine)

where vrb_routine is defined as:

   int vrb_routine(tag_t obj_id, double points[100][3],
                  char radii[100][256],
                  int smooth_overflow, int cliff_overflow,
                  int notch_overflow, int *number_pts)

The integer values for smooth_overflow, cliff_overflow, and
notch_overflow control the overflow during blending. The following
string defined constants should be used.

UF_MODL_BLEND_NO_OVERFLOW - allows overflow control.
UF_MODL_BLEND_SMOOTH_OVERFLOW - does not allow smooth overflow control.
UF_MODL_BLEND_CLIFF_OVERFLOW - does not allow cliff overflow control.
UF_MODL_BLEND_NOTCH_OVERFLOW - does not allow notch overflow control.

vrb_tol allows you to specify a variable radius blend tolerance and it
should be positive and bigger than 10E-8mm.

Environment: Internal  and  External
See Also: 
History:
 ***************************************************************************/
typedef int (*UF_MODL_var_blend_f_t)
                                     (tag_t a, /* <I> */
                                     double b[100][3], /* <I> */
                                     char c[100][256], /* <I> */
                                     int smooth_overflow, /* <I> */
                                     int cliff_overflow, /* <I> */
                                     int notch_overflow, /* <I> */
                                     double vrb_tol, /* <I> */
                                     int *d /* <I> */);

extern UFUNEXPORT int UF_MODL_register_var_blend(
UF_MODL_var_blend_f_t routine
               /* <I>
               Routine name. You define the routine.  The system
               calls the routine like this:
               error =  routine(tag_t obj_id,
                        double points[100][3],
                        char radii[100][256],
                        int smooth_overflow
                        int cliff_overflow
                        int notch_overflow
                        double vrb_tol
                        int *number_pts)
               where obj_id is each edge on the list that was
               provided to UF_MODL_create_blend. Therefore,
               you should define the  routine like this:
               int routine(tag_t obj_id,
                        double points[100][3],
                        char radii[100][256],
                        int smooth_overflow
                        int cliff_overflow
                        int notch_overflow
                        double vrb_tol
                        int *number_pts)
               and the routine returns an error if it failed. If the
               returned error is != 0, then the new form feature is
               deleted and an error is returned..
               */
);

/****************************************************************************
Used to unregister any previously set variable radius blend routine.

Environment: Internal  and  External
See Also:
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_unregister_var_blend( void );

/****************************************************************************
Registers a routine for creating a cliff blend. This allows you to
register a routine into the Open API environment for the cliff
blend.

To register a routine named cliff_routine(), the call is:
   UF_MODL_register_cliff_blend(cliff_routine)

where cliff_routine is defined as:
   int cliff_routine(tag_t obj_id,  int *cliff)

Environment: Internal  and  External
See Also:
History:
 ***************************************************************************/
typedef int (*UF_MODL_cliff_blend_f_t)(tag_t, /* <I> */ tag_t* /* <I> */);

extern UFUNEXPORT int UF_MODL_register_cliff_blend(
UF_MODL_cliff_blend_f_t var_routine
                 /* <I>
                 Routine name. You define the routine.  The system
                 calls the routine like this:
                 error =  routine((tag_t) obj_id, tag_t *cliff)
                 where obj_id is the new blend that was just created.
                 Therefore, you should define the  routine like this:
                 int routine(tag_t obj_id, tag_t *cliff)
                 and the routine returns an error if it failed. If the
                 returned error is != 0, then the new form feature is
                 deleted and an error is returned..
                 */
);

/****************************************************************************
Used to unregister any previously set cliff blend routine.

Environment: Internal  and  External
See Also:
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_unregister_cliff_blend( void );

/********************************************************************
Initialize face blend create data

Environment: Internal  and  External

See Also:

   The initial values UF_MODL_init_face_blend_data assigned to
   data structure UF_MODL_face_blend_create_data_t.

   first_set          = NULL
   first_set_size     = 0
   flip_first_normal  = FALSE
   second_set         = NULL
   second_set_size    = 0
   flip_second_normal = FALSE
   propagate          = FALSE
   cliff_edges        = NULL
   n_cliff_edges      = 0
   thls               = NULL
   n_thls             = 0
   proj_on_first_set  = TRUE
   end_overflow       = TRUE
   blend_tolerance    = system distance tolerance
   trim_option        = UF_TRIM_AND_ATTACH
   radius_type        = UF_CONSTANT
   default_radius     = "0.25"
   thls_1             = NULL
   n_thls_1           = 0
   law_parameters     = NULL

History: Originally released in V16.0
********************************************************************/
extern UFUNEXPORT void UF_MODL_init_face_blend_data
(
    UF_MODL_face_blend_create_data_p_t  create_data  /* <I>
                                                     Data describing the blend.
                                                     */
);

/********************************************************************
Creates a face blend

This function is intended to replace UF_MODL_create_blend_faces.

Creates face-to-face blends or construction of  blends, between
walls of faces that are not necessarily adjacent to each other (and not
necessarily part of the same body). A wall may be constructed from
faces on a single body or from multiple sheet bodies. In this case, the
sheets are sewn together automatically before blending (if possible).
Optionally, the wall faces may be trimmed automatically to the new
blend edges, and may also be attached to the blend. The blend radius
may be constant, controlled by a Law function along a spine curve or
by specification of Tangency Curves only.

It can accept individual faces, curves and edges for the face sets and
tangent hold lines. It can also accept the face, edge and curve collectors
in the same corresponding array. But for each array, only one collector
is allowed.

Environment: Internal  and  External

See Also:

History: Added in v16.0
         NX2.0 Allow user input collectors
********************************************************************/
extern UFUNEXPORT int UF_MODL_create_face_blend
(
    UF_MODL_face_blend_create_data_p_t  create_data, /* <I>
                                                     Data describing the blend.
                                                     */
    UF_MODL_blend_faces_limit_data_p_t  limit_data,  /* <I>
                                                     Data describing the blend.
                                                     */

    tag_t           *feature_tag,         /* <O>
                                          The object identifier of the created
                                          blend.
                                          */
    int             *num_bodies_created,  /* <O>
                                          This is unused, and always returns 0.
                                          */
    tag_t          **bodies_created,      /* <OF,len:num_bodies_created>
                                          This is unused, the pointer is
                                          always set to NULL.
                                          */
    int             *num_blend_faces,     /* <O>
                                          This is unused, and always returns 0.
                                          */
    tag_t          **blend_faces          /* <OF,len:num_blend_faces>
                                          This is unused, the pointer is
                                          always set to NULL.
                                          */
);

/********************************************************************
Ask face blend data

Environment: Internal  and  External

See Also:

History: Originally released in V16.0
********************************************************************/
extern UFUNEXPORT int UF_MODL_ask_blend_face_data
(
   tag_t feature_tag,              /*<I> The object identifier of the blend */
   UF_MODL_face_blend_create_data_p_t  read_data,
                                   /*<O> Data describing the blend*/
   UF_MODL_blend_faces_limit_data_p_t  limit_data
                                  /*<O> Data describing the blend*/
);

/*******************
Returns the defining data for a collector enabled Edge Blend feature.
To be used in place of UF_MODL_ask_edge_blend() when collection objects are desired.
Environment: Internal  and  External
See Also:
 UF_MODL_create_face_blend
 UF_MODL_ask_blend_face_data
History: This function was originally released in NX2.0.
********************/
extern UFUNEXPORT int UF_MODL_ask_blend_face_data1
(
   tag_t feature_tag,              /*<I> The object identifier of the blend */
   UF_MODL_face_blend_create_data_p_t  read_data,
                                   /*<O> Data describing the blend*/
   UF_MODL_blend_faces_limit_data_p_t  limit_data
                                  /*<O> Data describing the blend*/
);

/********************************************************************
Ask face blend law radii

Environment: Internal  and  External

See Also:

History: Originally released in V16.0
********************************************************************/
extern UFUNEXPORT int UF_MODL_ask_face_blend_law_radii
(
   tag_t feature,              /*<I> The object identifier of the blend */
   double **radii_values,      /*<OF,len:rad_num> Array of law radii values.  This is
                                      an array that must be freed by calling
                                      UF_free. */
   int *rad_num                /*<O> Data describing the blend*/
);

/********************************************************************
Ask conic face blend law radii for offset1

Environment: Internal  and  External

See Also:

History: Originally released in V16.0
********************************************************************/
extern UFUNEXPORT int UF_MODL_ask_face_blend_law_range1_radii
(
   tag_t feature,         /*<I> The object identifier of the blend */
   double **radii_values, /*<OF,len:rad_num> Array of law radii values.  This is an
                                array that must be freed by calling UF_free. */
   int *rad_num           /*<O> Number of radii */
);

/********************************************************************
Ask conic face blend law radii for offset2

Environment: Internal  and  External

See Also:

History: Originally released in V16.0
********************************************************************/
extern UFUNEXPORT int UF_MODL_ask_face_blend_law_range2_radii
(
   tag_t feature,         /*<I> The object identifier of the blend */
   double **radii_values, /*<OF,len:rad_num> Array of law radii values.  This is an
                                array that must be freed by calling UF_free. */
   int *rad_num           /*<O> Number of radii */
);

/********************************************************************
Set face blend law radii

Environment: Internal  and  External

See Also:

History: Originally released in V16.0
********************************************************************/
extern UFUNEXPORT int UF_MODL_set_face_blend_law_radii
(
   tag_t feature,         /*<I> The object identifier of the blend */
   double *radii_values,  /*<I,len:rad_num> Array of new law radii values */
   int rad_num            /*<I> Number of new radii */
);

/********************************************************************
Set conic face blend law radii for offset1

Environment: Internal  and  External

See Also:

History: Originally released in V16.0
********************************************************************/
extern UFUNEXPORT int UF_MODL_set_face_blend_law_range1_radii
(
   tag_t feature,        /*<I> The object identifier of the blend */
   double *radii_values, /*<I,len:rad_num> Array of new law radii values */
   int rad_num           /*<I> Number of new radii */
);

/********************************************************************
Set conic face blend law radii for offset2

Environment: Internal  and  External

See Also:

History: Originally released in V16.0
********************************************************************/
extern UFUNEXPORT int UF_MODL_set_face_blend_law_range2_radii
(
   tag_t feature,        /*<I> The object identifier of the blend */
   double *radii_values, /*<I,len:rad_num> Array of new law radii values */
   int rad_num           /*<I> Number of new radii */
);



/********************************************************************
Initialize the multiple radius blend data structure
Initial values assigned :
   blend_instanced     = FALSE
   num_setback         = 0
   num_var_rad         = 0
   num_stopshort       = 0
   vrb_tolerance       = APRTOL
   smooth_overflow     = TRUE
   cliff_overflow      = TRUE
   notch_overflow      = TRUE
   allow_twist_patches = TRUE
   soften_vertices     = FALSE
   var_radius_data     = NULL
   setback_data        = NULL
   stopshort_data      = NULL
   edge_data           = NULL
   var_edges           = NULL
Environment: Internal  and  External

See Also:
History: NX3.0 Release
********************************************************************/
extern UFUNEXPORT void UF_MODL_init_edge_blend_mult
(
    UF_MODL_edge_blend_mult_data_p_t blend_data /* <I>
                                                    User defining blend data
                                                 */
);
/********************************************************************
Initializes the  Blend Set(Chainset) data
Initial values assigned :
   edge_collector = NULL
   edges = NULL
   num_edges = 0
   radius = 0.25
   radius_exp = NULL
   status = 1
Environment: Internal  and  External

See Also:
History: NX3.0 Release
********************************************************************/
extern UFUNEXPORT void UF_MODL_init_edge_blend_set_mult
(
    UF_MODL_edge_blend_set_p_t blend_set /* <I>
                                                    User defining blend data
                                            */
);
/********************************************************************
Initializes the  Point data for variable radius blends
Initial values assigned :
   parameter = 0.0
   radius    = 0.25
   radius_exp = NULL
   status = 1
Environment: Internal  and  External

See Also:
History: NX3.0 Release
********************************************************************/
extern UFUNEXPORT void UF_MODL_init_edge_blend_point_mult
(
    UF_MODL_blend_point_data_p_t point_data /* <I>
                                                    User defining blend data
                                                 */
);
/********************************************************************
Initializes the  Setback data
Initial values assigned :
   distance = 0.5
   distance_exp = NULL
   edge = NULL_TAG
   from_start = true
   status = 1
Environment: Internal  and  External

See Also:
History: NX3.0 Release
********************************************************************/
extern UFUNEXPORT void UF_MODL_init_edge_blend_setback_mult
(
    UF_MODL_edge_blend_setback_data_p_t sb_data /* <I>
                                                    User defining blend data
                                                 */
);
/********************************************************************
Initializes the  StopShort data
Initial values assigned :
   distance = 20
   distance_exp = NULL
   edge = NULL
   from_start = true
   status = 1
Environment: Internal  and  External

See Also:
History: NX3.0 Release
********************************************************************/
extern UFUNEXPORT void UF_MODL_init_edge_blend_stopshort_mult
(
    UF_MODL_edge_blend_stopshort_data_p_t ss_data /* <I>
                                                    User defining blend data
                                                 */
);
/********************************************************************
Creates an edge blend with multiple radius chainsets as per NX3.0 Blend Functionality.
User van create multiple chainset with different radius values. Specify varaible radius points
on a given edge .Also specify Setback Distance values on an edge coming into a vertex.Also
can specify Stopshort values per edge.
Each Blend Set can take in Edges or collector tag.

Environment: Internal  and  External
It can accept a set of individual edges or a set of edge collectors.

See Also:
History: NX3.0 Release
********************************************************************/
extern UFUNEXPORT int UF_MODL_create_edge_blend_mult
(
    UF_MODL_edge_blend_mult_data_p_t blend_data, /* <I>
                                                    User defining blend data
                                                 */
    tag_t *blend_eid                             /* <O>
                                                    Feature object identifier of a created blend
                                                 */
);


/********************************************************************
Enquire whether it is a radius blend with multiple chainset capability
feature or not.


Environment: Internal  and  External
See Also:
History: NX3.0 Release
********************************************************************/
extern UFUNEXPORT logical UF_MODL_ask_edge_blend_is_mult
(
    tag_t feature_eid                      /* <I>
                                              Feature object identifier of a created blend
                                           */
);


/********************************************************************
Ask an edge blend data of a multiple radius blend feature. This API
will work even if it is a single constant radius blend.

Environment: Internal  and  External
See Also:
History: NX3.0 Release
********************************************************************/
extern UFUNEXPORT int UF_MODL_ask_edge_blend_mult
(
    tag_t feature_eid,                           /* <I>
                                                  Feature object identifier of a created blend
                                                 */
    UF_MODL_edge_blend_mult_data_p_t blend_data  /* <OF>
                                                    Data describing the created blend
                                                 */
);

/********************************************************************
Edit a mutiple radius edge blend

Environment: Internal  and  External

It can accept a set of individual edges or a set of edge collectors.

See Also:
History: NX3.0 Release
********************************************************************/
extern UFUNEXPORT int UF_MODL_edit_edge_blend_mult
(
    tag_t feature_eid,                            /* <I>
                                                     Feature object identifier of a created blend
                                                  */
    UF_MODL_edge_blend_mult_data_p_t blend_data   /* <I>
                                                     User defining blend data
                                                  */
);


#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif     /* UF_MODL_BLENDS_H_INCLUDED */
