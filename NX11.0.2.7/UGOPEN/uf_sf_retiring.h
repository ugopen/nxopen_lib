/*==================================================================================================

            Copyright (c) 2012 Siemens Product Lifecycle Management Software Inc.
                            Unpublished - All rights reserved

====================================================================================================



 File description:
          These routines are in the process of being removed from the NX Open API
          product.  Customers should use the designated replacement routines
          instead of the routines listed here.  Once a routine is placed
          here, it is eligible to be removed in the next release of NX.

====================================================================================================*/

#ifndef UF_SF_RETIRING
#define UF_SF_RETIRING
#include <uf_defs.h>
#include <uf_draw_types.h>
#include <uf_plist_types.h>
#include <uf_retiring_ugopenint.h>
#include <setjmp.h>
#include <uf_curve.h>
#include <uf_weld_types.h>
#include <uf_sf_post_datatypes.h>
#include <uf_ugmgr_types.h>
#include <uf_pd_types.h>
#include <uf_sf_enums.h>
#include <uf_sf_ugs_mesh.h>

#include <libufun_cae_exports.h>

/***************************************************************************

  ***************************************************************************/

#ifdef __cplusplus
extern "C" {
#endif


/****************************************************************************
Create New Mechanism and Setup Common

Initializes the mechanism name, assigns an object identifier, and sets
up parameters needed for the mechanism. Use this routine for parts
without existing mechanisms.

This function is retired.  Use UF_SF_create_scenario to create a new
scenario part and use UF_MOTION_initialize to set all the common
parameters for mechanism and motion objects.

Environment: Internal  and  External

See Also:

History:
*****************************************************************************/
extern UFUN_CAEEXPORT int uc6001(
char * cp1 ,/* <I>
            Mechanism name (30 char max)
            */
tag_t * nr2  /* <O>
             Mechanism object identifier
             */
);

/****************************************************************************
Delete objects of a mechanism.

This function has been retired.  Call UF_OBJ_delete_object or
UF_OBJ_delete_array_of_objects instead. (See uf_obj.h)

Environment: Internal  and  External
See Also:
History:
*****************************************************************************/
extern UFUN_CAEEXPORT void FTN(uf6009)(
tag_t *np1 /*<I>
             The object to be deleted.
           */
);

/****************************************************************************
Edit/Add Joint Motion Inputs

Motion inputs may only be applied to slider or revolute joints.

Return:
         Error Flag
        0 = No Errors
        1 = Joint object identifier Not Valid
        2 = Type Not Valid

This function is retired.  Please call UF_MOTION_set_joint_motion_input instead.

Environment: Internal  and  External

See Also:

History:
*****************************************************************************/
extern UFUN_CAEEXPORT int uc6025(
tag_t np1 ,/* <I>
           Joint object identifier
           */
int  ip2 ,/* <I>
          Type
          1 = Function String In cp3
          2 = Parameters In rp4 And ip5
          3 = Constant In rp4
          4 = Harmonic In rp4
          */
char * cp3 ,/* <I>
            Function String  (200 char max) - If ip2 = 1
            */
double * rp4 ,/* <I>
              Real Values (10 element array)
              10 Parameter Values - If ip2 = 2
              3 Constant Values  - If ip2 = 3
              4 Harmonic Values - If ip2 = 4
              */
int ip5  /* <I>
         Integer Parameter Value - If ip2 = 2
         */
);

/****************************************************************************
Add a Link to a Mechanism

Return:
         Error Flag
        0 = No Errors
        1 = Number Of object identifier's Not Valid - <1
        2 = Geometry object identifier's Not Valid

This function is retired.  Please call UF_MOTION_create_link instead.

Environment: Internal  and  External

See Also:

History:
*****************************************************************************/
extern UFUN_CAEEXPORT int uc6031(
char *   cp1 ,/* <I>
              Link Name (30 char *)
              */
int   ip2 ,/* <I>
           Number Of Geometry object identifier's
           */
tag_t *   np3 ,/* <I>
               Geometry object identifier's
               */
tag_t *  nr4  /* <O>
              Link object identifier
              */
);
/****************************************************************************
Read link weight, inertias and cog.  Inertia values represent the moments of
inertia of the mass of the link about the X, Y and Z axes and the products of
inertia of the mass with respect to the perpendicular axes XY, XZ, and YZ.

This function is retired.  Please call UF_MOTION_ask_link_mass_properties
instead.

Environment: Internal  and  External
See Also:
History:
*****************************************************************************/
extern UFUN_CAEEXPORT void FTN(uf6032)(
tag_t *np1, /* <I>
               Link object identifier
            */
int *ir2, /* <O>
             Weight Flag
             0 = No Weight
             1 = Weight Present In RR3
          */
double *rr3, /* <O>
                The weight.
             */
int *ir4, /* <O>
             Inertia Flag
             0 = No Inertias
             1 = Inertias Present in RR5, RR6, RR7
          */
double *rr5, /* <O>
                A six element array that will be filled with the inertias.
             */
double *rr6, /* <O>
               A three element array that will be filled with the inertia
               location.
             */
tag_t *nr7, /* <O>
               Inertia orientation matrix object identifier
             */
int *ir8, /* <O>
             COG Flag
             0 = No COG
             1 = COG Present In RR9
          */
double *rr9, /* <O>
                Three element array to receive the COG location.
             */
int *ir10 /* <O>
             Error Flag
             0 = No Errors
             1 = Link object identifier not valid
          */
);

/****************************************************************************
Return the Number of Geometry Object ID's Attached to Link

This function is retired.  Please call UF_MOTION_ask_link instead.

Environment: Internal  and  External
See Also:
History: In V10 and beyond, skeleton geometry is not valid.
*****************************************************************************/
extern UFUN_CAEEXPORT void FTN(uf6035)(
tag_t *np1,          /* <I>
                        Link object identifier
                     */
int *ir2,            /* <O>
                        Number Of Existing Geometry object identifier's
                     */
int *ir3,            /* <O>
                        Number Of Skeleton Geometry object identifier's
                     */
int *ir4             /* <O>
                        Error Flag
                            0 = No Error
                            1 = Link object identifier Not Valid
                     */
);
/****************************************************************************
Read the Geometry Object ID Associated with a Link

This function is retired.  Please call UF_MOTION_ask_link instead.

Environment: Internal  and  External
See Also:
History: In V10 and beyond, skeleton geometry is not valid.
*****************************************************************************/
extern UFUN_CAEEXPORT void FTN(uf6036)(
tag_t *np1,       /* <I>
                     Link object identifier
                  */
int *ip2,         /* <I>
                     Instance Of The object identifier Requested
                  */
int *ip3,         /* <I>
                     Flag
                         1 = Existing Geometry
                         2 = Skeleton Geometry
                  */
tag_t *nr4,       /* <O>
                     Geometry object identifier
                  */
int *ir5          /* <O>
                     Error Flag
                           0 = No Errors
                           1 = Link object identifier Not Valid
                           2 = Instance Number Not Valid
                           3 = Flag Not Valid
                  */
);
/****************************************************************************
Edit/Add Link Weight

This function is retired.  Please call UF_MOTION_set_link_mass_properties
instead.

Environment: Internal  and  External
See Also:
History:
*****************************************************************************/
extern UFUN_CAEEXPORT void FTN(uf6044)(
tag_t *np1,      /* <I>
                    Link object identifier
                 */
double *rp2,     /* <I>
                    Weight
                 */
int *ir3         /* <O>
                    Error Flag
                         0 = No Errors
                         1 = Link object identifier Not Valid
                 */
);
/****************************************************************************
Edit/Add Inertias to Link

This function is retired.  Please call UF_MOTION_set_link_mass_properties
instead.

Environment: Internal  and  External
See Also:
History:
*****************************************************************************/
extern UFUN_CAEEXPORT void FTN(uf6046)(
tag_t *np1,       /* <I>
                     Link object identifier
                  */
double *rp2,      /* <I>
                     Inertias
                  */
double *rp3,      /* <I>
                     Inertia Location
                  */
tag_t *np4,       /* <I>
                     Inertia Matrix object identifier
                  */
int *ir5          /* <O>
                     Error Flag
                           0 = No Errors
                           1 = Link object identifier Not Valid
                           2 = Inertia Matrix object identifier Not Valid
                  */
);

/****************************************************************************
Edit/Add Center of Gravity to Link

This function is retired.  Please call UF_MOTION_set_link_mass_properties
instead.

Environment: Internal  and  External
See Also:
History:
*****************************************************************************/
extern UFUN_CAEEXPORT void FTN(uf6048)(
tag_t *np1,       /* <I>
                     Link object identifier
                  */
double *rp2,      /* <I>
                     COG Location
                  */
int *ir3          /* <O>
                     Error Flag
                         0 = No Errors
                         1 = Link object identifier Not Valid
                  */
);

/****************************************************************************
Add a Marker to a Mechanism.  Markers to add to a mechanism marker represent
points of interest with respect to links. Analysis results can be obtained for
markers.

This function is retired.  Call UF_MOTION_create_marker instead.

Environment: Internal  and  External
See Also:
History:
*****************************************************************************/
extern UFUN_CAEEXPORT void FTN(uf6071)(
tag_t *np1,       /* <I>
                     Link object identifier
                  */
int *ip2,         /* <I>
                     Marker Type
                          0 = Link Inertia CSYS Origin
                              (Not Displayable)
                          1 = Regular Marker
                          2 = Center Of Gravity Marker
                     Note - 0 And 2 Are Available For Internal User
                            Function Use, Only
                  */
double *rp3,      /* <I>
                     Marker Location
                  */
tag_t *nr4,       /* <O>
                     Marker object identifier
                  */
int *ir5          /* <O>
                     Error Flag
                           0 = No Errors
                           1 = Link object identifier Not Valid
                           2 = Type Not Valid
                  */
);

/****************************************************************************
Allows you to create gear joints between two revolutes or a revolute
and slider joint. The contact point defines the point of contact and the
gear ratio. The z-axis of the orientation matrix must be tangent to
the pitch circles.

This function is retired.  Call UF_MOTION_create_joint_coupler instead.

Return:
         Error Code:
        0 = no errors
        1 = revolute  already associated to gear joint
        2 = revolute or slider associated to gear joint
        3 = input joints do not have  a valid common
                 link. Common link must be second object
                 of input joints
        4 = invalid revolute or slider configuration
        5 = Contact Point Causes Invalid Gear Ratio
        6 = Invalid Orientation Matrix
        7 = revolute_obj is an invalid object
        8 = joint_obj is an invalid object

Environment: Internal  and  External

See Also:

History:
 ***************************************************************************/
extern UFUN_CAEEXPORT int UF_MECH_create_gear_joint(
tag_t  revolute_obj ,/* <I>
                     Revolute object identifier
                     */
tag_t  rev_or_slider ,/* <I>
                      Revolute or Slider object identifier
                      */
double contact_point[3] ,/* <I>
                         Contact Point
                         */
double contact_orientation[9] ,/* <I>
                               Contact Point Orientation
                               */
tag_t * joint_obj  /* <O>
                   Gear Joint object identifier
                   */
);

/****************************************************************************
Cycle by mechanism object.  This function takes the object identifier and
object type entered and returns the next object identifier of the same type.
This function is specific to mechanisms.

This routine has been retired.  Call UF_OBJ_cycle_objs_in_part instead.
In past releases UF_OBJ_cycle_objs_in_part would not work for mechanism data.
However, since we now have only a single mechanism per part, it now works.

Environment: Internal  and  External
See Also:
History:
*****************************************************************************/
extern UFUN_CAEEXPORT void FTN(uf6010)(
tag_t *na1, /* <I/O>
               On input this is the previous tag found, use a NULL tag to
               start cycling.  On output, this is the next tag.  A NULL tag
               is output when the cycle is complete.
            */
int *ip2,   /* <I>
               Object Type To Cycle
               85 = Mechanism
               86 = Joint
               87 = Link
               88 = Spring
               90 = Force
               97 = Marker
               98 = Damper
               99 = Torque
            */
int *ir3     /* <O>
                Error Flag
                0 = No errors
                1 = Object type not valid
             */
);




/*********************************************************************************************************
* Creates two types of Edge-To-Face connection between polygon edge(s) and polygon face(s), which
* is obsolete in NX 6.0. This function is retired. GLUE Edge-To-Face can be replaced by 1D connection
* Edge-To-Face. Technically, MATCH Edge-To-Face has no replacement. The workaround for MATCH Edge-To-Face
* is model cleanup stitch edge to face.
*
* Environment: Internal  and  External
* See Also:
*History: Original release was in v17.0
*********************************************************************************************************/


extern UFUN_CAEEXPORT int UF_SF_create_edge_face_conn
(
UF_SF_ef_conn_info_t* uf_ef_conn_info, /* <I> This structure contains the
                                              information needed to create a
                                              edge-face connection mesh
                                       */
tag_t* mesh_tag                        /* <O> edge_face connection mesh recipe tag*/
);
/*******************************************************************************
Creates a contact mesh. Given an element tag outputs the number of
edges this element has and the nodes on those edges.

This function is retired. This function has been replaced with Journamation support.

Environment: Internal  and  External

See Also:

History:
**************************************************************************-----*/
extern UFUN_CAEEXPORT int UF_SF_create_contact_mesh(
    tag_p_t mesh,/* <I/O>
                 pointer to tag of the mesh to be updated. if
                 NULL_TAG, create new mesh.
                 */
                 UF_SF_contact_mesh_data_p_t mesh_data,/* <I>
                                                       Structure to mesh visual properties.
                                                       Set members to
                                                       UF_SF_MESH_VISUAL_NO_CHANGE whose
                                                       attribute you do not want to change.
                                                       */
                                                       UF_SF_orientation_data_p_t orient_data /* <I>
                                                                                              pointer to
                                                                                              UF_SF_orientation_data_structure
                                                                                              */
                                                                                              );

/*****************************************************************************
This user function is used to create a tet mesh on a set of polygon bodies
using the NX Tet mesher. It assumes default geometry abstraction parameters.

This function has been retired.Please see CAE.Mesh3dTetBuilder instead.

Environment: Internal and External
*******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_create_ugs_tet_mesh
(
UF_SF_ugs_tet_mesh_parms_p_t const mesh_parms, /*<I> Parameters which
                                               control the required
                                               tet Mesh */
                                               int num_bodies,   /*<I> Number of polygon bodies to
                                                                 be meshed */
                                                                 tag_p_t const bodies_p, /*<I,len:num_bodies>
                                                                                         Tag of the polygon bodies to
                                                                                         mesh */
                                                                                         tag_p_t mesh_tag        /*<O> tag of the created
                                                                                                                 mesh */
                                                                                                                 );

