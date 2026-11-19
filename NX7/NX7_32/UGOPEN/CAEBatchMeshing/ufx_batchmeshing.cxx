/*****************************************************************************
**
**                 ========================================
*                        B A T C H    M E S H I N G
*                        --------------------------
*                  ========================================
*
*                 ------------------------------------------
**                    Main File : ufx_batchmeshing.cxx
**                ParamFile : ufx_batchmeshing_paramreader.h, 
**                            ufx_batchmeshing_paramreader.cxx
**                     Nov. 27, 2005 : Initial creation
**                               Ashish Das 
*                 ------------------------------------------
*
**
** Description:
**    
*     
     General 
     =======
         This program generates tet mesh (as of Nov/2005) on a solid part in batch 
         mode. (It can be enhanced to generate other types of meshes in future.)

         In the case of tet mesh, the failure to generate tet mesh results in partial
         surface mesh and that is saved in fem file. Thus it is better to run with
         -fem option so that fem file is saved.  In case only -dat option is specified
         the partial surface mesh will not be dumped in the .dat file.

         
     Usage:  From command line :
     =========================

           ufx_batchmeshing  -?  -h or -H 
                             -part=<Partname> -p=<Parameter file name> 
                             -c=<Criteria file name> -no_idealize  
                             -fem -dat=<extension> -key_word=<some keyword string> 
                             
            -?  -h or -H                    : Help on usage.
                                         

            -part=<Partname>                : Part name without .prt extension.
                                              Error if part does not exist or error in 
                                              opening. Must be valid ug part file.
                                              The part name string is also used to build 
                                              name strings for .fem, .dat, idealized part 
                                              and .LOG file.
                                              [please see "More on naming convention" 
                                               below]

            -p=<Parameter file name>        : Parameter file name; must have specific 
                                              format.
                                              If not specified, program uses default 
                                              ug parameters.
                                              Example format is in the top of the file
                                              documentation in ufx_batchmeshing.cxx

            -c=<Criteria file name>         : Criteria file name; must have specific 
                                              format 
                                              If not specified, program uses defaults.
                                              Example format is in the top of the file
                                              documentation in ufx_batchmeshing.cxx

            -solver=<Solver name>           : Solver name values are
                                                  "MSC_NASTRAN"
                                                  "NX_NASTRAN"
                                                  "ANSYS" 
                                                  "ABAQUS" 
                                                  "NX_THERMAL_OR_FLOW"
                                              Default is NX_NASTRAN (if param opt. not 
                                              specified)

            -no_idealize                    : Do not create idealized part.
                                              (If not specified, will create idealized 
                                               part)
                                              If file exists, the old file is over-
                                              written.

            -fem                            : Tells program to save .fem file
                                              (If not specified will not save fem file)
                                              If file exists, the old file is over-
                                              written.

            -dat=<extension>                : Tells program to dump out nastran deck.
                                              (If not specified will not dump nastran bulk 
                                               data)
                                              The extension value (string) is optional and 
                                              is used by the program to specify extension 
                                              to the blk data file. Example some user prefer 
                                              .blk than .dat extension.
                                              If file exists, the old file is over-written.

            -key_word=<some keyword string> : This keyword is optional and is embeded into 
                                              the name string of the fem/idealized part,...
                                              names for identification. This allows user
                                              greater flexibility to name their fems, etc.
                                              Example if many meshes are needed on same part
                                              with different sizes say 5mm, 10mm etc., key 
                                              word "_5mm", "_10mm" etc. may be specified.
                                              [please see "More on naming convention" below]


      More on naming convention:
      =========================
         The batch meshing program takes the part name and builds name strings for
         idealized part/fem/sim/meshing report etc. using the part name. Following
         are the name strings build:
                
            Idealized part name   : "<Part_name>__IDEALIZED__<keyword>.prt"
            fem file name         : "<Part_name>__FEM__<keyword>.fem"
            batch mesh report log : "<Part_name>__FEM__<Keyword>__MeshReport.LOG" 
            sim file name         : "<Part_name>__SIM__<keyword>.sim"

            solver deck names     : "<Part_name>__<solver name>__<keyword>.<extn>"
            <extn> values for language settings:
                NX_NASTRAN  : ".dat"
                MSC_NASTRAN : ".dat" 
                ANSYS       : ".inp" 
                ABAQUS      : ".inp"
                NX_THERMAL_OR_FLOW : ".xml"


      Building Batch Meshing Executable using UG Open:
      ===============================================
         In order to build batch-mesher using UG Open following steps
         need to be followed:

         -  User must have UG open licence.
         -  In the command shell following variables must be available
            other wise do "export" or on windows "set"
              export UGII_BASE_DIR=<where_ever_UG_installed>/sol/kits
              export UGII_ROOT_DIR=$UGII_BASE_DIR/ugii 
              export UGII_USERFCN=$UGII_BASE_DIR/ugii
            Note above paths are for unix; for windows "/"'s are "\".
          
         -  Get following files from examples directory
               ufx_batchmeshing.cxx
               ufx_batchmeshing_paramreader.cxx
               ufx_batchmeshing_paramreader.hxx
        
         - Follow standard UG open build and link procvess using either
              $UGII_BASE_DIR/ugopen/ufcomp 
              $UGII_BASE_DIR/ugopen/uflink

           OR ugmenu.


      Looks of param file:
      ===================
          
           -  Here is a sample of param file (produced below)
              You may cut & paste in a text file and use.
           -  A line starting "# " i.e., # followed by blank is comment
              line and is ignored.
           -  If a parameter field is not specified default
              value is used.  
           -  Default values are in the macro UF_UG__BatchMesh_MESHParams 
              in this file.
           -  A sample param file is provided : sample_BatchMesh_param.txt
      
-----------------------  Sample batch mesh param file ------------------------

# Sample batch parameters file for Closures models with 12mm average element size


#mesh:

# 0.0 or (-)ive element size is auto size or not specified
element_size           12.0
# Valid values of element_type: TET_10, TET_4, TRI_3, TRI_6, QUAD_4, QUAD_8
element_type           TET_10

# Values of mid_node_option are "Mixed", "Straight", "Curved"
mid_node_option        Mixed
max_jacobian           12.345
surface_mesh_variation 50.0
volume_mesh_variation  50.0
small_feature_size     10.0

surf_component         1
feature_angle          30.0

#fillets:

# Values of fillet_type are  "all", "Inside", "Outside"
fillet_type            all
min_fillet_radius      0.0
max_fillet_radius      5.0
elem_per_quarter_round 3

-----------------------  Sample batch mesh param file ------------------------



      Looks of criteria file:
      ======================
          
           -  Here is a sample of criteria file (produced below)
              You may cut & paste in a text file and use.
           -  The numbers in the 1st column under "#" must be maintained.
           -  For tet meshing only aspect ratio, jacobian and tet collapse
              are used.
              The values taken for each are what is under "Ideal" column.
              Rest of the values are ignored (may be in future we will 
              use more of these).
           -  If no criteria file is specified or appropriate values
              are not set, default values are used.
           -  Default values are obtained from user defaults (set during mesh
              recipe creation from xmls).
           -  A sample criteria file is provided : sample_BatchMesh_criteria.txt
      
-----------------------  Sample batch mesh criteria file ------------------------

Sample Criteria file for Closure models with 12mm average element size

 #    Criterion     On  Wt   Ideal    Good    Warn    Fail   Worst 

 0 penalty value              0.00    0.00    0.80    1.00   10.00 
 1 min length        1   1   12.00    8.00    7.00    5.00    0.50 
 2 max length        1   1   12.00   15.00   20.00   25.00   50.00 
 3 aspect ratio      1   1    1.00    2.00    4.00    5.00   12.00 
 4 warpage           1   1    0.00    5.00   10.00   15.00   90.00 
 5 max angle quad    1   1   90.00  110.00  125.00  140.00  180.00 
 6 min angle quad    1   1   90.00   70.00   55.00   40.00    0.00 
 7 max angle tria    1   1   60.00   80.00  100.00  120.00  180.00 
 8 min angle tria    1   1   60.00   50.00   30.00   20.00    0.00 
 9 skew              1   1    0.00   10.00   55.00   60.00   90.00 
10 jacobian          1   1    1.00    0.90    0.60    0.50    0.00 
11 tet collapse      1   1    11.00    0.90    0.60    0.50    0.00 
12 chordal dev       0   0    0.00    0.30    0.80    1.00    2.00 
13 % of trias        1   1    2.00    3.00   4.640    5.00   6.111


-----------------------  Sample batch mesh criteria file ------------------------


      Notes on program for some one to hack & modify this code:
      ========================================================

           -  The data for the main program (i.e., the command line options) are 
              specified through the str  UF_UG_BatchMesh_CommandLineOpts_t. 

           -  If more command line arguements are needed, then easiest will be 
              to augment the structure UF_UG_BatchMesh_CommandLineOpts_t and 
              read/fill in the fields by following what is done in the routine
              do_command_line_arg_parsing(). (Use those standard ug open functions
              e.g., uc4620 etc., so that porting platforms are taken care off.)
              
              -> Note if adding a string variable in str declare it a char array
                 of length UF_UG_BATCH_MESH__MAX_NAME_LEN so that memory alloc
                 or free issues are not involved and looks like ug open does not
                 like strings above that length anyway.
              
              -> If a new field is added, do initialize it in the macro
                 UF_UG__BatchMesh_INITBatchParams(pzParams).

              -> Also, if possible add to the help text in the string below
                 scHelpText[]. (The format is easy to follow)
           
           -  The mesh parameters are specified through the structure 
              UF_UG_BatchMesh_Parms_t

              -> If a new field is added, do initialize it in the macro
                 UF_UG__BatchMesh_MESHParams(pzParams)

              do_Batch_Meshing__main is the highest level function that sets
              the batch meshing process, i.e., creates fem, idealized part
              does solver setting etc.

              Inside the function do_Batch_Meshing__main there is a for loop
              on bodies and a call to UF_SF_create_ugs_tet_mesh_wt_abstraction_control
              where tet meshing is done. So for surface meshing this is where
              surface mesh routine will have to be added.
        
*
*
* =======================================================================
*  Revision History
* =======================================================================
*    Date          Name                 Description of Change
*    ----          ----                 ---------------------
* 27-Nov-2005  Ashish Das      Initial version completed with all requirements. 
*                              (Supports only Tet meshing in NX401 and above)
* 13-Dec-2005  Ashish Das      Many minor fixes; added help & more comments.
*                              [1st time submission to environment]
* 06-Jan-2006  Ashish Das      Fixed some QAZ errors.
* 09-Jan-2006  Ashish Das      Fixed QAZ;s associated with help messaage.
* 13-Jan-2006  Ashish Das      After getting QAZ exception for compile error with
*                              include ufx_batchmeshing_paramreader.hxx.
* 17-Jan-2006  Ashish Das      Changes prototype of main : Compile error on linux.
* 17-Jan-2006  Ashish Das      Fix for PR 5386872 : Added option "None" to fillet
*                              processing. Corrected default small_feature_size to 10.0
* 19-Jan-2006  Ashish Das      Added date/time stamp and total process time.
* 02-Feb-2006  Ashish Das      Fix for political problems! QAZ folks do not like
*                              QAZ exceptions; revert back include to <> form.
* 08-Mar-2006  Ashish Das      Fix for political problems! QAZ folks do not like
*                              QAZ exceptions; revert back include to <> form.
*                              (Back-porting 02-Feb-2006 changes from Nx401)
* 14-Mar-2006  Ashish Das      Analysis type for Thermal & Flow option was not correct.
* 15-Mar-2006  Ashish Das      Added partial support for Quad & Tri meshing of body panels
*                              (Part I). 
* 21-Mar-2006  Ashish Das      Fix for idealized part not being deleted before fem creation.
* 23-Mar-2006  Ashish Das      QAZ errors because of new QAZ rules.
* 12-Sep-2006  Vasa M. Reddy   Turn on format option for partial meshes.
* 02-Oct-2006  Vasa M. Reddy   Initialize meshing and abstraction structures(PR: 5606156).
* 22-Nov-2006  Ashish Das      Enhancements requests from NX5 beta: Mesh transition,
*                              Meshing method for paving.
* 07-Mar-2007  Ashish Das      PR 5426353: Failure on linux platform; vfprintf crashing because
*                              va_start not called for each vprintf & vfprintf call.
* 28-Aug-2008  Ashish Das      Support for 2D mesh criteria.
* 17-Nov-2008  Ashish Das      Support for new NX6 meshing parameters.
*
**
*$HISTORY$
*****************************************************************************/


/* Include files */
#if ! defined ( __hp9000s800 ) && ! defined ( __sgi ) && ! defined ( __sun )
#   include <strstream>
#   include <iostream>
    using std::ostrstream;
    using std::endl;    
    using std::ends;
    using std::cerr;
#else
#   include <strstream.h>
#   include <iostream.h>
#endif
#include <uf.h>
#define UF_CALL(X) (report_error( __FILE__, __LINE__, #X, (X)))


/* ============================
        Includes needed 
   ============================ */
#include <stdio.h>
#include <time.h>
#include <string.h>
#include <stdarg.h>
#include <math.h>

#include <uf.h>
#include <uf_sf.h>
#include <uf_ui.h>
#include <uf_cfi.h>
#include <uf_obj.h>
#include <uf_defs.h>
#include <uf_part.h>
#include <uf_retiring.h> 
#include <uf_assem.h>


#include <ufx_batchmeshing_paramreader.hxx>
#include <uf_sf_mshvld.h>


/* ==========================================
      Text of the help on command usage
   ========================================== */

static char *scHelpText[] = {
    "UF_UG_BatchMeshing  -? -h -H -part=<Partname> -p=<Parameter file name>",
    "                    -c=<Criteria file name> -no_idealize",  
    "                    -fem -dat -key_word=<some keyword string>",
    "             ",
    "             ",
    "   -?  -h or -H               : Help on usage.",
    "             ",
    "             ",
    "   -part=<Partname>           : Part name without .prt extension.",
    "                                Error if part does not exist or error ",
    "                                in opening. Must be valid ug part ",
    "                                file. The part name string is also ", 
    "                                used to build name strings for .fem,", 
    "                                .dat, idealized part and .LOG file.",
    "                                [please see \"More on naming conven- ",
    "                                 tion\" below]",
    "             ",
    "             ",
    "   -p=<Parameter file name>   : Parameter file name(specified format)", 
    "                                If not specified, program uses default", 
    "                                ug parameters.",
    "                                For example format, see top of the file",
    "                                ufx_batchmeshing.cxx OR look in the DIR",
    "                                ($UGII_BASE_DIR/ugopen/CAEBatchMeshing)",
    "             ",
    "             ",
    "   -c=<Criteria file name>    : Criteria file name(specified format)",  
    "                                If not specified, program uses defaults.",
    "                                For example format, see top of the file",
    "                                ufx_batchmeshing.cxx  OR look in the DIR",
    "                                ($UGII_BASE_DIR/ugopen/CAEBatchMeshing)",
    "             ",
    "             ",
    "   -solver=<Solver name>      : Solver name values are", 
    "                                    \"MSC_NASTRAN\" ", 
    "                                    \"NX_NASTRAN\" ", 
    "                                    \"ANSYS\" ", 
    "                                    \"ABAQUS\" ", 
    "                                    \"NX_THERMAL_OR_FLOW\" ", 
    "                                Default is NX_NASTRAN (if param opt.", 
    "                                not specified)", 
    "             ",
    "             ",
    "   -no_idealize               : Do not create idealized part.",
    "                                (If not specified, will create idealized ",
    "                                 part)",
    "                                If file exists, the old file is over-",
    "                                written.",
    "             ",
    "             ",
    "   -fem                       : Tells program to save .fem file",
    "                                (If not specified will not save fem file)",
    "                                If file exists, the old file is over-",
    "                                written.",
    "             ",
    "             ",
    "   -dat=<extension>           : Tells program to dump out nastran deck.",
    "                                (If not specified will not dump nastran ",
    "                                 bulk data)",
    "                                The extension value (string) is optional", 
    "                                and is used by the program to specify",
    "                                extension to the blk data file. Example ",
    "                                some user prefer .blk than .dat extension.",
    "                                If file exists, the old file is over-",
    "                                written.",
    "             ",
    "             ",
    "   -key_word=<keyword string> : This keyword is optional and is embeded ",
    "                                into the name string of the fem/idealized ",
    "                                part,... names for identification. This",
    "                                allows user greater flexibility to name ",
    "                                their fems, etc. Example if many meshes ",
    "                                are needed on same part with different",
    "                                sizes say 5mm, 10mm etc., key word \"_5mm\",",
    "                                \"_10mm\" etc. may be specified. [please ",
    "                                see \"More on naming convention\" below]",
    "             ",
    "             ",
    "  More on naming convention:",
    "  =========================",
    "     The batch meshing program takes the part name and builds name strings",
    "     for idealized part/fem/sim/meshing report etc. using the part name. ",
    "     Following are the name strings build:",
    "             ",    
    "       Idealized part name  : \"<Part_name>__IDEALIZED__<keyword>.prt\"",
    "       fem file name        : \"<Part_name>__FEM__<keyword>.fem\" ",
    "       batch mesh report log: \"<Part_name>__FEM__<Keyword>__MeshReport.LOG\"",
    "       sim file name        : \"<Part_name>__SIM__<keyword>.sim\"",
    //{"             "}, 
    "       solver deck names    : \"<Part_name>__<solver name>__<keyword>.<extn>\"",
    "          <solver name> and <extn> values are:",
    "          NX_NASTRAN  : \".dat\" ",
    "          MSC_NASTRAN : \".dat\" ",
    "          ANSYS       : \".inp\" ",
    "          ABAQUS      : \".inp\" ",
    "          NX_THERMAL_OR_FLOW : \".xml\" ",
    "             ",
    /* Important : Leave the following line intact. */
    "END_HELP"
};


