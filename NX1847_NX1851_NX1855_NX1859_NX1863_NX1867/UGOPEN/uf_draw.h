/****************************************************************************

                       Copyright 1993-2004,2005 UGS Corp.
                            All rights reserved

******************************************************************************


File Description:

This is the Open C API interface to drawing control.  This allows the
programmer access to:

.  create/query section lines, section views, and get current drawing
.  edit section lines
.  edit section line preferences

Drawing view routines return data for the display part.  This is particularly
important when doing design-in-context where the work part is different from
the display part.

Many of the ucnnnn routines identify views using the view name.  For these
routines the following conventions are used.

In V10, when a drawing member view name is specified, it needs to be appended
with an "@" character to denote it as a drawing member view. Specifying the view
name this way is actually a short cut since the actual view name contains an
integer following the "@" character.  Optionally, you may enter the full name in
order to assure uniqueness of member view names (drawings can have more than one
instance of a given view on a single drawing in V10).

An example of a drawing member view name in V10 that is in some way derived
from the model view, TOP, is "TOP@3".  To specify the name of the model view,
"TOP" should be given.  To specify the name of the drawing member view, either
"TOP@" or "TOP@3" can be given.  The full names of all the member views for a
given drawing can be retrieved using uc6499.

Additionally, drawings have an associated drawing work view whose name is the
drawing name with "@0" appended to it.  Functions that create, retrieve, or
require the presence of a drawing will only be allowed in the drafting module
when running interactive NX Open API.

When drafting objects are created on a drawing in V10 Open C API, the objects
associated to the drafting object (the dimensioned objects) must be objects that
are on the drawing.

In routines that specify open and closed quotes = current drawing, view name,
etc., there are no spaces between the quotes ("").

In NX, when the drawing view is the work view, the layout which
contains the drawing is called !DRAWING. This layout name is read only and
cannot be used to set the current layout.

Drawing view routines return data for the display part.  This is particularly
important when doing design-in-context where the work part is different from
the display part.
 ****************************************************************************/

#ifndef UF_DRAW_H_INCLUDED
#define UF_DRAW_H_INCLUDED


/***************************************************************************

  ***************************************************************************/

#include <uf_defs.h>
#include <uf_draw_types.h>
#include <uf_drf_types.h>
#include <uf_retiring.h>
#include <uf_obj_types.h>
#include <libufun_exports.h>