/*****************************************************************************
This user function is used to create a tet mesh on a set of polygon bodies
using the NX Tet mesher. It also allows user to control geometry abstraction
parameters.

This function has been retired.Please see CAE.Mesh3dTetBuilder instead.

Environment: Internal and External
*******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_create_ugs_tet_mesh_wt_abstraction_control(UF_SF_ugs_tet_mesh_parms_p_t const  mesh_parms,/*<I> Parameters which
                                                                                                                          control the required
                                                                                                                          tet Mesh */
                                                                                                                          UF_SF_ugs_mesh_abstraction_params_p_t const  abs_data_p,/*<I> Abstraction control */
                                                                                                                          int    num_bodies,  /*<I> Number of polygon bodies to
                                                                                                                                              be meshed */
                                                                                                                                              tag_p_t const  bodies_p,/*<I,len:num_bodies>
                                                                                                                                                                      Tag of the polygon bodies to
                                                                                                                                                                      mesh */
                                                                                                                                                                      int    f_partial_surf_mesh,/*<I> 0 == don't allow creation of
                                                                                                                                                                                                 partial surface mesh,
                                                                                                                                                                                                 1 == allow creation of
                                                                                                                                                                                                 partial surface mesh with no format to solve,
                                                                                                                                                                                                 2 == allow creation of
                                                                                                                                                                                                 partial surface mesh with format to solve.
                                                                                                                                                                                                 */
                                                                                                                                                                                                 tag_p_t       mesh_tag   /*<O> tag of the created
                                                                                                                                                                                                                          mesh */
                                                                                                                                                                                                                          );