/* ==========================================
                  Defines
   ========================================== */
#define UF_UG_BATCH_MESH__VERSION         "1.0"  // Batch meshing version file
#define UF_UG_BATCH_MESH__SCREEN_DUMP_ON  1
#define UF_UG_BATCH_MESH__MAX_NAME_LEN    MAX_FSPEC_SIZE  /* Max file length */

/* Batch mesh parameter names */
#define UF_UG_BATCH_MESH__PARM_help_str1       "?"      /* Help related */
#define UF_UG_BATCH_MESH__PARM_help_str2       "h"
#define UF_UG_BATCH_MESH__PARM_help_str3       "H"

#define UF_UG_BATCH_MESH__PARM_input_part      "part"
#define UF_UG_BATCH_MESH__PARM_param_file      "p"
#define UF_UG_BATCH_MESH__PARM_criteria_file   "c"
#define UF_UG_BATCH_MESH__PARM_solver_name     "solver"
#define UF_UG_BATCH_MESH__PARM_idealize_output "no_idealize"
#define UF_UG_BATCH_MESH__PARM_fem_output      "fem"
#define UF_UG_BATCH_MESH__PARM_jt_output       "jt"
#define UF_UG_BATCH_MESH__PARM_nastran_output  "dat"
#define UF_UG_BATCH_MESH__PARM_key_word        "key_word"

#define UF_UG_BATCH_MESH__start_watch    0
#define UF_UG_BATCH_MESH__stop_watch     1

/* ==========================================
       Typedef's valid for this file 
   ========================================== */

/* ==========================================
       Typedef's valid for this file 
   ========================================== */

/* ==== Batch mesher command line options ==== */
typedef struct UF_UG_BatchMesh_CommandLineOpts_s
{
    char            run_key_word[UF_UG_BATCH_MESH__MAX_NAME_LEN];

    int             fPartFile;                                        /* Must be specified */
    char            part_file_name[UF_UG_BATCH_MESH__MAX_NAME_LEN];   /* Part file name */

    int             fParamFile;                                       /* TRUE => Param file specified  */
    char            param_file_name[UF_UG_BATCH_MESH__MAX_NAME_LEN];  /* FALSE=> Parm file not supplied */       
   
    int             fCriteriaFile;                                      /* TRUE => Criteria file specified */
    char            criteria_file_name[UF_UG_BATCH_MESH__MAX_NAME_LEN]; /* FALSE=> Parm file not supplied */       
   
    char            Solver_Name[UF_UG_BATCH_MESH__MAX_NAME_LEN];        /* Name of the solver 
                                                                           Default : NX NASTRAN */

    int             fOutIdealized;      /* TRUE/FALSE Whether to create idealized part */
    int             fOutputFEM;         /* TRUE/FALSE Whether to save fem */

    int             fOutputDAT;         /* TRUE/FALSE Whether to save NASTRAN .dat */
    char            dat_file_extn[UF_UG_BATCH_MESH__MAX_NAME_LEN]; /* Extension for dat file optional */

    int             fOutputJT;          /* TRUE/FALSE Whether to save JT file */

} UF_UG_BatchMesh_CommandLineOpts_t, *UF_UG_BatchMesh_CommandLineOpts_p_t;


/* ==== Mesher options ==== */
typedef struct UF_UG_BatchMesh_Parms_s
{
    char   scElemType[UF_UG_BATCH_MESH__MAX_NAME_LEN];  /* Element type string 
                                                           ALL_MESH_TYPES : be smart to mesh
                                                                            sheets tris, solids test
                                                           TET_4, TET_10
                                                           TRI_3, TRI_6
                                                           QUAD_4, QUAD_8 */

    int    midnodes;                            /* TRUE for tet10s,
                                                FALSE for tet4s. */
    int    fAutoSize;                        /* Whether to do auto size */
    double element_size;                     /* Desired element size.  If
                                                zero or negative, then mesher
                                                will choose element size
                                                internally. */
    UF_SF_ugs_mesher_midnode_option_t  midnode_option;
                                             /* Whether to project midnodes
                                                or not. */
    double maximum_midnode_jacobian;         /* If midnode_option =
                                                UF_SF_UGS_MESHER_mixed_midnodes,
                                                any element with a jacobian
                                                value higher than
                                                maximum_midnode_jacobian will
                                                have its midnodes
                                                straightened. */
    double minimum_face_angle;               /* Minimum angle at corner of a
                                                face that can support element.
                                                corners smaller than this will
                                                be pinched out.  This angle is
                                                measured in degrees. */
    int    surf_mesh_size_variation;         /* This controls how much variation
                                                in element size is
                                                desired/permitted in the mesh on
                                                the surface of the bodies being
                                                meshed. Valid values go from 0
                                                to 100.  This number does not
                                                coorespond directly to any
                                                actual meshing parameter, but
                                                rather is a relative scale that
                                                the user can use to indicate
                                                their tolerance for mesh
                                                variation.  It is used
                                                internally in the mesher to
                                                calculate expansion factors and
                                                a minimum element size. 0
                                                means that there will be
                                                minimumal element size
                                                variation.  100 means that there
                                                will be maximum element size
                                                variation. */
    int      tet_mesh_size_variation;           /* This controls whether the tets
                                                are permitted to expand as you
                                                progress into the interior of
                                                the body.  Valid values go from
                                                0 to 100.  0 means that
                                                element sizes must remain
                                                relatively constant.  100 means
                                                that the elements can expand
                                                very rapidly. */


    double    small_feature_size;           /* Small feature as % of element length */

    int       edge_merge_toggle;            /* Toggle for merge edge */
    double    edge_merge_angle;             /* Angle for merging edges */

    int       process_fillets;               /* true => Process fillets
                                                false=> do not process fillets */

    UF_SF_ugs_abstraction_fillet_type_option_t   fillet_type;   /* Fillet type */

    double    min_fillet_radius;             /* Min fillet radius */   
    double    max_fillet_radius;             /* Max fillet radius */
    int       elem_per_quarter_round;        /* No of elements per quarter round */

    /* =============================
       Additional params for 2d mesh
       ============================= */
    double    edge_match_tolerance;          /* UG edge matching
                                                tolerance. */ 
    int       format_mesh;                   /* TRUE if 2d mesh is a shell
                                                mesh that should be formatted
                                                to the solver.  FALSE if 2d
                                                mesh is a seed mesh and not to
                                                be formated out to solver.  */     
    int       attempt_quad_mapping;          /* TRUE if map mesher should be
                                                tried on faces for quad meshes
                                                or if free mesher should be
                                                called regardless of face
                                                shape. */      
    int       quad_only_option;              /* Applies only when attempt_quad_mapping=FALSE
                                                Values are:
                                                0 => Allow triangles OFF.
                                                1 => Allow triangles ON & 0 Triangle
                                                2 => Allow triangles ON & 1 Triangle 
                                                
                                                If attempt_quad_mapping==TRUE does not
                                                apply.*/
    int       split_poor_quads;              /* TRUE if poorly shaped quads
                                                should be split into
                                                triangles.
                                                FALSE if quads should be kept
                                                regardless of quality. */             
    double    maximum_quad_warp;            /* if split_poor_quads == TRUE,
                                                this is the warp quality
                                                threshold.  Any quad with
                                                greater warp than this will
                                                be split. */

    int       mesh_method;                  /* Only used for 2D mesh.
                                               Meshing method: 1=>"Paver" or 
                                                               0=>"Automatic" 
                                               Default : Automatic */

    int       mesh_transition_ON_OFF;       /* Mesh transition parameter Toggle state */

} UF_UG_BatchMesh_Parms_t, *UF_UG_BatchMesh_Parms_p_t;

/* ======================== 
         Static Data
   ======================== */
static FILE *UF_UG__BatchMesh_LOG = NULL;


/* ============================= 
         Macro Definitions
   ============================= */ 

/* --- Initialize parameters for batch run --- */
#define   UF_UG__BatchMesh_INITBatchParams(pzParams) \
          strcpy((pzParams)->run_key_word, "");      \
          (pzParams)->fPartFile = false;             \
          strcpy((pzParams)->part_file_name, "");    \
          (pzParams)->fParamFile = false;            \
          strcpy((pzParams)->param_file_name, "");   \
          (pzParams)->fCriteriaFile = false;         \
          strcpy((pzParams)->criteria_file_name, "");\
          strcpy((pzParams)->Solver_Name,"NX_NASTRAN");   \
          (pzParams)->fOutIdealized = true;          \
          (pzParams)->fOutputFEM = true;             \
          (pzParams)->fOutputDAT = false;            \
          strcpy((pzParams)->dat_file_extn, "");     \
          (pzParams)->fOutputJT = false;
              
/* --- Initialize meshing parameters  --- 
       The mid node options are:
          UF_SF_UGS_MESHER_straight_midnodes=0 :Midnodes placed at straight line linear location 
                                                between corner nodes. 
          UF_SF_UGS_MESHER_curved_midnodes=1   :Midnodes project to underlying geometry. 
          UF_SF_UGS_MESHER_mixed_midnodes=2    :Midnodes projected to underlying geometry, unless
                                                doing so would input Jacobian error threshold.
 */
#define   UF_UG__BatchMesh_MESHParams(pzParams)     \
          strcpy((pzParams)->scElemType, "ALL_MESH_TYPES"); \
          (pzParams)->midnodes = true;              \
          (pzParams)->fAutoSize = true;             \
          (pzParams)->element_size = -1;             \
          (pzParams)->midnode_option = UF_SF_UGS_MESHER_mixed_midnodes;        \
          (pzParams)->maximum_midnode_jacobian = 10;\
          (pzParams)->minimum_face_angle = 15;      \
          (pzParams)->surf_mesh_size_variation = 50;\
          (pzParams)->tet_mesh_size_variation = 50; \
          (pzParams)->small_feature_size = 10.0; \
          (pzParams)->edge_merge_toggle = false;            \
          (pzParams)->edge_merge_angle = 15;\
          (pzParams)->process_fillets = false; \
          (pzParams)->fillet_type = UF_SF_UGS_ABSTRACTION_FILLET__all; \
          (pzParams)->min_fillet_radius = 5; \
          (pzParams)->max_fillet_radius = 10; \
          (pzParams)->elem_per_quarter_round = 3; \
          (pzParams)->edge_match_tolerance = 0.508; \
          (pzParams)->format_mesh = TRUE; \
          (pzParams)->attempt_quad_mapping = TRUE; \
          (pzParams)->quad_only_option = 0; \
          (pzParams)->split_poor_quads = TRUE; \
          (pzParams)->maximum_quad_warp = 10.0;\
          (pzParams)->mesh_method = 0; \
          (pzParams)->mesh_transition_ON_OFF = false;



/* ==================================================
      Build appropriate solver deck extensions for 
      appropriate solver languages.
   ================================================== */
#define UF_UG__BatchMesh_GetDefaultSolverDeckFileExtn(scSolverName, scDeckExtn) \
          if (!strcmp((scSolverName), "MSC_NASTRAN"))                   \
             strcpy ((scDeckExtn), ".dat");                             \
          else if (!strcmp((scSolverName), "NX_NASTRAN"))               \
             strcpy ((scDeckExtn), ".dat");                             \
          else if (!strcmp((scSolverName), "ANSYS"))                    \
             strcpy ((scDeckExtn), ".inp");                             \
          else if (!strcmp((scSolverName), "ABAQUS"))                   \
             strcpy ((scDeckExtn), ".inp");                             \
          else if (!strcmp((scSolverName), "NX_THERMAL_OR_FLOW"))       \
             strcpy ((scDeckExtn), ".xml");                             \
          else                                                          \
             strcpy ((scDeckExtn), ".dat");

/* =============================================
      Get proper solver language setup.
   ============================================= */
#define UF_UG__BatchMesh_GetSolverDeckName(scSolverName, scDeckName) \
          if (!strcmp((scSolverName), "MSC_NASTRAN"))                   \
             strcpy ((scDeckName), "MSC_NASTRAN");                             \
          else if (!strcmp((scSolverName), "NX_NASTRAN"))               \
             strcpy ((scDeckName), "NX_NASTRAN");                             \
          else if (!strcmp((scSolverName), "ANSYS"))                    \
             strcpy ((scDeckName), "ANSYS");                             \
          else if (!strcmp((scSolverName), "ABAQUS"))                   \
             strcpy ((scDeckName), "ABAQUS");                             \
          else if (!strcmp((scSolverName), "NX_THERMAL_OR_FLOW"))       \
             strcpy ((scDeckName), "NX_THERMAL_OR_FLOW");                             \
          else                                                          \
             strcpy ((scDeckName), "NX_NASTRAN");

/* =============================================
      Check if mesh type set is 2D.
   ============================================= */
#define UF_UG__BatchMesh_Is2DMesh(scMeshType)      \
          ( (!strcmp((scMeshType), "TRI_3")) ||    \
            (!strcmp((scMeshType), "TRI_6")) ||    \
            (!strcmp((scMeshType), "QUAD_4"))||    \
            (!strcmp((scMeshType), "QUAD_8"))      \
            )

/* =======================================
      Check if mesh type set is 3D.
   ======================================= */
#define UF_UG__BatchMesh_Is3DMesh(scMeshType)      \
          ( (!strcmp((scMeshType), "TET_4")) ||    \
            (!strcmp((scMeshType), "TET_10"))     \
          )

/* ==============================================
      Check if mesh type is not set so we will
      use default value.
   ============================================== */
#define UF_UG__BatchMesh_MeshTypeNotSet(scMeshType)      \
          ( (!strcmp((scMeshType), "ALL_MESH_TYPES"))    \
          )


/* ==========================================
           Local function prototype
   ========================================== */
static void do_command_line_arg_parsing(char argc, 
                                        char *argv[],
                                        UF_UG_BatchMesh_CommandLineOpts_t *pzBatchRunParams,
                                        int  *pfDisplayCommandHelp);
static void get_mesh_parameters ( UF_UG_BatchMesh_CommandLineOpts_t *pzBatchRunParams, 
                                  UF_UG_BatchMesh_Parms_t           *pzMesh_params);
static int open_part( char *PartName, tag_t *part_tag);
static int create_fem__with_name_from_part_name ( tag_t         cad_part_tag,
                                                  /* char          *cad_part_name, */
                                                  const char*   solver_name,
                                                  const char*   analysis_type_name,
                                                  int           fCreateIdealizedPart,
                                                  UF_UG_BatchMesh_CommandLineOpts_t *pzBatchRunParams,
                                                  tag_t         *new_fem_tag);
static int create_sim__with_name_from_part_name ( tag_t         cad_part_tag,
                                                  tag_t         fem_tag, 
                                                  UF_UG_BatchMesh_CommandLineOpts_t *pzBatchRunParams,
                                                  tag_t         *new_sim_tag);
static int do_Batch_Meshing__main (tag_t                              tag_part_to_mesh,
                                   UF_UG_BatchMesh_CommandLineOpts_t *pzBatchRunParams);
