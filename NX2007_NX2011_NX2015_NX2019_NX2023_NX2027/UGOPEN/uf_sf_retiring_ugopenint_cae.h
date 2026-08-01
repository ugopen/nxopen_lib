/****************************************************************************

        Copyright (c) 2012 Siemens Product Lifecycle Management Software Inc.
                         Unpublished - All rights reserved
 

 


 File description:  
          These routines are in the process of being removed from the NX Open API.
          Customers should use the designated replacement routines
          instead of the routines listed here.  Once a routine is placed
          here, it is eligible to be removed in the next release.

***************************************************************************/

#ifndef UF_SF_RETIRING_UGOPENINT_CAE
#define UF_SF_RETIRING_UGOPENINT_CAE
#include <uf_defs.h>
#include <uf_sf_post_datatypes.h>
#include <libugopenint_cae_exports.h>
/***************************************************************************

  ***************************************************************************/

#ifdef __cplusplus
extern "C" {
#endif

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
extern UGOPENINT_CAEEXPORT int UF_SF_POST_animate_set_anim_type(int model_num, int ichoice);

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
extern UGOPENINT_CAEEXPORT int UF_SF_POST_animate_set_anim_num_frames(int model_num, int num_frm);

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
extern UGOPENINT_CAEEXPORT int UF_SF_POST_animate_set_anim_iter(int model_num, logical iter_sw);

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
extern UGOPENINT_CAEEXPORT int UF_SF_POST_animate_set_anim_iters(int model_num, int siter, int eiter);

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
extern UGOPENINT_CAEEXPORT int UF_SF_POST_animate_create_animation(int model_num);

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
extern UGOPENINT_CAEEXPORT int UF_SF_POST_animate_set_anim_cur_frame(int model_num, int cfrm);

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
extern UGOPENINT_CAEEXPORT int UF_SF_POST_animate_set_anim_cur_iter(int model_num, int citer);

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
extern UGOPENINT_CAEEXPORT int UF_SF_POST_animate_step_animation_frame(int model_num, logical truth);

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
extern UGOPENINT_CAEEXPORT int UF_SF_POST_animate_delete_animation(int model_num);




#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif /* UF_RETIRING_UGOPENINT */