/*****************************************************************************
This user function returns the mesh parameters used to mesh a given mesh.

This function has been retired.Please see CAE.Mesh2dBuilder instead.

Environment: Internal and External
*******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_ask_ugs_2d_mesh_parms
(
tag_t mesh_tag,    /*<I> The mesh to get mesh
                   parameters for. */
                   UF_SF_ugs_2d_mesh_parms_p_t const mesh_parms   /*<O> The meshing parameters
                                                                  returned */
                                                                  );


/*****************************************************************************
This user function returns the mesh parameters used to mesh a given mesh.

This function has been retired.Please see CAE.Mesh3dTetBuilder instead.

Environment: Internal and External
*******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_ask_ugs_tet_mesh_parms
(
tag_t mesh_tag,                                /*<I> The mesh to get mesh
                                               parameters for. */
                                               UF_SF_ugs_tet_mesh_parms_p_t const mesh_parms  /*<O> The meshing parameters
                                                                                              used to create
                                                                                              mesh_tag. */
                                                                                              );


/*****************************************************************************
This user function is used to create a 2d mesh on a set of polygon faces or
polygon bodies using the NX Surface mesher.

This function has been retired. Please see CAE.Mesh2dBuilder instead.

Environment: Internal and External
*******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_create_ugs_2d_mesh
(
UF_SF_ugs_2d_mesh_parms_p_t const mesh_parms,        /*<I> Parameters which
                                                     control the
                                                     required 2d
                                                     Mesh */
                                                     int num_geoms,          /*<I> Number of
                                                                             geometries to
                                                                             be meshed */
                                                                             tag_p_t const geoms_p,          /*<I,len:num_geoms>
                                                                                                             Tag of the
                                                                                                             geometries to
                                                                                                             mesh.  Could be
                                                                                                             a polygon face
                                                                                                             or a polygon body*/
                                                                                                             tag_p_t mesh_tag                /*<O> Tag of the
                                                                                                                                             created mesh */
                                                                                                                                             );

