/****************************************************************************
    Copyright (c) 2010,2014 Siemens Product Lifecycle Management Software, Inc.
                Unpublished - All rights reserved




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

#define UF_point_type                             2      /* Point entity */
#define    UF_point_subtype                            0
#define    UF_old_point_1_subtype                      1 /* Obsolete in v10 */
#define    UF_old_point_2_subtype                      2 /* Obsolete in v10 */

#define UF_line_type                              3      /* Line entity */
#define    UF_line_normal_subtype                      0
#define    UF_line_old_subtype                         1 /* Obsolete in v10 */
#define    UF_sketch_ref_line_subtype                101 /* Obsolete in V17.0. */
#define    UF_infinite_line_subtype                    2

#define UF_solid_collection_type                  4      /* Obsolete in V10 - Reused in NX 9.0 for UF_image_type */

#define UF_image_type                             4      /* Image (new in NX9.0) */
#define    UF_image_raster_image_subtype               0 /* Raster Image (new in NX9.0) */

#define UF_circle_type                            5   /* Circle entity - also called "arc" */
#define    UF_circle_open_subtype                      0 /* Not Used - To determine whether a circle is open or closed please use UF_MODL_ask_curve_periodicity */
#define    UF_circle_closed_subtype                    1 /* Not Used - To determine whether a circle is open or closed please use UF_MODL_ask_curve_periodicity */
#define    UF_sketch_ref_circle_subtype              101 /* Obsolete in V17.0. */

#define UF_conic_type                             6      /* Conic entity */
#define    UF_conic_ellipse_subtype                    2 /* Conic Arc - Ellipse */
#define    UF_conic_parabola_subtype                   3 /* Conic Arc - Parabola */
#define    UF_conic_hyperbola_subtype                  4 /* Conic Arc - Hyperbola */

#define UF_spcurve_type                           7        /* Obsolete in V10 */
#define    UF_spcurve_open_subtype                     1   /* Obsolete in V10 */
#define    UF_spcurve_closed_subtype                   2   /* Obsolete in V10 */
#define    UF_spcurve_periodic_subtype                 3   /* Obsolete in V10 */

#define UF_old_spline_type                        8        /* Obsolete in V10 - Reused in NX 9.0 for UF_product_interface_type */
#define    UF_spline_open_subtype                      1   /* Obsolete in V10 - Reused in NX 9.0 for UF_product_interface_geometry_subtype */
#define    UF_spline_closed_subtype                    2   /* Obsolete in V10 - Reused in NX 9.0 for UF_product_interface_collection_subtype */

#define UF_product_interface_type                 8        /* Product Interface object (new in NX9.0) */
#define    UF_product_interface_geometry_subtype       1   /* Product Interface Geometry object (new in NX9.0) */
#define    UF_product_interface_collection_subtype     2   /* Product Interface Collection object (new in NX9.0) */
#define    UF_product_interface_expression_subtype     3   /* Product Interface Expression object (new in NX9.0) */
 
#define UF_spline_type                            9        /* Spline entity (Renamed in V10) */
#define    UF_spline_subtype                           0
#define    UF_b_curve_bezier_subtype                   0   /* There is no difference
                                                              between subtype 0 and
                                                              subtype 1 */
#define    UF_b_curve_b_spline_subtype                 1   /* There is no difference
                                                              between subtype 0 and
                                                              subtype 1 */
#define    UF_sketch_ref_spline_subtype              101   /* Obsolete in V17.0 */
#define    UF_polyline_subtype                         2

#define UF_pattern_type                          10        /* Pattern entity */
#define    UF_pattern_subtype                          0
#define    UF_pattern_point_subtype                    1

#define UF_part_attribute_type                   11        /* Part Attribute */
#define    UF_part_attribute_subtype                   0
#define    UF_part_attribute_cache_subtype             1
#define    UF_temporary_part_attribute_subtype         2

#define UF_layer_category_type                   12        /* Layer category entity */

#define UF_kanji_type                            13        /* Kanji entity */

#define UF_boundary_type                         14

#define UF_group_type                            15        /* Group entity */

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

#define UF_drafting_entity_type                  25        /* Drafting entities */
#define    UF_draft_note_subtype                       1   /* Drafting note */
#define    UF_draft_label_subtype                      2   /* Drafting label */
#define    UF_draft_id_symbol_subtype                  3   /* Drafting ID symbol */
#define    UF_draft_fpt_subtype                        4   /* Drafting FPT Symbol */
#define    UF_draft_cntrline_subtype                   5   /* Drafting Centerline */
#define    UF_draft_crosshatch_subtype                 6   /* Drafting Crosshatch */
#define    UF_draft_assorted_parts_subtype             7   /* Drafting Assorted Parts */
#define    UF_draft_intersection_subtype               8   /* Drafting Intersection Point */
#define    UF_draft_target_point_subtype               9   /* Drafting Target Point */
#define    UF_draft_user_defined_subtype              10   /* Drafting User Defined Symbol */
#define    UF_draft_area_fill_subtype                 11   /* Drafting Area Fill */
#define    UF_draft_solid_fill_subtype                12   /* Drafting Solid Fill */
#define    UF_draft_linear_cntrln_subtype             13   /* Drafting Linear Centerline - created from the Center Mark command */
#define    UF_draft_full_cir_cntrln_subtype           14   /* Drafting Full Circular Centerline */
#define    UF_draft_part_cir_cntrln_subtype           15   /* Drafting Partial Circular Centerline */
#define    UF_draft_full_blt_circle_subtype           16   /* Drafting Full Bold Circle */
#define    UF_draft_part_blt_circle_subtype           17   /* Drafting Partial Bold Circle */
#define    UF_draft_offset_cntrpt_subtype             18   /* Drafting Offset Center Point */
#define    UF_draft_cyl_cntrln_subtype                19   /* Drafting Cylindrical Centerline */
#define    UF_draft_sym_cntrln_subtype                20   /* Drafting Symmetrical Centerline */
#define    UF_draft_block_cntrln_subtype              21   /* Drafting Centerline created from the 2d centerline command */
#define    UF_draft_label_on_parent_subtype           22   /* Drafting view lables created on the parent of a detail view */
#define    UF_draft_point_subtype                     37   /* Internal use only */
#define    UF_draft_facet_subtype                     41   /* Legacy - view contents for old-style faceted representation views */
#define    UF_draft_title_block_subtype               42   /* Drafting title block */
#define    UF_draft_frame_bar_subtype                 43   /* Drafting frame bar */
#define    UF_draft_arrow_subtype                     44   /* Drafting Arrow */
#define    UF_draft_cutting_plane_symbol_subtype      45   /* Stand alone section line created from the Section Line command */

#define UF_dimension_type                        26        /* Dimension entities */
#define    UF_dim_horizontal_subtype                   1   /* Horizontal dimension */
#define    UF_dim_vertical_subtype                     2   /* Vertical dimension */
#define    UF_dim_parallel_subtype                     3   /* Parallel dimension */
#define    UF_dim_cylindrical_subtype                  4   /* Cylindrical dimension */
#define    UF_dim_perpendicular_subtype                5   /* Perpendicular dimension */
#define    UF_dim_angular_minor_subtype                6   /* Angular dimension - minor */
#define    UF_dim_angular_major_subtype                7   /* Angular dimension - major */
#define    UF_dim_arc_length_subtype                   8   /* Arc Length dimension */
#define    UF_dim_radius_subtype                       9   /* Radius dimension */
#define    UF_dim_diameter_subtype                    10   /* Diameter dimension */
#define    UF_dim_hole_subtype                        11   /* Hole dimension */
#define    UF_dim_conc_circle_subtype                 12   /* Concentric Circle dimension */
#define    UF_dim_ordinate_horiz_subtype              13   /* Ordinate dimension - horizontal */
#define    UF_dim_ordinate_vert_subtype               14   /* Ordinate dimension - vertical */
#define    UF_dim_assorted_parts_subtype              15   /* Dimension by parts - only created by converted */
#define    UF_dim_folded_radius_subtype               16   /* Folded radius dimension */
#define    UF_dim_chain_dimensions_subtype            17   /* Obsolete */
#define    UF_dim_ordinate_origin_subtype             18   /* Ordinate origin - point ordinate dimensions are created from */
#define    UF_dim_perimeter_subtype                   19   /* Special dimension used by sketch only */
#define    UF_dim_chamfer_subtype                     20   /* Chamfer dimension */

#define UF_font_table_type                       27        /* Font Table */

#define UF_color_table_type                      28        /* Color Table */

#define UF_margin_type                           29

#define UF_gfem_load_type                        31       /* Obsolete in V16 */
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
#define    UF_sfem_bolt_recipe_nut_subtype                      7
#define    UF_sfem_bolt_recipe_tap_subtype                      8
#define    UF_sfem_bolt_recipe_spider_subtype                   9

#define UF_gfem_ferd_type                        34  /* Obsolete in V16 */
#define    UF_gfem_ferd_subtype                   0

#define UF_meshpoint_type                        34

#define UF_gfem_annotation_type                  35  /* Obsolete in V16 -- Reused */
#define    UF_gfem_annotation_subtype                  0

