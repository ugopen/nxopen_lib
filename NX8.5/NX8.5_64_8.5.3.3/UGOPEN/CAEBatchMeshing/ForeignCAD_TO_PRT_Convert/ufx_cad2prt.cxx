/*****************************************************************************
**
** ufx_cad2prt.cpp
**
** Description:
**    Main file for the application.
**
** Usage: From the command line (d:i:o:r:u:h)
** printf("usage: -i input_file_name -o output_part_file_name -u in|mm (ps only) -t iges|ps|step|jt|catia|xpk\n");
**
** Input files can be of the folling formats:
** iges -   IGES files
** ps   -   Parasolid files, .x_t
** step -   Step files
** jt   -   JT files
** catia    Catia files
** xpk  -   I-DEAS package files
**
** Output files will be an NX part
**
**  Note:
**      File name MUST be full path.
**      Units only needed for Parasolid processing
**
*
* =======================================================================
*  Revision History
* =======================================================================
*    Date          Name                 Description of Change
*    ----          ----                 ---------------------
* 20-Feb-2006    David Pinella      Initial creation (cms put by Ashish Das)
* 23-Feb-2006    Ashish Das         Fixed compile problems on unix with main returning
*                                   void.  All local functions made static. Renamed
*                                   getopts to get_cmdline_opts
* 08-Mar-2006    Ashish Das         Brought into nx5 from nx401.
* 17-Mar-2006    Ashish Das         Fix for PR 5417441 : cad2prt.exe crashes while saving
*                                   part if the output part already exists.
* 17-Apr-2008    Ashish Das         PR 5882980 : NX5032 exception thrown from UF_MODL_ask_list_count
*                                   when disjoint_list==NULL (i.e, when no disjoint sheet body remain)
* 05-Mar-2010 Keith Jaskot          Updated to gcc/g++ 4.3.2 for NX8, added <cstdlib>
* 21-Apr-2011    Jack Marr          First arg to main should be typed int, not char
* 21-Apr-2011    Jack Marr          Remove unnecessary headers
* 10-Jul-2012    Ashish Das         PR  6591078; Bad entity in call to es7010_no_occ from ugnx_cad2prt.exe 
*
**
*$HISTORY$
**
*****************************************************************************/

/* ============================
        Includes needed
   ============================ */
#include <stdio.h>
#include <time.h>
#include <string.h>
#include <stdarg.h>
#include <cstdlib>

#include <uf.h>
#include <uf_ps.h>
#include <uf_defs.h>
#include <uf_part.h>
#include <uf_assem.h>
#include <uf_mdlcmp.h>
#include <uf_obj.h>
#include <uf_object_types.h>
#include <NXOpen/Session.hxx>
#include <NXOpen/PartSaveStatus.hxx>
#include <NXOpen/Session.hxx>
#include <NXOpen/PartCollection.hxx>
#include <NXOpen/BasePart.hxx>
using namespace NXOpen;

/* ==========================================
                  Defines
   ========================================== */
//#define UF_UG_BATCH_MESH__SCREEN_DUMP_ON 1
//#define UF_UG_BATCH_MESH__MAX_NAME_LEN 256
//#define UF_CALL(X) (report_error( __FILE__, __LINE__, #X, (X)))
#define  cad2prt__MAX_NAME_LEN 256


/* ==========================================
       Typedef's valid for this file
   ========================================== */


/* ==========================================
           Local function prototypes
   ========================================== */
static int processParasolidPart(Session *theSession, char *fileIn, char *fileOut, int unitsType);
static int processIGESPart(Session *theSession, char *fileIn, char *fileOut);
static int processSTEPPart(Session *theSession, char *fileIn, char *fileOut);
static int processJTPart(Session *theSession, char *fileIn, char *fileOut);
static int processCATIAPart(Session *theSession, char *fileIn, char *fileOut);
static int processXPKPart(Session *theSession, char *fileIn, char *fileOut);
static int processProEPart(Session *theSession, char *fileIn, char *fileOut);

