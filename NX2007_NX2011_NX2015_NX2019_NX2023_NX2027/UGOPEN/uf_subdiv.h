/*******************************************************************************
             Copyright (c) 1998-2000 Unigraphics Solutions, Inc.
                       Unpublished - All Rights Reserved



File description:

Open C API interface to the routines to subdivide a face using an isocline method.

The subdiv functions provide routines that subdiv features. The subdiv feature
splits a face using an isocline method.  These functions enable you to:
.    Obtain the parameters used for a subdiv feature.
.    Obtain the type of subdiv feature.
.    Create a subdiv feature
.    Edit a subdiv feature.
.    Free space allocated by UF_SUBDIV_ask_parms.

******************************************************************************/

/* Do not process this file again if already included */
#ifndef UF_SUBDIV_H_INCLUDED
#define UF_SUBDIV_H_INCLUDED

/*****************************************************************************

******************************************************************************/

/**************************************************************************
 *
 *   Include files necessary for UF_SUBDIV feature definition
 *
 **************************************************************************/
#include <uf_defs.h>
#include <libufun_exports.h>

/**************************************************************************

 **************************************************************************/
#ifdef __cplusplus
extern "C" {
#endif


/**************************************************************************
 *
 *    UF_SUBDIV data definitions (#defines, enums, typedefs, etc.)
 *
 **************************************************************************/

enum UF_SUBDIV_type_e
{
    UF_SUBDIV_ISOCLINE = 1  /* Subdivide by isocline */
} ;
typedef enum UF_SUBDIV_type_e UF_SUBDIV_type_t, *UF_SUBDIV_type_p_t;

struct UF_SUBDIV_isocline_s
{
    tag_t body_tag;             /* The body to apply the feature to */
    tag_t *excluded_faces;      /* <len:face_count>Array of excluded faces or NULL if not used
                                   The excluded faces are not considered
                                   when applying the feature.
                                */
    int   face_count;           /* Number of faces in the exclude array */
    tag_t direction;            /* SO direction to use  for the isocline
                                   direction.  If NULL_TAG is used, then
                                   0,0,1 of the WCS will be created for
                                   the direction vector tag and used.
                                */
    char  *angle_str;           /* String value of the angle expression
                                   in degrees. This expression is then
                                   evaluated for the isocline angle.
                                */
    tag_t second_direction;     /* Optional SO second direction to apply
                                   to the steep faces from the first
                                   direction. This must not be parallel
                                   with the first direction. It applies a second
                                   isocline direction to the resultant steep
                                   faces from the first direction using the
                                   same angle expression. If this option
                                   is used, the angle expression must be
                                   positive.*/
} ;
typedef struct UF_SUBDIV_isocline_s UF_SUBDIV_isocline_t,
               *UF_SUBDIV_isocline_p_t;

union UF_SUBDIV_data_structures_union
{
    UF_SUBDIV_isocline_p_t    subdiv_type1; /*
                                            Data for the isocline type subdiv
                                            feature.
                                            */
};
typedef union UF_SUBDIV_data_structures_union UF_SUBDIV_data_structures_u,
                                           *UF_SUBDIV_data_structures_p_u;
/************************************************************************
 *
 *   UF_SUBDIV function interface
 *
 ************************************************************************/

/**********************************************************************
Creates a subdiv feature. The subdiv_type contains the method to use
for splitting faces. It indicates the type of parameters used in the
subdiv_structure_ptr structure. The output of this function is the
object identifier associated to the subdiv feature.

Environment: Internal  and  External

See Also: 

History: Originally released in V15.0
**********************************************************************/
extern UFUNEXPORT int UF_SUBDIV_create
    (
    UF_SUBDIV_type_t subdiv_type,       /* <I>
                                        type of subdiv feature
                                        */
    UF_SUBDIV_data_structures_p_u subdiv_structure_pointer,
                                        /* <I>
                                        pointer to one of the subdiv
                                        data structures
                                        */
    tag_p_t subdiv_tag                  /* <O>
                                        object identifier of the
                                        subdiv feature
                                        */
);

/**********************************************************************
Edits a subdiv feature. The subdiv_type contains the type of subdiv
feature being edited. It indicates the type of parameters used in the
subdiv_structure_ptr structure.

Environment: Internal  and  External

See Also: UF_SUBDIV_create

History: Originally released in V15.0
**********************************************************************/
extern UFUNEXPORT int UF_SUBDIV_edit
    (
    UF_SUBDIV_type_t subdiv_type,       /* <I>
                                        type of subdiv feature
                                        */
    UF_SUBDIV_data_structures_p_u subdiv_structure_pointer,
                                        /* <I>
                                        pointer to one of the subdiv
                                        data structures
                                        */
    tag_t subdiv_tag                    /* <I>
                                        object identifier of the
                                        subdiv feature
                                        */
    );

/**********************************************************************
Returns the parameters used for a subdiv feature. Given a subdiv
feature tag, determines the subdiv_type and the parameters for the
type in the subdiv_structure_ptr structure.

Environment: Internal  and  External

See Also: UF_SUBDIV_free
for freeing the data structures allocated by this routine.
         

History: Originally released in V15.0
**********************************************************************/
extern UFUNEXPORT int UF_SUBDIV_ask_parms
    (
    tag_t subdiv_tag,                   /* <I>
                                        Object identifier of the
                                        subdiv feature
                                        */
    UF_SUBDIV_type_p_t subdiv_type,     /* <O>
                                        type of subdiv feature
                                        */
    UF_SUBDIV_data_structures_p_u subdiv_structure_pointer
                                        /* <OF,free:UF_SUBDIV_free>
                                        pointer to one of the subdiv
                                        data structures.  This must be freed
                                        by calling UF_SUBDIV_free.
                                        */
    );

/**********************************************************************
This function frees any data retrieved via the ask_parms function.
Call UF_SUBDIV_free after a call to UF_SUBDIV_ask_parms.

Environment: Internal  and  External

See Also: UF_SUBDIV_create

History: Originally released in V15.0
**********************************************************************/
extern UFUNEXPORT int UF_SUBDIV_free
    (
    UF_SUBDIV_type_t subdiv_type,       /* <I>
                                        type of subdiv feature
                                        */
    UF_SUBDIV_data_structures_p_u subdiv_structure_pointer
                                        /* <I>
                                        pointer to one of the subdiv
                                        data structures
                                        */
    );

/**********************************************************************
This function returns the type of subdiv feature.Given a subdiv feature tag,
determines the subdiv_type.

Environment: Internal  and  External

See Also:  UF_SUBDIV_create

History: Originally released in V15.0
**********************************************************************/
extern UFUNEXPORT int UF_SUBDIV_ask_type
    (
    tag_t subdiv_tag,                   /* <I>
                                        object identifier of the
                                        subdiv feature
                                        */
    UF_SUBDIV_type_p_t subdiv_type      /* <O>
                                        type of subdiv feature
                                        */
    );


#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif /* UF_SUBDIV_H_INCLUDED */
