/*******************************************************************************
             Copyright (c) 1999-2003 Unigraphics Solutions Inc.
                       Unpublished - All Rights Reserved



File description:
   Open API modeling routines to create, edit and inquire about blends.

*****************************************************************************/

#ifndef UF_MODL_TREX_H_INCLUDED
#define UF_MODL_TREX_H_INCLUDED


/*==========================================================================

  ==========================================================================*/

#include <uf_defs.h>
#include <uf_modl_types.h>
#include <libufun_exports.h>

enum UF_MODL_TREX_algorithm_e
{
    UF_MODL_TREX_ALGORITHM_NONE=0,
    UF_MODL_TREX_ALGORITHM_COUNT,  /* Insert new versions above this line */
    UF_MODL_TREX_ALGORITHM_CURRENT=UF_MODL_TREX_ALGORITHM_COUNT - 1
};

enum UF_MODL_TREX_extend_method_e
{
    UF_MODL_TREX_C2=0,
    UF_MODL_TREX_LINEAR,
    UF_MODL_TREX_REFLECTED,
    UF_MODL_TREX_NATURAL
};
typedef enum UF_MODL_TREX_extend_method_e
             UF_MODL_TREX_extend_method_t;

enum UF_MODL_TREX_to_option_e
{
    UF_MODL_TREX_DISTANCE=0,
    UF_MODL_TREX_PERCENT,
    UF_MODL_TREX_SURFACE
};
typedef enum UF_MODL_TREX_to_option_e
             UF_MODL_TREX_to_option_t;

enum UF_MODL_TREX_region_option_e
{
    UF_MODL_TREX_KEEP=0,
    UF_MODL_TREX_REMOVE
};
typedef enum UF_MODL_TREX_region_option_e
             UF_MODL_TREX_region_option_t;

/*
 * Trim extend target/tool dataset
 */
struct UF_MODL_TREX_data_set_s
{
    tag_t                collector;
    double               extend_val;
    double               offset_val;
    int                  reversed;
};
typedef struct UF_MODL_TREX_data_set_s
               UF_MODL_TREX_data_set_t, *UF_MODL_TREX_data_set_p_t;

/*
 * Trim extend application data
 */
struct UF_MODL_TREX_appl_data_s
{
    int                           num_targets;       /* Number of target data sets */
    UF_MODL_TREX_data_set_p_t     *targets;          /* Array of target data sets */
    int                           num_tools;         /* Number of tool data sets */
    UF_MODL_TREX_data_set_p_t     *tools;            /* Array of tool data sets */

    UF_MODL_TREX_extend_method_t  extend_method;     /* Extend method */
    UF_MODL_TREX_to_option_t      to_option;         /* To option */
    UF_MODL_TREX_region_option_t   region_option;     /* Region option */

    int                  make_corner;       /* Make corner flag */
    int                  keep_boundaries;   /* Keep boundaries flag */
    int                  extract_sheets;    /* Extract sheets flag */

    double               dist_tol;          /* Distance Tolerance */

    int                  algorithm_version; /* Future Use */
};
typedef struct UF_MODL_TREX_appl_data_s
               UF_MODL_TREX_appl_data_t, *UF_MODL_TREX_appl_data_p_t;

