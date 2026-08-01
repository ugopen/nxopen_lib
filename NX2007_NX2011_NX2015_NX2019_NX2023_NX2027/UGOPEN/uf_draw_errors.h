/****************************************************************************

             Copyright (c) 1998-1999,2000,2001 Unigraphics Solutions, Inc.
                       Unpublished - All Rights Reserved                       

****************************************************************************




File description:

   This file contains all the error codes raised by the UF_DRAW module.

****************************************************************************/

#ifndef UF_DRAW_ERRORS_H_INCLUDED
#define UF_DRAW_ERRORS_H_INCLUDED

/***************************************************************************


 */

#define ERROR_UF_DRAW_base     1405000

#ifdef __cplusplus
extern "C" {
#endif

#define UF_DRAW_ERROR_BASE                        ERROR_UF_DRAW_base
#define UF_DRAW_ERROR_RANGE                       5000
#define UF_DRAW_NO_ERRORS                         0

#define IS_UF_DRAW_ERROR(error)   ((error >=UF_DRAW_ERROR_BASE)       && (error <=(UF_DRAW_ERROR_BASE + 999)))
#define IS_UF_DRAW_WARNING(error) ((error >=UF_DRAW_ERROR_BASE + 900) && (error <=(UF_DRAW_ERROR_BASE + 999)))

#define UF_DRAW_unrecoverable_error              (UF_DRAW_ERROR_BASE)
#define UF_DRAW_invalid_parameter                (UF_DRAW_ERROR_BASE +  1)
#define UF_DRAW_sxline_not_correct_type          (UF_DRAW_ERROR_BASE +  2)
#define UF_DRAW_tag_not_sxline                   (UF_DRAW_ERROR_BASE +  3)
#define UF_DRAW_invalid_sxline_leg               (UF_DRAW_ERROR_BASE +  4)
#define UF_DRAW_invalid_sxseg_type               (UF_DRAW_ERROR_BASE +  5)
#define UF_DRAW_no_add_to_half_sxline            (UF_DRAW_ERROR_BASE +  6)
#define UF_DRAW_null_object                      (UF_DRAW_ERROR_BASE +  7)
#define UF_DRAW_invalid_object_view              (UF_DRAW_ERROR_BASE +  8)
#define UF_DRAW_invalid_object_assoc             (UF_DRAW_ERROR_BASE +  9)
#define UF_DRAW_invalid_assoc_modifier           (UF_DRAW_ERROR_BASE + 10)
#define UF_DRAW_invalid_dwg_pos                  (UF_DRAW_ERROR_BASE + 11) 
#define UF_DRAW_object_is_view_dep               (UF_DRAW_ERROR_BASE + 12)
#define UF_DRAW_no_delete_half_sxline            (UF_DRAW_ERROR_BASE + 13)
#define UF_DRAW_tag_not_sxseg                    (UF_DRAW_ERROR_BASE + 14)
#define UF_DRAW_no_intersection                  (UF_DRAW_ERROR_BASE + 15)
#define UF_DRAW_no_arc_center                    (UF_DRAW_ERROR_BASE + 16)
#define UF_DRAW_no_end_point                     (UF_DRAW_ERROR_BASE + 17)
#define UF_DRAW_cannot_assoc_object              (UF_DRAW_ERROR_BASE + 18)
#define UF_DRAW_tag_not_sxview                   (UF_DRAW_ERROR_BASE + 19)
#define UF_DRAW_bad_num_sxsegs                   (UF_DRAW_ERROR_BASE + 20)
#define UF_DRAW_bad_num_leg1_sxsegs              (UF_DRAW_ERROR_BASE + 21)
#define UF_DRAW_tag_not_drawing                  (UF_DRAW_ERROR_BASE + 22)
#define UF_DRAW_bad_sxview_scale                 (UF_DRAW_ERROR_BASE + 23)
#define UF_DRAW_invalid_step_dir                 (UF_DRAW_ERROR_BASE + 24)
#define UF_DRAW_invalid_arrow_dir                (UF_DRAW_ERROR_BASE + 25)
#define UF_DRAW_tag_not_view                     (UF_DRAW_ERROR_BASE + 26)
#define UF_DRAW_bad_arrow_size                   (UF_DRAW_ERROR_BASE + 27)
#define UF_DRAW_bad_arrow_len                    (UF_DRAW_ERROR_BASE + 28)
#define UF_DRAW_bad_arrow_incl_angle             (UF_DRAW_ERROR_BASE + 29)
#define UF_DRAW_bad_arrow_dist_past_part         (UF_DRAW_ERROR_BASE + 30)
#define UF_DRAW_bad_arrow_stub_len               (UF_DRAW_ERROR_BASE + 31)
#define UF_DRAW_bad_arrow_head_type              (UF_DRAW_ERROR_BASE + 32)
#define UF_DRAW_bad_arrow_head_control           (UF_DRAW_ERROR_BASE + 33)
#define UF_DRAW_bad_sxline_display               (UF_DRAW_ERROR_BASE + 34)
#define UF_DRAW_not_two_cuts_defined             (UF_DRAW_ERROR_BASE + 35)
#define UF_DRAW_no_cut_in_leg1                   (UF_DRAW_ERROR_BASE + 36)
#define UF_DRAW_no_cut_in_leg2                   (UF_DRAW_ERROR_BASE + 37)
#define UF_DRAW_dwg_not_current                  (UF_DRAW_ERROR_BASE + 38)
#define UF_DRAW_no_more_views_to_dwg             (UF_DRAW_ERROR_BASE + 39)
#define UF_DRAW_pview_not_dwg_view               (UF_DRAW_ERROR_BASE + 40)
#define UF_DRAW_pview_not_detail_view            (UF_DRAW_ERROR_BASE + 41)
#define UF_DRAW_pview_not_sxview                 (UF_DRAW_ERROR_BASE + 42)
#define UF_DRAW_no_dwg_of_dwg_view               (UF_DRAW_ERROR_BASE + 43)
#define UF_DRAW_bad_num_step_sxsegs              (UF_DRAW_ERROR_BASE + 44)
#define UF_DRAW_tag_is_null                      (UF_DRAW_ERROR_BASE + 45)
#define UF_DRAW_invalid_parameter_value          (UF_DRAW_ERROR_BASE + 46)
#define UF_DRAW_invalid_view                     (UF_DRAW_ERROR_BASE + 47)
#define UF_DRAW_no_current_drawing               (UF_DRAW_ERROR_BASE + 48)
#define UF_DRAW_tag_not_sxsolid                  (UF_DRAW_ERROR_BASE + 49)
#define UF_DRAW_tag_not_sxedge                   (UF_DRAW_ERROR_BASE + 50)
#define UF_DRAW_vb_curve_disconnected            (UF_DRAW_ERROR_BASE + 51)
#define UF_DRAW_vb_curve_crosses_curve           (UF_DRAW_ERROR_BASE + 52)
#define UF_DRAW_vb_curve_self_intersects         (UF_DRAW_ERROR_BASE + 53)
#define UF_DRAW_vb_non_manifold_curve            (UF_DRAW_ERROR_BASE + 54)
#define UF_DRAW_vb_no_curve                      (UF_DRAW_ERROR_BASE + 55)
#define UF_DRAW_invalid_boundary_curves          (UF_DRAW_ERROR_BASE + 56)
#define UF_DRAW_view_is_not_member_view          (UF_DRAW_ERROR_BASE + 57)
#define UF_DRAW_view_is_expanded                 (UF_DRAW_ERROR_BASE + 58)
#define UF_DRAW_view_not_on_current_drawing      (UF_DRAW_ERROR_BASE + 59)     
#define UF_DRAW_view_is_not_active               (UF_DRAW_ERROR_BASE + 60)     
#define UF_DRAW_point_not_on_drawing             (UF_DRAW_ERROR_BASE + 61)     
#define UF_DRAW_invalid_view_type                (UF_DRAW_ERROR_BASE + 62)
#define UF_DRAW_invalid_hinge_dir                (UF_DRAW_ERROR_BASE + 63)
#define UF_DRAW_object_is_not_linear             (UF_DRAW_ERROR_BASE + 64)
#define UF_DRAW_vw_scale_is_not_parametric       (UF_DRAW_ERROR_BASE + 65)
#define UF_DRAW_part_not_loaded                  (UF_DRAW_ERROR_BASE + 66)
#define UF_DRAW_parameter_type_wrong             (UF_DRAW_ERROR_BASE + 67)
#define UF_DRAW_unable_to_simplify_curve         (UF_DRAW_ERROR_BASE + 68)
#define UF_DRAW_no_view_created                  (UF_DRAW_ERROR_BASE + 69)
#define UF_DRAW_invalid_view_bound_type          (UF_DRAW_ERROR_BASE + 70)
#define UF_DRAW_invalid_anchor_point             (UF_DRAW_ERROR_BASE + 71)
#define UF_DRAW_view_not_on_drawing              (UF_DRAW_ERROR_BASE + 72)
#define UF_DRAW_point_not_visible                (UF_DRAW_ERROR_BASE + 73)
#define UF_DRAW_point_not_smart                  (UF_DRAW_ERROR_BASE + 74)
#define UF_DRAW_curve_is_associative             (UF_DRAW_ERROR_BASE + 75)
#define UF_DRAW_invalid_spline                   (UF_DRAW_ERROR_BASE + 76)
#define UF_DRAW_view_indep_object                (UF_DRAW_ERROR_BASE + 77)
#define UF_DRAW_unable_to_edit_bnd_point         (UF_DRAW_ERROR_BASE + 78)
#define UF_DRAW_boundary_not_smart               (UF_DRAW_ERROR_BASE + 79)
#define UF_DRAW_invalid_note                     (UF_DRAW_ERROR_BASE + 80)
#define UF_DRAW_invalid_tabnot_cell              (UF_DRAW_ERROR_BASE + 81)
#define UF_DRAW_no_more_tabnot_fonts             (UF_DRAW_ERROR_BASE + 82)
#define UF_DRAW_no_more_tabnot_sizes             (UF_DRAW_ERROR_BASE + 83)
#define UF_DRAW_invalid_drawing_name             (UF_DRAW_ERROR_BASE + 84)
#define UF_DRAW_design_in_context                (UF_DRAW_ERROR_BASE + 85)
#define UF_DRAW_unable_to_delete_view            (UF_DRAW_ERROR_BASE + 86)
#define UF_DRAW_unable_to_set_ref_pt             (UF_DRAW_ERROR_BASE + 87)
#define UF_DRAW_view_pos_not_on_drawing          (UF_DRAW_ERROR_BASE + 88)
#define UF_DRAW_unable_to_obtain_display_data    (UF_DRAW_ERROR_BASE + 89)
#define UF_DRAW_no_drawing_view                  (UF_DRAW_ERROR_BASE + 90)
#define UF_DRAW_drawing_already_exists           (UF_DRAW_ERROR_BASE + 91)
#define UF_DRAW_view_already_exists              (UF_DRAW_ERROR_BASE + 92)
#define UF_DRAW_dwg_is_displayed                 (UF_DRAW_ERROR_BASE + 93)
#define UF_DRAW_view_cannot_be_made_ref          (UF_DRAW_ERROR_BASE + 94)
#define UF_DRAW_invalid_units_value              (UF_DRAW_ERROR_BASE + 95)
#define UF_DRAW_invalid_size_code_value          (UF_DRAW_ERROR_BASE + 96)
#define UF_DRAW_invalid_drawing_size_values      (UF_DRAW_ERROR_BASE + 97)
#define UF_DRAW_invalid_plot_scale               (UF_DRAW_ERROR_BASE + 98)
#define UF_DRAW_invalid_number_of_copies         (UF_DRAW_ERROR_BASE + 99)
#define UF_DRAW_invalid_pen_option               (UF_DRAW_ERROR_BASE + 100)
#define UF_DRAW_invalid_pen_number               (UF_DRAW_ERROR_BASE + 101)
#define UF_DRAW_tag_not_view_label               (UF_DRAW_ERROR_BASE + 102)
#define UF_DRAW_unable_to_rotate_view            (UF_DRAW_ERROR_BASE + 103)
#define UF_DRAW_view_is_facet_view               (UF_DRAW_ERROR_BASE + 104)
#define UF_DRAW_sketch_object                    (UF_DRAW_ERROR_BASE + 105)

/* errors 900 - 999 are reserved for warnings */
#define UF_DRAW_WARNING                          (UF_DRAW_ERROR_BASE + 900)
#define UF_DRAW_associative_views                (UF_DRAW_WARNING + 0)
#define UF_DRAW_parent_view_out_of_date          (UF_DRAW_WARNING + 1)

#ifdef __cplusplus
}
#endif

#endif /* UF_DRAW_ERRORS_H_INCLUDED */
