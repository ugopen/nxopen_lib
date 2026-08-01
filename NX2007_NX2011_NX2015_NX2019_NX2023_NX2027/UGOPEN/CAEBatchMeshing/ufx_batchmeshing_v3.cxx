/*****************************************************************************
**
**                 ========================================
*                        B A T C H    M E S H I N G
*                        --------------------------
*                  ========================================
*
*                 ------------------------------------------
**                    Main File : ufx_batchmeshing_v3.cxx
**                     May,01 2018 : Batch Mesher Version 3.0
*                 ------------------------------------------
*
**
** Description:
**
*
General
=======
This program generates meshes in batch mode. This version of batchmesher takes
advantage of recent developments in Selection Recipe. The input template
must have all the required set of definitions(Selection Recipe, Mesh, Mesh Controls etc..)
pre defined.


Usage:  From command line :
=========================

ufx_batchmeshing_v3  -?  -h or -H
-part=<Partname> -t=<Template file name>
-no_idealize
-fem -dat=<extension> -jt -key_word=<some keyword string>

-?  -h or -H                    : Help on usage.


-part=<Partname>                : Part file path.
Error if part does not exist or error in
opening. Must be valid ug part file.
The part name string is also used to build
name strings for .fem, .dat, idealized part
and .LOG file.
[please see "More on naming convention"
below]

-t=<Template file name>         : Template file name(specified format)",
the format of extension for",
template (.fem).",
User defined template can be placed:",
1. In any folder of user's choice but",
template option must be accompanied",
by the whole path to this file.",
e.g:-t=D:/workdir/partfolder/partname.prt.",
2. In any local template folder
($UGII_TEMPLATE_DIR) and",
can be added to a new or existing ",
(.pax) file",
3.In any installation template folder",
($UGII_BASE_DIR/ugii/templates) and",
can be added to a new or ",
existing (.pax) file",
If not specified, program uses defaults.",
For example format, see top of the file",
ufx_batchmeshing_v3.cxx  OR look in the DIR",
($UGII_BASE_DIR/ugopen/CAEBatchMeshing)",

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

-jt                             : Tells the program to dump Jt file from mesh.
(If not specified, no jt file will be saved)


-key_word=<some keyword string> : This keyword is optional and is embedded into
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
JT from mesh file name: "<Part_name>__MESH_JT__<keyword>.jt"

solver deck names     : "<Part_name>__<solver name>__<keyword>.<extn>"
<extn> values for language settings:
Simcenter Nastran  : ".dat"
MSC Nastran : ".dat"
ANSYS       : ".inp"
ABAQUS      : ".inp"
LSDYNA : ".k"
IDEAS_UNV : ".unv"
Samcef : ".dat"

Building Batch Meshing Executable using NX Open:
===============================================
In order to build batch-mesher using NX Open following steps
need to be followed:

-  User must have NX open licence.
-  In the command shell following variables must be available
other wise do "export" or on windows "set"
export UGII_BASE_DIR=<where_ever_UG_installed>/sol/kits
export UGII_USERFCN=$UGII_BASE_DIR/ugii
Note above paths are for unix; for windows "/"'s are "\".

-  Get following files from examples directory
ufx_batchmeshing_v3.cxx


- Follow standard NX open build and link process using either
$UGII_BASE_DIR/ugopen/ufcomp
$UGII_BASE_DIR/ugopen/uflink

-----------
Build Steps
-----------

Windows
-------
1. Using Visual Studio - create a new project using the NXOpen AppWizard.
This is described in the Automation -> NXOpen -> Open for C/C++ ->
Open C Reference Guide -> Overview -> Setting up your system -> Windows Operating System Setup.
When setting the Application Settings, select "An external application that runs independent of NX (EXE)"
and select C++ as the language.

2. Remove all the existing files from project.

3. Add the files from above to Source Files
by selecting the Project pulldown and select "Add Existing Item...". Select the file
using the popup window.

4. Build the internal image by going to the Build menu and selecting either
"Build Solution" or "Rebuild Solution".

This will create an executable called ufx_batchmeshing_v3.exe in the Debug directory.

Linux
----
1. Start up an NX command prompt window then start up ufmenu ($UGII_BASE_DIR/ugopen/ufmenu).
2. Compile the program accepting the defaults.
3. Link an internal user function program.
4. Answer the first question for linking with an "i" (Link internal/external user function (i/e):)
Select "y" for the next input to create an application with user interface code
Select "y" for the next input to Link a UG/Open++ Image (y/n).
5. Take the default linking options.
6. Provide the name of the program to link => Selection
7. Do not add any subroutines or libraries.

This will create ufx_batchmeshing_v3.so in the current directory.

Exit out of ufmenu.


Notes on program for some one to hack & modify this code:
========================================================

-  The data for the main program (i.e., the command line options) are
specified through the str  UF_UG_BatchMesh_CommandLineOpts_t.

-  If more command line arguements are needed, then easiest will be
to augment the structure UF_UG_BatchMesh_CommandLineOpts_t and
read/fill in the fields by following what is done in the routine
do_command_line_arg_parsing(). (Use those standard NX open functions
e.g., uc4620 etc., so that porting platforms are taken care off.)

-   Note if adding a string variable in str declare it a char array
of length MAX_FSPEC_BUFSIZE so that memory alloc
or free issues are not involved and looks like NX open does not
like strings above that length anyway.

-   Also, if possible add to the help text in the string below
scHelpText[]. (The format is easy to follow)

-   do_Batch_Meshing__main is the highest level function that sets
the batch meshing process, i.e., creates fem, idealized part
does solver setting etc.

*

//================================================================================
*/
#include <uf.h>
#define UF_CALL(X) (report_error( __FILE__, __LINE__, #X, (X)))

#include <stdio.h>
#include <time.h>
#include <set>
#include <string.h>
#include <stdarg.h>
#include <math.h>
#include <map>
#include <ctype.h>

#include <uf_assem.h>
#include <uf_cfi.h>
#include <uf_defs.h>
#include <uf_obj.h>
#include <uf_part.h>
#include <uf_retiring.h> 
#include <uf_sf_retiring.h>
#include <uf_sf.h>
#include <uf_sf_mshvld.h>
#include <uf_ui.h>


#include <NXOpen/BasePart.hxx>
#include <NXOpen/Body.hxx>
#include <NXOpen/BodyCollection.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/CAE_CAEBody.hxx>
#include <NXOpen/CAE_CAEFace.hxx>
#include <NXOpen/CAE_CaePart.hxx>
#include <NXOpen/CAE_CaeSession.hxx>
#include <NXOpen/CAE_DestinationCollectorBuilder.hxx>
#include <NXOpen/CAE_ElementTypeBuilder.hxx>
#include <NXOpen/CAE_FEModel.hxx>
#include <NXOpen/CAE_FemCreationOptions.hxx>
#include <NXOpen/CAE_FemPart.hxx>
#include <NXOpen/CAE_FemSynchronizeOptions.hxx>
#include <NXOpen/CAE_Mesh.hxx>
#include <NXOpen/CAE_Mesh2d.hxx>
#include <NXOpen/CAE_Mesh3d.hxx>
#include <NXOpen/CAE_Mesh2dBuilder.hxx>
#include <NXOpen/CAE_Mesh3dTetBuilder.hxx>
#include <NXOpen/CAE_MeshCollector.hxx>
#include <NXOpen/CAE_MeshControl.hxx>
#include <NXOpen/CAE_MeshControlBuilder.hxx>
#include <NXOpen/CAE_MeshControlCollection.hxx>
#include <NXOpen/CAE_MeshManager.hxx>
#include <NXOpen/CAE_ModelCheck_ITestValue.hxx>
#include <NXOpen/CAE_ModelCheck_QualityTestValue.hxx>
#include <NXOpen/CAE_ModelCheck_ElementQualitySetting.hxx>
#include <NXOpen/CAE_ModelCheck_ElementQualitySettingCollection.hxx>
#include <NXOpen/CAE_PropertyTable.hxx>
#include <NXOpen/CAE_SelectCAEFaceList.hxx>
#include <NXOpen/CAE_SimPart.hxx>
#include <NXOpen/CAE_SimSimulation.hxx>
#include <NXOpen/CAE_SimSolution.hxx>
#include <NXOpen/CAE_SimSolutionStep.hxx>
#include <NXOpen/DisplayableObject.hxx>
#include <NXOpen/Edge.hxx>
#include <NXOpen/Expression.hxx>
#include <NXOpen/Face.hxx>
#include <NXOpen/Information.hxx>
#include <NXOpen/ListingWindow.hxx>
#include <NXOpen/ModelingView.hxx>
#include <NXOpen/ModelingViewCollection.hxx>
#include <NXOpen/NXException.hxx>
#include <NXOpen/NXObject.hxx>
#include <NXOpen/NXObjectManager.hxx>
#include <NXOpen/Part.hxx>
#include <NXOpen/PartCollection.hxx>
#include <NXOpen/PhysicalMaterial.hxx>
#include <NXOpen/SelectDisplayableObjectList.hxx>
#include <NXOpen/SelectNXObjectList.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/Session.hxx>
#include <NXOpen/Unit.hxx>
#include <NXOpen/UnitCollection.hxx>
#include <NXOpen/Update.hxx>
#include <NXOpen/View.hxx>

using namespace std;
using namespace NXOpen;

/* ==========================================
Text of the help on command usage
========================================== */

static const char *scHelpText[] = {
    "UF_UG_BatchMeshing  -? -h -H -part=<Partname> ",
    "                    -t=<Template file name> -no_idealize",
    "                    -fem -dat -jt -key_word=<some keyword string>",
    "             ",
    "             ",
    "   -?  -h or -H               : Help on usage.",
    "             ",
    "             ",
    "   -part=<Partname>           : Part file path.",
    "                                Error if part does not exist or error ",
    "                                in opening. Must be valid ug part ",
    "                                file. The part name string is also ",
    "                                used to build name strings for .fem,",
    "                                .dat, idealized part and .LOG file.",
    "                                [please see \"More on naming conven- ",
    "                                 tion\" below]",
    "             ",
    "             ",
    "             ",
    "   -t=<Template file name>    : Template file name(specified format)",
    "                                the format of extension for",
    "                                template (.fem).",
    "                                User defined template can be placed:",
    "                                1. In any folder of user's choice but",
    "                                   template option must be accompanied",
    "                                   by the whole path to this file.",
    "                                e.g:-t=D:/workdir/partfolder/partname.prt.",
    "                                2. In any local template folder",
    "                                   ($UGII_TEMPLATE_DIR) and",
    "                                   can be added to a new or existing ",
    "                                   (.pax) file",
    "                                3.In any installation template folder",
    "                                  ($UGII_BASE_DIR/ugii/templates) and",
    "                                  can be added to a new or ",
    "                                  existing (.pax) file",
    "                                If not specified, program uses defaults.",
    "                                For example format, see top of the file",
    "                                ufx_batchmeshing_v3.cxx  OR look in the DIR",
    "                                ($UGII_BASE_DIR/ugopen/CAEBatchMeshing)",
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
    "   -jt=                       : Tells the program to dump Jt file from mesh.",
    "                                (If not specified, no jt file will be saved) ",
    "                                 bulk data)",
    "             ",
    "             ",
    "   -key_word=<keyword string> : This keyword is optional and is embedded ",
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
    "       JT from mesh file name:\"<Part_name>__MESH_JT__<keyword>.jt\"",
    //{"             "}, 
    "       solver deck names    : \"<Part_name>__<solver name>__<keyword>.<extn>\"",
    "          <solver name> and <extn> values are:",
    "          NX_NASTRAN  : \".dat\" ",
    "          MSC_Nastran : \".dat\" ",
    "          ANSYS       : \".inp\" ",
    "          ABAQUS      : \".inp\" ",
    "          LSDYNA : \".k\" ",
    "          IDEAS_UNV : \".unv\" ",
    "          Samcef : \".dat \" ",
    "             ",
    /* Important : Leave the following line intact. */
    "END_HELP"
};