static int getNumberOfBodies(tag_t partTag);
static tag_t sewSheetBodies(tag_t partTag);
static void dumpPartSummary(tag_t partTag);
static void extractSheetBodies(tag_t partTag);
static int getNumberOfObjects(tag_t partTag, int objType);
static int get_cmdline_opts(int argc, char *argv[], char *opt);

static int remove_existing_output_part_file (char *scOutputPart);

/* ==========================================
           Global data 
   ========================================== */
char *optarg;
int  optind = 1;
int  opterr = 1;
int  optopt;

/* Main routine */
extern int main( int argc, char *argv[] )
{
    tag_t               part_tag = NULL_TAG;
    tag_t               *saved_part_tags = NULL;
    int                 *error_list = NULL;
    int                 result, unitsType=1, cadType=8;
    char                fileIn[2048];
    char                fileOut[2048];

    Session             *theSession;

    int                 c;
    //extern char       *optarg;
    //extern int        optind, opterr, optopt;

    /* Loop over command line arguements */

    while ((c = get_cmdline_opts((int)argc, argv, "i:o:t:u:h")) != EOF)
      {
        if (c == (int)'i') {
            strcpy(fileIn, optarg);
        } 
        if (c == (int)'o') {
            strcpy(fileOut, optarg);
        }
        if (c == (int)'u') {
            if (!strcmp(optarg, "mm")) unitsType = 1;
            if (!strcmp(optarg, "in")) unitsType = 2;
        }
          if (c == (int)'t') {

              if (!strcmp(optarg, "ug")) cadType = 1;
              if (!strcmp(optarg, "ps")) cadType = 2;
              if (!strcmp(optarg, "iges")) cadType = 3;
              if (!strcmp(optarg, "step")) cadType = 4;
              if (!strcmp(optarg, "jt")) cadType = 5;
              if (!strcmp(optarg, "catia")) cadType = 6;
              if (!strcmp(optarg, "xpk")) cadType = 7;
              //if (!strcmp(optarg, "proe")) cadType = 8;
          }
          if (c == (int)'h') {
              printf("usage: -i input_file_name -o output_part_file_name -u in|mm (ps only) -t iges|ps|step|jt|catia|xpk\n");
              //printf("usage: -i input_file_name -o output_part_file_name -u in|mm (ps only) -t iges|ps|step|jt|catia|xpk|proe\n");
              return 0;
          }
      }
      printf("fileIn: %s\n", fileIn);
      printf("fileOut: %s\n", fileOut);
      printf("Units: %d\n", unitsType);
      printf("CadType: %d\n", cadType);

      // Skip if UG

      if (cadType == 1) 
      {
          printf("Skipping UG processing for UG file (processing not needed, native format)\n");
          return 0;
      }

        /* Initialize the API environment */
    if( UF_initialize() ) 
    {
        /* Failed to initialize */
        printf("Error: Could not initialize UGNX API environment...\n");
        return 0;
    }
    theSession = Session::GetSession();

  //
  // Delete potentially existing prt. file 
  //
  remove_existing_output_part_file (fileOut);

  // ----------------------------------------------
  //   Process if Parasolid
  // ----------------------------------------------
  if (cadType == 2)
  {
    printf("...Processing Parasolid file\n");
    result = processParasolidPart(theSession, fileIn, fileOut, unitsType);
  }

  // ----------------------------------------------
  //   Process if IGES
  // ----------------------------------------------
  else if (cadType == 3)
  {
    printf("...Processing IGES file\n");
    result = processIGESPart(theSession, fileIn, fileOut);
  }

  // ----------------------------------------------
  //   Process if STEP
  // ----------------------------------------------
  else if (cadType == 4)
  {
    printf("...Processing STEP file\n");
    result = processSTEPPart(theSession, fileIn, fileOut);
  }

  // ----------------------------------------------
  //   Process if JT
  // ----------------------------------------------
  else if (cadType == 5)
  {
    printf("...Processing JT file\n");
    result = processJTPart(theSession, fileIn, fileOut);
  }

  // ----------------------------------------------
  //   Process if CATIA
  // ----------------------------------------------
  else if (cadType == 6)
  {
    printf("...Processing CATIA file\n");
    result = processCATIAPart(theSession, fileIn, fileOut);
  }

  // ----------------------------------------------
  //   Process if XPK
  // ----------------------------------------------
  else if (cadType == 7)
  {
    printf("...Processing XPK file\n");
    result = processXPKPart(theSession, fileIn, fileOut);
  }

  // ----------------------------------------------
  //   Process if Pro E
  // ----------------------------------------------
  //else if (cadType == 8)
  //{
    //printf("...Processing Pro E file\n");
    //result = processProEPart(theSession, fileIn, fileOut);
  //}

  // ----------------------------------------------
  //   Unknown part option
  // ----------------------------------------------
  else {
    printf("Unknown CAD type selected...\n");
  }

  // ----------------------------------------------
  //   Menu: Tools->Journal->Stop
  // ----------------------------------------------

    /* Terminate the API environment */
    UF_terminate();

    printf("...Ending UGReadCAD processing...\n");
    return 0;
}

