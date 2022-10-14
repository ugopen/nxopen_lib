/*
 * ufx_batchmeshing_paramreader.hxx - class defintion for jaguar parameter 
 *                                  file reader 
 *
 * date (11-Nov-2005) SDRC/Ashish Das
 *
 **                 ========================================
 *                        B A T C H    M E S H I N G
 *                        --------------------------
 *                  ========================================
 *
 *                 ------------------------------------------
 **                    Main File : ufx_batchmeshing.cxx
 **                ParamFile : ufx_batchmeshing_paramreader.hxx, 
 **                            ufx_batchmeshing_paramreader.cxx
 **                     Nov. 27, 2005 : Initial creation
 **                               Ashish Das 
 *                 ------------------------------------------
 *
 
 */
#ifndef PARAMREADER_H
#define PARAMREADER_H

#include <stdio.h>
#include <string.h>
#include <string_size_types.h>

class paramReader
{
public:
 
    paramReader();
    virtual  ~paramReader();

    char *fgetsSkipComments(char *s,int iNum,FILE *fp) const;
    bool fStringHasPreFix(char *psInputString, const char *psPreFixString) const;
    int openFile(const char *fn, const char *mode);
    int closeFile();
    int read_params();
    int read_criteria();
    int RemoveBlank() const;
    int LocateStartOfValue(const char *scTextLine) const;
    int getNum(int *piNum);

    int ReadKeyWordAndValue(const char *scLineRead, int ValueType, int *pIntValue, double *pdDoubleValue, const char *scTextValue) const;
    
    /* === Public access routines === */

    /* ==============================
         Parameter access methods 
       ============================== */

    /* === Mesh parameters === */
    int  Get_body_type (char *scBody_Type) const;
    int  Get_element_size (double *dElem_Size) const;
    int  Get_element_type (char *scElem_Type) const;
    int  Get_midnode_option (char *scMid_Node_Opt) const;
    int  Get_surf_mesh_size_variation (double *dSurf_Mesh_Size_Var) const;
    int  Get_max_mesh_jacobian (double *dMax_Mesh_Jacobian) const;
    int  Get_tet_mesh_size_variation (double *dTet_Mesh_Size_Var) const;
    int  Get_small_feature_size (double *dSmall_Feature_Size) const;
    int  Get_attempt_mapped_meshing_ON_OFF (int *fMapped_Meshing_ON_OFF_Opt) const;
    int  Get_two_element_through_thickness_ON_OFF (int *fTwo_Element_Through_Thickness_ON_OFF_Opt) const;
    int  Get_auto_fix_failed_elements_ON_OFF (int *fAuto_fix_failed_elements_ON_OFF_Opt) const;
    int  Get_geomtery_tolerance_toggle(int *fgeomtery_tolerance_toggle) const;
    int  Get_geomtery_tolerance_value(double *dgeomtery_tolerance_value) const;

    /* additional params for quad/tri mesh */
    int  Get_match_edge_ON_OFF_Toggle (int *fMatch_Edge_Toggle_ON_OFF_Opt) const;
    int  Get_edge_match_tolerance     (double *dEdge_Match_Tol) const;   
    int  Get_attempt_quad_mapping     (int *fQuad_Mapping_ON_OFF_Opt) const;
    int  Get_split_poor_quads         (int *fSplit_Bad_Quad_ON_OFF_Opt) const;
    int  Get_maximum_quad_warp        (double *dMax_Quad_Warp) const;  
    int  Get_quad_only_option         (int *iQuad_only_option) const;    

    int  Get_max_included_angle_quad_toggle(int *fMax_incl_angle_quad_ON_OFF_Opt) const;
    int  Get_min_included_angle_quad_toggle(int *fMin_incl_angle_quad_ON_OFF_Opt) const;
    int  Get_max_included_angle_tria_toggle(int *fMax_incl_angle_tria_ON_OFF_Opt) const;
    int  Get_min_included_angle_tria_toggle(int *fMin_incl_angle_tria_ON_OFF_Opt) const;
    
    int  Get_max_included_angle_quad_value(double *dMax_incl_angle_quad) const;
    int  Get_min_included_angle_quad_value(double *dMin_incl_angle_quad) const;
    int  Get_max_included_angle_tria_value(double *dMax_incl_angle_tria) const;
    int  Get_min_included_angle_tria_value(double *dMin_incl_angle_tria) const;