static int get_a_material ( tag_t    *material_tag);
static void report_msg( char *msg);

static void write_info_fprintf(bool        fToConsole, 
                               FILE       *fp,             /* I   : File to print*/
                               const char *format_string,  /* I   */
                               ...                         /* I   */ );
static void display_command_help( char *scHelpText[] );
static int build_name_srting (  int       iNameOpt,
                                tag_t     cad_part_tag,
                                UF_UG_BatchMesh_CommandLineOpts_t *pzBatchRunParams, 
                                char      **NameString);
static void export_nastran_file ( tag_t cad_part_tag,
                                  tag_t fem_tag, 
                                  UF_UG_BatchMesh_CommandLineOpts_t *pzBatchRunParams);
static int rename_nastran_solver_deck_file ( tag_t cad_part_tag,
                                             char sol_name[], 
                                             UF_UG_BatchMesh_CommandLineOpts_t *pzBatchRunParams);
static void close_logfile (FILE   *fp  );
static FILE *open_logfile (tag_t  cad_part_tag, 
                           UF_UG_BatchMesh_CommandLineOpts_t *pzBatchRunParams );
static int write_mesh_quality_report ( char                              *scMestType,
                                       tag_t                             mesh_tag,
                                       UF_UG_BatchMesh_CommandLineOpts_t *pzBatchRunParams);
static void STOP_CLOCK ( int          start_end_flag, 
                         UF_timer_p_t pztimer, 
                         char         *scMessage);
static void Time_Sec_to_hr_min_sec(double dTimeSec, int *Hour, int *Min, double *dSec);
static void upper_to_lower_case ( char *scString);

static int validate_meshes
(
    int      num_meshes,
    tag_p_t  meshes_p,
    FILE     *details_fp
);

static int report_error( char *file, int line, char *call, int irc)
{
    if (irc)
    {
        char err[133],
             msg[133];

        sprintf(msg, "*** ERROR code %d at line %d in %s:\n+++ ",
            irc, line, file);
        UF_get_fail_message(irc, err);

        UF_print_syslog(msg, FALSE);
        UF_print_syslog(err, FALSE);
        UF_print_syslog("\n", FALSE);
        UF_print_syslog(call, FALSE);
        UF_print_syslog(";\n", FALSE);
    }

    return(irc);
}

/* ================================
            Main routine 
   ================================ */
extern int main( char argc, char *argv[] )
{
    int         iRc = 0;

    int                                     nParts_Saved = 0;
    tag_t                               part_tag = NULL_TAG;
    tag_t                               *saved_part_tags = NULL;
    
    
    UF_UG_BatchMesh_CommandLineOpts_t   zBatchRunParams;

    int                                 *error_list = NULL;

    char                                *ug_version = NULL;

    int                                 fDisplayCommandHelp = false;

    /* Just a printf to see if we indeed launch batch mesher */
    printf("Launching batchmesher core executable.\n");

    /* Initialize the API environment */
    if( UF_CALL(UF_initialize()) ) 
    {
        /* Failed to initialize */
        //printf("ERROR :  UG open module could not be initialized\n",);
        report_msg( "ERROR:  UG open module could not be initialized\n");
        report_msg( "        Exiting batchmesher...\n\n");
        return 0;
    }

    /* Command line processor */
    UF_CALL( UF_get_release(&ug_version) );
    printf("     \n\n");
    printf("==== Batch Meshing Version %s for UG %s ====\n",
                      UF_UG_BATCH_MESH__VERSION,ug_version);
    printf("   \n");
    printf("                 ==== REPORT ====  \n");
    printf("                      ------  \n\n");
    UF_free(ug_version);

    /* Command line parsing */
    do_command_line_arg_parsing ( argc, argv, &zBatchRunParams,
                                  &fDisplayCommandHelp);

    /* If user asked for help */
    if ( fDisplayCommandHelp )
       display_command_help( scHelpText );

    if ( zBatchRunParams.fPartFile== (int)true)
    {
        /* =================
             Open the part 
           ================= */
        iRc = open_part( zBatchRunParams.part_file_name, &part_tag);
        if ( iRc==0 || part_tag!=NULL_TAG)
        {
            /* =================================
                 Run batch meshing application
               ================================= */
            iRc = do_Batch_Meshing__main (part_tag, &zBatchRunParams);

            if ( zBatchRunParams.fOutputFEM==(int)true && iRc==0)
            {
                /* =========================
                    Save all the results
                ========================= */
                nParts_Saved = 0;
                iRc = UF_PART_save_all (&nParts_Saved, &saved_part_tags, &error_list);
                if ( saved_part_tags!=NULL )
                    UF_free(saved_part_tags);

                if ( error_list!=NULL )
                    UF_free (error_list);
            }

            /* ========================================================================
                Close the part
                scope   - 0 = Only specified part
                            1 = Part and all sub-assemblies
                mode    - 0 = Ask confirmation if part is modified
                                (Internal only, External assumes "Yes, Delete" answer)
                            1 = Unload part(s) even if modified
                            2 = Unload part(s) only if not modified
              ======================================================================== */
            UF_PART_close ( part_tag, 0, 1 );

        } /* if ( iRc!=0 || part_tag!=NULL_TAG) */
    }
    else
    {
        report_msg( "ERROR: Bad part name or Part name not supplied.\n");
        write_info_fprintf(true, NULL, "ERROR: Bad part name or Part name not supplied.\n");
        iRc = -9999;
    } /* if ( zBatchRunParams.fPartFile==true) */


    /* Terminate the API environment */
    UF_CALL(UF_terminate());

    return iRc;
}

/* ===========================================================
      Save the output files that are requested : .fem files
      nastran bulk data files ....
   =========================================================== */
static void export_nastran_file ( tag_t cad_part_tag,
                                  tag_t fem_tag, 
                                  UF_UG_BatchMesh_CommandLineOpts_t *pzBatchRunParams)
{
    int             iRc = 0;
    int             format_choice = 1;
    tag_t           new_sim_tag = NULL_TAG;

    tag_t           solution_desc = NULL_TAG, solver_desc = NULL_TAG;
    tag_t           language_tag = NULL_TAG, solution_tag = NULL_TAG;
    
    char            *sol_name = NULL;

    /* Timers */
    UF_timer_t     zSOLVER_DECK_time;
    
    if ( pzBatchRunParams->fOutputDAT==(int)true )
    {
        /* Start timer */
        STOP_CLOCK ( UF_UG_BATCH_MESH__start_watch, &zSOLVER_DECK_time, NULL );

        /* Create  simulation */
        iRc = create_sim__with_name_from_part_name ( cad_part_tag, fem_tag, 
                                        pzBatchRunParams, &new_sim_tag);
        if ( iRc==0 &&  new_sim_tag!=NULL_TAG )
        {
            /* Get language descriptor */
            UF_SFL_ask_cur_language_nx(&language_tag);

            /* Get solver descriptor */
            iRc = UF_SFL_ask_solver_nx  ( "NX NASTRAN", &solver_desc );

            /* Get any one solution descriptor */
            iRc = UF_SFL_ask_nth_solution_descriptor_nx ( language_tag,  0,&solution_desc );

            /* Create solution */
            build_name_srting ( 5, cad_part_tag, pzBatchRunParams, &sol_name);
            iRc = UF_SF_create_solution_nx( solution_desc, solver_desc, sol_name, 
                                            &solution_tag);
            

            /* =========================
                  Dump nastran deck 
               ========================= */
            UF_SF_solve_active_solution_nx(format_choice);

         
            /* Delete the sim now that solver deck is dumped. */
            //int uc4561( const char * fspec ,0 );
            //if ( iRc!=0 )
            //{
                /* Could not delete the file : Error out */
                //report_msg("\n        Could not delete existing .sim file.\n");
                //return -9999;
            //}

            
            /* Rename the nastran solver deck */
            rename_nastran_solver_deck_file ( cad_part_tag, sol_name, 
                                              pzBatchRunParams);
        }

        /* Solver deck time */
        STOP_CLOCK ( UF_UG_BATCH_MESH__stop_watch, &zSOLVER_DECK_time, 
                  "Time taken to dump solver deck ");
    }

    /* Free dynamically allocated memory */
    if ( sol_name!=NULL )
         UF_free (sol_name);

    return;

}

/* ===================================================================
         Re-names nastran solver deck file. (3rd party formatter
         do not give any control over the file name; so have to
         do it by renaming).
   =================================================================== */
static int rename_nastran_solver_deck_file ( tag_t cad_part_tag,
                                             char sol_name[], 
                                             UF_UG_BatchMesh_CommandLineOpts_t *pzBatchRunParams)
{

    int      iRc = 0, iLen = 0;

    char     *new_nastran_deck_name = NULL;
    char     *old_nastran_deck_name = NULL;
    char     scDeckExtn[UF_UG_BATCH_MESH__MAX_NAME_LEN] = {' '};

    /* Build name string of nastran deck to be */
    build_name_srting ( 6, cad_part_tag,pzBatchRunParams, 
                        &new_nastran_deck_name);

    
    /* Rename the solver deck file to what our naming convention 
       is. Typical names by nastran formater are in the form: 
       "<solution_name>-solver_deck.dat" 
       e.g. : blk_wth_hole__sim__my_run_test-solver_deck.dat 
       
       UF function to format solver internally builds the name string
       for dat file as : <Sim file name>-<solution name in lower case>.dat
       */
    build_name_srting ( 4, cad_part_tag,pzBatchRunParams, 
                        &old_nastran_deck_name);
    iLen = (int)strlen(old_nastran_deck_name);
    old_nastran_deck_name[iLen-4] = '\0'; /* Remove .sim*/
    strcat (old_nastran_deck_name, "-");
    upper_to_lower_case ( sol_name );
    upper_to_lower_case ( old_nastran_deck_name );
    strcat (old_nastran_deck_name, sol_name);

    /* Get extension based on solver language */
    UF_UG__BatchMesh_GetDefaultSolverDeckFileExtn(pzBatchRunParams->Solver_Name, \
                                                  scDeckExtn);
    strcat (old_nastran_deck_name, scDeckExtn);

    /* First check if there exists a file by name "new_nastran_deck_name".
       - if it does delet it first otherwise re-name will fail */
    iRc = uc4560 (new_nastran_deck_name, 0 );
    if ( iRc ==0 )
    {
        /* ========================================
           File exists IN CURRENT WORKING DIRECTORY
           So delete it from the system 
           ======================================== */
        iRc = uc4561 (new_nastran_deck_name, 0 );
        if ( iRc!=0 )
        {
            /* Could not delete the file : Error out */
            report_msg("Error : SOLVER Deck file already exists\n");
            report_msg("        File name : ");report_msg(new_nastran_deck_name);
            report_msg("\n        Could not delete existing file.\n");
            return -9999;
        }
    }

    /* Re-name the file */
    iRc = uc4562(old_nastran_deck_name ,0, new_nastran_deck_name);
    if ( iRc!=0 )
    {
        /* Could not delete the file : Error out */
        report_msg("\nCould not re-name solver deck file.\n");
        iRc = -9999;
        // return -9999;
    }
    
    /* Free dynamically allocated memory */
    if ( new_nastran_deck_name!=NULL )
        UF_free (new_nastran_deck_name);

    if ( old_nastran_deck_name!=NULL )
        UF_free (old_nastran_deck_name);

    return iRc;
}

/* ==========================================================
      Error message reporting function.

            msg         -i   Message string

      Return value:
            None
   ========================================================== */
static void report_msg( char *msg)
{       
    UF_print_syslog(msg, FALSE);
    //UF_print_syslog("\n", FALSE);

    if (!UF_UI_open_listing_window())
    {
        UF_UI_write_listing_window(msg);
        //UF_UI_write_listing_window("\n");
    }

} /* End of report_msg( char *msg) */

/* ==========================================================
      Function opens a part taking the part name string.

            PartName         -i   Name of the part
            part_tag         -o   Tag of the part

      Return value:
            0   => No error 
            !0  => Error in opening part.
   ========================================================== */
static int open_part( char *PartName, tag_t *part_tag )
{       
    
    int                     iRc = 0;
    UF_PART_load_status_t   error_status;

    /* Initialize output */
    *part_tag = NULL_TAG;

    
    /* Open the part */
    UF_PART_open( PartName, part_tag, &error_status );
    if ( *part_tag==NULL_TAG || error_status.failed )
    {
        report_msg("Can not open the part \n");
        iRc = -9999;
    }
    
    return iRc;

} /* End of open_part( char *PartName, tag_t *part_tag ) */

/* =======================================================================
      Function batch meshes a given part. High level routine that
      builds FEM name/creates fem etc.

            tag_part_to_mesh     -i   Tag of the part to batch mesh
            pzBatchRunParams     -i   Command line arguements regarding 
                                      the batch processing 

      Return value:
            0   => No error 
            !0  => Error.
   ======================================================================= */
