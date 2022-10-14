/*****************************************************************************
             Copyright (c) 1998-2003 Unigraphics Solutions Inc.
                       Unpublished - All Rights Reserved



File Description:

 Open C API interface to the Scenario product.

Overview:
---------
The Scenario module within NX provides Open API
routines to model an existing geometric model using discrete 3D, 2D,
1D, or 0D finite elements. It also has routines for the application of
loads and boundary conditions on to the geometric model. It has a set
of common functions appropriate to the finite element modeling of
various types of geometric models.

Concepts:
---------
A given geometric model can be meshed with appropriate finite
elements in Scenario. Scenario has a solid mesher that meshes using
tetrahedral elements, a shell mesher that meshes using quadrilateral
or triangular elements, 1D mesher for meshing along curves and a 0D
mesher for generating mass elements.

Loads and boundary conditions are applicable only to the geometry.
They are mapped to the corresponding nodes during analysis.

See the Scenario for FEA User Manual for details on meshing the
model geometry (see the Meshing the Model chapter). For details on
application of loads and boundary conditions, see the Loading the
Model section in the Loads and Boundary Conditions chapter.

NXOpen APIs (outside of Open C) are a good resource for Solution and Steps.
Most of the data that defines these objects is dynamically derived from external
sources.  Using JA to Journal the creation of a Solution and SolutionStep is
recommended.

Requirements:
------------
As with any user function, you must first call UF_initialize()
before calling any user function defined in this header.

 End User Functions equivalent to Scenario dialogs:

   Language definition API's:
     UF_SFL_ask_cur_language_nx
     UF_SFL_ask_num_element_descriptors_nx
     UF_SFL_ask_nth_element_descriptor_nx
     UF_SFL_ask_element_descriptor_nx
     UF_SFL_ask_element_descriptor_name_nx
     UF_SFL_ask_num_load_descriptors_nx
     UF_SFL_ask_nth_load_descriptor_nx
     UF_SFL_ask_load_descriptor_nx
     UF_SFL_ask_load_descriptor_name_nx
     UF_SFL_ask_num_bc_descriptors_nx
     UF_SFL_ask_nth_bc_descriptor_nx
     UF_SFL_ask_bc_descriptor_nx
     UF_SFL_ask_bc_descriptor_name_nx
     UF_SFL_ask_num_solution_descriptors_nx
     UF_SFL_ask_nth_solution_descriptor_nx
     UF_SFL_ask_solution_descriptor_nx
     UF_SFL_set_default_env_nx
     UF_SF_ask_language

   Solution and Step:
     UF_SF_ask_num_solutions_nx
     UF_SF_ask_nth_solution_nx
     UF_SF_ask_solution_nx
     UF_SF_ask_active_solution_nx
     UF_SF_ask_active_step_nx
     UF_SF_set_active_solution_and_step_nx
     UF_SF_solution_ask_descriptor_nx
     UF_SF_solution_ask_language_nx
     UF_SF_solution_ask_num_steps_nx
     UF_SF_solution_ask_nth_step_nx
     UF_SF_solution_ask_name_nx
     UF_SF_solution_set_name_nx
     UF_SF_solution_ask_property_count_nx
     UF_SF_solution_ask_property_by_index_nx
     UF_SF_solution_ask_property_nx
     UF_SF_solution_ask_solver_property_count_nx
     UF_SF_solution_ask_solver_property_by_index_nx
     UF_SF_solution_ask_solver_property_nx
     UF_SF_ask_step_nx
     UF_SF_step_ask_name_nx
     UF_SF_step_set_name_nx
     UF_SF_step_ask_property_count_nx
     UF_SF_step_ask_property_by_index_nx
     UF_SF_step_ask_property_nx
     UF_SF_add_to_solution_nx
     UF_SF_add_to_step_nx
     UF_SF_remove_from_solution_nx
     UF_SF_remove_from_step_nx
     UF_SF_locate_solution_loads_nx
     UF_SF_locate_solution_boundary_conditions_nx
     UF_SF_locate_step_loads_nx
     UF_SF_locate_step_boundary_conditions_nx
     UF_SF_locate_named_solution_nx
     UF_SF_locate_named_step_nx
     UF_SF_create_solution_nx
     UF_SF_create_step_nx
     UF_SF_delete_solution_nx
     UF_SF_delete_step_nx

   Scenario Meshers:
     UF_SF_create_0d_mesh
     UF_SF_create_1d_mesh
     UF_SF_create_1d_connection_mesh
     UF_SF_create_weld_mesh
     UF_SF_edit_beam_orientation
     UF_SF_create_edge_face_conn
     UF_SF_create_ugs_2d_mesh --- CAE.Mesh2dBuilder
     UF_SF_create_ugs_2d_mesh_with_hdpts --- CAE.MeshPoint and CAE.Mesh2dBuilder
     UF_SF_create_ugs_2d_mesh_wt_abstraction_control --- CAE.MeshControlBuilder and CAE.Mesh2dBuilder
     UF_SF_get_auto_element_size
     UF_SF_create_ugs_tet_mesh --- CAE.Mesh3dTetBuilder
     UF_SF_create_ugs_tet_mesh_wt_abstraction_control --- CAE.MeshControlBuilder and CAE.Mesh3dTetBuilder
     UF_SF_create_swept_hex_mesh
     UF_SF_ask_ugs_2d_mesh_parms --- CAE.Mesh2dBuild
     UF_SF_ask_ugs_tet_mesh_parms --- CAE.Mesh3dTetBuilder
     UF_SF_auto_create_mesh_mating_condition
     UF_SF_check_model_element_shapes
     UF_SF_ask_num_mesh_recipes
     UF_SF_ask_nth_mesh_recipe

   Section API:
     UF_SF_analyse_solid_section
     UF_SF_analyse_thin_section
     UF_SF_apply_beam_end_mass
     UF_SF_apply_offsets
     UF_SF_ask_beam_end_mass
     UF_SF_ask_mesh_sections
     UF_SF_ask_seciton_offsets
     UF_SF_ask_section_data
     UF_SF_ask_section_prop
     UF_SF_create_section
     UF_SF_edit_section
     UF_SF_free_section_data
     UF_SF_link_section
     UF_SF_locate_named_section
     UF_SF_locate_section
     UF_SF_unlink_section

   Combined Load cases API:
     UF_SF_ask_combined_load_cases
     UF_SF_ask_combined_load_case

   Material
     UF_SF_create_material
     UF_SF_link_material
     UF_SF_locate_material
     UF_SF_locate_named_material
     UF_SF_unlink_material
     UF_SF_ask_library_materials
     UF_SF_ask_material
     UF_SF_ask_material_strength
     UF_SF_ask_material_formability
     UF_SF_ask_material_fatigue
     UF_SF_ask_material_type
     UF_SF_init_matl_prop
     UF_SF_init_formability_prop
     UF_SF_init_fatigue_prop
     UF_SF_init_matl_strength_prop
     UF_SF_free_matl_prop
     UF_SF_free_matl_strength_prop
     UF_SF_free_formability_prop
     UF_SF_free_fatigue_prop
     UF_SF_retrieve_library_material

   SCENARIO MANAGER API:

     UF_SF_create_scenario_nx
     UF_SF_locate_scenarios
     UF_SF_is_scenario_part
     UF_SF_update_scenario

   SIMULATION MANAGER API:

     UF_SF_create_simulation
     UF_SF_simulation_ask_fem
     UF_SF_is_simulation

   FEM MANAGER API:

     UF_SF_create_fem
     UF_SF_create_fem_with_geom_opts
     UF_SF_is_fem
     UF_SF_fem_ask_cad_part

   IDEALIZED PART API:

     UF_SF_idealized_part_ask_master_part
     UF_SF_is_idealized_part

   SIMULATION/FEM/IDEALIZED OBJECT MAPPING:

     UF_SF_map_object_to_current_part

   SFMIDSRF MIDSURFACE API:

     UF_SF_create_offset_midsrf
     UF_SF_edit_offset_midsrf
     UF_SF_is_midsrf
     UF_SF_ask_midsrf_frec_type
     UF_SF_ask_offset_midsrf_thickness
     UF_SF_facepair_ask_midsrf_frec
     UF_SF_ask_midsrf_thickness
     UF_SF_create_userdef_midsrf
     UF_SF_edit_userdef_midsrf
     UF_SF_is_userdef_midsrf
     UF_SF_free_midsrf_user_parms


   IDEALIZE API:
     UF_SF_alloc_idealize_parms
     UF_SF_free_idealize_parms
     UF_SF_ask_idealize_parm_exp
     UF_SF_set_idealize_parm_exp
     UF_SF_ask_idealize_parm_faces
     UF_SF_set_idealize_parm_faces
     UF_SF_alloc_idealize_region
     UF_SF_free_idealize_region
     UF_SF_ask_idealize_region
     UF_SF_create_idealize_body
     UF_SF_create_idealize_region
     UF_SF_ask_idealize_parms
     UF_SF_edit_idealize_parms

     UF_SF_alloc_defeature_parms
     UF_SF_free_defeature_parms
     UF_SF_create_defeature_body
     UF_SF_edit_defeature_parms

   MISCELLANEOUS API:
     UF_SF_set_shell_thickness
     UF_SF_find_mesh
     UF_SF_ask_mesh_visuals
     UF_SF_set_mesh_visuals
     UF_SF_ask_mesh_dimension
     UF_SF_ask_dom_elm_type
     UF_SF_ask_geom_data
     UF_SF_ask_edge_density
     UF_SF_locate_hpt_mg_parents
     UF_SF_count_nodes
     UF_SF_count_elements
     UF_SF_locate_nodes_on_mesh
     UF_SF_locate_nodes_on_element
     UF_SF_locate_element
     UF_SF_locate_element_by_id
     UF_SF_locate_node_by_id
     UF_SF_ask_node
     UF_SF_ask_element
     UF_SF_ask_element_edges
     UF_SF_ask_node_pgeoms
     UF_SF_temp_display_node
     UF_SF_temp_display_element
     UF_SF_locate_nodes_on_geometry
     UF_SF_ask_element_type_names 

   These APIs are retired without replacement:
     UF_SF_ask_node_delta
     UF_SF_set_nodes_delta_by_id
     UF_SF_ask_elem_node_results
     UF_SF_set_elem_node_results
     UF_SF_free_elem_node_results
     UF_SF_get_extreme_values

     UF_SF_partition_body
     UF_SF_partition_body_nx5
     UF_SF_cae_information
     UF_SF_reset_element_ids
     UF_SF_reset_node_ids

     UF_SF_create_hardpoint_on_geom

   SOLVER APIs:

     UF_SF_solve_active_solution_nx

   COMPOSITE OBJECT APIs:
     UF_SF_perform_auto_compositing

   MESH MATING CONDITION APIs
     UF_SF_create_mesh_mating_condition
     UF_SF_delete_mesh_mating_condition
     UF_SF_edit_mesh_mating_condition
     UF_SF_ask_mesh_mating_condition
     UF_SF_locate_mesh_mating_condition_list
     UF_SF_locate_mesh_mating_condition_by_name

   AUTOMATIC FACE PAIR SUBDIVISION APIs
     UF_SF_create_auto_face_subdiv

   DISPLAY OR TRANSIENT MESH APIs
     UF_SF_create_disp_mesh --- retired without replacement
     UF_SF_delete_disp_mesh --- retired without replacement
     UF_SF_display_mesh
     UF_SF_free_disp_mesh   --- retired without replacement

   LEGEND APIs---These APIs are retired without replacement.
     UF_SF_LEGEND_create_legend
     UF_SF_LEGEND_delete_legend
     UF_SF_LEGEND_ask_attribute
     UF_SF_LEGEND_new_attr
     UF_SF_LEGEND_free_attr
     UF_SF_LEGEND_add_index_text_title
     UF_SF_LEGEND_add_title_line
     UF_SF_LEGEND_format_real_to_str

   DURABILITY APIs
     UF_SF_locate_named_dursol_nx
     UF_SF_ask_num_dursols_nx
     UF_SF_ask_nth_dursol_nx
     UF_SF_create_dursol_nx
     UF_SF_delete_dursol_nx
     UF_SF_ask_dursol_nx
     UF_SF_edit_dursol_nx
     UF_SF_dursol_add_load_nx
     UF_SF_dursol_remove_load_nx
     UF_SF_dursol_ask_load_count_nx
     UF_SF_dursol_ask_load_nx
     UF_SF_dursol_locate_all_members_nx
     UF_SF_create_lv_nx
     UF_SF_delete_lv_nx
     UF_SF_ask_lv_nx
     UF_SF_edit_lv_nx

   PROPERTY APIs
     UF_SF_property_ask_name_nx
     UF_SF_property_ask_type_nx
     UF_SF_property_set_value_nx
     UF_SF_property_ask_value_nx

   LANGUAGE SOLUTION APIs
     UF_SFL_solution_descriptor_ask_name_nx
     UF_SFL_solution_descriptor_ask_num_allowable_step_descriptors_nx
     UF_SFL_solution_descriptor_ask_nth_allowable_step_descriptor_nx
     UF_SFL_solution_ask_lbc_desc_valid_nx

   LANGUAGE STEP APIs
     UF_SFL_step_descriptor_ask_name_nx
     UF_SFL_step_ask_lbc_desc_valid_nx

   LANGUAGE SOLVER APIs
     UF_SFL_ask_num_solvers_nx
     UF_SFL_ask_nth_solver_nx
     UF_SFL_ask_solver_nx
     UF_SFL_ask_num_languages_nx
     UF_SFL_ask_nth_language_nx
     UF_SFL_ask_language_nx

   FEM GEOMETRIC ACCESS APIs

     UF_SF_polygon_body_ask_type
     UF_SF_ask_all_polygon_bodies
     UF_SF_body_ask_edges
     UF_SF_body_ask_faces
     UF_SF_body_ask_bounding_box
     UF_SF_body_ask_modl_body
     UF_SF_modl_body_ask_body
     UF_SF_face_ask_edges
     UF_SF_face_ask_body
     UF_SF_face_ask_area
     UF_SF_face_ask_bounding_box
     UF_SF_face_ask_adjacent_faces
     UF_SF_ask_adjacent_faces
     UF_SF_edge_ask_faces
     UF_SF_edge_ask_body
     UF_SF_edge_ask_length
     UF_SF_edge_ask_bounding_box
     UF_SF_edge_ask_adjacent_edges
     UF_SF_edge_ask_end_points
     UF_SF_find_minimum_distance
     UF_SF_ask_closest_point

******************************************************************************/

#ifndef  UF_SF__H_INCLUDED
#define  UF_SF__H_INCLUDED
#include <stdio.h>
#include <uf_defs.h>
#include <uf_sf_types.h>
#include <uf_sf_ugs_mesh.h>
#include <uf_sf_ugopenint.h>
#include <uf_disp.h>
#include <uf_sf_composite.h>
#include <uf_sf_disp_mesh.h>
#include <uf_sf_legend.h>
#include <uf_retiring.h>
#include <uf_sf_lang_names.h>
#include <uf_sf_model_checker.h>
#include <libufun_cae_exports.h>  /* Keep this include always last */



/****************************************************************************

 **************************************************************************/
#define ERROR_UF_SFEM_base     1765000

#define   UF_SF_NOT_INITIALIZED                   (ERROR_UF_SFEM_base)
#define   UF_SF_MESH_DIMENSION_BAD                (ERROR_UF_SFEM_base + 2)
#define   UF_SF_ELM_TYPE_BAD                      (ERROR_UF_SFEM_base + 3)
#define   UF_SF_SECT_TYPE_BAD                     (ERROR_UF_SFEM_base + 4)
#define   UF_SF_SECT_NO_MG                        (ERROR_UF_SFEM_base + 5)
#define   UF_SF_GEOMETRY_TYPE_BAD                 (ERROR_UF_SFEM_base + 6)
#define   UF_SF_NO_MESH_RECIPE                    (ERROR_UF_SFEM_base + 7)
#define   UF_SF_NO_GEOMETRY_TO_MESH               (ERROR_UF_SFEM_base + 8)
#define   UF_SF_MESH_ALREADY_ON_GEOMETRY          (ERROR_UF_SFEM_base + 9)
#define   UF_SF_UPDATE_FAILURE                    (ERROR_UF_SFEM_base + 10)
#define   UF_SF_INVALID_INPUT                     (ERROR_UF_SFEM_base + 11)
#define   UF_SF_MESH_DATA_BAD                     (ERROR_UF_SFEM_base + 12)
#define   UF_SF_NO_SHELL_MESH_TO_SOLID            (ERROR_UF_SFEM_base + 13)

#define   UF_SF_FAILED_TO_CREATE_ORIENTATION      (ERROR_UF_SFEM_base + 20)
#define   UF_SF_INVALID_FACE_TAG                  (ERROR_UF_SFEM_base + 21)
#define   UF_SF_INVALID_SECTION_NAME              (ERROR_UF_SFEM_base + 22)
#define   UF_SF_BLANK_SECTION_NAME                (ERROR_UF_SFEM_base + 23)
#define   UF_SF_INVALID_SECTION_DIMENSIONS        (ERROR_UF_SFEM_base + 24)
#define   UF_SF_SECTION_FAILED_TO_CREATE          (ERROR_UF_SFEM_base + 25)
#define   UF_SF_INVALID_SECTION_NAME_LENGTH       (ERROR_UF_SFEM_base + 26)
#define   UF_SF_INVALID_DUPLICATE_NAME            (ERROR_UF_SFEM_base + 27)
#define   UF_SF_SECTION_FAILED_TO_UPDATE          (ERROR_UF_SFEM_base + 28)
#define   UF_SF_ASKED_NAME_NOT_FOUND              (ERROR_UF_SFEM_base + 29)
#define   UF_SF_INVALID_MATERIAL_NAME             (ERROR_UF_SFEM_base + 30)
#define   UF_SF_BLANK_MATERIAL_NAME               (ERROR_UF_SFEM_base + 31)
#define   UF_SF_INVALID_MATERIAL_VALUES           (ERROR_UF_SFEM_base + 32)
#define   UF_SF_MATERIAL_FAILED_TO_CREATE         (ERROR_UF_SFEM_base + 33)
#define   UF_SF_INVALID_MATERIAL_NAME_LENGTH      (ERROR_UF_SFEM_base + 34)
#define   UF_SF_MATERIAL_FAILED_TO_UPDATE         (ERROR_UF_SFEM_base + 35)
#define   UF_SF_SECTION_FAILED_TO_DELETE          (ERROR_UF_SFEM_base + 36)
#define   UF_SF_INVALID_MATERIAL_TYPE             (ERROR_UF_SFEM_base + 37)
#define   UF_SF_NAS_ANA_S_SUBMIT_ERR              (ERROR_UF_SFEM_base + 38)
#define   UF_SF_NAS_ANA_S_ENV_VAR_ERR             (ERROR_UF_SFEM_base + 39)
#define   UF_SF_NAS_ANA_S_AUTHFILE_VAR_NOT_FOUND  (ERROR_UF_SFEM_base + 40)
#define   UF_SF_NAS_ANA_S_BOUNDARY_CONFLICTS      (ERROR_UF_SFEM_base + 41)
#define   UF_SF_NAS_ANA_S_FORMAT_COMPLETE         (ERROR_UF_SFEM_base + 42)
#define   UF_SF_NULL_TAG_NOT_ALLOWED              (ERROR_UF_SFEM_base + 43)
#define   UF_SF_NO_SECTION_PROPERTY_FOUND         (ERROR_UF_SFEM_base + 44)
#define   UF_SF_SECTION_FAILED_TO_LINK            (ERROR_UF_SFEM_base + 45)
#define   UF_SF_FAILED_TO_CREATE_OFFSET           (ERROR_UF_SFEM_base + 46)
#define   UF_SF_MATERIAL_FAILED_TO_LINK           (ERROR_UF_SFEM_base + 47)
#define   UF_SF_MATERIAL_FAILED_TO_DELETE         (ERROR_UF_SFEM_base + 48)
#define   UF_SF_NO_MATERIAL_FOUND                 (ERROR_UF_SFEM_base + 49)

#define   UF_SF_NO_LOAD_CASE_FOUND                (ERROR_UF_SFEM_base + 51)
#define   UF_SF_INVALID_TAG                       (ERROR_UF_SFEM_base + 52)
#define   UF_SF_ASKED_PROPERTY_NOT_FOUND          (ERROR_UF_SFEM_base + 53)
#define   UF_SF_NON_SCENARIO_PART                 (ERROR_UF_SFEM_base + 54)
#define   UF_SF_INSUFFICIENT_INFO_TO_CREATE_CSYS  (ERROR_UF_SFEM_base + 55)
#define   UF_SF_INVALID_PART_TAG                  (ERROR_UF_SFEM_base + 56)

#define   UF_SF_INVALID_PARAMETER                 (ERROR_UF_SFEM_base + 61)
#define   UF_SF_CLC_UNABLE_TO_CREATE              (ERROR_UF_SFEM_base + 62)
#define   UF_SF_CLC_UNABLE_TO_DELETE              (ERROR_UF_SFEM_base + 63)
#define   UF_SF_ANALYSIS_MODEL_EXISTS             (ERROR_UF_SFEM_base + 64)
#define   UF_SF_MATERIAL_FAILED_TO_UNLINK         (ERROR_UF_SFEM_base + 65)
#define   UF_SF_SECTION_FAILED_TO_UNLINK          (ERROR_UF_SFEM_base + 66)

#define   UF_SF_LANG_NOT_INITIALIZED              (ERROR_UF_SFEM_base + 67)
#define   UF_SF_LANG_ALREADY_DEFINED              (ERROR_UF_SFEM_base + 68)
#define   UF_SF_LANG_NOT_DEFINED                  (ERROR_UF_SFEM_base + 69)
#define   UF_SF_LANG_NOT_COMPLETE                 (ERROR_UF_SFEM_base + 69)
#define   UF_SF_LANG_IS_CURRENT                   (ERROR_UF_SFEM_base + 70)
#define   UF_SF_INVALID_NODE_UNIQUE_TOL           (ERROR_UF_SFEM_base + 71)
#define   UF_SF_BC_CONFLICTS_FOUND                (ERROR_UF_SFEM_base + 72)
#define   UF_SF_INVALID_EDGE_MATCH_TOL            (ERROR_UF_SFEM_base + 73)
#define   UF_SF_REQUESTED_OBJECT_NOT_FOUND        (ERROR_UF_SFEM_base + 74)
#define   UF_SF_INVALID_SMOOTHING_TOL             (ERROR_UF_SFEM_base + 75)
#define   UF_SF_INVALID_ON_SURFACE_TOL            (ERROR_UF_SFEM_base + 76)
#define   UF_SF_INVALID_TRANS_ROWS                (ERROR_UF_SFEM_base + 77)

#define   UF_SF_INVALID_ASSEMBLY_MESH_NAME        (ERROR_UF_SFEM_base + 78)
#define   UF_SF_INVALID_ASSEMBLY_GEOM_TAG         (ERROR_UF_SFEM_base + 79)
#define   UF_SF_INVALID_TARGET_GEOM_TAG           (ERROR_UF_SFEM_base + 80)
#define   UF_SF_INVALID_DUPLICATE_ASSEMBLY_MESH   (ERROR_UF_SFEM_base + 81)
#define   UF_SF_INVALID_AM_MERGE_TOLERANCE        (ERROR_UF_SFEM_base + 82)
#define   UF_SF_INVALID_AM_MATCH_TOLERANCE        (ERROR_UF_SFEM_base + 83)
#define   UF_SF_INVALID_ASSEMBLY_TYPE             (ERROR_UF_SFEM_base + 84)
#define   UF_SF_FAILED_TO_CREATE_ASSEMBLY_MESH    (ERROR_UF_SFEM_base + 85)
#define   UF_SF_INVALID_ASSEMBLY_MESH_TAG         (ERROR_UF_SFEM_base + 86)
#define   UF_SF_FAILED_TO_DELETE_ASSEMBLY_MESH    (ERROR_UF_SFEM_base + 87)
#define   UF_SF_FAILED_TO_LOCATE_ASSEMBLY_MESH    (ERROR_UF_SFEM_base + 88)
#define   UF_SF_FAILED_TO_ASK_ASSEMBLY_MESH       (ERROR_UF_SFEM_base + 89)

#define   UF_SF_AUTO_SUBDIVIDE_FAILED             (ERROR_UF_SFEM_base + 90)
#define   UF_SF_REGIONS_ON_SAME_BODY              (ERROR_UF_SFEM_base + 91)
#define   UF_SF_INCOMPATIBLE_REGIONS              (ERROR_UF_SFEM_base + 92)
#define   UF_SF_CONNECTION_CONFLICT               (ERROR_UF_SFEM_base + 93)
#define   UF_SF_FAILED_TO_AUTOCREATE_MMC          (ERROR_UF_SFEM_base + 94)
#define   UF_SF_INCREASE_MERGE_TOLERANCE          (ERROR_UF_SFEM_base + 95)
#define   UF_SF_FAILED_TO_EDIT_ASSEMBLY_MESH      (ERROR_UF_SFEM_base + 96)

