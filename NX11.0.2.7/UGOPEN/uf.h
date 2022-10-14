/*******************************************************************************

                     Copyright 2007 UGS Corp.
                       All Rights Reserved.

 *

File Description :
   Open C API general interface.  These are general purpose functions that
   will be common to most Open C API programs, as well as specialized functions
   that do not belong to any of the other interfaces.

***************************************************************************/

#ifndef UF_INCLUDED
#define UF_INCLUDED

/***************************************************************************

 ***************************************************************************/

#include <uf_defs.h>
#include <uf_cfi_types.h>
#include <uf_ugopenint.h>
#include <uf_cfi_types.h>
#include <uf_retiring.h>
#include <libufun_exports.h>

#ifdef __cplusplus
extern "C" {
#endif


#define NONE              0
#define METRIC            1
#define ENGLISH           2

/*****************************************************************************
    Unique identifiers for standard NX applications
*****************************************************************************/

#define UF_APP_NONE          (0)      /* No App Module (may be in External UF)*/
#define UF_APP_DRAFTING      (1)      /* Drafting */
#define UF_APP_MECHANISMS    (14)     /* CAE - Mechanisms */
#define UF_APP_CAM           (16)     /* Manufacturing */
/* obsoleted in NX 3         (38)        ICAD - Generative Modeling */
#define UF_APP_MODELING      (40)     /* Modeling */
#define UF_APP_VALISYS       (47)     /* Valisys - Quality Control */
#define UF_APP_GATEWAY       (48)     /* Gateway */

/* UGMX retired in V18.0.0.12 */
#define UF_APP_UGMX          (50)     /* UGMX Interface */

#define UF_APP_HARNESS       (51)
#define UF_APP_FLAT          (60)     /* Sheet Metal Design - Flat Patterns */
#define UF_APP_SHTNEST       (61)     /* Sheet Metal Design - Nesting */
#define UF_APP_PUNCH         (62)     /* Sheet Metal Design - Punch Press */
#define UF_APP_MPG           (63)  /* Sheet Metal Design - Multipart Gridding */
#define UF_APP_SSL           (64)     /* Sheet Metal Design - Surface Layout */
#define UF_APP_SHTFAB        (65)     /* Sheet Metal Design - Fabrication */
#define UF_APP_SMD           (66)     /* Sheet Metal Design Application */
#define UF_APP_BUILDER       (67)     /* UI Builder */
#define UF_APP_SFEM          (68)     /* CAE Advanced Simulation */
#define UF_APP_ROUTE         (69)     /* PSA - Routing Applications */
               /* obsoleted  (70)        PSA - Virtual Mockup (Division) */
#define UF_APP_PIPE          (71)     /* PSA - Routing - Piping */
#define UF_APP_TUBE          (72)     /* PSA - Routing - Tubing */
#define UF_APP_STEEL         (73)     /* PSA - Routing - Steel */
#define UF_APP_CONDUIT       (74)     /* PSA - Routing - Conduit */
#define UF_APP_RACEWAY       (75)     /* PSA - Routing - Raceway */
#define UF_APP_SHOPS         (76)     /* Manufacturing - Shop floor app */
#define UF_APP_WIRE          (77)     /* PSA - Routing - Wiring */
#define UF_APP_MTB           (78)     /* Manufacturing - Machine Tool Builder */
#define UF_APP_SKETCHER      (79)     /* Sketcher Task Environment */
#define UF_APP_NOPART        (80)     /* No Part loaded menubar */
               /* obsoleted  (81)        CAE - Advanced FEM */
#define UF_APP_ROUTE_MECH    (82)     /* PSA - Routing - Mechanical */
#define UF_APP_ROUTE_ELEC    (83)     /* PSA - Routing - Electrical */
#define UF_APP_ROUTE_LGCL    (84)     /* PSA - Routing - Logical */
#define UF_APP_SBSM          (85)     /* SBSM - Straight Break Sheet Metal */
#define UF_APP_SEQUENCING    (86)     /* Sequencing Task Environment */
#define UF_APP_UFUN          (87)     /* UFUN app */
#define UF_APP_STUDIO        (88)     /* Shape Studio */
#define UF_APP_DESFEM        (89)     /* CAE - Design Simulation */
#define UF_APP_SHIP          (90)     /* PSA - Ship Building */
#define UF_APP_AEROSM        (91)     /* PSA - Aerospace Sheet Metal Application */
#define UF_APP_FLEX_PCB      (92)     /* Flexible Printed Circuit Design */
#define UF_APP_INSPECTION    (93)     /* CMM Inspection Programming */
#define UF_APP_MECHATRONICS  (94)     /* Mechatronics Designer */
#define UF_APP_STYLER        (95)     /* Block Styler */
#define UF_APP_SUBSET_DEFINITION (96) /* Subset Definition task environment */
#define UF_APP_TRUE_STUDIO   (97)     /* True Studio Task Environment */
#define UF_APP_SHIP_BASICDESIGN (98)  /* Ship Building */
#define UF_APP_SHIP_DETAILSDESIGN (99)/* Ship Building */
#define UF_APP_SHIP_MANUFACTURE (100) /* Ship Building */
#define UF_APP_SINUCAST      (101)    /* SinuCAST */
#define UF_APP_SUBDIVISION_MODELING   (102)  /* Subdivision Modeling Task Environment */

/* Codesets supported by NX.  This is returned by the
   function UF_ask_codeset.  */

enum UF_codeset_e
{
    UF_CODESET_NOT_INITIALIZED=-2,  /* This is an error condition. */
    UF_CODESET_NOT_SUPPORT=-1,      /* This is an error condition. */
    UF_CODESET_ASCII,               /* Only ASCII characters are supported.
                                       If NX does not recognize a
                                       codeset, then it will revert to
                                       UF_CODESET_ASCII. */
    UF_CODESET_ISO8859_1,           /* Western European standard */
    UF_CODESET_EUC,                 /* Japanese EUC codeset */
    UF_CODESET_SJIS,                /* Japanese SJIS codeset */
    UF_CODESET_ISO8859_4,           /* Finnish, Latvian, Norwegian, Swedish
                                       and other European languages. */
    UF_CODESET_ISO8859_5,           /* Russian, Ukrainian, Bulgarian and other
                                       Eastern European languages. */
    UF_CODESET_ISO8859_8,           /* Hebrew codeset */
    UF_CODESET_BIG5,                /* Traditional Chinese for Taiwan */
    UF_CODESET_NT_866,              /* No longer used, placeholder only */
    UF_CODESET_ISO8859_2,           /* Czech, Polish, Slovak and other
                                       Eastern European languages. */
    UF_CODESET_NT_852,              /* No longer used, placeholder only */
    UF_CODESET_NT_862,              /* No longer used, placeholder only */
    UF_CODESET_KSC5601,             /* Korean codeset */
    UF_CODESET_GB2312,              /* Simplified Chinese for Mainland China */
    UF_CODESET_NT_1251,             /* Windows NT Russian codeset */
    UF_CODESET_NT_1255,             /* Windows NT Hebrew codeset */
    UF_CODESET_NT_1250,             /* Windows NT Eastern European codeset */
    UF_CODESET_NT_1252,             /* Windows NT Western European and US
                                       codeset */
    UF_CODESET_ISO8859_15,          /* Western European codeset including
                                       EURO */
    UF_CODESET_NT_1253,             /* Windows NT Greek codeset */
    UF_CODESET_ISO8859_7,           /* Greek Codeset  */
    UF_CODESET_UTF8,                /* UTF-8 Codeset */
    UF_CODESET_NT_1254,             /* Windows NT Turkish codeset */
    UF_CODESET_NT_1257,             /* Windows NT Baltic codeset */
    UF_CODESET_NT_1256,             /* Windows NT Arabic codeset */
    UF_CODESET_ISO8859_6,           /* Arabic Codeset */
    UF_CODESET_ISO8859_11,          /* Thai Unix and Windows (CP 874) */
    UF_CODESET_NT_1258              /* Vietnamese codeset */
};

typedef enum UF_codeset_e UF_codeset_t;

/*
   This type is used to hold information about a timer in NX.  You
   can have more than one timer active at a time, each active timer requires
   a UF_timer_t variable.
*/
typedef unsigned short UF_timer_t, *UF_timer_p_t;

/*
   The structure UF_timer_values_t below is used to get the values from the
   timer. The routine UF_end_timer fills the fields of this structure, when the
   timer is closed. The timer is initiated by the routine UF_begin_timer.
*/
struct UF_timer_values_s
{
    double cpu_time;      /* Total CPU time (User + System) for this process */
    double real_time;     /* Total elapsed time */
};
typedef struct UF_timer_values_s
               UF_timer_values_t, *UF_timer_values_p_t;


/*
   The structure UF_system_info_t below is used to get the information about
   the current process. The routine UF_ask_system_info retrieves the
   information about the process and fills the structure. Once the data is used,
   the memory allocated to these fields should be freed by calling the routine,
   UF_free_system_info.
*/
struct UF_system_info_s
{
    char *date_buf;        /* Current date and time info */
    char *user_name;       /* User, who is running this process */
    char *program_name;    /* The current program name */
    char *node_name;       /* Machine, on which this process is running */
    char *machine_type;    /* Hardware type on which the machine is running */
    char *os_name;         /* Operating system, on which this process is running
                              */
    char *os_version;      /* Version and release level of this Operating System
                              */
    long  physical_memory; /* Returns the number of bytes of physical memory
                              on this machine. */
    char **bundles_used;   /* <len:number_of_bundles>Array of the names of the bundles currently in use. */
    int   number_of_bundles;  /* The number of bundles currently in use */
};
typedef struct UF_system_info_s
               UF_system_info_t, *UF_system_info_p_t;


/****************************************************************************
*   Get the information about an Open C Program
*
*   This routine can be used to gather the system information of an Open C
*   program, like the machine name, Operating System information etc., and is
*   useful in benchmarking, where you want to record the information about
*   the machine the benchmark was run on.
*
*   This routine outputs the data through the structure UF_system_info_t.
*
*   Once the data is no longer needed, the memory allocated to the fields
*   of this structure should be freed by a corresponding call to the routine
*   UF_free_system_info.
*
*   Environment: Internal and External
*
*   See Also:
*    UF_free_system_info
*    UF_system_info_t
*
*   History: Released in V18.0, modified in NX 6.0 to return used bundles
****************************************************************************/
extern UFUNEXPORT int UF_ask_system_info(
       UF_system_info_p_t info  /* <OF,free:UF_free_system_info>
                                   structure to hold the process information.
                                   The allocated fields should be freed by
                                   calling UF_free_system_info
                                */
);


/****************************************************************************
*   Free the fields of the structure UF_system_info_t, containing the process
*   information
*
*   This structure is filled earlier by a call to the routine UF_ask_system_info
*
*   Environment: Internal and External
*
*   See Also:
*    UF_ask_system_info
*    UF_system_info_t
*
*   History: Released in V18.0
****************************************************************************/
extern UFUNEXPORT int UF_free_system_info(
       UF_system_info_p_t info  /* <I>
                                   structure whose fields are to be freed
                                */
); /* <NON_NXOPEN> */



/****************************************************************************
*   Start a timer.
*
*   This routine can be used to gather timing information about an Open C
*   program, and is useful in benchmarking. This routine will start a timer.
*   The timer will be stopped with a corresponding call to UF_end_timer.
*
*   More than one timer can be active at any time, this is useful when you
*   have one overall timer, and then several sub-timers timing individual
*   sub-operations.
*
*   Environment: Internal  and  External
*
*   See Also:
*    UF_end_timer
*    UF_timer_values_t
*
*   History: Released in V18.0
****************************************************************************/
extern UFUNEXPORT int UF_begin_timer (
                      UF_timer_p_t timer /* <O>
                                          * Timer id that is created
                                          */
);


/****************************************************************************
*   Stop the timer and get the timer values
*
*   This routine is used to gather timing information about an Open C program,
*   and is useful in benchmarking. This routine will stop the timer created by
*   a corresponding UF_begin_timer call, and output the timing information in
*   the structure UF_timer_values_t.
*
*   Environment: Internal  and  External
*
*   See Also:
*    UF_begin_timer
*    UF_timer_values_t
*
*   History: Released in V18.0
****************************************************************************/
extern UFUNEXPORT int UF_end_timer (
                      UF_timer_t timer,          /* <I>
                                                  * Timer to be stopped
                                                  */
                      UF_timer_values_p_t values /* <O>
                                                  * Timer values when it is
                                                  * stopped
                                                  */
);


/*****************************************************************************
 * Frees the memory allocated and returned by an Open C API routine.
 *
 * Return : void
 *
 * Environment: Internal  and  External
 *
 * See Also:
 *
 * History:
*****************************************************************************/
extern UFUNEXPORT void UF_free (
    void *data /* <I> Pointer to data item to free     */
);

/*****************************************************************************
 * Allocates a block of storage and returns a pointer to it. Use UF_free
 * to free the allocated memory when no longer required.
 *
 * Return:
 *     void *  - a pointer to the block of storage, aligned so
 *               that any data type can be stored in it.
 *               when error occur or nbytes = 0, a NULL pointer
 *               is returned
 *
 * Environment: Internal and External
 *
 * See Also:
 *
 * History: This function was originally released in V15.0
 *****************************************************************************/
extern UFUNEXPORT void *UF_allocate_memory(
    unsigned int  nbytes,         /* <I>
                  The number of bytes to be allocated.
                                  If 0, NULL is returned
                  */
    int          *error_code      /*<EC>
                  NX standard error code
                  0    success
                  !=0  failure
                  */
);
/*****************************************************************************
 * Reallocates a block of storage and returns a pointer to it. Use UF_free
 * to free the allocated memory when no longer required.
 *
 * Return:
 *     void *  - a pointer to the block of storage, aligned so
 *               that any data type can be stored in it.
 *               when error occur or nbytes = 0, a NULL pointer
 *               is returned
 *
 * Environment: Internal and External
 *
 * See Also:
 *
 * History: This function was originally released in V16.0
 *****************************************************************************/
extern UFUNEXPORT void *UF_reallocate_memory(
void         *data,               /* <I>
                                     Pointer to previously allocated memory
                                  */
    unsigned int  nbytes,         /* <I>
                                     The number of bytes to be allocated.
                                          If 0, NULL is returned
                                  */
    int          *error_code      /* <EC>
                                     NX standard error code
                                  */
);



/*****************************************************************************
 * Frees the memory allocated for an array of pointers and frees the
 * strings within the array. You must pass in the number of pointer in
 * the array.  Various Open C API routines malloc space for an array
 * of pointers, and then allocate space for each of the pointers.
 *
 * Return : void
 *
 * Environment: Internal  and  External
 *
 * See Also:
 *
 * History:
*****************************************************************************/
extern UFUNEXPORT void UF_free_string_array (
    int      n_strings ,     /* <I>
                 number of pointers
                 */
    char   **string_array    /*<I,len:n_strings> n_strings
                 pointer to the array of pointers to free
                 */
);/*<NON_NXOPEN>*/

/*****************************************************************************
 * Returns the message string associated with an error code.
 *
 * Environment: Internal  and  External
 *
 * See Also:
 *
 * History:
*****************************************************************************/
extern UFUNEXPORT int UF_get_fail_message (
    int    fail_code ,     /* <I>
               the failure code to translate
               */
    char   message[ 133 ]  /* <O>
               the message corresponding to the fail code
               */
);

/*****************************************************************************
 * Returns the message string associated with an error code in current user interface language.
 *
 * Environment: Internal  and  External
 *
 * See Also:
 *
 * History: Originally released in NX 10.0 
*****************************************************************************/
extern UFUNEXPORT int UF_get_translated_fail_message(
    int    fail_code ,     /* <I>
               the failure code to translate
               */
    char   ** message  /* <O>
               the message corresponding to the fail code
               */
);

/***************************************************************************
 * Explanation:  In UG V9, when an entity had a known Entity IDentifier    *
 * (EID), that EID was saved with the part and would be the same the next  *
 * time the part was loaded.  In V10, because multiple parts can be loaded *
 * at once, the Tag (ie, EID) of an object can not be guaranteed between   *
 * sessions.  For this reason, "Handles" were created to identify objects  *
 * between sessions.  To aid applications where the EID was saved in some  *
 * data file between sessions,  UF_ask_new_tag_of_entity()  was created to *
 * return the V10 tag corresponding to the EID of an entity in a V9 part   *
 ***************************************************************************/

/***************************************************************************
 * This function replaces UF_TAG_ask_handle_of_tag.
 *
 * Return the persistent HANDLE for an object tag.
 *
 * Multiple parts can be loaded into NX during a single session, and
 * the Tag (i.e. Object Identifier) cannot be guaranteed between sessions.
 * Consequently, "handles" were created to identify objects between sessions.
 * This handle is persistent between sessions once the object is saved to a part file.
 * A handle of a new object in this session which is never saved is not guaranteed
 * to stay the same until the object is saved. Recreating the same object in a new 
 * session may not be the same even if seemingly identical steps were taken to create
 * the object. This is particularly true across versions of software.
 *
 * Handles should not be compared directly for checking identity as they contain 
 * version information. Handles should be broken apart using UF_TAG_decompose_handle 
 * and the file_data strings compared and the sub_file_id integers compared but the 
 * version should be ignored.
 *
 * Operations which change the name of the part will change the handle as well - so
 * "Save As" will cause handles to change.
 *
 * This function will return an error when the part data of the handle
 * contains a character that cannot be represented.  For this reason
 * it is suggested that UF_TEXT_set_text_mode(UF_TEXT_ALL_UTF8) be
 * set when you are working with handles that may come from parts that have
 * characters that are outside of your locale (e.g. parts with Japanese 
 * characters on an english system).
 *
 * Output:
 * The name of handle for object tag. This string must be freed by calling UF_free.
 *
 * Environment: Internal  and  External
 * See Also:  UF_TAG_ask_tag_of_handle
 * History: Originally released in NX 10.0
 ***************************************************************************/
extern UFUNEXPORT int UF_TAG_ask_handle_from_tag (
    tag_t   object_tag,     /* <I>
                               tag of object to query for persistent handle
                            */
    char **handle           /* <OF>
                               Output handle for the tag.
                            */
   
);


/****************************************************************************
 * Return the object tag of a persistent HANDLE.
 *
 * Return:
 *       Returns object tag of object handle
 *
 * Environment: Internal  and  External
 *
 * See Also:  UF_TAG_ask_handle_from_tag
 *
 * History:
 ****************************************************************************/
extern UFUNEXPORT tag_t UF_TAG_ask_tag_of_handle (
    char   *object_handle  /* <I>
               Name of persistent handle
               */
);/* <NEC> */

#define UF_ask_new_tag_of_entity  UF_TAG_ask_new_tag_of_entity
/****************************************************************************
 * Returns the new tag of the object corresponding to the known object
 * ID in the V9 part. This only works for the Object IDs of the last V9
 * part loaded into this session.
 * NOTE: This was renamed from UF_ask_new_tag_of_entity()
 *
 * Return:
 *       New tag
 *
 * Environment: Internal  and  External
 * See Also:  UF_TAG_ask_handle_from_tag
 * History:
 ****************************************************************************/
extern UFUNEXPORT tag_t UF_TAG_ask_new_tag_of_entity (
    tag_t   v9_eid    /* <I>
              Known Object ID (EID) of V9 part
              */
);/* <NEC> */

/*****************************************************************************
 * Given the constituent parts of data manager, filename, subfile id and
 * version, this function returns the resulting handle.
 *
 * Environment: Internal  and  External
 *
 * See Also:
 *
 * History:
 ******************************************************************************/
extern UFUNEXPORT int UF_TAG_compose_handle (
    const char      *file_data ,    /* <I>
                    Data about the file.  This string would come
                                    from a call to UF_TAG_decompose_handle.
                    */
    unsigned int    sub_file_id ,   /* <I>
                    sub_file identifier. The sub_file is
                    an internal file in the part file database.
                    */
    unsigned int    version ,       /* <I>
                     Version of part
                     */
    char            **handle        /* <OF>
                     String containing the composed handle
                     */
);

/*****************************************************************************
 * Given the handle, the constituent parts of data manager, filename, subfile
 * id and version are returned.
 *
 * Note this function will return an error if you have UF_TEXT_set_text_mode() 
 * set to locale and the file that the data is coming from has characters 
 * outside of your locale.  It is suggested that you set your text mode to 
 * UF_TEXT_ALL_UTF8 when you are working with handles.
 *
 * Environment: Internal  and  External
 *
 * See Also:  UF_TAG_ask_new_tag_of_entity
 *   UF_TAG_ask_handle_from_tag
 *
 * History:
 ******************************************************************************/
extern UFUNEXPORT int UF_TAG_decompose_handle(
    char   *handle ,               /* <I>
                   Handle to decompose
                   */
    char  **file_data ,            /* <OF,free:UF_free>
                   Data about the file.  This can be used by
                                   UF_TAG_compose_handle. This argument
                                   must be freed by calling UF_free.
                   */
    unsigned int    *sub_file_id , /* <O>
                   Sub-file identifier for handle. The
                   sub_file is an internal file in the part
                   file database.
                   */
    unsigned int    *version       /* <O>
                   Version of part in which handle is located.
                   */
);

#define UF_set_program_name UF_MISC_set_program_name
/****************************************************************************
 * Each part file has an internal history storage area where the program
 * name can be stored when the system saves the part file. This function
 * enables you to specify either the entire program name (External
 * mode) or append a name to the program name (Internal mode). You
 * should call this routine before you call UF_PART_open since it does
 * not set the program name on parts that are already opened. A utility
 * called ug_inspect enables you to read the program name stored in the
 * history area.
 *
 * Interactively (Internal mode), when you are in NX, the program
 * name will take the version of NX currently being run (e.g. NX9.0.0.19)
 * and append the string being passed into UF_MISC_set_program_name. For
 * example, if you specify "XYZ version 9.0" as the name string to this
 * routine, then the program name in the history would look like:
 * NX 9.0.0.19XYZ version 9.0
 * To separate the version and string, put a leading space in the name being 
 * passed into this routine.  " XYZ version 9.0" passed in will create:
 * NX 9.0.0.19 XYZ version 9.0
 *
 * Once UF_terminate is called, the appended string is removed and it will
 * default back to the NX version number the next time the part is saved.
 *
 * In External mode, the program name is what you specify in the name
 * string. From our previous example this would be XYZ version 9.0.
 * The limitation for the length of the name string depends on which
 * mode you are in, Internal or External. The maximum length of the
 * entire program name is 128 characters. In Internal mode, because the
 * name string is concatenated to the program name you are limited to
 * 64 characters. In External mode, since the name string you specify
 * becomes the program name you are limited to 128 characters. In
 * either mode, if you specify a name that is to long, the name is
 * truncated to either 64 or 128 characters (Internal and External mode
 * respectively).
 *
 * The internal history area is like a log file. If you resave the part file
 * with a different program a new history entry is added to the part file.
 * That is, the history grows larger. Thus you are likely to see two lines of
 * history if you have saved the part file twice and specified a name with
 * each save.
 *
 * Return: void
 *
 * Environment: Internal  and  External
 *
 * See Also:
 *
 * History:
 ****************************************************************************/
extern UFUNEXPORT void UF_MISC_set_program_name (
    const char   *name   /* <I>
             Name of program to store in the internal history
             */
);

/****************************************************************************
 * Translates environment variables to their equivalence strings. You
 * must supply the complete name of the variable argument.  The pointer passed
 * back points to an operating system string.  This string must not be changed.
 *
 * Environment: Internal  and  External
 *
 * See Also: 
 *
 * History:
 ****************************************************************************/
extern UFUNEXPORT int UF_translate_variable (
    const char   *variable , /* <I>
                     Environment Variable to Translate
                 */
    char   **translation     /* <O>
                 Translated variable name or NULL if nonexistent.
                 */
);

/****************************************************************************
 * Sets an environment variable to the string specified in value. You must
 * supply the complete name of variable.
 *
 * Environment: Internal  and  External
 *
 * See Also: 
 *
 * History:
 ****************************************************************************/
extern UFUNEXPORT int UF_set_variable (
    const char   *variable , /* <I>
                             Environment Variable to set in Operating System
                             */
    const char   *value      /* <I>
                             Value or equivalence string for the variable.
                             */
);

/****************************************************************************
 * Initializes the Open C API environment and allocates an Open C
 * API execute license. If you do not call UF_initialize, then subsequent
 * calls to Open C API fail with an error code of
 * UF_err_program_not_initialized. This function must be the first
 * function you call after you have declared your variables.
 *
 * In external mode, you may only call UF_initialize once. Once 
 * UF_terminate is called, there is no way to reconnect to the Open C environment.  
 * 
 * Programs need to call UF_terminate before exiting to ensure licenses are
 * released and avoid errors in downstream NXOpen programs.
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * 
 *
 * History:
 ****************************************************************************/
extern UFUNEXPORT int UF_initialize (
    void
);/*<RETIRE_PYTHON>*/

/****************************************************************************
 * Same as UF_initialize with the addition that Direct Model is also initialized.
 *
 * Environment: Internal  and  External
 *
 * See Also:
 *
 * History:
 ****************************************************************************/
extern UFUNEXPORT int UF_initialize_dm (
    void
);

/****************************************************************************
 * Checks if the Open C API environment has been successfully
 * initialized.
 *
 * Return:
 *        return code:
 *          0 = Open C API is not initialized.
 *          1 = Open C API has been properly
 *              initialized.
 *
 * Environment: Internal  and  External
 *
 * See Also:
 *
 * History:
 ****************************************************************************/
extern UFUNEXPORT int UF_is_initialized (
    void
);/* <NEC> */

/****************************************************************************
 * Terminates the Open C API environment and deallocates a
 * Open C API execute license. If UF_terminate is not called, the
 * Open C API execute license may not be freed. Once UF_terminate
 * is called in an external Open C API program, the program will
 * exit. You will not be able to call UF_initialize again and continue
 * operation.
 *
 * Calling this method will release all licenses in the default context.
 *
 * Once UF_terminate has completed in an external program, you can no
 * longer write to the console window.  It must be reinitialized with system
 * calls.
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * 
 * History:
 ****************************************************************************/
extern UFUNEXPORT int UF_terminate (
    void
);

/****************************************************************************
 * Reserve a license against the specified license context.
 * If the specified user-defined context does not already exist it will be created.
 *
 * Environment: Internal  and  External
 *
 * See Also:
 *
 * History:
 ****************************************************************************/
extern UFUNEXPORT int UF_reserve
(
   const char* license , /* <I>
                             License feature name to be reserved
                             */
   const char* context_name  /* <I>
                             Name of context to reserve license against.  Will use the default context if NULL is specified.
                             */
);

/****************************************************************************
 * Release a license against the specified license context.
 *
 * Environment: Internal  and  External
 *
 * See Also:
 *
 * History:
 ****************************************************************************/
extern UFUNEXPORT int UF_release
(
   const char* license , /* <I>
                             License feature name to be released
                             */
   const char* context_name /* <I>
                             Name of context to release license against.  Will use the default context if NULL is specified.
                             */
);

/****************************************************************************
 * Release all licenses against the specified license context.  If
 * the context specified is a user-defined context it will be deleted.
 *
 * Environment: Internal  and  External
 *
 * See Also:
 *
 * History:
 ****************************************************************************/
extern UFUNEXPORT int UF_release_all
(
   const char* context_name /* <I>
                             Name of context release to release.  Will use the default context if NULL is specified.
                             */
);

/****************************************************************************
 * Returns the licenses that are currently reserved against a context.
 * This method will also output the licenses reserved against the default context in the syslog.
 *
 * Environment: Internal  and  External
 *
 * See Also:
 *
 * History:
 ****************************************************************************/
extern UFUNEXPORT int UF_get_reserved_licenses
(
   const char* context_name, /* <I>
                             Name of context to release against.  Will use the default context if NULL is specified.
                             */
   int *n_licenses,             /* <O>
                              The number of licenses.
                       */
   char*** licenses       /* <OF,len:n_licenses>
                       The list of license reserved against the specified context.  This must be
                       freed by calling UF_free_string_array.
                       */
);


/***************************************************************************
 * Encodes an input authorization file using an integer value for
 * perturbation.
 *
 * Environment: Internal
 *
 * See Also:
 *
 * History:
 *************************************************************************/
extern UFUNEXPORT int UF_encode_auth_file (
   int key ,          /* <I>
                      Value used to perturb the input file
                      */
   char *input_file , /* <I>
                      Input authorization file name
                      */
   char *output_file  /* <I>
                      Output encoded authorization file name
                      */
);

/***************************************************************************
 * Decodes an input authorization file using an integer key value that
 * matches the original key for perturbation.
 *
 * NOTE:  See %UGII_BASE_DIR%\UGALLIANCE\alliance_readme.txt for more information
 *
 * Environment: Internal
 *
 * See Also:
 *
 * History:
 **************************************************************************/
extern UFUNEXPORT int UF_decode_auth_file (
    int key ,         /* <I>
                      Integer valued key for decoding the input file
                      */
    char *input_file, /* <I>
                      Input authorization file to decode
                      Use the leaf name of a file located under the folder %UGALLIANCE%\auth_files.
                      Entering the full path will return an error of -5 "Invalid file name".
                      */
    void **out_mem    /* <OF>
                      Pointer to decoded contents of the authorization
                      file. Use UF_free to deallocate the memory.
                      */
);
/*****************************************************************************
 * Returns the current application module. The value that is returned
 * maps to a string defined constant. You can find the string in the
 * header file uf.h. The strings are of the form UF_APP_<module>.
 * For example, UF_APP_DRAFTING represents the drafting module.
 *
 * Note - if this function is called from an external program it will
 *        always return a FALSE and an app id of APP_NONE.
 *
 * Environment: Internal  and  External
 * See Also:
 * History:
 *****************************************************************************/
extern UFUNEXPORT int UF_ask_application_module(
                    int *module_id  /* <O>
                                    The module identification value of the
                                    current application.
                                    */
);

/*****************************************************************************
 * Calls and executes a GRIP program. Your GRIP program must be written,
 * compiled, linked, and ready to run.
 *
 * While a GRIP program executes, it can have access to an Open C API function
 * arguments and their contents. Argument passing to the GRIP program occurs
 * through UFARGS. After GRIP program termination, the Open C API program has
 * access to any assignments made by the GRIP program. The GRIP program
 * completes its execution and then UF_call_grip outputs a return value.
 *
 * Note:  If the path is omitted in the grip_executable string passed to
 * UF_call_grip, NX will look in the current directory for the grip program.
 * It will not look in the directory of the ufunc program or use any
 * environment variables, including UGII_INITIAL_GRIP_DIR, to search for the
 * GRIP program.
 *
 * UF_translate_variable can be used to extract an environment variable and
 * concatenate it with the program name.
 *
 * The following GRIP commands are not
 * supported in External mode when calling GRIP:
 *         ALL OF GRIP NC
 *         PLNOTE  EDTXHT  CHAIN
 *         BLANK   UNBLNK  RVBLNK
 * If any of these commands are encountered, an error is written to the
 * batch log file.
 *
 * Environment: Internal  and  External
 *
 * See Also: 
 *
 * History:
 ****************************************************************************/
extern UFUNEXPORT int UF_call_grip (
    char *grip_executable,  /* <I>
                                Name of GRIP program to execute (file name
                                or full path name).
                                */
    int count,          /* <I>
                                Count of arguments to pass to GRIP executable
                                */
    UF_args_p_t UFARGS      /* <I,len:count>
                                An array of structures where each element in
                                 the array is a structure that contains an
                                arguments type, size, and address.  Note that
                                if an argument is type UF_TYPE_CHAR, the array
                                must be initialized prior to the UF_call_grip
                                call.
                                */
);

/*****************************************************************************
 * This routine retrieves a customer default value from the database.
 * There are several different conditions that can arise from querying
 * the database:
 *     1) The record was found and its units match. The function
 *        returns SUCCESS(0)
 *     2) The record was not found. If units given was ENGLISH or METRIC
 *        nothing is returned and the function returns a FAILED(1). If
 *        the units given was NONE a second and/or third attempt is made
 *        with units ENGLISH THEN METRIC used instead. The results of
 *        these attempts can be any of the conditions outlined above.
 *
 * If you specify either METRIC or ENGLISH for units, this function
 * automatically appends _MU or _EU to the input name. For example, if you
 * specify METRIC and input the name "UG_gridSpacingY", the function searches
 * for "UG_gridSpacingY_MU".
 *
 * If you specify NONE for units, the function searches for the name
 * as specified. If the name is not found it searches again with _EU
 * appended to the name. If the name is still not found, then it
 * appends _MU to the name for its final search.
 *
 * Return:
 *        return code:
 *       0 = Success
 *       1 = Record not found
 *  <0 or >1 = Use UF_get_fail_message to get error.
 *
 * Environment: Internal  and  External
 *
 * See Also: 
 *
 * History:
 *****************************************************************************/
extern UFUNEXPORT int UF_get_customer_default(
            char * name ,           /* <I>
                                    Name of Module ID and default
                                    */
            int units ,             /* <I>
                                    Units are enumerated as follows:
                                    0 = NONE
                                    1 = METRIC
                                    2 = ENGLISH
                                    */
            char ** default_value  /* <OF>
                                   String containing default value. If
                                   *default_value is NULL then the value was
                                   not found or an error occurred. Use UF_free
                                   to deallocate memory when no longer required.
                                   */
);
/**************************************************************************
 * Returns the current major release version number. For example, if
 * you call this function from V10.4.1, it returns V10.4. You must use
 * UF_free to deallocate space used by release.
 *
 * Environment: Internal  and  External
 *
 * See Also:
 *
 * History:
****************************************************************************/
extern UFUNEXPORT int   UF_get_release(
            char ** release  /* <OF>
                             Major release version number
                             */
);

typedef void (*UF_load_f_p_t)( void );

 /**********************************************************************
 * Loads the shared library specified by library_name and finds the entry
 * point specified by symbol_name in that library.  The reference to the
 * specified entry point is output as a function pointer declared to accept
 * and return void (i.e. type UF_load_f_p_t).
 *
 * For the entry point to be found on Windows NT, you must declare it with
 * the DllExport macro, e.g.
 *
 *    extern DllExport int my_function(...
 *
 * without the DllExport, the name will not be exported.  Since the DllExport
 * also works on Unix systems, the best practice is just to always use the
 * DllExport macro for routines you want exported.
 *
 * If library_name is found but symbol_name is not, an appropriate error
 * code returns, but the loaded library may not be unloaded.  The user
 * should call UF_unload_library to explicitly unload library_name on
 * failure, if appropriate.
 *
 * To load a shared library into an external application - the library must
 * not be linked against any interactive libraries.  This can be accomplished
 * by using the "-noui" option on Unix.
 *
 * NOTE: UF_load_library is intended for function (i.e. "text" entry
 * point) lookup only.  It should NOT be used for data symbol lookup.
 *
 * Environment: Internal  and  External
 *
 * See Also:  UF_unload_library
 * 
 *
 * History:
 **********************************************************************/
extern UFUNEXPORT int UF_load_library(
const char * library_name ,/* <I>
                     Name of shared library to load.
                     */
const char * symbol_name ,/* <I>
                    Name of symbol (function) to find.
                    */
UF_load_f_p_t *function_ptr  /* <O>
                            Pointer to symbol (function) in library.
                            */
);/*<NON_NXOPEN>*/

 /**********************************************************************
 * Unloads the shared library specified by library_name.  UF_unload_library
 * unloads the library unconditionally, effectively invalidating all function
 * pointers previously set by calls to UF_load_library for the specified
 * library.
 *
 * Environment: Internal  and  External
 *
 * See Also:  UF_load_library
 * 
 *
 * History:
 *
  *********************************************************************/
extern UFUNEXPORT int UF_unload_library(
char * library_name  /* <I>
                     Name of shared library to unload.
                     */
);

/****************************************************************************
*   Force NX to shut down immediately.  This is a substitute for the standard
*   c function: exit(0)
*
*   Warning: depending on the current state of NX, forcing a shutdown
*   may produce warnings/errors as NX attempts to close itself.
*
*   Environment: Internal and External
*
*   History: NX 6.0.1
****************************************************************************/
extern UFUNEXPORT void UF_sys_exit( void );/*<NON_NXOPEN>*/

/*****************************************************************************
 * Checks to see if a NX Manager process is
 * active. It returns true if NX Manager is active.
 *
 * Environment: Internal  and  External
 *
 * See Also:
 *
 * History:
 *****************************************************************************/
extern UFUNEXPORT int UF_is_ugmanager_active(
    logical    *is_active    /* <O>
                     Returns true if NX Manager is active
                         */
);
/****************************************************************************
 * Returns the code set identifier supported by a machine. The code set
 * identifier can be any one of the enumerated constants in UF_codeset_e.
 *
 * Environment: Internal  and  External
 *
 * See Also:  UF_codeset_t
 *
 * History:
 ****************************************************************************/
extern UFUNEXPORT int UF_ask_codeset(
     UF_codeset_t *codeset      /*<O>
                                Pointer to the codeset identifier.
                                */
);

/*
 * These are the reasons against which call backs can be registered.
 *
 * The registered callbacks will be called whenever the specific reason occurs
 * in interactive NX.
 *
 * For all the reasons, except for UF_close_part_reason, the callbacks will be
 * called towards the end of that particular operation. For example, the
 * callbacks registered against UF_create_part_reason will be called when a
 * new part is created, after almost all the process of creating this new part
 * is completed.
 *
 * The UF_change_work_part_reason call back will be called after a work part change
 * has occurred. It should be noted that this callback may be called at times where the
 * old work part (which is passed as the part tag data to the call back routine) may
 * not necessarily be different from the new work part. For example, this call back is
 * also called if the display part has changed but the new work part is still the same tag
 * and now represents a component in a different display part. This call back may be 
 * called more than once as part of a single operation.
 * 
 * An attempt to query the work or display part in a UF_save_part_reason_callback
 * may return unexpected results.
 *
 * The callbacks registered against UF_close_part_reason will be called at the
 * beginning of part close.
 *
 * The callbacks registered against UF_modified_part_reason will be called
 * when the part is modified for the first time after opening it or after a
 * save operation.
 *
 * These callbacks give a handle to the user to do some extra processing, in
 * addition to the processing that NX does, during that particular operation.
 *
 * In NX Manager mode, when a new part is being created it first loads the
 * template part (seed part), changes the template part to be the work part
 * and then renames the work part to the new part name given.  So, the following callbacks are being called:
 * UF_modified_part_reason, UF_open_part_reason, UF_change_work_part_reason,
 * UF_rename_part_reason and UF_create_part_reason.
 */
enum UF_callback_reason_e
{
    UF_create_part_reason,    /* Callback when a new part is created. */
    UF_open_part_reason,      /* Callback when an existing part is opened. */
    UF_save_part_reason,      /* Callback when a part is saved. */
    UF_save_as_part_reason,   /* Callback when a part is saved-as. */
    UF_close_part_reason,     /* Callback when a part is closed. */
    UF_modified_part_reason,  /* Callback when a part is modified. */
    UF_rename_part_reason,    /* Callback when a part is renamed. */
    UF_change_work_part_reason, /* Callback when there is a new work part.
                                   The part returned is of the old work part.
                                   Use UF_ASSEM_ask_work_part to get new work part. */
    UF_post_save_as_part_reason, /* Callback reason for adding parts for
                                 Save As at the end of in progress Save As operation
                                 of selected part/parts, it's like nested Save As.
                                 Only issued in managed mode. */
    UF_max_reason             /* Do not use - not a valid reason */
};
typedef enum UF_callback_reason_e UF_callback_reason_e_t;

/* Definition of a callback function prototype. */
typedef void (*UF_callback_fn_t)(
    UF_callback_reason_e_t,  /* <I> reason the callback has been called */
    const void*,             /* <I> This is the pointer to the part tag that
                                    caused the callback. For UF_change_work_part_reason
                                    the part returned is of the old work part.
                                    Use UF_ASSEM_ask_work_part to get new work part.
                             */
    void*                    /* <I> This is a user supplied pointer.  Typically
                                    this will be a structure pointer of data
                                    that your callback function will need.
                             */
    );

typedef struct UF_registered_fn_s *UF_registered_fn_p_t;

/****************************************************************************
 * Registers the callback to be called whenever the reason specified
 * occurs within NX.
 *
 * Please note the following:
 *
 *       Once a routine is registered as a callback, the shared library it
 *       resides in should not be unloaded until it is deregistered.
 *
 *       The callback function must call UF_initialize and UF_terminate, if
 *       it makes any Open C function calls
 *
 *       The callback function receives three arguments:
 *           argument 1 - The reason the callback has been called
 *           argument 2 - A pointer to the part tag that caused the callback.
 *           argument 3 - A user supplied pointer. Typically this will be a
 *                        structure pointer of data that the callback function
 *                        will need.
 *
 *       The callback will be called towards the end of the processing for that
 *       particular reason. For example, the callback registered against
 *       UF_create_part_reason will be called when a new part is created, after
 *       almost all the process of creating this new part is completed.
 *
 *       The only exception to the above is UF_close_part_reason, for which
 *       the callback will be called at the beginning of closing the part.
 *
 *       NOTE: For the new and open part reasons the callback is run at a time
 *       when the newly created or opened part has not been set as the work part.
 *       Also operations such as create part, open part, save part or change display part 
 *       should not be called from callbacks fired by any of these same operations.
 *
 * Environment: Internal  and  External
 *
 * See Also:  UF_remove_callback_function
 *            UF_callback_reason_e
 *           
 *
 * History: V16 was changed to require the callback to call UF_initialize
 ****************************************************************************/
extern UFUNEXPORT int UF_add_callback_function (
    UF_callback_reason_e_t reason,    /* <I>
                                      Reason to call callback
                                      */
    UF_callback_fn_t fn,              /* <I>
                                      Function to call.  Note this function
                                      must call UF_initialize if it
                                      makes any Open C function calls.  It
                                      should also call UF_terminate.
                                      */
    void *user_data,                  /* <I>
                                      User data.  This pointer will be passed
                                      to your callback function as the third
                                      argument.  It will typically be a
                                      structure pointer with information that
                                      your callback function will require.
                                      */
    UF_registered_fn_p_t *function_id /* <O>
                                      Identifier to use to remove callback
                                      */
);

/****************************************************************************
 * Deregisters the callback specified by the identifier.
 *
 * Environment: Internal  and  External
 *
 * See Also:  UF_add_callback_function
 *
 * History:
 ****************************************************************************/
extern UFUNEXPORT int UF_remove_callback_function (
    UF_registered_fn_p_t function_id  /* <I>
                                      Identifier from UF_add_callback_function
                                      */
);

/****************************************************************************
 * The following set of routines allow the registration of routines to be
 * called when tags are created and deleted. This allows synchronisation of
 * data structures outside of NX with NX. Note that the routines registered
 * can not call any other UF routines themselves. Also the implementation
 * of any routine so registered must be very efficient as it will be called
 * very many times.
 *
 * Also it should be remembered that tags get reused. This means that the
 * order of events is important so the event is interpreted with respect
 * to the right incarnation of the tag.
 ****************************************************************************/

/****************************************************************************
 * This enum identifies the type of an event that occurred on a tag.
 ****************************************************************************/

enum UF_TAG_event_e
  { UF_TAG_EVENT_NORMAL_CREATE,       /* The tag was created. */
    UF_TAG_EVENT_UNDO_OVER_CREATE,    /* An undo occurred over the tag's
                                         creation and so is now invalid. */
    UF_TAG_EVENT_NORMAL_DELETE,       /* The tag was deleted. */
    UF_TAG_EVENT_UNDO_OVER_DELETE,    /* An undo occurred over the tag's
                                         deletion and so has come back to
                                         life. */
    UF_TAG_EVENT_UNDO_DELETE_EXPIRED, /* NX will now never undo over
                                         the deletion so it will never come back
                                         to life. */
    UF_TAG_EVENT_UNDO_CREATE_EXPIRED  /* NX will now never undo over
                                         the tags creation. */
  };
typedef enum UF_TAG_event_e UF_TAG_event_t;
/****************************************************************************
 * Type of the event notification callback.
 *****************************************************************************/

typedef void (*UF_TAG_event_fn_t)(UF_TAG_event_t reason, /* <I> */
                                  tag_t tag, /* <I> */
                                  void *closure /* <I> */);

/*****************************************************************************
 * Register a new tag event callback. All callbacks are called on all tags
 * for all events. This returns an identifier for the callback which is
 * used to allow it removal.
 *
 * Please note the following items:
 *   . The routines registered can not call any other Open C routines
 *     In particular, the tag cannot be queried or edited in any way.
 *   . The implementation of any routine so registered must be very
 *     efficient as it is called many times.
 *   . Recall that tags get reused. This means that the order of events is
 *     important so the event is interpreted with respect to the right
 *     "incarnation" of the tag.
 *
 * Environment: Internal  and  External
 *
 * See Also:  UF_TAG_unregister_event_cb
 *
 * History: This function was originally released in V15.0.
 ****************************************************************************/
extern UFUNEXPORT int UF_TAG_register_event_cb(
    UF_TAG_event_fn_t callback,         /* <I>
                                        Callback function
                                         */
    void *closure,                      /* <I>
                                        Pointer passed to callback on
                                        each call
                                        */
    int *callback_id                    /* <O>
                                        Identifier for callback
                                        */
);

/****************************************************************************
 * Unregister a previously registered callback.
 *
 * Environment: Internal  and  External
 *
 * See Also:  UF_TAG_register_event_cb
 *
 * History: This function was originally released in V15.0.
 ****************************************************************************/
extern UFUNEXPORT int UF_TAG_unregister_event_cb(
    int callback_id                     /* <I> - identifier of callback */
);

/****************************************************************************
*   Set a flag that determines if an Open C executable will issue
*   warnings when a function that is scheduled to be retired is called.
*   This can be used to alert the NX Open programmer that modification to
*   their program is required.
*
*   When routines are planned to be removed from the NX Open interface, the
*   prototype will be moved to uf_retiring.h, along with a description of
*   what the NX Open programmer should do.  A warning can be issued when
*   any of these routines are called by a NX Open application.  This routine
*   allows the NX Open programmer to set the value of this flag.
*
*   This routine overrides the environment variable
*   UGII_USING_RETIRING_FUNCTIONS which can be set by the user to get
*   the same warnings.  This routine is meant to be used when the programmer
*   wants to force a particular value for a program.
*
*   Environment: Internal and External
*
*   See Also:
*
*   History: Released in V16.0
****************************************************************************/
extern UFUNEXPORT int UF_set_retiring_flag(
      int value   /* <I>
                     0 = Don't warn user at all, this is the default
                     1 = Output a single message if any function is called
                         that is planned to be obsoleted
                     2 = Output a message for each function called that
                         is planned to be obsoleted.  The message will include
                         the routine name, and the number of times called.
                  */
);


/****************************************************************************
*   Output a message to the syslog.
*
*   This message can be used to print run time information about the NX Open
*   program to the syslog and is useful for state checking, validation and
*   debugging.
*
*   Printing the trace is especially useful while debugging and reporting a
*   problem.
*
*   Environment: Internal and External
*
*   See Also:
*
*   History: Released in V18.0
****************************************************************************/
extern UFUNEXPORT int UF_print_syslog(
       char *message, /* <I>
                         Message to be output to the syslog
                      */
       logical trace  /* <I>
                         TRUE = Print the stack trace along with the message
                         FALSE = Print only the message
                      */
);

/****************************************************************************
*   Get name of the current syslog
*
*   Environment: Internal and External
*
*   See Also:
*
*   History: Released in NX2.0.5
****************************************************************************/

extern UFUNEXPORT int UF_ask_syslog_filename(
       char **filename /* <OF>
                         pointer to dynamically allocated path
                         filename must be freed with UF_free()
                      */
);

/****************************************************************************
*   Find a given subdirectory and file.  This routine will traverse all the
*   directories specified in the file custom_dirs.dat and ug_custom_dirs.dat
*   looking for the file specified by the given subdirectory and filename.
*   This routine will return the first file found.
*
*   Environment: Internal and External
*
*   See Also:  UF_find_all_subdirectories
*
*   History: Released in NX 1.0
****************************************************************************/
extern UFUNEXPORT int UF_find_file(
       const char *subdirectory, /* <I>
                                    The subdirectory in which to look for the
                                    given file.
                           */
       const char *filename, /* <I>
                              The filename to look for, including any extension.
                       */
       char **path  /* <OF>
                       The filename found.  If no file is found, **path will
                       be NULL.  The path must be freed by calling UF_free.
                       */
);

/****************************************************************************
*   Find all subdirectories of a given name in the directories specified in
*   the file custom_dirs.dat and ug_custom_dirs.dat.  Since the same
*   subdirectory may be in multiple directories, an array of path names
*   will be returned.  As an example searching for the subdirectory "startup"
*   will return almost all of the directories, since this is a standard
*   subdirectory.
*
*   Environment: Internal and External
*
*   See Also:  UF_find_file
*
*   History: Released in NX 1.0
****************************************************************************/
extern UFUNEXPORT int UF_find_all_subdirectories(
       const char *subdirectory, /* <I>
                              The subdirectory to look for.
                           */
       int *num_found, /* <O>
                              The number of subdirectories found.
                       */
       char ***path  /* <OF,len:num_found>
                       The list of subdirectories found.  This must be
                       freed by calling UF_free_string_array.
                       */
);

/****************************************************************************
*   Select the listing device.  The listing device can be set to a file,
*   the listing window, or both file and listing window.  The listing
*   device can also be set to no output.
*
*   Return:
*        0 = Success
*        2 = Listing device is unavailable
*        otherwise an error code
*
*   Environment: Internal and External
*
*   See Also:  UF_UI_open_listing_window
*  UF_UI_close_listing_window
*  UF_UI_write_listing_window
*
*   History:
****************************************************************************/
extern UFUNEXPORT int uc4400(
int listing_device,    /*<I>
                       The listing device to use:
                         = 0 standard listing window
                         = 4 output to a file
                         = 8 output to both file and listing window
                         = 9 No output is written
                       */
char *file_spec,       /*<I>
                       This is only used for output to a file.  This is
                       the file specification for the output file, and
                       must be less than MAX_FSPEC_NCHARS characters.
                       */
int ip3                /*<I>
                       This is no longer used.
                       */
);

/****************************************************************************
*   Query the current disposition of the listing device.
*
*   Environment: Internal and External
*
*   Returns:
*      0 = Listing device is set to the listing window
*      4 = Listing device is set to a file
*      8 = Listing device is set to both file and the listing window
*      9 = Listing device is set to NULL
*   otherwise the return is an error code.
*
*   See Also:  UF_UI_open_listing_window
*  UF_UI_close_listing_window
*  UF_UI_write_listing_window
*  uc4400
*
*   History:
****************************************************************************/
extern UFUNEXPORT int uc4409(
char file_name[ MAX_FSPEC_BUFSIZE ], /* <O>
                 For return code 4 or 8, this is the file specification
                 of the listing device file.
                 */
int *ir3         /* <O>
                 Unused.
                 */
);

/****************************************************************************
*   Query the current NX Open program environment for the current image.
*
*   Note: This value is updated during initialization so it is set for
*   each image and won't remember the information from previous images.
*
*   Environment: Internal and External
*
*   Returns:
*     Void
*
*   History:
****************************************************************************/
extern UFUNEXPORT void FTN(uf3192)(
int *ir1 /* <O>
            The environment that the NX Open program is running in.
            0 is External Open, 1 is Internal Open.
         */
);

/******************************************************************************
 ******************************************************************************
 *****     WARNING:  The routines that follow will be obsoleted soon.     *****
 *****     Do not use them!  Use their indicated replacements.            *****
 ******************************************************************************
 ******************************************************************************
*/

/* uf4401 opens the listing device set by uc4400 for output
   if you only need to open the listing window for output
   (and not a particular listing device set by uc4400)
   this function may be replaced with UF_UI_open_listing_window */
extern UFUNEXPORT void FTN(uf4401)(int *ir1);

/* uf4402 closes listing device set by uc4400
   if you only need to close the listing window
   (and not a particular device set by uc4400)
   this function may be replaced by UF_UI_close_listing_window */
extern UFUNEXPORT void FTN(uf4402)(void);

/* uc4403 write character string to listing device set by call to uc4400
   if you only need to write to the listing window
   (as opposed to a listing device set by uc4400)
   this function may be replaced with UF_UI_write_listing_window */
extern UFUNEXPORT int uc4403(const char *cp1/* <I> */);

/* uc4404 write character string and integer to listing device set by uc4400
   if you only need to write the data to the listing window
   (and not a particular device set by uc4400)
   this function may be replaced by UF_UI_write_listing_window */
extern UFUNEXPORT int uc4404(const char *cp1/* <I> */, int ip2);

/* uc4406 write character string and real to listing device set by uc4400
   if you only need to write the data to the listing window
   (and not a particular listing device set by uc4400)
   this function may be replaced by UF_UI_write_listing_window */
extern UFUNEXPORT int uc4406(const char *cp1/* <I> */, double rp2);

/***************************************************************************

  ***************************************************************************/

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif /* UF_INCLUDED */