/*****************************************************************************
This user function is used to create a 2d mesh on a set of polygon faces or
polygon bodies using the NX Surface mesher.

This function has been retired. Please see CAE.Mesh2dBuilder instead.

Environment: Internal and External
*******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_create_ugs_2d_mesh_wt_abstraction_control
(
UF_SF_ugs_2d_mesh_parms_p_t const mesh_parms,        /*<I> Parameters which
                                                     control the
                                                     required 2d
                                                     Mesh */
                                                     UF_SF_ugs_mesh_abstraction_params_p_t const  abs_data_p, /*<I> Parameters for
                                                                                                              abstraction
                                                                                                              control */
                                                                                                              int num_geoms,                                       /*<I> Number of
                                                                                                                                                                   geometries to
                                                                                                                                                                   be meshed */
                                                                                                                                                                   tag_p_t const geoms_p,                               /*<I,len:num_geoms>
                                                                                                                                                                                                                        Tag of the
                                                                                                                                                                                                                        geometries to
                                                                                                                                                                                                                        mesh.  Could be
                                                                                                                                                                                                                        a polygon face
                                                                                                                                                                                                                        or a polygon body*/
                                                                                                                                                                                                                        tag_p_t mesh_tag                                     /*<O> Tag of the
                                                                                                                                                                                                                                                                             created mesh */
                                                                                                                                                                                                                                                                             );