#define UF_caemisc_type                          35
#define    UF_caemisc_edge_density_subtype             1
#define    UF_caemisc_face_density_subtype             2
#define    UF_caemisc_mmc_subtype                      3
#define    UF_caemisc_weld_row_subtype                 4
#define    UF_caemisc_mapped_hole_subtype              5
#define    UF_caemisc_fillet_density_subtype           6
#define    UF_caemisc_cylinder_density_subtype         7
#define    UF_caemisc_boundary_layer_subtype           8
#define    UF_caemisc_bounding_volume_subtype          9
#define    UF_caemisc_fem_rotation_axis_subtype       10  /* cae model rotation axis */
#define    UF_caemisc_selection_recipe_subtype          11 /*CAE Selection Recipe*/
#define    UF_caemisc_point_density_subtype             12 /* Mesh Control Type- Point Density */
#define    UF_caemisc_bounding_volume_density_subtype   13 /* Mesh Control Type- Bounding Volume Density */

#define UF_gfem_control_node_list_type           36  /* Obsolete in V16 */
#define    UF_gfem_control_node_list_subtype           0

#define UF_gfem_material_type                    37
#define    UF_gfem_material_subtype                    0

#define UF_instance_type                         38      /* Obsolete in V4 - Reused in NX 8.0 for UF_pdm_design_feature_type */

#define UF_pdm_design_feature_type               38
#define    UF_pdm_design_feature_subtype               0

#define UF_connection_type                       39      /* Obsolete in V4 */
#define    UF_connection_normal_subtype                0
#define    UF_connection_offpage_subtype               1
#define    UF_connection_special_subtype               2

#define UF_prefix_type                           40      /* Obsolete in V4, re-use it by UF_view_set_type */
#define UF_view_set_type                         40
#define    UF_view_set_subtype                         0

#define UF_tool_type                             41      /* Obsolete, reused by RM_component2d_type  */
#define UF_component2d_type                      41

#define UF_sub_entity_for_dim_type               42
#define    UF_dim_sub_line_subtype                     1
#define    UF_dim_sub_arc_subtype                      2
#define    UF_dim_sub_text_subtype                     3

#define UF_b_surface_type                        43        /* B-Surface Face */
#define    UF_b_surface_bezier_subtype                 0   /* Obsolete in V10 */
#define    UF_b_surface_b_spline_subtype               1   /* Obsolete in V10 */

#define UF_validation_type                       44

#define UF_coordinate_system_type                45
#define    UF_csys_normal_subtype                      0
#define    UF_csys_wcs_subtype                         1
#define    UF_csys_cylindrical_subtype                 2
#define    UF_csys_spherical_subtype                   3

#define UF_plane_type                            46      /* Plane */

#define UF_bounded_plane_loop_type               47      /* Obsolete in V7 */
#define    UF_bounded_plane_loop_subtype               0

#define UF_report_entity_type                    48      /* Obsolete in NX2 */
#define    UF_report_parts_list_subtype                1

#define UF_report_entry_entity_type              49      /* Obsolete in NX2 */
#define    UF_report_parts_list_entry_subtype          1

#define UF_pattern_definition_type               49      /* new in NX9 */
#define UF_pattern_definition_subtype                  0
#define UF_displayed_pattern_definition_subtype        1
#define UF_linear_pattern_definition_subtype           2
#define UF_circular_pattern_definition_subtype         3
#define UF_reference_pattern_definition_subtype        4
#define UF_pure_reference_pattern_definition_subtype   5

#define UF_nesting_type                          50

#define UF_tool_display_type                     51      /* Display of current tool/mcs */
#define UF_tool_display_subtype                        0 /* Tool display object */
#define UF_mcs_display_subtype                         1 /* MCS display object */

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
#define    UF_skeleton_entity_selection_plane_subtype 10 /* new in NX8 */
#define    UF_skeleton_drawing_sheetzones_grid_subtype 11 /* new in NX8 */

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
#define    UF_parm_display_data_subtype               21 /* Obsolete in NX12 */
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
#define    UF_parm_annotation_subtype                 42 /* OBSOLETE in NX12 */
#define    UF_parm_crvtr_disp_subtype                 43
#define    UF_parm_drawings_subtype                   44 /* OBSOLETE in NX12 */
#define    UF_parm_modeling_subtype                   45
#define    UF_parm_tabular_note_subtype               46 /* OBSOLETE in NX12 */
#define    UF_parm_parts_list_subtype                 47 /* OBSOLETE in NX12 */
#define    UF_parm_units_subtype                      48 /* OBSOLETE in NX12 */
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
#define    UF_parm_pmi_data_subtype                   63  /* OBSOLETE in NX12 */
#define    UF_parm_global_set_subtype                 64
#define    UF_parm_field_main_subtype                 65  /* root object of Fields */
#define    UF_parm_kmc_main_subtype                   66  /* root object of MOTION */
#define    UF_parm_cae_so_manager_subtype             67
#define    UF_parm_aero_sheet_metal_subtype           68
#define    UF_parm_flex_pcb_design_subtype            69
#define    UF_parm_caemodl_volume_subtype             70
#define    UF_parm_section_list_subtype               71
#define    UF_parm_autopopulate_subtype               72
#define    UF_parm_cae_ideal_main_subtype             73  /* Idealized part  */
#define    UF_parm_main_assy_fem_subtype              74  /* Root object of Assembly FEM */
#define    UF_parm_attr_subtype                       99  /* OBSOLETE in NX12 */
#define    UF_parm_student_edition_subtype            75
#define    UF_parm_imported_jt_data_subtype           77
#define    UF_parm_drafting_automation_subtype        78
#define    UF_parm_main_agent_subtype                 79 /* Root object of all CaeSim UpdateAgents */
#define    UF_parm_ship_bodyref                       80
#define    UF_parm_ship_rootobject                    81
#define    UF_parm_ftk_function_main_subtype          82 /* FTK function main object */
#define    UF_parm_layout2d_subtype                   83  
#define    UF_parm_drawto3d_subtype                   84 /* Root object subtype for Drawing to 3D functionality */
#define    UF_parm_ship_navigator                     85 /* Root object subtype for ship navigator data */
#define    UF_parm_draftingcore_subtype               87 /* Root Object for drafting core */

#define UF_device_type                           54      /* Obsolete in V15 - Reused In NX6 */
#define UF_dynamic_section_cut_type              54
#define    UF_dynamic_section_cut_subtype_any         -1
#define    UF_dynamic_section_body_cut_subtype        1
#define    UF_dynamic_section_component_cut_subtype   2

#define UF_matrix_type                           55      /* Matrix */

#define UF_gear_type                             56      /* Obsolete in V10 */
#define UF_sfem_dofset_type                      56      /* Reused UF_gear_type in NX750 */

#define UF_gear_mesh_type                        57      /* Obsolete in V10 */

#define UF_gear_train_type                       58      /* Obsolete in V10 */

#define UF_fatigue_type                          59      /* Obsolete in V10 - Reused */
#define UF_camera_type                           59

#define UF_view_type                             60
#define    UF_view_section_subtype                           0
#define    UF_view_instance_subtype                          1
#define    UF_view_imported_subtype                          2
#define    UF_view_base_member_subtype                       3
#define    UF_view_orthographic_subtype                      4
#define    UF_view_auxiliary_subtype                         5
#define    UF_view_detail_subtype                            6
#define    UF_view_modeling_subtype                          7
#define    UF_view_user_defined_subtype                      8
#define    UF_view_graph_subtype                             9
#define    UF_view_drawing_sheet_subtype                    10
#define    UF_view_cae_subtype                              11
#define    UF_view_break_subtype                            12
#define    UF_view_query_result_subtype                     13
#define    UF_view_drawing_subtype                          14
#define    UF_view_break_slave_subtype                      15
#define    UF_view_search_model_view_subtype                16
#define    UF_view_lightweight_section_subtype              17
#define    UF_view_imported_pmi_lightweight_section_subtype 18

#define UF_layout_type                           61
#define    UF_normal_layout_subtype                    0
#define    UF_canned_layout_subtype                    1

#define UF_drawing_type                          62         /* Drawing entities */
#define    UF_drafting_drawing_subtype                 0    /* Standard drawing */
#define    UF_layout_drawing_subtype                   1    /* Conceptual design Layout drawing */

#define UF_component_type                        63
#define    UF_component_subtype                        0
#define    UF_part_occurrence_subtype                  1
#define    UF_shadow_part_occ_subtype                  2
#define    UF_design_element_search_result_subtype     3

#define UF_reference_set_type                    64
#define    UF_reference_design_subtype                 0
#define    UF_reference_tool_subtype                   1
#define    UF_reference_parameter_subtype              2
#define    UF_reference_cam_template_subtype           3
#define    UF_reference_cam_task_subtype               4
#define    UF_reference_design_model_subtype           5
#define    UF_reference_design_lightweight_subtype     6
#define    UF_reference_flat_pattern_subtype           7

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

