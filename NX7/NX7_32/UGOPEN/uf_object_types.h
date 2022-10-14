/****************************************************************************
             Copyright (c) 1998-2007 UGS Corporation
                Unpublished - All Rights Reserved




File Description:

Define names of all NX object types and subtypes.



*****************************************************************************/

#ifndef UF_OBJECT_TYPES_H_INCLUDED
#define UF_OBJECT_TYPES_H_INCLUDED


/***************************************************************************

  ***************************************************************************/

#ifdef __cplusplus
extern "C" {
#endif

#define UF_dummy_type                             1      /* For internal use only */

#define UF_point_type                             2
#define    UF_point_subtype                            0
#define    UF_old_point_1_subtype                      1 /* Obsolete in v10 */
#define    UF_old_point_2_subtype                      2 /* Obsolete in v10 */

#define UF_line_type                              3
#define    UF_line_normal_subtype                      0
#define    UF_line_old_subtype                         1 /* Obsolete in v10 */
#define    UF_sketch_ref_line_subtype                101 /* Obsolete in V17.0. */

#define UF_solid_collection_type                  4      /* Obsolete in V10 */

#define UF_circle_type  /* Also called "arc" */   5
#define    UF_circle_open_subtype                      0 /* Not Used - To determine whether a circle is open or closed please use UF_MODL_ask_curve_periodicity */
#define    UF_circle_closed_subtype                    1 /* Not Used - To determine whether a circle is open or closed please use UF_MODL_ask_curve_periodicity */
#define    UF_sketch_ref_circle_subtype              101 /* Obsolete in V17.0. */

#define UF_conic_type                             6
#define    UF_conic_ellipse_subtype                    2
#define    UF_conic_parabola_subtype                   3
#define    UF_conic_hyperbola_subtype                  4

#define UF_spcurve_type                           7        /* Obsolete in V10 */
#define    UF_spcurve_open_subtype                     1   /* Obsolete in V10 */
#define    UF_spcurve_closed_subtype                   2   /* Obsolete in V10 */
#define    UF_spcurve_periodic_subtype                 3   /* Obsolete in V10 */

#define UF_old_spline_type                        8        /* Obsolete in V10 */
#define    UF_spline_open_subtype                      1   /* Obsolete in V10 */
#define    UF_spline_closed_subtype                    2   /* Obsolete in V10 */

#define UF_spline_type                            9        /*  Renamed in V10 */
#define    UF_spline_subtype                           0
#define    UF_b_curve_bezier_subtype                   0   /* There is no difference
                                                              between subtype 0 and
                                                              subtype 1 */
#define    UF_b_curve_b_spline_subtype                 1   /* There is no difference
                                                              between subtype 0 and
                                                              subtype 1 */
#define    UF_sketch_ref_spline_subtype              101   /* Obsolete in V17.0 */

#define UF_pattern_type                          10
#define    UF_pattern_subtype                          0
#define    UF_pattern_point_subtype                    1

#define UF_part_attribute_type                   11
#define    UF_part_attribute_subtype                   0
#define    UF_part_attribute_cache_subtype             1

#define UF_layer_category_type                   12

#define UF_kanji_type                            13

#define UF_boundary_type                         14

#define UF_group_type                            15

#define UF_cylinder_type                         16        /* Obsolete in V10 */
#define    UF_surface_normal_parallel_subtype          0
#define    UF_surface_normal_flipped_subtype          10

#define UF_cone_type                             17        /* Obsolete in V10 */
#define    UF_surface_normal_parallel_subtype          0
#define    UF_surface_normal_flipped_subtype          10

#define UF_sphere_type                           18        /* Obsolete in V10 */
#define    UF_surface_normal_parallel_subtype          0
#define    UF_surface_normal_flipped_subtype          10

#define UF_surface_of_revolution_type            19        /* Obsolete in V10 */
#define    UF_surface_normal_parallel_u_subtype        0
#define    UF_surface_normal_parallel_v_subtype        1
#define    UF_surface_normal_flipped_u_subtype        10
#define    UF_surface_normal_flipped_v_subtype        11

#define UF_tabulated_cylinder_type               20        /* Obsolete in V10 */
#define    UF_surface_normal_parallel_subtype          0
#define    UF_surface_normal_flipped_subtype          10

#define UF_ruled_surface_type                    21        /* Obsolete in V10 */
#define    UF_surface_normal_parallel_subtype          0
#define    UF_surface_normal_flipped_subtype          10

#define UF_bounded_plane_type                    22        /* Obsolete in V10 */
#define    UF_surface_normal_parallel_subtype          0
#define    UF_surface_normal_flipped_subtype          10

#define UF_blended_face_type                     23        /* Obsolete in V10 */
#define    UF_surface_normal_parallel_subtype          0
#define    UF_surface_normal_flipped_subtype          10

#define UF_sculptured_surface_type               24        /* Obsolete in V10 */
#define    UF_surface_normal_parallel_subtype          0
#define    UF_surface_normal_flipped_subtype          10

#define UF_drafting_entity_type                  25
#define    UF_draft_note_subtype                       1
#define    UF_draft_label_subtype                      2
#define    UF_draft_id_symbol_subtype                  3
#define    UF_draft_fpt_subtype                        4
#define    UF_draft_cntrline_subtype                   5
#define    UF_draft_crosshatch_subtype                 6
#define    UF_draft_assorted_parts_subtype             7
#define    UF_draft_intersection_subtype               8
#define    UF_draft_target_point_subtype               9
#define    UF_draft_user_defined_subtype              10
#define    UF_draft_area_fill_subtype                 11
#define    UF_draft_solid_fill_subtype                12
#define    UF_draft_linear_cntrln_subtype             13
#define    UF_draft_full_cir_cntrln_subtype           14
#define    UF_draft_part_cir_cntrln_subtype           15
#define    UF_draft_full_blt_circle_subtype           16
#define    UF_draft_part_blt_circle_subtype           17
#define    UF_draft_offset_cntrpt_subtype             18
#define    UF_draft_cyl_cntrln_subtype                19
#define    UF_draft_sym_cntrln_subtype                20
#define    UF_draft_block_cntrln_subtype              21
#define    UF_draft_label_on_parent_subtype           22
#define    UF_draft_point_subtype                     37
#define    UF_draft_facet_subtype                     41

#define UF_dimension_type                        26
#define    UF_dim_horizontal_subtype                   1
#define    UF_dim_vertical_subtype                     2
#define    UF_dim_parallel_subtype                     3
#define    UF_dim_cylindrical_subtype                  4
#define    UF_dim_perpendicular_subtype                5
#define    UF_dim_angular_minor_subtype                6
#define    UF_dim_angular_major_subtype                7
#define    UF_dim_arc_length_subtype                   8
#define    UF_dim_radius_subtype                       9
#define    UF_dim_diameter_subtype                    10
#define    UF_dim_hole_subtype                        11
#define    UF_dim_conc_circle_subtype                 12
#define    UF_dim_ordinate_horiz_subtype              13
#define    UF_dim_ordinate_vert_subtype               14
#define    UF_dim_assorted_parts_subtype              15
#define    UF_dim_folded_radius_subtype               16
#define    UF_dim_chain_dimensions_subtype            17
#define    UF_dim_ordinate_origin_subtype             18  /*CATa*/
#define    UF_dim_perimeter_subtype                   19
#define    UF_dim_chamfer_subtype                     20

#define UF_font_table_type                       27

#define UF_color_table_type                      28

#define UF_margin_type                           29

#define UF_gfem_load_type                        31  /* Obsolete in V16 */
#define    UF_gfem_load_force_subtype                  1
#define    UF_gfem_load_moment_subtype                 2
#define    UF_gfem_load_displacement_subtype           3
#define    UF_gfem_load_rotation_subtype               4
#define    UF_gfem_load_nodal_temp_subtype             5
#define    UF_gfem_load_edge_pressure_subtype          6
#define    UF_gfem_load_face_pressure_subtype          7

#define UF_caegeom_type                          31
#define    UF_caegeom_region_subtype                   8
#define    UF_caegeom_face_subtype                     9
#define    UF_caegeom_edge_subtype                     10
#define    UF_caegeom_vertex_subtype                   11
#define    UF_caegeom_body_subtype                     12
#define    UF_caegeom_volume_subtype                   13

#define UF_gfem_node_type                        32  /* Obsolete in V16 */
#define    UF_gfem_node_subtype                        0

#define UF_sfem_nxbc_type                        32  /* introduced in NX4 */
#define    UF_sfem_nxload_subtype                 1
#define    UF_sfem_nxconstraint_subtype           2
#define    UF_sfem_nxssso_subtype                 3

#define UF_gfem_element_type                     33  /* Obsolete in V16 */
#define    UF_gfem_element_form_1_subtype              1
#define    UF_gfem_element_form_2_subtype              2
#define    UF_gfem_element_form_3_subtype              3
#define    UF_gfem_element_form_4_subtype              4
#define    UF_gfem_element_form_5_subtype              5
#define    UF_gfem_element_form_6_subtype              6
#define    UF_gfem_element_form_7_subtype              7
#define    UF_gfem_element_form_8_subtype              8
#define    UF_gfem_element_form_9_subtype              9
#define    UF_gfem_element_form_10_subtype            10

#define UF_sfem_connection_recipe_type           33  /* introduced in NX6 */
#define    UF_sfem_connection_recipe_point_point_subtype        1
#define    UF_sfem_connection_recipe_point_edge_subtype         2
#define    UF_sfem_connection_recipe_point_face_subtype         3
#define    UF_sfem_connection_recipe_edge_edge_subtype          4
#define    UF_sfem_connection_recipe_edge_face_subtype          5
#define    UF_sfem_weld_connection_recipe_subtype               6

#define UF_gfem_ferd_type                        34  /* Obsolete in V16 */
#define    UF_gfem_ferd_subtype                   0

#define UF_meshpoint_type                        34

#define UF_gfem_annotation_type                  35  /* Obsolete in V16 -- Reused */
#define    UF_gfem_annotation_subtype                  0

#define UF_caemisc_type                          35
#define    UF_caemisc_edge_density_subtype             1
#define    UF_caemisc_face_density_subtype             2
#define    UF_caemisc_mmc_subtype                      3

#define UF_gfem_control_node_list_type           36  /* Obsolete in V16 */
#define    UF_gfem_control_node_list_subtype           0

#define UF_gfem_material_type                    37
#define    UF_gfem_material_subtype                    0

#define UF_instance_type                         38      /* Obsolete in V4 */

#define UF_connection_type                       39      /* Obsolete in V4 */
#define    UF_connection_normal_subtype                0
#define    UF_connection_offpage_subtype               1
#define    UF_connection_special_subtype               2

#define UF_prefix_type                           40      /* Obsolete in V4, re-use it by UF_view_set_type */
#define UF_view_set_type                         40
#define    UF_view_set_subtype                         0

#define UF_tool_type                             41      /* Obsolete */

#define UF_sub_entity_for_dim_type               42
#define    UF_dim_sub_line_subtype                     1
#define    UF_dim_sub_arc_subtype                      2
#define    UF_dim_sub_text_subtype                     3

#define UF_b_surface_type                        43
#define    UF_b_surface_bezier_subtype                 0   /* Obsolete in V10 */
#define    UF_b_surface_b_spline_subtype               1   /* Obsolete in V10 */

#define UF_validation_type                       44

#define UF_coordinate_system_type                45
#define    UF_csys_normal_subtype                      0
#define    UF_csys_wcs_subtype                         1
#define    UF_csys_cylindrical_subtype                 2
#define    UF_csys_spherical_subtype                   3

#define UF_plane_type                            46

#define UF_bounded_plane_loop_type               47      /* Obsolete in V7 */
#define    UF_bounded_plane_loop_subtype               0

#define UF_report_entity_type                    48      /* Obsolete in NX2 */
#define    UF_report_parts_list_subtype                1

#define UF_report_entry_entity_type              49      /* Obsolete in NX2 */
#define    UF_report_parts_list_entry_subtype          1

#define UF_nesting_type                          50

#define UF_tool_display_type                     51
#define UF_tool_display_subtype                        0
#define UF_mcs_display_subtype                         1

#define UF_skeleton_ent_type                     52
#define    UF_skeleton_grid_subtype                    1 /* obs. in NX2 */
#define    UF_skeleton_wind_bords_subtype              2
#define    UF_skeleton_wcs_display_subtype             3
#define    UF_skeleton_modeling_grid_subtype           4 /* new in NX2 */
#define    UF_skeleton_drawing_grid_subtype            5 /* new in NX2 */
#define    UF_skeleton_sketcher_grid_subtype           6 /* new in NX2 */
#define    UF_skeleton_shed_grid_subtype               7 /* new in NX6 */
#define    UF_skeleton_plane_grid_subtype              8 /* new in NX6 */
#define    UF_skeleton_datum_plane_grid_subtype        9 /* new in NX6 */

#define UF_parameter_type                        53      /* Global Data */
#define    UF_parm_mach_global_subtype                 1 /* Obsolete in V5 */
#define    UF_parm_lathe_global_subtype                2 /* Obsolete in V5 */
#define    UF_parm_lathe_rough_subtype                 3 /* Obsolete in V5 */
#define    UF_parm_lathe_finish_subtype                4 /* Obsolete in V5 */
#define    UF_parm_lathe_groove_subtype                5 /* Obsolete in V5 */
#define    UF_parm_lathe_thread_subtype                6 /* Obsolete in V5 */
#define    UF_parm_drill_subtype                       7 /* Obsolete in V5 */
#define    UF_parm_mill_global_subtype                 8 /* Obsolete in V5 */
#define    UF_parm_profile_subtype                     9 /* Obsolete in V5 */
#define    UF_parm_follow_pocket_subtype              10 /* Obsolete in V5 */
#define    UF_parm_zig_zag_subtype                    11 /* Obsolete in V5 */
#define    UF_parm_surf_contour_subtype               12 /* Obsolete in V5 */
#define    UF_parm_line_machining_subtype             13 /* Obsolete in V5 */
#define    UF_parm_solid_subtype                      13
#define    UF_parm_rough_to_depth_subtype             14 /* Obsolete in V5 */
#define    UF_parm_solid_color_subtype                14
#define    UF_parm_point_to_point_subtype             15 /* Obsolete in V5 */
#define    UF_parm_dimensions_data_subtype            16
#define    UF_parm_kanji_data_subtype                 17
#define    UF_parm_schematics_data_subtype            18 /* Obsolete in V10 */
#define    UF_parm_menu_table_data_subtype            19
#define    UF_parm_ug_data_subtype                    20
#define    UF_parm_display_data_subtype               21
#define    UF_parm_layer_data_subtype                 22
#define    UF_parm_gfem_femcom                        23  /* Obsolete in V16 */
#define    UF_parm_gfem_poscom                        24  /* Obsolete in V16 */
#define    UF_parm_model_bounds_subtype               25
#define    UF_parm_diagram_subtype                    26  /* Obsolete in NX3 */
#define    UF_parm_sheet_metal_subtype                30
#define    UF_parm_ladder_diagram_subtype             31
#define    UF_parm_calculator_subtype                 32
#define    UF_parm_member_view_subtype                33
#define    UF_parm_sketch_tol_data_subtype            34
#define    UF_parm_hidden_line_subtype                35
#define    UF_parm_font_table_subtype                 36
#define    UF_parm_rapid_proto_subtype                37
#define    UF_parm_drawing_control                    38
#define    UF_parm_section_line_subtype               39
#define    UF_parm_retain_ann_subtype                 40
#define    UF_parm_sfem_subtype                       41 /* OBSOLETE in NX4 */
#define    UF_parm_annotation_subtype                 42
#define    UF_parm_crvtr_disp_subtype                 43
#define    UF_parm_drawings_subtype                   44
#define    UF_parm_modeling_subtype                   45
#define    UF_parm_tabular_note_subtype               46
#define    UF_parm_parts_list_subtype                 47
#define    UF_parm_units_subtype                      48
#define    UF_parm_navigation_data_subtype            49
#define    UF_parm_jack_env_subtype                   50
#define    UF_parm_caemodl_vertex_subtype             51
#define    UF_parm_caemodl_edge_subtype               52
#define    UF_parm_caemodl_face_subtype               53
#define    UF_parm_caemodl_region_subtype             54
#define    UF_parm_caemodl_body_subtype               55
#define    UF_parm_sheet_metal_design_subtype         56
#define    UF_parm_cae_post_main_subtype              57
#define    UF_parm_caeabs_main_subtype                58
#define    UF_parm_wizard_subtype                     59  /* Root object of all Process Studio Wizard persistent data*/
#define    UF_parm_main_fem_subtype                   60  /* Root object of FEM */
#define    UF_parm_main_sim_subtype                   61  /* Root object of SIM */
#define    UF_parm_ship_building_subtype              62
#define    UF_parm_pmi_data_subtype                   63
#define    UF_parm_global_set_subtype                 64
#define    UF_parm_field_main_subtype                 65  /* root object of Fields */
#define    UF_parm_kmc_main_subtype                   66  /* root object of MOTION */
#define    UF_parm_cae_so_manager_subtype             67
#define    UF_parm_aero_sheet_metal_subtype           68
#define    UF_parm_flex_pcb_design_subtype            69
#define    UF_parm_caemodl_volume_subtype             70
#define    UF_parm_section_list_subtype               71
#define    UF_parm_autopopulate_subtype               72
#define    UF_parm_cae_ideal_main_subtype             73  /* Root object of Idealized part  */
#define    UF_parm_main_assy_fem_subtype              74  /* Root object of Assembly FEM */
#define    UF_parm_student_edition_subtype            75
#define    UF_parm_pirate_data_subtype                76
#define    UF_parm_imported_jt_data_subtype           77

#define UF_device_type                           54      /* Obsolete in V15 - Reused In NX6 */
#define UF_dynamic_section_cut_type              54
#define    UF_dynamic_section_cut_subtype_any         -1
#define    UF_dynamic_section_body_cut_subtype        1
#define    UF_dynamic_section_component_cut_subtype   2

#define UF_matrix_type                           55

#define UF_gear_type                             56      /* Obsolete in V10 */

#define UF_gear_mesh_type                        57      /* Obsolete in V10 */

#define UF_gear_train_type                       58      /* Obsolete in V10 */

#define UF_fatigue_type                          59      /* Obsolete in V10 - Reused */
#define UF_camera_type                           59

#define UF_view_type                             60
#define    UF_view_section_subtype                     0
#define    UF_view_instance_subtype                    1
#define    UF_view_imported_subtype                    2
#define    UF_view_base_member_subtype                 3
#define    UF_view_orthographic_subtype                4
#define    UF_view_auxiliary_subtype                   5
#define    UF_view_detail_subtype                      6
#define    UF_view_modeling_subtype                    7
#define    UF_view_user_defined_subtype                8
#define    UF_view_graph_subtype                       9
#define    UF_view_drawing_sheet_subtype              10
#define    UF_view_cae_subtype                        11
#define    UF_view_break_subtype                      12
#define    UF_view_query_result_subtype               13
#define    UF_view_drawing_subtype                    14

#define UF_layout_type                           61
#define    UF_normal_layout_subtype                    0
#define    UF_canned_layout_subtype                    1

#define UF_drawing_type                          62

#define UF_component_type                        63
#define    UF_component_subtype                        0
#define    UF_part_occurrence_subtype                  1
#define    UF_shadow_part_occ_subtype                  2

#define UF_reference_set_type                    64
#define    UF_reference_design_subtype                 0
#define    UF_reference_tool_subtype                   1
#define    UF_reference_parameter_subtype              2
#define    UF_reference_cam_template_subtype           3
#define    UF_reference_cam_task_subtype               4
#define    UF_reference_design_model_subtype           5
#define    UF_reference_design_lightweight_subtype     6

#define UF_offset_surface_type                   65
#define    UF_surface_normal_parallel_subtype          0
#define    UF_surface_normal_flipped_subtype          10

#define UF_foreign_surface_type                  66      /* Customer defined */
#define    UF_surface_normal_parallel_subtype          0
#define    UF_surface_normal_flipped_subtype          10

#define UF_foreign_surface_data_type             67      /* Customer defined */

#define UF_occ_instance_type                     68
#define UF_occ_instance_subtype                        0

#define UF_occ_shadow_part_type                  69
#define    UF_explosion_subtype                        0

#define UF_solid_type                            70
#define    UF_solid_body_subtype                       0
#define    UF_solid_swept_body_subtype                 1 /* Internal use only - not displayable */
#define    UF_solid_face_subtype                       2
#define    UF_solid_edge_subtype                       3
#define    UF_solid_silhouette_subtype                 4 /* Moved to type 201 in V10 */
#define    UF_solid_foreign_surf_subtype               5

#define UF_face_type                             71        /* Obsolete in V10 */
#define    UF_cylinder_subtype                        16   /* Obsolete in V10 */
#define    UF_cone_subtype                            17   /* Obsolete in V10 */
#define    UF_sphere_subtype                          18   /* Obsolete in V10 */
#define    UF_surface_of_revolution_subtype           19   /* Obsolete in V10 */
#define    UF_tabulated_cylinder_subtype              20   /* Obsolete in V10 */
#define    UF_ruled_surface_subtype                   21   /* Obsolete in V10 */
#define    UF_bounded_plane_subtype                   22   /* Obsolete in V10 */
#define    UF_fillet_surface_subtype                  23   /* Obsolete in V10 */
#define    UF_sculptured_surface_subtype              24   /* Obsolete in V10 */
#define    UF_b_surface_subtype                       43   /* Obsolete in V10 */
#define    UF_offset_surface_subtype                  65   /* Obsolete in V10 */
#define    UF_foreign_surface_subtype                 66   /* Obsolete in V10 */

#define UF_edge_type                             72        /* Obsolete in V10 */
#define    UF_edge_0_subtype                           0
#define    UF_edge_3_subtype                           3

#define UF_solid_composite_type                  73        /* Obsolete in V10 */

#define UF_history_type                          74

#define UF_gfem_post_data_type                   75  /* Obsolete in V16 */
#define    UF_gfem_post_data_subtype                   0

#define UF_gfem_post_ferd_type                   76  /* Obsolete in V16 */
#define    UF_gfem_control_ferd_subtype                1  /* Obsolete in V16 */
#define    UF_gfem_element_ferd_subtype                2  /* Obsolete in V16 */
#define    UF_gfem_node_ferd_subtype                   3  /* Obsolete in V16 */

#define UF_gfem_post_display_type                77  /* Obsolete in V16 */
#define    UF_gfem_vctr_display_subtype                1  /* Obsolete in V16 */
#define    UF_gfem_deflected_dsp_subtype               2  /* Obsolete in V16 */
#define    UF_gfem_vctr_deflctd_dsp_subtype            4  /* Obsolete in V16 */

#define UF_gfem_post_group_type                  78  /* Obsolete in V16 */
#define    UF_gfem_post_group_subtype                  0

#define UF_gfem_outline_type                     79  /* Obsolete in V16 */
#define    UF_gfem_outline_subtype                     0

#define UF_gfem_local_csys_type                  80  /* Obsolete in V16 */
#define    UF_gfem_local_csys_rect_subtype             1
#define    UF_gfem_local_csys_cyl_subtype              2
#define    UF_gfem_local_csys_spher_subtype            3

#define UF_gfem_loader_type                      81  /* Obsolete in V16 */
#define    UF_gfem_loader_subtype                      0

#define UF_sketch_tol_equation_type              82
#define    UF_sketch_header_equ_subtype                0
#define    UF_sketch_1_var_equ_subtype                 1
#define    UF_sketch_geo_equ_subtype                   2
#define    UF_sketch_geo2_equ_subtype                  3
#define    UF_sketch_dimension_equ_subtype             4
#define    UF_sketch_regular_equ_subtype               5
#define    UF_sketch_8_equ_subtype                     8
#define    UF_sketch_sym_equ_subtype                   9
#define    UF_sketch_inferred_equ_subtype             10

#define UF_sketch_tol_variable_type              83
#define    UF_sketch_circle_ep_var_subtype             0
#define    UF_sketch_param_pnt_var_subtype             1
#define    UF_sketch_invisible_var_subtype             2
#define    UF_sketch_line_slope_var_subtype            3
#define    UF_sketch_line_angle_var_subtype            3
#define    UF_sketch_arc_radius_var_subtype            4
#define    UF_sketch_arc_angle_var_subtype             4
#define    UF_sketch_bcurve_slope_var_subtype          5
#define    UF_sketch_fixed_circle_ep_var_subtype     100
#define    UF_sketch_fixed_param_pnt_var_subtype     101
#define    UF_sketch_fixed_invisible_var_subtype     102
#define    UF_sketch_fixed_line_slope_var_subtype    103
#define    UF_sketch_fixed_line_angle_var_subtype    103
#define    UF_sketch_fixed_arc_radius_var_subtype    104
#define    UF_sketch_fixed_arc_angle_var_subtype     104
#define    UF_sketch_fixed_bcurve_slope_var_subtype  105

#define UF_sketch_tol_output_reqst_type          84

#define UF_mdm_mechanism_type                    85

#define UF_mdm_joint_type                        86
#define    UF_mdm_revolute_subtype                     3
#define    UF_mdm_revolute_fixed_subtype               4
#define    UF_mdm_slider_subtype                       5
#define    UF_mdm_slider_fixed_subtype                 6
#define    UF_mdm_cylinder_subtype                     7
#define    UF_mdm_cylinder_fixed_subtype               8
#define    UF_mdm_screw_subtype                        9
#define    UF_mdm_screw_fixed_subtype                 10
#define    UF_mdm_universal_subtype                   11
#define    UF_mdm_universal_fixed_subtype             12
#define    UF_mdm_sphere_subtype                      13
#define    UF_mdm_sphere_fixed_subtype                14
#define    UF_mdm_planar_subtype                      15
#define    UF_mdm_planar_fixed_subtype                16
#define    UF_mdm_gear_subtype                        17
#define    UF_mdm_gear_fixed_subtype                  18
#define    UF_mdm_rckpn_subtype                       19
#define    UF_mdm_rckpn_fixed_subtype                 20
#define    UF_mdm_pt_crv_subtype                      21
#define    UF_mdm_pt_crv_fixed_curve_subtype          22
#define    UF_mdm_pt_crv_fixed_point_subtype          23
#define    UF_mdm_crv_crv_subtype                     24
#define    UF_mdm_cable_subtype                       25
#define    UF_mdm_joint_fixed_subtype                 26 /* all fixed joint type*/
/* CV joint subtype , Yi Chen  add,CV = constant velocity*/
#define    UF_mdm_cv_subtype                          27
#define    UF_mdm_cv_fixed_subtype                    28
/* Joint Primitives , Yi Chen  Add */
#define    UF_mdm_jprims_atpoint_subtype              111
#define    UF_mdm_jprims_inline_subtype               112  
#define    UF_mdm_jprims_inplane_subtype              113
#define    UF_mdm_jprims_orientation_subtype          114 
#define    UF_mdm_jprims_parallel_subtype             115
#define    UF_mdm_jprims_perpendicular_subtype        116

#define UF_mdm_link_type                         87

#define UF_mdm_spring_type                       88
#define    UF_mdm_spring_trans_2_pt_subtype            1
#define    UF_mdm_spring_trans_slider_subtype          2
#define    UF_mdm_spring_comp_2_pt_subtype             3
#define    UF_mdm_spring_comp_slider_subtype           4
#define    UF_mdm_spring_rot_rev_subtype               5
#define    UF_mdm_spring_rot_cam_subtype               6
#define    UF_mdm_spring_trans_cam_subtype             7
#define    UF_mdm_spring_trans_ext_links_subtype       8
#define    UF_mdm_spring_trans_ext_slider_subtype      9
#define UF_mdm_motion_vector_type                89

#define UF_mdm_force_type                        90

#define UF_shaft_stress_type                     91      /* Obsolete in V10 */

#define UF_shaft_feature_type                    92      /* Obsolete in V10 */

#define UF_shaft_load_type                       93      /* Obsolete in V10 */

#define UF_shaft_support_type                    94      /* Obsolete in V10 */

#define UF_shaft_section_type                    95      /* Obsolete in V10 */

#define UF_shaft_type                            96      /* Obsolete in V10 */

#define UF_mdm_analysis_pt_type                  97      /* Obsolete in V10 */

#define UF_mdm_marker_type                       97      /* replaces UF_mdm_analysis_pt_type */
#define    UF_mdm_inertia_marker_subtype               0
#define    UF_mdm_user_defined_marker_subtype          1
#define    UF_mdm_cofm_marker_subtype                  2

#define UF_mdm_damper_type                       98
#define    UF_mdm_damper_2_links_subtype               6
#define    UF_mdm_damper_slider_subtype                7
#define    UF_mdm_damper_rot_rev_subtype               8

#define UF_mdm_torque_type                       99
#define    UF_mdm_torque_form_subtype                  2
 
    /* Reusing the UF_gfem_property_set_type. This entity type is obsoleted in v16. It gets destroyed or converted upon loading.
       Using it for UF_mdm_constraint_type. */

#define UF_gfem_property_set_type                30
#define    UF_gfem_property_set_form_1_subtype         1
#define    UF_gfem_property_set_form_3_subtype         3
#define    UF_gfem_property_set_form_7_subtype         7

#define UF_mdm_constraint_type                   30         /* Reused UF_gfem_property_set_type since we no longer support GFEM */
#define UF_mdm_constraint_point_on_surface_subtype        2 /* Using 0 and 1 for pt_crv and crv_crv subtype that we may create in future */

#define UF_machining_operation_type             100
#define    UF_mach_instanced_oper_subtype              1
#define    UF_mach_orphan_oper_subtype                 2
#define    UF_mach_oldopr_subtype                     10       /* Obsolete */
#define    UF_mach_pocket_subtype                    110
#define    UF_mach_surface_contour_subtype           210
#define    UF_mach_vasc_subtype                      211
#define    UF_mach_cavity_milling_subtype            260
#define    UF_mach_face_milling_subtype              261
#define    UF_mach_volumn_milling_subtype            262
#define    UF_mach_zlevel_milling_subtype            263
#define    UF_mach_fb_hole_milling_subtype           264
#define    UF_mach_plunge_milling_subtype            265
#define    UF_mach_vazl_milling_subtype              266
#define    UF_mach_turn_rough_subtype                510
#define    UF_mach_turn_finish_subtype               520
#define    UF_mach_turn_teachmode_subtype            530
#define    UF_mach_turn_thread_subtype               540
#define    UF_mach_turn_cdrill_subtype               550
#define    UF_mach_turn_auxiliary_subtype            560
#define    UF_mach_hole_making_subtype               600
#define    UF_mach_wedm_subtype                      700
#define    UF_mach_mill_ud_subtype                   800
#define    UF_mach_gmc_subtype                       900 
#define    UF_mach_probing_subtype                  1000 
#define    UF_mach_mill_mc_subtype                  1100
#define    UF_mach_lathe_mc_subtype                 1200
#define    UF_mach_wedm_mc_subtype                  1300
#define    UF_mach_lathe_ud_subtype                 1400
#define    UF_mach_wedm_ud_subtype                  1500
#define    UF_mach_mass_edit_subtype                1600
#define    UF_insp_tolerance_subtype                1800
#define    UF_insp_path_subtype                     1900
#define    UF_insp_output_subtype                   2000
#define    UF_insp_misc_subtype                     2100
#define    UF_insp_align_subtype                    2200
#define    UF_insp_sensor_subtype                   2300
#define    UF_insp_construct_subtype                2400
#define    UF_insp_bounding_feature_subtype         2500
#define    UF_insp_feature_subtype                  2600

#define UF_machining_path_type                  101
#define    UF_machining_path_subtype                   0

#define UF_table_column_type                    102

#define UF_machining_ude_map_type               103

#define UF_data_declaration_type                104

#define UF_machining_geometry_grp_type          105
#define    UF_mill_geom_featr_subtype                 10
#define    UF_mill_bnd_featr_subtype                  20
#define    UF_mill_orient_subtype                     30
#define    UF_mill_volume_featr_subtype               35
#define    UF_turn_geom_subtype                       40
#define    UF_turn_bnd_subtype                        50
#define    UF_turn_orient_subtype                     60
#define    UF_turn_featr_subtype                      65
#define    UF_turn_avoidance_subtype                  67
#define    UF_mach_wedm_external_group_subtype        70
#define    UF_mach_wedm_internal_group_subtype        80
#define    UF_mach_wedm_open_group_subtype            90
#define    UF_mach_wedm_nocore_group_subtype         100
#define    UF_mach_wedm_feature_group_subtype        110
#define    UF_wedm_orient_subtype                    120
#define    UF_drill_geom_featr_subtype               130
#define    UF_ncfeatr_udf_subtype                    140
#define    UF_ncfeatr_uda_subtype                    150
#define    UF_fbm_geom_subtype                       160
#define    UF_mill_text_featr_subtype                170
#define    UF_blade_featr_subtype                    180

#define UF_machining_mach_tool_grp_type         106
#define    UF_machining_mach_subtype                   0
#define    UF_machining_mach_turret_subtype            1
#define    UF_machining_mach_pocket_subtype            2
#define    UF_machining_mach_kim_subtype               3
#define    UF_machining_mach_kim_comp_subtype          4
#define    UF_machining_mach_kim_degof_subtype         5
#define    UF_machining_mach_kim_junction_subtype      6
#define    UF_machining_mach_kim_valuator_subtype      7
#define    UF_machining_mach_sim_kim_pocket_subtype    8
#define    UF_machining_mach_sim_kim_tool_subtype      9
#define    UF_machining_mach_kim_main_subtype         10
#define    UF_machining_mach_kim_display_subtype      11
#define    UF_machining_mach_kim_collision_subtype    12
#define    UF_machining_mach_sim_kim_main_subtype     13
#define    UF_machining_mach_sim_kim_gouge_subtype    14
#define    UF_machining_mach_sim_kim_ipw_subtype      17
           /* machine tool builder object */
#define    UF_machining_mach_mtb_subtype             15
#define    UF_machining_mach_head_subtype            16
#define    UF_machining_mach_dyn_ipw_subtype         100
#define    UF_machining_mach_dyn_ipw_turn_subtype    101
#define    UF_machining_mach_dyn_ipw_mill_subtype    102
#define    UF_machining_mach_ipw_subtype             999

#define UF_machining_parameter_set_type         107
#define    UF_mach_mill_post_cmnds_subtype            11
#define    UF_mach_lathe_post_cmnds_subtype           13
#define    UF_mach_wed_post_cmnds_subtype             17
#define    UF_mach_pocket_subtype                    110
#define    UF_mach_surface_contour_subtype           210
#define    UF_mach_vasc_subtype                      211
#define    UF_mach_gssm_main_op_subtype              220
#define    UF_mach_gssm_sub_op_subtype               221
#define    UF_mach_gssm_grip_subtype                 222
#define    UF_mach_param_line_subtype                230
#define    UF_mach_zig_zag_surf_subtype              240
#define    UF_mach_rough_to_depth_subtype            250
#define    UF_mach_cavity_milling_subtype            260
#define    UF_mach_lathe_rough_subtype               310
#define    UF_mach_lathe_finish_subtype              320
#define    UF_mach_lathe_groove_subtype              330
#define    UF_mach_lathe_thread_subtype              340
#define    UF_mach_drill_subtype                     350
#define    UF_mach_lathe_face_subtype                360
#define    UF_mach_point_to_point_subtype            450
#define    UF_mach_seq_curve_mill_subtype            460
#define    UF_mach_seq_curve_lathe_subtype           461
#define    UF_mach_wedm_subtype                      700
#define    UF_mach_mill_ud_subtype                   800
#define    UF_mach_mill_mc_subtype                  1100
#define    UF_mach_lathe_mc_subtype                 1200
#define    UF_mach_wedm_mc_subtype                  1300
#define    UF_mach_lathe_ud_subtype                 1400
#define    UF_mach_wedm_ud_subtype                  1500
#define    UF_mach_mass_edit_subtype                1600

#define UF_last_operation_pointer_type          108

#define UF_machining_tool_type                  109
#define    UF_mach_tool_subtype                        0
#define    UF_mach_tool_wedm_subtype                   1
#define    UF_mach_tool_assm_subtype                   2

#define UF_machining_global_data_type           110

#define UF_machining_geom_type                  111
#define    UF_mach_geom_planar_mill_subtype            1
#define    UF_mach_geom_surf_mill_subtype              2
#define    UF_mach_geom_lathe_subtype                  3
#define    UF_mach_geom_pnt_to_pnt_subtype             4
#define    UF_mach_geom_seq_curve_subtype              5
#define    UF_mach_geom_seq_surf_subtype               6
#define    UF_mach_geom_face_bnd_subtype               7
#define    UF_mach_geom_camgeom_subtype                9
#define    UF_mach_geom_cut_level_subtype             11
#define    UF_mach_geom_contain_edge_subtype          12
#define    UF_mach_geom_feature_subtype               13
#define    UF_mach_geom_feature_list_subtype          14
#define    UF_mach_geom_text_subtype                  15

#define UF_machining_null_grp_type              112

#define UF_smart_container_type                 113
#define    UF_smart_empty_container_subtype            0
#define    UF_smart_face_container_subtype             1
#define    UF_smart_wireframe_container_subtype        2
#define    UF_smart_body_container_subtype             3
#define    UF_smart_mixed_container_subtype            4
#define    UF_smart_unknown_container_subtype          5

#define UF_machining_boundary_member_type       114
#define    UF_mach_geom_boundary_0_subtype             0
#define    UF_mach_geom_boundary_subtype               5
#define    UF_mach_geom_face_boundary_subtype          7
#define    UF_mach_geom_camgeom_subtype                9

#define UF_machining_master_operation_type      115
#define    UF_mach_wedm_external_trim_subtype          0
#define    UF_mach_wedm_internal_trim_subtype          1
#define    UF_mach_wedm_no_core_subtype                2
#define    UF_mach_wedm_open_profile_subtype           3
#define    UF_mach_wedm_cutoff_subtype                 4
#define    UF_mach_wedm_rough_pass_subtype             5
#define    UF_mach_wedm_backburn_subtype               6
#define    UF_mach_wedm_finish_trim_subtype            7
#define    UF_mach_wedm_ext_finish_trim_subtype        8
#define    UF_mach_wedm_subtype                      700

#define UF_machining_post_command_type          116
#define    UF_machining_mce_startup_subtype            1
#define    UF_machining_mce_endofpath_subtype          2
#define    UF_machining_mce_inpath_subtype             3
#define    UF_machining_mce_wedm_startup_subtype       4
#define    UF_machining_mce_wedm_endofpath_subtype     5
#define    UF_machining_mce_wedm_inpath_subtype        6
#define    UF_machining_mce_mill_mc_subtype            7
#define    UF_machining_mce_lathe_mc_subtype           8
#define    UF_machining_mce_wedm_mc_subtype            9
#define    UF_machining_mce_number_subtype            10

#define UF_machining_suboperation               117
#define    UF_mach_subop_ncm_subtype                  20
#define    UF_mach_subop_ncm_engret_subtype           21
#define    UF_mach_subop_ncm_appdep_subtype           22
#define    UF_mach_subop_ncm_trav_subtype             23
#define    UF_mach_subop_region_subtype               30
#define    UF_mach_subop_blade_subtype                40

#define    UF_mach_manual_move_subtype                100
#define    UF_mach_manual_move_data_subtype           101
#define    UF_insp_move_subtype                       200
#define    UF_insp_move_data_subtype                  201

#define UF_machining_boundary_type              118
#define    UF_mach_geom_boundary_subtype               5
#define    UF_mach_geom_camgeom_subtype                9

#define UF_machining_control_event_type         119
#define    UF_cevent_motion_subtype                  100
#define    UF_cevent_end_of_path_subtype             101
#define    UF_cevent_start_of_path_subtype           102
#define    UF_cevent_start_point_output_subtype      103
#define    UF_cevent_mom_post_event_subtype          104
#define    UF_cevent_3x_linear_subtype               150
#define    UF_cevent_3x_linear_with_feed_subtype     151
#define    UF_cevent_3x_linear_cust_feed_subtype     152
#define    UF_cevent_5x_linear_subtype               153
#define    UF_cevent_5x_linear_with_feed_subtype     154
#define    UF_cevent_5x_linear_cust_feed_subtype     155
#define    UF_cevent_3x_circular_subtype             156
#define    UF_cevent_3x_circular_with_feed_subtype   157
#define    UF_cevent_3x_circular_cust_feed_subtype   158
#define    UF_cevent_5x_circular_subtype             159
#define    UF_cevent_5x_circular_with_feed_subtype   160
#define    UF_cevent_5x_circular_cust_feed_subtype   161
#define    UF_cevent_3x_helical_subtype              162
#define    UF_cevent_3x_helical_with_feed_subtype    163
#define    UF_cevent_3x_helical_cust_feed_subtype    164
#define    UF_cevent_5x_helical_subtype              165
#define    UF_cevent_5x_helical_with_feed_subtype    166
#define    UF_cevent_5x_helical_cust_feed_subtype    167
#define    UF_cevent_3x_nurbs_subtype                168
#define    UF_cevent_3x_nurbs_with_feed_subtype      169
#define    UF_cevent_3x_nurbs_cust_feed_subtype      170
#define    UF_cevent_5x_nurbs_subtype                171
#define    UF_cevent_5x_nurbs_with_feed_subtype      172
#define    UF_cevent_5x_nurbs_cust_feed_subtype      173
#define    UF_cevent_mce_fromPoint_subtype           200
#define    UF_cevent_mce_startPoint_subtype          201
#define    UF_cevent_mce_startEngage_subtype         202
#define    UF_cevent_mce_returnPoint_subtype         203
#define    UF_cevent_mce_gohomePoint_subtype         204
#define    UF_cevent_mce_toolChange_subtype          205
#define    UF_cevent_mce_origin_subtype              206
#define    UF_cevent_mce_seqno_subtype               207
#define    UF_cevent_mce_setModes_subtype            208
#define    UF_cevent_mce_selectHead_subtype          209
#define    UF_cevent_mce_cutcom_subtype              210
#define    UF_cevent_mce_spindleOn_subtype           211
#define    UF_cevent_mce_spindleOff_subtype          212
#define    UF_cevent_mce_coolantOn_subtype           213
#define    UF_cevent_mce_coolantOff_subtype          214
#define    UF_cevent_mce_optStop_subtype             215
#define    UF_cevent_mce_stop_subtype                216
#define    UF_cevent_mce_optSkipOn_subtype           217
#define    UF_cevent_mce_optSkipOff_subtype          218
#define    UF_cevent_mce_dwell_subtype               219
#define    UF_cevent_mce_cycle_subtype               220
#define    UF_cevent_mce_auxfun_subtype              221
#define    UF_cevent_mce_prefun_subtype              222
#define    UF_cevent_mce_clamp_subtype               223
#define    UF_cevent_mce_toolLengthComp_subtype      224
#define    UF_cevent_mce_rotate_subtype              225
#define    UF_cevent_mce_toolPreselect_subtype       226
#define    UF_cevent_mce_userDefined_subtype         227
#define    UF_cevent_mce_pprint_subtype              228
#define    UF_cevent_mce_opMessage_subtype           229
#define    UF_cevent_mce_goto_subtype                230
#define    UF_cevent_mce_threadWire_subtype          231
#define    UF_cevent_mce_cutWire_subtype             232
#define    UF_cevent_mce_flush_subtype               233
#define    UF_cevent_mce_flushTank_subtype           234
#define    UF_cevent_mce_power_subtype               235
#define    UF_cevent_mce_wireGuides_subtype          236
#define    UF_cevent_mce_wireAngle_subtype           237
#define    UF_cevent_mce_fedrat_subtype              238
#define    UF_cevent_mce_wireCutcom_subtype          239
#define    UF_cevent_mce_latheThread_subtype         240
#define    UF_cevent_mce_goDelta_subtype             241
#define    UF_cevent_mce_from_subtype                242
#define    UF_cevent_mce_goHome_subtype              243
#define    UF_cevent_ude_subtype                     244
#define    UF_cevent_ud_path_subtype                 245
#define    UF_cevent_start_of_pass_subtype           246
#define    UF_cevent_end_of_pass_subtype             247
#define    UF_cevent_mce_smoothLeadIn_subtype        248
#define    UF_cevent_mce_smoothLeadOut_subtype       249
#define    UF_cevent_mce_spindleReverse_subtype      250
#define    UF_cevent_mce_trackingPointChange_subtype 251
#define    UF_cevent_mf_message_subtype              400
#define    UF_cevent_mf_close_debug_files_subtype    401
#define    UF_cevent_mf_dump_buffers_subtype         402
#define    UF_cevent_mf_change_status_subtype        403
#define    UF_cevent_mf_last_clsf_event_subtype      404
#define    UF_cevent_mf_start_of_fillet_subtype      405
#define    UF_cevent_mf_output_gohome_subtype        406
#define    UF_cevent_mf_highlight_subtype            407
#define    UF_cevent_mf_fillet_params_subtype        408
#define    UF_cevent_mf_operation_name_subtype       409
#define    UF_cevent_mf_tldata_subtype               410
#define    UF_cevent_mf_msys_subtype                 411
#define    UF_cevent_mf_list_deletion_subtype        413
#define    UF_cevent_mf_local_return_start_subtype   414
#define    UF_cevent_mf_local_return_end_subtype     415
#define    UF_cevent_mf_display_font_subtype         416
#define    UF_cevent_mf_slowdown_params_subtype      417
#define    UF_cevent_mf_cut_level_plane_subtype      418
#define    UF_cevent_mf_counter_value_subtype        419
#define    UF_cevent_mf_gouge_subtype                420
#define    UF_cevent_mf_unpropagable_event_subtype   421
#define    UF_cevent_scud_updown_cut_subtype         600
#define    UF_cevent_set_marker_subtype              601
#define    UF_cevent_manual_pattern_action_subtype   602
#define    UF_cevent_udc_subtype                     603
#define    UF_cevent_udc_off_subtype                 604
#define    UF_mach_sync_event_subtype                700

#define UF_machining_ncm_type                   120
#define    UF_mach_ncm_subtype                        10
#define    UF_mach_ncm_point_subtype                  20
#define    UF_mach_ncm_engret_subtype                 30
#define    UF_mach_ncm_transfer_subtype               40
#define    UF_mach_ncm_clgeom_subtype                 50

#define UF_machining_task_type                  121
#define    UF_mach_order_task_subtype                160
#define    UF_mach_clsf_task_subtype                 161
#define    UF_mach_optim_task_subtype                162

#define UF_machining_setup_type                 122
#define    UF_mach_setup_subtype                       0
#define    UF_insp_setup_subtype                      10

#define UF_machining_feedrate_type              123

#define UF_machining_display_type               124

#define UF_machining_dp_type                    125
#define    UF_mach_dp_none_subtype                      0
#define    UF_mach_dp_point_subtype                    10
#define    UF_mach_dp_curve_subtype                    20
#define    UF_mach_dp_surface_subtype                  30
#define    UF_mach_dp_boundary_subtype                 40
#define    UF_mach_dp_tool_path_subtype                50
#define    UF_mach_dp_radial_curve_subtype             60
#define    UF_mach_dp_spiral_subtype                   70
#define    UF_mach_dp_ud_subtype                       80
#define    UF_mach_dpm_none_subtype                   100
#define    UF_mach_dpm_amill_subtype                  110
#define    UF_mach_dpm_curve_subtype                  120
#define    UF_mach_dpm_surface_subtype                130
#define    UF_mach_dpm_interpolated_tool_path_subtype 135
#define    UF_mach_dpm_boundary_subtype               140
#define    UF_mach_dpm_tool_path_subtype              150
#define    UF_mach_dpm_radial_curve_subtype           160
#define    UF_mach_dpm_spiral_subtype                 170
#define    UF_mach_dpm_ud_subtype                     180
#define    UF_mach_dpm_fcut_subtype                   190
#define    UF_mach_dpm_line_subtype                   191
#define    UF_mach_dpm_arc_subtype                    192
#define    UF_mach_dpm_text_subtype                   193
#define    UF_mach_dpm_motions_subtype                194
#define    UF_mach_dpm_contour_subtype                200
#define    UF_mach_dpm_blade_rough_subtype            300

#define UF_machining_pathindex_type             126

#define UF_machining_tldsp_type                 127

#define UF_machining_mode_type                  128
#define    UF_mach_mode_subtype                        0
#define    UF_mach_mill_mode_subtype                  10
#define    UF_mach_lathe_mode_subtype                 20
#define    UF_mach_drill_mode_subtype                 30
#define    UF_mach_wedm_mode_subtype                  40
#define    UF_mach_turn_mode_subtype                 100

#define UF_machining_mthd_type                  128
#define    UF_mach_mthd_subtype                        0
#define    UF_mach_mill_mthd_subtype                  10
#define    UF_mach_lathe_mthd_subtype                 20
#define    UF_mach_drill_mthd_subtype                 30
#define    UF_mach_wedm_mthd_subtype                  40
#define    UF_mach_turn_mthd_subtype                 100
#define    UF_mach_hole_mthd_subtype                 110
#define    UF_insp_mthd_subtype                      120

#define UF_machining_clip_type                  129

#define UF_render_set_type                      130

#define UF_sketch_tol_csys_type                 131
#define    UF_sketch_tol_csys_rect_subtype             1
#define    UF_sketch_tol_csys_cyl_subtype              2
#define    UF_sketch_tol_csys_spher_subtype            3

#define UF_sketch_tol_feature_type              132        /* Obsolete in V10 */

#define UF_sketch_tol_mating_type               133        /* Obsolete in V10 */

#define UF_sketch_type                          134
#define    UF_v9_sketch_subtype                        0
#define    UF_v13_sketch_subtype                       1
#define    UF_extracted_sketch_subtype                 2

#define UF_ordinate_margin_type                 135
#define    UF_ord_margin_horizontal_subtype           13
#define    UF_ord_margin_vertical_subtype             14

#define UF_phys_material_type                   136

#define UF_ug_libraries_type                    137

#define UF_faceted_model_data_type              138

#define UF_faceted_model_type                   139
#define    UF_faceted_model_normal_subtype             0
#define    UF_faceted_model_cloud_subtype              1
#define    UF_faceted_model_promoted_subtype           2
#define    UF_faceted_model_jt_body_subtype            3
#define    UF_faceted_model_face_subtype               4
#define    UF_faceted_model_edge_subtype               5
#define    UF_faceted_model_map_subtype                6

#define UF_flange_type                          140
#define    UF_flange_0_subtype                         0
#define    UF_flange_1_subtype                         1

#define UF_bend_type                            141
#define    UF_bend_0_subtype                           0
#define    UF_bend_2_subtype                           2

#define UF_flat_pattern_type                    142
#define    UF_flat_pattern_subtype                     0
#define    UF_flat_pattern_user_subtype                1

#define UF_sheet_metal_type                     143

#define UF_table_type                           144
#define    UF_table_smd_subtype                        0
#define    UF_table_fam_subtype                        1

#define UF_mdm_genforce_type                    145
#define    UF_mdm_bush_subtype                         0
#define    UF_mdm_vforce_subtype                       1
#define    UF_mdm_vtorque_subtype                      2
#define    UF_mdm_contact_subtype                      3

#define UF_sfem_composite_type                  146
#define    UF_sfem_composite_body_subtype              0
#define    UF_sfem_composite_face_subtype              2
#define    UF_sfem_composite_edge_subtype              3
#define    UF_sfem_composite_vertex_subtype            4
#define    UF_sfem_composite_subface_subtype           5
#define    UF_sfem_composite_subedge_subtype           6

#define UF_cam_cut_method_type                  147

#define UF_dimension_set_type                   148
#define    UF_dim_chain_subtype                        0
#define    UF_dim_baseline_subtype                     1

#define UF_display_object_type                  149

#define UF_mdm_curve_curve_contact_type         150

#define UF_prefix1_type                         151      /* Obsolete in V10, reused by UF_drafting_supplemental_geometry_type */
#define UF_drafting_supplemental_geometry_type  151
#define    UF_drafting_region_subtype                  0
#define    UF_drafting_direction_subtype               1

#define UF_symbol_master_type                   152      /* Obsolete in V10 */

#define UF_logic_part_master_type               153      /* Obsolete in V10 */

#define UF_draft_callout_type                   154

#define UF_smsp_product_definition_type         155
#define    UF_smsp_product_definition_subtype          0
#define    UF_smsp_product_definition_geom_subtype     1
#define    UF_smsp_group_subtype                       2
#define    UF_smsp_root_subtype                        3
#define    UF_smsp_product_attribute_subtype           4
#define    UF_smsp_product_value_subtype               5
#define    UF_smsp_business_modifier_subtype           6
#define    UF_pmi_associated_objects_group_subtype     7

#define UF_symbol_type                          156      /* Obsolete in V10 */

#define UF_logic_part_type                      157      /* Obsolete in V10 */

#define UF_smart_model_instance_type            158
#define    UF_combined_attribute_instance_subtype      0
#define    UF_user_defined_attribute_instance_subtype  1
#define    UF_smart_model_instance_mark_subtype        2  /* Obsolete in NX5 */

#define UF_datum_reference_frame_type           159
#define    UF_single_subtype                           0
#define    UF_composite_subtype                        1

#define UF_constraint_type                      160      /* Was obsolete in V10 as UF_net_type */
#define    UF_constraint_subtype                       0
#define    UF_component_constraint_subtype             1
#define    UF_displayed_constraint_subtype             2

#define    UF_distance_constraint_subtype              3
#define    UF_angle_constraint_subtype                 4
#define    UF_radius_constraint_subtype                5
#define    UF_parallel_constraint_subtype              6
#define    UF_perpendicular_constraint_subtype         7
#define    UF_coincident_constraint_subtype            8
#define    UF_tangent_constraint_subtype               9
#define    UF_equal_radius_constraint_subtype          10
#define    UF_fixed_constraint_subtype                 11
#define    UF_symmetric_constraint_subtype             12
#define    UF_rigid_constraint_subtype                 13
#define    UF_concentric_constraint_subtype            14
#define    UF_coplanar_constraint_subtype              15
#define    UF_coaxial_constraint_subtype               16
#define    UF_wallthickness_constraint_subtype         17 

#define UF_connection1_type                     161      /* Obsolete in V10 */

#define UF_node_type                            162      /* Obsolete in V10 */

#define UF_report_net_list_type                 163      /* Obsolete in V10 */

#define UF_traceline_type                       164      /* Was obsolete in V10 as component list */
#define UF_traceline_automatic_subtype                 1
#define UF_traceline_curves_subtype                    2

#define UF_tabular_note_type                    165
#define UF_tabular_note_section_subtype                0
#define UF_tabular_note_subtype                        1
#define UF_tabular_note_row_subtype                    2
#define UF_tabular_note_column_subtype                 3
#define UF_parts_list_subtype                         11
#define UF_parts_list_row_subtype                     12
#define UF_parts_list_column_subtype                  13
#define UF_spline_gear_table_subtype                  21
#define UF_spline_gear_row_subtype                    22
#define UF_spline_gear_column_subtype                 23

#define UF_cam_material_type                    166

#define UF_rlist_type                           167
#define    UF_rlist_list_subtype                       1
#define    UF_rlist_format_subtype                     2
#define    UF_rlist_filter_subtype                     3
#define    UF_fmbd_annotation_subtype                  4

#define UF_route_route_type                     168
#define    UF_route_wire_subtype                       1
#define    UF_route_harness_subtype                    2
#define    UF_route_path_subtype                       3
#define    UF_route_path_fmbd_subtype                  4
#define    UF_route_path_offset_subtype                5
#define    UF_route_built_in_path_subtype              6
#define    UF_route_cable_subtype                      7
#define    UF_route_jumper_wire_subtype                8
#define    UF_route_segment_set_subtype                9
#define    UF_route_subroute_subtype                   10

/* <jfc> Analysis objects */
#define UF_analysis_type                        169
#define    UF_dynamic_deviation_subtype                0
#define    UF_surface_section_subtype                  1
#define    UF_multi_section_subtype                    2
#define    UF_highlight_lines_subtype                  3
#define    UF_surf_deviation_subtype                   4
#define    UF_gap_flushness_subtype                    5
#define    UF_curve_continuity_subtype                 6
#define    UF_cross_section_subtype                    7
#define    UF_curve_curvature_subtype                  8
  
/* Web Express based Report Writer used in Scenario */
#define UF_report_type                          170
#define     UF_report_scenario_subtype                 0

#define UF_cam_type                             171      /* Obsolete in V10  Reused */
#define UF_shed_material_type                   171      /* NX 6 */

#define UF_cam_body_type                        172      /* Obsolete in V10 */

#define UF_cam_follower_type                    173      /* Obsolete in V10 */

/* #define UF_cam_function_type                 174         Obsolete in V10 */
#define  UF_machining_mfgftr_type               174

#define UF_cam_solid_cross_section              175

#define UF_mdm_contact_type                     176     /* For Motion contacts*/
#define    UF_mdm_3d_contact_subtype                   0

#define UF_drafting_image_type                  177

#define  UF_tracking_point_type                 178
#define    UF_cutter_tracking_point_subtype            0
#define    UF_mill_tracking_point_subtype              1
#define    UF_turn_tracking_point_subtype              2
#define    UF_standard_tracking_point_subtype          3
#define    UF_probe_tracking_point_subtype             4
#define  UF_tool_holder_type                    179

#define UF_material_type                        180

#define UF_texture_type                         181

#define UF_light_source_type                    182

#define UF_curve_group_type                     183
#define    UF_dropped_edge_group_subtype               0
#define    UF_simplified_group_subtype                 1
#define    UF_invis_solid_record_subtype               2
#define    UF_dropped_curve_group_subtype              3
#define    UF_InterferenceCurveGroupSubtype            4

#define UF_general_face_set_type                184

#define UF_anim_traj_type                       185

#define UF_sheet_group_type                     186

#define UF_cs2_rigid_set_type                   187

#define UF_design_rule_type                     188
#define    UF_design_rule_rule_subtype                 0
#define    UF_design_rule_violation_subtype            1
#define    UF_design_rule_override_subtype             2
#define    UF_design_rule_function_subtype             3
#define    UF_design_rule_location_subtype             4    

#define UF_thd_symbolic_data_type               189

#define UF_foreign_surf_type                    190

#define UF_user_defined_object_type             191

#define UF_generic_entity_type                  UF_user_defined_object_type

#define UF_generic_ent_int_sub_ent_type         192      /* Obsolete in V10 */
#define UF_part_field_type                      192
#define    UF_part_field_connectivity_subtype          0
#define    UF_part_field_depvariable_subtype           1
#define    UF_part_field_expression_subtype            2
#define    UF_part_field_formula_subtype               3
#define    UF_part_field_link_subtype                  4
#define    UF_part_field_table_subtype                 5

#define UF_generic_ent_real_sub_ent_type        193      /* Obsolete in V10 */

#define UF_symbol_font_type                     194

#define UF_dataum_point_type                    195      /* not use */

#define UF_datum_axis_type                      196

#define UF_datum_plane_type                     197

#define UF_solid_section_type                   198

#define UF_section_edge_type                    199
#define    UF_section_edge_0_subtype                   1
#define    UF_section_edge_1_subtype                   1

#define UF_section_segment_type                 200
#define    UF_arrow_segment_subtype                    1
#define    UF_cut_segment_subtype                      2
#define    UF_bend_segment_subtype                     3

#define UF_solid_silhouette_type                201
#define    UF_solid_silhouette_sl_subtype              0
#define    UF_solid_silhouette_uvhatch_subtype         1
#define    UF_vicurve_subtype                          2

#define UF_section_line_type                    202
#define    UF_simple_section_line_subtype              1
#define    UF_stepped_section_line_subtype             2
#define    UF_aligned_section_line_subtype             3
#define    UF_half_section_line_subtype                4
#define    UF_unfolded_section_line_subtype            5
#define    UF_breakline_subtype                        6
#define    UF_folded_section_line_subtype              7

#define UF_solid_in_view_type                   203

#define UF_component_set_type                   204

#define UF_feature_type                         205
#define    UF_feature_subtype                          0

#define UF_zone_type                            206
#define    UF_zone_box_subtype                         0
#define    UF_zone_plane_subtype                       1

#define UF_filter_type                          207
#define    UF_general_filter_subtype                   0
#define    UF_component_filter_subtype                 1

#define UF_promotion_type                       208
#define    UF_promotion_subtype                        0

#define UF_mdm_measure_type                     209

#define UF_mdm_trace_type                       210

#define UF_mdm_interference_type                211

#define UF_script_type                          212

#define UF_spreadsheet_type                     213
#define    UF_spreadsheet_xess_subtype                 0
#define    UF_spreadsheet_excel_subtype                1

#define UF_reference_type                       214      /* obsolete */

#define UF_scalar_type                          215

#define UF_offset_type                          216

#define UF_direction_type                       217

#define UF_parametric_text_type                 218
#define     UF_tabular_note_cell_subtype               2
#define     UF_parts_list_cell_subtype                12
#define     UF_spline_gear_cell_subtype               22

#define UF_xform_type                           219

#define UF_route_control_point_type             220

#define UF_route_port_type                      221

#define UF_route_segment_type                   222     /* obsolete in NX1 */
#define UF_mdm_sensor_type                      222     /* Added by Jason Fu, 30-Mar-07, for Sensor */
#define    UF_mdm_sensor_displacement_subtype          0
#define    UF_mdm_sensor_velocity_subtype              1
#define    UF_mdm_sensor_acceleration_subtype          2
#define    UF_mdm_sensor_force_subtype                 3
#define    UF_mdm_sensor_torque_subtype                4

#define UF_route_connection_type                223

#define UF_route_stock_type                     224
#define    UF_route_stock_subtype                      0
#define    UF_route_overstock_subtype                  1
#define    UF_route_filler_subtype                     2

#define UF_route_part_anchor_type               225

#define UF_route_cross_section_type             226

#define UF_route_stock_data_type                227

#define UF_route_corner_type                    228
#define    UF_route_bend_corner_subtype                0
#define    UF_route_miter_corner_subtype               1
#define    UF_route_cope_corner_subtype                2
#define    UF_route_disc_corner_subtype                3
#define    UF_route_sbend_corner_subtype               4

#define UF_route_part_type_type                 229

#define UF_fam_type                             230
#define    UF_fam_subtype                              0
#define    UF_fam_part_subtype                         1

#define UF_fam_attr_type                        231
#define    UF_fam_attr_text_subtype                    1
#define    UF_fam_attr_numeric_subtype                 2
#define    UF_fam_attr_integer_subtype                 3
#define    UF_fam_attr_double_subtype                  4
#define    UF_fam_attr_string_subtype                  5
#define    UF_fam_attr_part_subtype                    6
#define    UF_fam_attr_name_subtype                    7
#define    UF_fam_attr_instance_subtype                8
#define    UF_fam_attr_exp_subtype                     9
#define    UF_fam_attr_mirror_subtype                 10
#define    UF_fam_attr_density_subtype                11
#define    UF_fam_attr_feature_subtype                12

#define UF_sfem_mesh_type                       232
#define    UF_sfem_generic_mesh_subtype                0
#define    UF_sfem_trans_mesh_subtype                  1
#define    UF_sfem_mesh_nodes_subtype                  2

#define UF_sfem_mesh_recipe_type                233 /* Obsolete in NX4 */
#define    UF_sfem_generic_mesh_recipe_subtype         0
#define    UF_sfem_weld_mesh_recipe_subtype            1
#define    UF_sfem_connection_mesh_recipe_subtype      2
#define    UF_sfem_conn_weld_mesh_recipe_subtype       3
#define    UF_sfem_2d_contact_mesh_recipe_subtype      4

#define UF_faceset_type                         234

#define UF_sfem_mesh_geometry_type              235
#define    UF_sfem_mesh_geometry_body_subtype          0
#define    UF_sfem_mesh_geometry_face_subtype          1
#define    UF_sfem_mesh_geometry_edge_subtype          2
#define    UF_sfem_mesh_geometry_curve_subtype         3
#define    UF_sfem_mesh_geometry_point_subtype         4
#define    UF_sfem_mesh_geometry_comp_body_subtype     5
#define    UF_sfem_mesh_geometry_comp_face_subtype     6
#define    UF_sfem_mesh_geometry_comp_edge_subtype     7

#define UF_feature_cache_type                   236

#define UF_sfem_load_type                       237 /* Obsolete in NX4 */
#define UF_mdm_motor_type                       237 /* Added by Jason Fu, 30-Mar-07, for Motor */
#define    UF_mdm_pmdc_velocity_subtype                0
#define    UF_mdm_pmdc_torque_subtype                  1

#define UF_sfem_bndcond_type                    238 /* Obsolete in NX4 */
#define UF_response_simulation_type             238
#define    UF_ra_sensor_subtype                        1
#define    UF_ra_strain_gage_subtype                   2

#define UF_sfem_property_type                   239
#define    UF_sfem_generic_property_subtype            1
#define    UF_sfem_mat_property_subtype                2
#define    UF_sfem_sect_property_subtype               3
#define    UF_sfem_property_proxy_subtype              4

#define UF_sfem_property_name_type              240

#define UF_axis_type                            241

#define UF_cs2_vertex_type                      242

#define UF_cs2_constraint_type                  243
#define    UF_cs2_simple_subtype                       0
#define    UF_cs2_dim_subtype                          1
#define    UF_cs2_helped_subtype                       2
#define    UF_cs2_dim_helped_subtype                   3
#define    UF_cs2_string_constraint_subtype            4
#define    UF_cs2_trim_constraint_subtype              5
#define    UF_cs2_offset_constraint_subtype            6
#define    UF_cs2_equation_constraint_subtype          7
#define    UF_cs2_pgm_offset_constraint_subtype        8
#define    UF_cs2_point_on_loop_subtype                9
#define    UF_cs2_recipe_trim_subtype                  10

#define UF_cs2_constraint_system_type           244
#define    UF_cs2_temporary_cs_subtype                 0
#define    UF_cs2_permanent_cs_subtype                 1

#define UF_attribute_category_type              245

#define UF_attribute_password_type              UF_attribute_category_type

#define UF_attribute_type                       246
#define    UF_string_attribute_subtype                 1
#define    UF_integer_attribute_subtype                2
#define    UF_scalar_attribute_subtype                 3
#define    UF_length_attribute_subtype                 4
#define    UF_area_attribute_subtype                   5
#define    UF_volume_attribute_subtype                 6
#define    UF_date_attribute_subtype                   7
#define    UF_reference_attribute_subtype              8
#define    UF_null_attribute_subtype                   9

#define UF_note_type                            247
#define    UF_general_note_subtype                     0
#define    UF_appended_text_subtype                    1
#define    UF_limit_or_fit_subtype                     2

#define UF_tol_feature_instance_type            248
#define    UF_feature_instance_subtype                 0
#define    UF_datum_identifier_instance_subtype        1
#define    UF_datum_point_instance_subtype             2
#define    UF_datum_line_instance_subtype              3
#define    UF_datum_area_instance_subtype              4 /* obsolete in V15.0 */
#define    UF_rectangular_area_instance_subtype        5
#define    UF_circular_area_instance_subtype           6
#define    UF_cylindrical_area_instance_subtype        7
#define    UF_directed_datum_ident_instance_subtype    8
#define    UF_user_defined_area_instance_subtype       9
#define    UF_complex_feature_instance_subtype        10
#define    UF_table_instance_subtype                  11

#define UF_engineering_text_type                249

#define UF_annotation_type                      250      /* obsolete in NX4 */
#define UF_pmi_filter_type                      250
#define    UF_pmi_filter_all_subtype                   0
#define    UF_pmi_filter_by_type_subtype               1
#define    UF_pmi_filter_by_view_subtype               2

#define UF_tolerance_feature_type               251
#define    UF_tolerance_model_subtype                  0
#define    UF_tolerance_feature_subtype                1
#define    UF_complex_tolerance_feature_subtype        2
#define    UF_complex_tolerance_subfeature_subtype     3
#define    UF_datum_object_subtype                     4

#define UF_leader_type                          252

#define UF_engineering_symbol_type              253
#define    UF_symbol_instance_subtype                  0

#define UF_feature_control_frame_type           254
#define    UF_straightness_subtype                     0
#define    UF_flatness_subtype                         1
#define    UF_circular_subtype                         2
#define    UF_cylindrical_subtype                      3
#define    UF_line_profile_subtype                     4
#define    UF_surface_profile_subtype                  5
#define    UF_angular_subtype                          6
#define    UF_perpendicular_subtype                    7
#define    UF_parallel_subtype                         8
#define    UF_position_subtype                         9
#define    UF_concentric_subtype                      10
#define    UF_symmetric_subtype                       11
#define    UF_circular_runout_subtype                 12
#define    UF_total_runout_subtype                    13

/* type and subtypes for NX3 post processor */
#define UF_sfpp_post_type                       255
#define    UF_sfpp_post_display_subtype                0
#define    UF_sfpp_post_def_fringe_subtype             1
#define    UF_sfpp_post_def_face_subtype               2
#define    UF_sfpp_post_def_edge_subtype               3
#define    UF_sfpp_post_undef_face_subtype             4
#define    UF_sfpp_post_undef_edge_subtype             5

/* Incremented max_entity_type after adding the types above - Amit */
#define UF_max_entity_type                     255

/*  */

/* special selection subtypes */
#define UF_all_subtype                          (-1)
#define UF_member_subtype                       (-2) /* to be obsoleted,
        use filter function to filter members out if needed */


#ifdef __cplusplus
}
#endif

#endif /* UF_OBJECT_TYPES_H_INCLUDED */