static int do_Batch_Meshing__main (tag_t tag_part_to_mesh,
                                   UF_UG_BatchMesh_CommandLineOpts_t *pzBatchRunParams)
{

     int                            iRc = 0, i = 0;
     tag_t                          work_part_tag = NULL_TAG;
     tag_t                          new_fem_tag = NULL_TAG;
     tag_t                          iThis_Body_tag = NULL_TAG;

     char                           *CAD_Part_Name = NULL;
     char                           *FEM_file_Name = NULL;
     char                           *SIM_file_Name = NULL;
     char                           *IDEALIZED_file_Name = NULL;
     char                           *SOLVER_file_Name = NULL;
     char                           *MESH_LOG_file_Name = NULL;

     int                            nCAEBodies = 0;
     tag_t                          *CAEBodies_p = NULL;
     int                            body_type = -1;
     
     double                         dElemSize = 0.0;

     UF_UG_BatchMesh_Parms_t                    zMesh_params;
     UF_SF_ugs_tet_mesh_parms_t                 tet_mesh_params;
     UF_SF_ugs_2d_mesh_parms_t                  mesh_2d_params;
     UF_SF_ugs_mesh_abstraction_params_t        abs_params;
     

     tag_t                          mesh_tag = NULL_TAG;
     tag_t                          material_tag = NULL_TAG;

     char                           scSolverName[MAX_LINE_LENGTH] = {' '};
     char                           scAnalysisType[MAX_LINE_LENGTH] = {' '};
     char                           scMeshType[UF_UG_BATCH_MESH__MAX_NAME_LEN] = {' '};

     UF_system_info_t               zSystemInfo;

     /* Timers */
     UF_timer_t                     zOVERALL_timer;

     /* Initialize */
     UF_SF_ugs_tet_mesh_parms_INIT ( &tet_mesh_params );
     UF_SF_ugs_mesh_abstraction_parms_INIT ( &abs_params );
     UF_SF_ugs_2d_mesh_parms_INIT ( &mesh_2d_params );
     
     zSystemInfo.date_buf = NULL;      /* Current date and time info */
     zSystemInfo.user_name = NULL;     /* User, who is running this process */
     zSystemInfo.program_name = NULL;  /* The current program name */
     zSystemInfo.node_name = NULL;     /* Machine, on which this process is running */
     zSystemInfo.machine_type = NULL;  /* Hardware type on which the machine is running */
     zSystemInfo.os_name = NULL;       /* Operating system, on which this process is running*/
     zSystemInfo.os_version = NULL;    /* Version and release level of this Operating System */
    
     
     /* Query the working part */
     work_part_tag = UF_ASSEM_ask_work_part();
     if ( work_part_tag == NULL_TAG )
     {
         report_msg("This NX Open program requires a work part \n");
         return 9999;
     }

     if ( work_part_tag!=tag_part_to_mesh )
     {
         report_msg("Programing Error: Work part is not same as part to mesh.\n");
         return 9999;
     }

     /* =============================
          Open MeshReport log file 
        ============================= */
     UF_UG__BatchMesh_LOG = open_logfile ( tag_part_to_mesh, pzBatchRunParams  );
     if ( UF_UG__BatchMesh_LOG==NULL )
     {
        /* Error in creating log file */
        report_msg("Error opening mesh report log file .");
        write_info_fprintf(true, NULL, "Error opening mesh report log file .\n");
        UF_UG__BatchMesh_LOG = NULL;
     }

     /* Get some system info : Date time user etc... */
     UF_ask_system_info(&zSystemInfo);

     /* Report info */
     write_info_fprintf ( true, UF_UG__BatchMesh_LOG, 
                          "===================================================\n" );
     write_info_fprintf ( true, UF_UG__BatchMesh_LOG, 
                          "               BATCH MESH generation  \n" );
     write_info_fprintf ( true, UF_UG__BatchMesh_LOG, 
                          "===================================================\n" );
     write_info_fprintf ( true, UF_UG__BatchMesh_LOG,"\n\n" );

     /* Dump system info into log file */
     write_info_fprintf ( true, UF_UG__BatchMesh_LOG, "System/Session Info    \n" );
     write_info_fprintf ( true, UF_UG__BatchMesh_LOG, "=================== \n" );
     if ( zSystemInfo.date_buf!=NULL )
         write_info_fprintf ( true, UF_UG__BatchMesh_LOG, "   Date & Time : %s \n", zSystemInfo.date_buf );
     else 
         write_info_fprintf ( true, UF_UG__BatchMesh_LOG, "   Date & Time : ---- \n" );

     if ( zSystemInfo.user_name!=NULL )
         write_info_fprintf ( true, UF_UG__BatchMesh_LOG, "   User Name : %s \n", zSystemInfo.user_name );
     else 
         write_info_fprintf ( true, UF_UG__BatchMesh_LOG, "   User Name : ---- \n" );

     if ( zSystemInfo.node_name!=NULL )
         write_info_fprintf ( true, UF_UG__BatchMesh_LOG, "   Machine Name : %s \n", zSystemInfo.node_name );
     else 
         write_info_fprintf ( true, UF_UG__BatchMesh_LOG, "   Machine Name : ---- \n" );

     if ( zSystemInfo.machine_type!=NULL )
         write_info_fprintf ( true, UF_UG__BatchMesh_LOG, "   Machine Type : %s \n", zSystemInfo.machine_type );
     else 
         write_info_fprintf ( true, UF_UG__BatchMesh_LOG, "   Machine Name : ---- \n" );

     if ( zSystemInfo.os_name!=NULL )
         write_info_fprintf ( true, UF_UG__BatchMesh_LOG, "   OS : %s [Version: %s]\n", 
                              zSystemInfo.os_name, zSystemInfo.os_version );
     else 
         write_info_fprintf ( true, UF_UG__BatchMesh_LOG, "   OS : ---- \n" );
     write_info_fprintf ( true, UF_UG__BatchMesh_LOG, "\n\n" );

     

     /* =================================
           Process parameters supplied 
        ================================= */
     get_mesh_parameters ( pzBatchRunParams, &zMesh_params);
     
     /* Solver name string */
     if ( !strcmp(pzBatchRunParams->Solver_Name, "Structures_P_E" ))
     {
         strcpy (scSolverName, "Structures P.E." );
         strcpy (scAnalysisType, "Structural");
     }
     else if ( !strcmp(pzBatchRunParams->Solver_Name,"MSC_NASTRAN" ))
     {
         strcpy (scSolverName , "MSC NASTRAN" );
         strcpy (scAnalysisType, "Structural");
     }
     else if ( !strcmp(pzBatchRunParams->Solver_Name,"NX_NASTRAN" ))
     {
         strcpy (scSolverName , "NX NASTRAN" );
         strcpy (scAnalysisType, "Structural");
     }
     else if ( !strcmp(pzBatchRunParams->Solver_Name,"ANSYS" ))
     {
         strcpy (scSolverName , "ANSYS" );
         strcpy (scAnalysisType, "Structural");
     }
     else if ( !strcmp(pzBatchRunParams->Solver_Name,"ABAQUS" ))
     {
         strcpy (scSolverName , "ABAQUS"  );
         strcpy (scAnalysisType, "Structural");
     }
     else if ( !strcmp(pzBatchRunParams->Solver_Name,"NX_THERMAL_OR_FLOW" ))
     {
         strcpy (scSolverName , "NX THERMAL / FLOW" );
         strcpy (scAnalysisType, "Thermal");
     }
     else
     {
         /* Default is NX nastran */
         strcpy (scSolverName , "NX NASTRAN" );
         strcpy (scAnalysisType, "Structural");
         write_info_fprintf ( true, UF_UG__BatchMesh_LOG, 
             "No solver language option specified : Default will be used  \n" );
     }
     write_info_fprintf ( true, UF_UG__BatchMesh_LOG, 
             "Solver language set to : %s  \n", scSolverName );
         
                     
     /* Start timer */
     STOP_CLOCK ( UF_UG_BATCH_MESH__start_watch, &zOVERALL_timer, NULL );

     /* =====================================
          Create a FEM on the native UG part.
        ===================================== */
     iRc = create_fem__with_name_from_part_name ( tag_part_to_mesh, scSolverName,
                                                  scAnalysisType, 
                                                  pzBatchRunParams->fOutIdealized,
                                                  pzBatchRunParams,
                                                  &new_fem_tag);
     if ( iRc!=0 || new_fem_tag==NULL_TAG )
     {
         report_msg("Error in creating FEM on part.\n");
         return 9999;
     }
     
     /* Get some material tag (Any one!) */
     iRc = get_a_material ( &material_tag );

     /* Ask all polygon bodies */
     iRc = UF_SF_ask_all_polygon_bodies (  &nCAEBodies, &CAEBodies_p );
     if ( iRc!=0 || nCAEBodies<=0)
     {
         report_msg("Error : 0 Polygon bodies found in FEM.\n");
         write_info_fprintf ( true, UF_UG__BatchMesh_LOG, "Error : CAE geometry creation has problem. \n" );
         return 9999;
     }

     /* ===============
         Report info
        =============== */
     write_info_fprintf ( true, UF_UG__BatchMesh_LOG, " \n\n" );

     /* Info on part */
     build_name_srting ( 0, tag_part_to_mesh,pzBatchRunParams, &CAD_Part_Name);
     write_info_fprintf ( true, UF_UG__BatchMesh_LOG, "Part name: %s (Part Tag = %u) \n",
                          CAD_Part_Name, tag_part_to_mesh, nCAEBodies );
     write_info_fprintf ( true, UF_UG__BatchMesh_LOG, "Total No of Bodies : %d \n\n",
                          nCAEBodies );

     /* Files saved */
     write_info_fprintf(true, UF_UG__BatchMesh_LOG, " \n");
     write_info_fprintf(true, UF_UG__BatchMesh_LOG, "Files To Be Saved \n");
     write_info_fprintf(true, UF_UG__BatchMesh_LOG, "================= \n");
     
     /* Key-word */
     if ( strlen(pzBatchRunParams->run_key_word))
     {
        write_info_fprintf ( true, UF_UG__BatchMesh_LOG, "\tKey-word for file names: %s \n",
                             pzBatchRunParams->run_key_word );
     }
     else
     {
        write_info_fprintf ( true, UF_UG__BatchMesh_LOG, "\tKey-word for file names: None specified\n");
     }

     /* Idealized part option */
     if ( pzBatchRunParams->fOutIdealized==(int)true)
     {
        build_name_srting ( 1, tag_part_to_mesh,pzBatchRunParams, &IDEALIZED_file_Name);
        write_info_fprintf ( true, UF_UG__BatchMesh_LOG, "\tIDEALIZED Part: %s \n",
                             IDEALIZED_file_Name );

        if (IDEALIZED_file_Name!=NULL)
        {
            UF_free(IDEALIZED_file_Name);
            IDEALIZED_file_Name = NULL;
        }
     }
     else
     {
        write_info_fprintf ( true, UF_UG__BatchMesh_LOG, "\tIDEALIZED Part: No idealized part option specified\n");
     }

     /* Info. on fem, sim etc... */
     if ( pzBatchRunParams->fOutputFEM==(int)true)
     {
        build_name_srting ( 2, tag_part_to_mesh,pzBatchRunParams, &FEM_file_Name);
        write_info_fprintf ( true, UF_UG__BatchMesh_LOG, "\tFEM file: %s \n",
                            FEM_file_Name );
        if (FEM_file_Name!=NULL)
        {
            UF_free(FEM_file_Name); 
            FEM_file_Name = NULL;
        }

        build_name_srting ( 4, tag_part_to_mesh,pzBatchRunParams, &SIM_file_Name);
        write_info_fprintf ( true, UF_UG__BatchMesh_LOG, "\tSIM file: %s \n",
                             SIM_file_Name );

        if (SIM_file_Name!=NULL)
        {
            UF_free(SIM_file_Name);
            SIM_file_Name = NULL;
        }
     }
     else
     {
        write_info_fprintf ( true, UF_UG__BatchMesh_LOG, "\tFEM file: No .fem option specified\n");
        write_info_fprintf ( true, UF_UG__BatchMesh_LOG, "\tSIM file: No .sim option specified\n");
     }

     
     /* Solver deck */
     if ( pzBatchRunParams->fOutputDAT==(int)true)
     {

        build_name_srting ( 6, tag_part_to_mesh,pzBatchRunParams, &SOLVER_file_Name);
        write_info_fprintf ( true, UF_UG__BatchMesh_LOG, "\tSOLVER Deck: %s \n",
                             SOLVER_file_Name );

        if (SOLVER_file_Name!=NULL)
        {
            UF_free(SOLVER_file_Name);
            SOLVER_file_Name = NULL;
        }
     }
     else
     {
        write_info_fprintf ( true, UF_UG__BatchMesh_LOG, "\tSOLVER Deck: No solver deck option specified\n");
     }

     /* Mesh log file */
     build_name_srting ( 3, tag_part_to_mesh,pzBatchRunParams, &MESH_LOG_file_Name);
     write_info_fprintf ( true, UF_UG__BatchMesh_LOG, "\tMESH Log file: %s \n",
                          MESH_LOG_file_Name );

     /* Warning on materials */
     write_info_fprintf ( true, UF_UG__BatchMesh_LOG, "\n");
     write_info_fprintf ( true, UF_UG__BatchMesh_LOG, "Warning: Arbitrary material property used. \n");
     write_info_fprintf ( true, UF_UG__BatchMesh_LOG, "         Remember to change it later. \n");
     write_info_fprintf ( true, UF_UG__BatchMesh_LOG, "\n\n");


     /* Loop over all bodies in the part */
     for ( i=0; i<nCAEBodies; i++)
     {

        /* Start processing message */
        write_info_fprintf ( true, UF_UG__BatchMesh_LOG, 
            "------   Start processing body No : %d   ----- \n",
                             i );
        iThis_Body_tag = CAEBodies_p[i];

        /* Assign material to body */
        iRc = UF_SF_link_material ( material_tag , iThis_Body_tag );

        /* Check body valid for tet mesh :
             0=>Solid; 
             1=>Sheet not mid-surface;
             2=>sheet mid surface */
        UF_SF_polygon_body_ask_type ( iThis_Body_tag, &body_type ) ;

        /* Start dump body by body */
        write_info_fprintf ( true, UF_UG__BatchMesh_LOG, "\n\n");
        write_info_fprintf ( true, UF_UG__BatchMesh_LOG, "Body No : %d (Body tag : %u )\n",
                             i+1, iThis_Body_tag);

        if (body_type==0)
        {
            /* Invalid body type : Skip the body */
            write_info_fprintf ( true, UF_UG__BatchMesh_LOG, "\tBody type: Solid Body.\n");
        }
        else if (body_type==1)
        {
            /* Invalid body type : Skip the body */
            write_info_fprintf ( true, UF_UG__BatchMesh_LOG, "\tBody type: Sheet Body [Not Mid-Surface].\n");
        }
        else if (body_type==2)
        {
            /* Invalid body type : Skip the body */
            write_info_fprintf ( true, UF_UG__BatchMesh_LOG, "\tBody type: Sheet Body [Mid-Surface].\n");
        }
        else
        {
            /* Invalid body type : Skip the body */
            write_info_fprintf ( true, UF_UG__BatchMesh_LOG, "\tUnknown/Invalid Body type: Skip meshing this body.\n");
            continue;
        }

        /* === Set up mesh params === */
        tet_mesh_params.midnodes                   = zMesh_params.midnodes;
        tet_mesh_params.element_size               = zMesh_params.element_size;
        tet_mesh_params.midnode_option             = zMesh_params.midnode_option;
        tet_mesh_params.maximum_midnode_jacobian   = zMesh_params.maximum_midnode_jacobian;
        tet_mesh_params.minimum_face_angle         = zMesh_params.minimum_face_angle;
        tet_mesh_params.surf_mesh_size_variation   = zMesh_params.surf_mesh_size_variation;
        tet_mesh_params.tet_mesh_size_variation    = zMesh_params.tet_mesh_size_variation;
        


        /* Set up 2d mesh params */
        if ( !strcmp(zMesh_params.scElemType, "TRI_3" ))
            mesh_2d_params.element_type = UF_SF_UGS_MESHER_tri3;
        else if ( !strcmp(zMesh_params.scElemType, "TRI_6" ))
            mesh_2d_params.element_type = UF_SF_UGS_MESHER_tri6;
        else if ( !strcmp(zMesh_params.scElemType, "QUAD_4" ))
            mesh_2d_params.element_type = UF_SF_UGS_MESHER_quad4;
        else if ( !strcmp(zMesh_params.scElemType, "QUAD_8" ))
            mesh_2d_params.element_type = UF_SF_UGS_MESHER_quad8;
        else
            /* User did not set any mesh type Use parabolic TRI 
               (That will go with tet_10)*/
            mesh_2d_params.element_type = UF_SF_UGS_MESHER_tri6;

                                             
        mesh_2d_params.element_size               = zMesh_params.element_size;                                
        mesh_2d_params.midnode_option             = zMesh_params.midnode_option;
        mesh_2d_params.maximum_midnode_jacobian   = zMesh_params.maximum_midnode_jacobian;         
        mesh_2d_params.minimum_face_angle         = zMesh_params.minimum_face_angle;               
        mesh_2d_params.surf_mesh_size_variation   = zMesh_params.surf_mesh_size_variation;
        /* Some additional opts specific to 2d mesh */
        mesh_2d_params.edge_match_tolerance       = zMesh_params.edge_match_tolerance;            
        mesh_2d_params.format_mesh                = zMesh_params.format_mesh;                        
        mesh_2d_params.attempt_quad_mapping       = zMesh_params.attempt_quad_mapping;     
        mesh_2d_params.quad_only_option           = zMesh_params.quad_only_option;    
        mesh_2d_params.split_poor_quads           = zMesh_params.split_poor_quads;                    
        mesh_2d_params.maximum_quad_warp          = zMesh_params.maximum_quad_warp;     
        mesh_2d_params.mesh_method                = zMesh_params.mesh_method;
        mesh_2d_params.mesh_transition            = zMesh_params.mesh_transition_ON_OFF; 


        /* Abstraction parameters */
        abs_params.small_feature = zMesh_params.small_feature_size; 
        abs_params.edge_angle = 10.0;

        /* Edge merge toggle 0 or 1 */
        if ( zMesh_params.edge_merge_toggle==(int)true )  
        {
            abs_params.edge_merge_toggle = (int)true;
            abs_params.edge_angle = zMesh_params.edge_merge_angle; 
        }
        else
            abs_params.edge_merge_toggle = (int)false;

        if (zMesh_params.process_fillets == (int)true)
        {
            abs_params.fillet_toggle = true;
            abs_params.fillet_type = zMesh_params.fillet_type;
            abs_params.fillet_num_elem = zMesh_params.elem_per_quarter_round;
            abs_params.fillet_min_rad = zMesh_params.min_fillet_radius;
            abs_params.fillet_max_rad = zMesh_params.max_fillet_radius; 
        }
        else 
            abs_params.fillet_toggle = false;
          
        /* Auto element size */
        if ( zMesh_params.fAutoSize == (int)true )  
        {
            UF_SF_get_auto_element_size ( 1, &iThis_Body_tag, &dElemSize );
            tet_mesh_params.element_size = dElemSize;
            mesh_2d_params.element_size = dElemSize;
        }
        
        /* Write out mesh criteria to log file */
        if ( zMesh_params.fAutoSize == (int)true )  
            write_info_fprintf ( true, UF_UG__BatchMesh_LOG, "\tElement Size used : %f (Auto-Size)\n",
                             dElemSize);
        else
            write_info_fprintf ( true, UF_UG__BatchMesh_LOG, "\tElement Size used : %f\n",
                                 mesh_2d_params.element_size);
        
        
        
        /* 1st decide mesh type based on whether set in param file */
        if ( UF_UG__BatchMesh_Is2DMesh(zMesh_params.scElemType))
        {
            /* Mesh type set to 2D mesh */
            strcpy (scMeshType, zMesh_params.scElemType);
            write_info_fprintf ( true, UF_UG__BatchMesh_LOG, "\tMesh Type : %s.\n",
                                 zMesh_params.scElemType );
      
            if ( body_type==0 )
            {
                /* Solid body and mesh type set to 2D (=> invalid opt for 2D mesh)*/
                write_info_fprintf ( true, UF_UG__BatchMesh_LOG, "\tBody Type: Solid; Skipped for 2D meshing\n");
                continue; /* Contiunue to next body in list */
            }
        }
        else if ( UF_UG__BatchMesh_Is3DMesh(zMesh_params.scElemType) )
        {
            /* Mesh type set to 3D mesh */
            strcpy (scMeshType, zMesh_params.scElemType);
            write_info_fprintf ( true, UF_UG__BatchMesh_LOG, "\tMesh Type : %s.\n",
                                 zMesh_params.scElemType );
            if ( body_type!=0 )
            {
                /* Sheet body and mesh type set to 3D (=> invalid opt for sheet)*/
                write_info_fprintf ( true, UF_UG__BatchMesh_LOG, "\tBody Type: Sheet; Not valid for Tet. meshing\n");
                continue; /* Contiunue to next body in list */
            }
        }
        else if ( UF_UG__BatchMesh_MeshTypeNotSet(zMesh_params.scElemType) )
        {
            /* User did not set mesh type required. So by rule
               solid bodies will be meshed tet. sheet bodies Tri. */
            if ( body_type!=0 )
            {
                /* Sheet body and mesh type set to default (i.e., not set) */
                if (mesh_2d_params.element_type==UF_SF_UGS_MESHER_tri3)
                    strcpy (scMeshType, "TRI_3");
                else if (mesh_2d_params.element_type==UF_SF_UGS_MESHER_tri6)
                    strcpy (scMeshType, "TRI_6");
                else if (mesh_2d_params.element_type==UF_SF_UGS_MESHER_quad4 )
                    strcpy (scMeshType, "QUAD_4");
                else if (mesh_2d_params.element_type==UF_SF_UGS_MESHER_quad8 )
                    strcpy (scMeshType, "QUAD_8");

                write_info_fprintf ( true, UF_UG__BatchMesh_LOG, "\tMesh Type : (NOT SET).\n");
                write_info_fprintf ( true, UF_UG__BatchMesh_LOG, "\tBody Type : Sheet (Use deafult %s).\n",
                                     scMeshType);
            }
            else 
            {
                /* Solid and mesh type set to default (i.e., not set)*/
                if (tet_mesh_params.midnodes == (int)true)
                    strcpy(scMeshType, "TET_10");
                else
                    strcpy(scMeshType, "TET_4");

                write_info_fprintf ( true, UF_UG__BatchMesh_LOG, "\tMesh Type : (NOT SET).\n");
                write_info_fprintf ( true, UF_UG__BatchMesh_LOG, "\tBody Type : Solid (Use default %s).\n",
                                     scMeshType);
            }
        } /* if ( UF_UG__BatchMesh_Is2DMesh(zMesh_params.scElemType)) */

        /* Dump in the report abstraction params */
        write_info_fprintf ( true, UF_UG__BatchMesh_LOG, "\n");
        write_info_fprintf ( true, UF_UG__BatchMesh_LOG, "\tAbstraction Parameters:\n");
        write_info_fprintf ( true, UF_UG__BatchMesh_LOG, "\t----------------------\n");

        if (abs_params.edge_merge_toggle==(int)true)
        {
            write_info_fprintf ( true, UF_UG__BatchMesh_LOG, "\t   Merge Edge Toggle :  ON\n");
            write_info_fprintf ( true, UF_UG__BatchMesh_LOG, "\t      Merge Edge Angle :  %f\n", 
                                 abs_params.edge_angle);
        }
        else
            write_info_fprintf ( true, UF_UG__BatchMesh_LOG, "\t   Merge Edge Toggle :  OFF\n");

        /* Samll feature tolerance */
        write_info_fprintf ( true, UF_UG__BatchMesh_LOG, "\t   Small Feature Size = %f %% Element Size\n",
                             abs_params.small_feature );

        if ( abs_params.fillet_toggle==(int)true)
        {
            write_info_fprintf ( true, UF_UG__BatchMesh_LOG, "\t   Fillet Toggle :  ON\n");
            if (abs_params.fillet_type==UF_SF_UGS_ABSTRACTION_FILLET__all)
                write_info_fprintf ( true, UF_UG__BatchMesh_LOG, "\t     Fillet Type = ALL\n");
            else if (abs_params.fillet_type==UF_SF_UGS_ABSTRACTION_FILLET__inside)
                write_info_fprintf ( true, UF_UG__BatchMesh_LOG, "\t     Fillet Type = Inside\n");
            else if (abs_params.fillet_type==UF_SF_UGS_ABSTRACTION_FILLET__outside)
                write_info_fprintf ( true, UF_UG__BatchMesh_LOG, "\t     Fillet Type = Outside \n");
            else
                write_info_fprintf ( true, UF_UG__BatchMesh_LOG, "\t     Fillet Type = ALL\n");
            
            write_info_fprintf ( true, UF_UG__BatchMesh_LOG, "\t     No of Elements/quarter round =  %d\n",
                                 abs_params.fillet_num_elem);
            write_info_fprintf ( true, UF_UG__BatchMesh_LOG, "\t     Min Fillet Radius =  %f\n",
                                 abs_params.fillet_min_rad);
            write_info_fprintf ( true, UF_UG__BatchMesh_LOG, "\t     Max Fillet Radius =  %f\n",
                                 abs_params.fillet_max_rad);
        }
        else
            write_info_fprintf ( true, UF_UG__BatchMesh_LOG, "\t   Fillet Toggle :  OFF\n");

        write_info_fprintf ( true, UF_UG__BatchMesh_LOG, "\t\n");

        

        /* Call tet mesher/2d mesher 
           Logic for meshing: 
           1.  User may have specified mesh type in param file.
               If so, then use that mesh type. If type 2D element skip bodies and
               if type 3D element skip sheet bodies.
           2.  User has not specified any element type in param file.
               Mesh solids with tet and sheets with TRI. */
        if ( UF_UG__BatchMesh_Is3DMesh(scMeshType))
        {
            /* ---- Mesh parameter settings : 3D mesh ---- */

            /* Now call Tet. mesher */
            if ( iThis_Body_tag != NULL_TAG ) 
                /* iRc = UF_SF_create_ugs_tet_mesh( &tet_mesh_params, 1, &iThis_Body_tag, &mesh_tag); */
                iRc = UF_SF_create_ugs_tet_mesh_wt_abstraction_control ( &tet_mesh_params, 
                                                                         &abs_params, 1, 
                                                                         &iThis_Body_tag, 
                                                                         2, &mesh_tag);
            else
                iRc = -1;
        }
        else if ( /*fDo2DMesh==TRUE*/ UF_UG__BatchMesh_Is2DMesh(scMeshType))
        {
            
            /* ---- Mesh parameter settings : 3D mesh ---- */
            if (mesh_2d_params.element_type==UF_SF_UGS_MESHER_quad4 ||
                mesh_2d_params.element_type==UF_SF_UGS_MESHER_quad8 )
            {
                /* Check if quad only is on: Set to 0 since not valid with
                   attempt mapping ON. */
                if (mesh_2d_params.attempt_quad_mapping==(int)true)
                {
                    if (mesh_2d_params.quad_only_option!=0)
                    {
                        write_info_fprintf ( true, UF_UG__BatchMesh_LOG, "\t   Quad only option needs attempt mapping OFF.\n");
                        write_info_fprintf ( true, UF_UG__BatchMesh_LOG, "\t   Resetting Quad only option to 0.\n");
                    }
                    mesh_2d_params.quad_only_option = 0;
                }
            }
            else
            {
                /* Check if quad only is on : set that to 0 because not valid with
                   tri mesh. */
                if (mesh_2d_params.quad_only_option!=0)
                {
                    write_info_fprintf ( true, UF_UG__BatchMesh_LOG, "\t   Quad only option not valid for Tri mesh.\n");
                    write_info_fprintf ( true, UF_UG__BatchMesh_LOG, "\t   Resetting Quad only option to 0.\n");
                }
                if (mesh_2d_params.quad_only_option!=0)
                    mesh_2d_params.quad_only_option = 0;

            }

            /* Now call 2d mesher */
            if ( iThis_Body_tag != NULL_TAG )
                iRc = UF_SF_create_ugs_2d_mesh_wt_abstraction_control (&mesh_2d_params,
                                                                       &abs_params, 1, 
                                                                       &iThis_Body_tag, 
                                                                       &mesh_tag);
            else
                iRc = -1;

        }
        else /* Neither 2D or 3D */
        {
            /* Unsupported mesh type */
            report_msg("Error : Failed to mesh body (Unsupported mesh type).\n");
            write_info_fprintf(true, UF_UG__BatchMesh_LOG, "Mesh generation failed. Unsupported mesh type\n");
        }


        if ( mesh_tag==NULL_TAG )
        {
            iRc = 100;
            report_msg("Error : Failed to mesh body.\n");
            write_info_fprintf(true, UF_UG__BatchMesh_LOG, "Mesh generation failed.\n");
        }  
        else
        {
            /* Set material on the mesh */
            //iRc = UF_SF_link_material ( material_tag , mesh_tag );

            /* ==================================================
                  Run quality criteria and report the results.
               ================================================== */
            write_mesh_quality_report ( scMeshType, mesh_tag, pzBatchRunParams );
        }

        /* De-limiter for next body */
        write_info_fprintf ( true, UF_UG__BatchMesh_LOG, 
            "------   Finished processing body No : %d   ----- \n\n\n",
                             i );

     } /* for ( i=0; i<nCAEBodies; i++) */

     /* ==========================================
          Output Nastran bulk data file if asked 
        ========================================== */
     if ( pzBatchRunParams->fOutputDAT==(int)true )
        export_nastran_file ( tag_part_to_mesh, new_fem_tag, pzBatchRunParams );
    

     /* ===================================
          Overall process time : End timer
        =================================== */
     STOP_CLOCK ( UF_UG_BATCH_MESH__stop_watch, &zOVERALL_timer, 
                  "Time taken (overall process) ");

     /* ==========================
          Close mesh report log
        ========================== */
     close_logfile ( UF_UG__BatchMesh_LOG  );

     /* Free dynamically allocated memory */
     if ( CAEBodies_p!=NULL )
         UF_free(CAEBodies_p);

     if ( CAD_Part_Name!=NULL )
         UF_free (CAD_Part_Name);

     if (FEM_file_Name!=NULL)
         UF_free(FEM_file_Name);
         
     if (SOLVER_file_Name!=NULL)
         UF_free(SOLVER_file_Name);

     if (SIM_file_Name != NULL)
         UF_free (SIM_file_Name);

     if (IDEALIZED_file_Name != NULL)
         UF_free (IDEALIZED_file_Name);

     if (MESH_LOG_file_Name != NULL)
         UF_free (MESH_LOG_file_Name);

     /* Free system info */
     UF_free_system_info(&zSystemInfo); 
 
     /* No error return */
     return iRc;

} /* End of do_Batch_Meshing (void) */