/*****************************************************************************
This user function is used to create a 2d mesh on a set of polygon faces or
polygon bodies using the NX Surface mesher.  It is the same as
UF_SF_create_ugs_2d_mesh, except that this function has 2 additional arguments
(num_hardpoints & hardpoints_p)

This function has been retired. Please see CAE.Mesh2dBuilder instead.

Environment: Internal and External
*******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_create_ugs_2d_mesh_with_hdpts
(
UF_SF_ugs_2d_mesh_parms_p_t const mesh_parms, /*<I> Parameters which
                                              control the
                                              required 2d
                                              Mesh */
                                              int num_geoms,   /*<I> Number of
                                                               polygon geometries to
                                                               be meshed */
                                                               tag_p_t const geoms_p, /*<I,len:num_geoms>
                                                                                      Tag of the
                                                                                      polgyon geometries to
                                                                                      mesh.  Could be
                                                                                      a geometric face
                                                                                      or a sheet body*/
                                                                                      int num_hardpoints,   /*<I> Number of hard
                                                                                                            points to honor
                                                                                                            in the mesh. */
                                                                                                            tag_p_t const hardpoints_p, /*<I,len:num_hardpoints>
                                                                                                                                        Array of tags of the
                                                                                                                                        hardpoints to honor.
                                                                                                                                        These points should
                                                                                                                                        spacially be on the
                                                                                                                                        interior of the polygon face,
                                                                                                                                        and should not be
                                                                                                                                        associated to the polygon face,
                                                                                                                                        but rather just points
                                                                                                                                        out in space. */
                                                                                                                                        tag_p_t mesh_tag             /*<O> Tag of the
                                                                                                                                                                     created mesh */
                                                                                                                                                                     );