#define UF_solid_type                            70      /* Solid */
#define    UF_solid_body_subtype                       0 /* Solid body */
#define    UF_solid_swept_body_subtype                 1 /* Internal use only - not displayable */
#define    UF_solid_face_subtype                       2 /* Solid face */
#define    UF_solid_edge_subtype                       3 /* Solid edge */
#define    UF_solid_silhouette_subtype                 4 /* Moved to type 201 in V10 */
#define    UF_solid_foreign_surf_subtype               5 /* Solid foreign Surface */

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
#define    UF_mdm_revolute_fixed_subtype               4 /* Obsolete in NX 12 */
#define    UF_mdm_slider_subtype                       5
#define    UF_mdm_slider_fixed_subtype                 6 /* Obsolete in NX 12 */
#define    UF_mdm_cylinder_subtype                     7
#define    UF_mdm_cylinder_fixed_subtype               8 /* Obsolete in NX 12 */
#define    UF_mdm_screw_subtype                        9
#define    UF_mdm_screw_fixed_subtype                 10 /* Obsolete in NX 12 */
#define    UF_mdm_universal_subtype                   11
#define    UF_mdm_universal_fixed_subtype             12 /* Obsolete in NX 12 */
#define    UF_mdm_sphere_subtype                      13
#define    UF_mdm_sphere_fixed_subtype                14 /* Obsolete in NX 12 */
#define    UF_mdm_planar_subtype                      15
#define    UF_mdm_planar_fixed_subtype                16 /* Obsolete in NX 12 */
#define    UF_mdm_gear_subtype                        17
#define    UF_mdm_gear_fixed_subtype                  18 /* Obsolete in NX 12 */
#define    UF_mdm_rckpn_subtype                       19
#define    UF_mdm_rckpn_fixed_subtype                 20 /* Obsolete in NX 12 */
#define    UF_mdm_pt_crv_subtype                      21
#define    UF_mdm_pt_crv_fixed_curve_subtype          22 /* Obsolete in NX 12 */
#define    UF_mdm_pt_crv_fixed_point_subtype          23 /* Obsolete in NX 12 */
#define    UF_mdm_crv_crv_subtype                     24
#define    UF_mdm_cable_subtype                       25
#define    UF_mdm_joint_fixed_subtype                 26 /* all fixed joint type*/
/* CV joint subtype - CV = constant velocity*/
#define    UF_mdm_cv_subtype                          27
#define    UF_mdm_cv_fixed_subtype                    28 /* Obsolete in NX 12 */
#define    UF_mdm_general_coupler_subtype             29
#define    UF_mdm_link_coupler_subtype                30 /* Motion LinkCoupler */

/* Joint Primitives */
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
#define    UF_mdm_spring_rot_cyl_subtype               10 /* Represents a spring defined on top of a cylindrical joint */
#define UF_mdm_motion_vector_type                89

#define UF_mdm_force_type                        90

#define UF_shaft_stress_type                     91      /* Obsolete in V10 */

#define UF_mechatronics_kinematics_type           91     /* The basic object type with displayable physical properties. */
#define  UF_mechatronics_rigid_body_subtype                   0  /* A Rigid Body defines objects to be able to move about the world. */
#define  UF_mechatronics_collision_body_subtype               1  /* A Collision Body defines objects to be able to collide with one another. */
#define  UF_mechatronics_trigger_body_subtype                 2  /* A Collision Sensor is able to detect the presence of objects that intersect with its volume. */
#define  UF_mechatronics_hinge_joint_subtype                  3  /* A Hinge Joint causes objects to be connected along an axis of rotation. */
#define  UF_mechatronics_sliding_joint_subtype                4  /* A Sliding Joint causes objects to be connected along a fixed linear axis. */
#define  UF_mechatronics_cylindrical_joint_subtype            5  /* A Cylindrical Joint is a connection that can move both linearly and rotationally. */
#define  UF_mechatronics_ball_joint_subtype                   6  /* Objects are connected at a shared point and can move all ways rotationally. */
#define  UF_mechatronics_fixed_joint_subtype                  7  /* Fixed joint is that objects are glued to one another completely. */
#define  UF_mechatronics_angular_spring_joint_subtype         8  /* Angular spring joint causes objects to behave as though there is a spring-like force between them that grows as the objects rotate relative to each other. */
#define  UF_mechatronics_linear_spring_joint_subtype          9  /* A Linear Spring Joint causes objects to behave as though there is a spring-like force between them that grows as the objects move farther apart or closer together. */
#define  UF_mechatronics_angular_limit_joint_subtype          10 /* Angular limit joint causes objects to stop moving when their relative position moves beyond a certain degree or get too close together. */
#define  UF_mechatronics_linear_limit_joint_subtype           11 /* Linear Limit Joint causes objects to stop moving when their relative position moves beyond a certain distance or get too close together. */
#define  UF_mechatronics_conveyor_surface_constraint_subtype  12 /* Transport Surface causes a face on a geometric object to behave like it is moving even if the object it is attached to is not. */
#define  UF_mechatronics_speed_constraint_subtype             13 /* A Speed Control causes objects attached to an axis to move continuously on that axis with a given speed. */
#define  UF_mechatronics_position_constraint_subtype          14 /* A Position Control causes objects attached to an axis to move along that axis to a given position. */
#define  UF_mechatronics_gear_constraint_subtype              15 /* A Gear causes objects attached to the axes to move in unison at a fixed ratio. */
#define  UF_mechatronics_cam_constraint_subtype               16 /* Cam Constraint like a gear but the relationship between object motions is determined by the motion profile or cam profile that is created by the user. */
#define  UF_mechatronics_breaking_constraint_subtype          17 /* Breaking constraint specifies that a joint can be broken if the force applied to it exceeds a certain value. */
#define  UF_mechatronics_prevent_collision_constraint_subtype 18 /* Prevent Collision Constraint changes the collision properties between a specific pair of bodies. */
#define  UF_mechatronics_change_material_constraint_subtype   19 /* Change Material Constraint changes the friction and restitution properties between a specific pair of bodies. */
#define  UF_mechatronics_object_source_subtype                20 /* Object Source is used to define some objects that can be copied during simulation. */
#define  UF_mechatronics_object_sink_subtype                  21 /* Object Sink is used to define some objects that delete copies of physics objects during simulation. */
#define  UF_mechatronics_graph_control_subtype                22 /* Graph Control is used to apply the values from the graph to the axis control over time. */
#define  UF_mechatronics_external_connection_subtype          23 /* External Connection objects are able to connect physics runtime properties to external signals. */
#define  UF_mechatronics_proxy_object_subtype                 24 /* A Proxy Object defines the object that has certain parameter attributes, encapsulates certain physics objects, and has some geometric representation. */
#define  UF_mechatronics_proxy_override_object_subtype        25 /* A Proxy Override Object defines the object to be the override of the proxy definition object. */
#define  UF_mechatronics_signal_adapter_subtype               26 /* A Signal Adapter is able to define signals and establish the connections between physics runtime properties and signals. */
#define  UF_mechatronics_adapter_signal_subtype               27 /* Signal may carry information for communicating with physics object or external device. */
#define  UF_mechatronics_signal_connection_subtype            28 /* A Signal Connection defines the data flow between signal and physics property or device. */
#define  UF_mechatronics_point_on_curve_joint_subtype         29 /* A Point On Curve Joint causes objects to be connected to a curve at a point on the curve. */
#define  UF_mechatronics_curve_on_curve_joint_subtype         30 /* A Curve On Curve Joint causes objects including one section curve to be connected to another curve. */
#define  UF_mechatronics_shmsignal_connection_subtype         31 /* Signal connection objects are able to connect MCD signals with SHM signals. */
#define  UF_mechatronics_object_transformer_subtype           32 /* An Object Transformer defines objects to be able to transform copies of rigid objects to another during simulation. */
#define  UF_mechatronics_spring_damper_subtype                33 /* A Spring Damper causes spring force and damping to an axis joint. */
#define  UF_mechatronics_read_write_device_subtype            34 /* An object is able to read or write parameters from or to a specific object. */
#define  UF_mechatronics_display_changer_subtype              35 /* Display Changer is used to change the display properties (Color, Translucency, and Visibility) of rigid body during simulation. */
#define  UF_mechatronics_virtual_axis_subtype                 36 /* A Virtual Axis joint holds kinematics information without geometry. */
#define  UF_mechatronics_path_constraint_joint_subtype        37 /* Path Constraint Joint defines a object that limits a rigid body on path, which is defined a sequence of orientation CSYS. */
#define  UF_mechatronics_distance_sensor_subtype              38 /*A distance sensor specifies the shortest distance between the sensor and collision body.*/
#define  UF_mechatronics_position_sensor_subtype              39 /*A position sensor returns the angular or linear position of the selected joint.*/
#define  UF_mechatronics_velocity_sensor_subtype              40 /*A velocity sensor returns the angular or linear velocity of the selected joint.*/
#define  UF_mechatronics_generic_sensor_subtype               41 /*A generic sensor returns the parameter value of the selected object.*/
#define  UF_mechatronics_limit_switch_subtype                 42 /*A limit switch references any runtime parameter from the selected object and has a boolean output.*/
#define  UF_mechatronics_relay_subtype                        43 /*A relay references any runtime parameter from the selected object and has a boolean output.*/
#define  UF_mechatronics_inclinometer_subtype                 44 /*An inclinometer returns the angle value of the selected rigid body.*/
#define  UF_mechatronics_accelerometer_subtype                45 /*An accelerometer returns the accelerometer value of the selected rigid body.*/
#define  UF_mechatronics_force_torque_constraint_subtype      46 /* A force or torque control is applied to both connected rigid bodies with respect to the axis joint. */
#define  UF_mechatronics_screw_joint_subtype                  47 /* A Screw Joint defines objects along a rotatable linear axis so that they can rotate and move at a fixed ratio. */
#define  UF_mechatronics_planar_joint_subtype                 48 /* A Planar Joint defines objects so that they are free to slide and rotate relative to each other while remaining in planar contact. */
#define  UF_mechatronics_rack_pinion_constraint_subtype       49 /* A Rack and Pinion constraint defines the motion of linear and rotary axes so that they move at a fixed ratio. */
#define  UF_mechatronics_signal_subtype                       50 /* MCD Signal is used as a communicator between MCD and external server  */
#define  UF_mechatronics_expression_block_subtype             51 /* Expression Block works like black box. It defines many slots (inputs/outputs) and calculates outputs via formula based on inputs. */
#define  UF_mechatronics_matlabsignal_connection_subtype      52 /* A Signal Connection defines the data flow between matlab signal and physics property or device. */
#define  UF_mechatronics_pneumatic_cylinder_subtype           53 /* A pneumatic cylinder causes forces according to the characteristic of a compressible fluid to move simulation objects. */
#define  UF_mechatronics_pneumatic_valve_subtype              54 /* A pneumatic valve controls a pneumatic cylinder. */
#define  UF_mechatronics_hydraulic_cylinder_subtype           55 /* A hydraulic cylinder causes forces according to the characteristic of a incompressible fluid to move simulation objects. */
#define  UF_mechatronics_hydraulic_valve_subtype              56 /* A hydraulic valve controls a hydraulic cylinder. */
#define  UF_mechatronics_transmitter_entry_subtype            57 /* A transmitter entry can transmit one rigid body from one window to another. */
#define  UF_mechatronics_transmitter_exit_subtype             58 /* A transmitter exit can transmit one rigid body from one window to another. */
#define  UF_mechatronics_signal_mapping_connection_subtype    59 /* A Signal Connection defines the data flow between external signals and mcd signal. */
#define  UF_mechatronics_snap_point_subtype                   60 /* A SnapPoint defines one body positioning or two bodies exactly lie upon each other */
#define  UF_mechatronics_three_joint_coupler_constraint_subtype 61 /* A three joint coupler. */
#define  UF_mechatronics_chain_joint_subtype                  62 /* A Chain Joint causes objects to be connected along a series of axises of rotation. */
#define  UF_mechatronics_tracer_subtype                       63 /* A Tracer will draw the path of a point in the onject. */
#define  UF_mechatronics_dynamic_object_instantiation_subtype 64 /* A dynamic object instantiation controls a set of align bodies.*/