/* ==========================================
Defines
========================================== */
#define UF_UG_BATCH_MESH__VERSION         "3.0"  // Batch meshing version file
#define UF_UG_BATCH_MESH__SCREEN_DUMP_ON  1

/* Batch mesh parameter names */
#define UF_UG_BATCH_MESH__PARM_help_str1       "?"      /* Help related */
#define UF_UG_BATCH_MESH__PARM_help_str2       "h"
#define UF_UG_BATCH_MESH__PARM_help_str3       "H"

#define UF_UG_BATCH_MESH__PARM_input_part      "part"
#define UF_UG_BATCH_MESH__PARM_template_file   "t"
#define UF_UG_BATCH_MESH__PARM_idealize_output "no_idealize"
#define UF_UG_BATCH_MESH__PARM_fem_output      "fem"
#define UF_UG_BATCH_MESH__PARM_jt_output       "jt"
#define UF_UG_BATCH_MESH__PARM_nastran_output  "dat"
#define UF_UG_BATCH_MESH__PARM_key_word        "key_word"

#define UF_UG_BATCH_MESH__start_watch    0
#define UF_UG_BATCH_MESH__stop_watch     1

#define ALL_BODY_TYPES    5

#define DECKUNITSMETRIC 4 /*(N)(m)(kg)*/
#define DECKUNITSENGLISH 6 /*(lbf)(in)(lbf-s^2/in)*/

#define JA_ERR_UNEXPECTED_SUCCESS 3520057


/* ==== Batch mesher command line options ==== */
typedef struct UF_UG_BatchMesh_CommandLineOpts_s
{
    char            run_key_word[MAX_FSPEC_BUFSIZE];

    int             fPartFile;                                        /* Must be specified */
    char            part_file_name[MAX_FSPEC_BUFSIZE];   /* Part file name */

    int             fTemplateFile;                                      /* TRUE => Template file specified */
    char            template_file_name[MAX_FSPEC_BUFSIZE]; /* FALSE=> Template file not supplied */

    char            Solver_Name[MAX_FSPEC_BUFSIZE];        /* Name of the solver
                                                           Default : NX NASTRAN */

    int             fOutIdealized;      /* TRUE/FALSE Whether to create idealized part */
    int             fOutputFEM;         /* TRUE/FALSE Whether to save fem */

    int             fOutputDAT;         /* TRUE/FALSE Whether to save NASTRAN .dat */
    char            dat_file_extn[MAX_FSPEC_BUFSIZE]; /* Extension for dat file optional */

    int             fOutputJT;          /* TRUE/FALSE Whether to save JT file */

} UF_UG_BatchMesh_CommandLineOpts_t, *UF_UG_BatchMesh_CommandLineOpts_p_t;

/* ========================
Static Data
======================== */
static FILE *UF_UG__BatchMesh_LOG = NULL;
static char  *MESH_LOG_file_Name = NULL;

/* =============================
Macro Definitions
============================= */

/* --- Initialize parameters for batch run --- */
#define   UF_UG__BatchMesh_INITBatchParams(pzParams) \
    strcpy((pzParams)->run_key_word, "");      \
    (pzParams)->fPartFile = false;             \
    strcpy((pzParams)->part_file_name, "");    \
    (pzParams)->fTemplateFile = false;         \
    strcpy((pzParams)->Solver_Name, "NX Nastran");   \
    strcpy((pzParams)->template_file_name, ""); \
    (pzParams)->fOutIdealized = true;          \
    (pzParams)->fOutputFEM = true;             \
    (pzParams)->fOutputDAT = false;            \
    strcpy((pzParams)->dat_file_extn, "dat");     \
    (pzParams)->fOutputJT = false;

/* ==================================================
Build appropriate solver deck extensions for
appropriate solver languages.
================================================== */
#define UF_UG__BatchMesh_GetDefaultSolverDeckFileExtn(scSolverName, scDeckExtn) \
          if (!strcmp((scSolverName), "ANSYS"))                    \
             strcpy ((scDeckExtn), ".inp");                             \
          else if (!strcmp((scSolverName), "ABAQUS"))                   \
             strcpy ((scDeckExtn), ".inp");                             \
          else if (!strcmp((scSolverName), "LSDYNA"))                    \
             strcpy ((scDeckExtn), ".k");                                \
          else if (!strcmp((scSolverName), "IDEAS UNV") )                \
             strcpy ((scDeckExtn), ".unv");                             \
          else                                                          \
             strcpy ((scDeckExtn), ".dat");

/* =============================================
Get proper solver language setup.
============================================= */
#define UF_UG__BatchMesh_GetSolverDeckName(scSolverName, scDeckName) \
if (!strcmp((scSolverName), "MSC NASTRAN") || !strcmp((scSolverName), "MSC Nastran"))                   \
             strcpy ((scDeckName), "MSC_Nastran");                             \
          else if (!strcmp((scSolverName), "Simcenter Nastran") || !strcmp((scSolverName), "NX NASTRAN"))               \
             strcpy ((scDeckName), "Simcenter_Nastran");                             \
          else if (!strcmp((scSolverName), "ANSYS")|| !strcmp((scSolverName), "Ansys"))                      \
             strcpy ((scDeckName), "ANSYS");                             \
          else if (!strcmp((scSolverName), "ABAQUS") || !strcmp((scSolverName), "Abaqus"))                   \
             strcpy ((scDeckName), "ABAQUS");                             \
          else if (!strcmp((scSolverName), "LSDYNA") || !strcmp((scSolverName), "LS-DYNA"))       \
             strcpy ((scDeckName), "LSDYNA");                             \
          else if (!strcmp((scSolverName), "IDEAS UNV") || !strcmp((scSolverName), "Ideas Unv"))       \
             strcpy ((scDeckName), "IDEAS_UNV");                             \
          else if (!strcmp((scSolverName), "Simcenter Samcef") || !strcmp((scSolverName), "SAMCEF"))       \
             strcpy ((scDeckName), "SAMCEF");                        \
          else if (!strcmp((scSolverName), "NX NASTRAN DESIGN"))       \
              strcpy((scDeckName), "NX_DESIGN_SIMULATION");           \
          else                                                          \
             strcpy ((scDeckName), "Simcenter_Nastran");

/* ==========================================
Local function prototype
========================================== */

static void do_command_line_arg_parsing(char argc,
    char *argv[],
    UF_UG_BatchMesh_CommandLineOpts_t *pzBatchRunParams,
    int  *pfDisplayCommandHelp);

static int create_fem_name_from_part_name(tag_t         cad_part_tag,
    int           fCreateIdealizedPart,
    UF_UG_BatchMesh_CommandLineOpts_t *pzBatchRunParams,
    char      **PartPathName,
    char      **FemPathName);
static int create_sim__with_name_from_part_name(tag_t         cad_part_tag,
    tag_t         fem_tag,
    UF_UG_BatchMesh_CommandLineOpts_t *pzBatchRunParams,
    tag_t         *new_sim_tag);
static int create_jt__with_name_from_part_name(tag_t tag_part_to_mesh, UF_UG_BatchMesh_CommandLineOpts_t *pzBatchRunParams, char** jtFilePath);
static int do_Batch_Meshing__main(UF_UG_BatchMesh_CommandLineOpts_t *pzBatchRunParams);
static void report_msg(char *msg);

static void write_info_fprintf(bool        fToConsole,
    FILE       *fp,             /* I   : File to print*/
    const char *format_string,  /* I   */
    ...                         /* I   */);
static void display_command_help(const char *scHelpText[]);
static int build_name_string(int       iNameOpt,
    tag_t     cad_part_tag,
    UF_UG_BatchMesh_CommandLineOpts_t *pzBatchRunParams,
    char      **NameString);
static void export_nastran_file(tag_t cad_part_tag,
    tag_t fem_tag, UF_UG_BatchMesh_CommandLineOpts_t *pzBatchRunParams);
static void close_logfile(FILE   *fp);
static bool isSolverSupported(const char * solverName);
static int validate_meshes
(
    int      num_meshes,
    tag_p_t  meshes_p,
    FILE     *details_fp
);
static FILE *open_logfile(tag_t  cad_part_tag,
    UF_UG_BatchMesh_CommandLineOpts_t *pzBatchRunParams);
//------------------------------------------------------------------------------------------------------------
static void start_batchmesher_logger(tag_t tag_part_to_mesh,
    UF_UG_BatchMesh_CommandLineOpts_t *pzBatchRunParams);
static void log_user_system_info(UF_system_info_t zSystemInfo);
static void log_pre_processing_info(int nCAEBodies, tag_t tag_part_to_mesh,
    UF_UG_BatchMesh_CommandLineOpts_t *pzBatchRunParams);
static int write_mesh_quality_report(CAE::Mesh *                        mesh);
static void STOP_CLOCK(int          start_end_flag,
    UF_timer_p_t pztimer,
    char         *scMessage);
static void Time_Sec_to_hr_min_sec(double dTimeSec, int *Hour, int *Min, double *dSec);
static void upper_to_lower_case(char *scString);
static bool isUnixEnv = false;

static int validate_meshes
(
    int      num_meshes,
    tag_p_t  meshes_p,
    FILE     *details_fp
);