/*****************************************************************************
**  Utilities
*****************************************************************************/

  /* ==========================================
           Parasolid Processing
   ========================================== */
static int processParasolidPart(Session *theSession, char *fileIn, char *fileOut, int unitsType)
{
    int            result;
    char        message[133];

    // ----------------------------------------------
    //   Menu: File->New...
    // ----------------------------------------------
    BasePart *basePart1;
    if (unitsType == 1) basePart1 = theSession->Parts()->NewBaseDisplay(fileOut, BasePart::UnitsMillimeters);
    if (unitsType == 2) basePart1 = theSession->Parts()->NewBaseDisplay(fileOut, BasePart::UnitsInches);
    
    Part *workPart(theSession->Parts()->Work());

    // ----------------------------------------------
    //   Import ParaSolid file
    // ----------------------------------------------
 
    uf_list_p_t body;
    result = UF_PS_import_data (fileIn, &body );

    UF_get_fail_message(result, message);
    printf("Status: %d - %s, File: %s\n", result, message, fileIn);

    // ----------------------------------------------
    //   Menu: File->Save
    // ----------------------------------------------

    PartSaveStatus *partSaveStatus1;
    partSaveStatus1 = workPart->Save(BasePart::SaveComponentsTrue, BasePart::CloseAfterSaveFalse);
    delete partSaveStatus1;

    return(0);
}

/* ==========================================
           IGES Processing
   ========================================== */
static int processIGESPart(Session *theSession, char *fileIn, char *fileOut)
{
    int                        result, numParts ;
    tag_t                    partTag;
    tag_t                    sew_id;

    // ----------------------------------------------
    //   Menu: File->New...
    // ----------------------------------------------

    BasePart *basePart1;
    PartLoadStatus *partLoadStatus1;
    basePart1 = theSession->Parts()->OpenBaseDisplay(fileIn, &partLoadStatus1);
    delete partLoadStatus1;
 
    Part *workPart(theSession->Parts()->Work());

    // ----------------------------------------------
    //   Menu: File->SaveAs
    // ----------------------------------------------

    PartSaveStatus *partSaveStatus1;
    partSaveStatus1 = workPart->SaveAs(fileOut);
    delete partSaveStatus1;

    numParts = UF_PART_ask_num_parts ( );
    partTag = workPart->Tag();

    // ----------------------------------------------
    //   Sew the part
    // ----------------------------------------------

    result = getNumberOfBodies(partTag);
    printf("numBodies = %d\n", result);
    sew_id = sewSheetBodies(partTag);

    // ----------------------------------------------
    //   Menu: File->Save
    // ----------------------------------------------

    partSaveStatus1 = workPart->Save(BasePart::SaveComponentsTrue, BasePart::CloseAfterSaveFalse);
    delete partSaveStatus1;

    return(0);
}

/* ==========================================
           STEP Processing
   ========================================== */
