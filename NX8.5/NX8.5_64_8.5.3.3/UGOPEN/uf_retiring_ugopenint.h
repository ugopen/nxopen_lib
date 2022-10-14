/****************************************************************************

           Copyright (c) 2000 Unigraphics Solutions Inc.
                         Unpublished - All rights reserved

 File description:  
          These routines are in the process of being removed from the UG/Open
          product.  Customers should use the designated replacement routines
          instead of the routines listed here.  Once a routine is placed
          here, it is eligible to be removed in the next release of Unigraphics.
 
****************************************************************************/

/*
 

*/

#ifndef UF_RETIRING_UGOPENINT
#define UF_RETIRING_UGOPENINT
#include <uf_defs.h>
#include <uf_sf_post_datatypes.h>
#include <libugopenint_exports.h>
/***************************************************************************

  ***************************************************************************/

#ifdef __cplusplus
extern "C" {
#endif


/*****************************************************************
Displays a WorldView help file page given the map file and the
WorldView locator.  This routine allows access to the help system
one level below the level of the routines UF_HELP_display_context and
UF_HELP_display_current_context. In the case of WorldView, the
UG translation map file contains the name of the map file and a
locator within the file.  It also allows the displaying of a WorldView
page by directly specifying the map file and locator.  Finally it
invokes WorldView if the program is not already running then loads
and positions the requested document page for viewing.

Environment: Internal
See Also:
History:
 *****************************************************************/
extern UGOPENINTEXPORT int UF_HELP_display_wv(
char * map_file ,/* <I>
                 Name of map file to use.
                 */
char * locator  /* <I>
                World View locator
                */
);


/*===================================2======================================*
 *   FUNCTION :
 *    UF_SF_POST_animate_set_anim_type
 *
 *   DESCRIPTION :
 *    This function sets the animation type.
 *    
 *   RETURN :
 *    Value = 0          when successful
 *
 *=========================================================================*/
extern UGOPENINTEXPORT int UF_SF_POST_animate_set_anim_type(int model_num, int ichoice);

/*===================================2======================================*
 *   FUNCTION :
 *    UF_SF_POST_animate_set_anim_num_frames
 *
 *   DESCRIPTION :
 *    This function sets the number of frames
 *    
 *   RETURN :
 *    Value = 0          when successful
 *
 *=========================================================================*/
extern UGOPENINTEXPORT int UF_SF_POST_animate_set_anim_num_frames(int model_num, int num_frm);

/*===================================2======================================*
 *   FUNCTION :
 *    UF_SF_POST_animate_set_anim_iter
 *
 *   DESCRIPTION :
 *    This function sets the whether the animation is by teration or by frames
 *    
 *   RETURN :
 *    Value = 0          when successful
 *
 *=========================================================================*/
extern UGOPENINTEXPORT int UF_SF_POST_animate_set_anim_iter(int model_num, logical iter_sw);

/*===================================2======================================*
 *   FUNCTION :
 *    UF_SF_POST_animate_set_anim_iters
 *
 *   DESCRIPTION :
 *    This function sets start and end iters of the system
 *    
 *   RETURN :
 *    Value = 0          when successful
 *
 *=========================================================================*/
extern UGOPENINTEXPORT int UF_SF_POST_animate_set_anim_iters(int model_num, int siter, int eiter);

/*===================================2======================================*
 *   FUNCTION :
 *    UF_SF_POST_animate_create_animation
 *
 *   DESCRIPTION :
 *    This function creates the animation.
 *    
 *   RETURN :
 *    Value = 0          when successful
 *
 *=========================================================================*/
extern UGOPENINTEXPORT int UF_SF_POST_animate_create_animation(int model_num);

/*===================================2======================================*
 *   FUNCTION :
 *    UF_SF_POST_animate_set_anim_cur_frame
 *
 *   DESCRIPTION :
 *    This function sets the current animation frame.
 *    
 *   RETURN :
 *    Value = 0          when successful
 *
 *=========================================================================*/
extern UGOPENINTEXPORT int UF_SF_POST_animate_set_anim_cur_frame(int model_num, int cfrm);

/*===================================2======================================*
 *   FUNCTION :
 *    UF_SF_POST_animate_set_anim_cur_iter
 *
 *   DESCRIPTION :
 *    This function sets the current animation iteration.
 *    
 *   RETURN :
 *    Value = 0          when successful
 *
 *=========================================================================*/
extern UGOPENINTEXPORT int UF_SF_POST_animate_set_anim_cur_iter(int model_num, int citer);

/*===================================2======================================*
 *   FUNCTION :
 *    UF_SF_POST_animate_step_animation_frame
 *
 *   DESCRIPTION :
 *    This function steps animations frame by frame.
 *    
 *   RETURN :
 *    Value = 0          when successful
 *
 *=========================================================================*/
extern UGOPENINTEXPORT int UF_SF_POST_animate_step_animation_frame(int model_num, logical truth);

/*===================================2======================================*
 *   FUNCTION :
 *    UF_SF_POST_animate_delete_animation
 *
 *   DESCRIPTION :
 *    This function deletes the animation type.
 *    
 *   RETURN :
 *    Value = 0          when successful
 *
 *=========================================================================*/
extern UGOPENINTEXPORT int UF_SF_POST_animate_delete_animation(int model_num);




#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif /* UF_RETIRING_UGOPENINT */