#define   UF_SF_FAILED_TO_CREATE_MIDSURFACE       (ERROR_UF_SFEM_base + 99)
#define   UF_SF_FAILED_TO_EDIT_MIDSURFACE         (ERROR_UF_SFEM_base + 100)
#define   UF_SF_SCENARIO_PART_NOT_FOUND           (ERROR_UF_SFEM_base + 101)

#define   UF_SF_UGS_MESH_INVALID_ELEM_SIZE        (ERROR_UF_SFEM_base + 102)
#define   UF_SF_UGS_MESH_ESIZE_LE_EDGE_MATCH_TOL  (ERROR_UF_SFEM_base + 103)
#define   UF_SF_UGS_MESH_ESIZE_LE_TINY_EDGE_TOL   (ERROR_UF_SFEM_base + 104)
#define   UF_SF_UGS_MESH_INVALID_MIN_FACE_ANGLE   (ERROR_UF_SFEM_base + 105)
#define   UF_SF_UGS_MESH_INVALID_MIDNODE_OPT      (ERROR_UF_SFEM_base + 106)
#define   UF_SF_UGS_MESH_INVALID_MAX_JACOBIAN     (ERROR_UF_SFEM_base + 107)
#define   UF_SF_UGS_MESH_INVALID_SURF_MESH_SIZE_VARIATION (ERROR_UF_SFEM_base + 108)
#define   UF_SF_UGS_MESH_INVALID_VOL_MESH_SIZE_VARIATION  (ERROR_UF_SFEM_base + 109)
#define   UF_SF_UGS_MESH_INVALID_MAX_QUAD_WARP    (ERROR_UF_SFEM_base + 110)
#define   UF_SF_STEP_INVALID_NAME                 (ERROR_UF_SFEM_base + 111)
#define   UF_SF_STEP_NAME_EXIST                   (ERROR_UF_SFEM_base + 112)
#define   UF_SF_INVALID_SCRATCH_DIR               (ERROR_UF_SFEM_base + 113)
#define   UF_SF_ABAQUS_INVALID_SOLVE_OPTION       (ERROR_UF_SFEM_base + 114)
#define   UF_SF_ABAQUS_NO_STEPS_DEFINED           (ERROR_UF_SFEM_base + 115)
#define   UF_SF_ABAQUS_ENV_VAR_ERROR              (ERROR_UF_SFEM_base + 116)
#define   UF_SF_ABAQUS_BC_CONFLICTS               (ERROR_UF_SFEM_base + 117)
#define   UF_SF_ABAQUS_ALL_STEPS_SUPPRESSEd       (ERROR_UF_SFEM_base + 118)
#define   UF_SF_ABAQUS_SUBMIT_ERROR               (ERROR_UF_SFEM_base + 119)
#define   UF_SF_NON_ABAQUS_ENV                    (ERROR_UF_SFEM_base + 120)
#define   UF_SF_UGS_MESH_INVALID_METHOD_OPT       (ERROR_UF_SFEM_base + 121)

#define   UF_SF_HPT_NO_GEOMETRY                   (ERROR_UF_SFEM_base + 122)
#define   UF_SF_HPT_INVALID_REFERENCE_PT          (ERROR_UF_SFEM_base + 123)
#define   UF_SF_HPT_INVALID_GEOMETRY_TYPE         (ERROR_UF_SFEM_base + 124)
#define   UF_SF_POST_INVALID_MODEL                (ERROR_UF_SFEM_base + 125)
#define   UF_SF_POST_RESULTS_NOT_FOUND            (ERROR_UF_SFEM_base + 126)
#define   UF_SF_POST_INVALID_RESULTS_TYPES        (ERROR_UF_SFEM_base + 127)

#define   UF_SF_UNABLE_TO_CREATE_COLLECTOR        (ERROR_UF_SFEM_base + 128)

#define   UF_SF_NO_ACTIVE_SOLUTION                (ERROR_UF_SFEM_base + 129)
#define   UF_SF_INCOMPATIBLE_SOLUTION             (ERROR_UF_SFEM_base + 130)

#define   UF_SF_UNKNOWN_PROPERTY_TYPE             (ERROR_UF_SFEM_base + 131)
#define   UF_SF_PROPERTY_NOT_FOUND                (ERROR_UF_SFEM_base + 132)

#define   UF_NAME_CONFLICT                        (ERROR_UF_SFEM_base + 133)
#define   UF_NAME_INVALID_CHAR                    (ERROR_UF_SFEM_base + 134)
#define   UF_RESULT_FILE_NAME_CONFLICT            (ERROR_UF_SFEM_base + 135)
#define   UF_NAME_TOO_LONG                        (ERROR_UF_SFEM_base + 136)

#define   UF_SF_FAILED_TO_CREATE_LOAD             (ERROR_UF_SFEM_base + 137)
#define   UF_SF_FAILED_TO_CREATE_CONSTRAINT       (ERROR_UF_SFEM_base + 138)

#define   UF_SF_INPUT_OBJECT_NOT_FROM_FEM         (ERROR_UF_SFEM_base + 139)

#define   UF_SF_FAILED                             1

#ifdef __cplusplus
extern "C" {
#endif

 /**************************************************************************
Creates a 0-D mesh  ( zero  dimensional  elements ) over  selected
geometry objects. Concentrated Mass is the only element type
available for 0-D meshing.

Return:
       Return code:
           0 = No error
       not 0 = Error code
               UF_SF_INVALID_INPUT
               UF_SF_NO_MESH_RECIPE
               UF_SF_UPDATE_FAILURE

Environment: Internal  and  External

See Also:

History:
************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_create_0d_mesh(
int num_geom_objects ,/* <I>
                      The number of geometry objects to be meshed
                      */
tag_t* geom_array ,/* <I,len:num_geom_objects>
                   pointer to an array of tags of geometry objects
                   */
UF_SF_0D_element_type_t element_type ,/* <I>
                                      Type of element
                                      UF_SF_0D_CONMASS = Concentrated
                                                         Mass Element
                                      */
double default_density ,/* <I>
                        The element density.
                        */
UF_SF_0D_density_type_t default_density_type ,/* <I>
                                              Default edge density
                                               to the element
                                              UF_SF_0D_EDGE_DENSITY_SIZE =
                                                Default size of the element
                                              UF_SF_0D_EDGE_DENSITY_NUMBER
                                                = Default number of elements
                                              */
double mass_value ,/* <I>
                   Mass value of the element
                   */
tag_t* mesh_tag /* <O>
                 Tag of the mesh created
                 */
);

 /**************************************************************************
Creates a 0-D mesh  ( zero  dimensional  elements ) over  selected
geometry objects. Concentrated Mass is the only element type
available for 0-D meshing. This function is different from the above in that
this function takes into account the distribute mass parameter

Return:
       Return code:
           0 = No error
       not 0 = Error code
               UF_SF_INVALID_INPUT
               UF_SF_NO_MESH_RECIPE
               UF_SF_UPDATE_FAILURE

Environment: Internal  and  External

See Also:

History:
************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_create_0d_mesh_dist_mass(
int num_geom_objects ,/* <I>
                      The number of geometry objects to be meshed
                      */
tag_t* geom_array ,/* <I,len:num_geom_objects>
                   pointer to an array of tags of geometry objects
                   */
UF_SF_0D_element_type_t element_type ,/* <I>
                                      Type of element
                                      UF_SF_0D_CONMASS = Concentrated
                                                         Mass Element
                                      */
double default_density ,/* <I>
                        The element density.
                        */
UF_SF_0D_density_type_t default_density_type ,/* <I>
                                              Default edge density
                                               to the element
                                              UF_SF_0D_EDGE_DENSITY_SIZE =
                                                Default size of the element
                                              UF_SF_0D_EDGE_DENSITY_NUMBER
                                                = Default number of elements
                                              */
double mass_value ,/* <I>
                   Mass value of the element
                   */
int distribute_mass ,/* <I>
                   Whether the mass is distributed among the elements
                   */
tag_t* mesh_tag /* <O>
                 Tag of the mesh created
                 */
);

/**************************************************************************
Creates a one dimensional (1D) mesh over selected geometry objects.
One dimensional elements are defined as two noded elements. The
element types available for 1-D meshing are: Bar, Beam, Rod,
Spring, and  Rigid Link.

Environment: Internal  and  External

See Also:

History:
************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_create_1d_mesh(
UF_SF_1d_mesh_data_t* mesh_data ,/* <I>
                                 pointer to the structure UF_SF_1d_mesh_data_t
                                 */
UF_SF_orientation_data_t* orient_data ,/* <I>
                                       pointer to the structure
                                       UF_SF_orientation_data_t. Pass NULL for
                                       default orientation.
                                       */
int num_group1_objects ,/* <I>
                        Number of geometry objects in group1
                        */
tag_t* group1_array ,/* <I,len:num_group1_objects>
                     pointer to an array of tags to the group1 objects
                     */
int num_group2_objects ,/* <I>
                        Number of geometry objects in group2
                        */
tag_t* group2_array ,/* <I,len:num_group2_objects>
                     pointer to an array of tags to group2 objects
                     */
tag_t* mesh_tag /* <O>
                 Tag of the mesh created
                 */
);

 /**************************************************************************
Creates a one dimensional (1D) mesh over two groups of selected geometry
objects. One dimensional elements are defined as two noded elements. The
element types available for 1-D meshing are: Bar, Beam, Rod, Spring, and
Rigid Link.

NOTE: This is the same as UF_SF_create_1d_mesh except for the additional
      direction arguments.  This allows the user to create connection
      meshes between edges and specify the correct directions.  These additional
      arguments are not needed if num_group2_objects == 0, or if the items in
      group2 are points.

Environment: Internal  and  External

See Also:

History:
************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_create_1d_connection_mesh(
UF_SF_1d_mesh_data_t* mesh_data ,/* <I>
                                 pointer to the structure UF_SF_1d_mesh_data_t
                                 */
UF_SF_orientation_data_t* orient_data ,/* <I>
                                       pointer to the structure
                                       UF_SF_orientation_data_t. Pass NULL for
                                       default orientation.
                                       */
int num_group1_objects ,/* <I>
                        Number of geometry objects in group1
                        */
tag_t* group1_array ,/* <I,len:num_group1_objects>
                     pointer to an array of tags to the group1 objects
                     */
UF_SF_mesh_geom_meshdir_p_t group1_direction_array ,/* <I,len:num_group1_objects>
                     pointer to an array of directions for group1_array.
                     Must be either UF_SF_MG_MESHDIR_FROM_START or
                     UF_SF_MG_MESHDIR_FROM_END.  Not needed if
                     num_group2_objects == 0
                     */
int num_group2_objects ,/* <I>
                        Number of geometry objects in group2
                        */
tag_t* group2_array ,/* <I,len:num_group2_objects>
                     pointer to an array of tags to group2 objects
                     */
UF_SF_mesh_geom_meshdir_p_t group2_direction_array ,/* <I,len:num_group2_objects>
                     pointer to an array of directions for group2_array.
                     Must be either UF_SF_MG_MESHDIR_FROM_START or
                     UF_SF_MG_MESHDIR_FROM_END
                     */
tag_t* mesh_tag /* <O>
                 Tag of the mesh created
                 */
);

/*****************************************************************************

Creates weld (1D) mesh over selected geometry objects.
weld elements are defined as two noded elements. The
element types available for 1-D meshing are: Bar, Beam, Rod,
Spring, and  Rigid Link.

Environment: Internal  and  External

See Also:

History:
************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_create_weld_mesh(
   UF_SF_1d_mesh_data_t* mesh_data , /* <I>
                                     UF_SF_1d_mesh_data_t
                                     */
   UF_SF_orientation_data_t* orient_data , /* <I>
                                           Pass NULL for default orientation
                                           not required.
                                           */
   int num_objects ,                       /* <I>
                               Number of points/curves.
                                           */
   tag_t* obj_array ,                      /* <I,len:num_objects>
                                            Array of tags to the points/curves.
                                           */
   int num_top_faces ,                     /* <I>
                                           Number of top polygon faces.
                                           */
   tag_t* top_face_array ,                 /* <I,len:num_top_faces>
                                           Array of tags to the top polygon faces.
                                           */
   int num_bot_faces ,                     /* <I>
                                           Number of bottom polygon faces.
                                           */
   tag_t* bot_face_array ,                 /* <I,len:num_bottom_faces>
                                           Array of tags to the bottom polygon faces.
                                           */
   tag_t* mesh_tag                         /* <O>
                                           Tag of new mesh.
                                           */
   );


/**************************************************************************
Given a bar/beam mesh and the orientation data this function updates
the mesh to the new orientation.

Environment: Internal  and  External

See Also:

History:
*****************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_edit_beam_orientation (
tag_t mesh_tag ,/* <I>
                Tag to a bar/beam mesh  to update orientation.
                */
UF_SF_orientation_data_t* orient_data /* <I>
                                     Mesh orientation data.
                                     */
);

/*****************************************************************************
This user function is used to compute auto-element size for polygon bodies.

Environment: Internal and External
*******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_get_auto_element_size
(
    int     num_objects, /*<I>  No of bodies in objects_p array*/
    tag_p_t objects_p,   /*<I>  list of bodies from which to calculate auto size*/
    double  *esize       /*<O>  Auto size value */
);

/*****************************************************************************
 *
 *  FUNCTION
 *      UF_SF_check_model_element_shapes
 *
 *  DESCRIPTION
 *      This function performs element shape check for the
 *      meshes passed in and writes the results to a file
 *      or appends at the end of an existing file.
 *
 *
 *  RETURN
 *    error == 0.
 *            >0 for error
 ******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_check_model_element_shapes
(
    int num_meshes,                    /*<I> Length of the mesh_tags array.*/
    tag_t mesh_tags[],                 /*<I,len:num_meshes> Array of mesh tags*/
    logical list_all_elems,            /*<I> TRUE/FALSE whether to list shape
                                             check result for all elements in
                                             respective meshes. */
    const char *output_file_with_path, /*<I> Name with path of output file.
                                             NULL if file_to_append_to is
                                             specified in arguement below. */
    FILE       *file_to_append_to       /*<I> Append output to end of the alteady
                                             opened file. The file must be opened
                                             in append mode.
                                             NULL if output_file_with_path specified. */
);


/******************************************************************************
Returns sections associated to the input mesh recipe or geometry
object such as a curve/edge or point.

The input mesh_object has to belong to a FEM part

Environment: Internal  and  External

See Also:

History:
******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_locate_section(
tag_t mesh_object ,/* <I>
                   Tag to mesh recipe or geometry object. Can
                   be a mesh_recipe, a curve/edge, or a point.
                   */
tag_t* section_tag /* <O>
                    Section tag or NULL_TAG if no section
                    found.  This must be freed by calling
                    UF_SF_free_section_data
                    */
);

/******************************************************************************
Given a tag to a UF_SF_property of subtype section, and a tag to a
edge/curve or point, finds the mesh_geometry and looks at the
mesh_geometry for an existing section property. If it is not the input
section, unlinks the old section and links the input section to the
mesh_recipe.

Environment: Internal  and  External

See Also:

History:
******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_link_section(
tag_t section_tag ,/* <I>
                   The tag of section property.
                   */
tag_t  mesh_geom_tag  /* <I>
                       Tag of the the 1D mesh, edge/ curve or point
                       to which section is to be attached.
                       */
);

/******************************************************************************
Unlinks the section from the object.

Environment: Internal  and  External

See Also:

History:
******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_unlink_section(
tag_t section_tag ,/* <I>
                   The tag of section property.
                   */
tag_t  mesh_geom_tag  /* <I>
                       Tag of the the 1D mesh, edge/ curve or point
                       to which section is to be attached.
                       */
);

/******************************************************************************
Given a name of a section, returns the section tag associated to the
name in the work part.

Environment: Internal  and  External

See Also:

History:
*****************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_locate_named_section(
char* section_name ,/* <I>
                    Section name string
                    */
tag_p_t  section_tag_ptr  /* <O>
                          Tag of the section attached to
                          object.
                          */
);




/*****************************************************************************
Applies end mass values to entities selected.

Environment: Internal  and  External

See Also:

History:
****************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_apply_beam_end_mass(
char* end_a_nsm_exp ,/* <I>
                     Beam end A mass expression
                     */
char* end_b_nsm_exp ,/* <I>
                     Beam end B mass expression
                     */
int num_items ,/* <I>
               Number of items to associate mass.
               */
tag_p_t   items_array /* <I,len:num_items>
                       Tags of items to associate end mass
                       Items can be edges or 1D mesh
                       */
);

/*****************************************************************************
Given a mesh tag, this function gets end A and end B mass values
associated with the object.

Environment: Internal  and  External

See Also:

History:
*****************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_ask_beam_end_mass(
tag_t object_tag ,/* <I>
                  Tag to mesh or mesh recipe
                  */
double* end_a_nsm ,/* <O>
                  End A nonstructural mass value
                  */
double* end_b_nsm /* <O>
                  End B nonstructural mass value
                 */
);

/*************************************************************************
Finds all the combined load cases in the given scenario part. If passed
NULL_TAG for part_tag then current work part will be traversed.

Environment: Internal  and  External

See Also:

History:
**************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_ask_combined_load_cases (
tag_t part_tag ,/* <I>
                part to retrieve from, NULL_TAG for
                current work part
                */
int*    num_clcs ,/* <O>
                  Number of combined load case sets found in
                  the current scenario part.
                  */
tag_t** clc_tags  /* <OF,len:num_clcs>
                  pointer to the pointer to the array of the tag
                  for the combined load cases. pass in NULL
                  if no allocation is desired.  If NULL is not passed in,
                  this array must be freed by calling UF_free.
                  */
);

/************************************************************************
Retrieves the definition of combined load case.

Environment: Internal  and  External

See Also:

History:
**************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_ask_combined_load_case (
tag_t  clc_tag ,/* <I>
                Tag of the combined load case.
                */
char** clc_name ,/* <OF>
                 Name of the combined load case.  This must be freed by
                 calling UF_free.
                 */
int* num_comps ,/* <O>
                Number of load cases in the combined load
                case definition.
                */
tag_t**  lbc_tags ,/* <OF,len:num_comps>
                   pointer to the pointer to the array of the
                   tags for load case components.  This must be freed by
                   calling UF_free.
                   */
double** lbc_scales  /* <OF,len:num_comps>
                     pointer to the pointer to the array of the
                     scale factors for load case components.  This must
                     be freed by calling UF_free.
                     */
);

/*************************************************************************
Creates a combined load case with a given name and definition.

Valid only when the work part is a Simulation.

Environment: Internal  and  External

See Also:

History:
**************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_create_combined_load_case (
char* clc_name ,/* <I>
                Name of the combined load case.
                */
int num_comps ,/* <I>
               Number of load cases in the combined load
               case definition.
               */
tag_t*  lbc_tags ,/* <I,len:num_comps>
                  pointer to the array of the tags for load case
                  components.
                  */
double* lbc_scales ,/* <I,len:num_comps>
                    pointer to the array of the scale factors for
                    load case components.
                    */
tag_t* clc_tag  /* <O>
                Tag of the combined load case.
                */
);

/****************************************************************************
Applies shell thickness to 2D meshes.

Valid only when the work part is a FEM

Environment: Internal  and  External

See Also:

History:
****************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_set_shell_thickness(
const char* shell_thick_exp ,/* <I>
                       Shell thickness value
                       */
int num_items ,/* <I>
               Number of items to associate shell thickness.
               */
tag_t* items_array  /* <I,len:num_items>
                    pointer to the array of 2D mesh tags.
                    */
);

 /**************************************************************************
Finds the dimension of the input mesh or mesh recipe namely
UF_SF_DIMENSION_0D for 0D mesh,  UF_SF_DIMENSION_1D
for 1D mesh, UF_SF_DIMENSION_2D for shell mesh or
UF_SF_DIMENSION_3D for Solid mesh.

Environment: Internal  and  External

See Also:

History:
************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_ask_mesh_dimension(
tag_t mesh_recipe ,/* <I>
                   Tag to mesh recipe or  mesh
                   */
UF_SF_mesh_dimension_t* dimension /* <O>
                                   The dimensionality of this mesh_recipe
                                   */
);

/**************************************************************************
Finds the dominant element type of the input mesh recipe.  For
example if the dimension of a mesh is 1D, the dominant element type
can be a beam or bar or a spring.  In case of 2D meshes the dominant
element type is UF_SF_QUAD4,  though couple of triangular
elements may get created in creating 2D mesh.

Environment: Internal  and  External

See Also:

History:
************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_ask_dom_elm_type (
tag_t mesh_recipe ,/* <I>
                   Tag to mesh recipe or  mesh
                   */
UF_SF_element_type_t* elm_type /* <O>
                                The dominant element type of this
                                mesh_recipe.
                                */
);

/**************************************************************************
Returns geometry data from given  mesh or mesh recipe.

Environment: Internal  and  External

See Also:

History:
 ***************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_ask_geom_data(
tag_t mesh_object ,/* <I>
                   Tag of the mesh
                   */
UF_SF_mesh_geom_usage_t usage_type ,/* <I>
                                    Type of usage
                                    (UF_SF_mesh_geom_usage_t) - refer to
                                    uf_sf_types.h
                                    */
int* num_geom_items ,/* <O>
                     Number of geometry items.
                     */
tag_t** geom_items_p /* <OF,len:num_geom_items>
                      pointer to list of tags to geometry items.  If the
                      number of geometry items is > 0, then this array must
                      be freed by calling UF_free.
                      */
);

/**************************************************************************---
Gets a number of edge densities given an input object. The edge
density is defined as the number of elements to be created along the
input object. There are two cases:  If elements exist, this function
returns the current number of elements. If elements do not exist, this
function gets the edge density attribute for this object and returns the
number of elements which would be created.  The valid types of input
objects are UF_line_type, UF_circle_type, UF_conic_type,
UF_spcurve_type,  UF_caegeom_edge_subtype.

Environment: Internal  and  External

See Also:

History:
 ***************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_ask_edge_density (
tag_t object_tag ,/* <I>
                  Tag of object to query.
                  */
UF_SF_edge_density_data_t* edge_density_data_ptr /* <O>
                                                  pointer to
                                                  UF_SF_edge_density_data_t
                                                  where the edge_density data
                                                  will be stored.
                                                  */
);

/**************************************************************************---
Locates all meshes related to the input object.

Environment: Internal  and  External

See Also:

History:
***************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_find_mesh(
tag_t object_tag ,/* <I>
                  Tag to input entity, group, load, boundary
                  condition, mesh_recipe, element or node.
                  */
UF_SF_mesh_dimension_t dimension ,/* <I>
                                  UF_SF_mesh_dimension_t of desired mesh
                                  recipe when object_tag is a mesh or
                                  element,This argument should be
                                  UF_SF_DIMENSION_ANY since only a
                                  single recipe is possible.
                                  */
int* num_of_meshes ,/* <O>
                    The number of meshes being returned.
                    Could be zero.
                    */
tag_t** mesh_items_p  /* <OF,len:num_of_meshes>
                      pointer to an array of mesh tags or NULL.  This
                      array must be freed by calling UF_free.
                      */
);

/**************************************************************************---
Given a mesh tag returns its visual properties.

Environment: Internal  and  External

See Also:

History:
***************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_ask_mesh_visuals(
tag_t mesh_tag ,/* <I>
                The tag of the mesh
                */
UF_SF_mesh_visuals_t* mesh_vis /* <O>
                                Structure to mesh visual properties.
                                */
);

/**************************************************************************
Sets a mesh's visual attributes.

Environment: Internal  and  External

See Also:

History:
***************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_set_mesh_visuals(
tag_t mesh_tag ,/* <I>
                The tag of the mesh
                */
UF_SF_mesh_visuals_t* mesh_vis /* <O>
                                Structure to mesh visual properties.
                                Set members to UF_SF_MESH_VISUAL_NO_CHANGE
                                whose attribute you do not want to change.
                                */
);

/******************************************************************************
Given a tag to a smart point, locate the parents whose mesh geometry
has to be updated.

Environment: Internal  and  External

See Also:

History:
*******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_locate_hpt_mg_parents(
tag_t point_tag ,/* <I>
                 Tag to a hard point.
                 */
int* parent_cnt ,/* <O>
                 Number of parents tags related to the point.
                 */
tag_p_t* parent_list  /* <OF,len:parent_cnt>
                      pointer to an array of parent tags.  This array must
                      be freed if parent_cnt is greater than 0.
                      */
);