    int  Get_mesh_transition_ON_OFF( int *fMesh_Transition_ON_OFF_Toggle) const;
    int  Get_2D_mesh_method      (char *scMesh_2D_method) const;
    int  Get_target_min_elm_edge_length( int *ftarget_min_elm_edge_length_Toggle_ON_OFF_Opt) const;
    int  Get_CAD_curvature_abstraction(int *fCAD_curvature_abstraction_Toggle_ON_OFF_Opt) const;    
    int  Get_multi_block_decomposition(int *fmulti_block_decomposition_Toggle_ON_OFF_Opt) const;
    int  Get_minimum_feature_length (double *dminimum_feature_length) const;
    int  Get_move_nodes_off_geometry(int *fmove_nodes_off_geometry_Toggle_ON_OFF_Opt) const;
    int  Get_max_warp_toggle_ON_OFF(int *fmax_warp_Toggle_ON_OFF_opt) const;

    /* ====== Merge edge data ===== */
    int  Get_merge_edge_ON_OFF_Toggle (int *fMerge_Edge_Toggle_ON_OFF_Opt) const;
    int  Get_merge_edge_angle_value (double *dMerge_Edge_Angle_Val) const;

    /* ====== Merge edge data ===== */
    int  Get_suppress_hole_ON_OFF_Toggle  (int *fSuppress_Hole_Toggle_ON_OFF_Opt) const;
    int  Get_suppress_hole_diameter_value (double *dSuppress_Hole_Diameter_Val) const;
    int  Get_suppress_hole_point_type     (char *scPoint_Type_Opt) const;

    /* === Fillet parameters === */
    int Get_fillet_type(char scFillet_Type[MEDIUM_STRING_BUFSIZE]) const;
    int Get_min_fillet_radius (double *dMin_Fillet_Radius) const;
    int Get_max_fillet_radius (double *dMax_Fillet_Radius) const;
    int Get_elem_per_quarter_round (int *iElem_per_Quarter_Round) const;


     /* ==============================
         Criteria access methods 
       ============================== */

    /* === Mesh criteria for tet mesh === */
    int  Get_Tet_Collapse (double *dTet_Collapse) const;
    int  Get_Aspect_Ratio (double *dAspect_Ratio) const;
    int  Get_Jacobian (double *dJacobian) const;

    /* === Additional criteria for 2D mesh === */
    int  Get_Warp (double *dWarp) const;
    int  Get_Skew (double *dSkew) const;
    int  Get_Taper (double *dTaper) const;
    int  Get_2D_MinAngle (double *dMinAngle) const;
    int  Get_2D_MaxAngle (double *dMaxAngle) const;
    int  Get_Jacobian_Ratio (double *dJacobian_Ratio) const;
    


public:
    


private:
    
    char m_nextLine[ MEDIUM_STRING_BUFSIZE ];
    FILE *m_fp_xml;

    /* ====== MESH Data returned ======*/
    int    fSET__body_type;
    char   body_type[ MEDIUM_STRING_BUFSIZE ];

    int    fSET__element_size;
    double element_size;                    

    int    fSET__element_type;
    char   element_type[ MEDIUM_STRING_BUFSIZE ];

    int    fSET__midnode_option;
    char   midnode_option[ MEDIUM_STRING_BUFSIZE ];     

    int    fSET__max_mesh_jacobian;
    double max_mesh_jacobian;    

    int    fSET__surf_mesh_size_variation;
    double surf_mesh_size_variation;           

    int    fSET__tet_mesh_size_variation;
    double tet_mesh_size_variation;             
                       
    int    fSET__small_feature_size;
    double small_feature_size;

    int    fSET__attempt_mapped_meshing_ON_OFF;
    int    attempt_mapped_meshing_ON_OFF;

    int    fSET__two_element_through_thickness_ON_OFF;
    int    two_element_through_thickness_ON_OFF;

    int    fSET__auto_fix_failed_elements_ON_OFF;
    int    auto_fix_failed_elements_ON_OFF;

    int    fSET__geomtery_tolerance_toggle;
    int    geomtery_tolerance_toggle;

    int    fSET__geomtery_tolerance_value;
    double    geomtery_tolerance_value;
    /* additional parameters for 2d/quad mesh */

    int    fSET_match_edge_ON_OFF_Toggle;
    int    match_edge_ON_OFF_Toggle;

    int    fSET_edge_match_tolerance;
    double edge_match_tolerance;

    int    fSET_attempt_quad_mapping;
    int    attempt_quad_mapping;

    int    fSET_split_poor_quads;
    int    split_poor_quads;

    int    fSET_quad_only_option;
    int    quad_only_option;