#ifdef __cplusplus
extern "C" {
#endif

/********************************************************************
Creates a trim and extend feature.

This is a complete interface to create a trim/extend feature. Extends the
target by a given distance or until a target. If extended until a tool then
the target will be trimmed by the tool and optionally can modify the tool
also to make a corner between the target and the tool.

Following types of collectors allowed for a target and tool.
  1. A connected set of free edges 
  2. A connected set of faces
     a) Could be a whole sheet body
     b) A connected set of faces of a sheet body

The collector is a Smart Container. For edges the collector should be created
with UF_MODL_create_smart_wireframe_container. For faces the collector should
be created with UF_MODL_create_smart_face_container.

For now only "Body Faces" are allowed for face collectors.

In case of "connected set of free edges" required extension distances are 
computed internally. No extensions are done if they are "a set of faces".
 
If successful, it returns the tag for the feature created. If not successful,
it returns a valid error code.

Return:
   0  : if successful
 !=0  : if there is a failure. Refer to TREX_* error codes in in uf_modl_error.h.

Environment: Internal  and  External

See Also:  UF_MODL_TREX_ask_trim_extend

History: Originally released in NX 2.0.1
********************************************************************/
extern UFUNEXPORT int UF_MODL_TREX_create_trex_feature
(
    UF_MODL_TREX_appl_data_p_t   feature_data,  /* <I> : Pointer to the structure 
                                                       containing defining data for
                                                       the trim extend operation
                                                */ 
    tag_t*                       feature          /* <O> : trim extend feature identifier 
                                                */   
);

/********************************************************************
Edits a trim and extend feature.

Edits the parameters of a trim/extend feature. All the creation parameters are available
for editing also. One can query for the creation parameters by calling UF_MODL_TREX_ask_trim_extend.
 
Return:
   0  : if successful
 !=0  : if there is a failure. Refer to TREX_* error codes in in uf_modl_error.h.

Environment: Internal  and  External

See Also:  UF_MODL_TREX_ask_trim_extend

History: Originally released in NX 2.0.1
********************************************************************/
extern UFUNEXPORT int UF_MODL_TREX_edit_trex_feature
(   
    UF_MODL_TREX_appl_data_p_t     feature_data,   /* <I> Pointer to the structure
                                                         containing defining data
                                                         for the trimextend operation
                                                    */ 
    tag_t                          feature         /* <I> Offset curve on face 
                                                         identifier 
                                                    */ 
);

/********************************************************************
Queries a trim and extend feature.

Returns the creation data for a trim / extend feature. Refer to UF_MODL_trex_input_p_t for
detailed information on the contents.
 
If successful, it returns the input data associated with the feature. If not successful,
it returns a valid error code.

Return:
   0  : if successful
 !=0  : if there is a failure. Refer to TREX_* error codes in in uf_modl_error.h.

Environment: Internal  and  External

See Also:  UF_MODL_TREX_edit_trex_feature
           UF_MODL_TREX_free_trex_data

History: Originally released in NX 2.0.1
********************************************************************/
extern UFUNEXPORT int UF_MODL_TREX_ask_trim_extend
(
   tag_t                      feature,           /* <I> The trim/extend feature tag */
   UF_MODL_TREX_appl_data_p_t feature_data       /* <OF> The feature data */
);

/********************************************************************
Initializes the trim and extend feature input data.

Return:
   0  : if successful
 !=0  : if there is a failure. Refer to TREX_* error codes in in uf_modl_error.h.

Environment: Internal  and  External

See Also:  UF_MODL_TREX_ask_trim_extend

History: Originally released in NX 2.0.1
********************************************************************/
extern UFUNEXPORT int UF_MODL_TREX_init_trex_data
(
   UF_MODL_TREX_appl_data_p_t  feature_data
);

/********************************************************************
Initializes the trim and extend target tool data set.

Return:
   0  : if successful
 !=0  : if there is a failure. Refer to TREX_* error codes in in uf_modl_error.h.

Environment: Internal  and  External

History:
********************************************************************/
extern UFUNEXPORT int UF_MODL_TREX_init_trex_data_set
(
   UF_MODL_TREX_data_set_p_t  feature_data_set
);

/********************************************************************
Frees the trim and extend feature input data.

Return:
   0  : if successful
 !=0  : if there is a failure. Refer to TREX_* error codes in in uf_modl_error.h.

Environment: Internal  and  External

See Also:  UF_MODL_TREX_ask_trim_extend

History: Originally released in NX 2.0.1
********************************************************************/
extern UFUNEXPORT int UF_MODL_TREX_free_trex_data
(
   UF_MODL_TREX_appl_data_p_t feature_data
);

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif     /* UF_MODL_TREX_H_INCLUDED */
