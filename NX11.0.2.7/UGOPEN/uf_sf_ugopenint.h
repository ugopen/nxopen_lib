/*****************************************************************************
             Copyright (c) 2000 Unigraphics Solutions, Inc.
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
 
 End User Functions equivalent to Scenario dialogs:
 
   Language definition API's:
     UF_SF_ask_anl_langs
     UF_SF_ask_language
     UF_SF_locate_anl_lang
     UF_SF_set_cur_anl_lang
    
   Scenario Meshers:
     UF_SF_create_0d_mesh
     UF_SF_create_1d_mesh
     UF_SF_create_weld_mesh
     UF_SF_edit_beam_orientation
     UF_SF_create_2d_mesh
     UF_SF_create_contact_mesh
 
   Scenario Constraints:
     UF_SF_create_load
     UF_SF_ask_load
     UF_SF_edit_load
     UF_SF_locate_load
     UF_SF_locate_load_geom
     UF_SF_create_load_case
     UF_SF_create_bc
     UF_SF_ask_bc
     UF_SF_edit_bc
     UF_SF_locate_bc
     UF_SF_locate_bc_geom
 
   Section API:
     UF_SF_apply_offsets
     UF_SF_ask_seciton_offsets
     UF_SF_ask_section_prop
     UF_SF_locate_section
     UF_SF_ask_mesh_sections
     UF_SF_ask_section_data
     UF_SF_free_section_data
     UF_SF_link_section
     UF_SF_unlink_section
     UF_SF_edit_section
     UF_SF_create_section
     UF_SF_locate_named_section
     UF_SF_apply_beam_end_mass
     UF_SF_ask_beam_end_mass
 
   Load cases API:
     UF_SF_create_load_case
     UF_SF_locate_all_lbc_cases
     UF_SF_add_to_lbc_case
     UF_SF_remove_from_lbc_case
     UF_SF_locate_lbc_members
     UF_SF_ask_lbc_name
     UF_SF_ask_lbc_case
     UF_SF_copy_lbc_to_case
     UF_SF_locate_named_lbc_case
 
   Combined Load cases API:
     UF_SF_ask_combined_load_cases
     UF_SF_ask_combined_load_case
     UF_SF_create_combined_load_case
 
   Material
     UF_SF_create_material
     UF_SF_link_material
     UF_SF_locate_material
     UF_SF_locate_named_material
     UF_SF_unlink_material
     UF_SF_ask_material
     UF_SF_ask_material_type
     UF_SF_init_matl_prop
     UF_SF_free_matl_prop
 
   SCENARIO MANAGER API:
 
     UF_SF_create_scenario
     UF_SF_locate_scenarios
     UF_SF_is_scenario_part
 
   SFMIDSRF MIDSURFACE API:

     UF_SF_create_offset_midsrf
     UF_SF_edit_offset_midsrf
     UF_SF_is_midsrf
     UF_SF_ask_midsrf_thickness
 
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
     UF_SF_temp_disp_results
     UF_SF_delete_disp_results
     UF_SF_LEGEND_set_colors
 
   SOLVER APIs:
 
     UF_SF_analysis_nastran
     UF_SF_analysis_ansys
 
******************************************************************************/

#ifndef  UF_SF_UGOPENINT_H_INCLUDED
#define  UF_SF_UGOPENINT_H_INCLUDED

#include <uf_defs.h>
#include <uf_disp.h>
#include <uf_sf_types.h>
#include <libugopenint_cae_exports.h>
#include <uf_sf_legend.h>

#ifdef __cplusplus
extern "C" {
#endif

/******************************************************************************
Generates the temporary display of an element.

Environment: Internal

See Also:

History:
******************************************************************************/
extern UGOPENINT_CAEEXPORT int UF_SF_temp_display_element (
tag_t node_tag ,/* <I>
                Tag of the element to be displayed.
                */
int color ,/* <I>
           Color to be used in temporary display.
           See uf_obj.h for color  constants.
           */
double height ,/* <I>
               Size of display for ID and symbol display.
               */
logical display_edges ,/* <I>
                       Indicates whether element edges are  to be
                       displayed.
                       */
logical display_id ,/* <I>
                    Indicates whether element label is to be displayed.
                    */
logical display_nodes ,/* <I>
                       Indicates whether element nodes are  to be
                       displayed.
                       */
UF_DISP_poly_marker_t node_marker ,/* <I>
                                   node_marker (uf_disp.h)
                                   */
logical   display_orientation /*<I>
                              Indicates whether element orientation is to
                              be displayed. (some 1d and 2d elms only)
                              */
                              
);

/******************************************************************************
Generates the temporary display of a node.

Environment: Internal

See Also:

History:
******************************************************************************/
extern UGOPENINT_CAEEXPORT int UF_SF_temp_display_node (
tag_t node_tag ,/* <I>
                Tag of the node to be displayed.
                */
int color ,/* <I>
           Color to be used in temporary display.
           See uf_obj.h for color  constants.
           */
double height ,/* <I>
               Height of display for ID and symbol display.
               */
logical display_id ,/* <I>
                    Indicates whether element label is to be displayed.
                    */
const char* object_symbol ,/* <I>
                     Object Symbol or NULL to concatenate preceding
                     to display id.
                     */
UF_DISP_poly_marker_t node_marker /* <I>
                                   node_marker (uf_disp.h)
                                   */
);

/******************************************************************************
Generates the temporary display of a mesh and the associated resutst.
                       
Environment: Internal   

See Also:

History: Originally released in V19.0
******************************************************************************/
extern UGOPENINT_CAEEXPORT int UF_SF_temp_disp_results
(
 
    UF_SF_COLOR_attr_p_t    color_att_p,   /*<I> Color attribute structure. */  
                                                     
    UF_SF_LEGEND_attr_p_t   legend_attr_p /*<I> Legend attribute structure or NULL. 
                                                If NULL a default legend will be   
                                                created and displayed.   
                                           */  

);
/******************************************************************************
Deletes the fringe display of the results associated with a mesh
and optionally the associated legend. 
                                                     

Environment: Internal  and  External

See Also:

History: Originally released in V19.0
******************************************************************************/
extern UGOPENINT_CAEEXPORT int UF_SF_delete_disp_results
(
    int       delete_legend_sw   /*<I> Switch indicating whether to 
                                   delete legend along with the fringe
                                   display of the results: 
                                   = 0 --> Do not delete legend 
                                   = 1 --> Delete legend
                                 */
);

/******************************************************************************
Sets the color attributes of the scalar-to-color mapping that is used in
rendering fringe displays.

Environment: Internal  and  External

See Also:

History: Originally released in V19.0           
******************************************************************************/
extern UGOPENINT_CAEEXPORT int UF_SF_LEGEND_set_colors
(

    UF_SF_COLOR_attr_p_t color_attr_p  /*<I> Color attribute structure defining
                                             parameters of the scalar-to-color
                                             mapping that is used in rendering
                                             fringe displays. */
);   

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif  /*  UF_SF_UGOPENINT_H_INCLUDED */