static int processSTEPPart(Session *theSession, char *fileIn, char *fileOut)
{
    // ----------------------------------------------
    //   Menu: File->New...
    // ----------------------------------------------
    BasePart *basePart1;
    PartLoadStatus *partLoadStatus1;
    basePart1 = theSession->Parts()->OpenBaseDisplay(fileIn, &partLoadStatus1);

    delete partLoadStatus1;
  
    Part *workPart(theSession->Parts()->Work());

    // ----------------------------------------------
    //   Menu: File->SaveAs
    // ----------------------------------------------

    PartSaveStatus *partSaveStatus1;
    partSaveStatus1 = workPart->SaveAs(fileOut);
    delete partSaveStatus1;

    return(0);
}

/* ==========================================
           JT Processing
   ========================================== */
static int processJTPart(Session *theSession, char *fileIn, char *fileOut)
{
    int                        result, numBodies, numParts;
    tag_t                    partTag, sew_id;
    char                    message[133];

    // ----------------------------------------------
    //   Menu: File->New...
    // ----------------------------------------------
    BasePart *basePart1;
    PartLoadStatus *partLoadStatus1;
    basePart1 = theSession->Parts()->OpenBaseDisplay(fileIn, &partLoadStatus1);

    delete partLoadStatus1;
  
    Part *workPart(theSession->Parts()->Work());

    partTag = workPart->Tag();

    // ----------------------------------------------
    //   Extract the precise
    // ----------------------------------------------

    result = UF_PART_update_jt_brep(partTag);
    UF_get_fail_message(result, message);
    printf("Result of brep extract = %d, Msg=%s\n", result, message);

    // ----------------------------------------------
    //   Sew
    // ----------------------------------------------

    numBodies = getNumberOfBodies(partTag);
    printf("numBodies = %d\n", numBodies);

    // If only 1 body then we have to extract the sheet bodies first

    if (numBodies == 1) 
    {
        dumpPartSummary(partTag);
        extractSheetBodies(partTag);
        dumpPartSummary(partTag);
        numBodies = getNumberOfBodies(partTag);
        printf("numBodies(2) = %d\n", numBodies);
    }
    if (numBodies > 1) sew_id = sewSheetBodies(partTag);
    numBodies = getNumberOfBodies(partTag);
    printf("numBodies(3) = %d\n", numBodies);
    dumpPartSummary(partTag);

    numParts = UF_PART_ask_num_parts ( );
    printf("numParts = %d\n", numParts);

    // ----------------------------------------------
    //   Menu: File->SaveAs
    // ----------------------------------------------

    PartSaveStatus *partSaveStatus1;
    partSaveStatus1 = workPart->SaveAs(fileOut);
    delete partSaveStatus1;

    return(0);
}

/* ==========================================
           CATIA Processing
   ========================================== */
static int processCATIAPart(Session *theSession, char *fileIn, char *fileOut)
{
    // ----------------------------------------------
    //   Menu: File->New...
    // ----------------------------------------------
    BasePart *basePart1;
    PartLoadStatus *partLoadStatus1;
    basePart1 = theSession->Parts()->OpenBaseDisplay(fileIn, &partLoadStatus1);
    delete partLoadStatus1;
  
    Part *workPart(theSession->Parts()->Work());

    // ----------------------------------------------
    //   Menu: File->SaveAs
    // ----------------------------------------------

    PartSaveStatus *partSaveStatus1;
    partSaveStatus1 = workPart->SaveAs(fileOut);
    delete partSaveStatus1;

    return(0);
}

/* ==========================================
           XPK Processing
   ========================================== */
static int processXPKPart(Session *theSession, char *fileIn, char *fileOut)
{
    // ----------------------------------------------
    //   Menu: File->New...
    // ----------------------------------------------
    BasePart *basePart1;
    PartLoadStatus *partLoadStatus1;
    basePart1 = theSession->Parts()->OpenBaseDisplay(fileIn, &partLoadStatus1);
    delete partLoadStatus1;
  
    Part *workPart(theSession->Parts()->Work());

    // ----------------------------------------------
    //   Menu: File->SaveAs
    // ----------------------------------------------

    PartSaveStatus *partSaveStatus1;
    partSaveStatus1 = workPart->SaveAs(fileOut);
    delete partSaveStatus1;

    return(0);
}

/* ==========================================
           ProE Processing
   ========================================== */
