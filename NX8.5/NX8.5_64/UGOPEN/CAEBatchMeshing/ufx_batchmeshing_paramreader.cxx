/*
 * ufx_batchmeshing_paramreader.cxx - implentation for parameter Reader for
 *                                    batch mesher
 *
 * date (13-Dec-2005) SDRC/Ashish Das ufx_batchmeshing_paramreader.cxx
 * 
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
//================================================================================
*  Revision History
*
*   DATE           NAME         DESCRIPTION OF CHANGE
*   13-Dec-2005    Ashish Das      Created.
*   06-Jan-2006    Ashish Das      Fixed some QAZ errors.
*   09-Jan-2006    Ashish Das      Fixed qaz with including ufx_batchmeshing_paramreader.hxx
*   13-Jan-2006  Ashish Das        After getting QAZ exception for compile error with
*                                  include ufx_batchmeshing_paramreader.hxx.
*   17-Jan-2006  Ashish Das        Fix for PR 5386872 : Added option "None" to fillet
*                                  processing. Corrected default small_feature_size to 10.0
*   08-Mar-2006  Ashish Das        Fix for political problems! QAZ folks do not like
*                                  QAZ exceptions; revert back include to <> form.
*                                  (Backporting 02-Feb-2006 from NX401)
*   23-Mar-2006  Ashish Das        QAZ errors because of new QAZ rules.
*   22-Nov-2006  Ashish Das        Enhancements requests from NX5 beta: Mesh transition,
*                                  Meshing method for paving.
*   28-Aug-2008  Ashish Das        Support for 2D mesh criteria.
*   17-Nov-2008  Ashish Das        Support for new NX6 meshing parameters.
*
* 
*   09-Sep-2010  Allen Gong        ARCH7304: Replace fopen with SYSS_fopen
*   27-Oct-2010  Keith Hafen       Back out above change
*   12-Jul-2012  Mike Walsh        Clean up qaz error and warnings
*$HISTORY$
//================================================================================
 */

#include <string.h>
#include <ctype.h>
#include <ufx_batchmeshing_paramreader.hxx>

/* Parameter keys */
#define  MESH_PARAM_mesh      "#mesh:"

#define      MESH_PARAM_mesh__elem_size                "element_size"
#define      MESH_PARAM_mesh__elem_type                "element_type"
#define      MESH_PARAM_mesh__mid_node_option          "mid_node_option"
#define      MESH_PARAM_mesh__max_mesh_jacobian        "max_jacobian"
#define      MESH_PARAM_mesh__surface_mesh_variation   "surface_mesh_variation"
#define      MESH_PARAM_mesh__volume_mesh_variation    "volume_mesh_variation"
#define      MESH_PARAM_mesh__small_feature_size       "small_feature_size"

/* Additional Parameter keys: QUAD/2D mesh specific */
#define      MESH_PARAM_mesh__edge_match_tolerance     "edge_match_tolerance"
#define      MESH_PARAM_mesh__attempt_quad_mapping     "attempt_quad_mapping"
#define      MESH_PARAM_mesh__split_poor_quads         "split_poor_quads"
#define      MESH_PARAM_mesh__maximum_quad_warp        "maximum_quad_warp"
#define      MESH_PARAM_mesh__quad_only_option         "quad_only_option"
#define      MESH_PARAM_mesh__mesh_transition          "mesh_transition"
#define      MESH_PARAM_mesh__meshing_method           "2D_meshing_method"


#define  MESH_PARAM_fillet    "#fillets:"

#define      MESH_PARAM_fillet__fillet_type              "fillet_type"
#define      MESH_PARAM_fillet__min_fillet_radius        "min_fillet_radius"
#define      MESH_PARAM_fillet__max_fillet_radius        "max_fillet_radius"
#define      MESH_PARAM_fillet__elem_per_quarter_round   "elem_per_quarter_round "


#define  MESH_PARAM_edge_merge    "#merge_edge:"

#define      MESH_PARAM_edge_merge__merge_edge_toggle        "merge_edge_ON_OFF"
#define      MESH_PARAM_edge_merge__merge_edge_angle_value   "merge_edge_angle_tolerance"




/* ===========================
              Macros
   =========================== */
#define  IsValid_MeshParam(scParam) \
        (strcmp((scParam), MESH_PARAM_mesh) ||      \
         strcmp((scParam), MESH_PARAM_mesh__elem_size) ||      \
         strcmp((scParam), MESH_PARAM_mesh__elem_type) ||     \
         strcmp((scParam), MESH_PARAM_mesh__mid_node_option) ||      \
         strcmp((scParam), MESH_PARAM_mesh__surface_mesh_variation) ||     \
         strcmp((scParam), MESH_PARAM_mesh__volume_mesh_variation)  ||   \
         strcmp((scParam), MESH_PARAM_mesh__small_feature_size)  || \
         strcmp((scParam), MESH_PARAM_mesh__mesh_transition)  ||   \
         strcmp((scParam), MESH_PARAM_mesh__meshing_method)   \
        )

#define  IsValid_FilletParam(scParam) \
        (strcmp((scParam), MESH_PARAM_fillet) ||      \
         strcmp((scParam), MESH_PARAM_fillet__fillet_type) ||      \
         strcmp((scParam), MESH_PARAM_fillet__min_fillet_radius) ||     \
         strcmp((scParam), MESH_PARAM_fillet__max_fillet_radius) ||      \
         strcmp((scParam), MESH_PARAM_fillet__elem_per_quarter_round)    \
        )

#define  IsValid_MergeEdgeParam(scParam) \
        (strcmp((scParam), MESH_PARAM_edge_merge__merge_edge_toggle) ||      \
         strcmp((scParam), MESH_PARAM_edge_merge__merge_edge_angle_value)    \
        )
        