#define UF_shaft_feature_type                    92      /* Obsolete in V10 */
#define UF_mdm_flexbody_type                     92      /* Reused in NX8 */

#define UF_shaft_load_type                       93      /* Obsolete in V10. Reused as UF_subdivision_mesh_type in NX9.0 */
#define UF_subdivision_mesh_type                             93 /* Reused UF_shaft_load_type in NX9.0 */
#define     UF_subdivision_mesh_body_subtype                  1
#define     UF_subdivision_mesh_face_subtype                  2
#define     UF_subdivision_mesh_edge_subtype                  3
#define     UF_subdivision_mesh_vertex_subtype                4

#define UF_shaft_support_type                    94      /* Obsolete in V10 */
#define UF_extended_type                         94      /* Prior to NX9, there was a limit (UF_max_entity_type) on the total number of object types.
                                                            This limit has been removed in NX9. UF_extended_type is a object type that stands for
                                                            all the object types over UF_max_entity_type (henceforth called extended object types).
                                                            This is just a dummy type to represent all the extended object types and part files will not have 
                                                            objects of this specific type.
                                                            Cycling APIs that were written prior to NX9 (UF_OBJ_cycle_objs_in_part and UF_OBJ_cycle_by_name_and_type)
                                                            will return all the objects of type over UF_max_entity_type (the so called UF_extended_type) when UF_extended_type
                                                            is passed in as input.
                                                         */

#define UF_shaft_section_type                    95      /* Obsolete in V10 */
#define UF_extended_displayable_type             95      /* Prior to NX9, there was a limit (UF_max_entity_type) on the total number of object types.
                                                            This limit has been removed in NX9. UF_extended_displayable_type is a object type that stands for
                                                            all the displayable object types over UF_max_entity_type (henceforth called extended displayable object types).
                                                            This is just a dummy type to represent all the extended object types and part files will not have 
                                                            objects of this specific type.
                                                            Cycling APIs that were written prior to NX9 (UF_OBJ_cycle_objs_in_part and UF_OBJ_cycle_by_name_and_type)
                                                            will return all the displayable objects of type over UF_max_entity_type (the so called UF_extended_displayable_type) 
                                                            when UF_extended_displayable_type is passed in as input.
                                                         */

#define UF_shaft_type                            96      /* Obsolete in V10 */

#define UF_mdm_analysis_pt_type                  97      /* Obsolete in V10 */

#define UF_mdm_marker_type                       97      /* replaces UF_mdm_analysis_pt_type */
#define    UF_mdm_inertia_marker_subtype               0
#define    UF_mdm_user_defined_marker_subtype          1
#define    UF_mdm_cofm_marker_subtype                  2
#define    UF_mdm_base_action_marker_subtype           3

#define UF_mdm_damper_type                       98
#define    UF_mdm_damper_2_links_subtype               6
#define    UF_mdm_damper_slider_subtype                7
#define    UF_mdm_damper_rot_rev_subtype               8
#define    UF_mdm_damper_rot_cyl_subtype               9 /* Represents a damper defined on top of a cylindrical joint */

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

#define UF_machining_operation_type             100        /* Machining operation (includes instanced operations)*/
#define    UF_mach_instanced_oper_subtype              1   /* Obsolete */
#define    UF_mach_orphan_oper_subtype                 2   /* Used for imported CLSF that has no corresponding operation in the part */
#define    UF_mach_oldopr_subtype                     10       /* Obsolete */
#define    UF_mach_pocket_subtype                    110   /* Planar mill profile / pocket operation */
#define    UF_mach_surface_contour_subtype           210   /* Fixed axis surface contouring */
#define    UF_mach_vasc_subtype                      211   /* Variable axis surface contouring */
#define    UF_mach_cavity_milling_subtype            260   /* Cavity Milling */
#define    UF_mach_face_milling_subtype              261   /* Face Milling */
#define    UF_mach_volumn_milling_subtype            262   /* Volume Milling */
#define    UF_mach_zlevel_milling_subtype            263   /* Z-Level Milling */
#define    UF_mach_fb_hole_milling_subtype           264   /* Feature based hole milling */
#define    UF_mach_plunge_milling_subtype            265   /* Plunge milling */
#define    UF_mach_vazl_milling_subtype              266   /* Variable axis Z-Level */
#define    UF_mach_turn_rough_subtype                510   /* Rough Turning */
#define    UF_mach_turn_finish_subtype               520   /* Finish Turning */
#define    UF_mach_turn_teachmode_subtype            530   /* Turn Teachmode */
#define    UF_mach_turn_thread_subtype               540   /* Thread Turning */
#define    UF_mach_turn_cdrill_subtype               550   /* Centerline Drilling */
#define    UF_mach_turn_auxiliary_subtype            560   /* Turn auxiliary */
#define    UF_mach_hole_making_subtype               600   /* Hole making */
#define    UF_mach_wedm_subtype                      700   /* Wire EDM */
#define    UF_mach_mill_ud_subtype                   800   /* User defined milling */
#define    UF_mach_gmc_subtype                       900   /* Generic motion */
#define    UF_mach_probing_subtype                  1000   /* Probing of mill parts */
#define    UF_mach_mill_probing_subtype             1010   /* Unused */
#define    UF_mach_turn_probing_subtype             1020   /* Probing of turned parts */
#define    UF_mach_mill_tool_probing_subtype        1030   /* Probing using a milling tool */
#define    UF_mach_turn_tool_probing_subtype        1040   /* Probing using a turing tool */
#define    UF_mach_robot_gmc_subtype                1050   /* Robot related generic motion */
#define    UF_mach_mill_mc_subtype                  1100   /* Mill machine control */
#define    UF_mach_lathe_mc_subtype                 1200   /* Lathe machine control */
#define    UF_mach_wedm_mc_subtype                  1300   /* Wire EDM machine control */
#define    UF_mach_lathe_ud_subtype                 1400   /* Lathe user defined */
#define    UF_mach_wedm_ud_subtype                  1500   /* Wire EDM user defined */
#define    UF_mach_mass_edit_subtype                1600   /* Operation for mass editing */
#define    UF_mach_thread_milling_subtype           1700   /* Thread milling */
#define    UF_insp_tolerance_subtype                1800
#define    UF_insp_path_subtype                     1900
#define    UF_insp_output_subtype                   2000
#define    UF_insp_misc_subtype                     2100
#define    UF_insp_align_subtype                    2200
#define    UF_insp_sensor_subtype                   2300
#define    UF_insp_construct_subtype                2400
#define    UF_insp_bounding_feature_subtype         2500
#define    UF_insp_feature_subtype                  2600
#define    UF_mach_cylinder_milling_subtype         2700  /* Hole milling */
#define    UF_mach_canned_cycle_subtype             2800
#define    UF_mach_laser_teachmode_subtype          2900  /* Laser teach mode */
#define    UF_mach_hole_drilling_subtype            3000  
#define    UF_mach_groove_milling_subtype           3100  /* Grove milling */
#define    UF_mach_chamfer_milling_subtype          3200  /* Chamfer Milling operation */
#define    UF_mach_radial_groove_milling_subtype    3300  /* Radial Groove Milling Operation */
#define    UF_mach_planar_additive_subtype          3400
#define    UF_mach_generic_feature_subtype          3500  /* Generic (machining) Feature Operation, based on (parametrically defined) manual cut pattern definition */