    int    fSET_maximum_quad_warp;
    double maximum_quad_warp;  

    int    fSET_mesh_transition_ON_OFF;
    int    mesh_transition_ON_OFF;

    int    fSET_2D_mesh_method;
    char   mesh_method_2D[ MEDIUM_STRING_BUFSIZE ];

    int    fSET_target_min_elm_edge_length;
    int    target_min_elm_edge_length_ON_OFF_Toggle;

    int    fSET__minimum_feature_length;
    double minimum_feature_length;

    int    fSET_CAD_curvature_abstraction;
    int    CAD_curvature_abstraction_ON_OFF_Toggle;    

    int    fSET_multi_block_decomposition;
    int    multi_block_decomposition_ON_OFF_Toggle;

    int    fSET_move_nodes_off_geometry;
    int    move_nodes_off_geometry_ON_OFF_Toggle;

    int    fSET_max_warp_toggle;
    int    max_warp_Toggle_ON_OFF_Toggle;

    /* ====== Merge edge data ===== */
    int    fSET__merge_edge_ON_OFF_Toggle;
    int    merge_edge_ON_OFF_Toggle;

    int    fSET__merge_edge_angle_value;
    double merge_edge_angle_value;

    /* ====== Suppress Hole data ===== */
    int    fSET__suppress_hole_ON_OFF_Toggle;
    int    suppress_hole_ON_OFF_Toggle;

    int    fSET__suppress_hole_diameter_value;
    double suppress_hole_diameter_value;

    int    fSET__suppress_hole_point_type;
    char   suppress_hole_point_type[ MEDIUM_STRING_BUFSIZE ];

    /* ====== Fillet Data ========= */

    int    fSET__fillet_type;
    char   fillet_type[ MEDIUM_STRING_BUFSIZE ];

    int    fSET__min_fillet_radius;
    double min_fillet_radius;

    int    fSET__max_fillet_radius;
    double max_fillet_radius;

    int    fSET__elem_per_quarter_round;
    int    elem_per_quarter_round;


    /* ====== Mesh Criteria Parameters ======= */
    int    fSET__tet_collapse;
    double tet_collapse;

    int    fSET__aspect_ratio;
    double aspect_ratio;

    int    fSET__jacobian;
    double jacobian;

    /* === Additional criteria for 2D mesh === */
    int    fSET__warp;
    double warp;

    int    fSET__skew;
    double skew;

    int    fSET__taper;
    double taper;

    int    fSET__2D_min_angle;
    double min_angle_2D;
    
    int    fSET__2D_max_angle;
    double max_angle_2D;

    int    fSET__2D_min_angle_quad_toggle;
    int    min_angle_2D_quad_toggle;

    int    fSET__2D_max_angle_quad_toggle;
    int    max_angle_2D_quad_toggle;

    int    fSET__2D_min_angle_tria_toggle;
    int    min_angle_2D_tria_toggle;

    int    fSET__2D_max_angle_tria_toggle;
    int    max_angle_2D_tria_toggle;

    int    fSET__2D_min_angle_quad;
    double min_angle_2D_quad;

    int    fSET__2D_max_angle_quad;
    double max_angle_2D_quad;

    int    fSET__2D_min_angle_tria;
    double min_angle_2D_tria;

    int    fSET__2D_max_angle_tria;
    double max_angle_2D_tria;

    int    fSET__jacobian_ratio;
    double jacobian_ratio;

    int ReadCriteriaValue( const char *scCriteria, const char *scLineString, double *pdDBL_value) const;

    /* ==================
         Set functions 
       ================== */

    /* ===== Mesh ===== */
    void Set_body_type ( const char scbody_Type[MEDIUM_STRING_BUFSIZE] ); 
    void Set_element_size (double dElem_Size);                   
    void Set_element_type ( const char scElem_Type[MEDIUM_STRING_BUFSIZE] ); 
    void Set_midnode_option (const char scMid_Node_Opt[MEDIUM_STRING_BUFSIZE]);                
    void Set_surf_mesh_size_variation (double dSurf_Mesh_Size_Var); 
    void Set_max_mesh_jacobian (double dMax_Mesh_Jacobian);
    void Set_tet_mesh_size_variation (double dTet_Mesh_Size_Var);  
    void Set_small_feature_size (double dSmall_Feature_Size);
    void Set_attempt_mapped_meshing_ON_OFF (int fMapped_Meshing_ON_OFF_Opt);
    void Set_two_element_through_thickness_ON_OFF_toggle (int fTwo_element_through_thickness_ON_OFF_Opt);
    void Set_auto_fix_failed_elements_ON_OFF_toggle (int fAuto_fix_failed_elements_ON_OFF_Opt);
    void Set_geomtery_tolerance_toggle(int fgeomtery_tolerance_toggle);
    void Set_geomtery_tolerance_value(double dgeomtery_tolerance_value);