static int processProEPart(Session *theSession, char *fileIn, char *fileOut)
{
    // ----------------------------------------------
    //   Menu: File->New...
    // ----------------------------------------------
    BasePart *basePart1;
    PartLoadStatus *partLoadStatus1;
    basePart1 = theSession->Parts()->OpenBaseDisplay(fileIn, &partLoadStatus1);
    delete partLoadStatus1;
  
    Part *workPart(theSession->Parts()->Work());

    // ----------------------------------------------
    //   Menu: File->SaveAs
    // ----------------------------------------------

    PartSaveStatus *partSaveStatus1;
    partSaveStatus1 = workPart->SaveAs(fileOut);
    delete partSaveStatus1;

    return(0);
}

/* ==========================================
           Return Number of bodies in a part
   ========================================== */

static int getNumberOfBodies(tag_t partTag)
{
    int                        result, nCount, type, mainType, subType;
    tag_t                    solid;

    type = UF_solid_type;
    solid = NULL_TAG;
    nCount = 0;

    /* Start the cycling process by passing in a NULL_TAG. */

    result = UF_OBJ_cycle_objs_in_part( partTag, type, &solid );
    UF_OBJ_ask_type_and_subtype (solid, &mainType, &subType );

    if (subType == 0) nCount++;

    /* Keep cycling until there are no more features to cycle. */

    while ( solid != NULL_TAG )
    {
        UF_OBJ_cycle_objs_in_part( partTag, type, &solid );

        if (solid!=NULL_TAG)
        {
            UF_OBJ_ask_type_and_subtype (solid, &mainType, &subType );
            if (subType == 0) nCount++;
        }
    }

    return(nCount);
}

/* ==========================================
           Sew all the sheet bodies
   ========================================== */

static tag_t sewSheetBodies(tag_t partTag)
{
    int                        result, nCount = 0, type, mainType, subType, numFaces;
    int                        t0=0, t1=0, t2=0, t3=0;
    tag_t                    solid, *faces, faceTarget[1];
    char                    message[133];
    uf_list_p_t                disjoint_list = NULL;
    tag_t                    sew_id;

    // ----------------------------------------------
    //   Sew the part
    // ----------------------------------------------
  
    nCount = 0;
    type = UF_solid_type;
    solid = NULL_TAG;

    /* Get the number of faces */

    numFaces = getNumberOfObjects(partTag, 0);
    printf("Num faces for mem allocation = %d\n", numFaces);
    faces = (tag_t*)malloc(numFaces*sizeof(tag_t));
    if (faces == NULL) 
    {
        printf("Could not allocate memory in sewSheetBodies\n");
        return(NULL);
    }

    /* Start the cycling process by passing in a NULL_TAG. */

    result = UF_OBJ_cycle_objs_in_part( partTag, type, &solid );
    if (solid!=NULL_TAG)
    {
        if (!UF_ASSEM_is_occurrence(solid))
        {
            UF_OBJ_ask_type_and_subtype (solid, &mainType, &subType );

            if (subType == 0) 
            {
                faceTarget[0] = solid;
                t0++;
            }
        }
    }

    /* Keep cycling until there are no more features to cycle. */

    while ( solid != NULL_TAG )
    {
      nCount++;
      UF_OBJ_cycle_objs_in_part( partTag, type, &solid );

      if (solid!=NULL_TAG)
      {
          if (!UF_ASSEM_is_occurrence(solid))
          {
                UF_OBJ_ask_type_and_subtype (solid, &mainType, &subType );
                if (subType == 0) 
                {
                    if (t0 == 0)
                    {
                        faceTarget[0] = solid;
                    } else
                    {
                        faces[t0-1] = solid;
                    }
                    t0++;
                }

                if (subType == 1) t1++;
                if (subType == 2) t2++;
                if (subType == 3) t3++;
          }
       }
    }

    result = UF_MODL_create_sew (0, 1, faceTarget, t0-1, faces, 0.0254, 1, &disjoint_list, &sew_id );

    if (disjoint_list!=NULL)
    {
        UF_MODL_ask_list_count (disjoint_list, &nCount);
        UF_MODL_delete_list(&disjoint_list);
    }

    UF_get_fail_message(result, message);
    printf("Result of sew = %d, Disjoint=%d Msg=%s\n", result, nCount, message);

    free(faces);

    return(sew_id);
}

