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
 **
//======================================================================
//                      REVISION HISTORY
//    DATE           NAME         DESCRIPTION OF CHANGE
// 
// 13-Dec-2005    Ashish Das              Initial Creation
// 22-Nov-2006    Ashish Das              Enhancements requests from NX5 beta: Mesh transition,
//                                        Meshing method for paving.
//
*$HISTORY$
//=======================================================================
 */
#ifndef PARAMREADER_H
#define PARAMREADER_H

#include <stdio.h>
#include <string.h>

#define PARAMREADER_MAX_LINE_LENGTH 256

class paramReader
{
public:
	
    paramReader();	
    virtual ~paramReader();

	char *fgetsSkipComments(char *s,int iNum,FILE *fp);
	bool fStringHasPreFix(char *psInputString,char *psPreFixString);
	int openFile(const char *fn, const char *mode);
	int closeFile(void);
    int read_params(void);
    int read_criteria(void);
	int RemoveBlank(void);
    int LocateStartOfValue(char *scTextLine);
    int getNum(int *piNum);


    int ReadKeyWordAndValue(char *scLineRead, int ValueType,
                            int *pIntValue, double *pdDoubleValue, 
                            char *scTextValue);
	
    /* === Public access routines === */

    
    

    /* ==============================
         Parameter access methods 
       ============================== */

    /* === Mesh parameters === */
    int  Get_element_size (double *dElem_Size);
    int  Get_element_type (char *scElem_Type);
    int  Get_midnode_option (char *scMid_Node_Opt);
    int  Get_surf_mesh_size_variation (double *dSurf_Mesh_Size_Var);
    int  Get_max_mesh_jacobian (double *dMax_Mesh_Jacobian);
    int  Get_tet_mesh_size_variation (double *dTet_Mesh_Size_Var);
    int  Get_small_feature_size (double *dSmall_Feature_Size);

    /* additional params for quad/tri mesh */
    int  Get_edge_match_tolerance  (double *dEdge_Match_Tol);   
    int  Get_attempt_quad_mapping  (int *fQuad_Mapping_ON_OFF_Opt);
    int  Get_split_poor_quads      (int *fSplit_Bad_Quad_ON_OFF_Opt);
    int  Get_maximum_quad_warp     (double *dMax_Quad_Warp);  
    
    int  Get_mesh_transition_ON_OFF( int *fMesh_Transition_ON_OFF_Toggle);
    int  Get_2D_mesh_method      (char *scMesh_2D_method);


    /* ====== Merge edge data ===== */
    int  Get_merge_edge_ON_OFF_Toggle (int *fMerge_Edge_Toggle_ON_OFF_Opt);
    int  Get_merge_edge_angle_value (double *dMerge_Edge_Angle_Val);


    /* === Fillet parameters === */
    int Get_fillet_type(char scFillet_Type[PARAMREADER_MAX_LINE_LENGTH]);
    int Get_min_fillet_radius (double *dMin_Fillet_Radius);
    int Get_max_fillet_radius (double *dMax_Fillet_Radius);
    int Get_elem_per_quarter_round (int *iElem_per_Quarter_Round);


     /* ==============================
         Criteria access methods 
       ============================== */

    /* === Mesh criteria for tet mesh === */
    int  Get_Tet_Collapse (double *dTet_Collapse);
    int  Get_Aspect_Ratio (double *dAspect_Ratio);
    int  Get_Jacobian (double *dJacobian);
    


public:
	


private:
	
	char m_nextLine[PARAMREADER_MAX_LINE_LENGTH];
	FILE *m_fp_xml;

    /* ====== MESH Data returned ======*/
    int    fSET__element_size;
    double element_size;                    

    int    fSET__element_type;
    char   element_type[PARAMREADER_MAX_LINE_LENGTH];

    int    fSET__midnode_option;
    char   midnode_option[PARAMREADER_MAX_LINE_LENGTH];     

    int    fSET__max_mesh_jacobian;
    double max_mesh_jacobian;    

    int    fSET__surf_mesh_size_variation;
    double surf_mesh_size_variation;           

    int    fSET__tet_mesh_size_variation;
    double tet_mesh_size_variation;             
                       
    int    fSET__small_feature_size;
    double small_feature_size;

    /* additional parameters for 2d/quad mesh */
    int    fSET_edge_match_tolerance;
    double edge_match_tolerance;

    int    fSET_attempt_quad_mapping;
    int    attempt_quad_mapping;

    int    fSET_split_poor_quads;
    int    split_poor_quads;

    int    fSET_maximum_quad_warp;
    double maximum_quad_warp;  

    int    fSET_mesh_transition_ON_OFF;
    int    mesh_transition_ON_OFF;

    int    fSET_2D_mesh_method;
    char   mesh_method_2D[PARAMREADER_MAX_LINE_LENGTH];

    /* ====== Merge edge data ===== */
    int    fSET__merge_edge_ON_OFF_Toggle;
    int    merge_edge_ON_OFF_Toggle;

    int    fSET__merge_edge_angle_value;
    double merge_edge_angle_value;


    /* ====== Fillet Data ========= */

    int    fSET__fillet_type;
    char   fillet_type[PARAMREADER_MAX_LINE_LENGTH];

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

     
    int ReadCriteriaValue( char *scCriteria, 
                            char *scLineString, 
                            double *pdDBL_value);

    /* ==================
         Set functions 
       ================== */

    /* ===== Mesh ===== */
    void Set_element_size (double dElem_Size);                   
    void Set_element_type ( char   scElem_Type[PARAMREADER_MAX_LINE_LENGTH] ); 
    void Set_midnode_option (char scMid_Node_Opt[PARAMREADER_MAX_LINE_LENGTH]);                
    void Set_surf_mesh_size_variation (double dSurf_Mesh_Size_Var); 
    void Set_max_mesh_jacobian (double dMax_Mesh_Jacobian);
    void Set_tet_mesh_size_variation (double dTet_Mesh_Size_Var);  
    void Set_small_feature_size (double dSmall_Feature_Size);

    /* additional methods for quad/tri specific params */
    void Set_edge_match_tolerance  (double dEdge_Match_Tol);   
    void Set_attempt_quad_mapping  (int fQuad_Mapping_ON_OFF_Opt);
    void Set_split_poor_quads      (int fSplit_Bad_Quad_ON_OFF_Opt);
    void Set_maximum_quad_warp     (double dMax_Quad_Warp);  

    void Set_mesh_transition_ON_OFF( int fMesh_Transition_ON_OFF_Toggle);
    void Set_2D_mesh_method(char  scMesh_2D_method[PARAMREADER_MAX_LINE_LENGTH]);


    /* ====== Merge edge data ===== */
    void Set_merge_edge_ON_OFF_Toggle (int fMerge_Edge_Toggle_ON_OFF_Opt);
    void Set_merge_edge_angle_value (double dMerge_Edge_Angle_Val);

    /* ===== Fillet ===== */
    void Set_fillet_type(char scFillet_Type[PARAMREADER_MAX_LINE_LENGTH]);
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

    paramReader( const paramReader &X){};

    paramReader& operator= ( const paramReader &X){ return *this; }

};


#endif //PARAMREADER