    /* additional methods for quad/tri specific params */
    void Set_match_edge_ON_OFF_Toggle (int fMatch_Edge_Toggle_ON_OFF_Opt);
    void Set_edge_match_tolerance  (double dEdge_Match_Tol);   
    void Set_attempt_quad_mapping  (int fQuad_Mapping_ON_OFF_Opt);
    void Set_split_poor_quads      (int fSplit_Bad_Quad_ON_OFF_Opt);
    void Set_maximum_quad_warp     (double dMax_Quad_Warp);  
    void Set_quad_only_option      (int iQuad_Only_Option);

    void  Set_max_included_angle_quad_toggle(int fMax_incl_angle_quad_ON_OFF_Opt);
    void  Set_min_included_angle_quad_toggle(int fMin_incl_angle_quad_ON_OFF_Opt);
    void  Set_max_included_angle_tria_toggle(int fMax_incl_angle_tria_ON_OFF_Opt);
    void  Set_min_included_angle_tria_toggle(int fMin_incl_angle_tria_ON_OFF_Opt);

    void  Set_max_included_angle_quad_value(double dMax_incl_angle_quad);
    void  Set_min_included_angle_quad_value(double dMin_incl_angle_quad);
    void  Set_max_included_angle_tria_value(double dMax_incl_angle_tria);
    void  Set_min_included_angle_tria_value(double dMin_incl_angle_tria);

    void Set_mesh_transition_ON_OFF( int fMesh_Transition_ON_OFF_Toggle);
    void Set_2D_mesh_method(const char scMesh_2D_method[MEDIUM_STRING_BUFSIZE]);
    void Set_target_min_elm_edge_length(int ftarget_min_elm_edge_length_Toggle_ON_OFF_Opt);
    void Set_CAD_curvature_abstraction(int fCAD_curvature_abstraction_Toggle_ON_OFF_Opt);   
    void Set_multi_block_decomposition(int fMulti_block_decomposition_Toggle_ON_OFF_Opt);
    void Set_minimum_feature_length (double dMinimum_feature_length);
    void Set_move_nodes_off_geometry(int fmove_nodes_off_geometry_Toggle_ON_OFF_Opt);
    void Set_max_warp_toggle(int fmax_warp_Toggle_ON_OFF_Opt);
    
    /* ====== Merge edge data ===== */
    void Set_merge_edge_ON_OFF_Toggle (int fMerge_Edge_Toggle_ON_OFF_Opt);
    void Set_merge_edge_angle_value (double dMerge_Edge_Angle_Val);

     /* ====== Suppress Hole data ===== */
    void Set_suppress_hole_ON_OFF_Toggle (int fSuppress_Hole_Toggle_ON_OFF_Opt);
    void Set_suppress_hole_diameter_value (double dSuppress_Hole_Diameter_Val);
    void Set_suppress_hole_point_type (const char scPoint_Type_Opt[MEDIUM_STRING_BUFSIZE]);

    /* ===== Fillet ===== */
    void Set_fillet_type(const char scFillet_Type[MEDIUM_STRING_BUFSIZE]);
    void Set_min_fillet_radius (double dMin_Fillet_Radius);
    void Set_max_fillet_radius (double dMax_Fillet_Radius);
    void Set_elem_per_quarter_round (int iElem_per_Quarter_Round);

    /* ==============================
         Criteria access methods 
       ============================== */

    /* === Mesh criteria for tet mesh === */
    void  Set_Tet_Collapse (double dTet_Collapse);
    void  Set_Aspect_Ratio (double dAspect_Ratio);
    void  Set_Jacobian (double dJacobian);

    /* === Additional criteria for 2D mesh === */
    void  Set_Warp (double dWarp);
    void  Set_Skew (double dSkew);
    void  Set_Taper (double dTaper);
    void  Set_2D_MinAngle (double dMinAngle);
    void  Set_2D_MaxAngle (double dMaxAngle);
    void  Set_Jacobian_Ratio (double dJacobian_Ratio);

    paramReader( const paramReader &X);
    paramReader& operator= ( const paramReader &X);
};


#endif //PARAMREADER