/**************************************************************************
Creates scenario part file from parent part (non scenario part file).
The input name should be shorter than 26 characters and should not
include the path name. This is required because the scenario subdirectory
is associated to the master model part.

Environment: Internal  and  External

See Also:

History: Originally released in NX3.0
*********************************************************************/
extern UFUN_CAEEXPORT int UF_SF_create_scenario_nx(
const char* scenario_name ,/* <I>
                     Name of Scenario part file to create.
                     */
tag_t* new_scenario_tag /* <O>
                         Tag of created Scenario part file.
                         */
);

 /**************************************************************************---
Checks whether the current part file is a Scenario type part or not.

Return:
         Return code:
           0 =  Scenario part
          UF_SF_NON_SCENARIO_PART =not a Scenario part.

Environment: Internal  and  External

See Also:

History:
 ***************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_is_scenario_part ( void );

/**************************************************************************
Switches between two scenarios.

Environment: Internal  and  External

See Also:

History:Written in V17.0
*********************************************************************/
extern UFUN_CAEEXPORT int UF_SF_switch_scenarios(
char     *scenario_1_name, /* <I> Name of first  scenario */
char     *scenario_2_name  /* <I> Name of second scenario */
);

/**************************************************************************
Locates all scenario parts and finds names of Scenario parts in the
current working  part.

Environment: Internal  and  External

See Also:

History:
*************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_locate_scenarios(
int*  number_of_scenarios ,/* <O>
                           Number of Scenario part files found.
                           */
char*** scenario_names  /* <OF,len:number_of_scenarios>
                        pointer to array of names of Scenario part
                        files. Maximum name size of each Scenario
                        part file is 24 characters.  This array must be
                        freed by calling UF_free_string_array.
                        */
);

/****************************************************************************
Creates either an isotropic, orthotropic, anisotropic or fluid material, with,
or without table properties, with, or without read-only constraints.

Initialize the UF_SF_material_prop_p_t, property_values structure using
UF_SF_init_matl_prop before setting new values.

Environment: Internal  and  External

See Also: html#UF_SF_init_matl_prop and
 html#UF_SF_free_matl_prop

History:
**************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_create_material    (
char* name ,/* <I>
            Name of material.  The maximum
            number of allowable characters is 80.
            */
char* category ,/* <I>
                Category of material, pass NULL if it is
                not required
                */
UF_SF_neutral_material_types_t material_type ,/* <I>
                                              The type of material to create.
                                              UF_SF_MATERIAL_ISOTROPIC =
                                              Isotropic material.
                                              UF_SF_MATERIAL_ORTHOTROPIC
                                              = Orthotropic material,
                                              UF_SF_MATERIAL_ANISOTROPIC
                                              = Anisotropic material.
                                              UF_SF_MATERIAL_FLUID
                                              = Fluid material.
                                              */
UF_SF_material_prop_p_t property_values ,/* <I>
                                         Input structure with Youngs modulus,
                                         poissons ratio, Mass density, Thermal
                                         conductivity, and Thermal Coefficient.
                                         Call "UF_SF_init_matl_prop" to
                                         initialize this structure before
                                         setting new values.
                                         */
UF_SF_library_material_t library_material ,/* <I>
                                           UF_SF_MATL_IS_READ_ONLY
                                           UF_SF_MATL_IS_EDITABLE
                                           */
tag_p_t material_tag /* <O>
                      Created material tag.
                      */
);

/*******************************************************************************
Given a tag to an object, this function returns the material tag
associated to the object.

Environment: Internal  and  External

See Also:

History:
*******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_locate_material(
tag_t object_tag ,/* <I>
                  The tag of object.
                  */
tag_t* material_tag /* <O>
                     Tag of the material attached to the object.
                     */
);

/*******************************************************************************
Given a tag to a material property, and a tag to a mesh or geometry,
this function checks the mesh or geometry for an existing material
property. If there is any material already present then it unlinks the
old material and links the input material. The valid objects are only
meshes or mesh recipes.

Environment: Internal  and  External

See Also:

History:
*******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_link_material(
tag_t material_tag ,/* <I>
                    The tag of material.
                    */
tag_t  object_tag /* <I>
                    Tag of the object to which material is to be
                    attached.
                    */
);

/**************************************************************************-----
Given a name of material, this function returns the material tag
associated to the name.

Environment: Internal  and  External

See Also:

History:
*******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_locate_named_material(
char* material_name ,/* <I>
                     Material name string.
                     The maximum number of allowable
                     characters is 80.
                     */
tag_p_t  material_tag_ptr /* <O>
                           Tag of the material attached to object.
                           */
);

/*******************************************************************************
Given and a tag to a mesh or geometry,  this function unlinks the
material from the object.

Environment: Internal  and  External

See Also:

History:
*******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_unlink_material(
tag_t  object_tag /* <I>
                    Tag of the object to which material is
                    attached.
                  */
);

/*******************************************************************************
    This routine looks up the type of a material.  The following types
    are supported in NX:

    UF_SF_MATERIAL_ISOTROPIC   -  isotropic.
    UF_SF_MATERIAL_ORTHOTROPIC -  orthotropic.
    UF_SF_MATERIAL_ANISOTROPIC -  anisotropic.
    UF_SF_MATERIAL_FLUID       -  fluid.

Environment: Internal  and  External

History: Originally released in V16.0
*******************************************************************************/
extern UFUN_CAEEXPORT   int  UF_SF_ask_material_type
    (
        tag_t                             material_tag,
                                          /* <I> Tag of the material */
        UF_SF_neutral_material_types_p_t  material_type
                                          /* <O> Material Type */
    );

/*******************************************************************************
Gets all the material properties such as Young's Modulus, poisson's
Ratio, Mass Density, Thermal Coefficient, Thermal Conduct, Heat
Capacity, Thermal Density and Convection Coefficient.  If any  one of
the above properties has not been applied on the material then the
corresponding value will be UF_SF_FREE_VALUE.

The UF_SF_material_prop_t, property_values must be initialized using
UF_SF_init_matl_prop.

Environment: Internal  and  External

See Also: UF_SF_init_matl_prop and
 UF_SF_free_matl_prop

History:
*******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_ask_material (
tag_t  material_tag ,/* <I>
                     Tag of the material.
                     */
char** material_name ,/* <OF>
                      Material name string.  pass in NULL if not
                      required. This must be freed by calling UF_free.
                      */
UF_SF_material_prop_t* property_values /* <OF,free:UF_SF_free_matl_prop>
                                        Structure containing material properties. 
                                        Pass in NULL if not required.
                                        The structure  must be
                                        initialized using UF_SF_init_matl_prop.
                                        Call UF_SF_free_matl_prop to free the
                                        storage allocated within the structure.
                                        */
);

/*******************************************************************************
Gets the plastic range material properties; Yield Strength and
Ultimate Tensile Strength.  If either one of the above properties has not
been applied on the material then the corresponding value will
be UF_SF_FREE_VALUE.

Environment: Internal  and  External

See Also: html#UF_SF_free_matl_strength_prop
 html#UF_SF_init_matl_strength_prop

History: This function was originally released in V19.1
*******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_ask_material_strength (
tag_t  material_tag ,/* <I>
                     Tag of the material.
                     */
UF_SF_material_strength_prop_p_t property_values
                                    /* <OF,free:UF_SF_free_matl_strength_prop>
                                        Structure containing material strength
                                        properties.  The structure should be
                                        allocated by the user, but data within
                                        the structure is dynamically allocated.
                                        Call html#UF_SF_free_matl_strength_prop
                                        to free the storage allocated within
                                        the structure.
                                        */
);


/*******************************************************************************
Gets the formability material properties; Work Hardening, Flow and
Stress Strain.  If any one of the above properties has not
been applied on the material then the corresponding value will
be UF_SF_FREE_VALUE.

Environment: Internal  and  External

See Also: html#UF_SF_free_formability_prop
 html#UF_SF_init_formability_prop

History: This function was originally released in V19.1
*******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_ask_material_formability (
tag_t  material_tag ,/* <I>
                     Tag of the material.
                     */
UF_SF_material_formability_prop_p_t property_values
                                    /* <OF,free:UF_SF_free_formability_prop>
                                        Structure containing material
                                        formability properties.
                                        The structure should be
                                        allocated by the user, but data within
                                        the structure is dynamically allocated.
                                        Call html#UF_SF_free_formability_prop
                                        to free the storage allocated within
                                        the structure.
                                        */
);

/*******************************************************************************
Gets the fatigue material properties; fatigue strength coefficient, fatigue
strength exponent, fatigue ductility coefficient, fatigue ductility exponent.
If any one of the above properties has not been applied on the material then
the corresponding value will be UF_SF_FREE_VALUE.

Environment: Internal  and  External

See Also: html#UF_SF_free_fatigue_prop
 html#UF_SF_init_fatigue_prop

History: This function was originally released in V20.0
*******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_ask_material_fatigue (
tag_t  material_tag ,/* <I>
                     Tag of the material.
                     */
UF_SF_material_fatigue_prop_p_t property_values
                                    /* <OF,free:UF_SF_free_fatigue_prop>
                                        Structure containing material
                                        fatigue properties.
                                        The structure should be
                                        allocated by the user, but data within
                                        the structure is dynamically allocated.
                                        Call html#UF_SF_free_fatigue_prop
                                        to free the storage allocated within
                                        the structure.
                                        */
);

/******************************************************************************
  UF_SF_add_material_strength:

  Add plastic range properties to the material.
******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_add_material_strength (
UF_SF_material_strength_prop_p_t property_values,
                                    /* <I>
                                        Structure containing material strength
                                        properties.  The structure should be
                                        allocated by the user, but data within
                                        the structure is dynamically allocated.
                                        Call html#UF_SF_free_matl_strength_prop
                                        to free the storage allocated within
                                        the structure.
                                        */
tag_t  material_tag /* <I>
                     Tag of the material.
                     */
);

/******************************************************************************
  UF_SF_add_material_fatigue:

  Add fatigue properties to the material.
******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_add_material_fatigue (
UF_SF_material_fatigue_prop_p_t property_values,
                                    /* <I>
                                        Structure containing material strength
                                        properties.  The structure should be
                                        allocated by the user, but data within
                                        the structure is dynamically allocated.
                                        Call html#UF_SF_free_matl_strength_prop
                                        to free the storage allocated within
                                        the structure.
                                        */
tag_t  material_tag /* <I>
                     Tag of the material.
                     */
);

/******************************************************************************
  Given a material tag and optionally name, categary, lib_reference and
  property_values, this function will update a material.

  Note that the type of the material cannot be updated.
  Rather, delete and create a new material.

  Returns:                                Completion status.
                                          =0 successful completion
                                          = SFMAT_INVALID_MATERIAL_NAME
                                          = SFMAT_INVALID_DUPLICATE_NAME
                                          = SFMAT_INVALID_TYPE
                                          = SFMAT_MATERIAL_FAILED_TO_UPDATED
                                          >0 error
******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_update_material
(
tag_t   material_tag,                  /*<I> The tag of material to be updated.*/
char*   name_str,                      /*<I> Pointer to string representing the
                                             the name to be given to the material.
                                       */
char*   category_str,                  /*<I>Pointer to string representing the
                                            the Category to be given to the
                                            material.
                                       */
char*   lib_reference,                 /*<I> Pointer to string representing the
                                             the library reference to be given
                                             to the material.
                                       */
UF_SF_material_prop_p_t
                       property_values /*<I> Contains the material property
                                             values.
                                       */
);

/******************************************************************************
  Similar to UF_SF_update_material but updates the strength material
  object only.
****************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_update_strength
(
tag_t                       material_tag,  /*<I> The tag of material to be updated.
                                                 May be the PHYS_MAT or SFMAT object
                                           */
UF_SF_material_strength_prop_p_t
                         property_values   /*<I> Contains the material strength property
                                                 values.
                                           */
);

/******************************************************************************
  Similar to UF_SF_update_material but updates the fatigue material
  object only.

*****************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_update_fatigue
(
tag_t                         material_tag, /* <I> The tag of material to be updated.
                                                   May be the PHYS_MAT or SFMAT object.
                                            */
UF_SF_material_fatigue_prop_p_t
                           property_values  /* <I> Contains the material strength
                                                   property values.
                                            */
);

/*******************************************************************************
Initializes pointers associated to the structure UF_SF_material_prop_t. Should
be called before using the structure to make sure the structure is properly
initialized.  Note that the type of each member of the structure will be
defaulted to expression.

Environment: Internal  and  External

See Also:

History: This function was originally released in V16.0
*******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_init_matl_prop (
UF_SF_material_prop_p_t property_values /* <I/O>
                                        Structure, whose members are to be
                                        initialized
                                        */
);

/*******************************************************************************
Initializes pointers associated to the structure UF_SF_material_strength_prop_t.
Should be called before using the structure to make sure the structure is
properly initialized.
Note that the type of each member of the structure will be defaulted to
expression.

Environment: Internal  and  External

See Also: html#UF_SF_free_matl_strength_prop

History: This function was originally released in V19.1
*******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_init_matl_strength_prop (
UF_SF_material_strength_prop_p_t property_values /* <I/O>
                                        Structure whose members are to be
                                        initialized
                                        */
);

/*******************************************************************************
Initializes pointers associated to the structure
UF_SF_material_formability_prop_t.
Should be called before using the structure to make sure the structure is
properly initialized.
Note that the type of each member of the structure will be defaulted to
expression.

Environment: Internal  and  External

See Also: html#UF_SF_free_formability_prop

History: This function was originally released in V19.1
*******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_init_formability_prop (
UF_SF_material_formability_prop_p_t property_values /* <I/O>
                                        Structure whose members are to be
                                        initialized
                                        */
);

/*******************************************************************************
Initializes pointers associated to the structure
UF_SF_material_fatigue_prop_t.
Should be called before using the structure to make sure the structure is
properly initialized.
Note that the type of each member of the structure will be defaulted to
expression.

Environment: Internal  and  External

See Also: html#UF_SF_free_fatigue_prop

History: This function was originally released in V19.1
*******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_init_fatigue_prop (
UF_SF_material_fatigue_prop_p_t property_values /* <I/O>
                                        Structure whose members are to be
                                        initialized
                                        */
);

/*******************************************************************************
Cleans up dynamic storage associated to a UF_SF_material_prop_t.
The structure UF_SF_material_prop_t must have been fully initialized using
UF_SF_init_matl_prop.

Environment: Internal  and  External

Returns:
       There is no return code.

See Also: html#UF_SF_init_matl_prop

History:
*******************************************************************************/
extern UFUN_CAEEXPORT void UF_SF_free_matl_prop (
 UF_SF_material_prop_t* property_values /* <I>
                                         pointer to the UF_SF_material_prop_t
                                         structure
                                         */
);/* <NEC> */


/*******************************************************************************
Cleans up dynamic storage associated to a UF_SF_material_prop_t.
The structure UF_SF_material_prop_t must have been fully initialized using
UF_SF_init_matl_strength_prop.


Environment: Internal  and  External

Returns:
       There is no return code.

See Also: html#UF_SF_init_matl_strength_prop

History: This function was originally released in V19.1
*******************************************************************************/
extern UFUN_CAEEXPORT void UF_SF_free_matl_strength_prop (
 UF_SF_material_strength_prop_p_t property_values /* <I>
                                         pointer to the
                                         UF_SF_material_strength_prop_t
                                         structure
                                         */
);/* <NEC> */


/*******************************************************************************
Cleans up dynamic storage associated to a UF_SF_material_prop_t.
The structure UF_SF_material_prop_t must have been fully initialized using
UF_SF_init_formability_prop.

Environment: Internal  and  External

Returns:
       There is no return code.

See Also: html#UF_SF_init_formability_prop

History: This function was originally released in V19.1
*******************************************************************************/
extern UFUN_CAEEXPORT void UF_SF_free_formability_prop (
 UF_SF_material_formability_prop_p_t property_values /* <I>
                                         pointer to the
                                         UF_SF_material_formability_prop_t
                                         structure
                                         */
);/* <NEC> */

/*******************************************************************************
Cleans up dynamic storage associated to a UF_SF_material_fatigue_prop_t.
The structure UF_SF_material_fatigue_prop_t must have been fully initialized using
UF_SF_init_fatigue_prop.

Environment: Internal  and  External

Returns:
       There is no return code.

See Also: html#UF_SF_init_fatigue_prop

History: This function was originally released in V19.1
*******************************************************************************/
extern UFUN_CAEEXPORT void UF_SF_free_fatigue_prop (
 UF_SF_material_fatigue_prop_p_t property_values /* <I>
                                         pointer to the
                                         UF_SF_material_fatigue_prop_t
                                         structure
                                         */
);/* <NEC> */


/*******************************************************************************
Counts nodes in a mesh. If mesh_tag is NULL_TAG, counts all nodes
in the current part.

Environment: Internal  and  External

See Also:

History:
*******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_count_nodes(
tag_t mesh ,/* <I>
            The tag of mesh.  If passed NULL_TAG
            then all meshes in the current part will be
            traversed
            */
int* number_of_nodes  /* <O>
                      Number of nodes found.
                      */
);
/*******************************************************************************
Counts number of all nodes of valid elements of current solver in the current part.

Environment: Internal and External

See Also:

History: Originally released in NX11.0
*******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_count_all_nodes_of_valid_elements(
    int* number_of_all_valid_nodes  /* <O>
                                    Number of all valid nodes found.
                                    */
);


/*******************************************************************************
Counts number of elements in a mesh. If mesh_tag is NULL_TAG,
counts all elements in the current part.

Environment: Internal  and  External

See Also:

History:

 *************************************************************************------*/
extern UFUN_CAEEXPORT int UF_SF_count_elements(
tag_t mesh ,/* <I>
            The tag of mesh.  If passed NULL_TAG
            then all meshes in the current part will be
            traversed
            */
int* number_of_elements  /* <O>
                         Number of elements found.
                         */
);

/*******************************************************************************
Counts number of all valid elements of current solver in the current part.

Environment: Internal  and  External

See Also:

History: Originally released in NX11.0

*************************************************************************------*/
extern UFUN_CAEEXPORT int UF_SF_count_all_valid_elements(
int* number_of_all_valid_elements  /* <O>
                                   Number of valid elements found.
                                   */
);


/**************************************************************************-----
Locates all nodes in a mesh.

If the given mesh tag is from a Simulation part or given a NULL_TAG and the
current work part is a Simulation part then node occurrences from that
Simulation part are returned.  Similarly if the given mesh tag is from a
FEM part or given a NULL_TAG and the current work part is a FEM part then
nodes from that FEM part are returned.

Environment: Internal  and  External

See Also:

History:
*************************************************************************------*/
extern UFUN_CAEEXPORT int UF_SF_locate_nodes_on_mesh (
tag_t mesh_tag ,/* <I>
                Mesh tag, pass in NULL_TAG to locate all
                nodes in current part.
                */
int* num_of_nodes ,/* <O>
                   The number of nodes. Could be zero.
                   */
tag_t** node_tags_p  /* <OF,len:num_of_nodes>
                     pointer to an array of node tags or NULL if
                     the number of nodes is zero.  This array must
                     be freed by calling UF_free.
                     */
);

/**************************************************************************-----
Locates the elements on a mesh if object is mesh tag. If object is a
node tag then parent element of node will be given as output. If there
are no elements , then returns num_of_elements = 0 and
element_tags_not =  NULL.

If the given mesh or node occurrence is from the Simulation part then
element occurrences associated with that mesh or node occurrence in the
Simulation part are returned.  Similarly if the given mesh or node is
from the FEM part then the elements associated with that mesh or node
in the FEM part are returned.

Environment: Internal  and  External

See Also:

History:
*************************************************************************------*/
extern UFUN_CAEEXPORT int UF_SF_locate_element (
tag_t mesh_tag ,/* <I>
                Mesh tag or Node tag
                */
int* num_of_elements ,/* <O>
                      The number of elements. Could be zero.
                      */
tag_t** element_tags_p  /* <OF,len:num_of_elements>
                        pointer to an array of element tags or NULL
                        if the number of elements is zero.  This array
                        must be freed by calling UF_free.
                        */
);

/**************************************************************************-----
Locates the nodes on a element. If there are no nodes, then returns
num_of_nodes = 0 and node_tags_not = NULL.

If given an element occurrence tag then node occurrences in the owning Simulation
part are returned. Similarly if the given an element tag then nodes in the owning
FEM part are returned.

Environment: Internal  and  External

See Also:

History:
*************************************************************************------*/
extern UFUN_CAEEXPORT int UF_SF_locate_nodes_on_element (
tag_t element_tag ,/* <I>
                   Element tag.
                   */
int* num_of_nodes ,/* <O>
                   The number of node. Could be zero.
                   */
tag_t** node_tags_p  /* <OF,len:num_of_nodes>
                     pointer to an array of node tags or NULL.  This
                     array must be freed by calling UF_free.
                     */
);

/*******************************************************************************
Finds an element entity's attributes.  These are the element id,
adaptivity, dimension and neutral type.

Environment: Internal  and  External

See Also:

History:
*******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_ask_element (
tag_t elm_tag ,/* <I>
               Element tag.
               */
int* elm_id ,/* <O>
             ID number of element
             */
UF_SF_elm_adaptivity_type_t* adaptivity ,/* <O>
                                         Element adaptivity.
                                         */
UF_SF_elm_dimension_type_t* dimension ,/* <O>
                                       Dimension of element ( 0D,
                                       1D, 2D or 3D )
                                       */
UF_SF_element_type_t* element_type  /* <O>
                                    Type of element .
                                    */
);

/*******************************************************************************
Finds a node entity's attributes.  These are the node id, boundary type,
element type, and absolute position.

Environment: Internal  and  External

See Also:

History:
*******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_ask_node (
tag_t node_tag ,/* <I>
                Node tag.
                */
int* node_id ,/* <O>
              ID number of node.
              */
UF_SF_node_btype_t* b_type ,/* <O>
                            Type of node boundary .
                            */
UF_SF_mid_node_type_t* e_type ,/* <O>
                               Type of mid node.
                               */
double abspos[3]  /* <O>
                node location in absolute
                coordinates.
                */
);

/*******************************************************************************
Given an element tag outputs the number of edges this element has
and the nodes on those edges.

If given an element occurrence tag then node occurrences in the owning Simulation
part are returned. Similarly if the given an element tag then nodes in the owning
FEM part are returned.

Environment: Internal  and  External

See Also:

History:
*******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_ask_element_edges(
tag_t elem_tag ,/* <I>
                The tag of the element
                */
int*    num_edges ,/* <O>
                   Number of edges the element has
                   */
tag_t** start_nodes ,/* <OF,len:num_edges>
                     Array of start nodes on these edges.  This must
                     be freed by calling UF_free.
                     */
tag_t** end_nodes ,/* <OF,len:num_edges>
                   Array of end nodes on these edges.  This must
                     be freed by calling UF_free.
                   */
tag_t** mid_nodes /* <OF,len:num_edges>
                   Array of mid side nodes on these edges, if any.  This must
                     be freed by calling UF_free.
                   */
);

/****************************************************************************
Set the default environment for the FE Model.
The default environment is used when no Solution is active.

Valid only when the work part is a FEM

Environment: Internal  and  External

See Also:

History: Originally released in NX3.0
***************************************************************************/
extern UFUN_CAEEXPORT int UF_SFL_set_default_env_nx (
const char* language_name /* <I>
                          Language name.  The name of the current language.
                          The syntax of the language name is "<solver name> - <analysis type>".
                          For example: "NX NASTRAN - Structural"
                          */
);

/*******************************************************************************
Given the input language_tag, finds its name in language_name. If
language_tag == NULL_TAG, return the name of the current
language. If there is is no current language and language_tag is
NULL_TAG, return "".  Pass NULL against any argument if
corresponding output is not desired.

Environment: Internal  and  External

See Also:

History:
*******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_ask_language (
tag_t language_tag ,/* <I>
                    Tag of the desired language or
                    NULL_TAG. When NULL_TAG, finds
                    the properties of current  language. If
                    there is no current language, returns "" as
                    language name.
                    */
char language_name[UF_SF_LANG_MAX_NAME_BUFSIZE] ,/* <O>
                     pointer to string which will contain the
                     found name or "". pe that this is not
                     dynamic space. A string at least
                     UF_SF_LANG_MAX_NAME_BUFSIZE
                     long is to be passed in.
                     */
int* version ,/* <O>
              The version of the language. If input == NULL, then no
              output is desired or returned.
              */
UF_SF_LANG_analysis_type_t* analysis_type ,/* <O>
                                           The type of analysis this
                                           language represents.
                                           If input == NULL, then no output
                                           is desired or returned.
                                           */
UF_SF_LANG_problem_abstract_t* problem_abstraction ,/* <O>
                                                    The problem abstraction
                                                    this language represents.
                                                    If input == NULL, then
                                                    no output is desired or
                                                    returned.
                                                    */
UF_SF_LANG_linearity_t* linearity ,/* <O>
                                   Linear or non-linear. If input == NULL,
                                   then no output is desired or returned.
                                   */