/*****************************************************************************
This user function can be used to generate the nodal locations and element
connectivity given a set of 3D planar point loops.
There must be at least one loop, and the direction of the loop points should
be CCW with respect to the plane(element) normal.   All additional loops will
be considers as holes with loop points oriented in the CW direction with
respect to the plane normal.   Loops must not intersect.

This function has been retired. Please see CAE.MeshFromBounbdaryBuilder instead.

Environment: Internal and External
*******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_mesh_2d_loops
(
int num_loops, /*<I> Number of
               loops to
               be meshed */
               int num_of_loop_pts[], /*<I,len:num_loops>
                                      An array containing
                                      the number of points in
                                      each boundary loop*/
                                      double* loop_pts,      /*<I>
                                                             This is an array
                                                             of doubles which correspond to
                                                             the pts in each loop.
                                                             The length of this array is the sum
                                                             of all of the values in num_of_loop_pts
                                                             times 3. */
                                                             double element_size,   /*<I>
                                                                                    The Size of the elements to use for
                                                                                    the interior of the mesh.  */
                                                                                    int element_type,      /*<I>
                                                                                                           The desired Element Type
                                                                                                           (Tris=3, Quads=4)
                                                                                                           Requesting quads can still
                                                                                                           produce some Triangular elements */
                                                                                                           int element_order,     /*<I>
                                                                                                                                  The desired Element Order
                                                                                                                                  (Linear=1)
                                                                                                                                  At this time only linear
                                                                                                                                  elements will be produced  */
                                                                                                                                  int* num_of_nodes,     /*<O> the number of mesh nodes
                                                                                                                                                         generated */
                                                                                                                                                         int** node_ids,        /*<O,len:num_of_nodes >
                                                                                                                                                                                This is an array
                                                                                                                                                                                of int which correspond to
                                                                                                                                                                                the node ids
                                                                                                                                                                                Caller must free up this memory by
                                                                                                                                                                                call UF_free */
                                                                                                                                                                                double** node_locs,    /*<O,len:num_of_nodes*3 >
                                                                                                                                                                                                       This is an array
                                                                                                                                                                                                       of doubles which correspond to
                                                                                                                                                                                                       the nodes generated by the mesher
                                                                                                                                                                                                       Caller must free up this memory by
                                                                                                                                                                                                       call UF_free */
                                                                                                                                                                                                       int* num_of_elements,  /*<O> the number of elements
                                                                                                                                                                                                                              generated */
                                                                                                                                                                                                                              int** element_ids,     /*<O,len:num_of_elements> the elements
                                                                                                                                                                                                                                                     ids */
                                                                                                                                                                                                                                                     int** num_of_element_nodes, /*<O,len:num_of_elements>
                                                                                                                                                                                                                                                                                 the number of nodes in this element */
                                                                                                                                                                                                                                                                                 int** element_connectivity  /*<O,len:num_of_elements*4 >
                                                                                                                                                                                                                                                                                                             This is an array
                                                                                                                                                                                                                                                                                                             of ints which correspond to
                                                                                                                                                                                                                                                                                                             the nodal connectivity for this element
                                                                                                                                                                                                                                                                                                             Elements may be have 3 or 4 nodes and
                                                                                                                                                                                                                                                                                                             these values represent the indexes into
                                                                                                                                                                                                                                                                                                             the node_locs array.
                                                                                                                                                                                                                                                                                                             Caller must free up this memory by
                                                                                                                                                                                                                                                                                                             call UF_free */
                                                                                                                                                                                                                                                                                                             );/*<NON_NXOPEN>*/

/*************************************************************************
*       function to export the expressions to the master part.
*
*
**************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_export_expression(void);

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif /* UF_SF_RETIRING */