static int report_error(char *file, int line, char *call, int irc)
{
    if (irc)
    {
        char err[133],
            msg[133];

        sprintf(msg, "*** ERROR code %d at line %d in %s:\n+++ ", irc, line, file);
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
extern int main(int argc, char *argv[])
{
    int         iRc = 0;

    int                                     nParts_Saved = 0;

    tag_t                               *saved_part_tags = NULL;


    UF_UG_BatchMesh_CommandLineOpts_t   zBatchRunParams;

    int                                 *error_list = NULL;

    char                                *ug_version = NULL;

    int                                 fDisplayCommandHelp = false;


    /* Just a printf to see if we indeed launch batch mesher */
    fprintf(stdout, "Launching batchmesher core executable.\n");

    /* Initialize the API environment */
    if (UF_CALL(UF_initialize()))
    {
        /* Failed to initialize */
        //fprintf(stdout,"ERROR :  UG open module could not be initialized\n",);
        report_msg("ERROR:  UG open module could not be initialized\n");
        report_msg("        Exiting batchmesher...\n\n");
        return 0;
    }


    /* Command line processor */
    UF_CALL(UF_get_release(&ug_version));
    fprintf(stdout, "     \n\n");
    fprintf(stdout, "==== Batch Meshing Version %s for UG %s ====\n",
        UF_UG_BATCH_MESH__VERSION, ug_version);
    fprintf(stdout, "   \n");
    fprintf(stdout, "                 ==== REPORT ====  \n");
    fprintf(stdout, "                      ------  \n\n");
    UF_free(ug_version);

    /* Command line parsing */
    do_command_line_arg_parsing(argc, argv, &zBatchRunParams,
        &fDisplayCommandHelp);

    /* If user asked for help */
    if (fDisplayCommandHelp)
        display_command_help(scHelpText);

    if (zBatchRunParams.fPartFile == (int)true)
    {
        /* ==================================
        Run batch meshing application
        ===================================== */
        iRc = do_Batch_Meshing__main(&zBatchRunParams);

        if (zBatchRunParams.fOutputFEM == (int)true && iRc == 0)
        {
            /* =========================
            Save all the results
            ============================ */
            nParts_Saved = 0;
            iRc = UF_PART_save_all(&nParts_Saved, &saved_part_tags, &error_list);
            if (saved_part_tags != NULL)
                UF_free(saved_part_tags);

            if (error_list != NULL)
                UF_free(error_list);
        }

        /* =========================
        Close all the Parts
        ============================ */
        try
        {
            Session *theSession = Session::GetSession();
            theSession->Parts()->CloseAll(BasePart::CloseModifiedCloseModified, NULL);
        }
        catch (const NXException &error)
        {
            if (error.ErrorCode() != JA_ERR_UNEXPECTED_SUCCESS)
            {
                write_info_fprintf(true, UF_UG__BatchMesh_LOG, "\nERROR: %s\n", (char*)error.Message());
                return 9999;
            }
        }

    }

    /* Terminate the API environment */
    UF_CALL(UF_terminate());

    return iRc;
}

/* ===========================================================
Save the output files that are requested : .fem files
nastran bulk data files ....
=========================================================== */
static void export_nastran_file(tag_t cad_part_tag,
    tag_t fem_tag, UF_UG_BatchMesh_CommandLineOpts_t *pzBatchRunParams)
{
    int             iRc = 0;
    int             format_choice = 1;
    tag_t           new_sim_tag = NULL_TAG;

    tag_t           solution_desc = NULL_TAG, solver_desc = NULL_TAG;
    tag_t           language_tag = NULL_TAG, solution_tag = NULL_TAG;

    char            *sol_name = NULL;

    /* Timers */
    UF_timer_t     zSOLVER_DECK_time;

    if (pzBatchRunParams->fOutputDAT == (int)true)
    {
        /* Start timer */
        STOP_CLOCK(UF_UG_BATCH_MESH__start_watch, &zSOLVER_DECK_time, NULL);

        /* Create  simulation */
        iRc = create_sim__with_name_from_part_name(cad_part_tag, fem_tag,
            pzBatchRunParams, &new_sim_tag);
        if (iRc == 0 && new_sim_tag != NULL_TAG)
        {
            char            scPartName[MAX_FSPEC_BUFSIZE];
            char            scPartDirectoryPath[MAX_FSPEC_BUFSIZE];
            char            *scSol_Directory = NULL;
            char            *scSol_Directory_Tmp = NULL;
            int      iRc = 0, iLen = 0, mem_error = 0;

            char     *new_nastran_deck_name = NULL;
            char     *old_nastran_deck_name = NULL;
            char     scDeckExtn[MAX_FSPEC_BUFSIZE] = { ' ' };
            int             iStrLen = 0;

            char            scCurrentDirectory[MAX_FSPEC_BUFSIZE];

            /* Init string variables */
            strcpy(scPartName, "");
            strcpy(scPartDirectoryPath, "");
            strcpy(scCurrentDirectory, "");

            build_name_string(6, cad_part_tag, pzBatchRunParams,
                &new_nastran_deck_name);
            UF_UG__BatchMesh_GetDefaultSolverDeckFileExtn(pzBatchRunParams->Solver_Name, \
                scDeckExtn);
            //strcat (new_nastran_deck_name, scDeckExtn);
            iRc = uc4576(pzBatchRunParams->part_file_name, 2, scPartDirectoryPath,
                scPartName);

            if (strlen(scPartDirectoryPath))
            {

                /* uc4565 : Get current directory */
                uc4565(1, scCurrentDirectory);

                iStrLen = (int)(strlen(scPartDirectoryPath) + strlen(new_nastran_deck_name) +
                    strlen(scCurrentDirectory) + 20);
                scSol_Directory = (char*)UF_allocate_memory(iStrLen * sizeof(char),
                    &mem_error);
                scSol_Directory_Tmp = (char*)UF_allocate_memory(iStrLen * sizeof(char),
                    &mem_error);

                strcpy(scSol_Directory_Tmp, scPartDirectoryPath);

                iRc = uc4575(scSol_Directory_Tmp, 0, new_nastran_deck_name,
                    scSol_Directory);

                iRc = uc4560(scSol_Directory, 0);
                if (iRc == 0)
                {
                    write_info_fprintf(true, UF_UG__BatchMesh_LOG, "WARNING : Deleting pre-existing file found with the same name. \n");
                    /* File exists : So delete it from the system */
                    iRc = uc4561(scSol_Directory, 0);
                    if (iRc != 0)
                    {
                        /* Could not delete the file : Error out */
                        report_msg("Error : Solver deck file already exists\n");
                        report_msg("        File name : "); report_msg(new_nastran_deck_name);
                        report_msg("\n        Could not delete existing file.\n");
                        write_info_fprintf(true, UF_UG__BatchMesh_LOG, "Error : Could not delete existing file. \n");
                        return;
                    }
                }

                NXObject *partObj = (NXObject *)NXObjectManager::Get(new_sim_tag);
                Session *theSession = Session::GetSession();
                CAE::SimPart *workSimPart(dynamic_cast<CAE::SimPart *>(partObj));
                CAE::SimPart *displaySimPart(dynamic_cast<CAE::SimPart *>(theSession->Parts()->BaseDisplay()));
                // ----------------------------------------------
                //   Menu: File->Export->Simulation...
                // ----------------------------------------------
                CAE::CaeDataContainer *caeDataContainer1;
                caeDataContainer1 = theSession->CaeSession()->GetDataContainer();
                int partunits;
                UF_PART_ask_units(cad_part_tag, &partunits);

                if (strcmp(pzBatchRunParams->Solver_Name, "SAMCEF") == 0)
                {
                    caeDataContainer1->AddInteger("output file method", 1);
                    caeDataContainer1->AddString("output file", new_nastran_deck_name);
                }
                else
                {
                    caeDataContainer1->AddInteger("solverInputFileNameMethod", 1);
                    caeDataContainer1->AddString("solverInputFileFullPath", scSol_Directory);
                }

                if (partunits != UF_PART_METRIC)
                    caeDataContainer1->AddInteger("units", DECKUNITSENGLISH);
                else
                    caeDataContainer1->AddInteger("units", DECKUNITSMETRIC);
                std::vector<TaggedObject *> tagvector1(1);
                TaggedObject *nullTaggedObject(NULL);
                tagvector1[0] = nullTaggedObject;
                caeDataContainer1->AddTaggedObjectVector("roundTripParam", tagvector1);

                caeDataContainer1->AddInteger("subsetExportIndex", 0);

                std::vector<TaggedObject *> tagvector2(0);
                caeDataContainer1->AddTaggedObjectVector("subsetExportGroups", tagvector2);

                caeDataContainer1->AddLogical("exportNasStatSection", true);

                caeDataContainer1->AddLogical("exportFileMgmtSection", true);

                caeDataContainer1->AddLogical("exportExecControlSection", true);

                caeDataContainer1->AddLogical("exportCaseControlSection", true);

                caeDataContainer1->AddLogical("exportSets", false);

                caeDataContainer1->AddLogical("exportBulkDataSection", true);

                caeDataContainer1->AddLogical("exportBeginEndData", true);

                caeDataContainer1->AddLogical("exportParams", true);

                std::vector<TaggedObject *> tagvector3(1);
                tagvector3[0] = nullTaggedObject;
                caeDataContainer1->AddTaggedObjectVector("additionalParam", tagvector3);

                caeDataContainer1->AddLogical("exportCoordSys", true);

                caeDataContainer1->AddLogical("exportNodes", true);

                caeDataContainer1->AddLogical("exportElements", true);

                caeDataContainer1->AddLogical("exportMaterials", true);

                caeDataContainer1->AddLogical("exportPhysProps", true);

                caeDataContainer1->AddLogical("exportLoads", true);

                caeDataContainer1->AddLogical("exportConstraints", true);

                caeDataContainer1->AddLogical("exportSimObjects", true);

                std::vector<TaggedObject *> tagvector4(1);
                tagvector4[0] = nullTaggedObject;
                caeDataContainer1->AddTaggedObjectVector("basicCsys", tagvector4);

                caeDataContainer1->AddInteger("selectiveExportMethod", 0);

                std::vector<NXString> stringarray1(0);
                caeDataContainer1->AddStrings("cardsToSkip", stringarray1);

                caeDataContainer1->AddInteger("exportSystemCellsFormat", 0);

                caeDataContainer1->AddLogical("exportPerformanceMode", true);

                caeDataContainer1->AddLogical("exportRealDataFilter", true);

                caeDataContainer1->AddDouble("exportRealFilterValue", 1e-015);

                caeDataContainer1->AddInteger("exportFormatType", 0);

                caeDataContainer1->AddInteger("exportFieldLength", 1);

                caeDataContainer1->AddInteger("exportExpFormat", 0);

                caeDataContainer1->AddInteger("exportRealDataPrecision", 0);

                caeDataContainer1->AddInteger("exportCardDescription", 0);

                caeDataContainer1->AddInteger("coordSysIdOffset", 0);

                caeDataContainer1->AddInteger("nodeIdOffset", 0);

                caeDataContainer1->AddInteger("elementIdOffset", 0);

                caeDataContainer1->AddInteger("materialIdOffset", 0);

                caeDataContainer1->AddInteger("physPropIdOffset", 0);

                caeDataContainer1->AddLogical("exportDofSetAltFormat", false);

                caeDataContainer1->AddLogical("unitsCollapsed", false);

                caeDataContainer1->AddLogical("fileCollapsed", false);

                caeDataContainer1->AddLogical("formattingCollapsed", true);

                caeDataContainer1->AddLogical("subsetExportCollapsed", true);

                caeDataContainer1->AddLogical("exportOptionsCollapsed", false);

                caeDataContainer1->AddLogical("modelOrientationCollapsed", true);

                caeDataContainer1->AddLogical("systemCellsCollpased", false);

                caeDataContainer1->AddLogical("bulkOptionsCollapsed", false);

                caeDataContainer1->AddLogical("offsetCollapsed", true);

                CAE::SimPart *simPart1(dynamic_cast<CAE::SimPart *>(workSimPart));
                simPart1->ExportSimulation(pzBatchRunParams->Solver_Name, caeDataContainer1);

                delete caeDataContainer1;
                /* Rename the nastran solver deck */
                //rename_nastran_solver_deck_file ( cad_part_tag, sol_name, 
                // pzBatchRunParams);
            }

            /* Solver deck time */
            STOP_CLOCK(UF_UG_BATCH_MESH__stop_watch, &zSOLVER_DECK_time,
                "\nTime taken to dump solver deck ");
        }

        /* Free dynamically allocated memory */
        if (sol_name != NULL)
            UF_free(sol_name);

    }
    return;
}

/* ==========================================================
Error message reporting function.

msg         -i   Message string

Return value:
None
========================================================== */
static void report_msg(char *msg)
{
    UF_print_syslog(msg, FALSE);
    //UF_print_syslog("\n", FALSE);

    if (!UF_UI_open_listing_window())
    {
        UF_UI_write_listing_window(msg);
        //UF_UI_write_listing_window("\n");
    }

} /* End of report_msg( char *msg) */

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
static int do_Batch_Meshing__main(UF_UG_BatchMesh_CommandLineOpts_t *pzBatchRunParams)
{
    int                            iRc = 0;
    try
    {

        //Intialize all names that would be used  
        char                           *scElementName = NULL;
        char                           *scMeshType = NULL;
        char                           *CAD_Part_Name = NULL;
        char                           *FEM_file_Name = NULL;
        char                           *SIM_file_Name = NULL;
        char                           *IDEALIZED_file_Name = NULL;
        char                           *SOLVER_file_Name = NULL;
        // char                           *MESH_LOG_file_Name = NULL;
        char                           *JT_MESH_file_Name = NULL;
        char                           *jt_file_path_name = NULL;

        NXString                       scSolverName = NULL;
        NXString                       scAnalysisType = NULL;
        // All the integers that would be used 
        int                            partunits = 0;
        int                            i = 0, iRMat = 0, iRbody = 0;
        int                            nCAEBodies = 0;
        tag_t                          *CAEBodies_p = NULL;

        int                           mem_error = 0;
        int                           iExpectedStrLen = 0;

        UF_system_info_t               zSystemInfo;

        // all the the tags that would be used
        tag_t                          tag_part_to_mesh = NULL_TAG;
        tag_t                          new_fem_tag = NULL_TAG;
        tag_t                          iThis_Body_tag = NULL_TAG;

        tag_t                          mesh_tag = NULL_TAG;

        UF_timer_t                     zOVERALL_timer;


        zSystemInfo.date_buf = NULL;      /* Current date and time info */
        zSystemInfo.user_name = NULL;     /* User, who is running this process */
        zSystemInfo.program_name = NULL;  /* The current program name */
        zSystemInfo.node_name = NULL;     /* Machine, on which this process is running */
        zSystemInfo.machine_type = NULL;  /* Hardware type on which the machine is running */
        zSystemInfo.os_name = NULL;       /* Operating system, on which this process is running*/
        zSystemInfo.os_version = NULL;    /* Version and release level of this Operating System */

                                          // Run the NX Session 
        Session *theSession = Session::GetSession();

        /* Start timer */
        STOP_CLOCK(UF_UG_BATCH_MESH__start_watch, &zOVERALL_timer, NULL);

        char            *Part_part_name = NULL;
        char            *Fem_part_name = NULL;

        
        /* =================
        Open the Template
        ================= */
        BasePart *basePart2;
        PartLoadStatus *partLoadStatus2 = NULL;
        if (pzBatchRunParams->fTemplateFile == (int)true)
        {
            try
            {
                basePart2 = theSession->Parts()->OpenActiveDisplay(pzBatchRunParams->template_file_name, NXOpen::DisplayPartOptionAllowAdditional, &partLoadStatus2);
            }
            catch (const NXException &error)
            {
                write_info_fprintf(true, UF_UG__BatchMesh_LOG, "\nThe selected template has not been found.\n");
                return 9999;
            }
        }
        else
        {
            write_info_fprintf(true, UF_UG__BatchMesh_LOG, "\n ######################## ERROR ################################## \n");
            write_info_fprintf(true, UF_UG__BatchMesh_LOG, "\n No Template Has been passed in the input. Aborting the Process....\n");
            return 9999;
        }

        if (partLoadStatus2 == NULL)
        {
            report_msg("Failed to load the template part.\n");
            write_info_fprintf(true, UF_UG__BatchMesh_LOG, "ERROR: Failed to load the template part.\n");
            return 9999;
        }
        CAE::FemPart *workFemPart = dynamic_cast<CAE::FemPart *>(theSession->Parts()->BaseWork());
        CAE::FemPart *displayFemPart = dynamic_cast<CAE::FemPart *>(theSession->Parts()->BaseDisplay());
        delete partLoadStatus2;
        theSession->ApplicationSwitchImmediate("UG_APP_SFEM");

        /* =================
        Open the part
        ================= */
        BasePart *basePart1;
        PartLoadStatus *partLoadStatus1;
        basePart1 = theSession->Parts()->OpenActiveDisplay(pzBatchRunParams->part_file_name, NXOpen::DisplayPartOptionAllowAdditional, &partLoadStatus1);
        tag_part_to_mesh = basePart1->Tag();
        delete partLoadStatus1;

        workFemPart = NULL;
        displayFemPart = NULL;
        Part *workPart(theSession->Parts()->Work());
        Part *displayPart(theSession->Parts()->Display());

        if (workPart->Tag() == NULL_TAG)
        {
            report_msg("This NX Open program requires a work part \n");
            write_info_fprintf(true, UF_UG__BatchMesh_LOG, "ERROR: BatchMesher requires a work part\n");
            return 9999;
        }

        if (workPart->Tag() != tag_part_to_mesh)
        {
            report_msg("Programing Error: Work part is not same as part to mesh.\n");
            write_info_fprintf(true, UF_UG__BatchMesh_LOG, "ERROR: Programing Error: Work part is not same as part to mesh.\n");
            return 9999;
        }

        // Function communicates to the batchmesher where to store the new FEM.
        // FEM's name is also determined in this function.
        iRc = create_fem_name_from_part_name(tag_part_to_mesh, pzBatchRunParams->fOutIdealized, pzBatchRunParams, &Part_part_name, &Fem_part_name);


        UF_PART_ask_units(tag_part_to_mesh, &partunits);

        //Crank up the Logger
        start_batchmesher_logger(tag_part_to_mesh, pzBatchRunParams);

        //Needs header here batchmeshing header
        log_user_system_info(zSystemInfo);

        UF_ask_system_info(&zSystemInfo);
        if (zSystemInfo.os_name != NULL)
        {
            /* Check for linux/unix */
            upper_to_lower_case(zSystemInfo.os_name);
            if (strstr(zSystemInfo.os_name, "windows") == NULL)
            {
                isUnixEnv = true;
            }
        }
        UF_free_system_info(&zSystemInfo);

        CAE::FemPart *femPart1(dynamic_cast<NXOpen::CAE::FemPart *>(basePart2));
        PartLoadStatus *partLoadStatus3;
        PartCollection::SdpsStatus status1;
        status1 = theSession->Parts()->SetDisplay(femPart1, false, true, &partLoadStatus3);
        
        BodyCollection *theBodies = workPart->Bodies();
        std::vector<Body *> bodies1;
        for (BodyCollection::iterator bodyIter = theBodies->begin(); bodyIter != theBodies->end(); bodyIter++)
        {
            NXOpen::Body* pzBody = *bodyIter;

            if (pzBody && !pzBody->IsBlanked())
            {
                bodies1.push_back(pzBody);
                nCAEBodies++;
            }
        }

        workPart = NULL;
        workFemPart = dynamic_cast<CAE::FemPart *>(theSession->Parts()->BaseWork()); 
        displayPart = NULL;
        displayFemPart = dynamic_cast<CAE::FemPart *>(theSession->Parts()->BaseDisplay()); 
        CAE::FemPart *femPart2(dynamic_cast<CAE::FemPart *>(workFemPart));
        theSession->Parts()->SetWork(femPart2);

        if (pzBatchRunParams->fOutputFEM == (int)true)
        {
            PartSaveStatus *partSaveStatus2;
            femPart2->AssignPermanentName(Fem_part_name);
            partSaveStatus2 = femPart2->Save(BasePart::SaveComponentsTrue, BasePart::CloseAfterSaveFalse);;
            delete partSaveStatus2;
        }

        if (pzBatchRunParams->fTemplateFile == (int)true)
            femPart2->GetSolverAndAnalysisType(&scSolverName, &scAnalysisType);

        int templateunits = 0;
        UF_PART_ask_units(femPart1->Tag(), &templateunits);

        if (templateunits != partunits)
        {
            report_msg("Units in the part do not match the units in the template..\n");
            write_info_fprintf(true, UF_UG__BatchMesh_LOG, "ERROR: Units in the part do not match the units in the template.\n");
            return 9999;
        }

        CAE::FemSynchronizeOptions *femSynchronizeOptions1;

        CAE::FemPart::UseBodiesOption useBodiesOption;
        vector<Body *> listOfBodies;

        CAE::FemPart *femPart3(dynamic_cast<CAE::FemPart *>(workFemPart));
        std::vector<NXString> description1(0);

        CAE::FemCreationOptions *femCreationOptions1;
        femCreationOptions1 = femPart3->NewFemCreationOptions();
        Part *part1(dynamic_cast<NXOpen::Part *>(basePart1));
        femCreationOptions1->SetCadData(part1, Part_part_name);

        femPart3->GetGeometryData(&useBodiesOption, listOfBodies, &femSynchronizeOptions1);
            
        femCreationOptions1->SetGeometryOptions(CAE::FemCreationOptions::UseBodiesOptionVisibleBodies, bodies1, femSynchronizeOptions1);
        femCreationOptions1->SetSolverOptions(scSolverName, scAnalysisType, CAE::BaseFemPart::AxisymAbstractionTypeNone);
        femCreationOptions1->SetDescription(description1);

        //FEM is created Here
        CAE::FemPart *femPart4(dynamic_cast<CAE::FemPart *>(workFemPart));
        femPart4->FinalizeCreation(femCreationOptions1);

        delete femCreationOptions1;
        delete femSynchronizeOptions1;

        CAE::FEModel *fEModel(dynamic_cast<CAE::FEModel *>(workFemPart->FindObject("FEModel")));
        CAE::MeshManager *meshManager(dynamic_cast<CAE::MeshManager *>(fEModel->Find("MeshManager")));

        iRbody = UF_SF_ask_all_polygon_bodies(&nCAEBodies, &CAEBodies_p);

        strcpy(pzBatchRunParams->Solver_Name, scSolverName.GetUTF8Text());

        log_pre_processing_info(nCAEBodies, tag_part_to_mesh, pzBatchRunParams);

        std::vector<CAE::Mesh *> Meshes;
        std::vector<CAE::Mesh *>::iterator iter;
        Meshes = meshManager->GetMeshes();

        if (pzBatchRunParams->fOutputFEM == (int)true)
        {
            CAE::FemPart *femPart5(dynamic_cast<CAE::FemPart *>(workFemPart));
            PartSaveStatus *partSaveStatus1;
            partSaveStatus1 = femPart5->Save(BasePart::SaveComponentsTrue, BasePart::CloseAfterSaveFalse);
            delete partSaveStatus1;
        }

        
        UF_ask_system_info(&zSystemInfo);

        /* ============================
        Output JT if asked for
        ============================ */
        if (pzBatchRunParams->fOutputJT == (int)true)
        {
            char* jtFilePath = NULL;
            int retCode = create_jt__with_name_from_part_name(tag_part_to_mesh, pzBatchRunParams,&jtFilePath);
            NXString nxStr(jtFilePath);
            if (retCode == 0)
            {
                CAE::FemPart *femPart6(dynamic_cast<CAE::FemPart *>(workFemPart));
                femPart6->ExportJt(nxStr);
            }
            UF_free(jtFilePath);
            jtFilePath = NULL;
        }

        /* ==========================================
        Output Nastran bulk data file if asked
        ========================================== */
        if (isSolverSupported(pzBatchRunParams->Solver_Name))
        {
            if (pzBatchRunParams->fOutputDAT == (int)true)
                export_nastran_file(tag_part_to_mesh, new_fem_tag, pzBatchRunParams);
        }
        else
        {
            write_info_fprintf(true, UF_UG__BatchMesh_LOG, " Info: Solver input file generation is not supported \n for this solver in this BatchMesher version \n");
        }
        

        /* ===================================
        Overall process time : End timer
        =================================== */
        STOP_CLOCK(UF_UG_BATCH_MESH__stop_watch, &zOVERALL_timer,
            "\nTime taken (overall process) ");

        /* ===================================
        Mesh Quality report
        =================================== */
        for (iter = Meshes.begin(); iter != Meshes.end(); ++iter)
        {
            if ((*iter)->Tag() == NULL_TAG)
            {
                iRc = 100;
                report_msg("Error : Failed to mesh body.\n");
                write_info_fprintf(true, UF_UG__BatchMesh_LOG, "Mesh generation failed.\n");
            }
            else
            {
                write_mesh_quality_report(*iter);
            }
        }

        /* ===================================
        Mesh Info report
        =================================== */
        for (iter = Meshes.begin(); iter != Meshes.end(); ++iter)
        {
            theSession->ListingWindow()->SelectDevice(ListingWindow::DeviceTypeFile, MESH_LOG_file_Name);
            theSession->ListingWindow()->Open();

            std::vector<NXObject *> selectedObjects1(1);
            selectedObjects1[0] = *iter;
            theSession->Information()->DisplayObjectsDetails(selectedObjects1);
        }

        /* ==========================
        Close mesh report log
        ========================== */
        close_logfile(UF_UG__BatchMesh_LOG);
        //close the file and flush the buffer
        theSession->ListingWindow()->Close();
        theSession->ListingWindow()->SelectDevice(ListingWindow::DeviceTypeNone, "");


        /* Free dynamically allocated memory */
        if (CAEBodies_p != NULL)
            UF_free(CAEBodies_p);

        if (CAD_Part_Name != NULL)
            UF_free(CAD_Part_Name);

        if (FEM_file_Name != NULL)
            UF_free(FEM_file_Name);

        if (SOLVER_file_Name != NULL)
            UF_free(SOLVER_file_Name);

        if (SIM_file_Name != NULL)
            UF_free(SIM_file_Name);

        if (IDEALIZED_file_Name != NULL)
            UF_free(IDEALIZED_file_Name);

        if (MESH_LOG_file_Name != NULL)
            UF_free(MESH_LOG_file_Name);

        if (JT_MESH_file_Name != NULL)
            UF_free(JT_MESH_file_Name);

        if (jt_file_path_name != NULL)
            UF_free(JT_MESH_file_Name);

        UF_free(scElementName);
        UF_free(scMeshType);
        /* Free system info */
        UF_free_system_info(&zSystemInfo);

    }
    catch (const NXException &error)
    {
        if (error.ErrorCode() != JA_ERR_UNEXPECTED_SUCCESS)
        {
            write_info_fprintf(true, UF_UG__BatchMesh_LOG, "\nERROR: %s\n", (char*)error.Message());
            return 9999;
        }
    }
    /* No error return */
    return iRc;

} /* End of do_Batch_Meshing (void) */

  /* ========================================================================
  This function creates a FEM.  Most of the data such as FEM name
  etc is derived from part name.

  cad_part_tag          i -  CAD part tag

  new_fem_tag           o - New fem tag

  Return
  0  => No error
  !0 => Error

  */
static int create_fem_name_from_part_name(tag_t         cad_part_tag,
    int           fCreateIdealizedPart,
    UF_UG_BatchMesh_CommandLineOpts_t *pzBatchRunParams,
    char      **PartPathName,
    char      **FemPathName)
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

    char            scPartName[MAX_FSPEC_BUFSIZE];
    char            scPartDirectoryPath[MAX_FSPEC_BUFSIZE];
    char            *scIdealizedPart_Directory = NULL;
    char            *scIdealizedPart_Directory_Tmp = NULL;
    char            *scFem_Directory = NULL;
    char            *scFem_Directory_Tmp = NULL;
    int             iStrLen = 0;

    char            scCurrentDirectory[MAX_FSPEC_BUFSIZE];

    /* Init string variables */
    strcpy(scPartName, "");
    strcpy(scPartDirectoryPath, "");
    strcpy(scCurrentDirectory, "");

    if (fCreateIdealizedPart == int(true))
    {
        /* Build name string for idealized part */
        build_name_string(1, cad_part_tag, pzBatchRunParams, &idealized_part_name);

        /* ==============================================
        Make sure idealized prt does not exist.
        If exists delete the file.
        ============================================== */
        iRc = uc4560(idealized_part_name, 0);
        if (iRc == 0)
        {
            /* ========================================
            File exists IN CURRENT WORKING DIRECTORY
            So delete it from the system
            ======================================== */
            iRc = uc4561(idealized_part_name, 0);
            if (iRc != 0)
            {
                /* Could not delete the file : Error out */
                report_msg("Error : Idealized part already exists\n");
                report_msg("        File name : "); report_msg(idealized_part_name);
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
            iRc = uc4576(pzBatchRunParams->part_file_name, 2, scPartDirectoryPath,
                scPartName);

            if (strlen(scPartDirectoryPath) == 0)
                uc4565(1, scPartDirectoryPath);

            if (strlen(scPartDirectoryPath))
            {

                /* uc4565 : Get current directory */
                uc4565(1, scCurrentDirectory);

                iStrLen = (int)(strlen(scPartDirectoryPath) + strlen(idealized_part_name) +
                    strlen(scCurrentDirectory) + 20);
                scIdealizedPart_Directory = (char*)UF_allocate_memory(iStrLen * sizeof(char),
                    &mem_error);
                scIdealizedPart_Directory_Tmp = (char*)UF_allocate_memory(iStrLen * sizeof(char),
                    &mem_error);
                *PartPathName = (char*)UF_allocate_memory(iStrLen * sizeof(char),
                    &mem_error);
                /* Idealized part is saved along with part. So in that
                directory look for idealized part */
                strcpy(scIdealizedPart_Directory_Tmp, scPartDirectoryPath);

                /* uc4575 : Build path & file name : Append directory path & file name */
                //iRc = uc4575( scCurrentDirectory, 0, scPartDirectoryPath, 
                //               scIdealizedPart_Directory_Tmp);
                iRc = uc4575(scIdealizedPart_Directory_Tmp, 2, idealized_part_name,
                    scIdealizedPart_Directory);

                strcpy(*PartPathName, scIdealizedPart_Directory);
                /* uc4560 : Checks whether the specified file of the given type exists */
                iRc = uc4560(scIdealizedPart_Directory, 0);
                if (iRc == 0)
                {
                    /* uc4561  Remove a given file from the file system. */
                    iRc = uc4561(scIdealizedPart_Directory, 0);
                    if (iRc != 0)
                    {
                        /* Could not delete the file : Error out */
                        report_msg("Error : Idealized part already exists\n");
                        report_msg("        File name : "); report_msg(idealized_part_name);
                        report_msg("\n        Could not delete existing file.\n");
                        if (scIdealizedPart_Directory != NULL)
                        {
                            UF_free(scIdealizedPart_Directory);
                            scIdealizedPart_Directory = NULL;
                        }
                        if (scIdealizedPart_Directory_Tmp != NULL)
                        {
                            UF_free(scIdealizedPart_Directory_Tmp);
                            scIdealizedPart_Directory_Tmp = NULL;
                        }
                        return -9999;
                    }
                }
                if (scIdealizedPart_Directory != NULL)
                {
                    UF_free(scIdealizedPart_Directory);
                    scIdealizedPart_Directory = NULL;
                }
                if (scIdealizedPart_Directory_Tmp != NULL)
                {
                    UF_free(scIdealizedPart_Directory_Tmp);
                    scIdealizedPart_Directory_Tmp = NULL;
                }
            }
        }
    }
    else
    {
        iStrLen = (int)(strlen(pzBatchRunParams->part_file_name));

        *PartPathName = (char*)UF_allocate_memory(iStrLen * sizeof(char),
            &mem_error);
        strcpy(*PartPathName, pzBatchRunParams->part_file_name);

    }

    /* Build name string for fem file */
    build_name_string(2, cad_part_tag, pzBatchRunParams, &fem_name);
    /* ==============================================
    Make sure fem file does not exist in OS.
    If exists delete the file.
    ============================================== */
    iRc = uc4560(fem_name, 0);
    if (iRc == 0)
    {
        /* File exists : So delete it from the system */
        iRc = uc4561(fem_name, 0);
        if (iRc != 0)
        {
            /* Could not delete the file : Error out */
            report_msg("Error : FEM file already exists\n");
            report_msg("        File name : "); report_msg(fem_name);
            report_msg("\n        Could not delete existing file.\n");
            return -9999;
        }
    }

    iRc = uc4576(pzBatchRunParams->part_file_name, 2, scPartDirectoryPath,
        scPartName);

    if (strlen(scPartDirectoryPath) == 0)
        uc4565(1, scPartDirectoryPath);

    if (strlen(scPartDirectoryPath))
    {

        /* uc4565 : Get current directory */
        uc4565(1, scCurrentDirectory);

        iStrLen = (int)(strlen(scPartDirectoryPath) + strlen(fem_name) +
            strlen(scCurrentDirectory) + 20);
        scFem_Directory = (char*)UF_allocate_memory(iStrLen * sizeof(char),
            &mem_error);
        scFem_Directory_Tmp = (char*)UF_allocate_memory(iStrLen * sizeof(char),
            &mem_error);
        *FemPathName = (char*)UF_allocate_memory(iStrLen * sizeof(char),
            &mem_error);
        strcpy(scFem_Directory_Tmp, scPartDirectoryPath);

        iRc = uc4575(scFem_Directory_Tmp, 0, fem_name,
            scFem_Directory);
        strcpy(*FemPathName, scFem_Directory);
        iRc = uc4560(*FemPathName, 0);
        if (iRc == 0)
        {
            write_info_fprintf(true, UF_UG__BatchMesh_LOG, "WARNING : Deleting pre-existing file found with the same name. \n");
            /* File exists : So delete it from the system */
            iRc = uc4561(*FemPathName, 0);
            if (iRc != 0)
            {
                /* Could not delete the file : Error out */
                report_msg("Error : FEM file already exists\n");
                report_msg("        File name : "); report_msg(fem_name);
                report_msg("\n        Could not delete existing file.\n");
                write_info_fprintf(true, UF_UG__BatchMesh_LOG, "Error : Could not delete existing file. \n");
                return -9999;
            }
        }

        iRc = 0;
    }
    num_desc_lines = 1;
    description = (char*)UF_allocate_memory(10 * sizeof(char), &mem_error);
    if (mem_error != 0)
    {
        iRc = mem_error;
        return iRc;
    }
    strcpy(description, " ");


    if (fem_name != NULL)
    {
        UF_free(fem_name);
    }

    if (idealized_part_name != NULL)
    {
        UF_free(idealized_part_name);
    }

    if (scIdealizedPart_Directory != NULL)
    {
        UF_free(scIdealizedPart_Directory);
        scIdealizedPart_Directory = NULL;
    }

    if (scIdealizedPart_Directory_Tmp != NULL)
    {
        UF_free(scIdealizedPart_Directory_Tmp);
        scIdealizedPart_Directory_Tmp = NULL;
    }

    if (scFem_Directory != NULL)
    {
        UF_free(scFem_Directory);
        scFem_Directory = NULL;
    }

    if (scFem_Directory_Tmp != NULL)
    {
        UF_free(scFem_Directory_Tmp);
        scFem_Directory_Tmp = NULL;
    }

    if (description != NULL)
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
static int create_sim__with_name_from_part_name(tag_t         cad_part_tag,
    tag_t         fem_tag,
    UF_UG_BatchMesh_CommandLineOpts_t *pzBatchRunParams,
    tag_t         *new_sim_tag)
{
    int             iRc = 0;
    int             mem_error = 0;

    char            *sim_name = NULL;
    char            *simpathname = NULL;

    int             num_desc_lines = 1;
    char            *description = NULL;
    char            *scSim_Directory = NULL;
    char            *scSim_Directory_Tmp = NULL;
    char            scPartName[MAX_FSPEC_BUFSIZE];
    char            scPartDirectoryPath[MAX_FSPEC_BUFSIZE];

    char            scCurrentDirectory[MAX_FSPEC_BUFSIZE];

    /* Build name string for sim file */
    build_name_string(4, cad_part_tag, pzBatchRunParams, &sim_name);

    /* ==============================================
    Make sure sim file does not exist in OS.
    If exists delete the file.
    ============================================== */
    iRc = uc4560(sim_name, 0);
    if (iRc == 0)
    {
        /* File exists : So delete it from the system */
        iRc = uc4561(sim_name, 0);
        if (iRc != 0)
        {
            /* Could not delete the file : Error out */
            report_msg("Error : SIM file already exists\n");
            report_msg("        File name : "); report_msg(sim_name);
            report_msg("\n        Could not delete existing file.\n");
            return -9999;
        }
    }
    num_desc_lines = 1;
    description = (char*)UF_allocate_memory(10 * sizeof(char), &mem_error);
    if (mem_error != 0)
    {
        iRc = mem_error;
        return iRc;
    }
    strcpy(description, " ");

    iRc = uc4576(pzBatchRunParams->part_file_name, 2, scPartDirectoryPath,
        scPartName);
    if (strlen(scPartDirectoryPath))
    {

        /* uc4565 : Get current directory */
        uc4565(1, scCurrentDirectory);

        int iStrLen = (int)(strlen(scPartDirectoryPath) + strlen(sim_name) +
            strlen(scCurrentDirectory) + 20);
        scSim_Directory = (char*)UF_allocate_memory(iStrLen * sizeof(char),
            &mem_error);
        scSim_Directory_Tmp = (char*)UF_allocate_memory(iStrLen * sizeof(char),
            &mem_error);
        simpathname = (char*)UF_allocate_memory(iStrLen * sizeof(char),
            &mem_error);
        strcpy(scSim_Directory_Tmp, scPartDirectoryPath);

        iRc = uc4575(scSim_Directory_Tmp, 0, sim_name,
            scSim_Directory);
        strcpy(simpathname, scSim_Directory);
        iRc = uc4560(simpathname, 0);
        if (iRc == 0)
        {
            write_info_fprintf(true, UF_UG__BatchMesh_LOG, "WARNING : Deleting pre-existing file found with the same name. \n");
            /* File exists : So delete it from the system */
            iRc = uc4561(simpathname, 0);
            if (iRc != 0)
            {
                /* Could not delete the file : Error out */
                report_msg("Error : SIM file already exists\n");
                report_msg("        File name : "); report_msg(sim_name);
                report_msg("\n        Could not delete existing file.\n");
                write_info_fprintf(true, UF_UG__BatchMesh_LOG, "Error : Could not delete existing file. \n");
                return -9999;
            }
        }

        iRc = 0;
    }

    /* Create SIM */
    Session      *theSession = Session::GetSession();
    CAE::FemPart *workFemPart(dynamic_cast<CAE::FemPart *>(theSession->Parts()->BaseWork()));
    CAE::FemPart *displayFemPart(dynamic_cast<CAE::FemPart *>(theSession->Parts()->BaseDisplay()));
    CAE::FemPart *femPart1(dynamic_cast<CAE::FemPart *>(workFemPart));

    BasePart *basePart2;
    basePart2 = theSession->Parts()->NewBaseDisplay(simpathname, BasePart::UnitsMillimeters);

    CAE::SimPart *workSimPart(dynamic_cast<CAE::SimPart *>(theSession->Parts()->BaseWork()));
    CAE::SimPart *displaySimPart(dynamic_cast<CAE::SimPart *>(theSession->Parts()->BaseDisplay()));
    CAE::SimPart *simPart1(dynamic_cast<CAE::SimPart *>(workSimPart));
    std::vector<NXString> description2(0);
    simPart1->FinalizeCreation(femPart1, -1, description2);
    //theSession->Parts()->SetWork(femPart1);

    *new_sim_tag = simPart1->Tag();
    if (iRc != 0 || *new_sim_tag == NULL_TAG)
        iRc = -9999;

    /* End : Free up dynamic allocations */
    if (sim_name != NULL)
        UF_free(sim_name);

    if (description != NULL)
        UF_free(description);

    return iRc;

} /* create_sim__with_name_from_part_name */

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
static int create_jt__with_name_from_part_name(tag_t  tag_part_to_mesh, UF_UG_BatchMesh_CommandLineOpts_t *pzBatchRunParams, char** jtFilePath)
{
    int mem_error = 0; int iRc = 0;
    char* JT_MESH_file_Name = NULL;
    char  scPartName[MAX_FSPEC_BUFSIZE];
    char  scPartDirectoryPath[MAX_FSPEC_BUFSIZE];
    char  scCurrentDirectory[MAX_FSPEC_BUFSIZE];

    build_name_string(7, tag_part_to_mesh, pzBatchRunParams, &JT_MESH_file_Name);

    iRc = uc4576(pzBatchRunParams->part_file_name, 2, scPartDirectoryPath, scPartName);
    if (strlen(scPartDirectoryPath))
    {
        /* uc4565 : Get current directory */
        uc4565(1, scCurrentDirectory);

        int iStrLen = (int)(strlen(scPartDirectoryPath) + strlen(JT_MESH_file_Name) +
            strlen(scCurrentDirectory) + 20);
        char* scJT_Directory = (char*)UF_allocate_memory(iStrLen * sizeof(char),
            &mem_error);
        char* scJT_Directory_Tmp = (char*)UF_allocate_memory(iStrLen * sizeof(char),
            &mem_error);
        *jtFilePath = (char*)UF_allocate_memory(iStrLen * sizeof(char),
            &mem_error);
        strcpy(scJT_Directory_Tmp, scPartDirectoryPath);

        iRc = uc4575(scJT_Directory_Tmp, 0, JT_MESH_file_Name, scJT_Directory);
        strcpy(*jtFilePath, scJT_Directory);
        iRc = uc4560(*jtFilePath, 0);
        if (iRc == 0)
        {
            write_info_fprintf(true, UF_UG__BatchMesh_LOG, "WARNING : Deleting pre-existing file found with the same name. \n");
            /* File exists : So delete it from the system */
            iRc = uc4561(*jtFilePath, 0);
            if (iRc != 0)
            {
                /* Could not delete the file : Error out */
                report_msg("Error : FEM file already exists\n");
                report_msg("        File name : "); report_msg(JT_MESH_file_Name);
                report_msg("\n        Could not delete existing file.\n");
                write_info_fprintf(true, UF_UG__BatchMesh_LOG, "Error : Could not delete existing file. \n");
                return -9999;
            }
        }
        UF_free(scJT_Directory);
        UF_free(scJT_Directory_Tmp);
        scJT_Directory = NULL;
        scJT_Directory_Tmp = NULL;
        iRc = 0;
    }

    UF_free(JT_MESH_file_Name);
    JT_MESH_file_Name = NULL;
    
    return iRc;

} /* create_jt__with_name_from_part_name */
  /* ================================================
  Open/Close file to write out mesh report.
  * ================================================ */
static FILE *open_logfile(tag_t      cad_part_tag,
    UF_UG_BatchMesh_CommandLineOpts_t *pzBatchRunParams)
{
    FILE   *fp = NULL;
    char   *MeshReport_LOG_name = NULL;

    /* Build name string from cad part name */
    build_name_string(3, cad_part_tag, pzBatchRunParams, &MeshReport_LOG_name);

    /* Create a file by that name; over-write any existing file */
    if (MeshReport_LOG_name != NULL)
    {
        fp = fopen(MeshReport_LOG_name, "wt");
        if (fp == NULL)
        {
            report_msg("Error opening mesh report log file ");
            report_msg(MeshReport_LOG_name);
            report_msg("\n \n");
        }
    }

    if (MeshReport_LOG_name != NULL)
        UF_free(MeshReport_LOG_name);
    return fp;
}

static void close_logfile(FILE   *fp)
{
    if (fp != NULL)
        fclose(fp);

    return;
}

/* ======================================================================
This function builds name string from CAD part name. Options
are to build name of fem file, idealized part file and mesh
log file (see iNameOpt arguement).

iNameOpt         i - 0 => CAD part name
1 => Idealized part file name
2 => FEM file name
3 => Mesh info LOG file
4 => Sim file name
5 => Solution name
6 => Nastran blk data name
7 => JT file name

cad_part_tag     i - Tag of the CAD part

pzBatchRunParams   i - Use key words, extensions etc.

NameString       o - Output name string
======================================================================= */
static int build_name_string(int       iNameOpt,
    tag_t     cad_part_tag,
    UF_UG_BatchMesh_CommandLineOpts_t *pzBatchRunParams,
    char      **NameString)
{
    int             iRc = 0;
    int             mem_error = 0;

    char            cad_part_name[MAX_FSPEC_BUFSIZE] = { "" };
    char            cad_part_full_path[MAX_FSPEC_BUFSIZE] = { "" };
    const char      *Fem_Name_Prefix = "__FEM";
    const char      *Ideal_Name_Prefix = "__IDEALIZED";
    const char      *Sim_Name_Prefix = "__SIM";
    const char      *MeshReport_Suffix = "__MeshReport.LOG";
    char            NASTRAN_prefix[MAX_FSPEC_BUFSIZE] = { ' ' };
    const char      *SOLUTION_prefix = "SOLVER_DECK";
    const char      *JT_Name_Prefix = "__MESH_JT";

    char            RunKeyWord[MAX_FSPEC_BUFSIZE] = { ' ' };

    int             iExpectedStrLen = 0;

    char            *fem_name = NULL;
    char            *idealized_part_name = NULL;
    char            *sim_name = NULL;
    char            *solver_name = NULL;
    char            *jt_name = NULL;

    char            scDeckExtn[MAX_FSPEC_BUFSIZE] = { ' ' };


    /* Initialize */
    strcpy(RunKeyWord, "");
    strcpy(NASTRAN_prefix, "");
    strcpy(scDeckExtn, "");

    /* Copy keyword */
    strcpy(RunKeyWord, pzBatchRunParams->run_key_word);

    /* Query part name */
    iRc = UF_PART_ask_part_name(cad_part_tag, cad_part_full_path);
    iRc = uc4574(cad_part_full_path, 2, cad_part_name); /* Arguement 2 => file type is .prt file */

    if (iNameOpt == 0)
    {
        /* ====================
        CAD PART NAME
        ==================== */
        iExpectedStrLen = ((int)strlen(cad_part_name)) + 20;
        *NameString = (char*)UF_allocate_memory((iExpectedStrLen) * sizeof(char), &mem_error);
        if (mem_error != 0)
        {
            iRc = mem_error;
            return iRc;
        }
        strcpy(*NameString, cad_part_name);
    }
    else if (iNameOpt == 1)
    {
        /* ===========================
        IDEALIZED PART NAME
        ===========================  */
        /* Build idealized part name : "<Part_name>__IDEALIZED__<key word>" */
        iExpectedStrLen = (int)(strlen(cad_part_name) + strlen(Ideal_Name_Prefix) +
            strlen(RunKeyWord) + 20);
        idealized_part_name = (char*)UF_allocate_memory((iExpectedStrLen) * sizeof(char), &mem_error);
        if (mem_error != 0)
        {
            iRc = mem_error;
            return iRc;
        }
        strcpy(idealized_part_name, cad_part_name);
        strcat(idealized_part_name, Ideal_Name_Prefix);
        if (strcmp(RunKeyWord, ""))
        {
            strcat(idealized_part_name, "__");
            strcat(idealized_part_name, RunKeyWord);
        }
        strcat(idealized_part_name, ".prt");

        /* Output string */
        *NameString = (char*)UF_allocate_memory((iExpectedStrLen) * sizeof(char), &mem_error);
        if (mem_error != 0)
        {
            iRc = mem_error;
            return iRc;
        }
        strcpy(*NameString, idealized_part_name);
    }
    else if (iNameOpt == 2 || iNameOpt == 3)
    {

        /* Build FEM name : "<Part_name>__FEM__<keyword>.fem";
        MeshReport Log : "<Part_name>__FEM__<keyword>__MeshReport.LOG" */
        iExpectedStrLen = (int)(strlen(cad_part_name) + strlen(Fem_Name_Prefix) + strlen(MeshReport_Suffix)
            + strlen(RunKeyWord) + 20);
        fem_name = (char*)UF_allocate_memory((iExpectedStrLen) * sizeof(char), &mem_error);
        if (mem_error != 0)
        {
            iRc = mem_error;
            return iRc;
        }
        strcpy(fem_name, cad_part_name);
        strcat(fem_name, Fem_Name_Prefix);
        if (strcmp(RunKeyWord, ""))
        {
            strcat(fem_name, "__");
            strcat(fem_name, RunKeyWord);
        }
        if (iNameOpt == 2)
            strcat(fem_name, ".fem");
        else if (iNameOpt == 3)
            strcat(fem_name, MeshReport_Suffix);

        /* Output string */
        *NameString = (char*)UF_allocate_memory((iExpectedStrLen) * sizeof(char), &mem_error);
        if (mem_error != 0)
        {
            iRc = mem_error;
            return iRc;
        }
        strcpy(*NameString, fem_name);
    }
    else if (iNameOpt == 4)
    {
        /* Build Sim name : "<Part_name>__SIM__<keyword>.sim"; */
        iExpectedStrLen = (int)(strlen(cad_part_name) + strlen(Sim_Name_Prefix) +
            strlen(RunKeyWord) + 20);
        sim_name = (char*)UF_allocate_memory((iExpectedStrLen) * sizeof(char), &mem_error);
        if (mem_error != 0)
        {
            iRc = mem_error;
            return iRc;
        }
        strcpy(sim_name, cad_part_name);
        strcat(sim_name, Sim_Name_Prefix);
        if (strcmp(RunKeyWord, ""))
        {
            strcat(sim_name, "__");
            strcat(sim_name, RunKeyWord);
        }
        strcat(sim_name, ".sim");


        /* Output string */
        *NameString = (char*)UF_allocate_memory((iExpectedStrLen) * sizeof(char), &mem_error);
        if (mem_error != 0)
        {
            iRc = mem_error;
            return iRc;
        }
        strcpy(*NameString, sim_name);
    }
    else if (iNameOpt == 5 || iNameOpt == 6)
    {
        if (iNameOpt == 6)
        {
            /* Add extension to the name */
            if (!strlen(pzBatchRunParams->dat_file_extn))
            {
                /* Get extension for what ever solver user has set while runing batch
                meshing */
                UF_UG__BatchMesh_GetDefaultSolverDeckFileExtn(pzBatchRunParams->Solver_Name, \
                    scDeckExtn);

            }
            else
            {
                /* User has specified extension; use it */
                strcat(scDeckExtn, ".");
                strcat(scDeckExtn, pzBatchRunParams->dat_file_extn);
            }
        }
        else
            strcpy(scDeckExtn, "");

        /* Build nastran bulk data name : "<Part_name>__<Solver name>__<Keyword>"; */
        UF_UG__BatchMesh_GetSolverDeckName(pzBatchRunParams->Solver_Name, NASTRAN_prefix);
        iExpectedStrLen = (int)(strlen(cad_part_name) + strlen(NASTRAN_prefix) + strlen(RunKeyWord) +
            strlen(scDeckExtn) + 20);
        solver_name = (char*)UF_allocate_memory((iExpectedStrLen) * sizeof(char), &mem_error);
        if (mem_error != 0)
        {
            iRc = mem_error;
            return iRc;
        }

        if (iNameOpt == 6)
        {

            strcpy(solver_name, cad_part_name);
            strcat(solver_name, "__");
            strcat(solver_name, NASTRAN_prefix);
            if (strcmp(RunKeyWord, ""))
            {
                strcat(solver_name, "__");
                strcat(solver_name, RunKeyWord);
            }
            strcat(solver_name, scDeckExtn);
        }
        else
        {
            /* Name option is 5 solver name */
            //////
            ///  A Note: The UF routine that creates solution 
            ///  automatically appends simulation name to the
            ///  solution name.  That string becomes very long
            ///  So for solution name we keep the string small
            strcpy(solver_name, SOLUTION_prefix);
        }


        /* Output string */
        *NameString = (char*)UF_allocate_memory((iExpectedStrLen) * sizeof(char), &mem_error);
        if (mem_error != 0)
        {
            iRc = mem_error;
            return iRc;
        }
        strcpy(*NameString, solver_name);

    }
    else if (iNameOpt == 7)
    {

        /* Build JT file name : "<Part_name>__FEM_JT__<keyword>.fem" */
        iExpectedStrLen = (int)(strlen(cad_part_name) + strlen(Fem_Name_Prefix) + strlen(MeshReport_Suffix)
            + strlen(RunKeyWord) + 20);
        jt_name = (char*)UF_allocate_memory((iExpectedStrLen) * sizeof(char), &mem_error);
        if (mem_error != 0)
        {
            iRc = mem_error;
            return iRc;
        }
        strcpy(jt_name, cad_part_name);
        strcat(jt_name, JT_Name_Prefix);
        if (strcmp(RunKeyWord, ""))
        {
            strcat(jt_name, "__");
            strcat(jt_name, RunKeyWord);
        }

        strcat(jt_name, ".jt");

        /* Output string */
        *NameString = (char*)UF_allocate_memory((iExpectedStrLen) * sizeof(char), &mem_error);
        if (mem_error != 0)
        {
            iRc = mem_error;
            return iRc;
        }
        strcpy(*NameString, jt_name);
    }



    /* End : Free up dynamic allocations */
    if (fem_name != NULL)
        UF_free(fem_name);

    if (sim_name != NULL)
        UF_free(sim_name);

    if (solver_name != NULL)
        UF_free(solver_name);

    if (idealized_part_name != NULL)
        UF_free(idealized_part_name);

    if (jt_name != NULL)
        UF_free(jt_name);


    return iRc;
} /* build_name_string */

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

    char     command_help[MAX_FSPEC_BUFSIZE] = { "" },      /* Command help */
        fspec_buffer[MAX_FSPEC_BUFSIZE] = { "" };


    /* Initi output */
    *pfDisplayCommandHelp = false;

    /* Initialize output structure */
    UF_UG__BatchMesh_INITBatchParams(pzBatchRunParams);

    /* Parse command line arguements */
    UF_CALL(uc4624(0, argc, argv));

    /* Get the key-word for the run */
    if (uc4620(UF_UG_BATCH_MESH__PARM_key_word, fspec_buffer) <= 0)
    {
        strcpy(pzBatchRunParams->run_key_word, "");
    }
    else
    {
        strcpy(pzBatchRunParams->run_key_word, fspec_buffer);
    }

    /* Part file name */
    if (uc4620(UF_UG_BATCH_MESH__PARM_input_part, fspec_buffer) <= 0)
    {
        pzBatchRunParams->fPartFile = false;
        strcpy(pzBatchRunParams->part_file_name, "");
    }
    else
    {
        pzBatchRunParams->fPartFile = true;
        strcpy(pzBatchRunParams->part_file_name, fspec_buffer);
    }

    /*Template Name */
    if (uc4620(UF_UG_BATCH_MESH__PARM_template_file, fspec_buffer) <= 0)
    {
        pzBatchRunParams->fTemplateFile = false;
        strcpy(pzBatchRunParams->template_file_name, "");
    }
    else
    {
        pzBatchRunParams->fTemplateFile = true;
        strcpy(pzBatchRunParams->template_file_name, fspec_buffer);
    }


    /* Output option : Whether to create idealized part */
    if (uc4620(UF_UG_BATCH_MESH__PARM_idealize_output, fspec_buffer) <= 0)
        pzBatchRunParams->fOutIdealized = true;
    else
        pzBatchRunParams->fOutIdealized = false;

    /* Output option : Whether to save fem file */
    if (uc4620(UF_UG_BATCH_MESH__PARM_fem_output, fspec_buffer) <= 0)
        pzBatchRunParams->fOutputFEM = false;
    else
        pzBatchRunParams->fOutputFEM = true;

    /* Output option : Whether to save jt file or not */
    if (uc4620(UF_UG_BATCH_MESH__PARM_jt_output, fspec_buffer) <= 0)
        pzBatchRunParams->fOutputJT = false;
    else
        pzBatchRunParams->fOutputJT = true;

    /* Output option : Whether to save nastran bulk data or not */
    if (uc4620(UF_UG_BATCH_MESH__PARM_nastran_output, fspec_buffer) <= 0)
    {
        pzBatchRunParams->fOutputDAT = false;
        strcpy(pzBatchRunParams->dat_file_extn, "");
    }
    else
    {
        pzBatchRunParams->fOutputDAT = true;
        strcpy(pzBatchRunParams->dat_file_extn, fspec_buffer);
    }

    /* Check if help dump is desired */
    if ((uc4620(UF_UG_BATCH_MESH__PARM_help_str1, command_help)>0) ||
        (uc4620(UF_UG_BATCH_MESH__PARM_help_str2, command_help)>0) ||
        (uc4620(UF_UG_BATCH_MESH__PARM_help_str3, command_help)>0))
    {
        *pfDisplayCommandHelp = true;
    }


    return;
}

/* ==================================
Convert string to lower case
==================================  */
static void upper_to_lower_case(char *scString)
{
    int i = 0, ichar = 0, nchar = 0;

    nchar = (int)strlen(scString);

    for (i = 0; i<nchar; i++)
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


    if (fToConsole)
    {
#if UF_UG_BATCH_MESH__SCREEN_DUMP_ON
        /* ====== #define flag ====== */
        va_start(variable_list, format_string);
        vprintf(format_string, variable_list);
        va_end(variable_list);
#endif
    }
    if (fp != NULL)
    {
        va_start(variable_list, format_string);
        vfprintf(fp, format_string, variable_list);
        va_end(variable_list);
    }

    if (fp != NULL)
        fflush(fp);
}

/* Display the help on command to user */
static void display_command_help(const char *scHelpText[])
{
    int   iLinesPrinted = 0;
    int   nMaxLines = 1000;
    while (!(!strcmp(scHelpText[iLinesPrinted], "END_HELP")))
    {
        printf("   %s \n", scHelpText[iLinesPrinted]);

        /* Sanity check */
        iLinesPrinted++;
        if (iLinesPrinted>nMaxLines)
            break;
    }

    printf("  \n\n");
    return;
}

void start_batchmesher_logger(tag_t tag_part_to_mesh,
    UF_UG_BatchMesh_CommandLineOpts_t *pzBatchRunParams)
{
    UF_UG__BatchMesh_LOG = open_logfile(tag_part_to_mesh, pzBatchRunParams);
    if (UF_UG__BatchMesh_LOG == NULL)
    {
        /* Error in creating log file */
        report_msg("Error opening mesh report log file .");
        write_info_fprintf(true, NULL, "Error opening mesh report log file .\n");
        UF_UG__BatchMesh_LOG = NULL;
    }

    /* Report info */
    write_info_fprintf(true, UF_UG__BatchMesh_LOG,
        "===================================================\n");
    write_info_fprintf(true, UF_UG__BatchMesh_LOG,
        "               BATCH MESH generation  \n");
    write_info_fprintf(true, UF_UG__BatchMesh_LOG,
        "===================================================\n");
    write_info_fprintf(true, UF_UG__BatchMesh_LOG, "\n\n");
}
void log_user_system_info(UF_system_info_t zSystemInfo)
{
    /* Get some system info : Date time user etc... */
    UF_ask_system_info(&zSystemInfo);

    /* Dump system info into log file */
    write_info_fprintf(true, UF_UG__BatchMesh_LOG, "System/Session Info    \n");
    write_info_fprintf(true, UF_UG__BatchMesh_LOG, "=================== \n");
    if (zSystemInfo.date_buf != NULL)
        write_info_fprintf(true, UF_UG__BatchMesh_LOG, "   Date & Time : %s \n", zSystemInfo.date_buf);
    else
        write_info_fprintf(true, UF_UG__BatchMesh_LOG, "   Date & Time : ---- \n");

    if (zSystemInfo.user_name != NULL)
        write_info_fprintf(true, UF_UG__BatchMesh_LOG, "   User Name : %s \n", zSystemInfo.user_name);
    else
        write_info_fprintf(true, UF_UG__BatchMesh_LOG, "   User Name : ---- \n");

    if (zSystemInfo.node_name != NULL)
        write_info_fprintf(true, UF_UG__BatchMesh_LOG, "   Machine Name : %s \n", zSystemInfo.node_name);
    else
        write_info_fprintf(true, UF_UG__BatchMesh_LOG, "   Machine Name : ---- \n");

    if (zSystemInfo.machine_type != NULL)
        write_info_fprintf(true, UF_UG__BatchMesh_LOG, "   Machine Type : %s \n", zSystemInfo.machine_type);
    else
        write_info_fprintf(true, UF_UG__BatchMesh_LOG, "   Machine Name : ---- \n");

    if (zSystemInfo.os_name != NULL)
        write_info_fprintf(true, UF_UG__BatchMesh_LOG, "   OS : %s [Version: %s]\n",
            zSystemInfo.os_name, zSystemInfo.os_version);
    else
        write_info_fprintf(true, UF_UG__BatchMesh_LOG, "   OS : ---- \n");
    write_info_fprintf(true, UF_UG__BatchMesh_LOG, "\n\n");

    UF_free_system_info(&zSystemInfo);
}
static void STOP_CLOCK(int          start_end_flag,
    UF_timer_p_t pztimer,
    char         *scMessage)
{


    UF_timer_values_t     zTime_values;
    int                   Hour = 0;
    int                   Min = 0;
    double                dSec = 0.0;

    if (start_end_flag == UF_UG_BATCH_MESH__start_watch)
    {
        /* Start the clock */
        UF_begin_timer(pztimer);

    }
    else if (start_end_flag == UF_UG_BATCH_MESH__stop_watch)
    {
        /* End clock and print time */
        UF_end_timer(*pztimer, &zTime_values);

        /* Convert secs into hr:min:sec */
        Time_Sec_to_hr_min_sec(zTime_values.cpu_time, &Hour, &Min, &dSec);


        /* Append the messages */
        write_info_fprintf(true, UF_UG__BatchMesh_LOG, scMessage);
        if (Hour>0)
            write_info_fprintf(true, UF_UG__BatchMesh_LOG,
                ":: %d hrs : %d min : %g sec", Hour, Min, dSec);
        else if (Min>0)
            write_info_fprintf(true, UF_UG__BatchMesh_LOG,
                ":: %d min : %g sec", Min, dSec);
        else
            write_info_fprintf(true, UF_UG__BatchMesh_LOG,
                "::  %g sec", dSec);


    }

} /* STOP_CLOCK */


static void Time_Sec_to_hr_min_sec(double dTimeSec, int *Hour, int *Min, double *dSec)
{
    double    dMinutes = 0.0, IntMins = 0.0;
    double    dHours = 0.0, IntHrs = 0.0;

    dMinutes = dTimeSec / 60;
    dHours = dMinutes / 60;
    dMinutes = modf(dHours, &IntHrs);
    *Hour = (int)IntHrs;

    dMinutes *= 60;
    *dSec = modf(dMinutes, &IntMins);
    *Min = (int)IntMins;

    (*dSec) *= 60;

}

void log_pre_processing_info(int nCAEBodies, tag_t tag_part_to_mesh,
    UF_UG_BatchMesh_CommandLineOpts_t *pzBatchRunParams)
{
    /* ===============
    Report info
    =============== */
    char                           *CAD_Part_Name = NULL;
    char                           *FEM_file_Name = NULL;
    char                           *SIM_file_Name = NULL;
    char                           *IDEALIZED_file_Name = NULL;
    char                           *SOLVER_file_Name = NULL;
    //char                           *MESH_LOG_file_Name = NULL;
    char                           *JT_MESH_file_Name = NULL;
    char                           *jt_file_path_name = NULL;

    write_info_fprintf(true, UF_UG__BatchMesh_LOG, " \n\n");

    /* Info on part */
    build_name_string(0, tag_part_to_mesh, pzBatchRunParams, &CAD_Part_Name);
    write_info_fprintf(true, UF_UG__BatchMesh_LOG, "Part name: %s (Part Tag = %u) \n",
        CAD_Part_Name, tag_part_to_mesh, nCAEBodies);
    write_info_fprintf(true, UF_UG__BatchMesh_LOG, "Total No of Bodies : %d \n\n",
        nCAEBodies);

    /* Files saved */
    write_info_fprintf(true, UF_UG__BatchMesh_LOG, " \n");
    write_info_fprintf(true, UF_UG__BatchMesh_LOG, "Files To Be Saved \n");
    write_info_fprintf(true, UF_UG__BatchMesh_LOG, "================= \n");

    /* Key-word */
    if (strlen(pzBatchRunParams->run_key_word))
    {
        write_info_fprintf(true, UF_UG__BatchMesh_LOG, "\tKey-word for file names: %s \n",
            pzBatchRunParams->run_key_word);
    }
    else
    {
        write_info_fprintf(true, UF_UG__BatchMesh_LOG, "\tKey-word for file names: None specified\n");
    }

    /* Idealized part option */
    if (pzBatchRunParams->fOutIdealized == (int)true)
    {
        build_name_string(1, tag_part_to_mesh, pzBatchRunParams, &IDEALIZED_file_Name);
        write_info_fprintf(true, UF_UG__BatchMesh_LOG, "\tIDEALIZED Part: %s \n",
            IDEALIZED_file_Name);

        if (IDEALIZED_file_Name != NULL)
        {
            UF_free(IDEALIZED_file_Name);
            IDEALIZED_file_Name = NULL;
        }
    }
    else
    {
        write_info_fprintf(true, UF_UG__BatchMesh_LOG, "\tIDEALIZED Part: No idealized part option specified\n");
    }

    /* Info. on fem  */
    if (pzBatchRunParams->fOutputFEM == (int)true)
    {
        build_name_string(2, tag_part_to_mesh, pzBatchRunParams, &FEM_file_Name);
        write_info_fprintf(true, UF_UG__BatchMesh_LOG, "\tFEM file: %s \n",
            FEM_file_Name);

        if (FEM_file_Name != NULL)
        {
            UF_free(FEM_file_Name);
            FEM_file_Name = NULL;
        }

        
    }
    else
    {
        write_info_fprintf(true, UF_UG__BatchMesh_LOG, "\tFEM file: No .fem option specified\n");
    }


    /* Info on sim and Solver deck */
    if (pzBatchRunParams->fOutputDAT == (int)true && isSolverSupported(pzBatchRunParams->Solver_Name))
    {
        build_name_string(6, tag_part_to_mesh, pzBatchRunParams, &SOLVER_file_Name);
        write_info_fprintf(true, UF_UG__BatchMesh_LOG, "\tSOLVER Deck: %s \n",
            SOLVER_file_Name);

        if (SOLVER_file_Name != NULL)
        {
            UF_free(SOLVER_file_Name);
            SOLVER_file_Name = NULL;
        }

        build_name_string(4, tag_part_to_mesh, pzBatchRunParams, &SIM_file_Name);
        write_info_fprintf(true, UF_UG__BatchMesh_LOG, "\tSIM file: %s \n",
            SIM_file_Name);

        if (SIM_file_Name != NULL)
        {
            UF_free(SIM_file_Name);
            SIM_file_Name = NULL;
        }
    }
    else
    {
        write_info_fprintf(true, UF_UG__BatchMesh_LOG, "\tSOLVER Deck: No solver deck & Sim options are  specified or Unsupported solver\n");
    }


    /* JT file from mesh */
    if (pzBatchRunParams->fOutputJT == (int)true)
    {

        build_name_string(7, tag_part_to_mesh, pzBatchRunParams, &JT_MESH_file_Name);
        write_info_fprintf(true, UF_UG__BatchMesh_LOG, "\tJT from mesh: %s \n",
            JT_MESH_file_Name);

        if (JT_MESH_file_Name != NULL)
        {
            UF_free(JT_MESH_file_Name);
            SOLVER_file_Name = NULL;
        }
    }
    else
    {
        write_info_fprintf(true, UF_UG__BatchMesh_LOG, "\tJT from mesh: No JT from mesh option specified\n");
    }


    /* Mesh log file */
    build_name_string(3, tag_part_to_mesh, pzBatchRunParams, &MESH_LOG_file_Name);
    write_info_fprintf(true, UF_UG__BatchMesh_LOG, "\tMESH Log file: %s \n",
        MESH_LOG_file_Name);

  
}

/* ===========================================================
This function runs mesh quality check and writes mesh
quality report.

scMeshType                i - TET_4,TET10, TRI_3, TRI_6, QUAD4
QUAD_8

mesh_tag                  i - Mesh tag

=========================================================== */
static int write_mesh_quality_report( CAE::Mesh *                        mesh)
{

    int                         iRc = 0;
    int                         iNumNodes = 0, iNumElements = 0;
    tag_t mesh_tag = mesh->Tag();
    const char                  *output_file_with_path = "MY_file.txt";
    

    write_info_fprintf(true, UF_UG__BatchMesh_LOG, " \n\n");
    write_info_fprintf(true, UF_UG__BatchMesh_LOG, "Element Quality Statistics \n");
    write_info_fprintf(true, UF_UG__BatchMesh_LOG, "========================== \n");

      /* Run the element shape check */
    iRc = UF_SF_check_model_element_shapes(1, &mesh_tag, false, output_file_with_path,
        UF_UG__BatchMesh_LOG);


    write_info_fprintf(true, UF_UG__BatchMesh_LOG, " \n\n");
    write_info_fprintf(true, UF_UG__BatchMesh_LOG, "Mesh Validation Info: \n");
    write_info_fprintf(true, UF_UG__BatchMesh_LOG, "===================== \n");
    iRc = validate_meshes(1, &mesh_tag, UF_UG__BatchMesh_LOG);



    return iRc;
} /* End of write_mesh_quality_report */

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
    int                           return_status = 0,
        num_total_errors = 0;
    UF_SF_mesh_error_container_t  error_container;

    UF_SF_init_mshvld_error_container(&error_container);


    return_status = UF_SF_validate_meshes(meshes_p,
        num_meshes,
        UF_SF_VALIDATE_MESH_ALL,
        &error_container);

    num_total_errors =
        error_container.mesh_asso_error_list.num_mesh_errors +
        error_container.elem_asso_error_list.num_mesh_errors +
        error_container.node_asso_error_list.num_mesh_errors +
        error_container.mesh_recipe_error_list.num_mesh_errors +
        error_container.geom_constraint_error_list.num_mesh_errors +
        error_container.user_attribute_error_list.num_mesh_errors;

    if (return_status !=0 || num_total_errors > 0)
    {
        write_info_fprintf(true, UF_UG__BatchMesh_LOG, "   Errors found while validating mesh\n\n");

        return_status = 1;
    }
    else
    {
        write_info_fprintf(true, UF_UG__BatchMesh_LOG, "   Mesh Validation successful.\n\n");
    }

    if (return_status == 1)
    {
        UF_SF_clean_mshvld_error_container(&error_container);
    }

    return return_status;
}

static bool isSolverSupported(const char* solverName)
{
    bool retVal = true;
    //Not all solvers are supported
    std::set <std::string> solverSet = { "MSC NASTRAN","NX NASTRAN","SAMCEF","NX NASTRAN DESIGN","ANSYS","ABAQUS","LSDYNA","IDEAS UNV" };
    std::string str(solverName);
    std::set <std::string>::iterator it = solverSet.find(str);

    if (it == solverSet.end())
        retVal = false;

    return retVal;
}