#define UF_machining_path_type                  101       
#define    UF_machining_path_subtype                   0  /* All tool paths */

#define UF_table_column_type                    102       /* Obsolete */

#define UF_machining_ude_map_type               103       /* Obsolete */
#define    UF_path_udem_subtype                        0 
#define    UF_custom_parameters_map_subtype            1
#define    UF_custom_parameter_subtype                 2

#define UF_data_declaration_type                104       /* Obsolete */

#define UF_machining_geometry_grp_type          105       /* Machining geometry group */
#define    UF_mill_geom_featr_subtype                 10  /* Milling geometry workpiece */
#define    UF_mill_bnd_featr_subtype                  20  /* Boundary geometry */
#define    UF_mill_orient_subtype                     30  /* Mill orientation */
#define    UF_mill_volume_featr_subtype               35  /* Milling feature volume */
#define    UF_turn_geom_subtype                       40  /* Turning geometry */
#define    UF_turn_bnd_subtype                        50  /* Turning boundary */
#define    UF_turn_orient_subtype                     60  /* Turning orientation */
#define    UF_turn_featr_subtype                      65  /* Turning feature */
#define    UF_turn_avoidance_subtype                  67  /* Turning avoidance */
#define    UF_mach_wedm_external_group_subtype        70  /* Wire EDM external */
#define    UF_mach_wedm_internal_group_subtype        80  /* Wire EDM internal */
#define    UF_mach_wedm_open_group_subtype            90  /* Wire EDM open  */
#define    UF_mach_wedm_nocore_group_subtype         100  /* Wire EDM nocore */ 
#define    UF_mach_wedm_feature_group_subtype        110  /* Wire EDM feature */
#define    UF_wedm_orient_subtype                    120  /* Wire EDM orientation */
#define    UF_drill_geom_featr_subtype               130  /* Drill geometry */
#define    UF_ncfeatr_udf_subtype                    140  /* Unused */
#define    UF_ncfeatr_uda_subtype                    150  /* Unused */
#define    UF_fbm_geom_subtype                       160  /* Feature based geometry */
#define    UF_mill_text_featr_subtype                170  /* Text geometry */
#define    UF_blade_featr_subtype                    180  /* Blade geometry */
#define    UF_cylindrical_geometry_subtype           190  /* Hole geometry */
#define    UF_feature_container_subtype              200
#define    UF_cam_feature_subtype                    210
#define    UF_attribute_container_subtype            220

#define UF_machining_mach_tool_grp_type         106        /* Machines in the machine tool view */
#define    UF_machining_mach_subtype                   0   /* Main machine */
#define    UF_machining_mach_turret_subtype            1   /* The subtypes represent the various components of the machine */
#define    UF_machining_mach_pocket_subtype            2   
#define    UF_machining_mach_kim_subtype               3   /* The kinematic model subtype for Machine Tool Builder */
#define    UF_machining_mach_kim_comp_subtype          4   /* Subtype for a kinematic component used when defining a kinematic model */
#define    UF_machining_mach_kim_degof_subtype         5   /* The subtype for an axis as it appears in the kinematic model */
#define    UF_machining_mach_kim_junction_subtype      6   
#define    UF_machining_mach_kim_valuator_subtype      7
#define    UF_machining_mach_sim_kim_pocket_subtype    8
#define    UF_machining_mach_sim_kim_tool_subtype      9
#define    UF_machining_mach_kim_main_subtype         10  /* The main kinematic object in the Machine Tool Builder environment */
#define    UF_machining_mach_kim_display_subtype      11
#define    UF_machining_mach_kim_collision_subtype    12
#define    UF_machining_mach_sim_kim_main_subtype     13  /* The main kinematic object, housing the kinematic model */
#define    UF_machining_mach_sim_kim_gouge_subtype    14
#define    UF_machining_mach_sim_kim_ipw_subtype      17
#define    UF_machining_mach_kim_sinucast_subtype     18  /* The collision avoidance object */
#define    UF_machining_mach_sim_kim_subtype          19  /* The kinematic model subtype as used in simulation */
#define    UF_machining_mach_kim_chain_subtype        20
#define    UF_machining_mach_kim_channel_subtype      21  /* The Kinematic Channel subtype used when defining machine kinematics */
#define    UF_machining_mach_tool_config_subtype      22  /* The machine tool configuration object used for importing archives */
#define    UF_machining_mach_tool_cycle_subtype       23  /* A machine cycle imported by Machine Tool Configuration */
#define    UF_machining_mach_kim_tool_carrier_subtype 24  /* Subtype representing the Tool Carrier used by Machine Tool Configuration */
#define    UF_machining_mach_kim_degof_aux_subtype    25  /* Auxiliary information for an axis imported through Machine Tool Configuration */
#define    UF_machining_mach_kim_channel_aux_subtype  26  /* Auxiliary information for channel information imported through Machine Tool Configuration */
#define    UF_machining_mach_sim_kim_snapshot_subtype 28  /* Snapshot which is stored in a simulation context (IPW e.g.) */ 

           /* machine tool builder object */
#define    UF_machining_mach_mtb_subtype                   15
#define    UF_machining_mach_head_subtype                  16
#define    UF_machining_mach_dyn_ipw_subtype               100
#define    UF_machining_mach_dyn_ipw_turn_subtype          101
#define    UF_machining_mach_dyn_ipw_mill_subtype          102
#define    UF_machining_mach_dyn_ipw_entity_subtype        103
#define    UF_machining_mach_kim_curve2d_subtype           200
#define    UF_machining_mach_kim_line2d_subtype            201
#define    UF_machining_mach_kim_arc2d_subtype             202
#define    UF_machining_mach_selectable_path_subtype       300
#define    UF_machining_mach_dynamic_revolved_body_subtype 301
#define    UF_machining_mach_ipw_subtype                   999

           /* press line simulation objects */
#define    UF_machining_pls_press_model_subtype      400
#define    UF_machining_pls_oper_subtype             401
#define    UF_machining_pls_press_geo_subtype        402
#define    UF_machining_pls_linear_cam_subtype       403
#define    UF_machining_pls_rotary_cam_subtype       404
#define    UF_machining_pls_user_motion_subtype      405
#define    UF_machining_pls_hyd_lifter_subtype       406
#define    UF_machining_pls_sim_control_subtype      407
#define    UF_machining_pls_cntl_col_subtype         408
#define    UF_machining_pls_cshn_cntl_subtype        409
#define    UF_machining_pls_mount_pnt_subtype        410
#define    UF_machining_pls_slide_adjust_subtype     411
#define    UF_machining_pls_cam_drv_subtype          412

           /* nc program manager object */
#define    UF_machining_mach_pm_subtype             1024  /* The nc program manager object */
#define    UF_machining_mach_pm_source_ext_subtype  1025  /* The nc program manager subtype for source from file system */
#define    UF_machining_mach_pm_source_ont_subtype  1026  /* The nc program manager subtype for source from operation navigator */
#define    UF_machining_mach_pm_program_subtype     1027  /* The nc program manager subtype for nc program file */
#define    UF_machining_mach_pm_breakpoint_subtype  1028  /* The nc program manager subtype for breakpoint */

#define UF_machining_parameter_set_type         107        /* Obsolete */
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

#define UF_last_operation_pointer_type          108         /* Obsolete */

#define UF_machining_tool_type                  109         /* Defined tools */
#define    UF_mach_tool_subtype                        0    /* Mill/turning/probing/wedm tools */
#define    UF_mach_tool_wedm_subtype                   1    /* Unused */
#define    UF_mach_tool_assm_subtype                   2    /* Tool assemblies */

#define UF_machining_global_data_type           110         /* Obsolete */

#define UF_machining_geom_type                  111         /* Geometry types for machining operations */
#define    UF_mach_geom_planar_mill_subtype            1    /* Planar milling geometry */
#define    UF_mach_geom_surf_mill_subtype              2    /* Surface contouring geometry */
#define    UF_mach_geom_lathe_subtype                  3    /* Turning geometry */
#define    UF_mach_geom_pnt_to_pnt_subtype             4    /* Point-to-point geometry */
#define    UF_mach_geom_seq_curve_subtype              5    /* Sequential curve mill/lathe geometry */
#define    UF_mach_geom_seq_surf_subtype               6    /* Sequential milling geometry */
#define    UF_mach_geom_face_bnd_subtype               7    /* Face boundary for WEDM */
#define    UF_mach_geom_camgeom_subtype                9    /* Part, drive, check geometry for milling */
#define    UF_mach_geom_cut_level_subtype             11    /* Cut levels for planar/cavity milling */
#define    UF_mach_geom_contain_edge_subtype          12    /* Containment geometry in surface contouring */
#define    UF_mach_geom_feature_subtype               13    /* Feature geometry */
#define    UF_mach_geom_feature_list_subtype          14    /* Feature list geometry */
#define    UF_mach_geom_text_subtype                  15    /* Drafting notes used as machinining geometry */
#define    UF_mach_geom_ipw_subtype                   16    /* In-Process Workpiece */

#define UF_machining_null_grp_type              112         /* Program order group for unused operations */

#define UF_smart_container_type                 113
#define    UF_smart_empty_container_subtype            0
#define    UF_smart_face_container_subtype             1
#define    UF_smart_wireframe_container_subtype        2
#define    UF_smart_body_container_subtype             3
#define    UF_smart_mixed_container_subtype            4
#define    UF_smart_unknown_container_subtype          5
/*   */
#define    UF_smart_sc_section_subtype                  6