UF_SF_LANG_time_depend_t* time_dependency ,/* <O>
                                           Steady-state or transient.
                                           If input == NULL, then no output
                                           is desired or returned.
                                           */
char** solver_name /* <OF>
                    The name of the solver to use.
                    If input == NULL, then no output is
                    desired or returned.  If a NULL is not passed in for
                    the solver_name, then the returned value must be freed
                    by calling UF_free.
                    */
);

/****************************************************************************
Returns tag of the current language.  Valid only when a FEM or Simulation
is the work part.  When a Simulation is active, he active Solution defines
the current language. If no Solution is active, then the default environment
defines the current language.  When a FEM is active, the default language of
the FEM is the current language.

Environment: Internal and External

See Also:

History: Originally released in NX3.0
***************************************************************************/
extern UFUN_CAEEXPORT int UF_SFL_ask_cur_language_nx (
tag_t *language_tag /* <O>
                    The tag of the language.
                    */
);

/****************************************************************************
Given a language tag, returns the number of element descriptors.
The element descriptors define what elements are valid for the language.
Valid only when the work part is a FEM or a Simulation.

Environment: Internal and External

See Also:

History: Originally released in NX3.0
***************************************************************************/
extern UFUN_CAEEXPORT int UF_SFL_ask_num_element_descriptors_nx (
tag_t language_tag,        /* <I>
                           Language tag.
                           */
int*  num_elem_descriptors /* <O>
                           The number of element descriptors.
                           */
);

/****************************************************************************
Given a language tag and index into the element descriptor list, returns the
tag of the element descriptor. This function can be used to loop over all
element descriptors in the language.

The number of element descriptors can be obtained from function
UF_SFL_ask_num_element_descriptors_nx.

The index is just a counter.
Valid indices are from 0 to (number of element descriptors-1).

Valid only when the work part is a FEM or a Simulation.

Environment: Internal and External

See Also: UF_SFL_ask_num_element_descriptors_nx

History: Originally released in NX3.0
***************************************************************************/
extern UFUN_CAEEXPORT int UF_SFL_ask_nth_element_descriptor_nx (
tag_t language_tag,        /* <I>
                           Language tag.
                           */
int   index,               /* <I>
                           Index into list of element descriptors.
                           Valid indices are from 0 to (number of element
                           descriptors-1).
                           The number of element descriptors can be obtained
                           from function UF_SFL_ask_num_element_descriptors_nx.
                           */
tag_t *elem_descriptor_tag /* <O>
                           The tag of the element descriptor.
                           */
);

/****************************************************************************
Given a language tag and element descriptor name, returns the tag of the
element descriptor.  Valid only when the work part is a FEM or a Simulation.

Environment: Internal and External

See Also:

History: Originally released in NX3.0
***************************************************************************/
extern UFUN_CAEEXPORT int UF_SFL_ask_element_descriptor_nx (
tag_t       language_tag,        /* <I>
                                 Language tag.
                                 */
const char* name,               /* <I>
                                 Name of the element descriptor.
                                 */
tag_t       *elem_descriptor_tag /* <O>
                                 The tag of the element descriptor.
                                 */
);

/****************************************************************************
Given an element descriptor tag, returns the element descriptor name.
Valid only when the work part is a FEM or a Simulation.

Environment: Internal and External

See Also:

History: Originally released in NX3.0
***************************************************************************/
extern UFUN_CAEEXPORT int UF_SFL_ask_element_descriptor_name_nx (
tag_t   elem_desc_tag, /* <I>
                       The tag of the element descriptor.
                       */
char** name_pp         /* <OF>
                       The name of the element descriptor.
                       NOTE: Caller must UF_free the string.
                       */
);

/****************************************************************************
Given a language tag, returns the number of load descriptors.
The load descriptors define what load types are valid for the language.
Valid only when the work part is a Simulation.

Environment: Internal and External

See Also:

History: Originally released in NX3.0
***************************************************************************/
extern UFUN_CAEEXPORT int UF_SFL_ask_num_load_descriptors_nx (
tag_t language_tag,        /* <I>
                           Language tag.
                           */
int*  num_load_descriptors /* <O>
                           The number of load descriptors.
                           */
);

/****************************************************************************
Given a language tag and index into the load descriptor list, returns the
tag of the load descriptor. This function can be used to loop over all
load descriptors in the language.

The number of load descriptors can be obtained from function
UF_SFL_ask_num_load_descriptors_nx.

The index is just a counter.
Valid indices are from 0 to (number of load descriptors-1).

Valid only when the work part is a Simulation.

Environment: Internal and External

See Also:  UF_SFL_ask_num_load_descriptors_nx

History: Originally released in NX3.0
***************************************************************************/
extern UFUN_CAEEXPORT int UF_SFL_ask_nth_load_descriptor_nx (
tag_t language_tag,        /* <I>
                           Language tag.
                           */
int   index,               /* <I>
                           Index into list of load descriptors.
                           Valid indices are from 0 to (number of load
                           descriptors-1).
                           The number of load descriptors can be obtained
                           from function UF_SFL_ask_num_load_descriptors_nx.
                           */
tag_t *load_descriptor_tag /* <O>
                           The tag of the load descriptor.
                           */
);

/****************************************************************************
Given a language tag and load descriptor name, returns the
tag of the load descriptor.

Valid only when the work part is a Simulation.

Environment: Internal and External

See Also:

History: Originally released in NX3.0
***************************************************************************/
extern UFUN_CAEEXPORT int UF_SFL_ask_load_descriptor_nx (
tag_t       language_tag,        /* <I>
                                 Language tag.
                                 */
const char*  name,              /* <I>
                                 Name of the load descriptor.
                                 */
tag_t       *load_descriptor_tag /* <O>
                                 The tag of the load descriptor.
                                 */
);

/****************************************************************************
Given a load descriptor tag, returns the load descriptor name.

Valid only when the work part is a Simulation.

Environment: Internal and External

See Also:

History: Originally released in NX3.0
***************************************************************************/
extern UFUN_CAEEXPORT int UF_SFL_ask_load_descriptor_name_nx (
tag_t   load_desc_tag, /* <I>
                       The tag of the load descriptor.
                       */
char** name_pp         /* <OF>
                       The name of the load descriptor.
                       NOTE: Caller must UF_free the string.
                       */
);

/****************************************************************************
Given a language tag, returns the number of bc descriptors.
The bc descriptors define what boundary condition types are valid for the
language.

Valid only when the work part is a Simulation.

Environment: Internal and External

See Also:

History: Originally released in NX3.0
***************************************************************************/
extern UFUN_CAEEXPORT int UF_SFL_ask_num_bc_descriptors_nx (
tag_t language_tag,      /* <I>
                         Language tag.
                         */
int*  num_bc_descriptors /* <O>
                         The number of bc descriptors.
                         */
);

/****************************************************************************
Given a language tag and index into the boundary condition (bc) descriptor
list, returns the tag of the bc descriptor. This function can be used to loop
over all bc descriptors in the language.

The number of bc descriptors can be obtained from function
UF_SFL_ask_num_bc_descriptors_nx.

The index is just a counter.
Valid indices are from 0 to (number of bc descriptors-1).

Valid only when the work part is a Simulation.

Environment: Internal and External

See Also:  UF_SFL_ask_num_bc_descriptors_nx

History: Originally released in NX3.0
***************************************************************************/
extern UFUN_CAEEXPORT int UF_SFL_ask_nth_bc_descriptor_nx (
tag_t language_tag,      /* <I>
                         Language tag.
                         */
int   index,             /* <I>
                         Index into list of bc descriptors.
                         Valid indices are from 0 to (number of bc
                         descriptors-1).
                         The number of bc descriptors can be obtained
                         from function UF_SFL_ask_num_bc_descriptors_nx.
                         */
tag_t *bc_descriptor_tag /* <O>
                         The tag of the bc descriptor.
                         */
);

/****************************************************************************
Given a language tag and boundary condition descriptor name, returns the
tag of the boundary condition descriptor.

Valid only when the work part is a Simulation.

Environment: Internal and External

See Also:

History: Originally released in NX3.0
***************************************************************************/
extern UFUN_CAEEXPORT int UF_SFL_ask_bc_descriptor_nx (
tag_t       language_tag,      /* <I>
                               Language tag.
                               */
const char* name,             /* <I>
                               Name of the bc descriptor.
                               */
tag_t       *bc_descriptor_tag /* <O>
                               The tag of the bc descriptor.
                               */
);

/****************************************************************************
Given an boundary condition descriptor tag, returns the boundary condition
descriptor name.

Valid only when the work part is a Simulation.

Environment: Internal and External

See Also:

History: Originally released in NX3.0
***************************************************************************/
extern UFUN_CAEEXPORT int UF_SFL_ask_bc_descriptor_name_nx (
tag_t  bc_desc_tag, /* <I>
                    The tag of the bc descriptor.
                    */
char** name_pp      /* <OF>
                    The name of the bc descriptor.
                    NOTE: Caller must UF_free the string.
                    */
);

/****************************************************************************
Given a language tag, returns the number of solution descriptors.
The solution descriptors define what solution types are valid for the
language.

Valid only when the work part is a Simulation.

Environment: Internal and External

See Also:

History: Originally released in NX3.0
***************************************************************************/
extern UFUN_CAEEXPORT int UF_SFL_ask_num_solution_descriptors_nx (
tag_t language_tag,            /* <I>
                               Language tag.
                               */
int*  num_solution_descriptors /* <O>
                               The number of solution descriptors.
                               */
);

/****************************************************************************
Given a language tag and index into the solution descriptor list, returns the
tag of the solution descriptor. This function can be used to loop over all
solution descriptors in the language.

The number of solution descriptors can be obtained from function
UF_SFL_ask_num_solution_descriptors_nx.

The index is just a counter.
Valid indices are from 0 to (number of solution descriptors-1).

Valid only when the work part is a Simulation.

Environment: Internal and External

See Also:  UF_SFL_ask_num_solution_descriptors_nx

History: Originally released in NX3.0
***************************************************************************/
extern UFUN_CAEEXPORT int UF_SFL_ask_nth_solution_descriptor_nx (
tag_t language_tag,            /* <I>
                               Language tag.
                               */
int   index,                   /* <I>
                               Index into list of solution descriptors.
                               Valid indices are from 0 to (number of solution
                               descriptors-1).
                               The number of solution descriptors can be obtained
                               from function UF_SFL_ask_num_solution_descriptors_nx.
                               */
tag_t *solution_descriptor_tag /* <O>
                               The tag of the solution descriptor.
                               */
);

/****************************************************************************
Given a language tag and solution descriptor name, returns the
tag of the solution descriptor.  The solution descriptor name
appears as "Analysis Type" on the "Create Solution" dialog.

Alternatively, one can call UF_SFL_ask_num_solution_descriptors_nx,
UF_SFL_ask_nth_solution_descriptor_nx, and then
UF_SFL_solution_descriptor_ask_name_nx to find the name for each solution
descriptor.

Valid only when the work part is a Simulation.

Environment: Internal and External

See Also:

History: Originally released in NX3.0
***************************************************************************/
extern UFUN_CAEEXPORT int UF_SFL_ask_solution_descriptor_nx (
tag_t       language_tag,            /* <I>
                                     Language tag.
                                     */
const char* name,                   /* <I>
                                     Name of the solution descriptor.
                                     */
tag_t       *solution_descriptor_tag /* <O>
                                     The tag of the solution descriptor.
                                     */
);

/*******************************************************************************
Returns the tag of the active solution.

Valid only when the work part is a Simulation.

Use UF_SF_ask_num_solutions_nx, UF_SF_ask_nth_solution_nx or UF_SF_solution_ask_name_nx
to see what solutions are in the part.  A call to UF_SF_set_active_solution_and_step_nx 
will make the solution active.

Environment: Internal  and  External

See Also:

History: Originally released in NX3.0
*******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_ask_active_solution_nx (
tag_t *active_solution     /* <O>
                           Pointer to the tag of the active
                           solution for the scenario part.
                           */
);


/*******************************************************************************
Returns the tag of the active step.

Valid only when the work part is a Simulation.

Environment: Internal  and  External

See Also:

History: Originally released in NX3.0
*******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_ask_active_step_nx (
tag_t *active_step     /* <O>
                       Pointer to the tag of the active
                       step for the scenario part.
                       */
);


/*******************************************************************************
Set the active solution and step.  The step must belong to the solution.

Valid only when the work part is a Simulation.

Environment: Internal  and  External

See Also:

History: Originally released in NX3.0
*******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_set_active_solution_and_step_nx (
tag_t active_solution,     /* <I>
                           Tag of the active solution for the scenario part.
                           */
tag_t active_step          /* <I>
                           Tag of the active step which belongs to the above
                           solution.
                           */
);

/*******************************************************************************
Get the descriptor for a existing solution.

Environment: Internal  and  External

See Also:

History: Originally released in NX3.0
*******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_solution_ask_descriptor_nx(
tag_t solution,   /* <I>
                   Tag of the solution.
                   */
tag_t* descriptor /* <O>
                   Tag of the descriptor.
                   */
);

/*******************************************************************************
Query the number of solutions.

Valid only when the work part is a Simulation.

Environment: Internal  and  External

See Also:

History: Originally released in NX3.0
*******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_ask_num_solutions_nx (
int    *solution_count    /* <O>
                          Number of solutions.
                          */
);


/*******************************************************************************
Given a index into a list of solutions, returns the tag of the solution. This
function can be used to loop over all solutions.

The number of solutions can be obtained from function
UF_SF_ask_num_solutions_nx.

The index is just a counter.
Valid indices are from 0 to (number of solutions-1).

Valid only when the work part is a Simulation.

Environment: Internal  and  External

See Also:  UF_SF_ask_num_solutions_nx

History: Originally released in NX3.0
*******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_ask_nth_solution_nx (
int solution,     /* <I>
                  Index of the solution to query.
                  Valid indices are from 0 to (number of solutions-1).
                  */
tag_t *solution_tag     /* <O>
                        Tag of the solution.
                        */
);


/*******************************************************************************
Query the number of steps.

Environment: Internal  and  External

See Also:

History: Originally released in NX3.0
*******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_solution_ask_num_steps_nx (
tag_t solution_tag,     /* <I>
                        Tag of the solution.
                        */
int    *step_count    /* <O>
                      Number of steps.
                      */
);


/*******************************************************************************
Given a solution and an index into the list of steps for the solution, returns
the tag of the step. This function can be used to loop over all steps in a
solution.

The number of steps can be obtained from function
UF_SF_solution_ask_num_steps_nx.

The index is just a counter.
Valid indices are from 0 to (number of steps-1).

Environment: Internal  and  External

See Also:  UF_SF_solution_ask_num_steps_nx

History: Originally released in NX3.0
*******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_solution_ask_nth_step_nx (
tag_t solution_tag,     /* <I>
                        Tag of the solution.
                        */
int step,               /* <I>
                        Index of the step to query.
                        Valid indices are from 0 to (number of steps-1).
                        */
tag_t *step_tag         /* <O>
                        Tag of the step.
                        */
);

/***************************************************************************
Adds loads or boundary conditions to the active solution. This function
needs to be  called after creating load or boundary condition.

Environment: Internal  and  External

See Also:
History: Originally released in NX3.0
****************************************************************************/
extern UFUN_CAEEXPORT  int  UF_SF_add_to_solution_nx(
            int      num_of_lbc, /*<I>
                                 Number of loads or boundary conditions to
                                 add to the active solution.
                                 */
            tag_t    *lbc        /*<I>
                                 pointer to array of tags for loads or
                                 boundary conditions.
                                 */
                                );

/***************************************************************************
Adds loads or boundary conditions to the active step. This function needs to be
called after creating load or boundary condition.

Functions to return load tags are UF_SF_locate_solution_loads_nx and
UF_SF_locate_step_loads_nx.

Environment: Internal  and  External

See Also:

History: Originally released in NX3.0
****************************************************************************/
extern UFUN_CAEEXPORT  int  UF_SF_add_to_step_nx(
                                  int      num_of_lbc,/*<I>
                                                      Number of loads or boundary conditions to
                                                      add to the active step.
                                                      */
                                  tag_t    *lbc       /*<I>
                                                      Pointer to array of tags for loads or
                                                      boundary conditions.
                                                      */
                                );


/***************************************************************************
Removes the specified number of loads and boundary conditions from
the active solution.

Environment: Internal  and  External

See Also:

History: Originally released in NX3.0
****************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_remove_from_solution_nx(
int num_of_lbc ,/* <I>
                Number of loads and boundary conditions.
               */
tag_t*  lbc /* <I>
            Pointer to the array of tags for  loads or
            boundary conditions.
            */
);


/***************************************************************************
Removes the specified number of loads and boundary conditions from
the active step.

Environment: Internal  and  External

See Also:

History: Originally released in NX3.0
****************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_remove_from_step_nx(
int num_of_lbc ,    /* <I>
                    Number of loads and boundary conditions.
                    */
tag_t*  lbc         /* <I>
                    Pointer to the array of tags for loads or
                    boundary conditions.
                    */
);

/***************************************************************************
Locates the loads in a solution.  Does not locate loads
in steps contained by the solution (see: UF_SF_locate_step_loads_nx).
The membs_pp pointer is undefined if num_members is zero.

Environment: Internal  and  External

See Also:  UF_SF_locate_step_loads_nx

History: Originally released in NX3.0
****************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_locate_solution_loads_nx(
tag_t solution ,/* <I>
                Tag of the solution.
                */
int *num_members ,/* <O>
                 Number of loads in the solution.
                 */
tag_t** membs_pp  /* <OF>
                  The pointer to the array of the tags of the loads.
                  If num_members is zero, this pointer should not be used.
                  If num_members is > 0, then this array must be freed by
                  calling UF_free.
                  */
);

/***************************************************************************
Locates the boundary conditions in a solution.  Does not locate
boundary conditions in steps contained by the solution (see:
UF_SF_locate_step_boundary_conditions_nx).
The membs_pp pointer is undefined if num_members is zero.

Environment: Internal  and  External

See Also:  UF_SF_locate_step_boundary_conditions_nx

History: Originally released in NX3.0
****************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_locate_solution_boundary_conditions_nx(
tag_t solution ,/* <I>
                Tag of the solution.
                */
int *num_members ,/* <O>
                 Number of boundary conditions in the solution.
                 */
tag_t** membs_pp  /* <OF>
                  The pointer to the array of the tags of the boundary conditions.
                  If num_members is zero, this pointer should not be used.
                  If num_members is > 0, then this array must be freed by calling
                  UF_free.
                  */
);


/***************************************************************************
Locates the loads in a step.
The membs_pp pointer is undefined if num_members is zero.

Environment: Internal  and  External

See Also:

History: Originally released in NX3.0
****************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_locate_step_loads_nx(
tag_t step, /* <I>
            Step tag.
            */
int *num_members,/* <O>
                 Number of loads in the step.
                 */
tag_t** membs_pp  /* <OF>
                  The pointer to the array of the tags of the loads.
                  If num_members is zero, this pointer should not be used.
                  If num_members is > 0, then this array must be freed by
                  calling UF_free.
                  */
);


/***************************************************************************
Locates the boundary conditions in a step.
The membs_pp pointer is undefined if num_members is zero.

Environment: Internal  and  External

See Also:

History: Originally released in NX3.0
****************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_locate_step_boundary_conditions_nx(
tag_t step, /* <I>
            Step tag.
            */
int *num_members,/* <O>
                 Number of boundary conditions in the step.
                 */
tag_t** membs_pp  /* <OF>
                  The pointer to the array of the tags of the boundary conditions.
                  If num_members is zero, this pointer should not be used.
                  If num_members is > 0, then this array must be freed by calling
                  UF_free.
                  */
);


/***************************************************************************
Given the tag of a solution, this function finds the name of the solution.

Environment: Internal  and  External

See Also:

History: Originally released in NX3.0
****************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_solution_ask_name_nx(
tag_t  solution ,/* <I>
                 Tag of the solution.
                 */
char solution_name[MAX_LINE_BUFSIZE]  /* <O>
                     Name of the solution.
                     The buffer must be declared using MAX_LINE_BUFSIZE so it can hold MAX_LINE_NCHARS characters.
                     */
);

/***************************************************************************
Given the tag of a step, this function finds the name of the step.

Environment: Internal  and  External

See Also:

History: Originally released in NX3.0
****************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_step_ask_name_nx(
tag_t  step ,    /* <I>
                 Step tag.
                 */
char step_name[MAX_LINE_BUFSIZE]  /* <O>
                  Name of the step.
                  The buffer must be declared using MAX_LINE_BUFSIZE so it can hold MAX_LINE_NCHARS characters.
                  */
);

/***************************************************************************
Given the tag of a solution and a new name, this function sets the name
of the solution associated to the given tag.

Returns:  0(success) OR > 1(failure):
          UF_NAME_CONFLICT - solution name name not unique
          UF_NAME_INVALID_CHAR - invalid character in name
          UF_RESULT_FILE_NAME_CONFLICT - solution name has potential
                                         conflict with existing result files.
          UF_NAME_TOO_LONG - solution name too long

Environment: Internal  and  External

See Also:

History:
****************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_solution_set_name_nx(
tag_t  solution, /* <I>
                 Tag of the solution attached to name.
                 */
const char* solution_name, /* <I>
                           Name of the solution.
                           The buffer must be declared using MAX_LINE_BUFSIZE so it can hold MAX_LINE_NCHARS characters.
                           */
logical rename_result_file /* <I>
                           Flag for renaming any associated result file.
                           If set to TRUE, the solution and result file will
                           be renamed the part will automatically be saved in
                           order to maintain the association between the
                           solution and the result file.
                           If set to FALSE, the solution will be renamed,
                           but the result file will retain its current name.
                           The association between the solution and the
                           result file will be lost.
                           */
);

/***************************************************************************
Given the tag of a step and a new name, this function sets the name
of the step associated to the given tag.

Returns:  0(success) OR > 1(failure).
          UF_NAME_CONFLICT - step name name not unique
          UF_NAME_INVALID_CHAR - invalid character in name
          UF_NAME_TOO_LONG - step name too long

Environment: Internal  and  External

See Also:

History:
****************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_step_set_name_nx(
tag_t  solution ,/* <I>
                    Tag of the parent solution.
                    */
tag_t  step ,/* <I>
                 Tag of the step attached to name.
                 */
const char* step_name  /* <I>
                          Name of the step.
                          The buffer must be declared using MAX_LINE_BUFSIZE so it can hold MAX_LINE_NCHARS characters.
                          */
);

/***************************************************************************
Given a load or boundary condition entity, this function finds the solutions
that use the load or boundary condition entity.

Valid only when the work part is a Simulation.

Environment: Internal  and  External

See Also:

History: Originally released in NX3.0
****************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_ask_solution_nx(
tag_t  lbc_tag ,/* <I>
                Tag of the load or boundary condition.
                */
int *num_members,/* <O>
                 Number of loads and bc's in the solution.
                 */
tag_t** solution_pp  /* <OF>
                    The pointer to the array of the tags of the solutions.
                    If num_members is zero, this pointer should not be used.
                    If num_members is > 0, then this array must be freed by
                    calling UF_free.
                    */
);


/***************************************************************************
Given a load or boundary condition entity, this function finds the steps
that use the load or boundary condition entity.

Valid only when the work part is a Simulation.

Environment: Internal  and  External

See Also:

History: Originally released in NX3.0
****************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_ask_step_nx(
tag_t  lbc_tag ,/* <I>
                Tag of the load or boundary condition.
                */
int *num_members ,/* <O>
                 Number of loads and bc's in the step.
                 */
tag_t** step_pp  /* <OF>
                  The pointer to the array of the tags of the steps.
                  If num_members is zero, this pointer should not be used.
                  If num_members is > 0, then this array must be freed by
                  calling UF_free.
                  */
);


/***************************************************************************
Given a name of a solution, this function finds the tag of the solution.

Valid only when the work part is a Simulation.

Environment: Internal  and  External

See Also:

History: Originally released in NX3.0
******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_locate_named_solution_nx(
const char* solution_name, /* <I>
                           Name of the solution.
                           */
tag_t*  solution_tag  /* <O>
                      Tag of the solution.
                      */
);


/***************************************************************************
Given the name of a step and the tag of its parent solution, this function
finds the step.

Environment: Internal  and  External

See Also:

History: Originally released in NX3.0
******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_locate_named_step_nx(
tag_t solution_tag,     /* <I>
                        Tag of the solution.
                        */
const char* step_name, /* <I>
                       Name of the step.
                       The buffer must be declared using MAX_LINE_BUFSIZE so it can hold MAX_LINE_NCHARS characters.
                       */
tag_t*  step_tag  /* <O>
                  Tag of the step.
                  */
);