#ifdef __cplusplus
extern "C" {
#endif

#define UF_DRAW_MODELING_VIEW 1
#define UF_DRAW_DRAWING_VIEW  2

/****************************************************************************
 * Adds a segment to a section line, then updates all of its associated
 * section views located on the current drawing. Associated section views
 * not on the current drawing are marked out of date. To perform this
 * edit on the section line without an update, use the suppress view
 * update feature provided in UF_DRF_set_suppress_view_update.
 * 
 *
 * Environment: Internal  and  External
 * See Also:  UF_DRF_set_suppress_view_update
 * History:
****************************************************************************/
extern UFUNEXPORT int UF_DRAW_add_sxline_sxseg(
  tag_t sxline_tag ,                /* <I>
                                    Tag of section line
                                    */
  UF_DRAW_sxseg_type_t sxseg_type , /* <I>
                                    Segment_type:
                                    UF_DRAW_sxseg_cut = cut segment
                                    (only type currently supported for add)
                                    */
  UF_DRAW_sxline_leg_t sxline_leg , /* <I>
                                    If a section line is a two-legged revolved
                                    type ,
                                    UF_DRAW_sxline_leg1= add segment to leg 1
                                    UF_DRAW_sxline_leg2= add segment to leg 2
                                    */
  UF_DRF_object_p_t object ,        /* <I>
                                    Object to associate new segment to
                                    */
  tag_t * sxseg_tag                 /* <O>
                                    Tag of added section segment
                                    */
);

/****************************************************************************
 * Adds a segment to a section line, then updates all of its associated
 * section views located on the current drawing. Associated section views
 * not on the current drawing are marked out of date. To perform this
 * edit on the section line without an update, use the suppress view
 * update feature provided in UF_DRF_set_suppress_view_update.
 *
 * Environment: Internal  and  External
 * See Also:  UF_DRAW_sxline_sxsegs_t
 *            UF_DRF_set_suppress_view_update
 *           
 *
 * History: Original release was in V14.0.
 ****************************************************************************/
extern UFUNEXPORT int UF_DRAW_add_sxseg(
 tag_t sxline_tag ,                    /* <I>
                                       Tag of section line
                                       */
 UF_DRAW_sxline_sxsegs_p_t sxseg_data ,/* <I>
                                       Segment data contains:
                                       segment type: UF_DRAW_sxseg_cut,
                                       linear segment angle, and object to
                                       associate to
                                       */
 tag_t * sxseg_tag                     /* <O>
                                       Tag of newly created section line
                                       segment.
                                       */
);

/****************************************************************************
 * Given the tag of a section edge, outputs the tag of its curve.  Note that
 * section edges that result from a section line's bend segment do not
 * have an associated curve tag. If a section edge from a bend segment is
 * input to this function, curve_tag is returned as a pointer to a null tag.
 * Return:
 *       Return code:
 *       0 = No error
 *       UF_DRAW_no_sxedge_curve = warning
 *       not 0 = Error code
 * Environment: Internal  and  External
 * See Also:
 * History:
 ****************************************************************************/
extern UFUNEXPORT int UF_DRAW_ask_curve_of_sxedge(
               tag_t sxseg_tag ,       /* <I>
                                       section edge tag
                                       */
               tag_t* curve_tag        /* <O>
                                       section edge curve tag
                                       */
);

/****************************************************************************
 * Outputs the associated face of a given silhouette that resides in a
 * drawing member view.  The silhouette must be a line, circle, conic or
 * spline type object.
 *
 * Environment: Internal  and  External
 * See Also: 
 *
 * History: Original Release was in V14.0.
 ****************************************************************************/
extern UFUNEXPORT int UF_DRAW_ask_face_of_sil(
         tag_t silhouette_tag ,    /* <I>
                                   Tag of silhouette in a drawing member view
                                   Must be a line, circle, conic, or spline type.
                                   */
         tag_t * face_tag          /* <O>
                                   Tag of face that the silhouette is
                                   associated to
                                   */
);

/****************************************************************************
 * Retrieves half section line information, given the tag of the section
 * line.   If a section line has an invalid section line status it
 * does not independently cause the return code to be set to a non-zero
 * value.
 *
 * Environment: Internal  and  External
 * See Also:  UF_DRAW_sxline_status_t
 *           See  UF_DRAW_create_half_sxview
 *              for more information about half section lines and views.
 *              
 * History:
 ****************************************************************************/
extern UFUNEXPORT int UF_DRAW_ask_half_sxline(
             tag_t sxline_tag    , /* <I>
                                   Tag of half section line to query
                                   */
             double step_dir[3] ,  /* <O>
                                   Step direction vector (unitized) relative
                                   to the drawing:
                                   step_dir[0] = x value
                                   step_dir[1] = y value
                                   step_dir[2] = z value
                                   */
             double arrow_dir[3] , /* <O>
                                   Arrow direction vector (unitized) relative
                                   to the drawing:
                                   arrow_dir[0] = x value
                                   arrow_dir[1] = y value
                                   arrow_dir[2] = z value
                                   */
             tag_t * pview_tag ,   /* <O>
                                   Parent view tag
                                   */
             int * num_sxviews ,   /* <O>
                                   Number of section views associated to the
                                   input section line
                                   */
            tag_p_t * sxview_tags ,/* <OF,len:num_sxviews>
                                   Array of Section line's section views
                                   Use UF_free to free memory
                                   */
            int * num_sxsegs ,     /* <O>
                                   Number of section line segments
                                   */
            tag_p_t * sxseg_tags , /* <OF,len:num_sxsegs>
                                   Array of section line segment tags
                                   Use UF_free to free memory
                                   */
 UF_DRAW_sxline_status_t * sxline_status  /* <O> Section line status
                                         */
);

/***************************************************************************
 * Retrieves revolved section line information, given the tag of the
 * section line. Note that if a section line has a invalid section line status
 * it does not independently cause the return code to be set to a
 * non-zero value.
 *
 * Environment: Internal  and  External
 * See Also:  UF_DRAW_sxline_status_t
 *          See  UF_DRAW_create_revolved_sxview
 *          for more information about revolved section lines and views.
 *          
 * History:
 ***************************************************************************/
extern UFUNEXPORT int UF_DRAW_ask_revolved_sxline(
       tag_t sxline_tag ,              /* <I>
                                       Tag of revolved section line to query
                                       */
       double step_dir[3] ,            /* <O>
                                       Step direction vector (unitized)
                                       relative to the drawing:
                                       step_dir[0] = x value
                                       step_dir[1] = y value
                                       step_dir[2] = z value
                                       */
       double arrow_dir[3] ,           /* <O>
                                       Arrow direction vector (unitized)
                                       relative to the drawing:
                                       arrow_dir[0] = x value
                                       arrow_dir[1] = y value
                                       arrow_dir[2] = z value
                                       */
       tag_t * pview_tag ,             /* <O>
                                       Parent view tag
                                       */
  UF_DRF_object_t * rotpt_object ,     /* <O>
                                       Object associated to rotation point
                                       */
       int * num_sxviews ,             /* <O>
                                       Number of section views associated to
                                       section line
                                       */
       tag_p_t * sxview_tags ,         /* <OF,len:num_sxviews>
                                       Array of section line's section view
                                       tags Use UF_free to free memory
                                       */
       int * num_sxsegs ,              /* <O>
                                       Number of section line segments.
                                       */
       int * num_leg1_sxsegs ,         /* <O>
                                       Number of section segments input to
                                       define the first leg. Cannot be greater
                                       than num_sxsegs. Any remaining segments
                                       define leg2.
                                       */
 UF_DRAW_sxline_leg_t * cut_plane_leg ,/* <O>
                                       Leg used to define cut plane
                                        = UF_DRAW_sxline_leg1
                                        = UF_DRAW_sxline_leg2
                                       */
        tag_p_t * sxseg_tags ,         /* <OF,len:num_sxsegs>
                                       Array of section line segment tags Use
                                       UF_free to free memory
                                       */
UF_DRAW_sxline_status_t * sxline_status  /* <O> Section line status */
);
/****************************************************************************
 * Outputs an array of silhouettes of the input body that reside in the
 * input drawing member view.
 *
 * Environment: Internal  and  External
 * See Also: 
 * History: Original Release was in V14.0.
 ***************************************************************************/
extern UFUNEXPORT int UF_DRAW_ask_body_sils_in_view(
            tag_t body_tag ,             /* <I>
                                         Tag of a body
                                         */
            tag_t view_tag ,             /* <I>
                                         Tag of a drawing member view
                                         */
            int * num_silhouettes ,      /* <O>
                                         Number of silhouettes
                                         */
            tag_p_t * silhouette_tags    /* <OF,len:num_silhouettes>
                                         If num_silhouettes > 0, this is an
                                         array of silhouette tags.  Use
                                         UF_free to deallocate this memory.
                                         */
);
/***************************************************************************
 * Outputs an array of silhouettes of the input face that reside in the
 * input drawing member view.
 *
 * Environment: Internal  and  External
 * See Also:
 *
 * History: Original Release was in V14.0.
 ***************************************************************************/
extern UFUNEXPORT int UF_DRAW_ask_face_sils_in_view(
                  tag_t face_tag ,       /* <I>
                                         Tag of a face
                                         */
                  tag_t view_tag ,      /* <I>
                                         Tag of a drawing member view
                                         */
                  int * num_silhouettes ,/* <O>
                                         Number of silhouettes
                                         */
                  tag_p_t * sil_tags     /* <OF,len:num_silhouettes>
                                         If num_silhouettes > 0, this is an
                                         array of silhouette tags. Use UF_free
                                         to deallocate memory when done.
                                         */
);


/***************************************************************************
 * Given the tag of a curve, outputs the tag of the associated drawing
 * member view curve group, the group's type, and subtype.
 *
 * Environment: Internal  and  External
 * See Also: 
 * History:
 ***************************************************************************/
extern UFUNEXPORT int UF_DRAW_ask_group_of_curve(
            tag_t curve_tag ,         /* <I>
                                      Tag of curve
                                      */
            tag_t * group_tag ,       /* <O>
                                      Tag of drawing member view curve group.
                                      The group_tag is a NULL_TAG if curve is
                                      not a drafting edge.
                                      */
            int * group_type ,        /* <O>
                                      Type of drawing member view curve group,
                                      either:
                                      UF_solid_silhouette_type,
                                      UF_solid_section_type or
                                      UF_curve_group_type
                                      */
            int * group_subtype       /* <O>
                                      Subtype of drawing member view curve
                                      group:
                                      If group is UF_solid_silhouette_type,
                                      either UF_solid_silhouette_sl_subtype,
                                      UF_solid_silhouette_uvhatch_subtype, or
                                      UF_vicurve_subtype
                                      Else if group is UF_curve_group_type,
                                      either UF_dropped_edge_group_subtype or
                                      UF_simplified_group_subtype
                                      Else = 0
                                      */
);


/***************************************************************************
 * Determines whether the specified curve is a thread curve.  This can
 * be used in conjunction with UF_DRAW_ask_group_of_curve to determine
 * if a thread curve is a thread silhouette or thread section edge.
 *
 * Environment: Internal  and  External
 * History:
 ***************************************************************************/
extern UFUNEXPORT int UF_DRAW_is_thread_curve(
            tag_t curve_tag,          /* <I>
                                      Tag of curve
                                      */
            logical *is_thread_curve  /* <O>
                                      TRUE = curve is a thread curve
                                             (thread silhouette or section edge)
                                      FALSE = curve is not a thread curve
                                      */
);

/***************************************************************************
 * Retrieves simple section line information, given the tag of the section
 * line.  If a section line has an invalid section line status, this
 * does not independently cause the return code to be set to a non-zero
 * value.
 *
 * Environment: Internal  and  External
 * See Also:  UF_DRAW_sxline_status_t
 *          See  UF_DRAW_create_simple_sxview
 *          for more information about simple section lines and views.
 *          
 * History:
 ***************************************************************************/
extern UFUNEXPORT int UF_DRAW_ask_simple_sxline(
            tag_t sxline_tag ,    /* <I>
                                     Tag of section line to query
                                     */
            double step_dir[3] ,     /* <O>
                                     Step direction vector (unitized) relative
                                     to the drawing:
                                     step_dir[0] = x value
                                     step_dir[1]= y value
                                     step_dir[2] = z value
                                     */
            double arrow_dir[3] ,    /* <O>
                                     Step direction vector (unitized) relative
                                     to the drawing:
                                     arrow_dir[0] = x value
                                     arrow_dir[1]= y value
                                     arrow_dir[2] = z value
                                     */
            tag_t * pview_tag ,      /* <O>
                                     Parent view tag
                                     */
            int * num_sxviews ,      /* <O>
                                     Number of section views associated to
                                     section line
                                     */
            tag_p_t * sxview_tags ,  /* <OF,len:num_sxviews>
                                     Array of section line's section views.
                                     Use UF_free to free memory.
                                     */
            int * num_sxsegs ,       /* <O>
                                     Number of section line segments
                                     */
            tag_p_t * sxseg_tags ,   /* <OF,len:num_sxsegs>
                                     Array of section line segment tags.
                                     Use UF_free to free memory
                                     */
 UF_DRAW_sxline_status_t * sxline_status  /* <O> Section line status
                                         */
);

/***************************************************************************
 * Retrieves stepped section line information, given the tag of the
 * section line. NOTE: If a section line has a invalid section line status it
 * does not independently cause the return code to be set to a non-zero
 * value.
 *
 * Environment: Internal  and  External
 * See Also:  UF_DRAW_sxline_status_t
 *          See  UF_DRAW_create_stepped_sxview
 *          for more information about stepped section lines and views.
 *          
 * History:
 ***************************************************************************/
extern UFUNEXPORT int UF_DRAW_ask_stepped_sxline(
            tag_t sxline_tag ,     /* <I>
                                      Tag of stepped section line to query
                                      */
            double step_dir[3] ,      /* <O>
                                      Step direction vector (unitized) relative
                                       to the drawing:
                                      step_dir[0] = x value
                                      step_dir[1] = y value
                                      step_dir[2] = z value
                                      */
            double arrow_dir[3] ,     /* <O>
                                      Arrow direction vector (unitized)
                                      relative to the drawing:
                                      arrow_dir[0] = x value
                                      arrow_dir[1] = y value
                                      arrow_dir[2] = z value
                                      */
            tag_t * pview_tag ,       /* <O>
                                      Parent view tag
                                      */
            int * num_sxviews ,       /* <O>
                                      Number of section views associated to
                                      section line
                                      */
            tag_p_t * sxview_tags ,   /* <OF,len:num_sxviews>
                                      Array of section line's section views.
                                      Use UF_free to free memory.
                                      */
            int * num_sxsegs ,        /* <O>
                                      Number of section line segments
                                      */
            tag_p_t * sxseg_tags ,    /* <OF,len:num_sxsegs>
                                      Array of section line's segment tags.
                                      Use UF_free to free memory.
                                      */
 UF_DRAW_sxline_status_t * sxline_status  /* <O> Section line status
                                         */
);

/***************************************************************************
 * Retrieves unfolded section line information, given the tag of the
 * section line.
 * NOTE: If a section line has an invalid section line status it does not
 * independently cause the return code to be set to a non-zero value.
 *
 * Environment: Internal  and  External
 * See Also:  UF_DRAW_sxline_status_t
 *           See  UF_DRAW_create_unfolded_sxview
 *           for more information about unfolded section lines and views.
 *           
 * History: Original release was in V14.0.
 ***************************************************************************/
extern UFUNEXPORT int UF_DRAW_ask_unfolded_sxline(
              tag_t sxline_tag ,       /* <I>
                                       Tag of unfolded section line to query
                                       */
              double step_dir[3] ,     /* <O>
                                       Step direction vector (unitized)
                                       relative to the drawing:
                                       step_dir[0] = x value
                                       step_dir[1] = y value
                                       step_dir[2] = z value
                                       */
              double arrow_dir[3] ,    /* <O>
                                       Arrow direction vector (unitized)
                                       relative to the drawing:
                                       arrow_dir[0] = x value
                                       arrow_dir[1] = y value
                                       arrow_dir[2] = z value
                                       */
              tag_t * pview_tag ,      /* <O>
                                       Parent view tag
                                       */
              int * num_sxviews ,      /* <O>
                                       Number of section views associated to
                                       section line
                                       */
              tag_p_t * sxview_tags ,  /* <OF,len:num_sxviews>
                                       Array of section line's section views.
                                       Use UF_free to free memory.
                                       */
              int * num_sxsegs ,       /* <O>
                                       Number of section line segments
                                       */
              tag_p_t * sxseg_tags ,   /* <OF,len:num_sxsegs>
                                       Array of section line's segment tags.
                                       Use UF_free to free memory.
                                       */
 UF_DRAW_sxline_status_t * sxline_status  /* <O> Section line status
                                         */
);

/***************************************************************************
 * Retrieves folded section line information, given the tag of the
 * section line.
 * NOTE: If a section line has an invalid section line status it does not
 * independently cause the return code to be set to a non-zero value.
 *
 * Environment: Internal  and  External
 * See Also:  UF_DRAW_sxline_status_t
 * History: Original release was in NX903.
 ***************************************************************************/
extern UFUNEXPORT int UF_DRAW_ask_folded_sxline(
              tag_t sxline_tag ,       /* <I>
                                       Tag of unfolded section line to query
                                       */
              double step_dir[3] ,     /* <O>
                                       Step direction vector (unitized)
                                       relative to the drawing:
                                       step_dir[0] = x value
                                       step_dir[1] = y value
                                       step_dir[2] = z value
                                       */
              double arrow_dir[3] ,    /* <O>
                                       Arrow direction vector (unitized)
                                       relative to the drawing:
                                       arrow_dir[0] = x value
                                       arrow_dir[1] = y value
                                       arrow_dir[2] = z value
                                       */
              tag_t * pview_tag ,      /* <O>
                                       Parent view tag
                                       */
              int * num_sxviews ,      /* <O>
                                       Number of section views associated to
                                       section line
                                       */
              tag_p_t * sxview_tags ,  /* <OF,len:num_sxviews>
                                       Array of section line's section views.
                                       Use UF_free to free memory.
                                       */
              int * num_sxsegs ,       /* <O>
                                       Number of section line segments
                                       */
              tag_p_t * sxseg_tags ,   /* <OF,len:num_sxsegs>
                                       Array of section line's segment tags.
                                       Use UF_free to free memory.
                                       */
 UF_DRAW_sxline_status_t * sxline_status  /* <O> Section line status
                                         */
);

/***************************************************************************
 * This routine retrieves the default section line display preferences,
 * including section line visibility and arrow parameters.
 *
 * Environment: Internal  and  External
 * See Also: 
 * History:
 ***************************************************************************/
extern UFUNEXPORT int UF_DRAW_ask_sxline_default_prfs(
   UF_DRAW_arrow_parms_t * arrow_parms ,   /* <O>
                                           Section line arrow parameters
                                           */
 UF_DRAW_sxline_display_t * sxline_display /* <O>
                                           Section line display:
                                           UF_DRAW_display_sxline = display
                                           section line.
                                           UF_DRAW_no_display_sxline =  do not
                                            display section line.
                                           */
);

/***************************************************************************
 * Given the tag of a solid section, outputs the number of associated
 * section edges and an array of tags of these section edges.
 *
 * Environment: Internal  and  External
 * See Also:
 *
 * History:
 ***************************************************************************/
extern UFUNEXPORT int UF_DRAW_ask_sxedges_of_sxsolid(
                 tag_t sxsolid_tag ,      /* <I>
                                          solid section tag
                                          */
                 int* num_sxedges ,       /* <O>
                                          number of section edges of solid
                                          section
                                          */
                 tag_t** sxedge_tags      /* <OF,len:num_sxedges>
                                          Array of section edge tags.  Use
                                          UF_free to free memory.
                                          */
);


/***************************************************************************
 * Retrieves the input section line's display preferences, including the
 * the section line's visibility and its arrow parameters.
 *
 * NOTE: Do not invoke this routine for section lines of type UF_DRAW_breakline.
 *
 * Environment: Internal  and  External
 * See Also: 
 * History:
 ***************************************************************************/
extern UFUNEXPORT int UF_DRAW_ask_sxline_display(
         tag_t sxline_tag ,           /* <I>
                                      Tag of section line
                                      */
UF_DRAW_arrow_parms_t * arrow_parms , /* <O>
                                      Section line arrow parameters
                                      */
UF_DRAW_sxline_display_t * sxline_display  /* <O>
                                           Section line display:
                                           UF_DRAW_display_sxline = display
                                           section line.
                                           UF_DRAW_no_display_sxline = do not
                                           display section line.
                                           */
);


/***************************************************************************
 * Retrieves the section line tag that is associated to the given section
 * view.
 *
 * Environment: Internal  and  External
 * See Also: 
 * History:
***************************************************************************/
extern UFUNEXPORT int UF_DRAW_ask_sxline_of_sxview(
                 tag_t sxview_tag ,     /* <I>
                                        Tag of section view
                                        */
                 tag_t * sxline_tag     /* <O>
                                        Tag of associated section line
                                        */
);


/***************************************************************************
 * Retrieves section line segment information, given the tag of the
 * section line segment.
 *
 * Environment: Internal  and  External
 * See Also:  UF_DRAW_sxline_sxsegs_t
 *           
 * History:
 ***************************************************************************/
extern UFUNEXPORT int UF_DRAW_ask_sxline_sxseg(
           tag_t sxseg_tag ,        /* <I>
                                    Tag of section line segment to query
                                    */
 UF_DRAW_sxseg_info_t * sxseg_info ,/* <O>
                                    Segment information
                                    */
           tag_t * curve_tag ,      /* <O>
                                    Tag of segment curve
                                    */
        UF_DRF_object_p_t * object  /* <OF>
                                    Object associated to segment.
                                    Use UF_free to free the memory.
                                    */
);

/***************************************************************************
 * Retrieves the section line type, given the tag of the section line.
 *
 * Environment: Internal  and  External
 * See Also: 
 * History:
***************************************************************************/
extern UFUNEXPORT int UF_DRAW_ask_sxline_type(
             tag_t sxline_tag ,      /* <I>
                                     Tag of section line to query its type
                                     */
UF_DRAW_sxline_type_t * sxline_type  /* <O>
                                     UF_DRAW_simple_sxline= simple section line
                                     UF_DRAW_stepped_sxline= stepped section
                                     line
                                     UF_DRAW_half_sxline = half section line
                                     UF_DRAW_revolved_sxline = revolved section
                                     line
                                     UF_DRAW_unfolded_sxline = unfolded section
                                      line
                                     */
);
/***************************************************************************
 * Given the tag of a solid section, output the tag of its associated
 * crosshatch entity. Note that if a section view has its crosshatch
 * preference turned off, a tag to a crosshatch entity that has no line
 * information will be output.
 *
 * Environment: Internal  and  External
 * See Also:
 * History:
***************************************************************************/
extern UFUNEXPORT int UF_DRAW_ask_xhatch_of_sxsolid(
                 tag_t sxsolid_tag ,     /* <I>
                                         section solid tag
                                         */
                 tag_t* xhatch_tag       /* <O>
                                         crosshatch tag
                                         */
);

/***************************************************************************
 * Creates a half section line and view.
 * 
 *
 * Environment: Internal  and  External
 * See Also:See the discussion on the half_sxsegs structure in the Types and
 * See Also:  UF_DRAW_half_sxsegs_t
 *          
 * History:
***************************************************************************/
extern UFUNEXPORT int UF_DRAW_create_half_sxview(
       tag_t dwg_tag ,                /* <I>
                                      Drawing tag
                                      */
       double sxview_scale ,          /* <I>
                                      Section view scale
                                      */
       double  step_dir[3] ,          /* <I>
                                      Step direction vector (unitized) relative
                                      to the drawing:
                                      step_dir[0] = x value
                                      step_dir[1] = y value
                                      step_dir[2] = z value
                                      */
       double  arrow_dir[3] ,         /* <I>
                                      Arrow direction vector (unitized)
                                      relative to the drawing.
                                       arrow_dir[0] = x value
                                       arrow_dir[1] = y value
                                       arrow_dir[2] = z value
                                      */
       tag_t pview_tag ,              /* <I>
                                      Parent view tag
                                      */
       int num_sxsegs ,               /* <I>
                                      Number of section segments.  A cut
                                      segment and bend segment must be provided
                                      (num_segs=2).  If the arrow segment
                                      location is optionally provided,
                                      num_segs=3.
                                      */
 UF_DRAW_half_sxsegs_p_t half_sxseg_objects ,/* <I,len:num_sxsegs>
                                             Section line segment object
                                             structure
                                             */
       double  view_placement_pt[2] , /* <I>
                                      View placement point on drawing in
                                      absolute drawing coordinates (x,y))
                                      */
       tag_t* sxview_tag              /* <O>
                                      Tag of newly created section view
                                      */
);


/***************************************************************************
 * Creates a revolved section view.  The system generates a
 * bend when two cut segments are input with no intervening bend
 * definition. The system also ignores the second of two consecutive
 * input bend segments. The system generates arrow segments if they are
 * not input.
 * 
 *
 * Environment: Internal  and  External
 * See Also:  UF_DRAW_sxline_sxsegs_t
 *           
 * History:
***************************************************************************/
extern UFUNEXPORT int UF_DRAW_create_revolved_sxview(
      tag_t dwg_tag ,                     /* <I>
                                          Drawing tag
                                          */
      double sxview_scale ,               /* <I>
                                          Section view scale
                                          */
      double  step_dir[3] ,               /* <I>
                                          Step direction vector (unitized)
                                          relative to the drawing:
                                          step_dir[0] = x value
                                          step_dir[1]= y value
                                          step_dir[2] = z value
                                          */
      double  arrow_dir[3] ,              /* <I>
                                          Arrow direction vector (unitized)
                                          relative to the drawing.
                                          arrow_dir[0] = x value
                                          arrow_dir[1] = y value
                                          arrow_dir[2] = z value
                                          */
      tag_t pview_tag ,                   /* <I>
                                          Parent view tag
                                          */
 UF_DRF_object_p_t rotpt_object ,         /* <I>
                                          Object defining rotation point
                                          associativity.
                                          */
      int num_sxsegs ,                    /* <I>
                                          Number of section segments used to
                                          initially define the section line.
                                          A cut segment must be defined
                                          (num_segs must be > 0). This
                                          number defines the size of the
                                          rev_sxseg_objects array.  A section
                                          line cannot have more than 99
                                          segments and cannot have more than
                                          49 cut segments.  */
      int num_leg1_sxsegs ,               /* <I>
                                          Number of section segments input to
                                          define the first leg. Cannot be
                                          greater than num_segs. Any remaining
                                          segments define leg2.
                                          */
UF_DRAW_sxline_sxsegs_p_t rev_sxsegs ,     /* <I,len:num_sxsegs>
                                           For each section segment defined, a
                                           segment type is given that determines
                                           whether the segment is a cut, bend,
                                           or arrow.  Bend and arrow segments
                                           are optional.  Also, for each
                                           section segment defined, an object
                                           is given to define the section
                                           segment associativity.
                                           */
      double  view_placement_pt[2] ,       /* <I>
                                           View placement point on drawing in
                                           absolute drawing coordinates (x,y))
                                           */
      tag_t * sxview_tag                   /* <O>
                                           Tag of newly created section view
                                           */
);

/***************************************************************************
 * Creates a simple section line and view. Only the cut segment of the
 * section line is input.  The arrow segments of the section line are
 * automatically generated.
 * 
 *
 * Environment: Internal  and  External
 * See Also:
 *           
 * History:
***************************************************************************/
extern UFUNEXPORT int UF_DRAW_create_simple_sxview(
     tag_t dwg_tag ,                 /* <I>
                                        Drawing tag
                                        */
     double sxview_scale ,              /* <I>
                                        Section view scale
                                        */
     double  step_dir[3] ,              /* <I>
                                        Step direction vector (unitized)
                                        relative to the drawing:
                                        step_dir[0] = x value
                                        step_dir[1] = y value
                                        step_dir[2] = z value
                                        */
     double  arrow_dir[3] ,             /* <I>
                                        Arrow direction vector (unitized)
                                        relative to the drawing.
                                        arrow_dir[0] = x value
                                        arrow_dir[1] = y value
                                        arrow_dir[2] = z value
                                        */
     tag_t pview_tag ,                  /* <I>
                                        Parent view tag
                                        */
     UF_DRF_object_p_t cut_object ,     /* <I>
                                        Object associated to cut segment
                                        */
     double  view_placement_pt[2] ,     /* <I>
                                        View placement point on drawing in
                                        absolute drawing coordinates (x,y)
                                        */
     tag_t * sxview_tag                 /* <O>
                                        Tag of newly created section view
                                        */
);


/***************************************************************************
 * Creates a stepped section view.  The system generates a
 * bend when two cut segments are input with no intervening bend
 * definition.  The system also ignores the second of two consecutive
 * input bend segments. The system generates arrow segments if they are
 * not input.
 * 
 *
 * Environment: Internal  and  External
 * See Also:  UF_DRAW_sxline_sxsegs_t
 *
 * History:
 ***************************************************************************/
extern UFUNEXPORT int UF_DRAW_create_stepped_sxview(
tag_t dwg_tag ,   /* <I>
                  Drawing tag
                  */
double sxview_scale ,/* <I>
                     Section view scale
                     */
double  step_dir[3] ,/* <I>
                     Step direction vector (unitized) relative
                     to the drawing:
                       step_dir[0] = x value
                       step_dir[1] = y value
                       step_dir[2] = z value
                     */
double  arrow_dir[3] ,/* <I>
                      Arrow direction vector (unitized) relative
                      to the drawing.
                        arrow_dir[0] = x value
                        arrow_dir[1] = y value
                        arrow_dir[2] = z value
                      */
tag_t pview_tag ,/* <I>
                 Parent view tag
                 */
int num_sxsegs ,/* <I>
                Number of section segments used to initially define the section
                line.  A cut segment must be provided (num_sxsegs>0).  This
                number determines the length of the stepped_sxsegs array.
                */
UF_DRAW_sxline_sxsegs_p_t stepped_sxsegs ,/* <I,len:num_sxsegs>
                                          For each section segment defined, a
                                          segment type is given that determines
                                          whether the segment is a cut, bend
                                          or arrow. Bend and arrow segments
                                          are optional.  Also, for each section
                                          seg ment defined, an object is given
                                          to de fine the section segment
                                          associativity.  A section line cannot
                                          have more than 99 segments and cannot
                                          have more than 49 cut segments.
                                          */
double  view_placement_pt[2] ,/* <I>
                              View placement point on drawing in
                              absolute drawing  coordinates (x,y))
                              */
tag_t * sxview_tag  /* <O>
                    Tag of newly created section view
                    */
);


/***************************************************************************
Creates an unfolded section view.
NOTE: The system generates arrow segments if they are not input.

Environment: Internal  and  External
See Also:  UF_DRAW_sxline_sxsegs_t
          
History: Original release was in V14.0.

***************************************************************************/
extern UFUNEXPORT int UF_DRAW_create_unfolded_sxview(
tag_t dwg_tag ,/* <I>
               Tag of drawing
               */
double sxview_scale ,/* <I>
                     Scale of section view
                     */
double step_dir[3] ,/* <I>
                    Step direction vector (unitized) relative to the drawing:
                      step_dir[0] = x value
                      step_dir[1] = y value
                      step_dir[2] = z value
                    */
double arrow_dir[3] ,/* <I>
                     Arrow direction vector (unitized) relative to the drawing.
                     arrow_dir[0] = x value
                     arrow_dir[1] = y value
                     arrow_dir[2] = z value
                     */
tag_t pview_tag ,/* <I>
                 Parent view tag
                 */
int num_sxsegs ,/* <I>
                Number of section segments used to initially define the section
                line. A cut segment must be provided (num_sxsegs>0). This number
                determines the length of the stepped_sxsegs array.
                */
UF_DRAW_sxline_sxsegs_p_t unfolded_sxsegs ,/* <I,len:num_sxsegs>
                                           For each section segment defined, a
                                           segment type is given that
                                           determines whether the segment is a
                                           cut, bend or arrow. Bend and arrow
                                           segments are op- tional. Also, for
                                           each section segment defined, an
                                           object is given to define the
                                           section segment associativity. A
                                           section line cannot have more than
                                           99 segments and cannot have more
                                           than 49 cut segments.
                                           */
double view_placement_pt[2] ,/* <I>
                             View placement point on drawing in
                             absolute drawing  coordinates (x,y))
                             */
tag_t * sxview_tag  /* <O>
                    Tag of newly created section view
                    */
);

/***************************************************************************
 * Deletes a segment of a section line, then updates all of the section
 * line's associated section views located on the current drawing.
 * Associated section views not on the current drawing are marked out
 * of date. To perform this edit on the section line without an update, use
 * the suppress view update feature provided in UF_DRF_set_suppress_view_update.
 * 
 *
 * Environment: Internal  and  External
 * See Also:  UF_DRF_set_suppress_view_update
 *
 * History:
 ***************************************************************************/
extern UFUNEXPORT int UF_DRAW_delete_sxline_sxseg(
tag_t sxseg_tag  /* <I>
                 Tag of section line segment to delete
                 */
);


/***************************************************************************
 * Edits the input section line's display preferences, including the the
 * section line's visibility and its arrow parameters, and updates the
 * display of the section line. The input preferences are also saved as the
 * new global section line display preferences.
 *
 * Environment: Internal  and  External
 * See Also:  UF_DRAW_arror_parms_t
 *
 * History:
 ***************************************************************************/
extern UFUNEXPORT int UF_DRAW_edit_sxline_display(
tag_t sxline_tag ,/* <I>
                     Tag of section line to edit
                     */
UF_DRAW_arrow_parms_p_t arrow_parms ,/* <I>
                                     Section line arrow parameters
                                     */
UF_DRAW_sxline_display_t sxline_display  /* <I>
                                         Section line display:
                                         UF_DRAW_display_sxline=display section
                                                                line
                                         UF_DRAW_no_display_sxline=do not
                                                           display section line
                                         */
);


/***************************************************************************
* Given the tag of a view, outputs whether the view is a section view.
*
* Environment: Internal  and  External
* See Also: 
* History: Original release was in V14.0.
***************************************************************************/
extern UFUNEXPORT int UF_DRAW_is_sxview(
tag_t view_tag ,/* <I>
                Tag of view
                */
logical * is_a_sxview  /* <O>
                       If TRUE, the view is a section view, else it is not.
                       */
);
/***************************************************************************
 * Moves a section line rotation point to a location defined by the input
 * new object, then updates all of the section line's associated section
 * views located on the current drawing. Associated section views not on
 * the current drawing are marked out of date. To perform edits on the
 * section line without an update, use the suppress view update feature
 * provided in UF_DRF_set_suppress_view_update.
 *
 * Environment: Internal  and  External
 * See Also:  UF_DRAW_create_revolved_sxview
 *            UF_DRF_set_suppress_view_update
 *           for more information on revolved section lines and section views.
 *           
 * History:
***************************************************************************/
extern UFUNEXPORT int UF_DRAW_move_sxline_rotpt(
tag_t sxline_tag ,/* <I>
                  Tag of revolved section line
                  */
UF_DRF_object_p_t new_object  /* <I>
                              New object to associate rotation point
                              */
);


/***************************************************************************
 * Moves a section line segment to a location defined by the input
 * new_object, then updates all of the section line's associated section
 * views located on the current drawing. Associated section views not on
 * the current drawing are marked out of date. To perform edits on the
 * section line without an update, use the suppress view update feature
 * provided in UF_DRF_set_suppress_view_update.
 * 
 *
 * Environment: Internal  and  External
 * See Also:  UF_DRF_set_suppress_view_update
 *          
 * History:
***************************************************************************/
extern UFUNEXPORT int UF_DRAW_move_sxline_sxseg(
tag_t sxseg_tag ,/* <I>
                 Tag of section line segment to move.
                 */
UF_DRF_object_p_t new_object  /* <I>
                              New object to associate segment.
                              */
);

/***************************************************************************
 * Moves a section line segment to a location defined by the input new
 * object of sxseg_data, then updates all of the section line's associated
 * section views located on the current drawing. Associated section views
 * not on the current drawing are marked out of date. To perform this
 * edit on the section line without an update, use the suppress view
 * update feature provided in UF_DRF_set_suppress_view_update.
 *
 * Environment: Internal  and  External
 * See Also:  UF_DRF_set_suppress_view_update
 *            UF_DRAW_sxline_sxsegs_t
 *           
 * History:Original release was in V14.0.
***************************************************************************/
extern UFUNEXPORT int UF_DRAW_move_sxseg(
tag_t sxseg_tag ,/* <I>
                 Tag of section line segment to move.
                 */
UF_DRAW_sxline_sxsegs_p_t sxseg_data  /* <I>
                                      Segment data contains:
                                      segment type: UF_DRAW_sxseg_cut,
                                      linear segment angle, and object to
                                      associate to. The sxseg_object is used
                                      to move all segments.  The sxseg_angle
                                      is used to move an unfolded sxseg.
                                      */
);

/***************************************************************************
 * Sets the section line default display preferences, including visibility
 * and arrow parameters.
 *
 * Environment: Internal  and  External
 * See Also:  UF_DRAW_arror_parms_t
 *           
 * History:
***************************************************************************/
extern UFUNEXPORT int UF_DRAW_set_sxline_default_prfs(
UF_DRAW_arrow_parms_p_t arrow_parms ,/* <I>
                                     Section line arrow parameters
                                     */
UF_DRAW_sxline_display_t sxline_display  /* <I>
                                         Section line display:
                                         UF_DRAW_display_sxline = display
                                                            section line.
                                         UF_DRAW_no_display_sxline = do not
                                                      display section line.
                                         */
);

/****************************************************************************
 * Updates one drawing member view on a drawing. The view update
 * process includes updating the view bounds, resectioning section views,
 * updating silhouettes, and updating hidden line display when
 * applicable.
 * NOTE: When running this function interactively you must be
 * operating in an application that creates, retrieves, or requires the
 * presence of a drawing (Gateway, Drafting, Valisys, and Genconnect).
 *
 * Environment: Internal  and  External
 * See Also:  UF_DRAW_ask_suppress_view_updat
 *            UF_DRAW_set_suppress_view_updat
 *            UF_DRAW_is_object_out_of_date
 *           
 * History:
 ****************************************************************************/
extern UFUNEXPORT int UF_DRAW_update_one_view(
tag_t drawing_tag ,/* <I>
                   Tag of drawing
                   */
tag_t view_tag  /* <I>
                Tag of view to update
                */
);

/****************************************************************************
 * Queries the up-to-date status of an object. Currently, only two types
 * of objects are valid: views and drawings.
 *
 * Environment: Internal  and  External
 * See Also:  UF_DRAW_ask_suppress_view_updat
 *            UF_DRAW_set_suppress_view_updat
 *            UF_DRAW_update_one_view
 *           
 * History:
 ****************************************************************************/
extern UFUNEXPORT int UF_DRAW_is_object_out_of_date(
tag_t object ,/* <I>
              tag of view or drawing
              */
logical * out_of_date  /* <O>
                       object out-of-date status
                       */
);

/****************************************************************************
 * Queries the current value of the Suppress View Update preference.
 * This preference is saved with a part.  Retrieves value from the root part.
 * If no parts are loaded, an error will occur.
 * If the preference is TRUE, then functions which perform implicit
 * drawing update, will not update the drawing member views.
 *
 * Note: Starting in nx2, this preference was saved with the part.
 *       Some parts may have been inadvertently saved in nx2 with suppress
 *       view updated turned off.
 *       To allow users to override the suppress view update setting, an
 *       environment variable "UGII_SUPPRESS_VIEW_UPDATE" can be set with
 *       values "0" or "1".  If set to 1, this will prevent an automatic
 *       update of the out-of-date views.
 *
 * Environment: Internal  and  External
 * See Also:  UF_DRAW_set_suppress_view_updat
 *            UF_DRAW_update_one_view
 *            UF_DRAW_is_object_out_of_date
 *           
 * History:
 ****************************************************************************/
extern UFUNEXPORT int UF_DRAW_ask_suppress_view_updat(
logical * suppress_view_update  /* <O>
                                Suppress View Update preference setting:
                                 TRUE = suppress all system initiated view
                                        updates
                                 FALSE = allow  all system initiated view
                                         updates
                                */
);

/***************************************************************************
 * Changes the value of the Suppress View Update preference. This
 * preference is saved to the root part.
 * If no parts are loaded, an error will occur.
 * If the preference is TRUE, then functions which perform implicit
 * drawing update, will not update the drawing member views.
 * Please note that manual views do not update automatically.
 * For a view to automatically update, set UF_DRAW_set_auto_update to TRUE,
 * and set suppress_view_update to FALSE.
 *
 * Note: Starting in nx2, this preference was saved with the part.
 *       Some parts may have been inadvertently saved with suppress view updated
 *       turned off.  To allow users to override the suppress view update setting,
 *       an environment variable "UGII_SUPPRESS_VIEW_UPDATE" can be set with
 *       values "0" or "1".  If set to 1, this will prevent an automatic
 *       update of the out-of-date views.
 *
 * Environment: Internal  and  External
 * See Also:  UF_DRF_ask_suppress_view_update
 *            UF_DRF_update_views
 *            UF_DRF_is_object_out_of_date
 *           
 * History:
 ****************************************************************************/
extern UFUNEXPORT int UF_DRAW_set_suppress_view_updat(
logical suppress_view_update  /* <I>
                              Suppress View Update preference setting:
                              TRUE = suppress all system initiated view updates.
                              FALSE = allow all system initiated view updates.
                              */
);

/****************************************************************************
 * Returns the structure of a single specified section view display setting.
 *
 * Environment: Internal  and  External
 * See Also:  UF_DRAW_set_sxview_display
 *           
 * History:
 ****************************************************************************/
extern UFUNEXPORT int UF_DRAW_ask_sxview_display(
tag_t view_tag ,/* <I>
                Tag of section view
                */
 UF_DRAW_sxview_prfs_t * sxview_parms  /* <O>
                                       Data structure contains the section
                                       view preference parameters.
                                       */
);

/****************************************************************************
 * Returns the count and array of solid sections created by the sectioning
 * of an input leg. Depending on whether the section view is a revolved
 * or non-revolved type the following descriptions will apply:
 * For Non-Revolved Section Views
 * Given the tag of a section view  output an array of solid section tags
 * that are sectioned in the input section view.
 * For Revolved Section Views
 * Given the tag of a section view and the leg number, output an array of
 * solid section tags that are sectioned in the input section view by the
 * leg of the section view's section line.
 *
 * Environment: Internal  and  External
 * See Also: 
 * History:
 ****************************************************************************/
extern UFUNEXPORT int UF_DRAW_ask_sxsolids_of_sxview(
tag_t sxview_tag ,/* <I>
                  Tag of section view
                  */
UF_DRAW_sxline_leg_t leg_num ,/* <I>
                              Leg number of the cut, UF_DRAW_sxline_leg1 or
                              UF_DRAW_sxline_leg2.  Required only if sxview_tag
                              was created from a two legged revolved section
                              line.
                              */
int* num_sxsolids ,/* <O>
                   Number of solid sections created by the sectioning
                   of the input leg.
                   */
tag_t** sxsolid_tags  /* <OF,len:num_sxsolids>
                      Array of solid sections created by the sectioning of
                      the input leg.  Use UF_free to free memory.
                      */
);

/****************************************************************************
 * Returns the structure of a single specified view display setting for a
 * specific drawing member view. The display structures are as follows:
 *
 * Environment: Internal  and  External
 * See Also: 
 *            UF_DRAW_view_prfs_t
 *
 * History:
 ****************************************************************************/
extern UFUNEXPORT int UF_DRAW_ask_view_display(
tag_t view_tag ,/* <I>
                Tag of drawing member view
                */
UF_DRAW_view_prfs_t * view_parms  /* <O>
                                  Data structure contains the hidden line
                                  removal, edge hiding edge, silhouette, uv
                                  hatch, smooth edge display, smooth edge
                                  color, font,, width and gap, virtual
                                  intersection color, font, width, gap, and
                                  status, tolerance, hidden line color, font,
                                  and width parameters, and the extracted edges
                                  setting.
                                  */
);

/****************************************************************************
 * Queries the current value of the Automatic Update preference
 * setting.
 *
 * Environment: Internal  and  External
 * See Also:  UF_DRAW_set_auto_update
 *           
 * History:
 *****************************************************************************/
extern UFUNEXPORT int UF_DRAW_ask_auto_update(
tag_t view_tag ,/* <I>
                Tag of section view
                */
logical * auto_update  /* <O>
                       TRUE =  Automatically update the view
                       FALSE = Do not automatically update the view
                       */
);

/******************************************************************************
 * Sets the value of a specified section view display preference.
 *
 * Environment: Internal  and  External
 * See Also:  UF_DRAW_ask_sxview_display
 *          
 * History:
 ******************************************************************************/
extern UFUNEXPORT int UF_DRAW_set_sxview_display(
tag_t view_tag ,/* <I>
                Tag of section view object
                */
UF_DRAW_sxview_prfs_t * sxview_parms  /* <I>
                                      Data structure contains the section
                                      view preference parameters.
                                      */
);

/****************************************************************************
 * Sets the value of a specified view display preference for a specific
 * drawing member view.

 * Note: Call UF_DRAW_update_one_view() to force this view to
 *       update after calling UF_DRAW_set_view_display()
 *
 * Environment: Internal  and  External
 * See Also:  UF_DRAW_ask_view_display
 *           
 * History:
 ****************************************************************************/
extern UFUNEXPORT int UF_DRAW_set_view_display(
tag_t view_tag ,/* <I>
                Tag of drawing member view
                */
UF_DRAW_view_prfs_t* view_parms  /* <I>
                                 Data structure contains the hidden line
                                 removal, edge hiding edge, silhouette, uv
                                 hatch, smooth edge display, smooth edge color,
                                 font, width and gap, virtual intersection
                                 color, font, width, gap, and status,
                                 tolerance, and hidden line color, font, and
                                 width parameters.
                                 */
);

/******************************************************************************
 * This function sets the current value of the Automatic Update
 * preference.
 *
 * Environment: Internal  and  External
 * See Also:  UF_DRAW_ask_auto_update
 *           
 * History:
 ******************************************************************************/
extern UFUNEXPORT int UF_DRAW_set_auto_update(
tag_t view_tag ,/* <I>
                Tag of view object
                */
logical * auto_update  /* <O>
                       TRUE =  Automatically update the view
                       FALSE = Do not automatically update the view
                       */
);

/****************************************************************************n
 * Returns the tag of the current drawing.
 *
 * Environment: Internal  and  External
 * See Also:
 * History:
 ******************************************************************************/
extern UFUNEXPORT int UF_DRAW_ask_current_drawing(
tag_t * drawing_tag  /* <O>
                            Tag of  current drawing
                            */
);

/******************************************************************************
 * Retrieves the view boundary curves, the smart defining points of those
 * curves, and the tolerance. These items are used to create an arbitrary
 * clipping bound for a view.
 *
 * Environment: Internal  and  External
 * See Also:  UF_DRAW_define_view_boundary
 *           
 * History:
******************************************************************************/
extern UFUNEXPORT int UF_DRAW_ask_boundary_curves(
tag_t view_tag ,/* <I>
                Tag of view whose view boundary curves are to be obtained.
                */
double * tolerance ,/* <O>
                    The chain tolerance used to create the arbitrary clipping
                    bounds for this view.
                    */
int * num_curves ,/* <O>
                  Count of structures.
                  = 0 if view does not have an arbitrary boundary defined.
                  */
UF_DRAW_view_boundary_t ** boundary_curves  /* <OF,len:num_curves,free:UF_DRAW_free_boundary>
                                            Pointer to view boundary structure.
                                            Use UF_DRAW_free_boundary to free
                                            the pointer.  If a boundary curve
                                            has been deleted, its curve_tag will
                                            be NULL.
                                            */
);

/******************************************************************************
 * Creates a view boundary of a closed, connected, non-self-intersecting
 * loop of curves. Valid curve types are UF_line_type, UF_circle_type,
 * and UF_spline_type. All curves must be visible in the view. If the
 * curve type is UF_circle_type, the circle must be in the plane of the
 * view.
 *
 * 
 *
 * Environment: Internal  and  External
 * See Also:  UF_DRAW_ask_boundary_curves
 *           
 * History:
 ******************************************************************************/
extern UFUNEXPORT int UF_DRAW_define_view_boundary(
tag_t view_tag ,/* <I>
                Tag of the view whose boundary is to be defined.
                */
int curve_count ,/* <I>
                 Count of tags of curves in curve_list
                 */
UF_DRAW_define_boundary_p_t* boundary_curves  /* <I,len:curve_count> curve_count
                                              Pointer to array of structures
                                              that are used to define the view
                                              boundary.
                                              */
);
/**************************************************************************
In order to provide appropriate .NET binding for UF_DRAW_define_view_boundary,  
UF_DRAW_define_view_boundary1 is introduced. 

Note: C/C++ users can continue to use UF_DRAW_define_view_boundary. 

For docuementation, refer to documentation of UF_DRAW_define_view_boundary.

History: Originally released in NX8.5.1
****************************************************************************/
extern UFUNEXPORT int UF_DRAW_define_view_boundary1(
tag_t view_tag ,/* <I>
                Tag of the view whose boundary is to be defined.
                */
int curve_count ,/* <I>
                 Count of tags of curves in curve_list
                 */
UF_DRAW_define_boundary_p_t* boundary_curves  /* <I,len:curve_count> curve_count
                                              Pointer to array of structures
                                              that are used to define the view
                                              boundary.
                                              */
);

/******************************************************************************
 * Defines the view boundary for the input view as an automatic view
 * boundary. The view cannot be a detail view. The view must be active
 * and on the current drawing. No view may be expanded prior to calling
 * this function.
 *
 * Environment: Internal  and  External
 * See Also: 
 * History:
 ******************************************************************************/
extern UFUNEXPORT int UF_DRAW_define_view_auto_rect(
tag_t  view_tag  /* <I>
                 Tag of view.
                 */
);

/******************************************************************************
 * Sets view borders for the given view on the current drawing.  The view
 * must be active on the current drawing. No view may be expanded
 * before calling this function.
 *
 * Environment: Internal  and  External
 * See Also: 
 * History:
 ******************************************************************************/
extern UFUNEXPORT int UF_DRAW_define_view_manual_rect(
tag_t  view_tag ,/* <I>
                 Tag of view.
                 */
double view_borders[4]  /* <I>
                       View Borders (Drawing Coordinates), can be any
                       two diagonal corners (X1,Y1,X2,Y2) of the view box.
                       */
);

/******************************************************************************
 * Accepts a view tag as an input parameter and returns the view
 * rendering method. Each rendering method corresponds with an ANSI
 * or ISO thread standard. Valid rendering methods are:
 *     UF_DRAW_THD_METH_NONE
 *     UF_DRAW_THD_METH_ANSI_SIMPLIFIED
 *     UF_DRAW_THD_METH_ANSI_SCHEMATIC
 *     UF_DRAW_THD_METH_ANSI_DETAILED
 *     UF_DRAW_THD_METH_ISO_SIMPLIFIED
 *     UF_DRAW_THD_METH_ISO_DETAILED
 *     UF_DRAW_THD_METH_ESKD_SIMPLIFIED
 *  The default rendering method for pre-V12 member views is
 *  UF_DRAW_THD_METH_NONE.
 *
 * Environment: Internal  and  External
 * See Also:See  UF_DRAW_ask_view_thd_app_pitch
 *               UF_DRAW_set_view_thd_meth
 *               UF_DRAW_set_view_thd_app_pitch
 *
 * History:
 *****************************************************************************/
extern UFUNEXPORT int UF_DRAW_ask_view_thd_meth(
tag_t view ,/* <I>
            tag of the drawing member view
            */
int * method  /* <O>
              the view's current rendering method
              */
);

/***************************************************************************
 * Accepts a view tag as an input parameter and returns the minimum
 * apparent pitch. The minimum apparent pitch is defined as the
 * minimum value used to visually represent the pitch when rendering
 * symbolic thread features on drawing member views. It can be used to
 * preserve the visual clarity of threads whose pitch is small relative to
 * the view scale.
 *
 * For example, if a view with a scale of 2.0 contained threads with an
 * actual pitch of 0.0125 inches, the actual thread pitch would render at
 * 0.0125 * 2 = 0.025 inches which may be unreadable when plotted at
 * full scale. If the view's minimum apparent pitch had been set to
 * 0.0625 inches, then that value (in drawing units) would be used to
 * render the thread pitch.
 *
 * Environment: Internal  and  External
 * See Also:  UF_DRAW_ask_view_thd_meth
 *            UF_DRAW_set_view_thd_meth
 *            UF_DRAW_set_view_thd_app_pitch
 * History:
****************************************************************************/
extern UFUNEXPORT int UF_DRAW_ask_view_thd_app_pitch(
tag_t view ,/* <I>
          Tag of drawing member view
          */
double * app_pitch  /* <O>
                    The minimum pitch for rendered threads in the given view
                    */
);

/*******************************************************************************
 * Accepts a view tag and a thread rendering method as input
 * parameters. Each rendering method corresponds with an ANSI or
 * ISO thread standard. Valid rendering methods are:
 * UF_DRAW_THD_METH_NONE
 * UF_DRAW_THD_METH_ANSI_SIMPLIFIED
 * UF_DRAW_THD_METH_ANSI_SCHEMATIC
 * UF_DRAW_THD_METH_ANSI_DETAILED
 * UF_DRAW_THD_METH_ISO_SIMPLIFIED
 * UF_DRAW_THD_METH_ISO_DETAILED
 * UF_DRAW_THD_METH_ESKD_SIMPLIFIED
 * Changing the method affects the display of all symbolic thread
 * features rendered in the specified view.
 *
 * Environment: Internal  and  External
 * See Also:  UF_DRAW_ask_view_thd_app_pitch
 *            UF_DRAW_ask_view_thd_meth
 *            UF_DRAW_set_view_thd_app_pitch
 *
 * History:
*****************************************************************************/
extern UFUNEXPORT int UF_DRAW_set_view_thd_meth(
tag_t view ,/* <I>
            tag of the drawing member view
            */
int method  /* <I>
            the thread rendering method you wish to use for this view.
            */
);

/******************************************************************************
 * Sets the minimum apparent pitch for all the threads in a drawing
 * member view. When set, any previously existing threads with an actual
 * pitch less than the minimum value are rendered using this value
 * instead.
 *
 * Environment: Internal  and  External
 * See Also:  UF_DRAW_ask_view_thd_app_pitch
 *            UF_DRAW_ask_view_thd_meth
 *            UF_DRAW_set_view_thd_meth
 * History:
 ****************************************************************************/
extern UFUNEXPORT int UF_DRAW_set_view_thd_app_pitch(
tag_t view ,/* <I>
            tag of drawing member view
            */
double app_picth  /* <I>
                  This is a double value representing the new minimum apparent
                  pitch for the view. This means that although a thread may
                  have a smaller pitch, the smallest pitch which will be drawn
                  is specified by app _pitch for visual clarity. For example,
                  if a thread had a pitch of 0.001 inches but the minimum
                  apparent pitch was 0.1, the thread would be drawn showing a
                  pitch of 0.1, although the actual modelling data remains
                  unchanged with a true pitch of 0.001 inches.  the minimum
                  apparent pitch for the view
                  */
);

/***************************************************************************
 * Redefines the section line's hinge line given the tag of a section line
 * and a drafting line object. The section view and any details of the
 * section view are reoriented about their center to reflect the newly
 * defined hinge line.
 *
 * To perform this edit on the section line without an update, use the
 * suppress view updated feature provided in UF_DRF_set_suppress_view_update.
 *
 * NOTE: The hinge_line.line_assoc_type must be either
 * UF_DRF_dwg_line, UF_DRF_existing_line or UF_DRF_two_points.
 * If hinge_line.line_assoc_type is UF_DRF_dwg_line, the hinge line has
 * no associativity and is defined by a direction vector defined from
 * hinge_line.object1.assoc_dwg_pos to hinge_line.point_object2.assoc_dwg_pos.
 *
 * Return:
 *          Return code:
 *         0 = No error
 *         UF_DRAW_hinge_not_linear = warning
 *     not 0 = Error code
 *
 * Environment: Internal  and  External
 * See Also:  UF_DRF_set_suppress_view_update
 *          
 * History:
 ***************************************************************************/
extern UFUNEXPORT int UF_DRAW_redefine_sxline_hinge(
tag_t sxline_tag ,/* <I>
                  section line tag
                  */
UF_DRF_line_object_p_t hinge_line ,/* <I>
                                   object to associate hinge line to
                                   */
logical arrow_same_dir  /* <I>
                        If true, the new arrow direction will point
                        away from the new hinge line in the same
                        relative direction as the old arrow pointed
                        away from the old hinge line.  Else, the
                        direction is flipped.
                        */
);

/******************************************************************************
 * Associates the expression to the view scale of drawing member views
 * or model views. The expression does not have to be in the same part
 * file as the view. An Expression from a different part file can be
 * associated to the view scale as long as the part containing the
 * expression is loaded.
 *
 * Return:
 *          Return code:
 *         0 = No error
 *         UF_DRAW_hinge_not_linear = warning
 *     not 0 = Error code
 *
 * Environment: Internal  and  External
 * See Also: 
 * History:
 ******************************************************************************/
extern UFUNEXPORT int UF_DRAW_set_view_parm_scale(
tag_t  view ,/* <I>
             The scale of this view is made associative to the expression.
             */
tag_t  exp_tag  /* <I>
                The expression which is to be associated to the view scale.
                */
);

/******************************************************************************
 * If the view scale is associative, this function outputs an expression tag
 * and view scale value. If the view scale is not associative, this function
 * still outputs the view scale value, but the expression is equal to a
 * NULL_TAG and returns an error.
 *
 * Return:
 *          Return code:
 *         0 = No error
 *         UF_DRAW_hinge_not_linear = warning
 *     not 0 = Error code
 *
 * Environment: Internal  and  External
 * See Also: 
 * History:
 ******************************************************************************/
extern UFUNEXPORT int UF_DRAW_ask_view_parm_scale(
tag_t view_tag ,/* <I>
                View from which the scale value and associated expression is
                obtained.
                */
tag_t * exp_tag ,/* <O>
                 Expression associated to the view scale, NULL_TAG if the view
                 scale is not associative
                 */
double * scale_value  /* <O>
                      The scale value of the view.
                      */
);

/******************************************************************************
 * Given a drawing curve (a silhouette or a section edge) or an edge that
 * is a conic or a spline, and the tag to a drawing member view where
 * this curve or edge is displayed, this function creates new arcs or lines
 * that approximate that conic or spline curve.
 * The approximation uses the drawing member view's tolerance view
 * display preference in its calculations.
 * Note that the simplification can be deleted by deleting any one of the
 * curves of the simplification.
 *
 * Environment: Internal  and  External
 * See Also: See  UF_DRAW_set_view_display
 *           to change the tolerance value. This tolerance value is defined in
 *            UF_DRAW_view_prfs_t
 *          
 *History: Original release was in V13.0.
 ******************************************************************************/
extern UFUNEXPORT int UF_DRAW_create_simplified_curve(
tag_t master_curve_tag ,/* <I>
                        Tag of the master curve or edge to simplify
                        */
tag_t view_tag ,/* <I>
                Tag of the drawing member view of the master_curve.  If the
                master_curve is a section edge or silhouette, view_tag will be
                ignored as simple curves will be created in the view of the
                master curve.
                */
logical flat_arc_to_line ,/* <I>
                          If TRUE, a post processing of the arc segments
                          output from the simplification will be performed to
                          convert flat arc segments with chordal tolerance less
                          than half the view display tolerance to line
                          segments.  Also, adjacent line segments and arc
                          segments will be joined if the result is within half
                          the view display tolerance.
                          */
int * num_segments ,/* <O>
                    Number of simplified curves
                    */
tag_p_t * segments  /* <OF,len:num_segments>
                    Array of simplified curves.  Use UF_free to free memory.
                    */
);

/******************************************************************************
 * Given a drawing curve (a silhouette or a section edge) or an edge that
 * is a conic or a spline, and the tag to a drawing member view where
 * this curve or edge resides, this function returns simplified curves (if
 * they exist), and the simplification creation information. If a
 * NULL_TAG is input as the view_tag and the master_curve_tag is a
 * section edge or silhouette, the view is inferred, and if the
 * master_curve_tag is an edge, the first view found where the edge is
 * simplified is used.
 *
 * Environment: Internal  and  External
 * See Also: 
 * History: Original release was in V13.0.
 ******************************************************************************/
extern UFUNEXPORT int UF_DRAW_ask_simplified_curve(
tag_t master_curve_tag ,/* <I>
                        Tag of the master curve or edge that was simplified.
                        */
tag_t * view_tag ,/* <I/O>
                  Tag of the drawing member view of the
                  master_curve.
                  */
logical * flat_arc_to_line ,/* <O>
                            If TRUE, a post processing of the arc segments
                            output from the simplification was performed to
                            convert flat arc segments with chordal tolerance
                            less than half the view display tolerance to line
                            segments.  Also, adjacent line segments and arc
                            segments may have been joined, if the result was
                            within half of the view display tolerance.
                            */
double * tolerance ,/* <O>
                    Tolerance that was used to produce the simplification.
                    */
int * num_segments ,/* <O>
                    Number of simplified curves
                    */
tag_p_t * segments  /* <OF,len:num_segments>
                    Array of simplified curves.  Use UF_free to free memory.
                    */
);

/****************************************************************************
 * Adds an orthographic view to the current drawing.
 *
 * Environment: Internal  and  External
 * See Also:  UF_DRAW_proj_dir_t
 *           
 * History:This function was originally released in V15.0
 ***************************************************************************/
extern UFUNEXPORT int UF_DRAW_add_orthographic_view(
   const tag_t      drawing_tag, /* <I>  The drawing tag (must be current
                                 drawing).
                                 */
   const tag_t   parent_view_tag, /* <I>
                                  tag of parent view.
                                  */
 const UF_DRAW_proj_dir_t projection_direction, /* <I>
                                                direction of projection if none
                                                specified, the projection
                                                direction is determined by the
                                                location of the drawing
                                                reference point relative to the
                                                center of the parent view
                                                */

   double      dwg_reference_point[2], /* <I>
                                       Drawing reference point (drawing
                                       coordinates)
                                       */
   tag_t          *ortho_view_tag    /* <O>
                                     tag of orthographic view
                                     */
);

/****************************************************************************
 * Adds an auxiliary view to the current drawing.
 *
 * Environment: Internal  and  External
 * See Also: 
 * History:This function was originally released in V15.0
 ***************************************************************************/
extern UFUNEXPORT int UF_DRAW_add_auxiliary_view(
const tag_t       drawing_tag, /* <I>
                               The drawing tag (must be current drawing).
                               */
const tag_t       parent_view_tag, /* <I>
                                   tag of parent view.
                                   */
const tag_t       hinge_line_tag, /* <I>
                                  tag of smart hinge line
                                  */
double            dwg_reference_point[2], /* <I>
                                          Drawing reference point (drawing
                                          coordinates)
                                          */
tag_t            *aux_view_tag /* <O>
                               tag of auxiliary view
                               */
);


/***************************************************************************
 * This function adds a detailed view to the current drawing.
 * There is currently a restriction requiring the input drawing
 * tag to be the tag of the current drawing. We intend to relax this
 * restriction in the future. As a result, we are requiring the input tag to
 * ensure that future code changes will not be required by NX Open
 * API developers.
 *
 * Environment: Internal  and  External
 * See Also: 
 * History: Original release was in V13.0.
 ***************************************************************************/
extern UFUNEXPORT int UF_DRAW_add_detail_view(
const tag_t drawing_tag ,/* <I>
                         Drawing Tag, must be the current drawing.
                         */
const tag_t parent_view_tag ,/* <I>
                             tag of parent view.
                             */
double xy1[2] ,/* <I>
               Left lower corner of area to create detailed view, in
               drawing coordinates (x1,y1).
               */
double xy2[2] ,/* <I>
               Right upper corner of area to create detailed view,
               in drawing coordinates (x2, y2).  This corner should
               be the diagonal corner to corner1.
               */
const double view_scale ,/* <I>
                         desired view scale of detailed view.
                         */
double dwg_reference_point[2] ,/* <I>
                               Drawing Reference point (in drawing
                               coordinates x,y)
                               */
tag_t * detail_view_tag  /* <O>
                         tag of new detail view.
                         */
);

/****************************************************************************
 * Adds an associative circular detail view to the current drawing.
 *
 * Environment: Internal  and  External
 * See Also: 
 * History: Original release was in V15.0.
 ***************************************************************************/
extern UFUNEXPORT int UF_DRAW_add_circ_detail_view(
 const tag_t       drawing_tag, /* <I>
                                The drawing tag (must be current drawing).
                                */
 const tag_t       parent_view_tag, /* <I>
                                    tag of parent view.
                                    */
 const tag_t       center_pt_tag, /* <I>
                                  tag of smart center point for the detail
                                  circle.
                                  */
 const tag_t       circle_pt_tag, /* <I>
                                  tag of smart point on the detail circle.
                                  */
 const double      view_scale, /* <I>
                               The desired view scale
                               */
 double            dwg_reference_point[2], /* <I>
                                           Drawing reference point (drawing
                                            coordinates)
                                           */
 tag_t            *detail_view_tag /* <O>
                                   tag of detail view
                                   */
);

/***************************************************************************
 * This function initializes the view info structure that
 * is used as an input to UF_DRAW_import_view.
 *
 * The default settings that are assinged to this structure are:
 *   view_info->view_status = UF_DRAW_ACTIVE_VIEW
 *   view_info->anchor_point = NULL_TAG
 *   view_info->view_scale = 1.0
 *   view_info->use_ref_pt = FALSE
 *   view_info->transfer_annotation = TRUE
 *   view_info->inherit_boundary = FALSE
 *   view_info->model_name[0] = '\0'
 *   view_info->arrangement_name[0] = '\0'
 *
 * Environment: Internal  and  External
 * History: Original release in V16.0.
 ***************************************************************************/
extern UFUNEXPORT void UF_DRAW_initialize_view_info(
UF_DRAW_view_info_t *view_info  /* <O> info structure to be initialized */
);/* <NEC> */

/***************************************************************************
 * This function gets the part name of the model view
 * that is imported into the drawing member view
 *
 * Environment: Internal and External
 * History: Original release in NX5.0.3
 ***************************************************************************/
extern UFUNEXPORT int UF_DRAW_get_view_model_view_part
(
    tag_t view,                                   /* <I> drawing member view                    */
    char  model_view_partname[ MAX_FSPEC_BUFSIZE ] /* <O> (filespec with path) part name of view */
);

/***************************************************************************
 * This function determines if the component is a Drafting component,
 * that is, if the component is a result of Add View from Part
 *
 * Environment: Internal and External
 * History: Original release in NX5.0.3
 ***************************************************************************/
extern UFUNEXPORT int UF_DRAW_is_drafting_component
(
    tag_t    component,            /* <I> component being tested                   */
    logical *is_drafting_component /* <O> true - component is a Drafting component */
);

/***************************************************************************
 * This function imports a view onto the current drawing.  Use the view
 * info structure to set the view status, anchor point, view scale, use
 * reference point, clean model view, transfer annotation, and inherit
 * boundary parameters.
 * NOTE: There is currently a restriction requiring the input drawing tag
 * to be the tag of the current drawing. We intend to relax this restriction
 * in the future. As a result, we are requiring the input tag to ensure that
 * future code changes will not be required by NX or by
 * NX Open API developers.
 *
 * Environment: Internal  and  External
 * History: Original release in V13.0.
 ***************************************************************************/
extern UFUNEXPORT int UF_DRAW_import_view(
const tag_t drawing_tag ,/* <I>
                         Drawing Tag, must be the current drawing.
                         */
const tag_t view_tag ,/* <I>
                      Tag of model view to import.
                      */
double dwg_reference_point[2] ,/* <I>
                               Drawing Reference Point (in drawing
                               coordinates, x,y).
                               */
UF_DRAW_view_info_t * view_info ,/* <I>
                                 View Info (see uf_draw_types.h).
                                 */
tag_t * draw_view_tag  /* <O>
                       View Tag of imported view on drawing
                       */
);


/***************************************************************************
 * This function retrieves the information about a drawing, including the
 * size, scale, units, and projection angle.
 *
 * Environment: Internal  and  External
 * See Also:  UF_DRAW_set_drawing_info
 *           
 * History: Original Release was in V13.0.
***************************************************************************/
extern UFUNEXPORT int UF_DRAW_ask_drawing_info(
tag_t drawing_tag ,/* <I>
                   Drawing Tag - if a NULL_TAG is passed in for the drawing_tag,
                   the current drawing will be used.
                   */
UF_DRAW_info_t * drawing_info  /* <O>
                               Pointer to Drawing Info Structure
                               */
);

/***************************************************************************
 * Sets the information about the current drawing, including the size,
 * scale, units, and projection angle. The projection angle cannot be
 * changed if a drawing has one or more auxiliary or orthogonal views.
 * NOTE: There is currently a restriction requiring the input drawing tag
 * to be the tag of the current drawing. We intend to relax this restriction
 * in the future. As a result, we are requiring the input tag to ensure that
 * future code changes will not be required by NX or by
 * NX Open API developers.
 *
 * Environment: Internal  and  External
 * See Also:  UF_DRAW_ask_drawing_info
 * History: Original release was in V13.0.
***************************************************************************/
extern UFUNEXPORT int UF_DRAW_set_drawing_info(
const tag_t drawing_tag ,/* <I>
                         Drawing Tag, must be the current drawing.
                         */
UF_DRAW_info_p_t drawing_info  /* <I>
                               Pointer to Drawing Info Structure
                               */
);

/***************************************************************************
 * Defines an associative view reference point that is to coincide with the
 * view anchor point. The anchor point must be on the model, or in the
 * view (not on the drawing sheet). An anchor point cannot be a point on
 * a drawing member view's boundary curves. The anchor point must be
 * a smart point. If you wish to use a "dumb point" to set the view
 * reference point, use uc6484.
 *
 * Please reference ufd_drw_set_view_anchor.c to review an example of
 * using this function.
 *
 * Environment: Internal  and  External
 * See Also:  UF_DRAW_ask_view_anchor
 *           
 * History: Original release was in V13.0.
***************************************************************************/
extern UFUNEXPORT int UF_DRAW_set_view_anchor(
const tag_t view_tag ,/* <I>
                      Tag of the view whose location is to be defined.
                      */
const tag_t anchor_point  /* <I>
                          Tag of a smart point which defines the location of
                          the model that will coincide with the drawing
                          reference point  The point must be a smart point
                          (see uf_so.h).
                          */
);

/**************************************************************************
 * Retrieves the view's anchor point.
 *
 * Environment: Internal  and  External
 * See Also:See the SAMPLE=ufd_drw_ask_view_anchor.c example ENDSAMPLE
 * History: Original Release was in V13.0.
***************************************************************************/
extern UFUNEXPORT int UF_DRAW_ask_view_anchor(
const tag_t view_tag ,/* <I>
                      Tag of view whose model reference point
                      is to be obtained.
                      */
tag_t * anchor_point  /* <O>
                      Pointer to tag of point that represents
                      the view reference point.
                      */
);
/****************************************************************************
Sets the view boundary type to Bound By Objects and defines an array of
objects that must be contained with the bounds of the view.

Environment: Internal  and  External
See Also:  UF_DRAW_ask_bound_by_objects
          
History: Original release was in V13.0
 ****************************************************************************/
extern UFUNEXPORT int UF_DRAW_define_bound_by_objects(
const tag_t view_tag ,/* <I>
                      Tag of the view whose location is to be defined.
                      */
const int num_objects ,/* <I>
                       Number of tags in the bounded_objects array.
                       */
tag_t* bounded_objects  /* <I,len:num_objects> num_objects
                        Array of tags of objects to be used to calculate the
                        bounding box for the view boundary.
                        */
);

/****************************************************************************
Retrieves the view's bounded objects.

Environment: Internal  and  External
See Also:  UF_DRAW_define_bound_by_objects
          
History: Original release was in V13.0.
****************************************************************************/
extern UFUNEXPORT int UF_DRAW_ask_bound_by_objects(
const tag_t view_tag ,/* <I>
                      Tag of view whose model reference point is to be obtained.
                      */
int* num_objects ,/* <O>
                  Pointer to int that represents the number
                  of object tags returned.
                  */
tag_t** bounded_objects  /* <OF,len:num_objects>
                         Pointer to tag array of objects used to
                         calculate the bounding box for the view
                         boundary. Use UF_free() to free this
                         array when done.
                         */
);

/****************************************************************************
Retrieves the view's boundary type.

Environment: Internal  and  External
See Also: 
History: Original Release was in V13.0.
****************************************************************************/
extern UFUNEXPORT int UF_DRAW_ask_boundary_type(
const tag_t view_tag ,/* <I>
                      Tag of view whose model reference point is to be
                      obtained.
                      */
UF_DRAW_boundary_type_t * boundary_type  /* <O>
                                         Boundary type of member view:
                                         UF_DRAW_BREAK_DETAIL_TYPE,
                                         UF_DRAW_MANUAL_RECTANGLE_TYPE,
                                         UF_DRAW_AUTOMATIC_RECTANGLE_TYPE,
                                         UF_DRAW_BOUND_BY_OBJECTS_TYPE
                                         */
);

/****************************************************************************
This routine copies a view and its associated annotation, leaving the
new view positioned on top of the original view.  The new view can be
moved to another drawing with UF_DRAW_move_view_to_drawing, or
to another position on the same drawing with UF_DRAW_move_view.

Environment: Internal  and  External
See Also:  UF_DRAW_move_view_to_drawing
           UF_DRAW_move_view
          
History: Original Release was in V13.0.
****************************************************************************/
extern UFUNEXPORT int UF_DRAW_copy_view(
tag_t view_tag ,/* <I>
                Tag of drawing member view to copy.  It must be on
                the current drawing.
                */
tag_t * new_view  /* <O>
                  Pointer to new view (copy of the original view).
                  */
);

/****************************************************************************
This routine moves a specified view to the given position on the
current drawing.

Environment: Internal  and  External
See Also:  UF_DRAW_copy_view
           UF_DRAW_move_view_to_drawing
          
History: Original release was in V13.0.
****************************************************************************/
extern UFUNEXPORT int UF_DRAW_move_view(
const tag_t view_tag ,/* <I>
                      Drawing member view to move.  It must be on
                      the current drawing.
                      */
const double drawing_reference_point[2]  /* <I>
                                         Desired drawing reference point, in
                                         drawing coordinates.
                                         */
);

/****************************************************************************
This routine moves a drawing member view to the specified drawing.
Annotation spanning the view and other views on the drawing are
deleted. If the view does not fit on a smaller destination drawing, an
error is returned.

Environment: Internal  and  External
See Also:  UF_DRAW_copy_view
           UF_DRAW_move_view
          
History: Original release was in V13.0.
****************************************************************************/
extern UFUNEXPORT int UF_DRAW_move_view_to_drawing(
tag_t view_tag ,/* <I>
                Tag of drawing member view to move.  It must be
                on the current drawing.
                */
const tag_t drawing_tag  /* <I>
                         Destination drawing tag.  It must not be the current
                         drawing.
                         */
);

/****************************************************************************
This routine makes the boundary associative with the model by
making each defining point in the boundary a smart point which is at a
fixed offset from the anchor point. The view's anchor point must be
defined, and it must be a smart point which is associated with the
model. This function uses the structure boundary_curves to return the
tags of each boundary curve's smart defining points. For this function
to successfully complete, none of the curves in the boundary can
already be associative with the model. If the boundary contains a
spline, that spline must be defined via defining points and cannot have
tangency or curvature constraints.

Environment: Internal  and  External
See Also:  UF_DRAW_define_view_boundary
           UF_DRAW_edit_boundary_point

Return:
         Return code:
          UF_DRAW_NO_ERRORS  - The view boundary was successfully
                               made to be associative.
          UF_DRAW_tag_is_null - The view tag or the model_reference_pt
                                tag is null.
          UF_DRAW_invalid_parameter - A parameter is invalid, such as
                                      curve_count is less than or equal
                                      to zero.
          UF_DRAW_anchor_point_is_not_smart_point - The anchor point is
                                                    not a smart point
                                                    associated with the
                                                    model.
          UF_DRAW_sketch_object - At least one of the curves in the
                                  boundary belongs to a sketch.
          UF_DRAW_curve_is_associative - At least one of the curves in the
                                         boundary is already associative
                                         and has smart defining points.
          UF_DRAW_invalid_spline - There is a spline in the boundary which
                                   violates the following rule. The spline
                                   must be defined via defining points and
                                   cannot have tangency or curvature
                                   constraints.

See Also: 
History: Original release was in V14.0.
****************************************************************************/
extern UFUNEXPORT int UF_DRAW_set_boundary_assoc(
tag_t view ,/* <I>
            Tag of the view whose boundary is to be
            made associative.  The view must have
            a break line/detail boundary type.  The
            view must have an anchor point
            defined.
            */
int * curve_count ,/* <O>
                   Pointer to count of curves in curve list
                   */
UF_DRAW_view_boundary_p_t * boundary_curves  /* <OF,len:curve_count,free:UF_DRAW_free_boundary>
                                             Pointer to curve list, i.e. array
                                             of structures containing the
                                             boundary curves and the points
                                             used to define them.   Use
                                             UF_DRAW_free_boundary to free the
                                             pointer.
                                             */
);

/***************************************************************************
 *  Frees the memory in the boundary_curves structure.
 *
 * Environment: Internal  and  External
 * See Also:  UF_DRAW_ask_bound_by_objects
 *           
 * History: Original release was in V14.0.
***************************************************************************/
extern UFUNEXPORT int UF_DRAW_free_boundary(
int  curve_count ,/* <I>
                  Count of curves in curve list
                  */
UF_DRAW_view_boundary_p_t boundary_curves  /* <I>
                                           Pointer to curve list, i.e. array of
                                           structures containing the boundary
                                           curves and their defining points.
                                           */
);/*<NON_NXOPEN>*/

/***************************************************************************
 * Replaces a smart defining point for an associative view boundary
 * curve with a new smart defining point. This function may return errors
 * used in UF_DRAW_define_view_boundary, because when defining_pt is
 * replaced with new_pt, the break line/detail boundary is redefined,
 * based on the new point location.
 *
 * Environment: Internal  and  External
 * See Also:  UF_DRAW_set_boundary_assoc
 *           
 *           
 * History: Original release was in V14.0.
***************************************************************************/
extern UFUNEXPORT int UF_DRAW_edit_boundary_point(
tag_t defining_point ,/* <I>
                      Tag of the defining point which is to be replaced
                      */
tag_t new_point ,/* <I>
                 Tag of the new point which will replace the defining point.
                 */
tag_t view_tag  /* <I>
                Tag of the view whose defining point is being replaced. The
                view must have a break line/detail type boundary, and the
                boundary must be associated to model geometry (via
                UF_DRAW_set_boundary_assoc).
                */
);

/***************************************************************************
 * Detemines if a note is associated to a drawing member view. If so, this
 * function returns the view tag as an output.  This routine is not meant to
 * determine the view associated to a view label.
 * Use UF_DRAW_ask_view_of_view_label() to determine the view associated to a
 * view label.
 *
 * Environment: Internal  and  External
 * See Also:  UF_DRAW_ask_view_notes
 *            UF_DRAW_attach_note_to_view
 *            UF_DRAW_detach_note_from_view
 *            UF_DRAW_ask_view_of_view_label
 *           
 *
 * History: Original release was in V14.0.
***************************************************************************/
extern UFUNEXPORT int UF_DRAW_ask_view_of_note(
tag_t note_tag ,/* <I>
                Note tag
                */
tag_t *view_tag  /* <O>
                 The drawing member view the note is associated to.
                 NULL_TAG if the note is not associated to a view.
                 */
);

/***************************************************************************
 * Checks whether a drawing member view has associated notes. If true,
 * this function returns the tags of the notes as output. Otherwise, the
 * number of the associated notes is zero (0).
 *
 * Environment: Internal  and  External
 * See Also:  UF_DRAW_ask_view_of_note
 *            UF_DRAW_attach_note_to_view
 *            UF_DRAW_detach_note_from_view
 *           
 *
 * History: Original release was in V14.0.
***************************************************************************/
extern UFUNEXPORT int UF_DRAW_ask_view_notes(
tag_t view_tag ,/* <I>
                Drawing member view tag
                */
int * num_notes ,/* <O>
                 Number of associated notes
                 */
tag_p_t * note_tags  /* <OF,len:num_notes>
                     If num_notes > 0, the array of note tags must be
                     freed. Use UF_free to free note_tags.
                     */
);

/***************************************************************************
 * Associates an existing note to an existing drawing member view. If the
 * note is already associated to another drawing member view, it need
 * not be disassociated from the view prior to calling this function.
 *
 * Environment: Internal  and  External
 * See Also:  UF_DRAW_ask_view_of_note
 *            UF_DRAW_ask_view_notes
 *            UF_DRAW_detach_note_from_view
 *           
 *
 * History: Original release was in V14.0.
***************************************************************************/
extern UFUNEXPORT int UF_DRAW_attach_note_to_view (
tag_t note_tag ,/* <I>
                Note tag to be associated to the view
                */
tag_t view_tag  /* <I>
                The drawing member view the note will be
                associated to.
                */
);

/***************************************************************************
 * Disassociates an existing note from an existing drawing member view.
 * NOTE: A section view label cannot be disassociated from the section
 * view. A section line cannot be disassociated from its parent view.
 *
 * Environment: Internal  and  External
 * See Also:  UF_DRAW_ask_view_of_note
 *            UF_DRAW_ask_view_notes
 *            UF_DRAW_attach_note_to_view
 *           
 * History: Original release was in V14.0.
***************************************************************************/
extern UFUNEXPORT int UF_DRAW_detach_note_from_view (
tag_t note_tag  /* <I>
                Note tag to be associated to the view
                */
);

/***************************************************************************

This routine creates a render set with the given display preferences

Environment: Internal  and  External
See also: See the example program  ufd_draw_render_set.c

History: Created in v16.0
 ****************************************************************************/
extern UFUNEXPORT int UF_DRAW_create_render_set
(
    char *render_set_name,                 /*<I> Desired name of render set. */
    UF_DRAW_render_prefs_t *render_parms,  /*<I> Pointer to render set
                                                 preferences structure,
                                                 with desired settings for
                                                 visible and hidden line
                                                 color, font, and widths,
                                                 edge hiding edge and hidden
                                                 line options.  */
    tag_t *render_set                      /*<O> Tag of newly created render
                                                 set, if successful. */
);

/***************************************************************************

This routine defines the objects (solids or component sets) the  given
render set will reference.  The objects will replace the objects the render set
referenced prior to calling this function.

Environment: Internal  and  External
See also: See the example program  ufd_draw_render_set.c

History: Created in v16.0

 ****************************************************************************/
extern UFUNEXPORT int UF_DRAW_set_render_set_objects
(
    tag_t render_set,    /*<I> Tag of render set. */
    int number_objects,  /*<I> Number of objects to be included in the render
                               set. Set to zero if you want the render set to
                               contain no objects.         */
    tag_t *objects       /*<I,len:number_objects> number_objects
                               Array of solids or component sets to be
                               referenced by the render set.  These objects will
                               replace the objects the render set referenced
                               prior to calling this function. Set to NULL if
                               you want the render set to contain no objects. */
);

/***************************************************************************

This routine retrieves the objects (solids or component sets) the  given
render set reference.

Environment: Internal  and  External
See also: See the example program  ufd_draw_render_set.c

History: Created in v16.0

 ****************************************************************************/
extern UFUNEXPORT int UF_DRAW_ask_render_set_objects
(
    tag_t render_set,    /*<I> Tag of render set. */
    int *number_objects, /*<O> Number of objects referenced by the render set.*/
    tag_p_t *objects     /*<OF,len:number_objects> Array of solids or component sets to be
                                referenced by the render set.  Use UF_free() to
                                free the memory pointed to by this variable. */
);

/***************************************************************************

This routine sets the display parameters for a given render set.

Environment: Internal  and  External
See also: See the example program  ufd_draw_render_set.c

History: Created in v16.0

 ****************************************************************************/
extern UFUNEXPORT int UF_DRAW_set_render_set_parms
(
    tag_t render_set,                      /*<I> Tag of render set. */
    UF_DRAW_render_prefs_t *render_parms   /*<I> Pointer to render set
                                                 preferences structure, with
                                                 desired settings for visible
                                                 and hidden line color, font,
                                                 and widths, edge hiding edge
                                                 and hidden line options.   */
);

/***************************************************************************

This routine retrieves the display parameters for a given render set.

Environment: Internal  and  External
See also: See the example program  ufd_draw_render_set.c

History: Created in v16.0

 ****************************************************************************/
extern UFUNEXPORT int UF_DRAW_ask_render_set_parms
(
    tag_t render_set,                      /*<I> Tag of render set.  If this is
                                                 a NULL_TAG, the function
                                                 retrieves the default
                                                 parameters.            */
    UF_DRAW_render_prefs_t *render_parms   /*<O> Pointer to render set
                                                 preferences structure, with
                                                 settings for visible and hidden
                                                 line color, font, and widths,
                                                 edge hiding edge and hidden
                                                 line options.          */
);

/***************************************************************************

This routine defines the render sets to be rendered in the given
drawing member view.  List the render sets in the desired rendering
order.

Environment: Internal  and  External
See also: See the example program  ufd_draw_render_set.c

History: Created in v16.0

 ****************************************************************************/
extern UFUNEXPORT int UF_DRAW_set_render_sets_for_view
(
    tag_t view,                /*<I> Tag of drawing member view. */
    int number_render_sets,    /*<I> Number of render sets      */
    tag_t *render_sets         /*<I,len:number_render_sets> Array of render sets to be rendered in the
                                     given view. List them in the desired
                                     rendering order.              */
);

/***************************************************************************

This routine retrieves the render sets references by the given drawing member
view.  These render sets are listed in the order they are rendered in.

Environment: Internal  and  External
See also: See the example program  ufd_draw_render_set.c

History: Created in v16.0

 ****************************************************************************/
extern UFUNEXPORT int UF_DRAW_ask_render_sets_of_view
(
    tag_t view,                /*<I> Tag of drawing member view. */
    int *number_render_sets,   /*<O> Number of render sets      */
    tag_p_t *render_sets       /*<OF,len:number_render_sets> Array of render sets referenced by the
                                      given view. They are listed in the
                                      rendering order.  This array must be freed
                                      by calling UF_free.  */
);

/***************************************************************************

This routine retrieves the render sets in the current part.


Environment: Internal  and  External
See also: See the example program  ufd_draw_render_set.c

History: Created in v16.0

 ****************************************************************************/
extern UFUNEXPORT int UF_DRAW_ask_render_sets
(
    int *number_render_sets,   /*<O> Number of render sets in the part.   */
    tag_p_t *render_sets       /*<OF,len:number_render_sets> Array of render sets in the current part.
                                      Use UF_free to free the memory.   */
);

/****************************************************************************
 * (use UF_DRAW_set_display_state)
 *
 * set drawing display state in the drafting application
 *
 * Return code:
 *      1 = OK
 *          if not 1,
 *          error_code = UF_DRAWING_STATE_OK
 *          error_code = UF_DRAWING_INVALID_STATE_FLAG
 *          error_code = UF_DRAWING_NOOP_WORK_MEM_VIEW
 *          error_code = UF_DRAWING_STATE_NOT_SET
 *          error_code = UF_DRAWING_NO_VIEW_AVAILABLE
 *
 * Environment: Internal and External
 * See also:
 * History:
 ****************************************************************************/
extern UFUNEXPORT int uc6476
(
    int view_type /* <I> type of view
                         1 = modeling view
                         2 = drawing view  */
);

/****************************************************************************
 * This routine sets the drawing display state.
 *
 *  Environment: Internal and External
 *  See also: See the example program  ufd_draw_aux_view.c
 *  History: New for V16.0
 ****************************************************************************/
extern UFUNEXPORT int UF_DRAW_set_display_state(
    const int view_type        /* <I>  Setting Flag
                                  1 = Modeling View
                                  2 = Drawing View
                               */
);

/****************************************************************************
 * (use UF_DRAW_ask_display_state)
 *
 * ask drawing display state in the drafting application
 *
 * Return code:
 *      1 = modeling view
 *      2 = drawing view
 *          if not 1 or 2, error_code
 *
 * Environment: Internal and External
 * See also:
 * History:
 ****************************************************************************/
extern UFUNEXPORT int uc6477 (void);

/****************************************************************************
 *
 * This routine retrieves the drawing display state in the drafting
 * application.  The view_type parameter does not indicate what type of view
 * is being displayed, it indicates what will be displayed when you are in
 * the Drafting application.
 * To determine if a drawing is currently displayed in any application, use
 * UF_DRAW_ask_current_drawing.
 * To determine the type of the work view, use UF_VIEW_ask_work_view
 * then UF_VIEW_ask_type.
 *
 *  Environment: Internal and External
 *  See also: See the example program  ufd_drw_ask_display_state.c
 *  History: New for V16.0
 ****************************************************************************/
extern UFUNEXPORT int UF_DRAW_ask_display_state(
    int *view_type                   /* <O>  Flag Setting:
                                             1 = Modeling View
                                             2 = Drawing View
                                     */
);

/****************************************************************************
 * (use UF_DRAW_create_drawing)
 *
 * create drawing
 *
 * Return code:
 *      0 = OK
 *          if not 0,
 *          error_code = UF_DRAWING_DESIGN_IN_CONTEXT
 *          error_code = UF_DRAWING_WORK_IN_MEMBER_VIEW
 *          error_code = UF_DRAWING_INVALID_DRAWING_NAME
 *          error_code = UF_DRAWING_DRAWING_ALREADY_EXISTS
 *          error_code = UF_DRAWING_VIEW_ALREADY_EXISTS
 *          error_code = UF_DRAWING_INVALID_UNITS
 *          error_code = UF_DRAWING_INVALID_SIZE_CODE
 *          error_code = UF_DRAWING_INVALID_DRAWING_SIZE
 *
 * Environment: Internal and External
 * See also:
 * History:
 ****************************************************************************/
extern UFUNEXPORT int uc6478
(
    const char   *drawing_name,  /* <I> drawing name
                                        " " = current drawing
                                        (UF_OBJ_NAME_NCHARS characters max)   */
    const int     drawing_units, /* <I> drawing units
                                        1 = inches
                                        2 = millimeters       */
    const int     size_code,     /* <I> drawing size code
                                        0 = custom size
                                        1 = A/A0
                                        2 = B/A1
                                        3 = C/A2
                                        4 = D/A3
                                        5 = E/A4
                                        6 = F/--
                                        7 = H/--
                                        8 = J/--              */
    const double *custom_size    /* <I> custom drawing size
                                        [0] height
                                        [1] width             */
);

/****************************************************************************
 *
 * This routine creates a new drawing.
 *
 * Environment: Internal and External
 * See also: See the example program  ufd_drw_create_drawing.c
 * History: New for V16.0
 *
 ****************************************************************************/
extern UFUNEXPORT int UF_DRAW_create_drawing(
    const char            *drawing_name, /* <I>  Name of the drawing. */
    const UF_DRAW_info_p_t drawing_info, /* <I>  The desired drawing info. */
    tag_p_t                drawing_tag   /* <O>  Tag of the new drawing. */
);

/****************************************************************************
 * (use UF_DRAW_ask_drawing_info)
 *
 * ask drawing size
 *
 * Return code:
 *      0 = OK
 *          if not 0 = error code
 *     21 = DRAWING DOES NOT EXIST
 *     22 = INVALID DRAWING NAME
 *     29 = NO CURRENT DRAWING
 *
 * Environment: Internal and External
 * See also:
 * History:
 ****************************************************************************/
extern UFUNEXPORT int uc6479
(
    const char *drawing_name,  /* <I> drawing name
                                      " " = current drawing
                                      (UF_OBJ_NAME_NCHARS characters max)   */
    int        *drawing_units, /* <O> drawing units
                                      1 = inches
                                      2 = millimeters       */
    int        *size_code,     /* <O> drawing size code
                                      0 = custom size
                                      1 = A/A0
                                      2 = B/A1
                                      3 = C/A2
                                      4 = D/A3
                                      5 = E/A4              */
    double     *custom_size    /* <O> custom drawing size
                                      [0] height
                                      [1] width             */
);

/****************************************************************************
 * (use UF_DRAW_set_drawing_info)
 *
 * set drawing size
 *
 * Return code:
 *      0 = OK
 *          if not 0 = error code
 *     21 = DRAWING DOES NOT EXIST
 *     22 = INVALID DRAWING NAME
 *     29 = NO CURRENT DRAWING
 *     31 = INVALID UNITS
 *     32 = INVALID SIZE CODE
 *     33 = INVALID DRAWING SIZE
 *     36 = CANNOT CHANGE DRAWING SIZE WHILE WORK IN MEMBER VIEW
 *
 * Environment: Internal and External
 * See also:
 * History:
 ****************************************************************************/
extern UFUNEXPORT int uc6480
(
    const char   *drawing_name,  /* <I> drawing name
                                        " " = current drawing
                                        (UF_OBJ_NAME_NCHARS characters max)   */
    const int     drawing_units, /* <I> drawing units
                                        1 = inches
                                        2 = millimeters       */
    const int     size_code,     /* <I> drawing size code
                                        0 = custom size
                                        1 = A/A0
                                        2 = B/A1
                                        3 = C/A2
                                        4 = D/A3
                                        5 = E/A4
                                        6 = F/--
                                        7 = H/--
                                        8 = J/--              */
    const double *custom_size    /* <I> custom drawing size
                                        [0] height
                                        [1] width             */
);

/* Use UF_DRAW_import_view
   uc6481 add view to drawing */
extern UFUNEXPORT int uc6481(const char    *dwg_name,       /* <I> */
                  const char    *view_name,      /* <I> */
                  const double  *reference_pt,   /* <I> */
                  const int      view_status     /* <I> */
);
/* Use UF_VIEW_delete
   uc6482 remove view from drawing */
extern UFUNEXPORT int uc6482(const char  *dwg_name,         /* <I> */
                  const char  *view_name         /* <I> */
);

/* uc6483 read view reference point on drawing
   Use UF_DRAW_ask_drawing_ref_pt
   This is actually the drawing reference point */
extern UFUNEXPORT int uc6483(const char  *dwg_name,         /* <I> */
                  const char  *view_name,        /* <I> */
                  double      *reference_pt      /* <O> */
);
/****************************************************************************
 *
 *  This routine reads the drawing reference point for a view on the drawing.
 *  This is the point which controls where the view is on the drawing sheet.
 *
 *  Environment: Internal and External
 * See also: See the example program  ufd_drw_cre_simple_sxvw.c
 *  History: New for V16.0
 ****************************************************************************/
extern UFUNEXPORT int UF_DRAW_ask_drawing_ref_pt(
    const tag_t view_tag,             /* <I>  Tag of the view.
                                         Must be a member view. If NULL_TAG,
                                         the work view is used. It will cause
                                         an error if the work view is not a
                                         member view. */
    double reference_pt[2]              /* <O>  Reference point
                                         (Drawing Coordinates).
                                         [0] - X-coordinate
                                         [1] - Y-coordinate  */
);


/* uc6484 set view reference point on drawing
   Use UF_DRAW_set_drawing_ref_pt */
extern UFUNEXPORT int uc6484(const char    *dwg_name,       /* <I> */
                  const char    *view_name,      /* <I> */
                  const double  *reference_pt    /* <I> */
);
/****************************************************************************
 *
 *  This routine sets the drawing reference point for a view on the drawing.
 *  This is the point which controls where the view is on the drawing sheet.
 *
 *  Environment: Internal and External
 *  See also: See the example program  ufd_drw_set_drawing_ref_pt.c
 *  History: New for V16.0
 ****************************************************************************/
extern UFUNEXPORT int UF_DRAW_set_drawing_ref_pt(
    const tag_t drawing_tag,     /* <I>  Tag of the drawing.
                                    If NULL_TAG, use current drawing. */
    const tag_t view_tag,        /* <I>  Tag of the view.
                                    If NULL_TAG, use work view. */
    const double reference_pt[2]   /* <I,len:2>  Reference point
                                    (Drawing Coordinates).
                                    [0] - X-coordinate
                                    [1] - Y-coordinate  */
);

/* uc6485 read view borders on current drawing
   Use UF_DRAW_ask_view_borders */
extern UFUNEXPORT int uc6485(const char *cp1/* <I> */, double *rr2);

/****************************************************************************
 *
 *  This routine reads the view borders on the current drawing.
 *
 *  Environment: Internal and External
 *  See also: See the example program  ufd_draw_ask_view_borders.c
 *  History: New for V16.0
 ****************************************************************************/
extern UFUNEXPORT int UF_DRAW_ask_view_borders(
    const tag_t view_tag,      /* <I>  Tag of the view.
                                  If NULL_TAG, use Work view. */
    double view_borders[4]       /* <O>  View Borders (Drawing Coordinates).
                                  [0] - X min
                                  [1] - Y min
                                  [2] - X max
                                  [3] - Y max  */
);

/* uc6486 set view borders on current drawing */
extern UFUNEXPORT int uc6486(const char *cp1/* <I> */, double *rp2);

/* uc6488 read view status in drawing
   Use UF_DRAW_ask_view_status */
extern UFUNEXPORT int uc6488(const char  *dwg_name,         /* <I> */
                  const char  *view_name,        /* <I> */
                  int         *view_status       /* <O> */
);
/****************************************************************************
 *  This routine reads the view status in the drawing.
 *
 *  Environment: Internal and External
 *  See also: See the example program  ufd_drw_set_view_status.c
 *  History: New for V16.0
 ****************************************************************************/
extern UFUNEXPORT int UF_DRAW_ask_view_status(
    const tag_t view_tag,              /* <I>  Tag of the view.
                                          If NULL_TAG, use Work view. */
    UF_DRAW_view_status_t *view_status /* <O>  View Status
                                          UF_DRAW_ACTIVE_VIEW
                                          UF_DRAW_REFERENCE_VIEW */
);

/* uc6489 set view status in drawing
   Use UF_DRAW_set_view_status */
extern UFUNEXPORT int uc6489(const char  *dwg_name,         /* <I> */
                  const char  *view_name,        /* <I> */
                  const int    view_status       /* <I> */
);

/****************************************************************************
 *  This routine sets the view status in the drawing.
 *
 *  Environment: Internal and External
 *  See also: See the example program  ufd_drw_set_view_status.c
 *  History: New for V16.0
 ****************************************************************************/
extern UFUNEXPORT int UF_DRAW_set_view_status(
    const tag_t view_tag,                   /* <I>  Tag of the view.
                                               If NULL_TAG, use work view. */
    const UF_DRAW_view_status_t view_status /* <I>  View Status.
                                               UF_DRAW_ACTIVE_VIEW
                                               UF_DRAW_REFERENCE_VIEW */
);

/* Use UF_DRAW_ask_current_drawing and UF_OBJ_ask_name.
   uc6492 read current drawing name */
extern UFUNEXPORT int uc6492(
   char cr1[ UF_OBJ_NAME_BUFSIZE ] /* <O> This parameter must be a character buffer large enough to
                    hold the returned drawing name (UF_OBJ_NAME_LEN + 1).
             */
);

/* uc6494 retrieve drawing
   Use UF_DRAW_open_drawing */
extern UFUNEXPORT int uc6494(const char *dwg_name/* <I> */);

/****************************************************************************
 *
 *  This routine opens a drawing.
 *
 *  Environment: Internal and External
 *  See also: See the example program  ufd_drw_create_drawing.c
 *  History: New for V16.0
 ****************************************************************************/
extern UFUNEXPORT int UF_DRAW_open_drawing(
    const tag_t drawing_tag     /* <I>  Tag of drawing to open. */
);

/* uc6495 delete drawing
   Use UF_DRAW_delete_drawing */
extern UFUNEXPORT int uc6495(
    const char *dwg_name         /* <I> */
    );


/****************************************************************************
 *  This routine deletes the drawing.
 *
 *  Environment: Internal and External
 *  See also: See the example program  ufd_drw_delete_drawing.c
 *  History: New for V16.0
 ****************************************************************************/
extern UFUNEXPORT int UF_DRAW_delete_drawing(
    const tag_t drawing_tag      /* <I>  Tag of drawing to delete. */
);

/* uc6496 rename drawing
   Use UF_DRAW_rename_drawing */
extern UFUNEXPORT int uc6496(const char *old_dwg_name,      /* <I> */
                  const char *new_dwg_name       /* <I> */
);

/****************************************************************************
 *  This routine renames a drawing.
 *
 *  Environment: Internal and External
 *  See also: See the example program  ufd_drw_rename_drawing.c
 *  History: New for V16.0
 ****************************************************************************/
extern UFUNEXPORT int UF_DRAW_rename_drawing(
    const tag_t drawing_tag,        /* <I>  Tag of the drawing.
                                       If NULL_TAG, use current drawing */
    const char  *new_drawing_name   /* <I>  New name for the drawing. */
);

/****************************************************************************
 *  uc6497 cycle drawings in a part
 *
 *  Return code of 0 = OK
 *                21 = Drawing does not exist
 *                22 = Invalid Drawing Name
 *                all other numbers - error
 *
 *  Environment: Internal and External
 ****************************************************************************/
extern UFUNEXPORT int uc6497(
    char ca1[ UF_OBJ_NAME_BUFSIZE ]      /* <I/O> Drawing name 
                            Pass in an empty string to start the cycle.
                            By calling this function in a loop and passing
                            the last drawing name - the next drawing will be
                            returned.  An empty string is returned when
                            all drawings have been cycled.*/
    );

/****************************************************************************
 *
 *  This routine returns the number of drawings in the current work part.
 *
 *  Environment: Internal and External
 *  See also: See the example program  ufd_drw_ask_num_drawings.c
 *  History: New for V16.0
 ****************************************************************************/
extern UFUNEXPORT int UF_DRAW_ask_num_drawings(
    int *num_drawings        /* <O>    Number of drawings. */
);

/****************************************************************************
 *
 *  This routine returns an array of all of the drawings in
 *  the current work part.
 *
 *  Please reference ufd_drw_object_out_of_date.c to review an example of
 *  using this function.
 *
 *  See also: See the example program  ufd_drw_object_out_of_date.c
 *  Environment: Internal and External
 *  History: New for V16.0
 ****************************************************************************/
extern UFUNEXPORT int UF_DRAW_ask_drawings(
    int *num_drawings,        /* <O>    Number of drawings. */
    tag_p_t *drawing_tags     /* <OF,len:num_drawings>   Array of drawing tags.
                                 Use UF_free to free this memory. */
);


/* uc6498 read number of views in a drawing */
extern UFUNEXPORT int uc6498(const char *cp1/* <I> */, int *ir2);

/* uc6499 cycle views in drawing */
extern UFUNEXPORT int uc6499(const char *cp1/* <I> */, char ca2[ UF_OBJ_NAME_BUFSIZE ]/* <I/O> */);


/****************************************************************************
 *
 *  This routine returns the number of views in the given drawing.
 *
 *  Environment: Internal and External
 *  See also: See the example program  ufd_drw_ask_num_views.c
 *  History: New for V16.0
 ****************************************************************************/
extern UFUNEXPORT int UF_DRAW_ask_num_views(
    const tag_t drawing_tag,     /* <I>   Tag of the drawing.
                                    If NULL_TAG, use current drawing. */
    int         *num_views       /* <O>   Number of views in the drawing. */
);

/****************************************************************************
 *
 *  This routine reads the number of member views in the given drawing and
 *  returns an array of the member view tags.
 *
 *  Environment: Internal and External
 *  See also: See the example program  ufd_draw_ask_view_angle.c
 *  History: New for V16.0
 ****************************************************************************/
extern UFUNEXPORT int UF_DRAW_ask_views(
    const tag_t drawing_tag,  /* <I>   Tag of the drawing.
                                 If NULL_TAG, use current drawing. */
    int        *num_views,    /* <O>   Number of views in the drawing. */
    tag_p_t    *view_tag     /* <OF,len:num_views>  Array of the view tags in the drawing.
                                 Use UF_free to free this memory. */
);


/******************************************************************************
 *  This routine retrieves the tag of the drawing which contains the
 *  given member view or drawing sheet view.
 *
 *  Environment: Internal and External
 *  See also: See the example program  ufd_drf_edit_dim_assoc.c
 *  History: New for V16.0
 ****************************************************************************/
extern UFUNEXPORT int UF_DRAW_ask_drawing_of_view(
    const tag_t   member_view,  /* <I> Tag of view whose drawing is unknown.
                                       may also be a drawing sheet view      */
    tag_t        *drawing       /* <O> Tag of the drawing containing
                                   member_view. NULL_TAG if not found. */
);


/******************************************************************************
 *  This routine retrieves the tag of the drawing view for the given
 *  drawing.
 *
 *  Environment: Internal and External
 *  See also: See the example program  ufd_drw_ask_num_views.c
 *  History: New for V18.0
 ****************************************************************************/
extern UFUNEXPORT int UF_DRAW_ask_view_of_drawing(
    const tag_t   drawing,  /* <I> Tag of drawing whose view is unknown. */
    tag_t        *view      /* <O> Tag of the view for the given drawing.
                                   NULL_TAG if not found. */
);

/******************************************************************************
 * This function updates those views that are out of date.
 *
 * Environment: Internal and External
 * See Also:
 * History: Originally released in V16.0
 ******************************************************************************/
extern UFUNEXPORT int UF_DRAW_upd_out_of_date_views (
    tag_t drawing_tag /* <I>
                      If drawing_tag is the tag of a drawing,
                      it updates all the out of date views on
                      the drawing. If drawing_tag is a NULL_TAG,
                      it updates all the views in the part.
                      */
);


/******************************************************************************
 * Sets the view scale to a specific value.
 *
 * Environment: Internal and External
 * See Also:  UF_DRAW_ask_view_scale
 *           
 * History: This function was originally released in V15.0.
 ******************************************************************************/
extern UFUNEXPORT int UF_DRAW_set_view_scale (
    tag_t               view_tag, /* <I>
                                  The view tag
                                  */
    double              scale     /* <I>
                                  The new scale (must be > 0.0)
                                  */
);

/******************************************************************************
 * Returns the view scale.  Also returns the expression tag if the view
 * scale is parametric. If the view scale is not parametric, it returns a
 * NULL_TAG.
 *
 * Environment: Internal & External
 * See Also: See  UF_DRAW_set_view_scale
 *           
 * History: This function was originally released in V15.0.

 ******************************************************************************/
extern UFUNEXPORT int UF_DRAW_ask_view_scale (
    tag_t               view_tag, /* <I>
                                  The view tag
                                  */
    tag_t               *exp_tag, /* <O>
                                  The expression tag
                                  */
    double              *scale_value /* <O>
                                     The scale of the view
                                     */
);

/******************************************************************************
 *  Sets the view angle to a specific value.
 *
 * Environment: Internal & External
 * See Also: See  UF_DRAW_ask_view_angle
 *           
 * History: This function was originally released in V15.0.
 ******************************************************************************/
extern UFUNEXPORT int UF_DRAW_set_view_angle (
    tag_t               view_tag, /* <I>
                                  The view tag
                                  */
    double              angle    /* <I>
                                 The new angle in degrees.
                                 */
);

/******************************************************************************
 * Returns the view angle in degrees.
 *
 * Environment: Internal & External
 * See Also: See  UF_DRAW_set_view_angle
 *           
 * History: This function was originally released in V15.0.

 ******************************************************************************/
extern UFUNEXPORT int UF_DRAW_ask_view_angle (
    tag_t               view_tag, /* <I>
                                  The view tag
                                  */
    double              *angle_value /* <O>
                                     The angle of the view in degrees
                                     */
);


/****************************************************************************
 *  This routine asks whether or not the component of a given section view
 *  is defined to be sectioned or non-sectioned.
 *
 *  Return:
 *      0 = OK
 *      if not 0 = Failing error code
 *                 Use UF_get_fail_message to obtain the message
 *                 string associated with the error code.
 *
 *  Please reference ufd_drw_comp_section_in_view.c to review an example
 *  of using this function.
 *
 *  See also:
 *
 *  Environment: Internal and External
 *
 *  History:
 *    New for V16.0
 ****************************************************************************/
extern UFUNEXPORT int UF_DRAW_ask_comp_section_in_view(
    const tag_t component,                     /* <I> Tag of the component
                                                   in the section view. */
    const tag_t sx_view,                       /* <I> Tag of the section view.*/
    UF_DRAW_comp_section_in_view_t *sx_property /* <O> Sectioning property
                                                   UF_DRAW_NON_SECTIONED
                                                   UF_DRAW_SECTIONED
                                                   UF_DRAW_NOT_VIEW_SPECIFIED */
);


/****************************************************************************
 *  This routine sets the component of a given section view to be sectioned
 *  or non-sectioned.
 *
 *  Return:
 *      0 = OK
 *      if not 0 = Failing error code
 *                 Use UF_get_fail_message to obtain the message
 *                 string associated with the error code.
 *
 *  Please reference ufd_drw_comp_section_in_view.c to review an example
 *  of using this function.
 *
 *  See also:
 *
 *  Environment: Internal and External
 *
 *  History:
 *    New for V16.0
 ****************************************************************************/
extern UFUNEXPORT int UF_DRAW_set_comp_section_in_view(
    const tag_t component,                    /* <I> Tag of the component
                                                        in the section view. */
    const tag_t sx_view,                      /* <I> Tag of the section view. */
    const UF_DRAW_comp_section_in_view_t sx_property /* <I> Sectioning property
                                                     UF_DRAW_NON_SECTIONED
                                                     UF_DRAW_SECTIONED
                                                     UF_DRAW_NOT_VIEW_SPECIFIED
                                                     */
);


/****************************************************************************
    This routine retrieves information from a pictorial section
    line, given the tag of the section line.  A pictorial section
    line cannot be revolved or unfolded.

    Return:
        0 = OK
        if not 0 = Failure error code
                   Use UF_get_fail_message to obtain the message
                   string associated with the error code.

    Please reference ufd_drw_cre_dmv_sxvw.c to review an example of
    using this function.

    See Also:  UF_DRAW_sxline_status_t

    Environment: Internal and External

    History: New for V16.0
 ****************************************************************************/
extern UFUNEXPORT int UF_DRAW_ask_pictorial_sxline
(
    tag_t                       sxline_tag,   /* <I> Tag of the section line. */
    UF_DRAW_sxline_type_t *     sxline_type,  /* <O> Type of section line. */
    double                      cut_dir[3],   /* <O> Original user-specified
                                                     cut direction:
                                                      cut_dir[0] = x value
                                                      cut_dir[1] = y value
                                                      cut_dir[2] = z value */
    double                      arrow_dir[3], /* <O> Original user-specified
                                                      arrow direction:
                                                       arrow_dir[0] = x value
                                                       arrow_dir[1] = y value
                                                       arrow_dir[2] = z value */
    tag_t *                     parent_view_tag,   /* <O> Parent view tag. */
    int *                       num_sxviews,       /* <O> Number of section
                                                      views associated
                                                      to the input section line.
                                                   */
    tag_p_t *                   sxview_tags,       /* <OF,len:num_sxviews> Array of section
                                                      line's section views. Use
                                                      UF_free to free this. */
    int *                       num_sxsegs,        /* <O> Number of section
                                                      line segments. */
    tag_p_t *                   sxseg_tags,        /* <OF,len:num_sxsegs> Array of section line
                                                      segment tags. Use UF_free
                                                      to free this. */
    logical *                   pictorial_sxview,  /* <O> Whether or not the
                                                      section view is pictorial.
                                                   */
    UF_DRAW_sxline_status_t *   sxline_status  /* <O> Section line status */
);


/****************************************************************************
    This routine allows the user to create a section line and a
    section view from any view, excluding revolved section view
    and unfolded section view.  The display of the section line
    is pictorial.

    Return:
        0 = OK
        if not 0 = Failure error code
                   Use UF_get_fail_message to obtain the message
                   string associated with the error code.

    Please reference ufd_drw_cre_dmv_sxvw.c to review an example of
    using this function.

    See also:

    Environment: Internal and External

    History:
      New for V16.0
 ****************************************************************************/
extern UFUNEXPORT int UF_DRAW_create_sxview_from_dmv
(
    tag_t                      drawing_tag,          /* <I> Drawing tag. */
    tag_t                      parent_view_tag,      /* <I> Parent view tag. */
    UF_DRAW_sxline_type_t      section_type,         /* <I> Type of the section.
                                                     */
    double                     section_view_scale,   /* <I> Section view scale.
                                                     */
    double                     cut_dir[3],           /* <I> Cut direction vector
                                                        (unitized) relative to
                                                        the model space
                                                           cut_dir[0] = x value
                                                           cut_dir[1] = y value
                                                           cut_dir[2] = z value
                                                     */
    double                     arrow_dir[3],         /* <I> Arrow direction
                                                        vector (unitized)
                                                        relative to the model
                                                        space
                                                         arrow_dir[0] = x value
                                                         arrow_dir[1] = y value
                                                         arrow_dir[2] = z value
                                                     */
    int                        num_sxsegs,           /* <I> Number of section
                                                        line segments */
    UF_DRAW_sxline_sxsegs_p_t  segment_data,         /* <I,len:num_sxsegs> Data of these
                                                        section segments */
    double                     view_placement_pt[2], /* <I> Location of the
                                                        section view relative
                                                        to the drawing. */
    logical                    expect_pictorial_sxview, /* <I> Whether or not
                                                        we expect a pictorial
                                                        sxview. */
    tag_t *                    section_view_tag         /* <O> Tag of the newly
                                                           created section view.
                                                        */
);


/***************************************************************************
 *  This routine creates a breakout section within a given view.
 *
 *  Return:
 *      0 = OK
 *      if not 0 = Failing error code
 *                 Use UF_get_fail_message to obtain the message
 *                 string associated with the error code.
 *
 *  Please reference ufd_drw_cre_breakout.c to review an example of using
 *  this function.
 *
 *  See also:
 *
 *  Environment: Internal and External
 *
 *  History: New for V16.0
 *************************************************************************/
extern UFUNEXPORT int UF_DRAW_create_breakout
(
    tag_t view_tag,                           /* <I> View to which the breakout
                                                 is to be added. */
    UF_DRAW_breakout_data_p_t breakout_data,  /* <I> Breakout section data. */
    tag_p_t breakline                         /* <O> Tag of the breakout
                                                 section created. */
);


/**************************************************************************
 *  This routine retrieves the breakout data from a given breakout
 *  section.
 *
 *  Return:
 *      0 = OK
 *      if not 0 = Failing error code
 *                 Use UF_get_fail_message to obtain the message
 *                 string associated with the error code.
 *
 *  Please reference ufd_drw_cre_breakout.c to review an example of using
 *  this function.
 *
 *  See also:
 *
 *  Environment: Internal and External
 *
 *  History: New for V16.0
 *************************************************************************/
extern UFUNEXPORT int UF_DRAW_ask_breakout_data
(
    tag_t breakline,                         /* <I> Tag of the breakout section. */
    tag_p_t view_tag,                        /* <O> View which contains the
                                                given breakout section. */
    UF_DRAW_breakout_data_p_t breakout_data  /* <O> Breakout section data. */
);


/**************************************************************************
 *  This routine modifies the breakout data of an existing breakout
 *  section by deleting the existing breakout section and creating
 *  a new one.
 *
 *  Return:
 *      0 = OK
 *      if not 0 = Failing error code
 *                 Use UF_get_fail_message to obtain the message
 *                 string associated with the error code.
 *
 *  Please reference ufd_drw_cre_breakout.c to review an example of using
 *  this function.
 *
 *  See also:
 *
 *  Environment: Internal and External
 *
 *  History: New for V16.0
 *************************************************************************/
extern UFUNEXPORT int UF_DRAW_set_breakout_data
(
    tag_t breakline,                          /* <I> Tag of the existing
                                                 breakout section. */
    UF_DRAW_breakout_data_p_t breakout_data,  /* <I> Breakout section data. */
    tag_p_t new_breakline                     /* <O> Tag of the new (modified)
                                                 breakout section. */
);


/************************************************************************
 *  This routine removes a breakout section from a given view.
 *
 *  Return:
 *      0 = OK
 *      if not 0 = Failing error code
 *                 Use UF_get_fail_message to obtain the message
 *                 string associated with the error code.
 *
 *  Please reference ufd_drw_cre_breakout.c to review an example of using
 *  this function.
 *
 *  See also:
 *
 *  Environment: Internal and External
 *
 *  History: New for V16.0
 ***********************************************************************/
extern UFUNEXPORT int UF_DRAW_remove_breakout
(
    tag_t breakline,        /* <I> Tag of a curve in the breakout. */
    logical delete_curves   /* <I> Whether or not to delete the
                               breakout curves. */
);

/***************************************************************************
 *  This routine retrieves the array of break regions for a given view.
 *
 *  Return:
 *      0 = OK
 *      if not 0 = Failing error code
 *                 Use UF_get_fail_message to obtain the message
 *                 string associated with the error code.
 *
 *  Please reference ufd_drw_broken_view.c to review an example of using
 *  this function.
 *
 *  See also:
 *
 *  Environment: Internal and External
 *
 *  History: New for V17.0
 *************************************************************************/
extern UFUNEXPORT int UF_DRAW_ask_break_regions
(
    tag_t view_tag,                           /* <I> View to be queried */
    int *num_regions,                         /* <O> Number of break regions */
    tag_p_t *break_regions                    /* <OF,len:num_regions> Tags of the break regions;
                                                 may be NULL */
);


/***************************************************************************
 *  This routine creates a break region for a given view.
 *
 *  Return:
 *      0 = OK
 *      if not 0 = Failing error code
 *                 Use UF_get_fail_message to obtain the message
 *                 string associated with the error code.
 *
 *  Please reference ufd_drw_broken_view.c to review an example of using
 *  this function.
 *
 *  See also:
 *
 *  Environment: Internal and External
 *
 *  History: New for V17.0
 *************************************************************************/
extern UFUNEXPORT int UF_DRAW_create_break_region
(
    tag_t view_tag,                           /* <I> View to which the break
                                                 region is to be added. */
    tag_t anchor_point,                       /* <I> tag of anchor_point for break region */
    int num_curves,                           /* <I> number of boundary curves */
    UF_DRAW_break_region_boundary_p_t curves, /* <I,len:num_curves> Break region boundary data. */
    tag_p_t break_region                      /* <O> Tag of the break region created. */
);


/**************************************************************************
 *  This routine retrieves the break region data for a given break region.
 *
 *  Return:
 *      0 = OK
 *      if not 0 = Failing error code
 *                 Use UF_get_fail_message to obtain the message
 *                 string associated with the error code.
 *
 *  Please reference ufd_drw_broken_view.c to review an example of using
 *  this function.
 *
 *  See also:
 *
 *  Environment: Internal and External
 *
 *  History: New for V16.0
 *************************************************************************/
extern UFUNEXPORT int UF_DRAW_ask_break_region_data
(
    tag_t region,                            /* <I> Tag of the break region. */
    UF_DRAW_break_region_data_p_t break_region_data  /* <O> Break region data. */
);


/**************************************************************************
 *  This routine modifies the break region data of an existing break region.
 *
 *  Return:
 *      0 = OK
 *      if not 0 = Failing error code
 *                 Use UF_get_fail_message to obtain the message
 *                 string associated with the error code.
 *
 *  Please reference ufd_drw_broken_view.c to review an example of using
 *  this function.
 *
 *  See also:
 *
 *  Environment: Internal and External
 *
 *  History: New for V17.0
 *************************************************************************/
extern UFUNEXPORT int UF_DRAW_set_break_region_data
(
    tag_t break_region,                               /* <I> Tag of the break region. */
    UF_DRAW_break_region_data_p_t break_region_data   /* <I> Break region data. */
);


/************************************************************************
 *  This routine removes a break region from a given view.
 *
 *  Return:
 *      0 = OK
 *      if not 0 = Failing error code
 *                 Use UF_get_fail_message to obtain the message
 *                 string associated with the error code.
 *
 *  Please reference ufd_drw_broken_view.c to review an example of using
 *  this function.
 *
 *  See also:
 *
 *  Environment: Internal and External
 *
 *  History: New for V17.0
 ***********************************************************************/
extern UFUNEXPORT int UF_DRAW_remove_break_region
(
    tag_t break_region,     /* <I> Tag of the break region to be removed */
    logical delete_curves   /* <I> Whether or not to delete the
                               visible break region boundary curves. */
);

/************************************************************************
 *  This routine retrieves the parameters from a view label object.  If
 *  the view label has been customized and the parameters cannot be
 *  determined, UF_DRAW_invalid_parameter will be returned and
 *  view_label_parms will not be changed.
 *
 *  Note:  If the input parameter view_label_tag is NULL_TAG, the
 *         view_label_parm_type element in the view_label_parms structure
 *         must be set to a valid type in order to retrieve global view label
 *         parameters for that type of view label.
 *
 *  Return:
 *      0 = successful
 *        = UF_DRAW_invalid_parameter
 *
 *   See also:
 *
 *   Environment : Internal  and  External
 *
 *   History: Created in v17.0
 ***********************************************************************/
extern UFUNEXPORT int UF_DRAW_ask_view_label_parms (
    tag_t    view_label_tag,                /* <I> View label tag OR NULL_TAG
                                                 to ask global preferences */
    UF_DRAW_view_label_parms_p_t view_label_parms    /* <I/O> Structure that will
                                                        be filled with the view
                                                        label parameters */
);/* <NEC> */

/************************************************************************
 *  This routine sets the parameters of a view label and updates the view
 *  label.
 *
 *  Return:
 *      0 = successful
 *        = UF_DRAW_invalid_parameter
 *
 *  See also:
 *
 *  Environment : Internal  and  External
 *
 *  History: Created in v17.0
 ***********************************************************************/
extern UFUNEXPORT int UF_DRAW_set_view_label_parms (
    tag_t    view_label_tag,                /* <I> View label tag OR NULL_TAG
                                               to set global preferences */
    UF_DRAW_view_label_parms_p_t view_label_parms    /* <I> Structure that is
                                                        filled with the view
                                                        view label parameters */
);

/************************************************************************
 *  This routine retrieves the tag of the view label associated to a view.
 *  If no view label is associated, view_label_tag is set to NULL_TAG.
 *
 *  Return:
 *      0 = successful
 *        = UF_DRAW_tag_not_view
 *
 *  See also:
 *
 *  Environment : Internal  and  External
 *
 *  History: Created in v17.0
 ***********************************************************************/
extern UFUNEXPORT int UF_DRAW_ask_view_label (
   tag_t    view_tag,            /* <I> Drawing member view tag */
   tag_t    * view_label_tag     /* <O> View label tag          */
);

/************************************************************************
 *  This routine retrieves the tag of the view associated to a view label.
 *  If no view is associated, view_tag is set to NULL_TAG.
 *
 *  Return:
 *      0 = successful
 *        = UF_DRAW_tag_not_view, UF_DRAW_invalid_parameter
 *
 *  See also:
 *
 *  Environment : Internal  and  External
 *
 *  History: Created in v19.0
 ***********************************************************************/
extern UFUNEXPORT int UF_DRAW_ask_view_of_view_label (
   tag_t    view_label_tag,      /* <I> view label tag */
   tag_t    * view_tag           /* <O> Drawing member view label tag */
);
/************************************************************************
 *  This routine adds a view label to the specified view.  If a view
 *  already has a view label, the function edits the existing view label.
 *
 * Return:
 *      = 0 : successful
 *      = UF_DRAW_tag_not_view
 *      = UF_DRAW_invalid_parameter
 *
 *  See also:
 *
 *  Environment : Internal  and  External
 *
 *  History: Created in v17.0
 ***********************************************************************/
extern UFUNEXPORT int UF_DRAW_create_view_label (
    tag_t      view_tag,                       /* <I> Drawing member view tag */
    UF_DRAW_view_label_parms_p_t view_label_parms,   /* <I> Structure that is
                                                        filled with the view
                                                        view label parameters */
    tag_t      *view_label_tag                          /* <O> View label tag */
);
/************************************************************************
 *  This routine deletes a view label from the specified view.  The
 *  routine silently ignores views that do not already include a view label.
 *
 *  Return:
 *      = 0 : successful
 *      = UF_DRAW_tag_not_view
 *
 *  See also:
 *
 *  Environment : Internal  and  External
 *
 *  History: Created in v17.0
 ***********************************************************************/
extern UFUNEXPORT int UF_DRAW_delete_view_label (
         tag_t    view_tag     /* <I> Drawing member view tag */
);

/****************************************************************************
 *  This routine sets the plane to the drawing member view. The view will be
 *  rotated to the plane after view update.   
 *  Either the plane or the x_vector, or both, needs to be defined.
 *  If a tag of an xform is used for the plane, then an x_vector is not needed to fully define the orientation.
 *  If a tag of a plane is used for the plane, then an x_vector is needed to fully define the orientation.
 *
 *  Return:
 *      0 = OK
 *      if not 0 = Failing error code
 *                 Use UF_get_fail_message to obtain the message
 *                 string associated with the error code.
 *
 *
 *  See also:
 *
 *  Environment: Internal and External
 *
 *  History:
 *    New for V18.0
 *
 ****************************************************************************/
extern UFUNEXPORT int UF_DRAW_set_dmv_rotation_plane(
    const tag_t view,                                 /* <I> Tag of the view */
    const tag_t plane,                                /* <I> Tag of the plane */
    const tag_t x_vector                              /* <I> Tag of the x direction */
);

/****************************************************************************
 *  This routine outputs the plane tag which is associated with the view
 *  orientation.
 *
 *  Return:
 *      0 = OK
 *      if not 0 = Failing error code
 *                 Use UF_get_fail_message to obtain the message
 *                 string associated with the error code.
 *
 *
 *  See also:
 *
 *  Environment: Internal and External
 *
 *  History:
 *    New for V18.0
 *
 ****************************************************************************/
extern UFUNEXPORT int UF_DRAW_ask_dmv_rotation_plane(
    const tag_t view,                                  /* <I> Tag of the view */
    tag_p_t plane                                      /* <O> The associated plane */
);


/****************************************************************************
 *  This routine removes the associativity between the plane tag and the view,
 *  and restores the view orientation.
 *
 *  Return:
 *      0 = OK
 *      if not 0 = Failing error code
 *                 Use UF_get_fail_message to obtain the message
 *                 string associated with the error code.
 *
 *
 *  See also:
 *
 *  Environment: Internal and External
 *
 *  History:
 *    New for V18.0
 *
 ****************************************************************************/
extern UFUNEXPORT int UF_DRAW_remove_dmv_rotation_plane(
    const tag_t view                                  /* <I> Tag of the view */
);

/****************************************************************************
 *  This routine displays the input faces and/or bodies, and erases all the
 *  others in the section view.
 *
 *  Return:
 *      0 = OK
 *      if not 0 = Failing error code
 *                 Use UF_get_fail_message to obtain the message
 *                 string associated with the error code.
 *
 *
 *  See also:
 *
 *  Environment: Internal and External
 *
 *  History:
 *    New for V18.0
 *
 ****************************************************************************/
extern UFUNEXPORT int UF_DRAW_erase_sxview_objects(
    const tag_t view,            /* <I> Tag of the view */
    const int num_objects,       /* <I> Number of objects */
    const tag_p_t objects        /* <I,len:num_objects> num_objects
                                 An array of objects */
);

/****************************************************************************
 *  This routine outputs the diusplayed objects which were defined by the user.
 *
 *
 *  Return:
 *      0 = OK
 *      if not 0 = Failing error code
 *                 Use UF_get_fail_message to obtain the message
 *                 string associated with the error code.
 *
 *
 *  See also:
 *
 *  Environment: Internal and External
 *
 *  History:
 *    New for V18.0
 *
 ****************************************************************************/
extern UFUNEXPORT int UF_DRAW_ask_displayed_objects(
    const tag_t view,            /* <I> Tag of the view */
    int *num_objects,            /* <O> Number of objects */
    tag_p_t *objects             /* <OF,len:num_objects> num_objects
                                         An array of objects and must be freed
                                         by UF_free() */
);

/****************************************************************************
 *
 *  UF_DRAW_ask_solid_of_section
 *
 *  DESCRIPTION -
 *      Given the tag of a section solid, output the tag of its solid.
 *
 *
 *  PARAMETERS -
 *      sxsolid_tag           <I>     Tag of section
 *      solid_tag             <O>     Tag of solid
 *  Returns -
 *     0 = OK
 *     if not 0 = error code
 *
 ****************************************************************************/

extern UFUNEXPORT int UF_DRAW_ask_solid_of_section(
    tag_t                            sxsolid_tag, /*<I> Tag of section */
    tag_t                            *solid_tag /*<O> Tag of solid */);

/****************************************************************************
 *
 *  This routine gets members and count of members of a drafting curve group.
 *
 *  Return:
 *      0 = OK
 *      if not 0 = Failing error code
 *                 Use UF_get_fail_message to obtain the message
 *                 string associated with the error code.
 *
 *  See also:
 *
 *  Environment: Internal and External
 *
 *  History:
 *    New for V19.0
 *
 ****************************************************************************/
extern  UFUNEXPORT int UF_DRAW_ask_curve_group_members(
    tag_t curve_group,  /* <I> Tag of drafting curve group */
    tag_t** curves,     /* <OF,len:curve_count> curve_count
                           Tag array of all curves in the drafting curve group and must be freed
                           by UF_free()*/
    int * curve_count   /* <O> Number of curves in the drafting curve group*/
);

/****************************************************************************
 *
 *  UF_DRAW_ask_border_color
 *
 *  DESCRIPTION -
 *      Output the color of view borders
 *
 *
 *  PARAMETERS -
 *      border_color             <O>     Color of view borders
 *  Returns -
 *     0 = OK
 *     if not 0 = error code
 *
 ****************************************************************************/
extern UFUNEXPORT int UF_DRAW_ask_border_color(int *border_color /* <O> */ );

/****************************************************************************
 *
 *  UF_DRAW_set_border_color
 *
 *  DESCRIPTION -
 *      Set the color of view borders
 *
 *
 *  PARAMETERS -
 *      border_color             <I>     Color of view borders
 *  Returns -
 *     0 = OK
 *     if not 0 = error code
 *
 ****************************************************************************/
extern UFUNEXPORT int UF_DRAW_set_border_color(int border_color /* <I> */);

/****************************************************************************
 *
 *  UF_DRAW_ask_border_display
 *
 *  DESCRIPTION -
 *      Ask the view border display status
 *
 *
 *  PARAMETERS -
 *      border_display             <O>  True if borders are displayed
 *  Returns -
 *     0 = OK
 *     if not 0 = error code
 *
 ****************************************************************************/
extern UFUNEXPORT int UF_DRAW_ask_border_display(logical *border_display /* <O> */);

/****************************************************************************
 *
 *  UF_DRAW_set_border_display
 *
 *  DESCRIPTION -
 *      Set the view border display status
 *
 *
 *  PARAMETERS -
 *      border_display             <I>  True, if borders are to be displayed
 *  Returns -
 *     0 = OK
 *     if not 0 = error code
 *
 ****************************************************************************/
extern UFUNEXPORT int UF_DRAW_set_border_display(logical border_display /* <I> */);


/****************************************************************************
 *
 *  UF_DRAW_retrieve_drawing_cgm
 *
 *  DESCRIPTION -
 *      Function will retrieve drawing cgm data stored in NX QAF.
 *      The drawing cgm data will be stored in TMP_DIR, the file name will be
 *      TMP_DIR/file_name-sheet_name.cgm
 *
 *  Returns -
 *     0 = OK
 *     if not 0 = error code
 *
 ****************************************************************************/
extern UFUNEXPORT int UF_DRAW_retrieve_drawing_cgm(
    char *file_name,                         /* <I> file name used to query cgm data */
    char ***out_file_names,                  /* <OF,len:num_sheets> an array of output name files */
    int *num_sheets                          /* <O> number of output file names */
);

/******************************************************************************
 *
 *  UF_DRAW_ask_drafting_curve_parents
 *
 *  DESCRIPTION -
 *      This routine returns the parents and count of parents for input drafting curve.
 *
 *  Returns -
 *     0 = OK
 *     if not 0 = error code
 *
 *  History:
 *    Initially released in NX 9.0.2-MP1
 *
 ******************************************************************************/
extern UFUNEXPORT int UF_DRAW_ask_drafting_curve_parents(
        tag_t input_curve_tag ,             /* <I> Tag of the input drafting curve whose parents are to queried */
        int *parents_count ,                /* <O> Number of parents*/
        tag_t **parents                     /* <OF,len:parents_count> Array of parents for input drafting curve and must be freed
                                            by UF_free() */
);

/******************************************************************************
 *
 *  UF_DRAW_ask_drafting_curve_type
 *
 *  DESCRIPTION -
 *      This routine returns the type of input drafting curve.
 *
 *  Returns -
 *     0 = OK
 *     if not 0 = error code
 *
 *  History:
 *    Initially released in NX 9.0.2-MP1
 *
 ******************************************************************************/
extern UFUNEXPORT int UF_DRAW_ask_drafting_curve_type(
        tag_t input_curve_tag ,                                  /* <I> Tag of the input drafting curve whose parents are to queried */
        UF_DRAW_drafting_curve_type_t* curve_type                /* <O> drafting curve type*/
);

/*END */

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif /* UF_DRAW_H_INCLUDED */