#define UF_machining_boundary_member_type       114         /* Boundary entity */
#define    UF_mach_geom_boundary_0_subtype             0    /* Unused */
#define    UF_mach_geom_boundary_subtype               5    /* Boundary created from curves */
#define    UF_mach_geom_face_boundary_subtype          7    /* Boundary created from a face */
#define    UF_mach_geom_camgeom_subtype                9    
#define    UF_mach_geom_camgeom_data_subtype          10

#define UF_machining_master_operation_type      115         /* Master operation data */
#define    UF_mach_wedm_external_trim_subtype          0    /* These subtypes are unused.  Subtypes used are the same as for operation (type 100 */
#define    UF_mach_wedm_internal_trim_subtype          1
#define    UF_mach_wedm_no_core_subtype                2
#define    UF_mach_wedm_open_profile_subtype           3
#define    UF_mach_wedm_cutoff_subtype                 4
#define    UF_mach_wedm_rough_pass_subtype             5
#define    UF_mach_wedm_backburn_subtype               6
#define    UF_mach_wedm_finish_trim_subtype            7
#define    UF_mach_wedm_ext_finish_trim_subtype        8
#define    UF_mach_wedm_subtype                      700

#define UF_machining_post_command_type          116         /* Postprocessor command storage */
#define    UF_machining_mce_startup_subtype            1    /* Start of path machine control events */
#define    UF_machining_mce_endofpath_subtype          2    /* End of path machine control events */
#define    UF_machining_mce_inpath_subtype             3    /* In-path machine control events */
#define    UF_machining_mce_wedm_startup_subtype       4    /* Wire EDM startup commands */
#define    UF_machining_mce_wedm_endofpath_subtype     5    /* Wire EDM end of path commands */
#define    UF_machining_mce_wedm_inpath_subtype        6    /* Wire EDM in-path commands */
#define    UF_machining_mce_mill_mc_subtype            7    /* Mill machine control events */
#define    UF_machining_mce_lathe_mc_subtype           8    /* Lathe machine control events */
#define    UF_machining_mce_wedm_mc_subtype            9    /* Wire EDM machine control events */
#define    UF_machining_mce_number_subtype            10    /* Unused */

#define UF_machining_suboperation               117        
#define    UF_mach_subop_ncm_subtype                  20
#define    UF_mach_subop_ncm_engret_subtype           21
#define    UF_mach_subop_ncm_appdep_subtype           22
#define    UF_mach_subop_ncm_trav_subtype             23
#define    UF_mach_subop_region_subtype               30
#define    UF_mach_subop_region_shape_subtype         31
#define    UF_mach_subop_region_element_subtype       32
#define    UF_mach_subop_blade_subtype                40
#define    UF_mach_subop_containment_subtype          41
#define    UF_mach_subop_floorwall_subtype            42
#define    UF_mach_subop_tool_axis_data_subtype       43
#define    UF_mach_subop_command_subtype              44
#define    UF_tilt_subop_data_subtype                 45
#define    UF_mach_region_manager_subtype             46
#define    UF_work_instruction_subtype                47

#define    UF_mach_manual_move_subtype                100
#define    UF_mach_manual_move_data_subtype           101
#define    UF_insp_move_subtype                       200
#define    UF_insp_move_data_subtype                  201
#define    UF_mach_laser_move_subtype                 300
#define    UF_mach_laser_move_data_subtype            301

#define    UF_mach_delegate_object_subtype            400   /* Storage of data new to an MP release */
#define    UF_machining_path_data_subtype             500  /* Path Data */


#define UF_machining_boundary_type              118         /* Machining boundaries */
#define    UF_mach_geom_boundary_subtype               5    /* Boundary from curves/edges */
#define    UF_mach_geom_camgeom_subtype                9    /* Boundary from faces */

#define UF_machining_control_event_type         119         /* Unused */
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

#define UF_machining_ncm_type                   120         /* Non-cutting moves */
#define    UF_mach_ncm_subtype                        10    /* Non-cutting move data */
#define    UF_mach_ncm_point_subtype                  20    /* Moves to a point */
#define    UF_mach_ncm_engret_subtype                 30    /* Engage/retract data */
#define    UF_mach_ncm_transfer_subtype               40    /* Transfer data */
#define    UF_mach_ncm_clgeom_subtype                 50    /* Clearance geometry */

#define UF_machining_task_type                  121         /* Machining task */
#define    UF_mach_order_task_subtype                160    /* Operation order */
#define    UF_mach_clsf_task_subtype                 161    /* CL-Source files */
#define    UF_mach_optim_task_subtype                162    /* Optimiziation task */
#define    UF_mach_mergepath_task_subtype            163    /* Tool path merge task */
#define    UF_mach_mergepath_subtractive_subtype     164    /* Tool path merge task for subtractive operations */

#define UF_machining_setup_type                 122         /* Manufacturing setup */
#define    UF_mach_setup_subtype                       0    /* CAM Setup */
#define    UF_insp_setup_subtype                      10    /* Inspection Setup */

#define UF_machining_feedrate_type              123         /* Unused */
 
#define UF_machining_display_type               124         /* Unused */

#define UF_machining_dp_type                    125         /* Surface contouring drive method data */
#define    UF_mach_dp_none_subtype                      0   /* Subtypes 0 - 80 unused */
#define    UF_mach_dp_point_subtype                    10   
#define    UF_mach_dp_curve_subtype                    20   
#define    UF_mach_dp_surface_subtype                  30   
#define    UF_mach_dp_boundary_subtype                 40   
#define    UF_mach_dp_tool_path_subtype                50   
#define    UF_mach_dp_radial_curve_subtype             60   
#define    UF_mach_dp_spiral_subtype                   70   
#define    UF_mach_dp_ud_subtype                       80   
#define    UF_mach_dpm_none_subtype                   100   /* Undefined drive method */
#define    UF_mach_dpm_amill_subtype                  110   /* Area milling */
#define    UF_mach_dpm_curve_subtype                  120   /* Curve or point subtype */
#define    UF_mach_dpm_surface_subtype                130   /* Surface Area */
#define    UF_mach_dpm_interpolated_tool_path_subtype 135   /* Streamline */
#define    UF_mach_dpm_boundary_subtype               140   /* Boundary */
#define    UF_mach_dpm_tool_path_subtype              150   /* Input tool path */
#define    UF_mach_dpm_radial_curve_subtype           160   /* Radial curve */
#define    UF_mach_dpm_spiral_subtype                 170   /* Spiral */
#define    UF_mach_dpm_ud_subtype                     180   /* User defined */
#define    UF_mach_dpm_fcut_subtype                   190   /* Flow cut */
#define    UF_mach_dpm_line_subtype                   191
#define    UF_mach_dpm_arc_subtype                    192
#define    UF_mach_dpm_text_subtype                   193   /* Text drive method */
#define    UF_mach_dpm_motions_subtype                194
#define    UF_mach_dpm_contour_subtype                200
#define    UF_mach_dpm_blade_rough_subtype            300   /* Blade rough */
#define    UF_mach_dpm_blade_finish_subtype           400   /* Blade finish */
#define    UF_mach_dpm_hub_finish_subtype             500   /* Hub finish */
#define    UF_mach_dpm_blend_finish_subtype           600
#define    UF_mach_dpm_edge_finish_subtype            700
#define    UF_mach_dpm_rotary_additive_subtype        800   /* Rotary additive */
#define    UF_mach_dpm_3D_free_form_additive_subtype  900   /* 3D Free Form additive */
#define    UF_mach_dpm_tube_rough_subtype            1000   /* Tube rough */
#define    UF_mach_dpm_tube_finish_subtype           1010   /* Tube finish */
#define    UF_mach_dpm_free_form_buildup_additive_subtype    1020   /* Free Form Buildup additive */
#define    UF_mach_dpm_guided_curve_subtype          1030   /* Guided curve for 3x or 5x */     
#define    UF_mach_dpm_tube_additive_thinwall_subtype    1040   /* Tube additive thinwall */
#define    UF_mach_dpm_tube_additive_subtype             1050   /* Tube additive infill */

#define UF_machining_pathindex_type             126
#define    UF_machining_tool_path_subtype               0
#define    UF_machining_contact_path_subtype            1

#define UF_machining_tldsp_type                 127

#define UF_machining_mode_type                  128        /* See methods below */
#define    UF_mach_mode_subtype                        0
#define    UF_mach_mill_mode_subtype                  10
#define    UF_mach_lathe_mode_subtype                 20
#define    UF_mach_drill_mode_subtype                 30
#define    UF_mach_wedm_mode_subtype                  40
#define    UF_mach_turn_mode_subtype                 100

#define UF_machining_mthd_type                  128        /* Machining method group */
#define    UF_mach_mthd_subtype                        0   /* Unused method */
#define    UF_mach_mill_mthd_subtype                  10   /* Mill */
#define    UF_mach_lathe_mthd_subtype                 20   /* Legacy Lathe */
#define    UF_mach_drill_mthd_subtype                 30   /* Point to point */
#define    UF_mach_wedm_mthd_subtype                  40   /* Wire Edm */
#define    UF_mach_turn_mthd_subtype                 100   /* Turning */
#define    UF_mach_hole_mthd_subtype                 110   /* Hole-making */
#define    UF_insp_mthd_subtype                      120   /* Inspection */
#define    UF_mach_laser_mthd_subtype                130   /* Laser cutting */

