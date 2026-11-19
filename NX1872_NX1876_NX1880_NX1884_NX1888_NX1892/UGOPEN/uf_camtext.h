/*******************************************************************************
                Copyright (c) 2002 Unigraphics Solutions, Inc.
                      Unpublished - All rights reserved
******************************************************************************
 *****************************************************************************
 *
 *    
 * 
 *
 * File description:
 *
 * This file contains the Open C API interface to text geometry in CAM.  
 * Text geometry includes drafting note and drafting label objects.
 *
 * The CAM text geometry routines in this file enable you to:
 *   . Append entities to CAM geometry
 *   . Get CAM geometry items
 *   . Delete CAM geometry
 *   . Get the item entity
 *   . Delete a sigle item from CAM geometry
 *
 ******************************************************************************/
#ifndef UF_CAMTEXT_H_INCLUDED
#define UF_CAMTEXT_H_INCLUDED


#include <uf.h>
#include <uf_defs.h>
#include <uf_param_indices.h>
#include <libufun_cam_exports.h>


#ifdef __cplusplus
extern "C" {
#endif

/*
   **************************************************************************
   ***************************     Definitions    ***************************
   **************************************************************************
*/

/*
   **************************************************************************
   ***************************     Structures     ***************************
   **************************************************************************
*/

/* 
 * An object which is used to access a CAM geometry. 
 */
typedef void  *UF_CAMTEXT_item_t;

/* 
 * The following information shows the objects using the Text geometry.
 * An error code is returned by the functions if a wrong type 
 * of objects uses the text geometry.
 *
 *   Mill text geometry Group:   
 *     Text Geometry
 *
 *   Planar Text Operation: 
 *     Text Geometry
 *
 *   Surface Contouring with Text drive method Operation:
 *     Text Geometry
 *
 */


/*
   **************************************************************************
   ******************     Functions Relating to Geometry    *****************
   **************************************************************************
*/

/***************************************************************************
 *
 * Appends a list of geometry entities to the object .
 *
 * The allowed types of entities are drafting note and drafting label objects.
 * If the entity list contains any invalid entities, an error code is returned
 * and no geometry entity is appended.
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * History: Released in NX2.0
********************************************************************** */
extern UFUN_CAMEXPORT int UF_CAMTEXT_append_items
(
    tag_t                   object_tag,       /* <I> the parent object of the 
                                                     geometry */
    int                     count,            /* <I> the count of geometry entities */
    tag_t                   *entity_list      /* <I,len:count> the list of geometry entities */
);
                   
/***************************************************************************
 *
 * Gets all the text geometry items from the object.
 *
 * Environment: Internal  and  External
 *
 * See Also: 
 * History: Released in NX2.0
********************************************************************** */
extern UFUN_CAMEXPORT int UF_CAMTEXT_ask_items
(
    tag_t                 object_tag,       /* <I>  the parent object of the 
                                                    geometry */
    int                   *count,           /* <O>  the count of geometry items */
    UF_CAMTEXT_item_t     **items           /* <OF,len:count> the list of geometry items
                                                    it must be freed using UF_free */
);
                   
/***************************************************************************
 *
 * Deletes all the text geometry items from the object.
 *
 * Environment: Internal  and  External
 *
 * See Also: 
 * History: Released in NX2.0
 ***************************************************************************/
extern UFUN_CAMEXPORT int UF_CAMTEXT_delete_geometry
(
    tag_t              object_tag           /* <I> the parent object of the 
                                                   geometry */
);
                   
/***************************************************************************
 *
 * Gets the geometry entity of the item.
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * History: Released in NX2.0
********************************************************************** */
extern UFUN_CAMEXPORT int UF_CAMTEXT_ask_item_entity
(
    UF_CAMTEXT_item_t     item,             /* <I> the geometry item */
    tag_t                 *entity           /* <O> the item entity */
);
                   
/***************************************************************************
 *
 * Deletes one text geometry item from the object.
 *
 * Environment: Internal  and  External
 *
 * See Also: 
 * History: Released in NX2.0
********************************************************************** */
extern UFUN_CAMEXPORT int UF_CAMTEXT_delete_item
(
    tag_t                 object_tag,       /* <I> the parent object of the 
                                                   geometry */
    UF_CAMTEXT_item_t     item              /* <I> the item to be deleted */
);

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif /* UF_CAMTEXT_H_INCLUDED */
