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


/*****************************************************************************
This user function is used to compute auto-element size for polygon bodies.
This method will be replaced by NXOpen.CAE.MeshManager.GetAutoElementSize

Environment: Internal and External
*******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_get_auto_element_size
(
    int     num_objects, /*<I>  No of bodies in objects_p array*/
    tag_p_t objects_p,   /*<I>  list of bodies from which to calculate auto size*/
    double  *esize       /*<O>  Auto size value */
);

/*****************************************************************************
This user function is used to ask the elemnt type name in the current 
solver language.

Environment: Internal and External
*******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_ask_element_type_names
(
    UF_SF_element_type_t element_type, /*<I> Parameters which control the required tet Mesh */    
    char**  element_name_array         /*<O> tag of the created mesh */
);

/* -- the following method is needed by the batch mesher (ufx_batchmeshing.cxx). do not remove -- */
/*****************************************************************************
This user function returns the mesh parameters used to mesh a given mesh.

This function has been retired.Please see CAE.Mesh2dBuilder instead.

Environment: Internal and External
*******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_ask_ugs_2d_mesh_parms
(
    tag_t mesh_tag,                                /*<I> The mesh to get mesh parameters for. */
    UF_SF_ugs_2d_mesh_parms_p_t const mesh_parms   /*<O> The meshing parameters returned */
);

/* -- the following method is needed by the batch mesher (ufx_batchmesing.cxx). do not remove -- */
/*****************************************************************************
This user function returns the mesh parameters used to mesh a given mesh.

This function has been retired.Please see CAE.Mesh3dTetBuilder instead.

Environment: Internal and External
*******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_ask_ugs_tet_mesh_parms
(
    tag_t mesh_tag,                                /*<I> The mesh to get mesh parameters for. */
    UF_SF_ugs_tet_mesh_parms_p_t const mesh_parms  /*<O> The meshing parameters used to create mesh_tag. */
);


#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY
#endif /* UF_SF_RETIRING */