/*************************************************************************
Creates a solution with a given name.

Environment: Internal  and  External

See Also:

History: Originally released in NX3.0
**************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_create_solution_nx(
tag_t solution_desc, /* <I>
                      Tag for the solution descriptor.
                      */
tag_t solver_desc, /* <I>
                      Tag for the solver descriptor.
                      */
const char* solution_name ,/* <I>
                            Name for the solution.
                            */
tag_t* solution_tag /* <O>
                     Tag for the solution.
                     */
);


/*************************************************************************
Creates a step with a given name.

Steps are subdivisions of a CAE solution.
UF_SFL_solution_ask_step_descriptor_nx - Given a solution descriptor tag
and allowable step descriptor name, returns the tag of the step descriptor.

If the user does not know the step descriptor name, they can use the following:
UF_SFL_solution_ask_num_allowable_step_descriptors_nx
UF_SFL_solution_ask_nth_allowable_step_descriptor_nx
UF_SFL_step_descriptor_ask_name_nx

Environment: Internal  and  External

See Also:

History: Originally released in NX3.0
**************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_create_step_nx(
tag_t step_desc, /* <I>
                 Tag for the step descriptor.
                 */
const char* step_name, /* <I>
                       Name for the step.
                       */
tag_t solution_tag, /* <I>
                    Tag for the parent solution.
                    */
tag_t* step_tag /* <O>
                Tag for the step.
                */
);

/*************************************************************************
Get the language of a solution.

Environment: Internal  and  External

See Also:

History: Originally released in NX3.0
**************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_solution_ask_language_nx(
tag_t solution, /* <I>
                 Tag for the solution.
                 */
tag_t* language /* <O>
                 Tag for the language.
                 */
);

/*************************************************************************
Given a solution, query the number of properties that it references.

Environment: Internal  and  External

See Also:

History: Originally released in NX3.0
**************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_solution_ask_property_count_nx(
tag_t solution,   /* <I>
                  Tag for the solution.
                  */
int* num_props   /* <O>
                 Number of properties.
                 */
);

/*************************************************************************
Given a solution and index into the solution's property list, returns the
tag of the property descriptor. This function can be used to loop over all
property descriptors in the solution.

The number of property descriptors can be obtained from function
UF_SF_solution_ask_property_count_nx.

The index is just a counter.
Valid indices are from 0 to (number of property descriptors-1).

Environment: Internal  and  External

See Also:  UF_SF_solution_ask_property_count_nx

History: Originally released in NX3.0
**************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_solution_ask_property_by_index_nx(
tag_t solution,     /* <I>
                    Tag for the solution.
                    */
int property,       /* <I>
                    Index into list of properties.
                    Valid indices are from 0 to (number of properties-1).
                    The number of properties can be obtained
                    from function UF_SF_solution_ask_property_count_nx.
                    */
tag_t* property_tag /* <O>
                    Tag for the property.
                    */
);

/*************************************************************************
Given a solution and the name of a property that it references, returns
the tag of the property.

Environment: Internal  and  External

See Also:

History: Originally released in NX3.0
**************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_solution_ask_property_nx(
tag_t solution,     /* <I>
                    Tag for the solution.
                    */
const char* property_name, /* <I>
                           Property name.
                           */
tag_t* property_tag /* <O>
                    Tag for the property.
                    */
);

/*************************************************************************
Given a solution, query the number of solver properties that it references.

Environment: Internal  and  External

See Also:

History: Originally released in NX3.0
**************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_solution_ask_solver_property_count_nx(
tag_t solution,   /* <I>
                  Tag for the solution.
                  */
int* num_props   /* <O>
                 Number of properties.
                 */
);

/*************************************************************************
Given a solution and index into the solution's solver property list,
returns the tag of the solver property descriptor. This function can be
used to loop over all solver property descriptors in the solution.

The number of solver property descriptors can be obtained from function
UF_SF_solution_ask_solver_property_count_nx.

The index is just a counter.
Valid indices are from 0 to (number of solver property descriptors-1).

See Also:  UF_SF_solution_ask_solver_property_count_nx

History: Originally released in NX3.0
**************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_solution_ask_solver_property_by_index_nx(
tag_t solution,     /* <I>
                    Tag for the solution.
                    */
int property,       /* <I>
                    Index into list of solver properties for the solution.
                    Valid indices are from 0 to (number of solver properties-1).
                    The number of solver properties can be obtained
                    from function UF_SF_solution_ask_solver_property_count_nx.
                    */
tag_t* property_tag /* <O>
                    Tag for the property.
                    */
);

/*************************************************************************
Given a solution and the name of a solver property that it references,
returns the tag of the solver property.

Environment: Internal  and  External

See Also:

History: Originally released in NX3.0
**************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_solution_ask_solver_property_nx(
tag_t solution,     /* <I>
                     Tag for the solution.
                     */
const char* property_name, /* <I>
                           Property name.
                           */
tag_t* property_tag /* <O>
                    Tag for the property.
                    */
);

/*************************************************************************
Given a step, query the number of properties that it references.

Environment: Internal  and  External

See Also:

History: Originally released in NX3.0
**************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_step_ask_property_count_nx(
tag_t step,       /* <I>
                  Tag for the step.
                  */
int* num_props   /* <O>
                 Number of properties.
                 */
);

/*************************************************************************
Given a solution step and index into the step's property list, returns the
tag of the property descriptor. This function can be used to loop over all
property descriptors in the step.

The number of property descriptors can be obtained from function
UF_SF_step_ask_property_count_nx.

The index is just a counter.
Valid indices are from 0 to (number of property descriptors-1).

Environment: Internal  and  External

See Also:  UF_SF_step_ask_property_count_nx

History: Originally released in NX3.0
**************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_step_ask_property_by_index_nx(
tag_t step,         /* <I>
                    Tag for the step.
                    */
int property,       /* <I>
                    Index into list of properties for the step.
                    Valid indices are from 0 to (number of property descriptors-1).
                    */
tag_t* property_tag /* <O>
                    Tag for the property.
                    */
);

/*************************************************************************
Given a solution step and the name of a property that it references,
returns the tag of the property.

Environment: Internal  and  External

See Also:

History: Originally released in NX3.0
**************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_step_ask_property_nx(
tag_t step,          /* <I>
                     Tag for the step.
                     */
const char* property_name,/* <I>
                          Property name.
                          */
tag_t* property_tag  /* <O>
                     Tag for the property.
                     */
);

/*************************************************************************
Delete a solution.

Valid only when the work part is a Simulation.

Environment: Internal  and  External

See Also:

History: Originally released in NX3.0
**************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_delete_solution_nx(
tag_t solution  /* <I>
                 Tag for the solution.
                 */
);

/*************************************************************************
Delete a step.

Valid only when the work part is a Simulation.

Environment: Internal  and  External

See Also:

History: Originally released in NX3.0
**************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_delete_step_nx(
tag_t step  /* <I>
            Tag for the step.
            */
);

/*******************************************************************************
Given a tag to a node entity, locates the parent geometry features
linked to the node.

If given a node occurrence from a Simulation part then polygonal (CAE) geometry
occurrences from that Simulation part are returned.  Similarly if given a node
from a FEM part then polygonal (CAE) geometry from that FEM part are returned.

Environment: Internal  and  External

See Also:

History:
*******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_ask_node_pgeoms (
tag_t node_tag ,/* <I>
                Tag to a node object.
                */
int* parent_cnt ,/* <O>
                 Number of parent geometry tags related to
                 the node.
                 */
tag_p_t* parent_list ,/* <OF,len:parent_cnt>
                      pointer to an array of parent geometry tags
                      found  or NULL if not found.  This array must be
                      freed by calling UF_free.
                      */
UF_SF_mesh_geometry_types_p_t* geom_types  /* <OF,len:parent_cnt>
                                           pointer to an array of
                                           parent geometry types
                                           found or NULL if not found.
                                           geom_types is 1:1 with objects list.
                                           This array must be freed by calling
                                           UF_free.
                                           */
);

/**************************************************************************-----
Locates and returns the the list element tags which match the list of
input element ids.  If there are no elements, then returns
num_of_elements = 0 and element_tags_not =  NULL.

Environment: Internal  and  External

See Also:

History:
*************************************************************************------*/
extern UFUN_CAEEXPORT int UF_SF_locate_element_by_id (
tag_t mesh_tag ,/* <I>
                Mesh tag, pass in NULL_TAG to locate all
                elements in current part.
                */
int num_of_ids ,/* <I>
                The number of element ids to look for.
                */
int element_ids[] ,/* <I,len:num_of_ids>
                   An array of element ids for which element
                   tags are to be returned.
                   */
int* num_of_elements ,/* <O>
                      The number of elements found. Could be
                      zero.
                      */
tag_t** element_tags_p  /* <OF,len:num_of_elements>
                        pointer to an array of element tags or NULL.
                        This array must be freed by calling UF_free.
                        */
);

/**************************************************************************-----
Locates and returns the the list node tags which match the list of input
node ids.  If there are no nodes , then returns num_of_nodes = 0 and
node_tags_p =  NULL.

Environment: Internal  and  External

See Also:

History:
*************************************************************************------*/
extern UFUN_CAEEXPORT int UF_SF_locate_node_by_id (
tag_t mesh_tag ,/* <I>
                Mesh tag, pass in NULL_TAG to locate all
                nodes in current part.
                */
int num_of_ids ,/* <I>
                The number of node ids to look for.
                */
int node_ids[] ,/* <I,len:num_of_ids>
                An array of node ids for which element tags
                are to be returned.
                */
int* num_of_node ,/* <O>
                  The number of nodes found. Could be zero.
                  */
tag_t** node_tags_p  /* <OF,len:num_of_node>
                     pointer to an array of node tags or NULL.  This
                     must be freed by calling UF_free.
                     */
);

/*******************************************************************************
Auto creates surface contact meshes. For a given capture distance, a mesh is created
for every pair of meshes created. A mesh has only one source polygon face and one target
polygon face.

Environment: Internal  and  External

See Also:

History:
**************************************************************************-----*/
extern UFUN_CAEEXPORT int UF_SF_auto_create_surface_contact_mesh(
double capture_distance ,/* <I>
              The mimimum distance between two polygon faces of different polygon bodies that
              form a contact pair.
              */
void *property ,/* <I>
                                       Structure to define mesh properties.
                                       The valid structures are
                                       UF_SF_SURFACE_CONTACT_ANS_data_p_t,
                                       UF_SF_SURFACE_CONTACT_NAS_data_p_t,
                                       UF_SF_SURFACE_CONTACT_UGFEA_data_p_t

                                       */
int *num_meshes, /* <O>
                                        Pointer to number of meshes
                                         */
tag_p_t *mesh_recipes /* <OF,len:num_meshes>
                        Pointer to the number of mesh recipe tags created. */

);


/*******************************************************************************
Creates a surface contact mesh for a given source and target polygon face. The source and target
polygon face should belong to a different polygon body.

Environment: Internal  and  External

See Also:

History:
**************************************************************************-----*/
extern UFUN_CAEEXPORT int UF_SF_create_surface_contact_mesh(
tag_t source_face ,/* <I>
                      The source side polygon face on which contact need to be created.
                   */
tag_t target_face ,/* <I>
                      The target side polygon face on which contact need to be created.
                   */
void *property ,/* <I>
                                       Structure to define mesh properties.
                                       The valid structures are
                                       UF_SF_SURFACE_CONTACT_ANS_data_p_t,
                                       UF_SF_SURFACE_CONTACT_NAS_data_p_t,
                                       UF_SF_SURFACE_CONTACT_UGFEA_data_p_t

                                       */

tag_p_t mesh_recipe /* <O>           Pointer to the mesh recipe tag created. */
);

/*******************************************************************************
Given a tag to a geometry, find all nodes on it

If given a polygon geometry (CAE geometry) occurrence then node occurrences
in the owning Simulation part are returned. Similarly if given a ploygon geometry
then nodes in the owning FEM part are returned.

Environment: Internal  and  External

See Also:

History:
*******************************************************************************/
extern UFUN_CAEEXPORT  int  UF_SF_locate_nodes_on_geometry(
tag_t   geom_tag, /* <I>
                  Tag of CAE geometry.
                  */
UF_SF_node_switch_t type_sw, /* <I>
                             switch indicating face/solid interior nodes are
                             desired, SFOM_node_switch_t
                             It can be one of the three choices:
                              UF_SF_SWITCH_ON_BOUNDARY: boundary nodes only
                              UF_SF_SWITCH_IN_INTERIOR: internal nodes only
                              UF_SF_SWITCH_ALL:         all nodes
                             */
int     *nodes_cnt, /* <O>
                    number of nodes on the geometry
                    */
tag_p_t *nodes_list /* <OF,len:nodes_cnt>
                    list of node tags on the geometry
                    */
);

/*******************************************************************************
Create a SFEM assembly_mesh object.

Environment: Internal  and  External

See Also:

History: This function was originally released in V16.0
*******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_create_mesh_mating_condition (
tag_t                  assembling_geom,  /*<I>
                                           Assembling region polygon geometry tag
                                         */
tag_t                  target_geom,      /*<I>
                                         Target region polygon geometry tag
                                         */
char*                  assembly_name,    /*<I>
                                         Assembly mesh name
                                         */
int                    seed_mesh,        /*<I>
                                         Flag of seed mesh
                                         */
UF_SF_assembly_type_t  assembly_type,    /*<I>
                                         Assembly mesh type
                                         */
double                 merge_tolerance,  /*<I>
                                         Node merge tolerance
                                         */
double                 match_tolerance,  /*<I>
                                         match tolerance to define if an
                                         independent node matchs with a master
                                         element
                                         */
tag_t                  *assembly_mesh    /*<O>
                                         Tag of the newly created assembly mesh
                                         */
                        );

/*******************************************************************************
Delete a SFEM assembly_mesh object.

Environment: Internal  and  External

See Also:

History:
*******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_delete_mesh_mating_condition
(
    int    num_mmc,      /*<I>
                         Number of MMCs to be deleted
                         */
    tag_t  mmc_array[]   /*<I>
                         Array of MMC tags to be deleted
                         */
);

/*******************************************************************************
Edit a SFEM assembly_mesh object.

Environment: Internal  and  External

See Also:

History:
*******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_edit_mesh_mating_condition
(
    int    num_mmc,               /*<I>
                                  Number of MMCs to be deleted
                                  */
    tag_t  mmc_array[],           /*<I>
                                  Array of MMC tags to be deleted
                                  */
    int    make_mesh_coincident,  /*<I>
                                  coincident or non-coincident
                                  */
    int    mesh_mating_type       /*<I>
                                  Glue or Free
                                              = 0 --> GLUE
                                              = 3 --> FREE
                                              NOTE: There is no 1 or 2 Type
                                  */
);

/*******************************************************************************
Return a list of all the assembly_mesh objects.

Environment: Internal  and  External

See Also:

History: This function was originally released in V16.0
*******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_locate_mesh_mating_condition_list (
int*        assembly_mesh_cnt,  /*<O>
                                Count of Assembly mesh objects returned
                                */
tag_t**     assembly_mesh_tags  /*<OF,len:assembly_mesh_cnt>
                                Pointer to an array of tags.  If not desired,
                                input a NULL pointer.  This array must be
                                freed by calling UF_free.
                                */
);

/*******************************************************************************
Locate the assembly mesh object from an assembly mesh name.

Environment: Internal  and  External

See Also:

History: This function was originally released in V16.0
*******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_locate_mesh_mating_condition_by_name (
char*   assembly_name,  /*<I>
                        Assembly mesh name
                        */
tag_t*  assembly_mesh   /*<O>
                        Tag of the assembly mesh object
                        */
);

/*******************************************************************************
Given an assembly mesh tag, obtain the infomation about the assembly mesh.
If some information is unneeded, the input pointer can be set to NULL.


Environment: Internal  and  External

See Also:

History: This function was originally released in V16.0
*******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_ask_mesh_mating_condition (
tag_t                   assembly_mesh_tag,  /*<I>
                                            Assembly mesh tag
                                            */
tag_t*                  assembling_geom,    /*<O>
                                            Assembling region geometry tag
                                            */
tag_t*                  target_geom,        /*<O>
                                            Target region geometry tag
                                            */
char**                  assembly_name,      /*<OF>
                                            Assembly mesh name
                                            */
int*                    seed_mesh,          /*<O>
                                            Flag of seed mesh
                                            */
UF_SF_assembly_type_t*  assembly_type,      /*<O>
                                            Assembly mesh type
                                            */
double*                 merge_tolerance,    /*<O>
                                            Node merge tolerance
                                            */
double*                 match_tolerance     /*<O>
                                            match tolerance to define if an
                                            independent node matchs with a
                                            master element
                                            */
);

/*******************************************************************************
    This function creates a midsurface using offset method. This creation
    requires the user to specify the following:

    1) A Seed Face - This is the face on the body from which the function
                     propagates and collects all the faces based on the
                     following criteria:

         a) Cliff Angle: The propagation halts and does not take the face
                         concerned in to the collection if the angle between
                         the normals of the current face and this face is
                         greater than the cliff angle.  Please note that this
                         is the only criterion which is given as input.

      NOTE: There are other criteria which the system computes such as the
            thickness of the body at the seed face, thickness of the body
            adjacent to the seed face and also the set of edges which belong
            to the set of faces opposite to the propagation.

    2) The percentage distance is the percentage of the thickness (distance) at
       which the midsurface will be placed from the seed face, after creation
       within the body.

Environment: Internal  and  External

See Also:

History: Originally released in V16.0
*******************************************************************************/

extern UFUN_CAEEXPORT int UF_SF_create_offset_midsrf
(
   tag_t    seed_face,       /*<I> The tag of the seed face on the solid body.*/
   double   cliff_angle,     /*<I> The user input cliff angle to define the
                                   boundary*/
   double   percentage_dist, /*<I> Percentage location of midsurface */
   tag_t   *midsurface_tag   /*<O> Midsurface sheet body tag that was created.*/
);


/*******************************************************************************
    This function edits a midsurface which was created using offset method.
    This requires the user to specify the following:

        Seed Face:  Optional. This has to be specified if the user wants the
                    seed face to be different from the original seed face of
                    the midsurface. Otherwise, this parameter can be set to NULL.

        Cliff Angle: If a different cliff angle has to be chosen, other than
                     the one with which the midsurface was created. Otherwise,
                     this can either be zero or it can be the original Cliff
                     Angle.

      NOTE: There are other criteria which the system computes such as the
            thickness of the body at the seed face, thickness of the body
            adjacent to the seed face and also the set of edges which belong
            to the set of faces opposite to the propagation.

      percentage distance: is the percentage of the thickness (distance) at
      which the midsurface will be placed from the seed face, after creation
      within the body.

    The output is the tag of the modified midsurface.

Environment: Internal  and  External

See Also:

History: Originally released in V16.0
*******************************************************************************/

extern UFUN_CAEEXPORT int UF_SF_edit_offset_midsrf
(
   tag_t   seed_face,      /*<I> A tag of a seed face on the solid body. This
                                 may be different than the original seed face.*/
   double  cliff_angle,    /*<I> The user input cliff angle to define the
                                 boundary*/
   double  percentage_dist,/*<I> Percentage location of midsurface */
   tag_t  *midsurface_tag  /*<I/O> Midsurface sheet body tag*/
);


/**************************************************************************-----
Query a sheet body to see if it is an offset midsurface.
This function may not be used for general midsurface. If the input is a
midsurface created by Facepair method, this function will return FALSE.


Environment: Internal  and  External

See Also:

History: Originally released in V16.0
 *************************************************************************----*/

extern UFUN_CAEEXPORT int UF_SF_is_offset_midsrf
(
       tag_t      sheet_body_tag,  /*<I> Tag of the sheet body.*/
       logical   *is_midsrf /* <O> TRUE if the sheet body is an offset
                                   midsurface, FALSE otherwise. */
);

/**************************************************************************----
Query the thickness of an offset midsurface. Please note that this
function will not return the thickness if the midsurface is created
by a method other than the offset method (e.g., Facepair method).

Environment: Internal  and  External

See Also:

History: Originally released in V16.0
*************************************************************************-----*/

extern UFUN_CAEEXPORT int UF_SF_ask_offset_midsrf_thickness
(
   tag_t       midsrf_tag, /*<I> Tag of the midsurface. */
   double     *thickness   /*<O> The thickness of the midsurface.  If the
                                 tag is not an offset midsurface, then
                                 the thickness will be returned as 0.0. */
);

/*******************************************************************************
    This routine allocates a parameter object for an idealize feature

    The parameter object is used to hold all information needed to create an
    idealize feature.  All expressions associated with this object will be
    initialized to NULL_TAG.  All face sets associated with this object will
    be initalize to contain 0 faces

Environment: Internal  and  External

See Also:

History: Originally released in V17.0
*******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_alloc_idealize_parms
(
  UF_SF_idealize_parms_p_t   *parms_p   /* <OF,free:UF_SF_free_idealize_parms>
                                        Allocated idealize parameter entity
                                        Use UF_SF_free_idealize_parms to free
                                        memory associated to this entity
                                        */
);

/*******************************************************************************
    This routine frees memory associated to a parameter object for an idealize
    feature

Environment: Internal  and  External

See Also:

History: Originally released in V17.0
*******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_free_idealize_parms
(
  UF_SF_idealize_parms_p_t   parms_p    /* <I>
                                        Idealize parameter entity to freed
                                        */
);

/*******************************************************************************
    This routine gets a specified expression from a parameter object for an
    idealize feature

Environment: Internal  and  External

See Also:

History: Originally released in V17.0
*******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_ask_idealize_parm_exp
(
  UF_SF_idealize_parms_p_t   parms_p,     /* <I>
                                          Idealize parameter entity to query
                                          */
  UF_SF_idealize_parm_exp_t  parm_exp_t,  /* <I>
                                          Specific expression to retrieve from
                                          idealize parameter entity
                                          */
  tag_t                      *exp_tag     /* <O>
                                          Tag of the expression used for the
                                          specific idealize parameter
                                          Can be NULL_TAG which means that this
                                          parameter is not used
                                          */
);

/*******************************************************************************
    This routine sets a specified expression from a parameter object for an
    idealize feature

Environment: Internal  and  External

See Also:

History: Originally released in V17.0
*******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_set_idealize_parm_exp
(
  UF_SF_idealize_parms_p_t   parms_p,     /* <I>
                                          Idealize parameter entity to set
                                          */
  UF_SF_idealize_parm_exp_t  parm_exp_t,  /* <I>
                                          Specific expression to set in the
                                          idealize parameter entity
                                          */
  tag_t                      exp_tag      /* <I>
                                          Tag of the expression to be used for the
                                          specific idealize parameter
                                          Can be NULL_TAG which means that this
                                          parameter will not be used
                                          */
);

/*******************************************************************************
    This routine gets a specified set of faces from a parameter object for an
    idealize feature

Environment: Internal  and  External

See Also:

History: Originally released in V17.0
*******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_ask_idealize_parm_faces
(
    UF_SF_idealize_parms_p_t   parms_p,     /* <I>
                                            Idealize parameter entity to query
                                            */
    UF_SF_idealize_parm_face_t parm_face_t, /* <I>
                                            Specific face set parameter to query
                                            */
    int                        *num_faces,  /* <O>
                                            Number of faces returned in faces array
                                            */
    tag_t                      **faces      /* <OF,len:num_faces>
                                            Array of face tags.  This should be
                                            freed by calling UF_free.
                                            */
);

/*******************************************************************************
    This routine sets a specified set of faces from a parameter object for an
    idealize feature

Environment: Internal  and  External

See Also:

History: Originally released in V17.0
*******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_set_idealize_parm_faces
(
    UF_SF_idealize_parms_p_t   parms_p,     /* <I>
                                            Idealize parameter entity to query
                                            */
    UF_SF_idealize_parm_face_t parm_face_t, /* <I>
                                            Specific face set parameter to query
                                            */
    int                        num_faces,   /* <I>
                                            Number of faces in the faces array
                                            */
    tag_t                      *faces       /* <I,len:num_faces>
                                            Array of face tags
                                            */
);

/*******************************************************************************
    This routine allocates a region object for an idealize feature

    The region object is used to hold all information needed to create an
    idealize feature associated to a body region.

Environment: Internal  and  External

See Also:

History: Originally released in V17.0
*******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_alloc_idealize_region
(
    tag_t                      seed_face,     /* <I>
                                              Seed face for the region (required)
                                              */
    int                        num_bnd_faces, /* <I>
                                              Number of boundary faces in the
                                              bnd_faces array.  Can be 0
                                              */
    tag_t                      *bnd_faces,    /* <I,len:num_bnd_faces>
                                              Array of boundary faces.
                                              Can be NULL if num_bnd_faces == 0
                                              */
    tag_t                      angle_exp,     /* <I>
                                              Expression to be used for the tagential
                                              edge angle which is used for the region
                                              boundary, Can be NULL_TAG
                                              */
    UF_SF_idealize_region_p_t  *region_p      /* <OF,free:UF_SF_free_idealize_region>
                                              Idealize region entity created
                                              Use UF_SF_free_idealize_region to free
                                              */
);