static void STOP_CLOCK ( int          start_end_flag, 
                         UF_timer_p_t pztimer, 
                         char         *scMessage)
{

    
    UF_timer_values_t     zTime_values;
    int                   Hour = 0;
    int                   Min = 0;
    double                dSec = 0.0;

    if ( start_end_flag==UF_UG_BATCH_MESH__start_watch )
    {
        /* Start the clock */
        UF_begin_timer (pztimer);

    }
    else if (start_end_flag==UF_UG_BATCH_MESH__stop_watch )
    {
        /* End clock and print time */
        UF_end_timer ( *pztimer, &zTime_values);

        /* Convert secs into hr:min:sec */
        Time_Sec_to_hr_min_sec(zTime_values.cpu_time, &Hour, &Min, &dSec);
        

        /* Append the messages */
        write_info_fprintf ( true, UF_UG__BatchMesh_LOG, scMessage );
        if ( Hour>0 )
            write_info_fprintf ( true, UF_UG__BatchMesh_LOG, 
                                 ":: %d hrs : %d min : %g sec", Hour, Min, dSec );
        else if ( Min>0 )
            write_info_fprintf ( true, UF_UG__BatchMesh_LOG, 
                                 ":: %d min : %g sec", Min, dSec );
        else
            write_info_fprintf ( true, UF_UG__BatchMesh_LOG, 
                                 "::  %g sec", dSec );


    }

} /* STOP_CLOCK */


static void Time_Sec_to_hr_min_sec(double dTimeSec, int *Hour, int *Min, double *dSec)
{
        double    dMinutes = 0.0, IntMins = 0.0;
        double    dHours = 0.0, IntHrs = 0.0;

        dMinutes = dTimeSec/60;
        dHours   = dMinutes/60;
        dMinutes = modf(dHours, &IntHrs);
        *Hour = (int)IntHrs;

        dMinutes *= 60;
        *dSec = modf(dMinutes, &IntMins);
        *Min = (int)IntMins;

        (*dSec) *= 60;

}
static int get_a_material ( tag_t    *material_tag)
{
    int             iRc = 0, i = 0;

    char            *type_filter = "ISO";      /* Doesn't matter take any 
                                                  isotropic materials = "ISO".
                                                  orthotropic materials = "ORTHO".
                                                  anisotropic materials = "ANISO".
                                                  fluid materials = "FLUID". */
    char            *category_filter = "*";
    char            *name_filter = "*";
    int             material_count = 0; 
    char            **material_librefs = NULL;  /* <OF,len:material_count>
                               An array of characters strings containing the
                               library reference field of each material.
                               Call UF_free_string_array to free the
                               storage allocated within the structure. */
    char            **material_names = NULL;    /* Call UF_free_string_array to free the
                               storage allocated within the structure. */
    char            **material_types = NULL;    /* Call UF_free_string_array to free the
                                        storage allocated within the structure.*/

    /* Init output */
    *material_tag = NULL_TAG;


    /* ========================================================================
        Since no material is specified by the user and we only need to dump a 
        nastran bulk data/ansys/... So:
        - We call list of all elements available 
        - Take the very first one
        - Assign it!
       ======================================================================== */


    /* ==== Ask list of materials ===== */
    iRc = UF_SF_ask_library_materials ( type_filter, category_filter, name_filter,   
                                        &material_count, &material_librefs, &material_names,
                                        &material_types );

    /* Take the very first one */
    iRc = UF_SF_retrieve_library_material ( material_librefs[0], material_tag );

    /* Free allocated memory */
    for ( i=0;i<material_count;i++)
    {
        UF_free(material_librefs[i]);
        UF_free(material_names[i]);
        UF_free(material_types[i]);
    }
    UF_free(material_librefs);
    UF_free(material_names);
    UF_free(material_types);
    
    return iRc;
}

/* ===================================================================
     This function fills in the parameters for batch meshing run.
     Either parameters are read from user supplied param file or
     if file is not supplied default parameters are used.
   =================================================================== */
