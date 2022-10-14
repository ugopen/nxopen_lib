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

#include <libufun_cae_exports.h>

/***************************************************************************

  ***************************************************************************/

#ifdef __cplusplus
extern "C" {
#endif


/* The next two enums and three structures aren't used anymore.  Moving from
uf_sf_types.h to here in NX7. */

/*  Element types supported by Auto Solid Mesher  */
enum UF_SF_asm_element_types_e
{
    UF_SF_ASM_SYSTEM_DEFAULT_TYPE = 0,  /* System default. */
    UF_SF_ASM_TETRA,                    /* Elements are tetrahedral. */
    UF_SF_ASM_TETRA_10                  /* Elements are tetrahedral with 10
                                           nodes. */
};
typedef enum UF_SF_asm_element_types_e UF_SF_asm_element_types_t;


/*  Auto Solid Mesher contact types  */
enum UF_SF_contact_types_e
{
    UF_SF_ASM_FIXED = 0,
    UF_SF_ASM_FREE
};
typedef enum UF_SF_contact_types_e UF_SF_contact_types_t;


/*********************** ASM attributes and parameters ************************/

/* Mesh attributes related to model geometry */
struct  UF_SF_asm_mesh_attributes_data_s
{
    double              max_elem_size;  /*  Maximum Element Size        */
    double              min_elem_size;  /*  Minimum Element Size        */
    int                 check_aspect_ratio;     /*  0 = OFF  , 1 = ON   */
    double              aspect_ratio;   /*  Aspect ratio value > 0.     */
    int                 curvature_control;      /*  0 = OFF  , 1 = ON   */
    double              curvature_factor;       /*  Curvature value > 0.*/
    int                 small_feature_control;  /*  0 = OFF  , 1 = ON   */
    double              small_feature_factor;   /*  Feature factor value > 0. */
    UF_SF_contact_types_t  contact_type;        /*  FIXED or FREE       */
};
typedef struct  UF_SF_asm_mesh_attributes_data_s
                                             UF_SF_asm_mesh_attributes_data_t,
                                            *UF_SF_asm_mesh_attributes_data_p_t;

/* Parameters unique to the Auto Solid Mesher */
struct UF_SF_asm_mesh_parameters_data_s
{
    UF_SF_asm_element_types_t  element_type;    /*  TETRA or TETRA_10   */
    double              def_elem_size;          /*  Default Element Size*/
    int                 model_augmentation;     /*  0 = OFF  , 1 = ON   */
    int                 surface_smoothing;      /*  0 = OFF  , 1 = ON   */
    int                 explicit_smoothing;     /*  0 = OFF  , 1 = ON   */
    int                 midnode_snapping;       /*  0 = OFF  , 1 = ON   */
};
typedef struct UF_SF_asm_mesh_parameters_data_s
                                             UF_SF_asm_mesh_parameters_data_t,
                                            *UF_SF_asm_mesh_parameters_data_p_t;

/* Mesh attributes and parameters structure */
struct UF_SF_asm_mesh_data_s
{
    UF_SF_asm_mesh_attributes_data_p_t  attribs;
    UF_SF_asm_mesh_parameters_data_p_t  params;

};
typedef struct UF_SF_asm_mesh_data_s  UF_SF_asm_mesh_data_t,
                                     *UF_SF_asm_mesh_data_p_t;


/*------------------------------------------------------------------------
Creates scenario part file from parent part (non scenario part file).

Calls to this function should be replaced with calls to
UF_SF_create_scenario_nx.

The input name should be shorter than 26 characters and should not
include path name. The reason for that is the scenario subdirectory is
associated to the master model part.

Environment: Internal  and  External

See Also:

History:
*------------------------------------------------------------------*/
extern UFUN_CAEEXPORT int UF_SF_create_scenario(
char* scenario_name ,/* <I>
                     Name of Scenario part file to create.
                     */
tag_t* new_scenario_tag /* <O>
                         Tag of created Scenario part file.
                         */
);

/*******************************************************************************-
 *
 * This routine try to load VKI meshing library.
 *
 * Environment: Internal & External
 *
 * See Also:
 *
 * History: Released in v18.0
 *******************************************************************************/
extern UFUN_CAEEXPORT int  UF_SF_load_vki_mesh_lib(void);

/*******************************************************************************-
 *
 * This routine try to load VDM library.
 *
 * Environment: Internal & External
 *
 * See Also:
 *
 * History: Released in v18.0
 *******************************************************************************/
extern UFUN_CAEEXPORT int  UF_SF_load_vdm_lib(void);

/*******************************************************************************-
 *
 * This routine try to load Hyper Opt library.
 *
 * Environment: Internal & External
 *
 * See Also:
 *
 * History: Released in v18.0
 *******************************************************************************/
extern UFUN_CAEEXPORT int  UF_SF_load_hypopt_lib(void);

/*******************************************************************************-
 *
 * This routine try to load ADAMS library.
 *
 * Environment: Internal & External
 *
 * See Also:
 *
 * History: Released in v18.0
 *******************************************************************************/
extern UFUN_CAEEXPORT int  UF_SF_load_adams_lib(void);


extern UFUN_CAEEXPORT int UF_SF_POST_add_post_view( int post_view_num );

extern UFUN_CAEEXPORT int UF_SF_POST_load_post_view( int post_view_num );

extern UFUN_CAEEXPORT int UF_SF_POST_clone_post_view( int post_view_num );

extern UFUN_CAEEXPORT int UF_SF_POST_set_post_view_name( int    post_view_num , /*<I> The new name length */

                                                     char** post_view_name /* <I,len:post_view_num> The new name */);

extern UFUN_CAEEXPORT int UF_SF_POST_delete_post_view( int post_view_num );

/*==========================================================================*
 *
 *   FUNCTION :
 *    UF_SF_POST_set_active_view()
 *
 *   DESCRIPTION :
 *    
 *
 *   INPUT
 *   
 *
 *   RETURN
 *    Value = 0          when successful
 *
 *=========================================================================*/
extern UFUN_CAEEXPORT int UF_SF_POST_set_active_view( int view_num );

/*==========================================================================*
 *
 *   FUNCTION :
 *    UF_SF_POST_add_to_selected_views()
 *
 *   DESCRIPTION :
 *    
 *
 *   INPUT
 *   
 *
 *   RETURN
 *    Value = 0          when successful
 *
 *=========================================================================*/
extern UFUN_CAEEXPORT int UF_SF_POST_add_to_selected_views( int view_num );

/*==========================================================================*
 *
 *   FUNCTION :
 *    UF_SF_POST_delete_from_selected_views()
 *
 *   DESCRIPTION :
 *    
 *
 *   INPUT
 *   
 *
 *   RETURN
 *    Value = 0          when successful
 *
 *=========================================================================*/
extern UFUN_CAEEXPORT int UF_SF_POST_delete_from_selected_views( int view_num );

/*=====================================21====================================*
 *
 *   FUNCTION :
 *
 *   UF_SF_POST_is_initialized(logical *is_initialized)
 *
 *   DESCRIPTION :
 *
 *   This function checks if Post if initialized
 *
 *   INPUT
 *
 *
 *   OUTPUT
 *
 *    is_initialized     - TRUE if initialized
 *                       - FALSE if not 
 *   RETURN
 *     value= 0       when successful.
 *=========================================================================*/
extern UFUN_CAEEXPORT int UF_SF_POST_is_initialized(
     logical *is_initialized  /* <O>  if Post is initialized */
);

/*==========================================================================*
 *
 *   FUNCTION :
 *    UF_SF_POST_post_view_layout()
 *
 *   DESCRIPTION :
 *    This function displays the screen in standard layouts of 2,3,4,6 & 9 views.
 *
 *   INPUT
 *   UF_SF_POST_layout_type_t :- type of layout wanted 
 *
 *   RETURN
 *    Value = 0          when successful
 *
 *=========================================================================*/
extern UFUN_CAEEXPORT int UF_SF_POST_view_layout( UF_SF_POST_layout_type_t layout_option );


/*==========================================================================
*  
*   FUNCTION :  
*    UF_SF_post_set_target()  
*  
*   DESCRIPTION :  
*    This function sets target
*    
*   INPUT
*     target
*      
*   RETURN :  
*    Value = 0          when successful  
*  
*=========================================================================*/
extern UFUN_CAEEXPORT int UF_SF_post_set_target(UF_SF_POST_target_t target);
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


#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif /* UF_SF_RETIRING */