/*******************************************************************************
    This routine frees a region object for an idealize feature

Environment: Internal  and  External

See Also:

History: Originally released in V17.0
*******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_free_idealize_region
(
    UF_SF_idealize_region_p_t  region_p       /* <I>
                                              Idealize region entity in which to free
                                              */
);

/*******************************************************************************
    This routine returns the information in a region object for an idealize
    feature

    The region object is used to hold all information needed to create an
    idealize feature associated to a body region.

Environment: Internal  and  External

See Also:

History: Originally released in V17.0
*******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_ask_idealize_region
(
    UF_SF_idealize_region_p_t  region_p,      /* <I>
                                              Idealize region entity in which to query
                                              */
    tag_t                      *seed_face,     /* <O>
                                               Seed face for the region
                                               Pass NULL if return parameter is not wanted
                                               */
    int                        *num_bnd_faces, /* <O>
                                               Number of boundary faces in the
                                               bnd_faces array.  Can be 0
                                               Pass NULL if return parameter is not wanted
                                               If NULL is passed in, bnd_faces will be
                                               returned as NULL
                                               */
    tag_t                      **bnd_faces,    /* <OF,len:num_bnd_faces>
                                               Array of boundary faces.
                                               Is NULL if num_bnd_faces == 0
                                               Pass NULL if return parameter is not wanted
                                               */
    tag_t                      *angle_exp      /* <I>
                                               Expression used for the tagential
                                               edge angle which is used for the region
                                               boundary, Can be NULL_TAG

                                               */
);

/*******************************************************************************
    This routine creates an idealize feature for an entire body

    This routine takes the tag of a body and an idealize parms object that is
    set to the desired operation and creates an idealize feature.  Since removal
    of all specified faces and edges is not guaranteed, returned are the edges
    of all failing wounds (edges of the face or hole edge in a sheet body)
    idealize feature associated to a body region.

Environment: Internal  and  External

See Also:

History: Originally released in V17.0
*******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_create_idealize_body
(
  tag_t     body_tag,           /* <I>
                                Body to be simplified (Solid or Sheet)
                                */
  UF_SF_idealize_parms_p_t parms_p,
                                /* <I>
                                Parameters of the new idealize feature
                                */
  tag_t    *feature_tag,        /* <O>
                                The feature created
                                */
  int   *n_failing_wound_edges, /* <O>
                                Number of edges of failing wounds
                                */
  tag_t **failing_wound_edges   /* <OF,len:n_failing_wound_edges>
                                Array of edges of failing wounds.  This must
                                be freed by calling UF_free.
                                */
);


/*******************************************************************************
    This routine creates an idealize feature for specified region of a body

    This routine takes a region object and an idealize parms object that is
    set to the desired operations and creates an idealize feature.  Since removal
    of all specified faces and edges is not guaranteed, returned are the edges
    of all failing wounds (edges of the face or hole edge in a sheet body)
    idealize feature associated to a body region.

Environment: Internal  and  External

See Also:

History: Originally released in V17.0
*******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_create_idealize_region
(

  UF_SF_idealize_region_p_t   region_p,
                                /* <I>
                                Parameters that define the region of the body
                                to be simplified.
                                */
  UF_SF_idealize_parms_p_t parms_p,
                                /* <I>
                                Parameters of the new idealize feature
                                */
  tag_t    *feature_tag,        /* <O>
                                The feature created
                                */
  int   *n_failing_wound_edges, /* <O>
                                Number of edges of failing wounds
                                */
  tag_t **failing_wound_edges   /* <OF,len:n_failing_wound_edges>
                                Array of edges of failing wounds.  This must
                                be freed by calling UF_free.
                                */
);

/*******************************************************************************
    This routine returns the definition of an idealize feature

    This routine takes the feature tag of an idealize feature and returns the
    parameters associated to it.

Environment: Internal  and  External

See Also:

History: Originally released in V17.0
*******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_ask_idealize_parms
(
  tag_t feature_tag,           /* <I>
                               The idealize feature
                               */

  logical *is_region,
                               /* <O>
                               Flag indicating whether the idealize feature
                               is from a region versus a body
                               is_region = TRUE  -> Feature is from a region
                               is_region = FALSE -> Feature is from a body
                               */
  void *body_region,
                                /* <OF>
                               If NULL on input only the idealize_parms
                               will be returned.
                               Pointer to a UF_SF_idealize_region_p_t or to
                               a tag_p_t for the body depending on the returned
                               value of the flag is_region.
                               If is_region = TRUE  -> output is a pointer to
                               an instance of UF_SF_idealize_region_data_p_t
                               If is_region = FALSE  -> output is a pointer to
                               a tag_p_t that identifies the body.

                               Use UF_SF_idealize_free_region if a region
                               Use UF_free if a body
                               */
  UF_SF_idealize_parms_p_t idealize_parms
                               /* <OF>
                               The parameters of the idealize feature.
                               Use UF_SF_idealize_free_parms to free
                               */
);

/*******************************************************************************
    This routine edits idealize feature

    This routine takes the feature tag of an idealize feature and edits
    it according to the new parameter object definition.  Since removal
    of all specified faces and edges is not guaranteed, returned are the edges
    of all failing wounds (edges of the face or hole edge in a sheet body)
    idealize feature associated to a body region.

Environment: Internal  and  External

See Also:

History: Originally released in V17.0
*******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_edit_idealize_parms
(
  tag_t   feature_tag,         /* <I>
                               The idealize feature
                               */
  UF_SF_idealize_parms_p_t  parms_p,
                               /* <I>
                               New parameters of the idealize feature
                               */
  int *n_failing_wound_edges,  /* <O>
                               The number of failing wound edges
                               */
  tag_t **failing_wound_edges  /* <OF,len:n_failing_wound_edges>
                               Array of failing wound edges.  This must be
                               freed by calling UF_free.
                               */
);

/**********************************************************************************

  Given an array of solid bodies or faces (but not both). this function
  automatically creates the information of the pairs of faces that
  are mated within the given 'distance_tolerance'. It then uses this information
  to subdivide the overlapping face pairs using the opposite edges of each face
  pair. Finally, it outputs the faces pairs that became coincident
  as a result of subdivision. In addition, it also outputs the face pairs that
  are already coincident with or without an equal number of edges. However, there are
  two options as described below to control the output.

  1. subdivision_needed  - The user can specify whether the subdivision is needed
     or not. If it is not needed, only those face pairs that are found to be
     already coincident will be output.  (1 for needed, 0 otherwise)
  2. face_search_option - It gives the caller an option to specify whether
     all types of face pairs needs to be searched or only coincident pairs are of
     interest. (1 for search all faces, 0 for search only coincident ones)

  When face pairs are coincident with an equal number of edges, the relative_status in
  the output structure 'resulting_pairs' is UF_SF_IDENTICAL_FACES_EQ_EDGES. Further,
  when the face pairs are coincident with unequal number of edges, the relative_status
  in the output structure is UF_SF_IDENTICAL_FACES_UNEQ_EDGES.

  Caller of this function is responsible for freeing up the memory of the output
  structure array 'resulting_pairs'.

Environment: Internal  and  External

See Also:

History: Originally released in V17.0
*******************************************************************************/

extern UFUN_CAEEXPORT int UF_SF_create_auto_face_subdiv (
 tag_t                          *objects,              /* <I,len:obj_count>
                                                          An array of solid bodies or faces */
 int                            obj_count,             /* <I>
                                                          Count of the  above array */
 double                         distance_tolerance,    /* <I>
                                                          Tolerance for face pairing */
 int                            subdivision_needed,    /* <I>
                                                          Whether subdivision needed
                                                          1 for YES, 0 for NO        */
 int                            face_search_option,    /* <I>
                                                          1 for all faces
                                                          0 for coincident faces only */
 UF_SF_resulting_face_pairs_p_t *resulting_pairs,      /* <OF,len:resulting_pairs_count>
                                                          Array of face pair structures. This
                                                          must be freed by calling UF_free.*/
 int                            *resulting_pairs_count /* <O>
                                                          Count of the above structures */
);

/*******************************************************************************-
 *
 * This routine finds all the mesh entities in the work part.
 *
 * Environment: Internal & External
 *
 * See Also:
 *
 * History: Written in v18.0
 *******************************************************************************/
extern UFUN_CAEEXPORT  int   UF_SF_locate_all_meshes (
                            tag_t mesh_tag,       /* <I>
                                        Mesh tag, pass in NULL_TAG to locate all
                                        tags in current part.
                                        */
                            int   *mesh_count,    /* <O> mesh count */
                            tag_p_t* mesh_pointer /* <OF,len:mesh_count>
                                                     mesh array.  This
                                                     array must be freed by
                                                     calling UF_free. */
                            );

/*******************************************************************************
Test the GPE module

Environment: Internal  and  External

See Also:

History:

 *************************************************************************------*/
extern UFUN_CAEEXPORT int UF_SF_test_gpe( FILE *fp  /* <I> file pointer */
                                    );

/*******************************************************************************
This routine initializes Scenario

Environment: Internal and External

See Also:

History:
 *************************************************************************------*/
extern UFUN_CAEEXPORT int UF_SF_open_scenario(
                            const char* scenario_name,   /* <I>
                                                     scenario to be opened */
                            tag_t master_part_tag
                                                   /* <I>
                                                     master part tag */
                            );

/*******************************************************************************
This routine clone a Scenario

Environment: Internal and External

See Also:

History:
 *************************************************************************------*/
extern UFUN_CAEEXPORT int UF_SF_clone_scenario(
                       tag_t   master_part_tag, /* <I>
                                                  master part tag */
                       const char   *orig_scen,       /* <I>
                                                  original scenario */
                       const char   *cloned_scen      /* <I>
                                                  name of the clone */
                       );

/*******************************************************************************
This routine closes the current Scenario which is opened
when using UF_SF_open_scenario

Environment: Internal and External

See Also:

History:

 *************************************************************************------*/
extern UFUN_CAEEXPORT int UF_SF_close_scenario(
                                            void
                                          );

/*******************************************************************************
This routine deletes the specified Scenario

Environment: Internal and External

See Also:

History:

 *************************************************************************------*/
extern UFUN_CAEEXPORT int UF_SF_delete_scenario(
                            tag_t master_tag,   /* <I>
                                                  master part tag */

                            const char *scenario_name /* <I>
                                                  scenario to be deleted */
                            );

/*******************************************************************************
This routine renames the current Scenario

Environment: Internal and External

See Also:

History:
 *************************************************************************------*/
extern UFUN_CAEEXPORT int UF_SF_rename_scenario(
                            tag_t master_tag,   /* <I>
                                               master part tag   */
                            const char *old_scenario, /* <I>
                                               old scenario name */
                            const char *new_scenario
                                                /* <I>
                                               new scenario name */
                            );

/*******************************************************************************
This routine saves the current Scenario (Not valid for FEMs or Simulation parts)

Environment: Internal and External

See Also:

History:
 *************************************************************************------*/
extern UFUN_CAEEXPORT int UF_SF_save_scenario(
                                           void
                                         );

/*******************************************************************************
Displays a mesh object.


Environment: Internal  and  External

See Also:

History: Originally released in V19.0
*******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_display_mesh
(
    tag_t              mesh_tag      /*<I> Tag of mesh object to be displayed. */
);

/**************************************************************************
 *        This function will set the edge density given an input
 *        object.
 *        The edge density is defined as the number of elements to be created
 *        along the input object.  There are several cases:
 *
 ************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_set_edge_density
(
    tag_t   object_tag,              /* <I>- Tag of object to query.      */
    UF_SF_edge_density_data_t
            edge_density_data        /* <I> UF_SF_edge_density_data_t
                                          where the edge_density data will be stowed.
                                     */
);

/*******************************************************************************
Query material librefs and names from the NX Material library.

The output is optionally limited by material type, category and name
filters.
Each filter is a character string containing a regular
expression.
To disable a filter, enter "*".
To specify a filter,
code, for example, "IRON*" to find all materials named with a prefix
of "IRON". The usual material types are "ISO" "ORTHO" "ANISO" "FLUID",
filters are case insensitive.

The outputs of this function are the material count and 3 arrays.
The libref field is used to retrive the actual material from the
library. The name is intended to be the identifier that the user will
see displayed. The material type is passed back as a convenience to
allow post query filtering.

The 3 lists are arrays for allocated character strings.
Use UF_free_string_array to free each array.

Environment: Internal  and  External

See Also: UF_free_string_array

History: Originally released in NX2
*******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_ask_library_materials (
char*     type_filter,      /* <I>
                               A regular expression string which filters
                               the material type.
                               To find all materials, enter "*".
                               To find all isotropic materials, enter "ISO".
                               To find all orthotropic materials, enter "ORTHO".
                               To find all anisotropic materials, enter "ANISO".
                               To find all fluid materials, enter "FLUID".
                             */
char*     category_filter,  /* <I>
                               A regular expression string which filters
                               the material category.
                               To find all materials, enter "*".
                             */
char*     name_filter,      /* <I>
                               A regular expression string which filters
                               the material name.
                               To find all materials, enter "*".
                             */
int*      material_count,   /* <O>
                               The number of materials listed in the arrays.
                             */
char***  material_librefs,  /* <OF,len:material_count>
                               An array of characters strings containing the
                               library reference field of each material.
                               Call UF_free_string_array to free the
                               storage allocated within the structure.
                             */
char***  material_names,    /* <OF,len:material_count>
                               An array of characters strings containing the
                               name field of each material.
                               Call UF_free_string_array to free the
                               storage allocated within the structure.
                             */
char***  material_types     /* <OF,len:material_count>
                               An array of characters strings containing the
                               type field of each material.
                               Call UF_free_string_array to free the
                               storage allocated within the structure.
                             */
);



/*******************************************************************************
Given a material libref from the NX Material library,
retrieve the material from the library into the context part.

Use UF_SF_ask_library_materials to read the librefs.

Use UF_SF_ask_material to read the properties of the new material.

If a material of the same name or libref already exists in the
context part file, then an error is returned.

Environment: Internal  and  External

See Also: UF_SF_ask_library_materials
          UF_SF_ask_material

History: Originally released in NX2
*******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_retrieve_library_material (
char*     libref,            /* <I>
                               The library reference string read from the
                               NX Material Library.
                             */
tag_p_t   material_tag      /* <O>
                               Tag of the retrieved material, or NULL_TAG if
                               an error.
                             */
);


/*************************************************************************
 *    This function will partition solid bodies into 2 solid bodies.
 *
 * Environment: Internal  and  External
 *
 * See Also:
.*
.* History:
 ************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_partition_body
(
    int     num_solid_bodies,       /*<I> The number of solid bodies to partition.*/
    tag_p_t solid_body_tags,        /*<I,len:num_solid_bodies> Array of solid
                                                               bodies to partition.
                                    */
    tag_t   tool_body,              /*<I> tag of the tool to use to define the
                                          partition.
                                    */
    int     *num_partitioned_bodies,/*<O> Number of bodies generated after
                                          partitioning
                                    */
    tag_p_t *partitioned_bodies     /*<OF,len:num_partitioned_bodies> */
);

/*************************************************************************
 *    This function will partition solid bodies into 2 solid bodies.
 *    The method of partitioning will be based on the "Associate" toggle
 *    as follows ...
 *    1.  Associate toggle ON  implies that the existing behavior (the
 *        two resulting bodies are fully associated to the CAD master part)
 *        will be maintained
 *    2.  Associate toggle OFF implies that the two resulting bodies become
 *        unparameterized and not associated to the CAD master part.
 *
 * Environment: Internal  and  External
 *
 * See Also:
.*
.* History:
 ************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_partition_body_nx5
(
    int     associate,              /*<I> Associative toggle state
                                          ( 1 implies resultant bodies are
                                            associated to CAD part
                                            0 implies resultant bodies are not
                                            associated to CAD part .. they become
                                            unparameterized ) */
    int     num_solid_bodies,       /*<I> The number of solid bodies to partition.*/
    tag_p_t solid_body_tags,        /*<I,len:num_solid_bodies> Array of solid
                                                               bodies to partition.
                                    */
    tag_t   tool_body,              /*<I> tag of the tool to use to define the
                                          partition.
                                    */
    int     *num_partitioned_bodies,/*<O> Number of bodies generated after
                                          partitioning
                                    */
    tag_p_t *partitioned_bodies     /*<OF,len:num_partitioned_bodies> */
);

/*******************************************************************************
    This function creates a midsurface feature using the user defined method.
    This creation requires the user to specify the following via an instance of
    UF_SF_midsef_userdef_parms_t structure:

    1) A target solid body

    2) A collection of one or more sheet bodies.

    3) The thickness of the midsurface which will be used only for the thickness
       extraction at formatting time only if the automatic method fails if at least
       one of the specified sheet bodies is not fully contained in the target solid.

Environment: Internal  and  External

See Also:

History: Originally released in NX2
*******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_create_userdef_midsrf
(
    UF_SF_midsrf_user_parms_p_t parms_p,
                               /* <I>
                                Parameters of the new user defined midsurface
                                feature */
    tag_t   *feature_tag       /*<O> Tag of user defined midsurface feature.*/
);

/*******************************************************************************
    This function edits a midsurface feature which was created using the user
    defined method.
    This requires the user to specify the following via an instance of
    UF_SF_midsef_userdef_parms_t structure:


    1) A target solid body. If no  change set this parameter to NULL.

    2) A collection of one or more sheet bodies.
       The specified sheet bodies will redefine the midsurface.
       If the pointer is NULL then the midsurface will remain the same.

    3) The thickness of the midsurface which will be used only for the thickness
       extraction at formatting time only if the automatic method fails if at least
       one of the specified sheet bodies is not fully contained in the target solid.
       If a different thickness has to be chosen, other than the one with which the
       midsurface was created. Otherwise, this can either be zero or it can be the
       original thickness. If no change set this parameter to 0.

Environment: Internal  and  External

See Also:

History: Originally released in NX2
*******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_edit_userdef_midsrf
(
    UF_SF_midsrf_user_parms_p_t parms_p,
                               /* <I>
                                Parameters of the user defined midsurface
                                feature to be edited. */
   tag_t   *feature_tag       /*<I/O> Tag of user defined midsurface feature.*/

);

/******************************************************************************
  This function determines if a given object is a user defined midsurface

Environment: Internal  and  External

See Also:

History: Originally released in NX2
******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_is_userdef_midsrf
(
   tag_t       sheet_body_tag,  /*<I> Tag of given object */
   logical    *is_midsrf,       /*<O> Flag signifying the outcome:
                                    = TRUE -->  object is a user defined Midsurface
                                    = FALSE --> object is NOT a user defined Midsurface
                                */
   tag_t      *feature_tag      /*<O> Tag of the user defined midsurface feature
                                      if the object is associated with such a feature.
                                */
);

/*************************************************************************
 *  runs a duplicate nodes model check on the
 *  current scenario model.
 *
 *  ENVIRONMENT
 *    Internal and External
 *
 * History:
 ************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_cae_information
(
    UF_SF_scenario_info_t info_type,  /*<I> The type of information that is requested*/
    int num_entities,                 /*<I> The number of entities to get the
                                            requested information for.
                                      */
    tag_p_t entities_tags,            /*<I,len:num_entities>
                                         The tags of the meshes, sections, loads,
                                         etc. that we need info for.  Type of
                                         entitiy is determined by info_type.
                                         UF_SF_fea_summary_info,        num_entities
                                                                        should be 0 and
                                                                        entities_tags
                                                                        should be NULL.
                                        UF_SF_mesh_info,                specify mesh tags
                                        UF_SF_load_info,                specify load tags
                                        UF_SF_load_case_info,           specify a load tag
                                                                        in each desired
                                                                        load case
                                        UF_SF_dur_event_info,           event information
                                        UF_SF_boundary_condition_info,  specify bc tags
                                        UF_SF_material_info,            specify solid or
                                                                        sheet body or mesh
                                                                        tags to display
                                                                        material info for.
                                        UF_SF_section_info,             specify the tag of
                                                                        the curve, edge,
                                                                        point, or mesh
                                                                         which is
                                                                        associated to the
                                                                        section you
                                                                        want information
                                                                        about.
                                        UF_SF_mesh_mating_condition_info specify the tags
                                                                         of the assembly
                                                                         mesh that you want
                                                                         info about.  This
                                                                         tag is returned
                                                                         from
                                        UF_SF_locate_mesh_mating_condition_by_name
                                      */
const char *output_file_with_path     /*<I> Full path including filename of file
                                            where results of model check should be
                                            written.  Caller is responsible for
                                            allocating and deallocating this array.
                                      */
);

/******************************************************************************
  This function resets all element IDs, starting at a specified ID.
  Each time you update a Scenario model, the mesher numbers elements
  starting from the highest available ID when it remeshes the model.
  After multiple updates, element ID numbers can become too high.
  Use this function to reset the element IDs.

  This call works only when a FEM part is the work part

Environment: Internal  and  External

See Also:

History: Originally released in NX3
******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_reset_element_ids
(
    int start_id   /*<I> Start ID */
);

/******************************************************************************
  This function resets all node IDs, starting at a specified ID.
  Each time you update a Scenario model, the mesher numbers nodes
  starting from the highest available ID when it remeshes the model.
  After multiple updates, node ID numbers can become too high.
  Use this function to reset the node IDs.

  This call works only when a FEM part is the work part

Environment: Internal  and  External

See Also:

History: Originally released in NX3
******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_reset_node_ids
(
    int start_id   /*<I> Start ID */
);

/******************************************************************************
  This function determines if a given object is a midsurface

Environment: Internal  and  External

See Also:

History: Originally released in NX2
******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_is_midsrf
(
   tag_t     sheet_body_tag,     /*<I> Tag of given object */
   logical  *is_midsrf,          /*<O> Flag signifying the outcome:
                                       = TRUE -->  object is a Midsurface
                                       = FALSE --> object is NOT a Midsurface
                                 */
   int      *midsrf_type,        /*<O> Tag of the midsurface feature
                                       if the object is associated with such a feature.
                                 */
   tag_t    *feature_tag         /*<O> Tag of the midsurface feature
                                       if the object is associated with such a feature.
                                       NOTE: If the midsurface is facepair type the
                                       feature of the facepair has as midsurface body
                                       the given sheet body.
                                 */
) ;

/******************************************************************************
Frees an instance of UF_SF_midsrf_user_parms_t structure.

Environment: Internal  and  External

See Also:

History: Originally released in NX2
******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_free_midsrf_user_parms
(
    UF_SF_midsrf_user_parms_p_t parms_p /*<I> Midsurface user defined parms to free. */
);

/******************************************************************************
  This function determines the type of a midsurface feature

Environment: Internal  and  External

See Also:

History: Originally released in NX2
******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_ask_midsrf_frec_type
(
   tag_t     feature_tag,      /*<I> Tag of given feature*/
   int      *midsrf_type       /*<O> Type of midsurface if object is a midsurface
                                      = UF_SF_MIDSRF_FACEPAIR_METHOD
                                      = UF_SF_MIDSRF_OFFSET_METHOD
                                      = UF_SF_MIDSRF_USER_DEF_METHOD
                                      = UF_SF_MIDSRF_NON_EXIST -> If feature is not a midsurface
                               */
);

/******************************************************************************
  This function determines the parent midsurface feature of a given facepair
  feature.

Environment: Internal  and  External

See Also:

History: Originally released in NX2
******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_facepair_ask_midsrf_frec
(
   tag_t     facepair_feature_tag,      /*<I> facepair_feature_tag
                                              Tag of given facepair feature
                                        */
   tag_t    *midsrf_feature_tag         /*<O> Tag of parent feature of given
                                              facepair feature.
                                        */
);

/******************************************************************************
  This function will create a 3d Hex mesh in a solid body.

Environment: Internal  and  External

See Also:

History: Originally released in NX2
******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_create_swept_hex_mesh
(
    tag_t   solid_body,                /*<I> The tag of the polygon solid body to mesh*/
    tag_t   source_face,               /*<I> The tag of the face to use as the
                                             source polygon face for sweeping.*/
    logical midnodes,                  /*<I> If TRUE,  Hex20s will be created.
                                             If FALSE, Hex8s  will be created.
                                       */
    double  elem_size,                 /*<I> Desired element size. This will be used
                                             to mesh the source polygon face and determine the
                                             number of sweeping layers.
                                       */
    tag_p_t mesh_tag                   /*<O> The tag of the mesh created.*/
);