/* ==========================================
           Dump summary of part
   ========================================== */

static void dumpPartSummary(tag_t partTag)
{
    int                        result, type, mainType, subType;
    int                        nCount0, nCount2, nCount3, nCount5;
    tag_t                    solid;

    type = UF_solid_type;
    solid = NULL_TAG;
    nCount0 = 0;
    nCount2 = 0;
    nCount3 = 0;
    nCount5 = 0;

    /* Start the cycling process by passing in a NULL_TAG. */

    result = UF_OBJ_cycle_objs_in_part( partTag, type, &solid );
    UF_OBJ_ask_type_and_subtype (solid, &mainType, &subType );

    if (subType == 0) nCount0++;
    if (subType == 2) nCount2++;
    if (subType == 3) nCount3++;
    if (subType == 5) nCount5++;

    /* Keep cycling until there are no more features to cycle. */

    while ( solid != NULL_TAG )
    {
        UF_OBJ_cycle_objs_in_part( partTag, type, &solid );
        if (solid!=NULL_TAG)
        {

            UF_OBJ_ask_type_and_subtype (solid, &mainType, &subType );
            if (subType == 0) nCount0++;
            if (subType == 2) nCount2++;
            if (subType == 3) nCount3++;
            if (subType == 5) nCount5++;
        }
    }

    printf("Bodies count = Body %d Face %d Edge %d Foreign %d \n", nCount0, nCount2, nCount3, nCount5);

    return;
}

/* ==========================================
           Extract the sheet bodies
   ========================================== */

static void extractSheetBodies(tag_t partTag)
{
    int                        i, result, type, mainType, subType, numFaces;
    int                        nCount;
    tag_t                    solid, sheet_body, *faces = NULL, origBody = NULL_TAG;

    int                      fIsOccu = (int)false;

    type = UF_solid_type;
    solid = NULL_TAG;
    nCount = 0;

    /* Get the number of faces */

    numFaces = getNumberOfObjects(partTag, 2);
    printf("Num faces for mem allocation = %d\n", numFaces);
    faces = (tag_t*)malloc(numFaces*sizeof(tag_t));
    if (faces == NULL) 
    {
        printf("Could not allocate memory in extractSheetBodies\n");
        return;
    }

    /* Start the cycling process by passing in a NULL_TAG. */

    result = UF_OBJ_cycle_objs_in_part( partTag, type, &solid );
    if (solid!=NULL_TAG)
    {
        fIsOccu = UF_ASSEM_is_occurrence(solid);

        UF_OBJ_ask_type_and_subtype (solid, &mainType, &subType );

        if (subType == 0) origBody = solid;
        if (subType == 2) 
        {
            faces[nCount] = solid;
            nCount++;
        }
    }

    /* Keep cycling until there are no more features to cycle. */

    while ( solid != NULL_TAG )
    {
        UF_OBJ_cycle_objs_in_part( partTag, type, &solid );

        if (solid!=NULL_TAG)
        {
            fIsOccu = UF_ASSEM_is_occurrence(solid);

            UF_OBJ_ask_type_and_subtype (solid, &mainType, &subType );

            if (subType == 0) origBody = solid;
            if (subType == 2) 
            {
                faces[nCount] = solid; 
                nCount++;
            }
        }
    }

    for(i=0;i<nCount;i++)
    {
        result = UF_MODL_extract_face (faces[i], 0, &sheet_body );
    }

    // Delete the original body

    result = UF_OBJ_delete_object (origBody);
    printf("Delete object result = %d\n", result);

    free(faces);

    return;
}

/* ==========================================
           Get the number of selected objects
   ========================================== */
