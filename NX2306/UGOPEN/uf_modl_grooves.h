/*****************************************************************************
             Copyright (c) 1998-2000 Unigraphics Solutions Inc.
                       Unpublished - All Rights Reserved                       



File description: 
    Open API modeling routines to create, edit and inquire about grooves.

*****************************************************************************/

#ifndef UF_MODL_GROOVES_H_INCLUDED
#define UF_MODL_GROOVES_H_INCLUDED


/***************************************************************************

  ***************************************************************************/

#include <uf_defs.h>
#include <uf_modl_types.h>
#include <libufun_exports.h>

#ifdef __cplusplus
extern "C" {
#endif

/********************************************************************
Creates a ball groove feature by inputting its location, direction,
diameter and width. Along with these items a placement face is
needed to determine which face the ball groove is associated to. The
output of this function is the object identifier associated to the ball
groove.

Environment: Internal  and  External
See Also:
History:
********************************************************************/
extern UFUNEXPORT int UF_MODL_create_ball_groove(
double  location[3] ,/* <I>
                     Ball groove location.
                     */
double  direction[3] ,/* <I>
                      Ball groove direction
                      */
char * diame ,/* <I>
              Ball groove diameter.
              */
char * width ,/* <I>
              Ball groove width.
              */
tag_t  face ,/* <I>
             Face for the RPO constraint.
             */
tag_t * feature_obj_id  /* <O>
                        Feature object identifier of created ball groove
                        */
);

/********************************************************************
Gets U groove parameters.

Environment: Internal  and  External
See Also:
History:
********************************************************************/
extern UFUNEXPORT int UF_MODL_ask_u_groove_parms(
tag_t feature_obj_id ,/* <I>
                      A feature object identifier.
                      */
int  edit ,/* <I>
           This is an unused flag. It was used to determine
           whether to return the right-hand side or both sides
           of an expression. Currently, both sides of an
           expression are returned.
           */
char ** groove_dia ,/* <OF>
                    Groove diameter.  This must be freed by
                    calling UF_free.
                    */
char ** width ,/* <OF>
               Groove width.  This must be freed by
               calling UF_free.
               */
char ** corner_rad  /* <OF>
                    Groove corner radius.  This must be freed by
                    calling UF_free.
                    */
);

/********************************************************************
Gets rectangular groove parameters.

Environment: Internal  and  External
See Also:
History:
********************************************************************/
extern UFUNEXPORT int UF_MODL_ask_rect_groove_parms(
tag_t feature_obj_id ,/* <I>
                      A feature object identifier
                      */
int edit ,/* <I>
          This is an unused flag. It was used to determine
          whether to return the right-hand side or both sides
          of an expression. Currently, both sides of an
          expression are returned.
          */
char  **groove_dia ,/* <OF>
                    Groove diameter.  This must be freed by
                    calling UF_free.
                    */
char  **width  /* <OF>
               Groove width.  This must be freed by
               calling UF_free.
               */
);

/********************************************************************
Gets ball groove parameters.

Environment: Internal  and  External
See Also:
History:
********************************************************************/
extern UFUNEXPORT int UF_MODL_ask_ball_groove_parms(
tag_t feature_obj_id ,/* <I>
                      A feature object identifier
                      */
int  edit ,/* <I>
           This is an unused flag. It used to determine whether
           to return the right-hand side or both sides of an
           expression. Currently, both sides of an expression
           are returned.
           */
char ** groove_dia ,/* <OF>
                    Groove diameter.  This must be freed by calling
                    UF_free.
                    */
char ** ball_dia  /* <OF>
                  Ball diameter.  This must be freed by calling
                  UF_free.
                  */
);

/********************************************************************
Creates a rectangular groove feature by inputting its location,
direction, diameter and width. Along with these items a placement
face is needed to determine which face the groove is associated to.
The output of this function is the object identifier associated to the
rectangular groove.


Environment: Internal  and  External
See Also:

History:
********************************************************************/
extern UFUNEXPORT int UF_MODL_create_rect_groove(
double  location[3] ,/* <I>
                     Rectangular groove location.
                     */
double  direction[3] ,/* <I>
                      Rectangular groove direction.
                      */
char * diame ,/* <I>
              Rectangular groove diameter.
              */
char * width ,/* <I>
              Rectangular groove width.
              */
tag_t  face ,/* <I>
             Face for the RPO constraint. The face should be of
             type UF_cylinder_type or UF_cone_type.
             */
tag_t * feature_obj_id  /* <O>
                        Feature object identifier of created rectangular
                        groove
                        */
);

/****************************************************************************
Creates a U-groove feature by inputting its location, direction,
diameter, width, and corner radius. Along with these items a
placement face is needed to determine which face the groove is
associated to. The output of this function is the object identifier
associated to the U-groove.

Environment: Internal  and  External
See Also:
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_create_u_groove(
double  location[3] ,/* <I>
                     U groove location.
                     */
double  direction[3] ,/* <I>
                      U groove direction.
                      */
char * diame ,/* <I>
              U groove diameter
              */
char * width ,/* <I>
              U groove width.
              */
char * corner ,/* <I>
               U groove corner radius
               */
tag_t  face ,/* <I>
             Face for the RPO constraint.
             */
tag_t * feature_obj_id  /* <O>
                        Feature object identifier of created u-groove
                        */
);

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif     /* UF_MODL_GROOVES_H_INCLUDED */