/******************************************************************************
  This function updates a structures part file.

  This call works only when a FEM part is the work part

  Returns
   int       error        = 0 --> Success
                          = UF_SF_NON_SCENARIO_PART -> Not a scenario file

Environment: Internal  and  External

See Also:

History: Originally released in V17.0
******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_update_scenario ( void );

/**************************************************************************
Given an input object this function returns the corresponding object in the
  current work part

   This function was written to aid users who have developed applications based
   on the Pre-NX4 data model that had a single scenario part the referenced a master cad
   part.  When Pre-NX4 structures scenario parts are migrated to NX4 the data in the scenario
   will be moved into one of the following 3 parts.  assumes the following part hierachy:
         Sim part     ( loads, contraints & solution data)
            |
            V
          Fem Part    ( CAE Geometry, Meshes, Elements & node)
            |
            V
       Idealized Part ( Modeling data, idealize feature, midsurfaces ......   )  Optional layer
            |
            V
       Master Cad Part


   At this time the only mappings we will support are:

    Part where
    input object          Current work
    exists                part type
    ===============       =============    ===============
    Idealized part    ==> Fem part         Returns mapped object if possible
    Idealized part    ==> Sim part         Returns mapped object if possible

    Fem part          ==> Sim part         Returns mapped object if possible

    Cad part          ==> Cad part         Return input tag
    Idealized part    ==> Idealized part   Return input tag
    Fem part          ==> Fem part         Return input tag
    Sim part          ==> Sim part         Return input tag


Environment: Internal  and  External

See Also:

History: Originally released in NX4.0
*********************************************************************/
extern UFUN_CAEEXPORT tag_t UF_SF_map_object_to_current_part
(
    tag_t           object_tag  /* <I> Tag of a object to be mapped */
);

/**************************************************************************
Returns the master part for the given idealized part  ( NULL_TAG if no master part exists )

Environment: Internal  and  External

See Also:

History: Originally released in NX4.0
*********************************************************************/
extern UFUN_CAEEXPORT tag_t UF_SF_idealized_part_ask_master_part
(
    tag_t           idealized_part_tag  /* <I> Tag of a Idealized Part */
);

/**************************************************************************
Returns true if the input tag is a idealized part

Environment: Internal  and  External

See Also:

History: Originally released in NX4.0
*********************************************************************/
extern UFUN_CAEEXPORT logical UF_SF_is_idealized_part
(
    tag_t           idealized_part_tag  /* <I> Tag of a Idealized Part */
);


/**************************************************************************
Creates fem part file

Environment: Internal  and  External

See Also:

History: Originally released in NX4.0
*********************************************************************/
extern UFUN_CAEEXPORT int UF_SF_create_fem
(
    const char*     fem_name,           /* <I> Name of FEM part file to create.                     */
    tag_t           cad_part_tag,       /* <I> Tag of the CAD part to associate the FEM to.
                                               Pass NULL_TAG to create a stand-alone FEM part       */
    const char*     idealized_part_name,/* <I> Name of the Idealized part.
                                               Pass NULL for no Idealized part                      */
    logical         use_all_bodies_flag,/* <I> Flag indicating whether to use all bodies or not     */
    int             num_bodies,         /* <I> Number of bodies to use in creating the FEM
                                               Valid only when use_all_bodies_flag == false          */
    const tag_t*    body_tags,          /* <I,len:num_bodies> List of body tags to use in creating the FEM
                                               Valid only when use_all_bodies_flag == false          */
    const char*     solver_name,        /* <I> The name of the solver.
                                               Available solvers are:
                                                    "NX NASTRAN",
                                                    "MSC NASTRAN",
                                                    "ANSYS",
                                                    "ABAQUS",
                                                    "NX THERMAL / FLOW"
                                                    "NX NASTRAN DESIGN"                             */
    const char*     analysis_type_name, /* <I> The name of the analysis type.
                                               Available analysis types are:
                                               For "NX NASTRAN", "MSC NASTRAN", "ANSYS" & "ABAQUS":
                                                    "Structural",
                                                    "Thermal",
                                                    "Axisymmetric Structural",
                                                    "Axisymmetric Thermal"
                                               For "NX THERMAL / FLOW":
                                                    "Thermal"
                                                    "Flow"
                                                    "Coupled Thermal-Flow"
                                               For "NX NASTRAN DESIGN":
                                                    "Structural",
                                                    "Thermal"                                       */
    int             num_desc_lines,     /* <I> Number of lines in the FEM description.              */
    const char**    description,        /* <I,len:num_desc_lines> Description of this FEM part.                        */
    tag_t*          new_fem_tag         /* <O> Tag of created FEM part file.                        */
);

/**************************************************************************
Creates fem part file with geometry options

Environment: Internal  and  External

See Also:

History: Originally released in NX4.0.4
*********************************************************************/
extern UFUN_CAEEXPORT int UF_SF_create_fem_with_geom_opts
(
    const char*          fem_name,           /* <I> Name of FEM part file to create.                     */
    tag_t                cad_part_tag,       /* <I> Tag of the CAD part to associate the FEM to.
                                                    Pass NULL_TAG to create a stand-alone FEM part       */
    const char*          idealized_part_name,/* <I> Name of the Idealized part.
                                                    Pass NULL for no Idealized part                      */
    logical              use_all_bodies_flag,/* <I> Flag indicating whether to use all bodies or not     */
    int                  num_bodies,         /* <I> Number of bodies to use in creating the FEM
                                                    Valid only when use_all_bodies_flag == true          */
    const tag_t*         body_tags,          /* <I> List of body tags to use in creating the FEM
                                                    Valid only when use_all_bodies_flag == true          */
    const char*          solver_name,        /* <I> The name of the solver.
                                                    Available solvers are:
                                                         "NX NASTRAN",
                                                         "MSC NASTRAN",
                                                         "ANSYS",
                                                         "ABAQUS",
                                                         "NX THERMAL / FLOW"
                                                         "NX NASTRAN DESIGN"                             */
    const char*          analysis_type_name, /* <I> The name of the analysis type.
                                                    Available analysis types are:
                                                    For "NX NASTRAN", "MSC NASTRAN", "ANSYS" & "ABAQUS":
                                                         "Structural",
                                                         "Thermal",
                                                         "Axisymmetric Structural",
                                                         "Axisymmetric Thermal"
                                                    For "NX THERMAL / FLOW":
                                                         "Thermal"
                                                         "Flow"
                                                         "Coupled Thermal-Flow"
                                                    For "NX NASTRAN DESIGN":
                                                         "Structural",
                                                         "Thermal"                                       */
    int                  num_desc_lines,     /* <I> Number of lines in the FEM description.              */
    const char**         description,        /* <I,len:num_desc_lines> Description of this FEM part.                        */
    UF_SF_geom_options_t geom_options,       /* <I> Geometry options                                     */
    tag_t*               new_fem_tag         /* <O> Tag of created FEM part file.                        */
);

/**************************************************************************
Returns the cad part for the given Fem  ( NULL_TAG if no cad part exists )

Environment: Internal  and  External

See Also:

History: Originally released in NX4.0
*********************************************************************/
extern UFUN_CAEEXPORT tag_t UF_SF_fem_ask_cad_part
(
    tag_t           fem_tag,            /* <I> Tag of a Fem */
    logical*        is_idealized_part   /* <O> True if cad part returned is an idealized part */
);

/**************************************************************************
Returns true if the input tag is a Fem

Environment: Internal  and  External

See Also:

History: Originally released in NX4.0
*********************************************************************/
extern UFUN_CAEEXPORT logical UF_SF_is_fem
(
    tag_t           fem_tag     /* <I> Tag of a fem */
);

/**************************************************************************
Creates Simulation part file

Environment: Internal  and  External

See Also:

History: Originally released in NX4.0
*********************************************************************/
extern UFUN_CAEEXPORT int UF_SF_create_simulation
(
    const char*     simulation_name,    /* <I> Name of Simulation part file to create. */
    tag_t           fem_tag,            /* <I> Tag of the FEM part to create the Simulation on. */
    int             num_desc_lines,     /* <I> Number of lines in the Simulation description. */
    const char**    description,        /* <I,len:num_desc_lines> Description of this Simulation part. */
    tag_t*          new_simulation_tag  /* <O> Tag of created Simulation part file. */
);

/**************************************************************************
Returns the Fem for the given Simulation  ( NULL_TAG if no fem exists )

Environment: Internal  and  External

See Also:

History: Originally released in NX4.0
*********************************************************************/
extern UFUN_CAEEXPORT tag_t UF_SF_simulation_ask_fem
(
    tag_t           simulation_tag     /* <I> Tag of a Simulation */
);

/**************************************************************************
Returns true if the input tag is a Simulation

Environment: Internal  and  External

See Also:

History: Originally released in NX4.0
*********************************************************************/
extern UFUN_CAEEXPORT logical UF_SF_is_simulation
(
    tag_t           simulation_tag     /* <I> Tag of a Simulation */
);



/****************************************************************************
* Creates automatically mesh mating conditions from an array of polygon bodies.
*
* Environment: Internal  and  External
*
* See Also:
*
* History:
******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_auto_create_mesh_mating_condition
(
int             entity_num,             /*<I> Number of entities in array */
tag_t           entity_array[],         /*<I,len:entity_num>
                                         Array of tags of the entities (polygon bodies)
                                        */
double          merge_tolerance,        /*<I> Merge tolerance for assembly mesh*/
int             make_mesh_coincident,   /*<I> Make Mesh Coincident switch (0 or 1)*/
int             coincident_face_only,   /*<I> Coincident face switch (0 or 1)*/
int             mesh_mating_type,       /*<I> Mesh mating type
                                              = 0 --> GLUE
                                              = 3 --> FREE
                                              NOTE: There is no 1 or 2 Type
                                        */
int            *num_assembly_meshes,    /*<O> Number of assembly mesh tags created*/
tag_t         **assembly_meshes         /*<OF,len:num_assembly_meshes>
                                              Array of assembly mesh tags created
                                              Free when done
                                        */
);

/****************************************************************************
*  Exports html files comprising the report generated by UF_SF_create_report.
*  Valid only when a Simulation part is the work part
*
* Environment: Internal or External
*
* See Also:
*
* History: Released in NX3
*****************************************************************************/
extern   UFUN_CAEEXPORT int     UF_SF_write_report ( void );

/****************************************************************************
* Creates the Scenario report objects based on a template file.
* Valid only when a Simulation part is the work part
*
* Environment: Internal or External
*
* See Also:
*
* History: Released in NX3
*****************************************************************************/
extern   UFUN_CAEEXPORT int     UF_SF_create_report ( void );

/************************************************************************************
 * Creates a hardpoint associated to either a face, an edge or curve.  This hardpoint
 * will then be honored by any meshing operation performed on that edge or face.
 *
 * Environment: Internal or External
 *
 * See Also:
 *
 * History: Released in NX3
 * **********************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_create_hardpoint_on_geom
(
    tag_t geom_tag,         /*<I> The tag of the geometry that the hardpoint
                                  should be associated to.  This geometry can
                                  be either a face, an edge or a curve. */
    double ref_point[3],    /*<I> The 3d location of reference point in absolute csys.
                                  The actual hardpoint location will be determined
                                  by projecting this point on to a face or computing
                                  minimum distance of this point to an edge or curve. */
    tag_p_t hardpoint_tag   /*<O> The tag of the hardpoint created */
);

/****************************************************************************
Given a property tag, returns the name of the property.

Environment: Internal and External

See Also:

History: Originally released in NX3.0
***************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_property_ask_name_nx (
tag_t property_tag,     /* <I>
                        The tag of the property.
                        */
char** property_name_pp /* <OF>
                        The name of the property.
                        NOTE: Caller must UF_free the string.
                        */
);

/****************************************************************************
Given a property tag, returns the property type.

Environment: Internal and External

See Also:

History: Originally released in NX3.0
***************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_property_ask_type_nx (
tag_t property_tag,                     /* <I>
                                        The tag of the property.
                                        */
UF_SF_fem_value_type_t *property_type /* <O>
                                      The property type.
                                      */
);

/****************************************************************************
Sets a property value.

Environment: Internal and External

See Also:

History: Originally released in NX3.0
***************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_property_set_value_nx (
tag_t       property_tag, /* <I>
                          The tag of the property.
                          */
logical bool_value, /* <I>
                    Property value, if type SFOM_FEM_VALUE_BOOL.
                    */
int int_value, /* <I>
               Property value, if type is one of the following:
                UF_SF_FEM_VALUE_INT
                UF_SF_FEM_VALUE_ENUM
               */
double scalar_value, /* <I>
                     Property value, if type is UF_SF_FEM_VALUE_SCALAR.
                     */
char* const text_value,  /* <I>
                         Property value, if type is UF_SF_FEM_VALUE_TEXT.
                         */
int num_lines,  /* <I>
                If type is UF_SF_FEM_VALUE_MULTI_STRING, this is the number
                of text lines in the property.
                */
char** const multi_text_value /* <I,len:num_lines>
                              If type is UF_SF_FEM_VALUE_MULTI_STRING, this
                              is the array of text lines in the property.
                              */
);

/****************************************************************************
Given a property tag, returns the property value.

Environment: Internal and External

See Also:

History: Originally released in NX3.0
***************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_property_ask_value_nx (
tag_t  property_tag, /* <I>
                     The tag of the property.
                     */
logical *bool_value,/* <O>
                     Property value, if type SFOM_FEM_VALUE_BOOL.
                     */
int    *int_value,   /* <O>
                     Property value, if type is one of the following:
                     UF_SF_FEM_VALUE_INT
                     UF_SF_FEM_VALUE_ENUM
                     */
double *scalar_value,/* <O>
                     Property value, if type UF_SF_FEM_VALUE_SCALAR.
                     */
char** text_value,   /* <OF>
                     Property value, if type is UF_SF_FEM_VALUE_TEXT.

                     NOTE: Caller must UF_free the string.
                     */
int *num_lines,     /* <O>
                    If type is UF_SF_FEM_VALUE_MULTI_STRING, this is the number
                    of text lines in the property.
                    */
char*** multi_text_value   /* <OF,len:num_lines>
                           If type is UF_SF_FEM_VALUE_MULTI_STRING, this
                           is the array of text lines in the property.

                           NOTE: Call UF_free_string_array to free the
                           storage allocated within the structure.
                           */
);

/****************************************************************************
Initiates solve of the active solution.

Environment: Internal and External

See Also:

History: Originally released in NX3.0
***************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_solve_active_solution_nx (
int format_choice /* <I>
                  Format/Solve option
                  0 (for format and solve)
                  1 (for format only)
                  */
);

/****************************************************************************
Given a solution descriptor tag, returns the solution descriptor name.

Environment: Internal and External

See Also:

History: Originally released in NX3.0
***************************************************************************/
extern UFUN_CAEEXPORT int UF_SFL_solution_descriptor_ask_name_nx (
tag_t sol_desc_tag, /* <I>
                    Solution descriptor tag.
                    */
char** name_pp      /* <OF>
                    The name of the solution descriptor.
                    NOTE: Caller must UF_free the string.
                    */
);

/****************************************************************************
Given a solution descriptor tag, returns the number of allowable step
descriptors. An allowable step descriptor defines a step type that is valid for
a given solution type.

Valid only if the work part is a Simulation.

Environment: Internal and External

See Also:

History: Originally released in NX3.0
***************************************************************************/
extern UFUN_CAEEXPORT int UF_SFL_solution_ask_num_allowable_step_descriptors_nx (
tag_t sol_desc_tag,       /* <I>
                          Solution descriptor tag.
                          */
int* num_allow_step_descs /* <O>
                          The number of allowable step descriptors.
                          */
);

/****************************************************************************
Given a solution descriptor tag and index into the allowable step descriptor
list, returns the tag of the allowable step descriptor.

This function can be used to loop over all allowable step descriptors for a
given solution descriptor.

The number of allowable step descriptors can be obtained from function
UF_SFL_solution_ask_num_allowable_step_descriptors_nx.

The index is just a counter.
Valid indices are from 0 to (number of allowable step descriptors-1).

Valid only if the work part is a Simulation.

Environment: Internal and External

See Also:

History: Originally released in NX3.0
***************************************************************************/
extern UFUN_CAEEXPORT int UF_SFL_solution_ask_nth_allowable_step_descriptor_nx (
tag_t sol_desc_tag,        /* <I>
                           Solution descriptor tag.
                           */
int   index,               /* <I>
                           Index into list of allowable step descriptors.
                           Valid indices are from 0 to (number of allowable
                           step descriptors-1).
                           The number of allowable step descriptors can be
                           obtained from function
                           UF_SFL_solution_num_allowable_step_descriptors_nx.
                           */
tag_t *step_descriptor_tag /* <O>
                           The tag of the allowable step descriptor.
                           */
);

/****************************************************************************
Given a solution descriptor tag and allowable step descriptor name,
returns the tag of the step descriptor.

Valid only when the work part is a Simulation.

Environment: Internal and External

See Also:

History: Originally released in NX3.0
***************************************************************************/
extern UFUN_CAEEXPORT int UF_SFL_solution_ask_step_descriptor_nx (
tag_t sol_desc_tag,        /* <I>
                           Solution descriptor tag.
                           */
const char * step_desc_name,               /* <I>
                           Step descriptor name.
                           */
tag_t *step_descriptor_tag /* <O>
                           The tag of the allowable step descriptor.
                           */
);


/****************************************************************************
Identifies whether a lbc descriptor is valid for a given solution descriptor.

Environment: Internal and External

See Also:

History: Originally released in NX3.0
***************************************************************************/
extern UFUN_CAEEXPORT int UF_SFL_solution_ask_lbc_desc_valid_nx (
tag_t sol_desc_tag, /* <I>
                    Solution descriptor tag.
                    */
tag_t lbc_desc_tag, /* <I>
                    LBC descriptor tag.
                    */
logical *valid      /* <O>
                    True if the lbc descriptor is valid for the solution,
                    otherwise false.
                    */
);


/****************************************************************************
Given a step descriptor tag, returns the step descriptor name.

Environment: Internal and External

See Also:

History: Originally released in NX3.0
***************************************************************************/
extern UFUN_CAEEXPORT int UF_SFL_step_descriptor_ask_name_nx (
tag_t step_desc_tag,                /* <I>
                                    Step descriptor tag.
                                    */
char** name_pp                      /* <OF>
                                    The name of the step descriptor.
                                    NOTE: Caller must UF_free the string.
                                    */
);

/****************************************************************************
Identifies whether a lbc descriptor is valid for a given step descriptor.

Environment: Internal and External

See Also:

History: Originally released in NX3.0
***************************************************************************/
extern UFUN_CAEEXPORT int UF_SFL_step_ask_lbc_desc_valid_nx (
tag_t step_desc_tag,                /* <I>
                                    Step descriptor tag.
                                    */
tag_t lbc_desc_tag,                 /* <I>
                                    LBC descriptor tag.
                                    */
logical *valid                      /* <O>
                                    True if the lbc descriptor is valid for
                                    the step, otherwise false.
                                    */
);

/****************************************************************************
Returns number of solvers.

Valid only when the work part is a Simulation

Environment: Internal and External

See Also:

History: Originally released in NX3.0
***************************************************************************/
extern UFUN_CAEEXPORT int UF_SFL_ask_num_solvers_nx (
int *num_solvers /* <O>
                 The number of solvers.
                 */
);

/****************************************************************************
Given a index into the list of solvers, returns the tag of the solver
descriptor. This function can be used to loop over all solver descriptors.

The number of solver descriptors can be obtained from function
UF_SFL_ask_num_solvers_nx.

The index is just a counter.
Valid indices are from 0 to (number of solver descriptors-1).

Valid only if the work part is a Simulation.

Environment: Internal and External

See Also:

History: Originally released in NX3.0
***************************************************************************/
extern UFUN_CAEEXPORT int UF_SFL_ask_nth_solver_nx (
int     index,                         /* <I>
                                       Index into list of solvers.
                                       Valid indices are from 0 to (number of
                                       solvers-1).
                                       The number of solvers can be obtained
                                       from function UF_SFL_ask_num_solvers.
                                       */
tag_t   *solver_desc_tag               /* <O>
                                       The tag of the solver descriptor.
                                       */
);

/****************************************************************************
Given a solver name, returns the tag of the solver descriptor.

Valid only when the work part is a Simulation

Environment: Internal and External

See Also:

History: Originally released in NX3.0
***************************************************************************/
extern UFUN_CAEEXPORT int UF_SFL_ask_solver_nx
(
const char* solver_name,               /* <I>
                                       Name of the solver.
                                       */
tag_t       *solver_desc_tag           /* <O>
                                       The tag of the solver descriptor.
                                       */
);

/****************************************************************************
Given a solver descriptor, returns number of languages that are valid for
the solver.

Valid only if the work part is a Simulation

Environment: Internal and External

See Also:

History: Originally released in NX3.0
***************************************************************************/
extern UFUN_CAEEXPORT int UF_SFL_ask_num_languages_nx
(
tag_t solver_desc_tag,              /* <I>
                                    Solver descriptor tag.
                                    */
int *num_languages                  /* <O>
                                    The number of languages.
                                    */
);

/****************************************************************************
Given a solver descriptor tag and index into the solver's language list,
returns the tag of the language. This function can be used to loop over all
languages that are valid for the solver.

The number of languages for the solver can be obtained from function
UF_SFL_ask_num_languages_nx.

The index is just a counter.
Valid indices are from 0 to (number of languages-1).

Valid only if the work part is a Simulation

Environment: Internal and External

See Also:

History: Originally released in NX3.0
***************************************************************************/
extern UFUN_CAEEXPORT int UF_SFL_ask_nth_language_nx
(
tag_t   solver_desc_tag,               /* <I>
                                       Solver descriptor tag.
                                       */
int     index,                         /* <I>
                                       Index into list of languages.
                                       Valid indices are from 0 to (number of
                                       languages-1).
                                       The number of languages can be obtained
                                       from function UF_SFL_ask_num_languages_nx.
                                       */
tag_t   *language_tag                  /* <O>
                                       The tag of the language.
                                       */
);

/****************************************************************************
Given a solver descriptor tag and language name, returns the
tag of the language.

Valid only if the work part is a Simulation

Environment: Internal and External

See Also:

History: Originally released in NX3.0
*****************************************************************************/
extern UFUN_CAEEXPORT int UF_SFL_ask_language_nx
(
tag_t       solver_desc_tag,              /* <I>
                                          Solver descriptor tag.
                                          */
const char* lang_name,                    /* <I>
                                          Name of the language.
                                          */
tag_t       *language_tag                 /* <O>
                                          The tag of the language.
                                          */
);

/****************************************************************************
*    This routine allocates an instance of UF_SF_defeature_parms_t structure
*    used to hold all information needed to create a defeature feature.
*
*    The structure is allocated and the retained_faces, removed_faces fields
*    are set from the corresponding input parameters.
*    The region substructure will be allocated and initialized to the values
*    of the input parameters that define the region.
*
* Environment: Internal  and  External
*
* History: Originally released in NX3.0
*****************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_alloc_defeature_parms
(

    int                       num_ret_faces,  /* <I>
                                              Number of retained faces in the
                                              retained_faces array.  Can be 0
                                              */
    tag_t                    *ret_faces_a,    /* <I,len:num_ret_faces>
                                              Array of retained faces.
                                              Can be NULL if num_bnd_faces == 0
                                              */
    int                       num_rem_faces,  /* <I>
                                              Number of removed faces in the
                                              removed_faces array.  Can be 0
                                              */
    tag_t                    *rem_faces_a,   /* <I,len:num_rem_faces>
                                              Array of retained faces.
                                              Can be NULL if num_bnd_faces == 0
                                             */
    tag_t                     seed_face,      /* <I>
                                              Seed face for the region
                                              (required to derive the body)
                                              */
    int                       num_bnd_faces,  /* <I>
                                              Number of boundary faces in the
                                              bnd_faces array.  Can be 0
                                              */
    tag_t                     *bnd_faces,     /* <I,len:num_bnd_faces>
                                              Array of boundary faces.
                                              Can be NULL if num_bnd_faces == 0
                                              */
    tag_t                     angle_exp,      /* <I>
                                              Expression to be used for the tagential
                                              edge angle which is used for the region
                                              boundary, Can be NULL_TAG
                                              */
    UF_SF_defeature_parms_p_t *defeature_parms_p
                                              /* <OF,free:UF_SF_free_defeature_parms>
                                              Idealize region entity created.
                                              Use UF_SF_free_defeature_parms
                                              to free.
                                              */
);

/****************************************************************************
*   This routine frees memory associated with an allocated instance of the
*   UF_SF_defeature_parms_s structure used to define the parameters of a
*   defeature feature
*
* Environment: Internal  and  External
*
* History: Originally released in NX3.0
*****************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_free_defeature_parms
(
  UF_SF_defeature_parms_p_t   def_parms_p  /* <I>
                                            Defeature parameter entity to free
                                           */
);