static int getNumberOfObjects(tag_t partTag, int objType)
{
    int                        nCount, type, mainType, subType, result;
    tag_t                    solid;

    type = UF_solid_type;
    solid = NULL_TAG;
    nCount = 0;

    /* Start the cycling process by passing in a NULL_TAG. */

    result = UF_OBJ_cycle_objs_in_part( partTag, type, &solid );
    if (solid!=NULL_TAG)
    {
        UF_OBJ_ask_type_and_subtype (solid, &mainType, &subType );

        if (subType == objType) nCount++;
    }


    /* Keep cycling until there are no more features to cycle. */

    while ( solid != NULL_TAG )
    {
        UF_OBJ_cycle_objs_in_part( partTag, type, &solid );

        if (solid!=NULL_TAG)
        {
            UF_OBJ_ask_type_and_subtype (solid, &mainType, &subType );

            if (subType == objType) 
                nCount++;
        }
    }

    return(nCount);
}

/* NAME
 *    getopt - GET OPTion letter from command line
 *        Reason: new routine
 *
 * SYNOPSIS
 *    int getopt(argc, argv, opt)
 *       int argc;
 *       char *argv[], *opt;
 *
 *    extern char *optarg;
 *    extern int optind, opterr;
 *
 *    Inputs:
 *       argc   - argument count
 *       argv   - argument vector
 *       opt    - list of valid options (options followed by : have arguments)
 *       opterr - error message flag
 *
 *    Outputs:
 *       optind - index of next entry in argv to be processed
 *       optarg - pointer to the start of the option argument
 *       returns the next option letter in argv that matches one in opt,
 *                '?' if the next option letter doesn't match, and EOF
 *                at end
 *
 * DESCRIPTION
 *    getopt is a command line parser that returns the next option letter in
 *    argv that matches a letter in opt.  If a letter in opt is followed by
 *    a colon, the option is expected to have an argument that may be
 *    separated from it by white space - optarg is set to point to the
 *    argument.  When all options have been processed, EOF is returned.  The
 *    special option "--" may be used to delimit the end of the options.  An
 *    isolated dash ("-") is not interpreted as an option.  When an option
 *    letter is found that doesn't match any letter in opt, an error message
 *    is printed on stderr unless opterr has been set to zero.
 */

static int get_cmdline_opts(int argc, char *argv[], char *opt)
   {
   register int c;
   register char *p;
   static int i = 1;

   if (i == 1)
      {
      if (optind >= argc  ||  argv[optind][0] != '-'  ||
            argv[optind][1] == '\0')
         return EOF;
      if (strcmp(argv[optind], "--") == 0)
         {
         ++optind;
         return EOF;
         }
      }
   optopt = c = argv[optind][i];
   if (c == ':'  ||  (p = strchr(opt, c)) == NULL)
      {
      if (opterr)
         fprintf(stderr, "%s: illegal option -- %c\n", argv[0], c);
      ++i;
      if (argv[optind][i] == '\0')
         {
         ++optind;
         i = 1;
         }
      return '?';
      }
   else if (*++p == ':')
      {
      if (argv[optind][i + 1] != '\0')
         optarg = &argv[optind++][i + 1];
      else
         {
         ++optind;
         if (optind >= argc)
            {
            if (opterr)
               fprintf(stderr, "%s: option requires an argument -- %c\n",
                     argv[0], c);
            i = 1;
            return '?';
            }
         optarg = argv[optind++];
         }
      i = 1;
      }
   else
      {
      ++i;
      if (argv[optind][i] == '\0')
         {
         i = 1;
         ++optind;
         }
      optarg = 0;
      }
   return c;
   }

/* ===========================================================
     PR: 5417441 : Cad convertor crashes when output prt
     exists in the directory.

     Check for the out put prt and delete it.
   =========================================================== */
static int remove_existing_output_part_file (char *scOutputPart)
{

    int    iRc = 0;

    /* Check if part file already exists */
    iRc = uc4560 (scOutputPart, 0 );
    if ( iRc ==0 )
    {
        /* Part file already wxists : delete it */
        iRc = uc4561 (scOutputPart, 0 );
        if ( iRc!=0 )
        {
            /* Could not delete the file : Error out */
            printf("Error : Idealized part already exists\n");
            printf("        File name : ");
            printf("%s", scOutputPart);
            printf("\n        Could not delete existing file.\n");
            return -9999;
        }
    }
    
    return iRc;
}/* remove_existing_output_part */