static void get_mesh_parameters ( UF_UG_BatchMesh_CommandLineOpts_t *pzBatchRunParams, 
                                  UF_UG_BatchMesh_Parms_t           *pzMesh_params)
{

    int                            iRc = 0;

    //UF_SF_ugs_tet_mesh_parms_t     mesh_params;
    paramReader                    meshParamReader;
    
    double                         fDBL_Value = 0.0;
    int                            fUseDefault = true;

    char                           scMeshType[UF_UG_BATCH_MESH__MAX_NAME_LEN]={' '};
    char                           scMidNodeOpt[UF_UG_BATCH_MESH__MAX_NAME_LEN]={' '};
    char                           sc2DMeshMethod[UF_UG_BATCH_MESH__MAX_NAME_LEN]={' '};
    char                           scFilletType[UF_UG_BATCH_MESH__MAX_NAME_LEN]={' '};

    
    /* Initialize the batch mesh parameters */
    UF_UG__BatchMesh_MESHParams(pzMesh_params);

    /* Initialize locals */
    strcpy (scMeshType,"");
    strcpy (scMidNodeOpt,"");
    strcpy (sc2DMeshMethod,"");
    strcpy (scFilletType,"");

    /* Get default parameters */
    /* UF_SF_ugs_tet_mesh_parms_INIT(&mesh_params);*/

    /* Check if user has supplied user defined param file */
    if ( pzBatchRunParams->fParamFile==(int)true)
    {
        /* Read parameters from file : Open the criteria files and 
           parameter files */
        if ( pzBatchRunParams->fParamFile==(int)true)
        {
            iRc = meshParamReader.openFile(pzBatchRunParams->param_file_name, "rt");
            if ( iRc!=0) 
            {
                /* Issue message that we could not open parameter file */
                report_msg("Error : Batch meshing parameter file could not be opened.\n");
                report_msg("        (Bad file name or path) \n");
                report_msg("        File name : "); report_msg(pzBatchRunParams->param_file_name);
                report_msg("\n        Default values will be used.");
                report_msg("\n\n");
                
                fUseDefault = true;
            }
            else
            {
                /* Read parameter file */
                iRc = meshParamReader.read_params();

                /* === mesh parameters === */
                meshParamReader.Get_element_size (&pzMesh_params->element_size);
                if ( pzMesh_params->element_size<=0)
                    pzMesh_params->fAutoSize = true;
                else
                    pzMesh_params->fAutoSize = false;
                meshParamReader.Get_element_type (scMeshType);
                strcpy (pzMesh_params->scElemType, scMeshType);
                if ( (meshParamReader.fStringHasPreFix(scMeshType,"TET_4")) ||
                     (meshParamReader.fStringHasPreFix(scMeshType,"TRI_3")) ||
                     (meshParamReader.fStringHasPreFix(scMeshType,"QUAD_4")) 
                   )
                    pzMesh_params->midnodes = false;
                meshParamReader.Get_midnode_option (scMidNodeOpt);
                if ( meshParamReader.fStringHasPreFix(scMidNodeOpt,"Linear") )
                    pzMesh_params->midnode_option = UF_SF_UGS_MESHER_straight_midnodes;
                else if ( meshParamReader.fStringHasPreFix(scMidNodeOpt, "Curved") )
                    pzMesh_params->midnode_option = UF_SF_UGS_MESHER_curved_midnodes;
                else if ( meshParamReader.fStringHasPreFix(scMidNodeOpt, "Mixed") )
                    pzMesh_params->midnode_option = UF_SF_UGS_MESHER_mixed_midnodes;

                meshParamReader.Get_max_mesh_jacobian (&pzMesh_params->maximum_midnode_jacobian);

                fDBL_Value = -1.0;
                meshParamReader.Get_surf_mesh_size_variation (&fDBL_Value);
                if ( fDBL_Value>=0)
                   pzMesh_params->surf_mesh_size_variation = (int)fDBL_Value;
                fDBL_Value = -1.0;
                meshParamReader.Get_tet_mesh_size_variation (&fDBL_Value);
                if ( fDBL_Value>=0)
                   pzMesh_params->tet_mesh_size_variation = (int)fDBL_Value;

                /* Additional quad/2d mesh related parameters */
                meshParamReader.Get_edge_match_tolerance  (&pzMesh_params->edge_match_tolerance );   
                meshParamReader.Get_attempt_quad_mapping  (&pzMesh_params->attempt_quad_mapping );
                meshParamReader.Get_quad_only_option      (&pzMesh_params->quad_only_option );
                meshParamReader.Get_split_poor_quads      (&pzMesh_params->split_poor_quads );
                meshParamReader.Get_maximum_quad_warp     (&pzMesh_params->maximum_quad_warp );  

                /* Mesh transition toggle */
                meshParamReader.Get_mesh_transition_ON_OFF(&pzMesh_params->mesh_transition_ON_OFF);

                /* Meshing method 2D : "Automatic" or "Paver" */
                meshParamReader.Get_2D_mesh_method(sc2DMeshMethod);
                if ( meshParamReader.fStringHasPreFix(sc2DMeshMethod,"Automatic") )
                    pzMesh_params->mesh_method = 0;
                else if ( meshParamReader.fStringHasPreFix(sc2DMeshMethod,"Paver") )
                    pzMesh_params->mesh_method = 1;
                else /*Default: Automatic */
                    pzMesh_params->mesh_method = 0; 

                /* === Abstraction related parameters === */
                meshParamReader.Get_small_feature_size (&pzMesh_params->small_feature_size); 

                /* === Merge edge params === */
                meshParamReader.Get_merge_edge_ON_OFF_Toggle (&pzMesh_params->edge_merge_toggle);
                if (pzMesh_params->edge_merge_toggle==(int)true)
                    meshParamReader.Get_merge_edge_angle_value (&pzMesh_params->edge_merge_angle);
                else
                    pzMesh_params->edge_merge_angle = 15.0;

                /* === Fillet parameters === */
                if ( meshParamReader.Get_fillet_type(scFilletType))
                {
                    pzMesh_params->process_fillets = true;
                    if ( meshParamReader.fStringHasPreFix(scFilletType,"All") )
                        pzMesh_params->fillet_type = UF_SF_UGS_ABSTRACTION_FILLET__all;
                    else if ( meshParamReader.fStringHasPreFix(scFilletType,"Inside") )
                        pzMesh_params->fillet_type = UF_SF_UGS_ABSTRACTION_FILLET__inside;
                    else if ( meshParamReader.fStringHasPreFix(scFilletType,"Outside") )
                        pzMesh_params->fillet_type = UF_SF_UGS_ABSTRACTION_FILLET__outside;
                    else if ( meshParamReader.fStringHasPreFix(scFilletType,"None") )
                        pzMesh_params->process_fillets = false;

                }
                else
                    pzMesh_params->process_fillets = false;
            
                meshParamReader.Get_min_fillet_radius (&pzMesh_params->min_fillet_radius);
                meshParamReader.Get_max_fillet_radius (&pzMesh_params->max_fillet_radius);
                meshParamReader.Get_elem_per_quarter_round (&pzMesh_params->elem_per_quarter_round);

                meshParamReader.closeFile();
                fUseDefault = false;
            } /* Read the file */
        }
        else
            fUseDefault = true;
        
    }

#if 0
    /* Use default if parameter file not supplied */
    if (fUseDefault)
    {
        /* User did not supply param file; Take default parameters */
        pzMesh_params->midnodes = mesh_params.midnodes;
        pzMesh_params->element_size = mesh_params.element_size;
        pzMesh_params->midnode_option = mesh_params.midnode_option;
        pzMesh_params->maximum_midnode_jacobian = mesh_params.maximum_midnode_jacobian;
        pzMesh_params->minimum_face_angle = mesh_params.minimum_face_angle;
        pzMesh_params->surf_mesh_size_variation = mesh_params.surf_mesh_size_variation;
        pzMesh_params->tet_mesh_size_variation = mesh_params.tet_mesh_size_variation;


    }
#endif

    return;
        
}

/* ===========================================================
     This function runs mesh quality check and writes mesh
     quality report.

     scMeshType                i - TET_4,TET10, TRI_3, TRI_6, QUAD4 
                                   QUAD_8

     mesh_tag                  i - Mesh tag
     pzBatchRunParams          i - Command line options.
                                   (Used to read criteria files)

   =========================================================== */
static int write_mesh_quality_report ( char                              *scMeshType,
                                       tag_t                             mesh_tag,
                                       UF_UG_BatchMesh_CommandLineOpts_t *pzBatchRunParams)
{
    
    int                         iRc = 0;

    int                         iNumNodes = 0, iNumElements = 0;

    const char                  *output_file_with_path = "MY_file.txt";

    UF_SF_ugs_tet_mesh_parms_t  mesh_parms;
    UF_SF_ugs_2d_mesh_parms_t   mesh_2d_parms;
    int                         fUse_2D_params = FALSE;

    UF_SF_THRESHOLD_shape_t     eElemType;
    UF_SF_THRESHOLD_data_t      zThresholdValues;

    /* 3D & 2D specific */
    double                            element_size = 0.0;
    int                               midnodes = (int)false;
    UF_SF_ugs_mesher_midnode_option_t midnode_option;
    double                            maximum_midnode_jacobian = 0.0;        
    double                            minimum_face_angle = 0.0;               
    int                               surf_mesh_size_variation = 0;           
    int                               tet_mesh_size_variation = 0;   

    /* 2D mesh specific additional parameters */
    double                            edge_match_tolerance = 0.0;             
    int                               format_mesh = 0;                         
    int                               attempt_quad_mapping = 0;                
    int                               split_poor_quads = 0;                    
    double                            maximum_quad_warp = 0.0;           
    
    paramReader                       meshCriteriaReader;

    /* Stupid QAZ errors */
    /* Initialize */
    UF_SF_ugs_tet_mesh_parms_INIT ( &mesh_parms );
    UF_SF_ugs_2d_mesh_parms_INIT ( &mesh_2d_parms );

    /* Ask mesh size & other info */
    fUse_2D_params = FALSE;
    if ( UF_UG__BatchMesh_Is3DMesh(scMeshType) )
        UF_SF_ask_ugs_tet_mesh_parms ( mesh_tag,   &mesh_parms );
    else if ( UF_UG__BatchMesh_Is2DMesh(scMeshType) )
    {
        fUse_2D_params = TRUE;
        UF_SF_ask_ugs_2d_mesh_parms ( mesh_tag, &mesh_2d_parms);
    }
    else
    {
        /* Invalid mesh type : Should never come in here. */
        iRc = -1;
        report_msg("Error : Programming error.\n");
        report_msg("        write_mesh_quality_report called with invalid input. ");
        return iRc;
    }


    write_info_fprintf(true, UF_UG__BatchMesh_LOG, " \n");
    write_info_fprintf(true, UF_UG__BatchMesh_LOG, "Mesh Statistics \n");
    write_info_fprintf(true, UF_UG__BatchMesh_LOG, "=============== \n");

    write_info_fprintf(true, UF_UG__BatchMesh_LOG, " \n");              

    /* Element size from actual mesh */
    if ( fUse_2D_params==TRUE )
        element_size = mesh_2d_parms.element_size;
    else
        element_size = mesh_parms.element_size;
    write_info_fprintf(true, UF_UG__BatchMesh_LOG, "   Global element size = %f\n", element_size);

    /* Mid node opt from actual mesh */
    if ( fUse_2D_params==TRUE )
    {
        if ( (!strcmp((scMeshType), "TRI_6")) ||    
             (!strcmp((scMeshType), "QUAD_8"))
           )
           midnodes = (int)true;
        else
            midnodes = (int)false;

        midnode_option = mesh_2d_parms.midnode_option;
    }
    else
    {
        midnodes = mesh_parms.midnodes;
        midnode_option = mesh_parms.midnode_option;
    }
    if (midnodes==(int)true)
    {
        if (midnode_option==UF_SF_UGS_MESHER_straight_midnodes)
            write_info_fprintf(true, UF_UG__BatchMesh_LOG, "   Mid-Node option = LINEAR\n");
        else if (midnode_option==UF_SF_UGS_MESHER_curved_midnodes)
            write_info_fprintf(true, UF_UG__BatchMesh_LOG, "   Mid-Node option = CURVED\n");
        else if (midnode_option==UF_SF_UGS_MESHER_mixed_midnodes)
            write_info_fprintf(true, UF_UG__BatchMesh_LOG, "   Mid-Node option = MIXED (CURVED and/or LINEAR)\n");
    }

    /* Jacobian/Surface mesh variation/tet mesh variation */
    if ( fUse_2D_params==TRUE )
    {
        maximum_midnode_jacobian = mesh_2d_parms.maximum_midnode_jacobian;
        surf_mesh_size_variation = mesh_2d_parms.surf_mesh_size_variation;
    }
    else
    {
        maximum_midnode_jacobian = mesh_parms.maximum_midnode_jacobian;
        surf_mesh_size_variation = mesh_parms.surf_mesh_size_variation;
    }
    write_info_fprintf(true, UF_UG__BatchMesh_LOG, "   Desired Jacobian = %f\n", 
                             maximum_midnode_jacobian);
    write_info_fprintf(true, UF_UG__BatchMesh_LOG, "   Surface mesh size variation = %d\n", 
                             surf_mesh_size_variation);

    /* Tet specific */
    if ( fUse_2D_params==FALSE)
        write_info_fprintf(true, UF_UG__BatchMesh_LOG, "   Tet. mesh size variation = %d\n", 
                             mesh_parms.tet_mesh_size_variation);

    /* Quad/2D mesh specific */
    if ( fUse_2D_params==TRUE )
    {
           
        /* Meshing Method */
        if (mesh_2d_parms.mesh_method==0)
            write_info_fprintf(true, UF_UG__BatchMesh_LOG, "   2D Mesh Generation Method = AUTOMATIC\n");
        else
            write_info_fprintf(true, UF_UG__BatchMesh_LOG, "   2D Mesh Generation Method = PAVING\n");

        write_info_fprintf(true, UF_UG__BatchMesh_LOG, "   Edge match Tol = %f\n", 
                             mesh_2d_parms.edge_match_tolerance);
        //write_info_fprintf(true, UF_UG__BatchMesh_LOG, "   Format mesh = %d\n", 
        //                     mesh_2d_parms.format_mesh);

        /* Mesh transition */
        if (mesh_2d_parms.mesh_transition==(int)true)
            write_info_fprintf(true, UF_UG__BatchMesh_LOG, "   Mesh Transition = ON\n");
        else
            write_info_fprintf(true, UF_UG__BatchMesh_LOG, "   Mesh Transition = OFF\n");


        /* Quad specific */
        if ( (!strcmp((scMeshType), "QUAD_4")) ||    
             (!strcmp((scMeshType), "QUAD_8"))
           )
        {
            /* Quad mapping */
            if ( mesh_2d_parms.attempt_quad_mapping==(int)true )
                write_info_fprintf(true, UF_UG__BatchMesh_LOG, "   Attempt QUAD Mapping = ON\n");
            else
                write_info_fprintf(true, UF_UG__BatchMesh_LOG, "   Attempt QUAD Mapping = OFF\n");

            if ( mesh_2d_parms.quad_only_option==0 )
                write_info_fprintf(true, UF_UG__BatchMesh_LOG, "   QUAD only option = OFF\n");
            else if ( mesh_2d_parms.quad_only_option==1 )
                write_info_fprintf(true, UF_UG__BatchMesh_LOG, "   QUAD only option = ON (Allow 0 Triangles)\n");
            else if ( mesh_2d_parms.quad_only_option==2 )
                write_info_fprintf(true, UF_UG__BatchMesh_LOG, "   QUAD only option = ON (Allow 1 Triangle)\n");
            else 
                write_info_fprintf(true, UF_UG__BatchMesh_LOG, "   QUAD only option = Invalid setting (Ignored)\n");

            /* Splitting quads */
            if ( mesh_2d_parms.split_poor_quads==(int)true )
                write_info_fprintf(true, UF_UG__BatchMesh_LOG, "   Split poor QUADs = ON\n");
            else
                write_info_fprintf(true, UF_UG__BatchMesh_LOG, "   Split poor QUADs = OFF\n");

            /* Quad warp param */
            write_info_fprintf(true, UF_UG__BatchMesh_LOG, "   Max. QUAD warp = %f\n",
                               mesh_2d_parms.maximum_quad_warp);
            
        } /* Quad mesh */

    } /* if ( fUse_2D_params==TRUE ) */
    write_info_fprintf(true, UF_UG__BatchMesh_LOG, "  \n");
                            

    /* Get the number of nodes & elements from the mesh */
    UF_SF_count_nodes( mesh_tag, &iNumNodes );
    UF_SF_count_elements( mesh_tag, &iNumElements );
    if ( iNumNodes > 0 && iNumElements > 0 )
    {
        write_info_fprintf(true, UF_UG__BatchMesh_LOG, "   No of Nodes = %d\n", iNumNodes);
        write_info_fprintf(true, UF_UG__BatchMesh_LOG, "   No of Elements = %d\n", iNumElements);
    }
    
    write_info_fprintf(true, UF_UG__BatchMesh_LOG, " \n\n");
    write_info_fprintf(true, UF_UG__BatchMesh_LOG, "Element Quality Statistics \n");
    write_info_fprintf(true, UF_UG__BatchMesh_LOG, "========================== \n");

    /* Element quality check info */
    if ( pzBatchRunParams->fCriteriaFile==(int)true )
    {
        eElemType = UF_SF_THRESHOLD_shape_tetra4;
        if ( mesh_parms.midnodes==(int)true )
            eElemType = UF_SF_THRESHOLD_shape_tetra10;

        /* Get current shape check threshold value */
        iRc = UF_SF_element_shapes_ask_threshold_values ( eElemType, &zThresholdValues );
        
        /* Read user's criteria settings from criteria file */
        iRc = meshCriteriaReader.openFile(pzBatchRunParams->criteria_file_name, "rt");
        if ( iRc==0) 
        {
            /* Read criteria file */
            iRc = meshCriteriaReader.read_criteria();
            
            if (meshCriteriaReader.Get_Aspect_Ratio (&zThresholdValues.aspect_real_data))
                zThresholdValues.aspect_toggle_data = true;
            else
                zThresholdValues.aspect_toggle_data = false;

           
            if (meshCriteriaReader.Get_Jacobian (&zThresholdValues.jacobian_zero_real_data))
                zThresholdValues.jacobian_zero_toggle_data = true;
            else
                zThresholdValues.jacobian_zero_toggle_data = false;

            if (meshCriteriaReader.Get_Tet_Collapse (&zThresholdValues.tet_collapse_real_data))
                zThresholdValues.tet_collapse_toggle_data = true;
            else
                zThresholdValues.tet_collapse_toggle_data = false;

            /* === 2D mesh related === */
            if (meshCriteriaReader.Get_Warp (&zThresholdValues.warp_real_data))
                zThresholdValues.warp_toggle_data = true;
            else
                zThresholdValues.warp_toggle_data = false;

            if (meshCriteriaReader.Get_Skew (&zThresholdValues.skew_real_data))
                zThresholdValues.skew_toggle_data = true;
            else
                zThresholdValues.skew_toggle_data = false;

            if (meshCriteriaReader.Get_Taper (&zThresholdValues.taper_real_data))
                zThresholdValues.taper_toggle_data = true;
            else
                zThresholdValues.taper_toggle_data = false;

            if (meshCriteriaReader.Get_2D_MinAngle (&zThresholdValues.minimum_angle_real_data))
                zThresholdValues.minmax_angle_toggle_data = true;
            else
                zThresholdValues.minmax_angle_toggle_data = false;

            if (meshCriteriaReader.Get_2D_MaxAngle (&zThresholdValues.maximum_angle_real_data))
                zThresholdValues.minmax_angle_toggle_data = true;
            else
                zThresholdValues.minmax_angle_toggle_data = false;

            if (meshCriteriaReader.Get_Jacobian_Ratio (&zThresholdValues.jacobian_real_data))
                zThresholdValues.jacobian_toggle_data = true;
            else
                zThresholdValues.jacobian_toggle_data = false;


            /* Close criteria file */
            meshCriteriaReader.closeFile();

            /* Re-set shape check thresholds with user's values */
            iRc = UF_SF_element_shapes_set_threshold_values ( eElemType, &zThresholdValues );
            
        } /* Read the file */
        else
        {
            /* Issue error that criteria file could not be opened */

            report_msg("Error : Batch meshing criteria file could not be opened.\n");
            report_msg("        (Bad file name or path) ");
            report_msg("        File name : "); report_msg(pzBatchRunParams->criteria_file_name);
            report_msg("\n        Default values will be used.");
            report_msg("\n\n");
        }

    } /* if ( pzBatchRunParams->fCriteriaFile==true ) */

    /* Run the element shape check */
    iRc = UF_SF_check_model_element_shapes ( 1, &mesh_tag, false, output_file_with_path,
                                            UF_UG__BatchMesh_LOG); 
                                

    write_info_fprintf(true, UF_UG__BatchMesh_LOG, " \n\n");
    write_info_fprintf(true, UF_UG__BatchMesh_LOG, "Mesh Validation Info: \n");
    write_info_fprintf(true, UF_UG__BatchMesh_LOG, "===================== \n");
    iRc = validate_meshes (1,&mesh_tag,UF_UG__BatchMesh_LOG);

    return iRc;
} /* End of write_mesh_quality_report */