/*****************************************************************************
*    This routine creates a defeature feature for specified set of faces of the
*   body that either define a region or are explicitly selected, or both.
*
*   This routine takes a region object and an idealize parms object that is
*   set to the desired operations and creates an idealize feature.
*   Since removal of all specified faces and edges is not guarenteed,
*   returned are the edges of all failing wounds (edges of the face or hole
*   edge in a sheet body).
*
* Environment: Internal  and  External
*
* History: Originally released in NX3.0
*******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_create_defeature_body
(

   UF_SF_defeature_parms_p_t   defeature_parms_p,
                                /* <I>
                                Parameters that define a set of faces on a
                                body to be simplified.
                                The body is derived from a seed face.
                                The faces may be extracted automatically
                                based on the parameters that define a
                                region, or they can be specified
                                explicitly, or both.
                                */
  tag_t    *feature_tag,        /* <O>
                                The feature created
                                */
  int   *n_failing_wound_edges, /* <O>
                                Number of edges of failing wounds
                                */
  tag_t **failing_wound_edges   /* <OF,len:n_failing_wound_edges>
                                Array of edges of failing wounds.
                                This must be freed by calling UF_free.
                                */
);

/****************************************************************************
    This routine edits a defeature feature

    This routine takes the feature tag of a defeature feature and edits
    it according to the new parmater object definition.  Since removal
    of all specified faces and edges is not guarenteed, returned are the edges
    of all failing wounds (edges of the face or hole edge in a sheet body).
    idealize feature associated to a body region.

Environment: Internal  and  External

History: Originally released in NX3.0
*****************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_edit_defeature_parms
(
  tag_t   feature_tag,         /* <I>
                               The defeature feature
                               */
  UF_SF_defeature_parms_p_t   defeature_parms_p,
                               /* <I>
                               Parameters that define a set of faces on a
                               body to be simplified.
                               The body is derived from a seed face.
                               The faces may be extracted automatically
                               based on the parameters that define a
                               region, or they can be specified
                               explicitly, or both.
                               */
  int *n_failing_wound_edges,  /* <O>
                               The number of failing wound edges
                               */
  tag_t **failing_wound_edges  /* <OF,len:n_failing_wound_edges>
                               Array of failing wound edges.  This must be
                               freed by calling UF_free.
                               */
);

/****************************************************************************
This function will return the tag of a Durability Solution, given its name.

Valid only when the work part is a Simulation.

Environment: Internal  and  External

History: Originally released in NX3.0
*****************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_locate_named_dursol_nx(
const char* dursol_name, /* <I>
                         Name of the durability solution
                         The buffer must be declared using MAX_LINE_BUFSIZE so it can hold MAX_LINE_NCHARS characters. 
                         */
tag_t*  dursol_tag /* <O>
                   Tag of the durability solution with the specified name.
                               */
);

/****************************************************************************
This function will return the number of Durability Solutions.

Valid only when the work part is a Simulation.

Environment: Internal  and  External

History: Originally released in NX3.0
*****************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_ask_num_dursols_nx (
int *num_dursols   /* <O>
                   Number of Durability Solutions.
                   */
);

/****************************************************************************
This function will return the tag of the specified Durability Solution.

UF_SF_ask_nth_dursol_nx

Environment: Internal  and  External

History: Originally released in NX3.0
*****************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_ask_nth_dursol_nx (
int    index,     /* <I>
                  Index of the Durability Solution.
                  Valid range is
                        0 : (number of Durability Solutions)-1
                  */
tag_t *dursol_tag /* <O>
                  Durability Solution tag.
                  */
);

/****************************************************************************
This function will create a Durability Solution.
From NX7.5, this function will create a durability metasolution
and a default static event referring to the solution tag.

Richer features are available in NXOpen.
Valid only when the work part is a Simulation.

Environment: Internal  and  External

History: Originally released in NX3.0
*****************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_create_dursol_nx (
const char* name,   /* <I>
                    Durability Solution name.
                    */
tag_t solution_tag, /* <I>
                    Tag of the solution.
                    */
tag_t *dursol_tag   /* <O>
                    Durability Solution tag.
                    */
);

/****************************************************************************
This function will delete a Durability solution.

Valid only when the work part is a Simulation.

Environment: Internal  and  External

History: Originally released in NX3.0
*****************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_delete_dursol_nx (
tag_t dursol_tag /* <I>
                 Durability Solution tag.
                 */
);

/****************************************************************************
This function will ask a Durability Solution's values.
From NX7.5, this function will return the metasolution name, followed by
parameters from the first static event. If the static event is not available,
an error will be returned.

Valid only when the work part is a Simulation.

Environment: Internal  and  External

History: Originally released in NX3.0
*****************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_ask_dursol_nx (
tag_t             dursol_tag,              /* <I>
                                           Durability Solution tag.
                                           */
char              dursol_name[MAX_LINE_BUFSIZE],             /* <O>
                                           Name of Durability Solution.
                                           The buffer must be declared using MAX_LINE_BUFSIZE so it can hold MAX_LINE_NCHARS characters. 
                                           If NULL, value will not be returned.
                                           */
tag_t             *solution_tag,           /* <O>
                                           Tag of the solution
                                           If NULL, value will not be returned.
                                           */
UF_SF_dursol_stress_criterion_t
                  *stress_criterion,       /* <O>
                                           Stress criterion
                                           If NULL, value will not be returned.
                                           */
UF_SF_dursol_stress_type_t
                  *stress_type,            /* <O>
                                           Stress type
                                           If NULL, value will not be returned.
                                           */
UF_SF_dursol_design_life_criterion_t
                  *design_life_criterion,  /* <O>
                                           Design life criterion
                                           If NULL, value will not be returned.
                                           */
int               *fatigue_cycles,         /* <O>
                                           Number of fatigue duty cycles
                                           If NULL, value will not be returned.
                                           */
double            *k_factor,               /* <O>
                                           Fatigue strength factor (Kf)
                                           If NULL, value will not be returned.
                                           */
UF_SF_dursol_fatigue_life_criterion_t
                  *fatigue_life_criterion, /* <O>
                                           Fatigue life criterion
                                           If NULL, value will not be returned.
                                           */
int               *design_cycles           /* <O>
                                           Number of design cycles desired for
                                           fatigue strength.
                                           If NULL, value will not be returned.
                                           */
);

/****************************************************************************
This function will edit a Durability Solution's values.
From NX7.5, this function will edit the metasolution name, followed by
parameters of the first static event. If the static event is not available,
an error will be returned.

Valid only when the work part is a Simulation.

Environment: Internal  and  External

History: Originally released in NX3.0
*****************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_edit_dursol_nx (
tag_t             dursol_tag,              /* <I>
                                           Durability Solution tag.
                                           */
const char*       dursol_name,             /* <I>
                                           Name of Durability Solution.
                                           The buffer must be declared using MAX_LINE_BUFSIZE so it can hold MAX_LINE_NCHARS characters.
                                           If NULL, value will not be modified.
                                           */
UF_SF_dursol_stress_criterion_t
                  *stress_criterion,       /* <I>
                                           Stress criterion
                                           If NULL, value will not be modified.
                                           */
UF_SF_dursol_stress_type_t
                  *stress_type,            /* <I>
                                           Stress type
                                           If NULL, value will not be modified.
                                           */
UF_SF_dursol_design_life_criterion_t
                  *design_life_criterion,  /* <I>
                                           Design life criterion
                                           If NULL, value will not be modified.
                                           */
int               *fatigue_cycles,         /* <I>
                                           Number of fatigue duty cycles
                                           If NULL, value will not be modified.
                                           */
double            *k_factor,               /* <I>
                                           Fatigue strength factor (Kf)
                                           If NULL, value will not be modified.
                                           */
UF_SF_dursol_fatigue_life_criterion_t
                  *fatigue_life_criterion, /* <I>
                                           Fatigue life criterion
                                           If NULL, value will not be returned.
                                           */
int               *design_cycles           /* <I>
                                           Number of design cycles desired for
                                           fatigue strength.
                                           If NULL, value will not be returned.
                                           */
);

/****************************************************************************
This function will add a Durability Load to a Durability Solution.
Valid only when the work part is a Simulation.
From NX7.5, this command will do nothing. A load when created has been automatically
added to the static event it belongs to.
Environment: Internal  and  External

History: Originally released in NX3.0
*****************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_dursol_add_load_nx (
tag_t dursol_tag,  /* <I>
                   Durability Solution tag
                   */
tag_t lv_tag       /* <I>
                   Load Variation tag
                   */
);

/****************************************************************************
This function will remove a Durability Load from a Durability Solution.

Valid only when the work part is a Simulation.

Environment: Internal  and  External

History: Originally released in NX3.0
*****************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_dursol_remove_load_nx (
tag_t dursol_tag, /* <I>
                  Durability Solution tag
                  */
tag_t lv_tag      /* <I>
                  Load Variation tag
                  */
);

/****************************************************************************
This function returns the number of Load Variations defined for
the specific Durability Solution.
From NX7.5, this function will return the number of load variations
on the first available static event in the durability solution.
Valid only when the work part is a Simulation.

Environment: Internal  and  External

History: Originally released in NX3.0
*****************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_dursol_ask_load_count_nx (
tag_t dursol_tag, /* <I>
                  Durability Solution tag
                  */
int   *num_lv     /* <O>
                  Number of load variations found.
                  */
);

/****************************************************************************
This function returns the tag of the specified Load Variation in the
Durability Solution.
From NX7.5, this function will return the nth load variation
on the first available static event in the durability solution.

Valid only when the work part is a Simulation.

Environment: Internal  and  External

History: Originally released in NX3.0
*****************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_dursol_ask_load_nx (
tag_t dursol_tag, /* <I>
                  Durability Solution tag
                  */
int   lv_index,   /* <I>
                  The index of the Load Variation.
                  Valid range is
                       0 : (number of Load Variations)-1
                  */
tag_t *lv_tag     /* <O>
                  Tag of Load Variation
                  */
);

/****************************************************************************
This function will return all the load variation object tags and the total
count for the given Durability Solution.

Valid only when the work part is a Simulation.

Environment: Internal  and  External

History: Originally released in NX3.0
*****************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_dursol_locate_all_members_nx (
tag_t         dursol_tag,      /* <I>
                               Durability Solution tag
                               */
int*          num_lv,          /* <O>
                               Number of Load Variations
                               */
tag_p_t*      lv_pp            /* <OF,len:num_lv>
                               List of Load Variation tags
                               If *lv_pp != NULL, must be freed in
                               the calling routine by calling UF_free.
                               */
);

/****************************************************************************
This function will create a Durability load variation.
From NX7.5, this function will create a durability load variation to 
the first available static event. In case the event is not available, an error
will be returned.
Valid only when the work part is a Simulation.

Environment: Internal  and  External

History: Originally released in NX3.0
*****************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_create_lv_nx (
const char *lv_name,                    /* <I>
                                        Load variation name
                                        If lv_name = NULL, a default name
                                        will be assigned.
                                        */
double scaling_factor,                  /* <I>
                                        Scaling factor
                                        */
int count,                              /* <I>
                                        Number of cycles
                                        */
UF_SF_lv_function_mode_t function_type, /* <I>
                                        Scaling function type
                                            UF_SF_HALF_UNIT_CYCLE
                                            UF_SF_FULL_UNIT_CYCLE
                                        */
tag_t solution_step_tag,                /* <I>
                                        Solution Step tag
                                        */
tag_t dursol_tag,                       /* <I>
                                        Durablity Solution tag
                                        */
tag_t *lv_tag                           /* <O>
                                        Load Variation tag
                                        */
);

/****************************************************************************
This function will delete a Durability load variation.

Valid only when the work part is a Simulation.

Environment: Internal  and  External

History: Originally released in NX3.0
*****************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_delete_lv_nx (
tag_t dursol_tag, /* <I>
                  Durability Solution tag
                  */
tag_t lv_tag      /* <I>
                  Load Variation tag
                  */
);

/****************************************************************************
This function will ask a Durability load variation's values.
From NX7.5, the number of cycles will be the number of occurrences on
the parent static event.
Valid only when the work part is a Simulation.

Environment: Internal  and  External

History: Originally released in NX3.0
*****************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_ask_lv_nx (
tag_t                    lv_tag,            /* <I>
                                            Load Variation tag
                                            */
char                     lv_name[MAX_LINE_BUFSIZE],           /* <O>
                                            Name
                                            The buffer must be declared using MAX_LINE_BUFSIZE so it can hold MAX_LINE_NCHARS characters. 
                                            If NULL, value will not be returned.
                                            */
double                   *scaling_factor,   /* <O>
                                            Scaling factor
                                            If NULL, value will not be returned.
                                            */
int                      *count,            /* <O>
                                            Number of cycles
                                            If NULL, value will not be returned.
                                            */
UF_SF_lv_function_mode_t *function_type,    /* <O>
                                            Scaling function type
                                              UF_SF_HALF_UNIT_CYCLE
                                              UF_SF_FULL_UNIT_CYCLE
                                            If NULL, value will not be returned.
                                            */
tag_t                    *solution_step_tag /* <O>
                                            Solution Step tag
                                            If NULL, value will not be returned.
                                            */
);

/****************************************************************************
This function will edit a Durability load variation's values.
From NX7.5, this function will modify the number of Occurrences on the
parent static event using count.
Valid only when the work part is a Simulation.

Environment: Internal  and  External

History: Originally released in NX3.0
*****************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_edit_lv_nx (
tag_t                    lv_tag,          /* <I>
                                          Load Variation tag
                                          */
const char*              lv_name,         /* <I>
                                          The buffer must be declared using MAX_LINE_BUFSIZE so it can hold MAX_LINE_NCHARS characters. 
                                          If NULL, value will not be modified.
                                          */
double                   *scaling_factor, /* <I>
                                          Scaling factor
                                          If NULL, value will not be modified.
                                          */
int                      *count,          /* <I>
                                          Number of cycles
                                          If NULL, value will not be modified.
                                          */
UF_SF_lv_function_mode_t *function_type   /* <I>
                                          Scaling function type
                                            UF_SF_HALF_UNIT_CYCLE
                                            UF_SF_FULL_UNIT_CYCLE
                                          If NULL, value will not be modified.
                                          */
);

/****************************************************************************
This function will get all polygon bodies in the part.

Environment: Internal  and  External

History: Originally released in NX4.0
*****************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_ask_all_polygon_bodies (  int        *num_polygon_bodies,/*<O> Number of polygon bodies in the fem*/
                                                      tag_t      **polygon_bodies        /*<OF,len:num_polygon_bodies> Tags of polygon bodies*/);

/****************************************************************************
This function will get polygon body type : i.e, Sheet body or Solid body.

Environment: Internal  and  External

History: Originally released in NX4.0
*****************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_polygon_body_ask_type (  tag_t    polygon_body,/*<I> Polygon body tag*/
                                                     int      *body_type    /*<O> Polygon body type; 0=>Solid; 1=>Sheet not mid-surface; 2=>sheet mid surface*/);


/****************************************************************************
This function will get polygon edges related to polygon body.

Environment: Internal  and  External

History: Originally released in NX4.0
*****************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_body_ask_edges (  tag_t      cae_tag,  /*<I> Polygon body*/
                                   int        *num_edges,/*<O> Number of polygon edges */
                                   tag_p_t    *edges       /*<OF,len:num_edges> Tags of polygon edges */);
/****************************************************************************
This function will get polygon faces related to polygon body.

Environment: Internal  and  External

History: Originally released in NX4.0
*****************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_body_ask_faces (  tag_t      cae_tag,             /*<I> Polygon body */
                                   int        *num_faces,/*<O> Number of polygon faces */
                                   tag_p_t    *faces         /*<OF,len:num_faces>Polygon faces*/);
/****************************************************************************
This function will get MODL body related to Polygon body.

Environment: Internal  and  External

History: Originally released in NX4.0
*****************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_body_ask_modl_body (  tag_t      cae_tag,     /*<I> Polygon body */
                                       tag_p_t    modl_body_p /*<O> CAD MODL body */);
/****************************************************************************
This function will get Polygon body related to MODL body.

Valid only when the work part is a FEM

Environment: Internal  and  External

History: Originally released in NX4.0
*****************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_modl_body_ask_body ( tag_t      modl_body,  /*<I> CAD MODL body */
                                      tag_p_t    cae_body_p  /*<O> Polygon body */);
/****************************************************************************
This function will get volume and centroid of Polygon body

Environment: Internal  and  External

History: Originally released in NX4.0
*****************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_body_ask_volume_and_centroid( tag_t      cae_tag,   /*<I> Polygon body */
                                               double     *pd_volume, /*<O> Volume */
                                               double     centroid[3]/*<O> Centroid */ ) ;
/****************************************************************************
This function will get bounding box of Polygon body

Environment: Internal  and  External

History: Originally released in NX4.0
*****************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_body_ask_bounding_box (  tag_t      cae_tag,   /*<I> Polygon body */
                                          double     pad_bounding_volume[6]  /*<O> Bounding box */);
/****************************************************************************
This function will get polygon edges related to polygon face.

Environment: Internal  and  External

History: Originally released in NX4.0
*****************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_face_ask_edges (  tag_t      cae_tag,             /*<I> Polygon face */
                                   int        *num_edges,/*<O> Number of polygon edges */
                                   tag_p_t    *edges /*<OF,len:num_edges> Polygon edges */)       ;
/****************************************************************************
This function will get polygon body related to polygon face.

Environment: Internal  and  External

History: Originally released in NX4.0
*****************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_face_ask_body (  tag_t      cae_tag,        /*<I> Polygon face */
                                  tag_p_t    body_p          /*<O> Polygon body */);
/****************************************************************************
This function will find area of polygon face.

Environment: Internal  and  External

History: Originally released in NX4.0
*****************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_face_ask_area (  tag_t      cae_tag, /*<I> Polygon face */
                                  double     *pd_area  /*<O> Face Area */ ) ;
/****************************************************************************
This function will get bounding box of polygon face.

Environment: Internal  and  External

History: Originally released in NX4.0
*****************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_face_ask_bounding_box (  tag_t      cae_tag, /*<I> Polygon face */
                                          double     pad_bounding_box[6] /*<O> Bounding box */);
/****************************************************************************
This function will get adjacent polygon faces of input polygon face.

Environment: Internal  and  External

History: Originally released in NX4.0
*****************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_face_ask_adjacent_faces (  tag_t      cae_tag, /*<I> Polygon face */
                                            int        *num_faces,/*<O> Number of faces */
                                            tag_p_t    *faces /*<OF,len:num_faces> Polygon faces*/)          ;
/****************************************************************************
This function will project passed in points and finds required data on face.

Environment: Internal  and  External

History: Originally released in NX4.0
*****************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_face_evaluate_closest_point ( tag_t      cae_tag, /*<I> Polygon face*/
                                 int num_evaluations,      /*<I> number of evaluations in U parameter */
                                 double xyz[],  /*<I> Input 3d points (can be NULL) */
                                 double xyz_cl[],/*<O> Output closest 3d points (can be NULL) */
                                 double uv_cl[], /*<O> uv values (can be NULL) */
                                 double nrml[], /*<O> normals (can be NULL)*/
                                 double dist[], /*<O> distance between input and projection*/
                                 int in_out[]   /*<O> 0 -> inside, 1 -> outside, 2 -> boundary*/);
/****************************************************************************
This function will find 3d location for given param value.

Environment: Internal  and  External

History: Originally released in NX4.0
*****************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_face_evaluate_param_location (  tag_t      cae_tag, /*<I> Polygon face*/
                                                        double     ad_param[2], /*<I> UV Param values */
                                                        double     ad_out_point[3] /*<O> Corresponding point */ );
/****************************************************************************
This function will get polygon faces related to polygon edge.

Environment: Internal  and  External

History: Originally released in NX4.0
*****************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_edge_ask_faces ( tag_t      cae_tag,             /*<I> Polygon edge */
                                  int        *num_faces,/*<O> Number of faces */
                                  tag_p_t    *faces /*<OF,len:num_faces> Polygon faces*/)          ;
/****************************************************************************
This function will get adjacent polygon edges of input polygon edge.

Environment: Internal  and  External

History: Originally released in NX4.0
*****************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_edge_ask_adjacent_edges (  tag_t      cae_tag,             /*<I> Polygon edge */
                                            int        *num_edges,/*<O> Number of edges */
                                            tag_p_t    *edges /*<OF,len:num_edges> Polygon edges */ )       ;
/****************************************************************************
This function will polygon body related to polygon edge.

Environment: Internal  and  External

History: Originally released in NX4.0
*****************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_edge_ask_body ( tag_t      cae_tag,        /*<I> Polygon edge */
                                 tag_p_t    body_p /*<O> Polygon body */)       ;
/****************************************************************************
This function will get bounding box of polygon edge.

Environment: Internal  and  External

History: Originally released in NX4.0
*****************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_edge_ask_bounding_box (  tag_t      cae_tag,/*<I> Polygon edge */
                                          double     pad_bounding_box[6] /*<O> Bounding box */);
/****************************************************************************
This function will end points and tangents of polygon edge.

Environment: Internal  and  External

History: Originally released in NX4.0
*****************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_edge_ask_end_points (tag_t      cae_tag,         /*<I> Polygon edge */
                                      double     start_pt[3],     /*<O> Start point location */
                                      double     end_pt[3],       /*<O> End point location */
                                      double     start_tangent[3],/*<O> Start tanget */
                                      double     end_tangent[3]   /*<O> End tangent */);
/****************************************************************************
This function will find the length of polygon edge.

Environment: Internal  and  External

History: Originally released in NX4.0
*****************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_edge_ask_length (  tag_t      cae_tag,  /*<I> Polygon edge */
                                               double     *pd_length /*<O> Length of edge */ );
/****************************************************************************
This function will project passed in point and finds param location on edge.

Environment: Internal  and  External

History: Originally released in NX4.0
*****************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_edge_evaluate_closest_point (  tag_t      cae_tag, /*<I> Polygon edge*/
                                                       double     ad_point[3], /*<I> Input point to project*/
                                                       double     ad_out_point[3], /*<O> Projected point */
                                                       double     *pd_param  /*<O>Param value between 0 to 1*/ );
/****************************************************************************
This function will find 3d location for given param value.

Environment: Internal  and  External

History: Originally released in NX4.0
*****************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_edge_evaluate_param_location (  tag_t      cae_tag, /*<I> Polygon edge*/
                                                        double     d_param, /*<I> Param value between 0 to 1*/
                                                        double     ad_out_point[3] /*<O> Corresponding point */ );
/****************************************************************************
Given two entities (atleast one should be polygon geometry), gives minimum distance
and points on the entities.

Environment: Internal  and  External

History: Originally released in NX4.0
*****************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_find_minimum_distance ( tag_t     entity_1,   /*<I> Polygon edge/face/body */
                                         tag_t     entity_2,   /*<I> Polygon edge/face/body */
                                         double    *min_dist,  /*<O> Minimum distance */
                                         double    point1[3],  /*<O> Point on entity_1 */
                                         double    point2[3]   /*<O> Point on entity_2 */);
/****************************************************************************
  Given a point and a Polygon geometry ( i.e. Edge, Face, Body), Returns the projected
  point and distance.

Environment: Internal  and  External

History: Originally released in NX4.0
*****************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_ask_closest_point ( double    point[3],          /*<I> Input point */
                                     tag_t     entity,            /*<I> Polygon edge/face/body */
                                     double    closest_point[3],  /*<O> Closest point on entity */
                                     double    *min_dist          /*<O> Minimum distance */ );

/**************************************************************************
Query number of mesh recipes in a given FEM part.

Environment: Internal  and  External

History: Originally released in NX4.01
*********************************************************************/
extern UFUN_CAEEXPORT int UF_SF_ask_num_mesh_recipes( tag_t fem_tag,        /*<I> FEM part */
                                                  int *num_mesh_recipes /*<O> Number of mesh recipes */
);

/**************************************************************************
Query nth mesh recipe in a given FEM part.

Environment: Internal  and  External

History: Originally released in NX4.01
*********************************************************************/
extern UFUN_CAEEXPORT int UF_SF_ask_nth_mesh_recipe(
tag_t   fem_tag,            /* <I>
                            FEM part
                            */
int     index,              /* <I>
                            Index into list of mesh recipes.
                            Valid indices are from 0 to (number of mesh
                            recipes-1).
                            The number of mesh recipes can be obtained
                            from function UF_SF_ask_num_mesh_recipes.
                            */
tag_p_t mesh_recipe_tag     /* <O>
                            Mesh recipe
                            */
);

/*****************************************************************************
This user function is used to ask the elemnt type name in the current 
solver language.

Environment: Internal and External
*******************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_ask_element_type_names
(
    UF_SF_element_type_t element_type, /*<I> Parameters which
                                                         control the required
                                                         tet Mesh */    
    char**  element_name_array                     /*<O> tag of the created
                                                         mesh */
);

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif  /*  UF_SF__H_INCLUDED */