#define UF_machining_clip_type                  129        /* Machining clipboard */

#define UF_render_set_type                      130

#define UF_sketch_tol_csys_type                 131
#define    UF_sketch_tol_csys_rect_subtype             1
#define    UF_sketch_tol_csys_cyl_subtype              2
#define    UF_sketch_tol_csys_spher_subtype            3

#define UF_sketch_tol_feature_type              132        /* Obsolete in V10 */
#define UF_component2d_definition_type          132        /* Reused in NX9 */

#define UF_sketch_tol_mating_type               133        /* Obsolete in V10 */

#define UF_sketch_type                          134        /* Sketch object */
#define    UF_v9_sketch_subtype                        0  
#define    UF_v13_sketch_subtype                       1
#define    UF_extracted_sketch_subtype                 2   /* Linked Sketch entity */

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
#define    UF_mdm_vforce_subtype                       1    /* Motion Vector Force entity */
#define    UF_mdm_vtorque_subtype                      2    /* Motion Vector Torque entity */
#define    UF_mdm_contact_subtype                      3    
#define    UF_mdm_tire_subtype                         4    /* Motion Tire entity */
#define    UF_mdm_beam_force_subtype                   5    /* Motion Beam Force entity */

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

#define UF_symbol_master_type                   152      /* Obsolete in V10, reused by UF_drafting_break_type */
#define UF_drafting_break_type                  152

#define UF_logic_part_master_type               153      /* Obsolete in V10 */
#define UF_drafting_search_type                 153
#define   UF_drafting_search_criteria_type            0

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
#define    UF_smsp_drafting_attribute_subtype          8

#define UF_symbol_type                          156      /* Obsolete in V10, reused by UF_drafting_body_type */
#define UF_drafting_body_type                   156

#define UF_logic_part_type                      157      /* Obsolete in V10 */
#define UF_drawing_template_region_type              157
#define UF_drawing_template_region_subtype             0

#define UF_smart_model_instance_type            158
#define    UF_combined_attribute_instance_subtype      0
#define    UF_user_defined_attribute_instance_subtype  1
#define    UF_smart_model_instance_mark_subtype        2  /* Obsolete in NX5 */
#define    UF_combined_drafting_instance_subtype       2
#define    UF_user_defined_drafting_instance_subtype   3

#define UF_datum_reference_frame_type           159
#define    UF_single_subtype                           0
#define    UF_composite_subtype                        1

#define UF_constraint_type                      160      /* Was obsolete in V10 as UF_net_type */
#define    UF_constraint_subtype                       0
#define    UF_component_constraint_subtype             1
#define    UF_displayed_constraint_subtype             2
#define    UF_component_constraint_group_subtype       3

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

#define UF_mechatronics_data_type               161  /* The object encapsulating some kind of mechatronics data. */
#define   UF_mechatronics_collision_material_subtype        0  /* A Collision Material defines the material property of objects for physics simulation. */
#define   UF_mechatronics_function_table_subtype            1  /* A Motion Profile is used to define motion profile for a cam constraint. */
#define   UF_mechatronics_function_subtype                  2  /* Defines processes to satisfy the requirements in system engineering. */
#define   UF_mechatronics_sequence_editor_operation_subtype 3  /* Defines an operation which is going to be executed following the time or event sequence defined by the user. */
#define   UF_mechatronics_sequence_editor_trigger_subtype   4  /* Defines a linkage between two operations. */
#define   UF_mechatronics_runtime_behavior_subtype          5  /* Runtime Behavior is a generic runtime behavior that uses CLR code like C# to act with physical objects. */
#define   UF_mechatronics_function_parm_subtype             6  /* Defines the parameters which is used by function object. */
#define   UF_mechatronics_function_comp_container_subtype   7  /* The container owning by function object holds components. */
#define   UF_mechatronics_function_oper_container_subtype   8  /* The container owning by function object holds operations. */
#define   UF_mechatronics_sequence_editor_parameter_subtype 9  /* Defines the parameters which is used by an operation. */
#define   UF_mechatronics_sequence_editor_condition_subtype 10 /* Defines a condition which is going to trigger an operation when it is met. */
#define   UF_mechatronics_logic_subtype                     11 /* Defines interactions to implement the functions in system engineering. */
#define   UF_mechatronics_requirement_subtype               12 /* Defines needs or conditions to meet for a new or altered product in system engineering. */
#define   UF_mechatronics_runtime_formula_subtype           13 /* Runtime Formula objects are able to connect physics runtime properties to a formula. */
#define   UF_mechatronics_adapter_formula_subtype           14 /* Adapter Formula objects are able to connect signals to a formula. */
#define   UF_mechatronics_physics_preference_subtype        15 /* A Physics Preference defines parameters of physics objects and simulation engine. */
#define   UF_mechatronics_physics_folder_object_subtype     16 /* Defines a folder to group several physics objects. */
#define   UF_mechatronics_physics_folder_locator_subtype    17 /* Defines an object to order and locate the folders. */
#define   UF_mechatronics_system_root_subtype               18 /* Defines the root object of a tree structure in system engineering. */
#define   UF_mechatronics_link_manager_subtype              19 /* Defines an object to manage all kinds of linkage between objects in system engineering. */
#define   UF_mechatronics_electrical_part_subtype           20 /* Electrical Part holds the part attributes for communicating with EPLAN. */
#define   UF_mechatronics_runtime_nc_subtype                21 /* Runtime NC objects are able to run Common Simulation Engine with NC file and connect the CSE output events to the MCD objects. */
#define   UF_mechatronics_segment_table_subtype             22 /* Defines a cam profile used for a cam constraint. */
#define   UF_mechatronics_tag_form_subtype                  23 /* Defines a tag form with definitions of parameter type for physics simulation. */
#define   UF_mechatronics_tag_table_subtype                 24 /* A tag table holds a set of data instance of a tag form. */
#define   UF_mechatronics_snap_shot_node_subtype            25 /* Defines an object which stores the simulation data at a given time. */
#define   UF_mechatronics_symbol_table_subtype              26 /* SymbolTable object maintains all Symbols that are used for Signal creating. */
#define   UF_mechatronics_expression_block_formula_subtype  27 /* Expression Block Formula are used to calculate outputs/states based on inputs/params via formula. */
#define   UF_mechatronics_external_signal_configuration_subtype  28 /* Defines external signals for clients (OPC DA, OPC UA, SHM, etc...). */
#define   UF_mechatronics_mcd_signal_server_configuration_subtype  29 /*Defines MCD signals servers (SHM, TCP, UDP, etc..).*/
#define   UF_mechatronics_dynamic_object_table_subtype      30 /* Obsolete in NX12.0.2*/

#define UF_node_type                            162      /* Obsolete in V10 */
#define UF_point_cloud_type                     162      /* Reference Point Cloud (new in NX11.0) */

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

#define UF_fmbd_cut_sheet_subtype                     24
#define UF_fmbd_cut_sheet_row_subtype                 25
#define UF_fmbd_cut_sheet_column_subtype              26
#define UF_fmbd_cut_sheet_header_row_subtype          27
#define UF_fmbd_cut_sheet_cell_subtype                28

#define UF_fmbd_object_attribute_subtype              29
#define UF_fmbd_object_attribute_row_subtype          30
#define UF_fmbd_object_attribute_column_subtype       31
#define UF_fmbd_object_attribute_cell_subtype         32

#define UF_fmbd_pin_list_subtype                     33
#define UF_fmbd_pin_list_row_subtype                 34
#define UF_fmbd_pin_list_column_subtype              35
#define UF_fmbd_pin_list_header_row_subtype          36
#define UF_fmbd_pin_list_cell_subtype                37

#define UF_tabular_hole_table_subtype                38
#define UF_tabular_hole_table_row_subtype            39
#define UF_tabular_hole_table_col_subtype            40

#define UF_bend_table_subtype                        41
#define UF_bend_table_row_subtype                    42
#define UF_bend_table_column_subtype                 43

#define UF_cam_material_type                    166

#define UF_rlist_type                           167
#define    UF_rlist_list_subtype                       1
#define    UF_rlist_format_subtype                     2
#define    UF_rlist_filter_subtype                     3
#define    UF_fmbd_annotation_subtype                  4

#define UF_route_route_type                     168        /* Represents a route or path in the Routing application */
#define    UF_route_wire_subtype                       1   /* Represents a wire in the Routing Electrical application */
#define    UF_route_harness_subtype                    2   /* Represents a harness in the Routing Electrical application */
#define    UF_route_path_subtype                       3   /* Represents a path in the Routing application */
#define    UF_route_path_fmbd_subtype                  4   /* Obsolete */
#define    UF_route_path_offset_subtype                5   /* Obsolete */
#define    UF_route_built_in_path_subtype              6   /* Represents a path built into a component using Qualify Part */
#define    UF_route_cable_subtype                      7   /* Obsolete */
#define    UF_route_jumper_wire_subtype                8   /* Represents a wire that goes from one pin on a connector to another pin on the
                                                              same connector.  In other words, a jumper wire.  Used in the 
                                                              Routing Electrical application */
#define    UF_route_segment_set_subtype                9   /* Represents the object that manages the segments for an overstock. */
#define    UF_route_subroute_subtype                   10   /* Represents the partial path within a Run in Routing Mechanical. */