/* ========================================================================
      This function creates a FEM.  Most of the data such as FEM name 
      etc is derived from part name.

          cad_part_tag          i -  CAD part tag

          solver_name           i -  The name of the solver.
                                     Available solvers are:
                                        "NX NASTRAN",
                                        "MSC NASTRAN",
                                        "ANSYS",
                                        "ABAQUS",
                                        "NX THERMAL / FLOW"
                                        "NX NASTRAN DESIGN"   

          analysis_type_name    i -  The name of the analysis type.
                                     Available analysis types for solver types are:

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
                                            "Thermal"       

          new_fem_tag           o - New fem tag

      Return 
          0  => No error
          !0 => Error
         
 */
static int create_fem__with_name_from_part_name ( tag_t         cad_part_tag,
                                                  /* char          *cad_part_name, */
                                                  const char*   solver_name,
                                                  const char*   analysis_type_name,
                                                  int           fCreateIdealizedPart,
                                           UF_UG_BatchMesh_CommandLineOpts_t *pzBatchRunParams,
                                                  tag_t         *new_fem_tag)
{
    int             iRc = 0;
    int             mem_error = 0;
    
    
    char            *fem_name = NULL;                         
    char            *idealized_part_name = NULL;                          
                                               
    logical         use_all_bodies_flag = 0;
    int             num_bodies = 0;    
    tag_t           *body_tags = NULL;
                                
    int             num_desc_lines = 1;
    char            *description = NULL;

    char            scPartName[UF_UG_BATCH_MESH__MAX_NAME_LEN];
    char            scPartDirectoryPath[UF_UG_BATCH_MESH__MAX_NAME_LEN];
    char            *scIdealizedPart_Directory = NULL;
    char            *scIdealizedPart_Directory_Tmp = NULL;
    int             iStrLen = 0;
   
    char            scCurrentDirectory[UF_UG_BATCH_MESH__MAX_NAME_LEN];

    /* Init string variables */
    strcpy (scPartName, "");
    strcpy (scPartDirectoryPath, "");
    strcpy (scCurrentDirectory, "");

    /* Build name string for idealized part */
    build_name_srting ( 1, cad_part_tag, pzBatchRunParams, &idealized_part_name);

    /* ==============================================
          Make sure idealized prt does not exist.
          If exists delete the file.
       ============================================== */
    iRc = uc4560 (idealized_part_name, 0 );
    if ( iRc ==0 )
    {
        /* ========================================
           File exists IN CURRENT WORKING DIRECTORY
           So delete it from the system 
           ======================================== */
        iRc = uc4561 (idealized_part_name, 0 );
        if ( iRc!=0 )
        {
            /* Could not delete the file : Error out */
            report_msg("Error : Idealized part already exists\n");
            report_msg("        File name : ");report_msg(idealized_part_name);
            report_msg("\n        Could not delete existing file.\n");
            return -9999;
        }
    }
    else
    {
       /* ==============================================
          Make attempt to locate it in directory of part 
          and then delete it.
          ============================================== */

       /* Separate directory path from part name*/
       iRc = uc4576(pzBatchRunParams->part_file_name,2, scPartDirectoryPath, 
                    scPartName); 

       if (strlen(scPartDirectoryPath))
       {
 
           /* uc4565 : Get current directory */
           uc4565(1, scCurrentDirectory);

           iStrLen = (int)(strlen(scPartDirectoryPath) + strlen(idealized_part_name)+
                     strlen(scCurrentDirectory) +20);
           scIdealizedPart_Directory = (char* )UF_allocate_memory(iStrLen*sizeof(char), 
                                               &mem_error);
           scIdealizedPart_Directory_Tmp = (char* )UF_allocate_memory(iStrLen*sizeof(char), 
                                               &mem_error);

           /* Idealized part is saved along with part. So in that
              directory look for idealized part */
           strcpy ( scIdealizedPart_Directory_Tmp, scPartDirectoryPath);

           /* uc4575 : Build path & file name : Append directory path & file name */
           //iRc = uc4575( scCurrentDirectory, 0, scPartDirectoryPath, 
           //               scIdealizedPart_Directory_Tmp);
           iRc = uc4575( scIdealizedPart_Directory_Tmp, 2, idealized_part_name, 
                         scIdealizedPart_Directory);


           /* uc4560 : Checks whether the specified file of the given type exists */
           iRc = uc4560 (scIdealizedPart_Directory, 0 );
           if ( iRc ==0 )
           {
               /* uc4561  Remove a given file from the file system. */
               iRc = uc4561 (scIdealizedPart_Directory, 0 );
               if ( iRc!=0 )
               {
                   /* Could not delete the file : Error out */
                   report_msg("Error : Idealized part already exists\n");
                   report_msg("        File name : ");report_msg(idealized_part_name);
                   report_msg("\n        Could not delete existing file.\n");
                   if ( scIdealizedPart_Directory!=NULL )
                   {
                        UF_free (scIdealizedPart_Directory);
                        scIdealizedPart_Directory = NULL;
                   }
                   if ( scIdealizedPart_Directory_Tmp!=NULL)
                   {
                        UF_free (scIdealizedPart_Directory_Tmp);
                        scIdealizedPart_Directory_Tmp = NULL;
                   }
                    return -9999;
               }
           }
           if ( scIdealizedPart_Directory!=NULL )
           {
               UF_free (scIdealizedPart_Directory);
               scIdealizedPart_Directory = NULL;
           }
           if ( scIdealizedPart_Directory_Tmp!=NULL)
           {
               UF_free (scIdealizedPart_Directory_Tmp);
               scIdealizedPart_Directory_Tmp = NULL;
           }
       } /* if (!strlen(scPartDirectoryPath)) */

    } /* if ( iRc ==0 ) for uc4560 call */
       
    
    /* Build name string for fem file */
    build_name_srting ( 2, cad_part_tag, pzBatchRunParams, &fem_name);
    /* ==============================================
          Make sure fem file does not exist in OS.
          If exists delete the file.
       ============================================== */
    iRc = uc4560 (fem_name, 0 );
    if ( iRc ==0 )
    {
        /* File exists : So delete it from the system */
        iRc = uc4561 (fem_name, 0 );
        if ( iRc!=0 )
        {
            /* Could not delete the file : Error out */
            report_msg("Error : FEM file already exists\n");
            report_msg("        File name : ");report_msg(fem_name);
            report_msg("\n        Could not delete existing file.\n");
            return -9999;
        }
    }
    num_desc_lines = 1;
    description = (char* )UF_allocate_memory(10*sizeof(char), &mem_error);
    if (mem_error != 0)
    {
        iRc = mem_error;
        return iRc;
    }
    strcpy( description, " " ); 

    /* Create FEM */
    use_all_bodies_flag = true;
    if ( fCreateIdealizedPart == false )
    {
         iRc = UF_SF_create_fem ( fem_name, cad_part_tag, NULL, use_all_bodies_flag,
                       num_bodies, body_tags, 
                       solver_name, analysis_type_name, num_desc_lines, 
                       (const char**)&description, new_fem_tag );
    }
    else
    {
        iRc = UF_SF_create_fem ( fem_name, cad_part_tag, idealized_part_name, use_all_bodies_flag,
                        num_bodies, body_tags, 
                        solver_name, analysis_type_name, num_desc_lines, 
                        (const char**)&description, new_fem_tag );
    }
    if ( iRc!=0 || *new_fem_tag==NULL_TAG)
        iRc = -9999;

    /* End : Free up dynamic allocations */
    if ( fem_name!=NULL )
    {
        UF_free(fem_name);
    }

    if ( idealized_part_name!=NULL )
    {
        UF_free(idealized_part_name);
    }

    if ( scIdealizedPart_Directory!=NULL )
    {
        UF_free (scIdealizedPart_Directory);
        scIdealizedPart_Directory = NULL;
    }

    if ( scIdealizedPart_Directory_Tmp!=NULL)
    {
        UF_free (scIdealizedPart_Directory_Tmp);
        scIdealizedPart_Directory_Tmp = NULL;
    }

    if ( description!=NULL )
        UF_free(description);

    return iRc;

} /* create_fem__with_name_from_part_name */


/* 
  ========================================================================
      This function creates a SIM.  Most of the data such as FEM name 
      etc is derived from part name.

          cad_part_tag          i -  CAD part tag

          
          new_sim_tag           o - New fem tag

      Return 
          0  => No error
          !0 => Error
   ========================================================================
 */
static int create_sim__with_name_from_part_name ( tag_t         cad_part_tag,
                                                  tag_t         fem_tag, 
                                                  UF_UG_BatchMesh_CommandLineOpts_t *pzBatchRunParams,
                                                  tag_t         *new_sim_tag)
{
    int             iRc = 0;
    int             mem_error = 0;
    
    char            *sim_name = NULL;        
                                
    int             num_desc_lines = 1;
    char            *description = NULL;
   
    
    /* Build name string for sim file */
    build_name_srting ( 4, cad_part_tag, pzBatchRunParams, &sim_name);

    /* ==============================================
          Make sure sim file does not exist in OS.
          If exists delete the file.
       ============================================== */
    iRc = uc4560 (sim_name, 0 );
    if ( iRc ==0 )
    {
        /* File exists : So delete it from the system */
        iRc = uc4561 (sim_name, 0 );
        if ( iRc!=0 )
        {
            /* Could not delete the file : Error out */
            report_msg("Error : SIM file already exists\n");
            report_msg("        File name : ");report_msg(sim_name);
            report_msg("\n        Could not delete existing file.\n");
            return -9999;
        }
    }
    num_desc_lines = 1;
    description = (char* )UF_allocate_memory(10*sizeof(char), &mem_error);
    if (mem_error != 0)
    {
        iRc = mem_error;
        return iRc;
    }
    strcpy( description, " " ); 

    /* Create SIM */
    iRc = UF_SF_create_simulation (sim_name, fem_tag,  
                                   num_desc_lines, (const char**)&description,       
                                   new_sim_tag  );
    if ( iRc!=0 || *new_sim_tag==NULL_TAG)
        iRc = -9999;



    /* End : Free up dynamic allocations */
    if ( sim_name!=NULL )
        UF_free(sim_name);

    if ( description!=NULL )
        UF_free(description);

    return iRc;

} /* create_sim__with_name_from_part_name */


/* ==========================
      Run mesh validation.
   ========================== */
static int validate_meshes
(
    int      num_meshes,
    tag_p_t  meshes_p,
    FILE     *details_fp
)
{
    int                           return_status    = 0,
                                  num_total_errors = 0;
    UF_SF_mesh_error_container_t  error_container;

    UF_SF_init_mshvld_error_container( &error_container );


    return_status = UF_SF_validate_meshes( meshes_p,
                                           num_meshes,
                                           UF_SF_VALIDATE_MESH_ALL,
                                           &error_container );

    if ( return_status )
    {
        write_info_fprintf(true, UF_UG__BatchMesh_LOG, "   Errors found while validating mesh\n\n");
        
        return_status = 1;
        goto exit_mshvld;
    }
    else
    {
        write_info_fprintf(true, UF_UG__BatchMesh_LOG, "   Mesh Validation successful.\n\n");
    }

    num_total_errors =
    error_container.mesh_asso_error_list.num_mesh_errors +
    error_container.elem_asso_error_list.num_mesh_errors +
    error_container.node_asso_error_list.num_mesh_errors +
    error_container.mesh_recipe_error_list.num_mesh_errors +
    error_container.geom_constraint_error_list.num_mesh_errors +
    error_container.user_attribute_error_list.num_mesh_errors;

    if ( num_total_errors > 0 )
    {
        write_info_fprintf(true, UF_UG__BatchMesh_LOG, "   %d Errors found while validating mesh\n", 
                           num_total_errors);
        
        return_status = 1;
        goto exit_mshvld;
    }


    exit_mshvld:

    UF_SF_clean_mshvld_error_container( &error_container );

    return return_status;
}


/* ================================================
      Open/Close file to write out mesh report.
 * ================================================ */
static FILE *open_logfile (tag_t      cad_part_tag, 
                           UF_UG_BatchMesh_CommandLineOpts_t *pzBatchRunParams)
{
    FILE   *fp = NULL;
    char   *MeshReport_LOG_name = NULL;

    /* Build name string from cad part name */
    build_name_srting ( 3, cad_part_tag, pzBatchRunParams, &MeshReport_LOG_name);

    /* Create a file by that name; over-write any existing file */
    if ( MeshReport_LOG_name!=NULL )
    {
        fp = fopen (MeshReport_LOG_name, "wt");
        if (fp==NULL)
        {
            report_msg("Error opening mesh report log file ");
            report_msg(MeshReport_LOG_name);
            report_msg("\n \n");
        }
    }

    if ( MeshReport_LOG_name!=NULL )
        UF_free(MeshReport_LOG_name);
    return fp;
}