#define  IsValid_Param(scParam) \
         (IsValid_FilletParam((scParam)) || \
          IsValid_MergeEdgeParam((scParam)) || \
          IsValid_MeshParam((scParam))
        
#define  IsValidParamSet(scParam) \
         (strcmp((scParam), MESH_PARAM_mesh) ||  \
          strcmp((scParam), MESH_PARAM_fillet) || \
          strcmp((scParam), MESH_PARAM_edge_merge))


/* =========================================================
       Function prototypes for some utility functions
   ========================================================= */
static int CountNonBlank ( const char *scString );
static int CountBlank ( const char *scString );

paramReader::paramReader( void ): m_nextLine(), m_fp_xml(0), 
                                 fSET__element_size(0), element_size(0.0), 
                                 fSET__element_type(0), element_type(), 
                                 fSET__midnode_option(0), midnode_option(),
                                 fSET__max_mesh_jacobian(0), max_mesh_jacobian(0.0),
                                 fSET__surf_mesh_size_variation(0), surf_mesh_size_variation(0.0),
                                 fSET__tet_mesh_size_variation(0), tet_mesh_size_variation(0.0),
                                 fSET__small_feature_size(0), small_feature_size(0.0),
                                 fSET_edge_match_tolerance(0), edge_match_tolerance(0.0),
                                 fSET_attempt_quad_mapping(0), attempt_quad_mapping(0),
                                 fSET_split_poor_quads(0), split_poor_quads(0),
                                 fSET_quad_only_option(0), quad_only_option(0),
                                 fSET_maximum_quad_warp(0), maximum_quad_warp(0.0),
                                 fSET_mesh_transition_ON_OFF(0), mesh_transition_ON_OFF(0),
                                 fSET_2D_mesh_method(0), mesh_method_2D(),
                                 fSET__merge_edge_ON_OFF_Toggle(0), merge_edge_ON_OFF_Toggle(0),
                                 fSET__merge_edge_angle_value(0), merge_edge_angle_value(0.0),
                                 fSET__fillet_type(0), fillet_type(), 
                                 fSET__min_fillet_radius(0), min_fillet_radius(0.0),
                                 fSET__max_fillet_radius(0), max_fillet_radius(0.0),
                                 fSET__elem_per_quarter_round(0), elem_per_quarter_round(0),
                                 fSET__tet_collapse(0), tet_collapse(0.0),
                                 fSET__aspect_ratio(0), aspect_ratio(0.0),
                                 fSET__jacobian(0), jacobian(0.0),
                                 fSET__warp(0), warp(0.0),
                                 fSET__skew(0), skew(0.0),
                                 fSET__taper(0), taper(0.0),
                                 fSET__2D_min_angle(0), min_angle_2D(0.0),
                                 fSET__2D_max_angle(0), max_angle_2D(0.0),
                                 fSET__jacobian_ratio(0), jacobian_ratio(0.0)
{
    // initialize character arrays to empty strings
    strcpy (m_nextLine, "");
    strcpy (element_type, "");
    strcpy (midnode_option, "");
    strcpy (mesh_method_2D, "");
    strcpy (fillet_type, "");
}

/* Destructor */
paramReader::~paramReader()
{
    /* Close the open file */
    if ( m_fp_xml!=NULL)
    {
       closeFile();
       m_fp_xml = NULL;
    }
}


int  paramReader::Get_element_size (double *dElem_Size) const
{
    if (fSET__element_size)
        *dElem_Size =element_size;   
    return fSET__element_size;
}

void paramReader::Set_element_size (double dElem_Size)
{
    fSET__element_size = true;
    element_size = dElem_Size;   
}


int  paramReader::Get_element_type (char *scElem_Type) const
{
    if (fSET__element_type)
        strcpy(scElem_Type, element_type);
    return fSET__element_type;
}
void paramReader::Set_element_type ( const char   scElement_type[PARAMREADER_MAX_LINE_LENGTH] )
{
    fSET__element_type = true;
    strcpy(element_type, scElement_type); 
}


int  paramReader::Get_midnode_option (char *scMid_Node_Opt) const
{
    if (fSET__midnode_option)
        strcpy(scMid_Node_Opt, midnode_option); 
    return fSET__midnode_option;
}
void paramReader::Set_midnode_option (const char scMid_Node_Opt[PARAMREADER_MAX_LINE_LENGTH])
{
    fSET__midnode_option = true;
    strcpy(midnode_option,scMid_Node_Opt);  
}

int  paramReader::Get_surf_mesh_size_variation (double *dSurf_Mesh_Size_Var) const
{
    if (fSET__surf_mesh_size_variation)
        *dSurf_Mesh_Size_Var = surf_mesh_size_variation;
    return fSET__surf_mesh_size_variation;
}
void paramReader::Set_surf_mesh_size_variation (double dSurf_Mesh_Size_Var)
{
    fSET__surf_mesh_size_variation = true;
    surf_mesh_size_variation = dSurf_Mesh_Size_Var; 
}


int  paramReader::Get_max_mesh_jacobian (double *dMax_Mesh_Jacobian) const
{
    if (fSET__max_mesh_jacobian)
        *dMax_Mesh_Jacobian = max_mesh_jacobian;   
    return fSET__max_mesh_jacobian;
}

void paramReader::Set_max_mesh_jacobian (double dMax_Mesh_Jacobian)
{
    fSET__max_mesh_jacobian = true;
    max_mesh_jacobian = dMax_Mesh_Jacobian;   
}


int  paramReader::Get_tet_mesh_size_variation (double *dTet_Mesh_Size_Var) const
{
    if ( fSET__tet_mesh_size_variation )
        *dTet_Mesh_Size_Var = tet_mesh_size_variation;   
    return fSET__tet_mesh_size_variation;
}
void paramReader::Set_tet_mesh_size_variation (double dTet_Mesh_Size_Var)
{
    fSET__tet_mesh_size_variation = true;
    tet_mesh_size_variation = dTet_Mesh_Size_Var;     
}
                       


int  paramReader::Get_edge_match_tolerance  (double *dEdge_Match_Tol) const
{
    if ( fSET_edge_match_tolerance )
        *dEdge_Match_Tol = edge_match_tolerance;   
    return fSET_edge_match_tolerance;
}
void paramReader::Set_edge_match_tolerance  (double dEdge_Match_Tol)
{
    fSET_edge_match_tolerance = true;
    edge_match_tolerance = dEdge_Match_Tol;     
}



int paramReader::Get_attempt_quad_mapping  (int *fQuad_Mapping_ON_OFF_Opt) const
{
    if ( fSET_attempt_quad_mapping )
        *fQuad_Mapping_ON_OFF_Opt = attempt_quad_mapping;   
    return fSET_attempt_quad_mapping;
}
void paramReader::Set_attempt_quad_mapping  (int fQuad_Mapping_ON_OFF_Opt)
{
    fSET_attempt_quad_mapping = true;
    attempt_quad_mapping = fQuad_Mapping_ON_OFF_Opt;     
}




int paramReader::Get_split_poor_quads  (int *fSplit_Bad_Quad_ON_OFF_Opt) const
{
    if ( fSET_split_poor_quads )
        *fSplit_Bad_Quad_ON_OFF_Opt = split_poor_quads;   
    return fSET_split_poor_quads;
}
void paramReader::Set_split_poor_quads (int fSplit_Bad_Quad_ON_OFF_Opt)
{
    fSET_split_poor_quads = true;
    split_poor_quads = fSplit_Bad_Quad_ON_OFF_Opt;     
}



int paramReader::Get_maximum_quad_warp (double *dMax_Quad_Warp) const
{
    if ( fSET_maximum_quad_warp )
        *dMax_Quad_Warp = maximum_quad_warp;   
    return fSET_maximum_quad_warp;
}
void paramReader::Set_maximum_quad_warp (double dMax_Quad_Warp)
{
    fSET_maximum_quad_warp = true;
    maximum_quad_warp = dMax_Quad_Warp;     
}



int  paramReader::Get_quad_only_option      (int *iQuad_only_option) const
{
    if ( fSET_quad_only_option )
        *iQuad_only_option = quad_only_option;   
    return fSET_quad_only_option;
}

void paramReader::Set_quad_only_option  (int iQuad_Only_Option)
{
    fSET_quad_only_option = true;
    quad_only_option = iQuad_Only_Option;
}





int paramReader::Get_mesh_transition_ON_OFF  (int *fMesh_Transition_ON_OFF_Toggle) const
{
    if ( fSET_mesh_transition_ON_OFF )
        *fMesh_Transition_ON_OFF_Toggle = mesh_transition_ON_OFF;   
    return fSET_mesh_transition_ON_OFF;
}
void paramReader::Set_mesh_transition_ON_OFF (int fMesh_Transition_ON_OFF_Toggle)
{
    fSET_mesh_transition_ON_OFF = true;
    mesh_transition_ON_OFF = fMesh_Transition_ON_OFF_Toggle;     
}



void paramReader::Set_2D_mesh_method (const char scMesh_2D_method[PARAMREADER_MAX_LINE_LENGTH])
{
    fSET_2D_mesh_method = true;
    strcpy(mesh_method_2D, scMesh_2D_method); 
}
int paramReader::Get_2D_mesh_method (char *scMesh_2D_method) const
{
    if (fSET_2D_mesh_method)
        strcpy(scMesh_2D_method, mesh_method_2D);
    return fSET_2D_mesh_method;
}




int  paramReader::Get_small_feature_size (double *dSmall_Feature_Size) const
{
    if ( fSET__small_feature_size == (int)true )
        *dSmall_Feature_Size = small_feature_size;
    return fSET__small_feature_size;
}
void paramReader::Set_small_feature_size (double dSmall_Feature_Size)
{
    fSET__small_feature_size = true;
    small_feature_size = dSmall_Feature_Size;
}



void paramReader::Set_fillet_type(const char scFillet_Type[PARAMREADER_MAX_LINE_LENGTH])
{
    fSET__fillet_type = true;
    strcpy (fillet_type, scFillet_Type);
}
int paramReader::Get_fillet_type(char scFillet_Type[PARAMREADER_MAX_LINE_LENGTH]) const
{
    if (fSET__fillet_type)
        strcpy(scFillet_Type, fillet_type);
    return fSET__fillet_type;
}


void paramReader::Set_min_fillet_radius (double dMin_Fillet_Radius)
{
    fSET__min_fillet_radius = true;
    min_fillet_radius = dMin_Fillet_Radius;
}
int paramReader::Get_min_fillet_radius (double *dMin_Fillet_Radius) const
{
    if (fSET__min_fillet_radius)
        *dMin_Fillet_Radius = min_fillet_radius;
    return fSET__min_fillet_radius;
}


void paramReader::Set_max_fillet_radius (double dMax_Fillet_Radius)
{
    fSET__max_fillet_radius = true;
    max_fillet_radius = dMax_Fillet_Radius;
}
int paramReader::Get_max_fillet_radius (double *dMax_Fillet_Radius) const
{
    if (fSET__max_fillet_radius )
        *dMax_Fillet_Radius = max_fillet_radius;
    return fSET__max_fillet_radius;
}


void paramReader::Set_elem_per_quarter_round (int iElem_per_Quarter_Round)
{
    fSET__elem_per_quarter_round = true;
    elem_per_quarter_round = iElem_per_Quarter_Round;
}
int paramReader::Get_elem_per_quarter_round (int *iElem_per_Quarter_Round) const
{
    if (fSET__elem_per_quarter_round)
        *iElem_per_Quarter_Round = elem_per_quarter_round;
    return fSET__elem_per_quarter_round;
}

    
void paramReader::Set_merge_edge_angle_value (double dMerge_Edge_Angle_Val)
{
    fSET__merge_edge_angle_value = true;
    merge_edge_angle_value = dMerge_Edge_Angle_Val;
}
int paramReader::Get_merge_edge_angle_value (double *dMerge_Edge_Angle_Val) const
{
    if (fSET__merge_edge_angle_value )
        *dMerge_Edge_Angle_Val = merge_edge_angle_value;
    return fSET__merge_edge_angle_value;
}



int paramReader::Get_merge_edge_ON_OFF_Toggle  (int *fMerge_Edge_Toggle_ON_OFF_Opt) const
{
    if ( fSET__merge_edge_ON_OFF_Toggle )
        *fMerge_Edge_Toggle_ON_OFF_Opt = merge_edge_ON_OFF_Toggle;   
    return fSET__merge_edge_ON_OFF_Toggle;
}
void paramReader::Set_merge_edge_ON_OFF_Toggle (int fMerge_Edge_Toggle_ON_OFF_Opt)
{
    fSET__merge_edge_ON_OFF_Toggle = true;
    merge_edge_ON_OFF_Toggle = fMerge_Edge_Toggle_ON_OFF_Opt;     
}



void   paramReader::Set_Tet_Collapse (double dTet_Collapse)
{
    fSET__tet_collapse = true;
    tet_collapse = dTet_Collapse;
}
int   paramReader::Get_Tet_Collapse (double *dTet_Collapse) const
{
    if (fSET__tet_collapse)
        *dTet_Collapse = tet_collapse;
    return fSET__tet_collapse;

}



void   paramReader::Set_Aspect_Ratio (double dAspect_Ratio)
{
    fSET__aspect_ratio = true;
    aspect_ratio = dAspect_Ratio;
}
int   paramReader::Get_Aspect_Ratio (double *dAspect_Ratio) const
{
    if (fSET__aspect_ratio)
        *dAspect_Ratio = aspect_ratio;
    return fSET__aspect_ratio;
}



void   paramReader::Set_Jacobian (double dJacobian)
{
    fSET__jacobian = true;
    jacobian = dJacobian;

}
int   paramReader::Get_Jacobian (double *dJacobian) const
{
    if (fSET__jacobian)
        *dJacobian = jacobian;
    return fSET__jacobian;
}
 

void   paramReader::Set_Warp (double dWarp)
{
    fSET__warp = true;
    warp = dWarp;
}
int   paramReader::Get_Warp (double *dWarp) const
{
    if (fSET__warp)
        *dWarp = warp;
    return fSET__warp;

}


void   paramReader::Set_Skew (double dSkew)
{
    fSET__skew = true;
    skew = dSkew;
}
int   paramReader::Get_Skew (double *dSkew) const
{
    if (fSET__skew)
        *dSkew = skew;
    return fSET__skew;

}


void   paramReader::Set_Taper (double dTaper)
{
    fSET__taper = true;
    taper = dTaper;
}
int   paramReader::Get_Taper (double *dTaper) const
{
    if (fSET__taper)
        *dTaper = taper;
    return fSET__taper;

}

  
void   paramReader::Set_2D_MinAngle (double dMinAngle)
{
    fSET__2D_min_angle = true;
    min_angle_2D = dMinAngle;
}
int   paramReader::Get_2D_MinAngle (double *dMinAngle) const
{
    if (fSET__2D_min_angle)
        *dMinAngle = min_angle_2D;
    return fSET__2D_min_angle;
}


void   paramReader::Set_2D_MaxAngle (double dMaxAngle)
{
    fSET__2D_max_angle = true;
    max_angle_2D = dMaxAngle;
}
int   paramReader::Get_2D_MaxAngle (double *dMaxAngle) const
{
    if (fSET__2D_max_angle)
        *dMaxAngle = max_angle_2D;
    return fSET__2D_max_angle;
}



void   paramReader::Set_Jacobian_Ratio (double dJacobian_Ratio)
{
    fSET__jacobian_ratio = true;
    jacobian_ratio = dJacobian_Ratio;
}
int   paramReader::Get_Jacobian_Ratio (double *dJacobian_Ratio) const
{
    if (fSET__jacobian_ratio)
        *dJacobian_Ratio = jacobian_ratio;
    return fSET__jacobian_ratio;
}

/*
 * --------------------------------------------------------------------------
 *  fStringHasPreFix(char *psInputString,char *PreFixString)
 * --------------------------------------------------------------------------
 */


bool paramReader::fStringHasPreFix(char *psInputString,const char *psPreFixString) const
{
    /*
    // Checks if the input string has a prefix 
    // 
    // The prefix match can be lower case or upper case or a mix
    // Use a temporary array for the prefix as it is a constant string.
    */
    bool fHasPrefix = false;
    int i, ichar, nchar;
    int nPreFixLength = 0;
    char psPreFixStringTemp[PARAMREADER_MAX_LINE_LENGTH];

    /*
    //  1. compute the length of the prefix 
    */
    nPreFixLength = (int) strlen(psPreFixString);
    nchar         = (int) strlen(psInputString);

    if (nPreFixLength > nchar)
    {
        /* No match is possible here */
        return fHasPrefix = false;
    }

    /*
    // Convert the input string to lower case as well as the prefix 
    */
    for (i=0;i<nchar;i++)
    {
        ichar = psInputString[i];
        psInputString[i] = tolower(ichar);
    }

    for (i=0;i<nPreFixLength;i++)
    {
        ichar = psPreFixString[i];
        psPreFixStringTemp[i] = tolower(ichar);
    }

    /* Null terminated string */
    psPreFixStringTemp[i]='\0';

    /*
    //  Compare !
    */
    
    /* Find the first non-space char. */
    i = 0;
    while (psInputString[i] == ' ' && i < PARAMREADER_MAX_LINE_LENGTH)
          {
           i++;
          }

    /* Check for start of vertices of tri. */
    if (0 == strncmp(psPreFixStringTemp, &(psInputString[i]),nPreFixLength)  )
    {
        fHasPrefix = true;
    }
    else
    {
        fHasPrefix = false;
    }
    return fHasPrefix;
}

/* Count non-blank characters */
static int CountNonBlank ( const char *scString )
{
    int iChar = 0;
    while ( scString[iChar] != ' ' && 
            scString[iChar] != '\0' &&
            iChar < PARAMREADER_MAX_LINE_LENGTH)
    {
        iChar++;
    }

    return iChar;
}

/* Count blank characters */
static int CountBlank ( const char *scString )
{
    int iChar = 0;
    while ( scString[iChar] == ' ' && 
            scString[iChar] != '\0' &&
            iChar < PARAMREADER_MAX_LINE_LENGTH)
    {
        iChar++;
    }

    return iChar;
}


int paramReader::RemoveBlank() const
{
    int iChar = 0;
    while ( m_nextLine[iChar] == ' ' && iChar < PARAMREADER_MAX_LINE_LENGTH)
    {
        iChar++;
    }

    return iChar;
}


int paramReader::LocateStartOfValue(const char *scTextLine) const
{
    int iValueLoc = -1; /* -1 => Error in locating value */
    int i = 0, nchar = 0;
    nchar         = (int) strlen(scTextLine);

    /* Find the first non-space char. */
    i = 0;
    while (scTextLine[i] == ' ' && i<nchar && i < PARAMREADER_MAX_LINE_LENGTH)
    {
        i++;
    }

    /* Look for start of next blank character */
    while (scTextLine[i] != ' ' && i<nchar && i < PARAMREADER_MAX_LINE_LENGTH)
    {
        i++;
    }

    /* Again count blanks; after this lies the value */
    while (scTextLine[i] == ' ' && i<nchar && i < PARAMREADER_MAX_LINE_LENGTH)
    {
        i++;
    }
    
    if ( i<nchar )
        iValueLoc = i;

    return iValueLoc;
}




int paramReader::openFile(const char *fn, const char *mode)
{
    /*
    * --------------------------------------------------------------------------
    *  gfOpen / graceful version of fopen /
    * --------------------------------------------------------------------------
    */
    int iRet = 0;


   if (NULL == (m_fp_xml=fopen(fn,mode)) )
      {
       perror(fn);
       /*
       // Exit 
       */
       iRet = -1;
      }

   return iRet;
}

int paramReader::closeFile()
{

    int iOut = 0; 
    int iRet = 0;

    if ( NULL != m_fp_xml)
    { 
        iOut = fclose(m_fp_xml);
        m_fp_xml = NULL;
        if (EOF == iOut)
        {
           fprintf(stderr," Error closing file \n");
           iRet = -1;
        }
    }
    return iRet;
}



/* =============================================================
     Given a line read from file, gets the parameter key word 
   ============================================================= */
int paramReader::ReadKeyWordAndValue(const char *scLineRead, int ValueType, int *pIntValue, double *pdDoubleValue, const char *scTextValue) const
{

    // Read <NUM> 
    int iRet = 0;
    return iRet;
}

char *paramReader::fgetsSkipComments(char *s, int iNum, FILE *fp) const
{
   char *pRet;
   int iCommentState = 0;
   while((pRet = fgets(s,iNum,fp))!=0)
   {
       if(paramReader::fStringHasPreFix(s,"<COMMENT>"))
       {
        iCommentState++;
        continue;
       }
       else if(paramReader::fStringHasPreFix(s,"</COMMENT>"))
       {
        iCommentState--;
        continue;
       }
       if(iCommentState > 0) 
           continue;
       else 
           break;
   }
   return(pRet);
}

/*
 * --------------------------------------------------------------------------
 * read_XML
 // The Tags have to be read in a certain order : 
 // i.e. we expect # Facet points and # Edge facet points to come first to 
 // derive the total number of points' uses.
 * --------------------------------------------------------------------------
 */
int paramReader::read_params()
{
 
    
  int  iRet = 0;
  int  iCnt=0, fSkipParamLines = false, fParmHeadCardRead = false;

  char          scCurrParamCategory[PARAMREADER_MAX_LINE_LENGTH] = {' '};

  int           iValueLoc = 0;
  float         fREAL_value = 0.0;
  int           iINT_value = 0;
  char          scSTR_value[PARAMREADER_MAX_LINE_LENGTH] = {' '};

  int           i = 0, nStrLen = 0;
 

  /* // Start at the beginning of the file  */

  if (0 == m_fp_xml) 
  {
      goto Exit;
  }
  rewind(m_fp_xml);
  
  fParmHeadCardRead = false;
  while (fgetsSkipComments(m_nextLine, PARAMREADER_MAX_LINE_LENGTH, m_fp_xml)) 
  {
      /* Get parameter name string */
      if ( m_nextLine[0]=='#' )
      {
          /* Decide what what category of parameters we are in
             e.g.: "#mesh:" or "#fillets:" etc. */

          if ( fStringHasPreFix(m_nextLine,MESH_PARAM_mesh) )
          {
                strcpy(scCurrParamCategory, MESH_PARAM_mesh );
                fSkipParamLines = false;
                fParmHeadCardRead = true;
          }
          else if ( fStringHasPreFix(m_nextLine,MESH_PARAM_edge_merge) )
          {
                strcpy(scCurrParamCategory, MESH_PARAM_edge_merge );
                fSkipParamLines = false;
                fParmHeadCardRead = true;
          }
          else if ( fStringHasPreFix(m_nextLine,MESH_PARAM_fillet) )
          {
                strcpy(scCurrParamCategory, MESH_PARAM_fillet );
                fSkipParamLines = false;
                fParmHeadCardRead = true;
          }
          else if ( !fParmHeadCardRead )
              fSkipParamLines = true;
      }
      else 
      {
          /* These lines are in actual parameter values in a
             particular category */
          if ( !fSkipParamLines )
          {
                /* ==========================================
                           Mesh related parameters 
                   ========================================== */
                               
                if ( fStringHasPreFix(m_nextLine,MESH_PARAM_mesh__elem_size) )
                {
                    iValueLoc = LocateStartOfValue (m_nextLine);
                    iCnt = sscanf(&m_nextLine[iValueLoc], "%g",&fREAL_value);
                    if ( (EOF == iCnt) || (  1 != iCnt) ) 
                        iRet = -1;
                    Set_element_size ((double)fREAL_value);  
                }
                else if ( fStringHasPreFix(m_nextLine,MESH_PARAM_mesh__elem_type) )
                {
                    iValueLoc = LocateStartOfValue (m_nextLine);
                    iCnt = sscanf(&m_nextLine[iValueLoc], "%s", scSTR_value);
                    if ( (EOF == iCnt) || (  1 != iCnt) ) 
                        iRet = -1;
                    nStrLen = (int) strlen(scSTR_value);
                    for (i=0;i<nStrLen;i++)
                        scSTR_value[i] = toupper(scSTR_value[i]);
                    Set_element_type ( scSTR_value ); 
                }
                else if ( fStringHasPreFix(m_nextLine,MESH_PARAM_mesh__mid_node_option) )
                {
                    iValueLoc = LocateStartOfValue (m_nextLine);
                    iCnt = sscanf(&m_nextLine[iValueLoc], "%s",scSTR_value);
                    if ( (EOF == iCnt) || (  1 != iCnt) ) 
                        iRet = -1;
                    Set_midnode_option (scSTR_value);       
                }
                else if ( fStringHasPreFix(m_nextLine,MESH_PARAM_mesh__max_mesh_jacobian) )
                {
                    iCnt = sscanf(&m_nextLine[iValueLoc], "%g",&fREAL_value);
                    if ( (EOF == iCnt) || (  1 != iCnt) ) 
                        iRet = -1;
                    Set_max_mesh_jacobian ((double)fREAL_value);
                }
                else if ( fStringHasPreFix(m_nextLine,MESH_PARAM_mesh__surface_mesh_variation) )
                {
                    iValueLoc = LocateStartOfValue (m_nextLine);
                    iCnt = sscanf(&m_nextLine[iValueLoc], "%g",&fREAL_value);
                    if ( (EOF == iCnt) || (  1 != iCnt) ) 
                        iRet = -1;
                    Set_surf_mesh_size_variation ((double)fREAL_value);   
                }
                else if ( fStringHasPreFix(m_nextLine,MESH_PARAM_mesh__volume_mesh_variation) )
                {
                    iValueLoc = LocateStartOfValue (m_nextLine);
                    iCnt = sscanf(&m_nextLine[iValueLoc], "%g",&fREAL_value);
                    if ( (EOF == iCnt) || (  1 != iCnt) ) 
                        iRet = -1;
                    Set_tet_mesh_size_variation ((double)fREAL_value);  
                }

                /* additional quad/2d mesh params */
                else if ( fStringHasPreFix(m_nextLine,MESH_PARAM_mesh__edge_match_tolerance) )
                {
                    iValueLoc = LocateStartOfValue (m_nextLine);
                    iCnt = sscanf(&m_nextLine[iValueLoc], "%g",&fREAL_value);
                    if ( (EOF == iCnt) || (  1 != iCnt) ) 
                        iRet = -1;
                    Set_edge_match_tolerance ((double)fREAL_value);  
                }
                else if ( fStringHasPreFix(m_nextLine,MESH_PARAM_mesh__maximum_quad_warp) )
                {
                    iValueLoc = LocateStartOfValue (m_nextLine);
                    iCnt = sscanf(&m_nextLine[iValueLoc], "%g",&fREAL_value);
                    if ( (EOF == iCnt) || (  1 != iCnt) ) 
                        iRet = -1;
                    Set_maximum_quad_warp ((double)fREAL_value);  
                }
                else if ( fStringHasPreFix(m_nextLine,MESH_PARAM_mesh__attempt_quad_mapping) )
                {
                    iValueLoc = LocateStartOfValue (m_nextLine);
                    iCnt = sscanf(&m_nextLine[iValueLoc], "%s",scSTR_value);
                    if ( (EOF == iCnt) || (  1 != iCnt) ) 
                        iRet = -1;
                    if (fStringHasPreFix(scSTR_value,"ON") )
                        iINT_value = (int)true;
                    else 
                        iINT_value = (int)false;
                    Set_attempt_quad_mapping (iINT_value);   
                }
                else if ( fStringHasPreFix(m_nextLine,MESH_PARAM_mesh__split_poor_quads) )
                {
                    iValueLoc = LocateStartOfValue (m_nextLine);
                    iCnt = sscanf(&m_nextLine[iValueLoc], "%s",scSTR_value);
                    if ( (EOF == iCnt) || (  1 != iCnt) ) 
                        iRet = -1;
                    if (fStringHasPreFix(scSTR_value,"ON"))
                        iINT_value = (int)true;
                    else 
                        iINT_value = (int)false;
                    Set_split_poor_quads (iINT_value); 
                }
                else if ( fStringHasPreFix(m_nextLine,MESH_PARAM_mesh__quad_only_option) )
                {
                    iValueLoc = LocateStartOfValue (m_nextLine);
                    iCnt = sscanf(&m_nextLine[iValueLoc], "%i",&iINT_value);
                    if ( (EOF == iCnt) || (  1 != iCnt) ) 
                        iRet = -1;
                    if (iINT_value==0 || iINT_value==1 || iINT_value==2)
                        Set_quad_only_option (iINT_value);   
                    else
                    {   
                        /* Invalid value : set it off */
                        iINT_value = 0; 
                        Set_quad_only_option (iINT_value); 
                    }
                }
                else if ( fStringHasPreFix(m_nextLine,MESH_PARAM_mesh__mesh_transition) )
                {

                    iValueLoc = LocateStartOfValue (m_nextLine);
                    iCnt = sscanf(&m_nextLine[iValueLoc], "%s",scSTR_value);
                    if ( (EOF == iCnt) || (  1 != iCnt) ) 
                        iRet = -1;
                    if (fStringHasPreFix(scSTR_value,"ON"))
                        iINT_value = (int)true;
                    else 
                        iINT_value = (int)false;
                    Set_mesh_transition_ON_OFF (iINT_value);
                }
                else if ( fStringHasPreFix(m_nextLine,MESH_PARAM_mesh__meshing_method) )
                {
                    iValueLoc = LocateStartOfValue (m_nextLine);
                    iCnt = sscanf(&m_nextLine[iValueLoc], "%s",scSTR_value);
                    if ( (EOF == iCnt) || (  1 != iCnt) ) 
                        iRet = -1;
                    Set_2D_mesh_method (scSTR_value);
                }

                /* Geometry abstraction related */
                else if ( fStringHasPreFix(m_nextLine,MESH_PARAM_mesh__small_feature_size))
                {
                    iValueLoc = LocateStartOfValue (m_nextLine);
                    iCnt = sscanf(&m_nextLine[iValueLoc], "%g",&fREAL_value);
                    if ( (EOF == iCnt) || (  1 != iCnt) ) 
                        iRet = -1;
                    Set_small_feature_size ((double)fREAL_value);
                }
                

                /* ==========================================
                         Merge edge related parameters 
                   ========================================== */
                
                else if ( fStringHasPreFix(m_nextLine,MESH_PARAM_edge_merge__merge_edge_toggle) )
                {
                    iValueLoc = LocateStartOfValue (m_nextLine);
                    iCnt = sscanf(&m_nextLine[iValueLoc], "%s",scSTR_value);
                    if ( (EOF == iCnt) || (  1 != iCnt) ) 
                        iRet = -1;
                    if (fStringHasPreFix(scSTR_value,"ON"))
                        iINT_value = (int)true;
                    else 
                        iINT_value = (int)false;
                    Set_merge_edge_ON_OFF_Toggle (iINT_value);
                }
                else if ( fStringHasPreFix(m_nextLine,MESH_PARAM_edge_merge__merge_edge_angle_value) )
                {
                    iValueLoc = LocateStartOfValue (m_nextLine);
                    iCnt = sscanf(&m_nextLine[iValueLoc], "%g",&fREAL_value);
                    if ( (EOF == iCnt) || (  1 != iCnt) ) 
                        iRet = -1;
                    Set_merge_edge_angle_value ((double)fREAL_value);
                }

                /* ==========================================
                           Fillet related parameters 
                   ========================================== */
                
                else if ( fStringHasPreFix(m_nextLine,MESH_PARAM_fillet__fillet_type) )
                {
                    iValueLoc = LocateStartOfValue (m_nextLine);
                    iCnt = sscanf(&m_nextLine[iValueLoc], "%s",scSTR_value);
                    if ( (EOF == iCnt) || (  1 != iCnt) ) 
                        iRet = -1;
                    Set_fillet_type(scSTR_value);
                }
                else if ( fStringHasPreFix(m_nextLine,MESH_PARAM_fillet__min_fillet_radius) )
                {
                    iValueLoc = LocateStartOfValue (m_nextLine);
                    iCnt = sscanf(&m_nextLine[iValueLoc], "%g",&fREAL_value);
                    if ( (EOF == iCnt) || (  1 != iCnt) ) 
                        iRet = -1;
                    Set_min_fillet_radius ((double)fREAL_value);
                }
                else if ( fStringHasPreFix(m_nextLine,MESH_PARAM_fillet__max_fillet_radius) )
                {
                    iValueLoc = LocateStartOfValue (m_nextLine);
                    iCnt = sscanf(&m_nextLine[iValueLoc], "%g",&fREAL_value);
                    if ( (EOF == iCnt) || (  1 != iCnt) ) 
                        iRet = -1;
                    Set_max_fillet_radius ((double)fREAL_value);
                }
                else if ( fStringHasPreFix(m_nextLine,MESH_PARAM_fillet__elem_per_quarter_round) )
                {
                    iValueLoc = LocateStartOfValue (m_nextLine);
                    iCnt = sscanf(&m_nextLine[iValueLoc], "%i",&iINT_value);
                    if ( (EOF == iCnt) || (  1 != iCnt) ) 
                        iRet = -1;
                    Set_elem_per_quarter_round (iINT_value);
                }
                
          }

      }
  } /* End of while loop */

  /* If we have gone that far ... */
  iRet = 0;

  goto Exit;

Exit:

   return iRet;
}

int paramReader::ReadCriteriaValue( const char *scCriteria, const char *scLineString, double *pdDBL_value) const
{

    bool  fHasCriteria = true;
    int   iCnt = 0, iStrLoc = 0;
    int   nPreFixLength = 0, nLineLength = 0;
    char  psCritStringTemp[PARAMREADER_MAX_LINE_LENGTH] = {' '};
    float fREAL_value = 0.0;
    int   iINT_value = 0;

    /* Init. output */
    *pdDBL_value = 0.0;

    /* Trivial checks */
    nPreFixLength = (int) strlen(scCriteria);
    nLineLength   = (int) strlen(scLineString);

    if (nPreFixLength > nLineLength)
    {
        /* No match is possible here */
        return fHasCriteria = false;
    }

    /* Atypical formatted line in criteria file looks :
        8 min angle tria    1   1   60.00   50.00   30.00   20.00    0.00 
        9 skew              1   1    0.00   10.00   55.00   60.00   90.00 
       10 jacobian          1   1    1.00    0.90    0.60    0.50    0.00  
       
       We need to read value in 5th column */

    iStrLoc = CountBlank (scLineString);
    iStrLoc += CountNonBlank ( &scLineString[iStrLoc] );
    iStrLoc += CountBlank (&scLineString[iStrLoc]);

    /* Check if the name is criteria string is indeed present */
    strncpy(psCritStringTemp, &scLineString[iStrLoc], nPreFixLength);
    psCritStringTemp[nPreFixLength+1]= '\0';
    if ( !fStringHasPreFix(psCritStringTemp, scCriteria) )
    {
        /* Criteria string match NOT found */
        return fHasCriteria = false;
    }
    
    iStrLoc += ((int) strlen(scCriteria));

    iStrLoc += CountBlank (&scLineString[iStrLoc]);
    /* ON/OFF value for the criteria */
    iCnt = sscanf(&scLineString[iStrLoc], "%d",&iINT_value);
    fHasCriteria = iINT_value;
    iStrLoc += CountNonBlank (&scLineString[iStrLoc]);

    iStrLoc += CountBlank (&scLineString[iStrLoc]);
    iStrLoc += CountNonBlank (&scLineString[iStrLoc]);

    iStrLoc += CountBlank (&scLineString[iStrLoc]);


    iCnt = sscanf(&scLineString[iStrLoc], "%f",&fREAL_value);
    if ( (EOF == iCnt) || (  1 != iCnt) ) 
        return fHasCriteria = false;
    *pdDBL_value = fREAL_value;

    return fHasCriteria;
}

/*
 * --------------------------------------------------------------------------
 * read_criteria
 // Read criteria file.
 * --------------------------------------------------------------------------
 */
int paramReader::read_criteria()
{
    
  int  iRet = 0;
  int  iCnt=0;

  int           iValueLoc = 0;
  double        dDBL_value = 0.0;
  int           iINT_value = 0;
 

  /* // Start at the beginning of the file  */

  if (0 == m_fp_xml) 
  {
      goto Exit;
  }
  rewind(m_fp_xml);
  
  while (fgetsSkipComments(m_nextLine, PARAMREADER_MAX_LINE_LENGTH, m_fp_xml)) 
  {

      iValueLoc = CountBlank (m_nextLine);
      if ( m_nextLine[iValueLoc]>='0' && m_nextLine[iValueLoc]<='9' )
      {
          /* Read only lines starting with Nos */
          iCnt = sscanf(&m_nextLine[iValueLoc], "%d",&iINT_value);
          if ( (EOF == iCnt) || (  1 != iCnt) ) 
              iRet = -1;
          if ( iINT_value==3 )
          {
              /* Aspect ratio */
              if ( ReadCriteriaValue( "aspect ratio", m_nextLine, &dDBL_value))
                  Set_Aspect_Ratio (dDBL_value);
          }
          else if ( iINT_value==10 )
          {
              /* Jacobian */
              if ( ReadCriteriaValue( "jacobian", m_nextLine, &dDBL_value))
                  Set_Jacobian (dDBL_value);
          }
          else if ( iINT_value==11 )
          {
              /* Tet collapse */
              if (ReadCriteriaValue( "tet collapse", m_nextLine, &dDBL_value))
                  Set_Tet_Collapse (dDBL_value);
          }
          
          else if ( iINT_value==1 )
          {
              /* Warp */
              if (ReadCriteriaValue( "warp", m_nextLine, &dDBL_value))
                  Set_Warp (dDBL_value);
          }
          else if ( iINT_value==6 )
          {
              /* Skew */
              if (ReadCriteriaValue( "skew", m_nextLine, &dDBL_value))
                  Set_Skew (dDBL_value);
          }
          else if ( iINT_value==2 )
          {
              /* Taper */
              if (ReadCriteriaValue( "taper", m_nextLine, &dDBL_value))
                  Set_Taper (dDBL_value);
          }
          else if ( iINT_value==4 )
          {
              /* Min angle */
              if (ReadCriteriaValue( "2D min angle", m_nextLine, &dDBL_value))
                  Set_2D_MinAngle (dDBL_value);
          }
          else if ( iINT_value==5 )
          {
              /* Max angle */
              if (ReadCriteriaValue( "2D max angle", m_nextLine, &dDBL_value))
                  Set_2D_MaxAngle (dDBL_value);
          }
          else if ( iINT_value==7 )
          {
              /* Jacobian ratio */
              if (ReadCriteriaValue( "jacobian ratio", m_nextLine, &dDBL_value))
                  Set_Jacobian_Ratio (dDBL_value);
          }
          
      }
                
  } /* while (fgetsSkipComments(m_nextLine, PARAMREADER_MAX_LINE_LENGTH,... */

  Exit:

  return iRet;
}