/*  Analysis objects */
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
#define    UF_surface_intersection_subtype             9
#define    UF_draft_analysis_subtype                   10
#define    UF_trim_angle_check_subtype                 11
#define    UF_local_radius_analysis_subtype            12
#define    UF_mold_flow_moldex3d_subtype               13
#define    UF_face_curvature_subtype                   14
#define    UF_face_analysis_subtype                    15    /* Represents a face analysis object. */
#define    UF_thickness_analysis_subtype               16    /* Wall Thickness Analysis AO */

/* Web Express based Report Writer used in Scenario */
#define UF_report_type                          170
#define     UF_report_scenario_subtype                 0

#define UF_cam_type                             171      /* Obsolete in V10  Reused */
#define UF_shed_material_type                   171      /* NX 6 */

#define UF_cam_body_type                        172      /* Obsolete in V10 - Reused */
#define UF_route_fitting_overstock_type         172      /* Represents an overstock on a fitting */

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
#define    UF_cgfx_material_subtype                    1

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
#define UF_part_field_type                      192      /* Represents a field type in CAE application*/
#define    UF_part_field_connectivity_subtype          0 /* Represents a connectivity field */
#define    UF_part_field_depvariable_subtype           1 /* Represents a dependent variable */
#define    UF_part_field_expression_subtype            2 /* Represents a field using expression */
#define    UF_part_field_formula_subtype               3 /* Represents a formula field */
#define    UF_part_field_link_subtype                  4 /* Represents a link field */
#define    UF_part_field_table_subtype                 5 /* Represents a table field */
#define    UF_part_field_links_table_subtype           6 /* Represents a link table field */
#define    UF_part_field_reference_subtype             7 /* Represents a reference field */
#define    UF_part_field_conditionparam_subtype        8 /* Represents a field for condition parameter */


#define UF_generic_ent_real_sub_ent_type        193      /* Obsolete in V10 */
#define UF_asso_param_object_type               193
#define    UF_asso_param_object_subtype               0
#define    UF_asso_param_object_group_subtype         1

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
#define    UF_zone_display_subtype                     2

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
#define UF_view_alignment_type                  214

#define UF_scalar_type                          215

#define UF_offset_type                          216

#define UF_direction_type                       217

#define UF_parametric_text_type                 218
#define     UF_tabular_note_cell_subtype               2
#define     UF_parts_list_cell_subtype                12
#define     UF_spline_gear_cell_subtype               22

#define UF_xform_type                           219

#define UF_route_control_point_type             220    /* Represents a Routing control point used to connect segments together. */

#define UF_route_port_type                      221    /* Represents a Routing port used to connect components to segments
                                                          or to other components. */

#define UF_route_segment_type                   222     /* Obsolete */
#define UF_mdm_sensor_type                      222     /* Added for Sensor */
#define    UF_mdm_sensor_displacement_subtype          0
#define    UF_mdm_sensor_velocity_subtype              1
#define    UF_mdm_sensor_acceleration_subtype          2
#define    UF_mdm_sensor_force_subtype                 3
#define    UF_mdm_sensor_torque_subtype                4

#define UF_route_connection_type                223     /* Represents a connection between two Routing ports. */

#define UF_route_stock_type                     224       /* Represents various kinds of stock in the Routing applications. */
#define    UF_route_stock_subtype                      0  /* Represents a generic stock in the Routing applications. */
#define    UF_route_overstock_subtype                  1  /* Represents a stock placed over other stocks in the Routing applications. */
#define    UF_route_filler_subtype                     2  /* Represents a stock placed under other stocks in the Routing applications. */
#define    UF_route_stock_transition_subtype           3  /* Represents a stock whose shape transitions in size between two different stocks. */

#define UF_route_part_anchor_type               225     /* Represents an anchor point defined in a component using Qualify Part. */

#define UF_route_cross_section_type             226     /* Represents the cross section of a stock defined in Qualify Part. */

#define UF_route_stock_data_type                227     /* Represents the data that defines a stock, such as diameter, material, etc. */

#define UF_route_corner_type                    228     /* Represents various types of corners used between segments in the Routing applications. */
#define    UF_route_corner_subtype                   999  /* Represents a generic corner of constant radius between two segments. */
#define    UF_route_bend_corner_subtype                0  /* Represents a bend corner between two segments used in the Routing Mechanical application. */
#define    UF_route_miter_corner_subtype               1  /* Represents a miter corner between two segments used in the Routing Mechanical application. */
#define    UF_route_cope_corner_subtype                2  /* Represents a cope corner between two segments used in the Routing Mechanical application. */
#define    UF_route_disc_corner_subtype                3  /* Represents a discontinuity corner between two segments that breaks one stock into two stocks. */
#define    UF_route_sbend_corner_subtype               4  /* Represents a "S" shaped corner between two segments used in the Routing Mechanical application. */

#define UF_route_part_type_type                 229     /* Represents a part qualified as a Routing part. */

#define UF_fam_type                             230
#define    UF_fam_subtype                              0
#define    UF_fam_part_subtype                         1

/*  */

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
#define    UF_fam_attr_mass_subtype                   13
#define    UF_fam_attr_material_subtype               14

#define UF_sfem_mesh_type                       232
#define    UF_sfem_generic_mesh_subtype                0
#define    UF_sfem_trans_mesh_subtype                  1
#define    UF_sfem_mesh_nodes_subtype                  2
#define    UF_sfem_super_element_subtype               3

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
#define UF_mdm_motor_type                       237 /* Added for Motor */
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

#define UF_cs2_vertex_type                      242        /* Vertex object that is created at all control points of a sketch object */

#define UF_cs2_constraint_type                  243        /* Constraint in a sketch */
#define    UF_cs2_simple_subtype                       0   /* Simple constraint that does not require help data such as Fixed, Horizontal etc. */
#define    UF_cs2_dim_subtype                          1   /* Dimensional constraint that does not require help data such as Radial or Angular */
#define    UF_cs2_helped_subtype                       2   /* Constraint that require a help data such as Tangent, Point on Curve etc. */
#define    UF_cs2_dim_helped_subtype                   3   /* Dimensional constraint that require a help data such as Parallel Dimension */
#define    UF_cs2_string_constraint_subtype            4   /* Legacy Point on String constraint - one that existed until NX6 */
#define    UF_cs2_trim_constraint_subtype              5   /* Legacy Associative Trim constraint - one that existed until NX6 */
#define    UF_cs2_offset_constraint_subtype            6   /* Legacy Offset constraint - one that existed until NX5 */
#define    UF_cs2_equation_constraint_subtype          7   /* Perimeter constraint */
#define    UF_cs2_pgm_offset_constraint_subtype        8   /* New Sketch Offset Constraint added in NX5 */
#define    UF_cs2_point_on_loop_subtype                9   /* New Point on String constraint added in NX6 */
#define    UF_cs2_recipe_trim_subtype                  10  /* New Recipe Trim Constraint added in NX6 */
#define    UF_cs2_pattern_constraint_subtype           11  /* Pattern constraint */
#define    UF_cs2_polygon_constraint_subtype           12  /* Polygon constraint */
#define    UF_cs2_pattern_value_constraint_subtype     13  /* Constraint that controls the pitch distance in a Pattern Constraint */
#define    UF_cs2_rigid_set_subtype                    14  /* Sketch Group created with Rigid option */
#define    UF_cs2_g1_constraint_subtype                15  /* G1 continuity constraint on Spline */
#define    UF_cs2_g2_constraint_subtype                16  /* G2 continuity constraint on Spline */
#define    UF_cs2_equal_parameter_subtype              17  /* Constraint that supports Gx continuity constraint between two splines */
#define    UF_cs2_alignment_subtype                    18  /* Horizontal/Vertical alignment constraint between two vertices */
#define    UF_cs2_tangent_to_string_subtype            19  /* Tangent to a string of recipe curves */
#define    UF_cs2_perpendicular_to_string_subtype      20  /* Perpendicular to a string of recipe curves */
#define    UF_cs2_scalable_set_subtype                 21  /* Sketch Group created with Scalable option */

#define UF_cs2_constraint_system_type           244        /* CS2_constraint_system object manages the constraints and geometries in a sketch */
#define    UF_cs2_temporary_cs_subtype                 0   /* Temporary system created Constraint system for generating previews */
#define    UF_cs2_permanent_cs_subtype                 1   /* All user created sketches have CS2 of this subtype */

#define UF_attribute_category_type              245      /* Obsolete in NX7 */
#define UF_attribute_password_type              245      /* Obsolete in NX7 */

#define UF_attribute_type                       246      /* Obsolete in NX7 */
#define    UF_string_attribute_subtype                 1 /* Obsolete in NX7 */       
#define    UF_integer_attribute_subtype                2 /* Obsolete in NX7 */
#define    UF_scalar_attribute_subtype                 3 /* Obsolete in NX7 */
#define    UF_length_attribute_subtype                 4 /* Obsolete in NX7 */
#define    UF_area_attribute_subtype                   5 /* Obsolete in NX7 */
#define    UF_volume_attribute_subtype                 6 /* Obsolete in NX7 */
#define    UF_date_attribute_subtype                   7 /* Obsolete in NX7 */
#define    UF_reference_attribute_subtype              8 /* Obsolete in NX7 */
#define    UF_null_attribute_subtype                   9 /* Obsolete in NX7 */

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

#define UF_leader_type                          252 /* There are no subtypes for this object */

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