static void close_logfile (FILE   *fp  )
{
    if (fp!=NULL)
        fclose (fp);
   
    return;
}

/* ======================================================================
      This function builds name string from CAD part name. Options
      are to build name of fem file, idealized part file and mesh
      log file.

      iNameOpt         i - 0 => CAD part name
                           1 => Idealized part file name
                           2 => FEM file name
                           3 => Mesh info LOG file
                           4 => Sim file name
                           5 => Solution name
                           6 => Nastran blk data name 

      cad_part_tag     i - Tag of the CAD part

    pzBatchRunParams   i - Use key words, extensions etc.

      NameString       o - Output name string
  ======================================================================= */
static int build_name_srting ( int       iNameOpt,
                               tag_t     cad_part_tag,
                               UF_UG_BatchMesh_CommandLineOpts_t *pzBatchRunParams, 
                               char      **NameString)
{
    int             iRc = 0;
    int             mem_error = 0;

    char            cad_part_name[UF_UG_BATCH_MESH__MAX_NAME_LEN] = {""};
    char            cad_part_full_path[UF_UG_BATCH_MESH__MAX_NAME_LEN] = {""};
    const char      *Fem_Name_Prefix="__FEM";
    const char      *Ideal_Name_Prefix="__IDEALIZED";
    const char      *Sim_Name_Prefix="__SIM";
    const char      *MeshReport_Suffix = "__MeshReport.LOG";
    char            NASTRAN_prefix[UF_UG_BATCH_MESH__MAX_NAME_LEN]= {' '};
    const char      *SOLUTION_prefix = "SOLVER_DECK";

    char            RunKeyWord[UF_UG_BATCH_MESH__MAX_NAME_LEN] = {' '};

    int             iExpectedStrLen = 0;

    char            *fem_name = NULL;                         
    char            *idealized_part_name = NULL;    
    char            *sim_name = NULL;   
    char            *solver_name = NULL;

    char            scDeckExtn[UF_UG_BATCH_MESH__MAX_NAME_LEN] = {' '};

    
    /* Initialize */
    strcpy( RunKeyWord, "");
    strcpy( NASTRAN_prefix, "");
    strcpy( scDeckExtn, "");

    /* Copy keyword */
    strcpy (RunKeyWord, pzBatchRunParams->run_key_word);
    
    /* Query part name */
    iRc = UF_PART_ask_part_name( cad_part_tag, cad_part_full_path);
    iRc = uc4574 ( cad_part_full_path, 2, cad_part_name); /* Arguement 2 => file type is .prt file */

    if ( iNameOpt==0 )
    {
        /* ====================
              CAD PART NAME 
           ==================== */
        iExpectedStrLen = ((int)strlen(cad_part_name))+20;
        *NameString = (char*)UF_allocate_memory((iExpectedStrLen)*sizeof(char), &mem_error);
        if (mem_error != 0)
        {
            iRc = mem_error;
            return iRc;
        }
        strcpy( *NameString, cad_part_name);
    }
    else if ( iNameOpt==1 )
    {
        /* ===========================
              IDEALIZED PART NAME 
           ===========================  */
        /* Build idealized part name : "<Part_name>__IDEALIZED__<key word>" */
        iExpectedStrLen = (int)(strlen(cad_part_name)+strlen(Ideal_Name_Prefix)+ 
                                strlen(RunKeyWord)+20);
        idealized_part_name = (char*)UF_allocate_memory((iExpectedStrLen)*sizeof(char), &mem_error);
        if (mem_error != 0)
        {
            iRc = mem_error;
            return iRc;
        }
        strcpy( idealized_part_name, cad_part_name );
        strcat( idealized_part_name, Ideal_Name_Prefix );
        if ( strcmp(RunKeyWord,"") )
        {
            strcat( idealized_part_name, "__");
            strcat( idealized_part_name, RunKeyWord );
        }
        strcat( idealized_part_name, ".prt" );

         /* Output string */
        *NameString = (char*)UF_allocate_memory((iExpectedStrLen)*sizeof(char), &mem_error);
        if (mem_error != 0)
        {
            iRc = mem_error;
            return iRc;
        }
        strcpy( *NameString, idealized_part_name);
    }
    else if ( iNameOpt==2 || iNameOpt==3 )
    {

        /* Build FEM name : "<Part_name>__FEM__<keyword>.fem";
                 MeshReport Log : "<Part_name>__FEM__<keyword>__MeshReport.LOG" */
        iExpectedStrLen = (int)(strlen(cad_part_name)+strlen(Fem_Name_Prefix)+strlen(MeshReport_Suffix)
                          + strlen(RunKeyWord)+20);
        fem_name = (char*)UF_allocate_memory((iExpectedStrLen)*sizeof(char), &mem_error);
        if (mem_error != 0)
        {
            iRc = mem_error;
            return iRc;
        }
        strcpy( fem_name, cad_part_name  );
        strcat( fem_name, Fem_Name_Prefix );
        if ( strcmp(RunKeyWord,"") )
        {
            strcat( fem_name, "__");
            strcat( fem_name, RunKeyWord );
        }
        if ( iNameOpt == 2)
            strcat( fem_name, ".fem" );
        else if (iNameOpt == 3)
            strcat( fem_name, MeshReport_Suffix );

        /* Output string */
        *NameString = (char*)UF_allocate_memory((iExpectedStrLen)*sizeof(char), &mem_error);
        if (mem_error != 0)
        {
            iRc = mem_error;
            return iRc;
        }
        strcpy( *NameString, fem_name);
    }
    else if (  iNameOpt==4 )
    {
        /* Build Sim name : "<Part_name>__SIM__<keyword>.sim"; */
        iExpectedStrLen = (int)(strlen(cad_part_name)+strlen(Sim_Name_Prefix)+ 
                                strlen(RunKeyWord)+ 20);
        sim_name = (char*)UF_allocate_memory((iExpectedStrLen)*sizeof(char), &mem_error);
        if (mem_error != 0)
        {
            iRc = mem_error;
            return iRc;
        }
        strcpy( sim_name, cad_part_name  );
        strcat( sim_name, Sim_Name_Prefix );
        if ( strcmp(RunKeyWord,"") )
        {
            strcat( sim_name, "__");
            strcat( sim_name, RunKeyWord );
        }
        strcat( sim_name, ".sim" );
        

        /* Output string */
        *NameString = (char*)UF_allocate_memory((iExpectedStrLen)*sizeof(char), &mem_error);
        if (mem_error != 0)
        {
            iRc = mem_error;
            return iRc;
        }
        strcpy( *NameString, sim_name);
    }
    else if (  iNameOpt==5 || iNameOpt==6 )
    {
        if ( iNameOpt==6 )
        {
            /* Add extension to the name */
            if ( !strlen(pzBatchRunParams->dat_file_extn) )
            {
                /* Get extension for what ever solver user has set while runing batch
                meshing */
                UF_UG__BatchMesh_GetDefaultSolverDeckFileExtn(pzBatchRunParams->Solver_Name, \
                                                            scDeckExtn);
                
            }
            else
            {
                /* User has specified extension; use it */
                strcat( scDeckExtn, ".");
                strcat( scDeckExtn, pzBatchRunParams->dat_file_extn);
            }
        }
        else
            strcpy (scDeckExtn,"");

        /* Build nastran bulk data name : "<Part_name>__<Solver name>__<Keyword>"; */
        UF_UG__BatchMesh_GetSolverDeckName(pzBatchRunParams->Solver_Name, NASTRAN_prefix);
        iExpectedStrLen = (int)(strlen(cad_part_name)+strlen(NASTRAN_prefix)+ strlen(RunKeyWord) +
                          strlen(scDeckExtn)+ 20);
        solver_name = (char*)UF_allocate_memory((iExpectedStrLen)*sizeof(char), &mem_error);
        if (mem_error != 0)
        {
            iRc = mem_error;
            return iRc;
        }

        if ( iNameOpt==6 )
        {
            
            strcpy( solver_name, cad_part_name  );
            strcat( solver_name, "__" );
            strcat( solver_name, NASTRAN_prefix );
            if ( strcmp(RunKeyWord,"") )
            {
                strcat( solver_name, "__");
                strcat( solver_name, RunKeyWord );
            }
            if ( iNameOpt==6)
                strcat( solver_name, scDeckExtn);
               
        }
        else
        {
            /* Name option is 5 solver name */
            //////
            ///  A Note: The UF routine that creates solution 
            ///  automatically appends simulation name to the
            ///  solution name.  That string becomes very long
            ///  So for solution name we keep the string small
            strcpy( solver_name, SOLUTION_prefix);
        }
            

        /* Output string */
        *NameString = (char*)UF_allocate_memory((iExpectedStrLen)*sizeof(char), &mem_error);
        if (mem_error != 0)
        {
            iRc = mem_error;
            return iRc;
        }
        strcpy( *NameString, solver_name);

    }



    /* End : Free up dynamic allocations */
    if ( fem_name!=NULL )
        UF_free(fem_name);

    if ( sim_name!=NULL )
        UF_free (sim_name);

    if (solver_name!=NULL )
        UF_free (solver_name);

    if ( idealized_part_name!=NULL )
        UF_free(idealized_part_name);
   
    
    return iRc;
} /* build_name_srting */

/* ======================================================================
   Parse command line arguements to extract relevant parameters.

    argc, argv        i - Command line arguements
    pzBatchRunParams  o - Parameters from command line arguement parsing
        
   ====================================================================== */
 
static void do_command_line_arg_parsing(char argc, 
                                        char *argv[],
                                        UF_UG_BatchMesh_CommandLineOpts_t *pzBatchRunParams,
                                        int  *pfDisplayCommandHelp)
{

    char     command_help[MAX_FSPEC_SIZE+1]={""},      /* Command help */    
             param_file[MAX_FSPEC_SIZE+1]={""},        /* Parameter file name */
             criteria_file[MAX_FSPEC_SIZE+1]={""},     /* Criteria file name */
             part_file[MAX_FSPEC_SIZE+1]={""},         /* Part filename storing  */

             solver_name[MAX_FSPEC_SIZE+1]={""},       /* Solver name */
             out_no_idealized[MAX_FSPEC_SIZE+1]={""},  /* Output opt: no idealized */
             out_fem[MAX_FSPEC_SIZE+1]={""},           /* Output opt: FEM file */
             out_jt[MAX_FSPEC_SIZE+1]={""},            /*             JT file */
             out_nastran[MAX_FSPEC_SIZE+1]={""},       /*             NASTRAN file */           
             run_key_word[MAX_FSPEC_SIZE+1]={""};      /* Run key word */
            
             
    /* Initi output */
    *pfDisplayCommandHelp = false;

    /* Initialize output structure */
    UF_UG__BatchMesh_INITBatchParams(pzBatchRunParams);

    /* Parse command line arguements */
    UF_CALL(uc4624( 0 , argc , argv  ));

    /* Get the key-word for the run */
    if (uc4620( UF_UG_BATCH_MESH__PARM_key_word , run_key_word)<=0)
    {
        strcpy(run_key_word,"");
        strcpy(pzBatchRunParams->run_key_word, "");
    }
    else
    {
        strcpy(pzBatchRunParams->run_key_word, run_key_word);
    }

    /* Part file name */
    if (uc4620( UF_UG_BATCH_MESH__PARM_input_part , part_file)<=0)
    {
        pzBatchRunParams->fPartFile = false;
        strcpy(part_file,"");
    }
    else
    {
        pzBatchRunParams->fPartFile = true;
        strcpy(pzBatchRunParams->part_file_name, part_file);
    }

    /* Parameter file name */
    if (uc4620( UF_UG_BATCH_MESH__PARM_param_file , param_file)<=0)
    {
        pzBatchRunParams->fParamFile = false;
        strcpy(param_file,"");
    }
    else
    {
        pzBatchRunParams->fParamFile = true;
        strcpy(pzBatchRunParams->param_file_name, param_file);
        
    }

    /* Criteria file name */
    if (uc4620( UF_UG_BATCH_MESH__PARM_criteria_file, criteria_file)<=0)
    {
        pzBatchRunParams->fCriteriaFile = false;
        strcpy(criteria_file,"");
    }
    else
    {
        pzBatchRunParams->fCriteriaFile = true;
        strcpy(pzBatchRunParams->criteria_file_name, criteria_file);
    }

    /* Solver name */
    if (uc4620( UF_UG_BATCH_MESH__PARM_solver_name , solver_name)<=0)
    {
        /* Default solver */
        strcpy(pzBatchRunParams->Solver_Name, "--Not_Specified--");
    }
    else
    {
        strcpy(pzBatchRunParams->Solver_Name, solver_name);
    }

    /* Output option : Whether to create idealized part */
    if (uc4620( UF_UG_BATCH_MESH__PARM_idealize_output, out_no_idealized)<=0)
        pzBatchRunParams->fOutIdealized = true;
    else
        pzBatchRunParams->fOutIdealized = false;

    /* Output option : Whether to save fem file */
    if (uc4620( UF_UG_BATCH_MESH__PARM_fem_output, out_fem)<=0)
        pzBatchRunParams->fOutputFEM = false;
    else
        pzBatchRunParams->fOutputFEM = true;

    /* Output option : Whether to save jt file or not */
    if (uc4620( UF_UG_BATCH_MESH__PARM_jt_output, out_jt)<=0)
        pzBatchRunParams->fOutputJT = false;
    else
        pzBatchRunParams->fOutputJT = true;
   
    /* Output option : Whether to save nastran bulk data or not */
    if (uc4620( UF_UG_BATCH_MESH__PARM_nastran_output, out_nastran)<=0)
    {
        pzBatchRunParams->fOutputDAT = false;
        strcpy(pzBatchRunParams->dat_file_extn, "");
    }
    else
    {
        pzBatchRunParams->fOutputDAT = true;
        strcpy(pzBatchRunParams->dat_file_extn, out_nastran);
    }

    /* Check if help dump is desired */
    if ( (uc4620(UF_UG_BATCH_MESH__PARM_help_str1, command_help)>0) ||      
         (uc4620(UF_UG_BATCH_MESH__PARM_help_str2, command_help)>0) ||
         (uc4620(UF_UG_BATCH_MESH__PARM_help_str3, command_help)>0) )
    {
        *pfDisplayCommandHelp = true;
    }


    return;
}

/* ==================================
     Convert string to lower case
   ==================================  */
static void upper_to_lower_case ( char *scString)
{
    int i = 0, ichar = 0, nchar = 0;

    nchar = (int)strlen (scString);

    for (i=0;i<nchar;i++)
    {
        ichar = scString[i];
        scString[i] = tolower(ichar);
    }
    return;
}

/* =========================================================================
   Writes formatted infor to file or console.
        
        fToConsole          i - true => Write formatted string to console
                                false   otherwise
        fp                  i - File to write the formatted string to
                                NULL => not write to file
        format_string       i - Format string
        ...                 i - data to print.
 * ========================================================================= */
static void write_info_fprintf(bool        fToConsole, 
                               FILE       *fp,             /* I   : File to print*/
                               const char *format_string,  /* I   */
                               ...                         /* I   */
                              )
{
    va_list variable_list;
    
    
    if ( fToConsole==(int)true)
    {
#if UF_UG_BATCH_MESH__SCREEN_DUMP_ON
        /* ====== #define flag ====== */
        va_start(variable_list, format_string);
        vprintf(format_string, variable_list);
        va_end(variable_list);
#endif
    }
    if ( fp!=NULL)
    {
        va_start(variable_list, format_string);
        vfprintf(fp, format_string, variable_list);
        va_end(variable_list);
    }

    if (fp!=NULL)
        fflush(fp);
}

/* Display the help on command to user */
static void display_command_help( char *scHelpText[] )
{
    int   iLinesPrinted = 0;
    int   nMaxLines = 1000;
    while ( !(!strcmp(scHelpText[iLinesPrinted], "END_HELP")) )
    {
        printf ("   %s \n", scHelpText[iLinesPrinted]);

        /* Sanity check */
        iLinesPrinted++;
        if (iLinesPrinted>nMaxLines)
            break;
    }

    printf ("  \n\n");
    return;
}

