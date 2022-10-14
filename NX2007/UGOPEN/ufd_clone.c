/*
===============================================================================


                     Copyright 2007 UGS Corp.
                       All Rights Reserved.

===============================================================================

File description:

This file implements the command-line utility ug_clone for driving the
Unigraphics clone functionality, including Clone based Import and
Export. It defines a main style entry point UFD_clone_main. The
file ufd_clone_main.c provides example code showing how to use the
UFD_clone_main function.

This file *is* the implementation of the shipped ug_clone utility. If
you wish to modify or extend this utility, you can use the code in
this file as a base to write your own version.

No attempt is made to implement a user_name naming mechanism. If
user_name is specified as a default_naming, the operation will fail
unless all default names are satisfied by loading log files.


===========================================================================*/
#include <unidefs.h>

#include <stdlib.h>
#include <stdarg.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <error_finally.h>
#include <PDM_PDIClientCachers.hxx>

#include <uf.h>
#include <uf_attr.h>
#include <uf_assem.h>
#include <uf_cfi.h> /* for uc4621 */
#include <uf_part.h>
#include <uf_clone.h>
#include <ufd_clone.h>
#include <uf_ugmgr.h>
#include <uf_kf_ugmgr.h>
#include <error_privileged.h>

/*================================================================================

  Typedefs

  ================================================================================*/

typedef void (*switch_handler_t)(const char *);

typedef struct switch_descriptor_s
{
    char *switch_name;          /* the name of the switch */
    int min_chars;              /* the minimum number of characters required to match this switch */
    switch_handler_t handler;   /* function which will process the switch, receives the value if any */
    logical multi;              /* true if this switch can occur more than once */
    logical seen;               /* true if this switch has been seen
                                   already */
    char * help_text;           /* help text added to switch when help is printed */
} switch_descriptor_t, *switch_descriptor_p_t;

/*================================================================================

  Function Declarations

  ================================================================================*/

/*
  output functions
*/
static void error(char *format,...);
static void log_and_stderr_printf (char *format,...); /* <BV> PR# 4285623 */
static void message(char *format,...);
static int  vlog_and_stderr_printf( const char * format, va_list args ); /* <BV> PR# 4285623 */


/*
  argument processing functions
*/

static void ignore_arg(const char *ignored);
static void operation(const char * switch_value);
static void assembly(const char * switch_value);
static void part(const char * switch_value);
static void default_checkin(const char * switch_value);
static void default_checkout(const char * switch_value);
static void default_action(const char * switch_value);
static void default_naming(const char * switch_value);
static void default_folder(const char * switch_value);
static void default_directory(const char * switch_value);
static void default_type(const char * switch_value);
static void associated_file_root_dir(const char * switch_value);
static void copy_associated_files(const char * switch_value);
static void copy_nonmaster(const char * switch_value);
static void default_owner(const char * switch_value);
static void retain_ownership(const char * switch_value);
static void name_rule(const char * switch_value);
static void assign_default_project(const char * switch_value);
static void load_log_file(const char * switch_value);
static void save_log_file(const char * switch_value);
static void help(const char * ignored);
static void dryrun(const char *ignored);
static void family_treatment(const char * switch_value);
static void folder(const char * switch_value);
static void directory(const char * switch_value);
static void revision_rule(const char *switch_value);
static void propagate_actions(const char * switch_value);
static void autotranslate_mode(const char * switch_value);
static void export_dfa_kf( const char * switch_value);
static void export_dfa_list( const char *ignored );
static void export_extern_files(const char *switch_value);
static void import_dfa_kf( const char * switch_value);
static void import_dfa_list( const char *ignored );
static void rev_up_read_only(const char *ignored);
static void validation_mode(const char * switch_value);
static void validation_rule(const char * switch_value);
static void abort_import_on_fail(const char * switch_value);
static void treat_validation_warning(const char * switch_value);
static void treat_validation_outdated(const char * switch_value);
static void attach_log_file( const char *ignored ); /* NXDM MultiCad Clone (NXDM50101) project */
static void copy_related_drawings(const char* switch_value);  // Fetch Related Drawings during clone/export
static void copy_related_cae_parts(const char* switch_value); // Fetch Related CAE parts during clone/export
static void id_display_rule(const char * switch_value);
static void exclude_reference_only(const char* switch_value);
static void exclude_ngc(const char* switch_value);

/*
  Utility functions for  processing strings
*/
static char * copy_string(const char *string);
static int compare_strings(const char * string1, const char * string2);
static logical is_prefix(const char * prefix, const char * string, int min_match_required);
static const char *find_value(const char * switch_spec);
static switch_descriptor_p_t match_switch(const char * switch_spec);

/*
  Other functions
*/

static void process_switches(int argc, char **argv);
static void quit(int exit_code);
static void uf_check(int return_code, char *error_format,...);
static UF_CLONE_notify_response_t callback_fn (UF_CLONE_notify_cb_t callback_point, const char *input_part,
                                               const void *data);
static void register_callbacks(void);
static int ug_legacy_trans(const char input[ MAX_FSPEC_BUFSIZE ], char output[ MAX_FSPEC_BUFSIZE ]);
static logical is_the_value_dfa( const char *value, int option );

/* <novak> 05-Dec-08 Functions to handle encryption
*/
static void handle_encryption(int argc, char **argv,  char *output_str);
static logical parameter_set(int argc, char **argv, char *switch_name, char *value);

/*================================================================================

  Global Variables

  ================================================================================*/

static switch_descriptor_t switch_descriptors[] = {
/*   switch name                min   handler function          multi seen
                               length                                      */
    {"tcserver_port",             13,  ignore_arg,               false, false,
     "=9999"},
    {"pim",                       3,  ignore_arg,               true, false,
     "=yes to initialize Teamcenter Integration for NX rather than native NX"}, /* multi is harmless, though not useful */
    {"user",                      1,  ignore_arg,               false, false,
     "=<user> to specify Teamcenter user name"},
    {"group",                     1,  ignore_arg,               false, false,
     "=<group> to specify Teamcenter group name"},
    {"password",                  1,  ignore_arg,               false, false,
     " to specify Teamcenter password"},
    {"pf",                        2,  ignore_arg,               false, false,
     "=<filename> file to specify the Teamcenter password"},
    {"encrypt",                   1,  ignore_arg,               false, false,
     " to specify Teamcenter password"},
    {"corba_ior_file",            14,  ignore_arg,               false, false,
     " to specify imanserver IOR file"},
    {"corba_soa_ior_file",        18,  ignore_arg,               false, false,
     " to specify corba SOA IOR file"},
    {"http_url",                   8,  ignore_arg,               false, false,
     " to specify http url for 4 tier configuration"},
    {"http_cookie",               11,  ignore_arg,               false, false,
     " to specify http cookie for 4 tier configuration"},
    {"http_vmid",                  9,  ignore_arg,               false, false,
     " to specify http vmid for 4 tier configuration"},
    {"operation",                 1,  operation,                false, false,
     "=clone|edit|import|export required, must precede arguments below"},
    {"family_treatment",          3,  family_treatment,         false, false,
     "=lose|strip_status|error specifies how to treat Part Family \nMembers\nIf adding an assembly containing Family Members, this switch must be positioned \nbefore the -assembly switch.\nDefault is error"
    },
    {"validation_mode",          12,  validation_mode,         false, false,
     "=off|import_from_part|run_validation|run_validation_hybrid \nspecifies how to import validation results\nthis switch must be positioned before the -assembly switch, -part switch \nand -dryrun switch.\nDefault is off"
    },
    {"validation_rule",          12,  validation_rule,         false, false,
    "=<validation rule dataset name or validation rule file name> \nspecifies the dataset or native file name used to qualify the validation \nresults to be imported.\nthis switch must be specified when -validation_mode is not off. \nthe name should be in CLI format. "
    },
    {"abort_import_on_fail",  12,  abort_import_on_fail,         false, false,
     "=no|yes specifies whether to abort the part importing \nwhen validation results do not satisfy the validation rule.\nDefault is no"
    },
    {"treat_validation_warning_as_pass",  18,  treat_validation_warning,         false, false,
      "=yes|no specifies how to treat the \nvalidation result status of pass with warning.\nDefault is yes"
    },
    {"treat_validation_outdated_as_pass",  18,  treat_validation_outdated,         false, false,
    "=no|yes specifies how to treat the \nvalidation result status of pass but outdated.\nDefault is no"
    },
    {"assembly",                  4,  assembly,                 true,  false,
     "=<root assembly> to add an assembly to the operation"},
    {"part",                      3,  part,                     true,  false,
     "=<single part> to add a part to the operation"},
    {"directory",                 3,  directory,                true,  false,
     "=<directory name> to add all assemblies in that directory to the operation. \nThe -dir option is for adding the Top parts involved in the clone operation"},
    {"folder",                 3,  folder,                true,  false,
     "=<folder name> as <user>:<folder>:<folder...> to add all assemblies in \nthat folder to the operation"},
    {"default_checkin",           14, default_checkin,          false, false,
     "=yes:yes|yes:no|no, default is no"},
    {"default_checkout",          14, default_checkout,         false, false,
     "=yes:<comment>|no, default is no"},
    {"default_action",            9,  default_action,           false, false,
     "=clone|retain|overwrite|use_existing|exclude|new_revision"},
    {"default_naming",            9,  default_naming,           false, false,
     "=autogen|autotranslate|autotranslate_using_altid|name_rule|user_name"},
    {"autotranslate_mode",         3,  autotranslate_mode,       false, false,
     "=<default|legacy> \nspecifies whether autotranslate mode for import should be:\n\tthe default or \n\tlegacy compatible (use DB_ attributes if present otherwise leaf name)\nDefault is default"},
    {"default_type",              9,  default_type,             false, false,
     "=<item_type> specifies default Teamcenter item type"},
    {"associated_file_root_dir",  4,  associated_file_root_dir, false, false,
     "=<directory> specifies default Teamcenter Associated \nfile directory"},
    {"copy_associated_files",     6,  copy_associated_files,    false, false,
     "=yes|no specifies whether to copy Teamcenter Associated \nfiles\ndefault is yes"},
    {"copy_related_drawings",     17,  copy_related_drawings,    false, false,
     "=yes|no specifies whether to copy related independent drawing parts \nthis switch is to be used before adding an/a assembly/part to \nthe operation \ndefault is no"},
    {"copy_related_cae_parts",    16,  copy_related_cae_parts,    false, false,
     "=<none|ideal|fem|all> specifies whether to copy related independent \ncae parts of selected type \nthis switch is to be used before adding an/a assembly/part to \nthe operation \ndefault is none"},
    {"copy_non_master",           6,  copy_nonmaster,           true,  false,
     "=<nonmaster-type>:yes|no\nspecifies whether to copy Teamcenter Non-Master files"},
    {"default_owner",             9,  default_owner,            false, false,
     "=<user>:<group> specifies default Teamcenter user and group \nto own parts"},
    {"retain_ownership",          12,  retain_ownership,        false, false,
    "=yes|no specifies whether to retain original ownership for the cloned part objects. \n(clone only).\nIn case both retain_ownership flag and default_owner are used, default_owner will be ignored." },
    {"default_project",           9, assign_default_project,    false, false,
     "=yes|no specifies whether the items to be cloned assigned under \nthe default project mentioned in the customer defaults or not."},
    {"name_rule",                 1,  name_rule,                false, false,
     "=prepend:<string>|append:<string>|replace:<base_string>:\n<replace_string>|rename:<string>"},
    {"default_folder",            9,  default_folder,           false,  false,
     "=<default-folder>"},
    {"default_directory",         9,  default_directory,        false,  false,
     "=<default-directory>"},
    {"load_log_file",             1,  load_log_file,            true,  false,
     "=<log-file-name>"},
    {"save_log_file",             1,  save_log_file,            false, false,
     "=<log-file-name>"},
    {"revision_rule",             1,  revision_rule,            true, false,
     "=<revision rule name>\n if specified, then it should be before the assembly switch"},
    {"dryrun",                    2,  dryrun,                   false, false,
     ""},
    {"propagate_actions",         9,  propagate_actions,        false, false,
     "=<yes|no> specifies whether to propagate action settings \nto referenced and referencing parts\nDefault is no. \nThis option is intended for use by other applications driving ug_clone, \nnot for direct use."},
    {"export_dfa_kf",             13,  export_dfa_kf,            false, false,
     " specify this option in the beginning of the argument list \nto export the dfa files\nExamples to use export_dfa_kf\n\t1.ug_clone -pim=yes -export_dfa_kf=dfa_only -o=export -part=\n<dfaclassname> (for dfa files)\n\t2.ug_clone -pim=yes -export_dfa_kf=dfa_in_part -o=export -part=\n<@DB/testprt/A> (for dfa files referenced by part)"},
    {"export_dfa_list",           15,  export_dfa_list,            false, false,
     " specify this option to export the dfa filenames listed in \nan input file\nExamples to use export_dfa_list\n\tug_clone -pim=yes -export_dfa_kf=dfa_only -export_dfa_list -o=\nexport -part=<input file list name>"},
     {"export_external_files",      15,  export_extern_files,      false, false,
     " <yes|no> specifies whether to export the external files referenced."},
    {"import_dfa_kf",             13, import_dfa_kf,            false, false,
     " specify this argument in the beginning of the argument list \nto import dfa files.\nExample to use import_dfa_kf\n\tug_clone -pim=yes -o=import -import_dfa_kf=dfa_only -part=\n<dfa_filename>."},
    {"import_dfa_list",           15, import_dfa_list,           false, false,
     " specify this option to import the dfa filenames listed in \nan input file\nExample to use import_dfa_list\n\tug_clone -pim=yes -o=import -import_dfa_kf=dfa_only -import_dfa_list \n-part=<input file list name>"},
    {"rev_up_read_only",          6,  rev_up_read_only,         false, false,
     " specifies that new revision will be created if operation=\nIMPORT,\naction=OVERWRITE, and dataset is read only"},
    {"attach_log_file",          6,  attach_log_file,           false, false,
     " specifies that the clone log file will be attached as named \nreference to root nodes"}, /* NXDM MultiCad Clone (NXDM50101) project */
    {"id_display_rule",   15,  id_display_rule,         false, false,
     "=<identifier display rule>\n Specifies identifier display rule to be used for current export. \n Value will be igored if default_naming is not autotranslate_using_altid or if given id display rule is invalid or can't be set." },
    {"exclude_reference_only",   11, exclude_reference_only,     false, false,
     "=yes|no specifies whether to apply exclude action to reference only components"},
    {"exclude_ngc",   11, exclude_ngc,     false, false,
     "=yes|no specifies whether to apply exclude action NGC components" },
    {"help",                      1,  help,                     false, false,
     " produces this message"}

};

static char *operation_names[] = {
    "clone",
    "edit",
    "import",
    "export"
};

static const char *switch_starts = "-";

#ifdef WNT
static const char * switch_terminators = "=:";
#else
static const char *switch_terminators = "=";
#endif

/* <junankar> 17-Aug-2012
   If stdarg.h does not supply a platform specific version of va_copy, then use this
*/
#ifndef va_copy
#define va_copy(dst, src) ((dst) = (src))
#endif

static const char * program_name = NULL;

static char * part_being_operated_on = NULL;

/* DFA global variables */
static logical is_dfa          = false;
static logical is_dfa_in_part  = false;
static logical is_dfa_list     = false;
static logical dfa_export      = false;
static logical dfa_import      = false;
static int dfa_export_option;

/*================================================================================

  Function Definitions

  ================================================================================*/

// <deshpanm> 25-Jul-2020
// assertion handler - write into syslog and continue
static ERROR_assertion_option_t ug_clone_assertion_handler(const char* file, int line, const char* msg)
{
    log_and_stderr_printf("***ASSERTION: File: %s Line: %d %s", file, line, msg);
    return ERROR_assert_normally;
}

/*
  copies the given string into allocated memory
*/
static char * copy_string(const char *string)
{
    char * result;
    int ier;
    result = (char *)UF_allocate_memory(strlen(string) +1, &ier);
    if (ier != 0)
        error("Failed to allocate memory copy string %s",string);

    strcpy(result,string);
    return result;
}

/*
  returns the  index of the first character at which the two strings
  differ, compared case-independently
*/
static int compare_strings
(
    const char * string1,
    const char * string2
)
{
    int i = 0;

    for (i = 0; string1[i] != '\0' && string2[i] != '\0'; i++)
    {
        if (tolower(string1[i]) != tolower(string2[i]))
            break;
    }

    return (i);
}

/*  <deshpanm> 16-Jun-2010
   case insensitive string comparison function
*/
static int str_compare_i(const char *a, const char *b)
{
    if ( a == NULL )
    {
        return ( b == NULL ) ? 0 : -1;
    }
    else
    {
        if ( b == NULL )
        {
            return 1;
        }

        while (*b != '\0')
        {
            char ca = toupper(*a);
            char cb = toupper(*b);

            if (ca != cb)
                return ca - cb;

            a++;
            b++;
        }
    }

    return *a - *b;
}

static logical is_prefix (const char *prefix, const char *string, int min_match_required)
{
    int matched_length = compare_strings(prefix, string);

    /*
      if we've matched at least min_match_required chars, and also matched the
      whole of the given prefix, the result is true
   */
    return (matched_length >= min_match_required &&
            matched_length == strlen(prefix));

}
/*
  returns a pointer to the position in the given string *after* the
  valid switch terminator characters for this platform, or NULL if no
  value was found.
*/

static const char *find_value(const char *switch_spec)
{
    int switch_length = strcspn(switch_spec,switch_terminators);
    if (switch_spec[switch_length] == '\0')
        return NULL;
    else
        return &(switch_spec[switch_length+1]);
}

/*
  matches input switches against the allowed switches, allowing
  abbreviations by recognizing a match if the whole of the input
  switch matches *and* it is longer than the minimum number of
  characters required for that switch.
*/
static switch_descriptor_p_t match_switch(const char * switch_spec)
{
    int i = sizeof(switch_descriptors)/sizeof(switch_descriptors[0]);
    const char * switch_start = &(switch_spec[1]);
    char switch_name[64];
    int switch_length = strcspn(switch_start,switch_terminators);
    /*
      check that switch begins with a valid char, strchr will return
      NULL if switch[0] is not found in switch_starts
    */
    if (strchr(switch_starts,switch_spec[0]) == NULL)
        return NULL;

    strncpy(switch_name,switch_start,switch_length);
    switch_name[switch_length] = '\0';

    while (--i >= 0)
    {
        if (is_prefix(switch_name, switch_descriptors[i].switch_name,switch_descriptors[i].min_chars))
            return   &(switch_descriptors[i]);
    }
    return NULL; /* not found */

}

static void process_switches(int argc, char **argv)
{
    int i                   = 0;
    int j                   = 0;
    int default_rev_rule    = 0;


    program_name = argv[0];

    for (i = 1; i < argc; i++)
    {
        switch_descriptor_p_t descriptor = match_switch(argv[i]);

        if (descriptor == NULL)
        {
            // <g0oqef> 23-Oct-2017 TCIN120002
            // Skip ECN switch from raising error out as this is used to set Active Change Notice and handled at the UGMGR initialize
            char switch_name[64];
            int switch_length = strcspn(argv[i], switch_terminators);
            strncpy(switch_name, argv[i], switch_length);
            switch_name[switch_length] = '\0';
            if (strcmp(switch_name,"-ecn")==0)
                continue;
            error("Unknown switch %s, use -help for usage information", argv[i]);
        }

        if (descriptor != NULL)
        {
            if (descriptor->seen && !descriptor->multi)
                error("Repeated switch %s", argv[i]);

            descriptor->seen = true;

            descriptor->handler(find_value(argv[i]));

            // <deshpama> 13-Jul-2011 Fix PR#2172464
            // Display warning message, if assembly argument not found after revision_rule
            if (strcmp(descriptor->switch_name, "revision_rule") == 0)
            {
                for (j = i + 1; j < argc; j++)
                {
                    // <ingle> 06-May-2015 PR#7375423
                    // Also add folder to the switch which can come directly after revision_rule
                    switch_descriptor_p_t assem_descriptor = match_switch(argv[j]);
                    if (assem_descriptor != NULL &&
                        (strcmp(assem_descriptor->switch_name, "assembly") == 0 ||
                            strcmp(assem_descriptor->switch_name, "revision_rule") == 0 ||
                            strcmp(assem_descriptor->switch_name, "part") == 0 ||
                            strcmp(assem_descriptor->switch_name, "folder") == 0))
                    {
                        default_rev_rule = 1;
                        break;
                    }
                }

                if (default_rev_rule == 0)
                {
                    log_and_stderr_printf("\nWarning: %s : %s must specify before assembly.\n", descriptor->switch_name, find_value(argv[i]));
                }
                else
                {
                    default_rev_rule = 0;
                }
            }
        }
    }
}

static void report_log_file_failure(UF_CLONE_log_file_failure_p_t failure, const char * log_file_name)
{
    if (failure->invalid_token != NULL)
        log_and_stderr_printf("\nWarning: Invalid token \"%s\" found on line %d of log-file %s\n",
                failure->invalid_token,failure->line_number,log_file_name);
    else
        log_and_stderr_printf("\nWarning: Invalid log file detected on line %d of %s\n",failure->line_number,log_file_name);
    UF_free(failure->input_part_name);
    UF_free(failure->invalid_token);
}

static void report_naming_failures(UF_CLONE_naming_failures_p_t failures)
{
    int i;

    for (i = 0; i < failures->n_failures; i++)
    {
        char input_display_name[ MAX_FSPEC_BUFSIZE ];
        char output_display_name[ MAX_FSPEC_BUFSIZE ];
        char error_message[ MAX_LINE_BUFSIZE ];

        int rc = UF_PART_name_for_display(failures->input_names[i],input_display_name);

        if (rc != 0)
            strncpy(input_display_name,failures->input_names[i], MAX_FSPEC_BUFSIZE-1);

        if (failures->output_names[i] == NULL)
            strcpy(output_display_name,"");
        else
        {
            rc = UF_PART_name_for_display(failures->output_names[i], output_display_name);
            if (rc != 0)
                strncpy(output_display_name,failures->output_names[i], MAX_FSPEC_BUFSIZE-1);
        }

        rc = UF_get_fail_message(failures->statuses[i],error_message);
        if (rc != 0)
            strcpy(error_message,"Unknown error");

        log_and_stderr_printf("\nWarning: Error renaming %s%s%s: %s\n",input_display_name,
                 output_display_name[0] == '\0' ? "" : " -> ",
                 output_display_name[0] == '\0' ? "" : output_display_name,
                 error_message);
    }

    /*
      free the fields that need it
    */
    UF_free_string_array(failures->n_failures,failures->input_names);
    UF_free_string_array(failures->n_failures,failures->output_names);
    UF_free(failures->statuses);

}

static int report_load_status(UF_PART_load_status_p_t load_status)
{
    int i;
    int result = 0;

    /*
      report missing components

    */
    for (i = 0; i < load_status->n_parts; i++)
    {
        if (load_status->statuses[i] == UF_CLONE_err_comp_not_found)
        {
            char display_name[ MAX_FSPEC_BUFSIZE ];
            int display_rc = UF_PART_name_for_display(load_status->file_names[i],display_name);
            if (display_rc != 0)
                strncpy(display_name,load_status->file_names[i], MAX_FSPEC_BUFSIZE-1);

            log_and_stderr_printf("\nWarning: Component not found: %s\n",display_name);
        }
    }

    /*
      report out of sync BVRs
    */
    for (i = 0; i < load_status->n_parts; i++)
    {
        if (load_status->statuses[i] == UF_CLONE_err_bvr_out_of_sync)
        {
            char display_name[ MAX_FSPEC_BUFSIZE ];
            int display_rc = UF_PART_name_for_display(load_status->file_names[i],display_name);
            if (display_rc != 0)
                strncpy(display_name,load_status->file_names[i], MAX_FSPEC_BUFSIZE-1);

            log_and_stderr_printf("\nWarning: BVR out of sync: %s\n",display_name);
        }
    }

    /*
      check for other errors
    */
    for (i = 0; i < load_status->n_parts; i++)
    {
        if (load_status->statuses[i] != UF_CLONE_err_bvr_out_of_sync &&
            load_status->statuses[i] != UF_CLONE_err_comp_not_found)
        {
            result = load_status->statuses[i];
            break;
        }
    }

    /*
      free the load status fields that need it
    */
    UF_free_string_array(load_status->n_parts,load_status->file_names);
    UF_free(load_status->statuses);

    return result;
}

/*
  Argument processing functions
*/
/*
   function to be called for switches which should be ignored

*/
static void ignore_arg(const char *ignored)
{
    return;
}
/*
   function which prints out a help message built from the argument descriptors structure

*/

static void help(const char *ignored)
{
    int switch_count = sizeof(switch_descriptors)/sizeof(switch_descriptors[0]);
    int i = 0;

    message("Usage: %s ",program_name);

    for (i = 0; i < switch_count; i++)
    {
        char buffer[64];

        if (switch_descriptors[i].min_chars < strlen(switch_descriptors[i].switch_name))
        {
            strncpy(buffer,switch_descriptors[i].switch_name,switch_descriptors[i].min_chars);
            buffer[switch_descriptors[i].min_chars] = '\0';
            if ( strlen(buffer) < 64 )
            {
                strncat(buffer,"[",64-strlen(buffer));
                if ( strlen(buffer) < 64 )
                {
                    strncat(buffer,switch_descriptors[i].switch_name + switch_descriptors[i].min_chars, 64-strlen(buffer));
                    if ( strlen(buffer) < 64 )
                    {
                        strncat(buffer,"]", 64-strlen(buffer));
                    }
                }
            }
        }
        else
            strncpy(buffer,switch_descriptors[i].switch_name,64-1);
        message("%c%s%s",switch_starts[0],buffer,switch_descriptors[i].help_text);
        if (switch_descriptors[i].multi)
            message("\t\tmay be repeated");
    }

    quit(EXIT_SUCCESS);
}

/*
  Function which processes the operation switch, checks for each of the
  valid  operation types (which may be abbreviated to unique prefices),
  reports an error (and quits) if the operation type is not correctly specified
*/
static void operation(const char * switch_value)
{
    char *noWarning = NULL;

    /*<x_sardea> 22-Jul-2004 :Fix for warning C4701
    */
    UF_CLONE_operation_class_t op = UF_CLONE_clone_operation;

    if (switch_value == NULL || switch_value[0] == '\0')
        error("Value required for operation switch");
    else if (is_prefix(switch_value,"clone",0))
        op = UF_CLONE_clone_operation;
    else if (is_prefix(switch_value,"edit",2))
        op = UF_CLONE_edit_operation;
    else if (is_prefix(switch_value,"export",2))
        op = UF_CLONE_export_operation;
    else if (is_prefix(switch_value,"import",0))
    {
        op = UF_CLONE_import_operation;

        UF_translate_variable("UGII_UGMGR_TCIN_IMPORT_NO_WARN", &noWarning);
        if (noWarning == NULL || strcmp(noWarning, "yes") != 0)
        {
            log_and_stderr_printf("-------------------------------------------------------------------\n");
            log_and_stderr_printf("Warning: The \"-o[peration]=import\" option will be deprecated from ug_clone utility.\n");
            log_and_stderr_printf("Use the \"tcin_import\" utility instead.\n");
            log_and_stderr_printf("-------------------------------------------------------------------\n");
        }
    }
    else
        error("Unexpected value %s given to operation switch",switch_value);

    uf_check(UF_CLONE_initialise(op),"while initializing %s operation",operation_names[op]);

    /*
      Make sure that a log file gets generated with a default name
      if the user never sets one explicitly.
    */
    {
        char default_log_file[ MAX_FSPEC_BUFSIZE ];
        sprintf(default_log_file,"%s.clone",operation_names[op]);
        uf_check(UF_CLONE_set_logfile(default_log_file),"While setting default log file to %s",default_log_file);
    }

    if ( op == UF_CLONE_export_operation )
        dfa_export = true;
}

static void assembly(const char * switch_value)
{
    if (switch_value == NULL || switch_value[0] == '\0')
        error("Value required for assembly switch");
    else
    {
        /* check the input value whether it is assembly or dfa */
        /*if dfa is present do some other processing */
        if( !is_the_value_dfa( switch_value, UF_KF_UGMGR_EXPORT_DFA_IN_ASSEMBLY ) )
        {
            UF_PART_load_status_t load_status;
            int rc = UF_CLONE_add_assembly(switch_value,&load_status);
            int load_stat_rc = 0;
            if (load_status.failed)
            {
                load_stat_rc = report_load_status(&load_status);
                rc = (load_stat_rc == 0) ? rc : load_stat_rc;
            }

            // <deshpanm> 14-Jun-2010 PR#1667647 skip the failed parts during processing
            // instead of exiting the clone process with error
            if(rc != 0)
            {
                int message_code = 0;
                char message[ MAX_LINE_BUFSIZE ];
                char display_name[ MAX_FSPEC_BUFSIZE ];

                int display_rc = UF_PART_name_for_display(switch_value, display_name);
                if (display_rc != 0)
                    strncpy(display_name, switch_value, MAX_FSPEC_BUFSIZE-1);

                message_code = UF_get_fail_message(rc, message);
                if (message_code != 0)
                    strcpy(message,"Unknown error!");

                log_and_stderr_printf ("\nWarning: (%d) - %s\n\tWhile adding assembly %s to the operation\n", rc, message, display_name);
            }
        }
    }
}

static void part(const char *switch_value)
{
    if (switch_value == NULL || switch_value[0] == '\0')
        error("Value required for part switch");
    else
    {
        if (!dfa_import)
        {
            /* check the input value whether it is part or dfa */
            /*if dfa is present do some other processing */
            if( !is_the_value_dfa( switch_value, UF_KF_UGMGR_EXPORT_DFA_IN_PART) )
            {
                int rc = UF_CLONE_add_part(switch_value);

                /* <APB> 26-May-1999
                   allow out of sync BVR but warn about it
                */
                if (rc == UF_CLONE_err_bvr_out_of_sync)
                {
                    log_and_stderr_printf("\nWarning: BVR out of sync: %s\n",switch_value);
                    rc = 0;
                }
                else
                    uf_check(rc,"While adding part %s to the operation",switch_value);
            }
        }
    }
}

/*
  parses a switch values of no, yes:no and yes:yes to match the checkin
  data values checkin, and error if not checked in. There's no point in
  setting error if not checked in if checkin is not set. This function
  will in fact accept an prefix of yes as meaning yes, and anything else
  as meaning no!
*/
static void default_checkin(const char *switch_value)
{
    UF_CLONE_checkin_data_t checkin_data;
    char * switch_copy = NULL;
    char *switch_part = NULL;

    if (switch_value == NULL || switch_value[0] == '\0')
        error("Value required for default_checkin switch");

    switch_copy = copy_string(switch_value);

    switch_part = strtok(switch_copy,":");

    checkin_data.checkin = false;
    checkin_data.error_if_no_co = false;

    if (is_prefix(switch_part,"yes",0))
    {
        checkin_data.checkin = true;

        switch_part = strtok(NULL,":");

        if (switch_part == NULL)
            error("value for default_checkin switch must be no, yes:no or yes:yes");

        checkin_data.error_if_no_co = is_prefix(switch_part,"yes",0);
    }

    UF_free(switch_copy);

    uf_check(UF_CLONE_set_def_ci(&checkin_data),"While setting default checkin to %s",switch_value);
}

static void default_checkout(const char *switch_value)
{
    UF_CLONE_checkout_data_t checkout_data;
    char * switch_copy = NULL;
    char *switch_part = NULL;

    if (switch_value == NULL || switch_value[0] == '\0')
        error("Value required for default_checkin switch");

    switch_copy = copy_string(switch_value);
    switch_part = strtok(switch_copy,":");

    checkout_data.checkout = false;
    checkout_data.comment = "";

    if (is_prefix(switch_part,"yes",0))
    {
        checkout_data.checkout = true;

        switch_part = strtok(NULL,":");

        if (switch_part != NULL)
            checkout_data.comment = switch_part;
    }

    uf_check(UF_CLONE_set_def_co(&checkout_data),"While setting default checkout to %s",switch_value);

    UF_free(switch_copy);
}

static void default_action(const char * switch_value)
{
    UF_CLONE_action_t action = UF_CLONE_clone;
    if (switch_value == NULL || switch_value[0] == '\0')
        error("Value required for default_action switch");
    else if (is_prefix(switch_value,"clone",0))
        action = UF_CLONE_clone;
    else if (is_prefix(switch_value,"overwrite",0))
        action = UF_CLONE_overwrite;
    else if (is_prefix(switch_value,"retain",0))
        action = UF_CLONE_retain;
    else if (is_prefix(switch_value,"use_existing",0))
        action = UF_CLONE_use_existing;
    else if (is_prefix(switch_value,"exclude",0))
        action = UF_CLONE_exclude;
    else if (is_prefix(switch_value,"new_revision",0))
        action = UF_CLONE_new_revision;
    else
        error("Unexpected value %s for default_action switch",switch_value);

    uf_check(UF_CLONE_set_def_action(action),"While setting default action to %s",switch_value);

}

static void default_naming(const char *switch_value)
{
    UF_CLONE_naming_technique_t naming= UF_CLONE_autogen;
    if (switch_value == NULL || switch_value[0] == '\0')
        error("Value required for default_naming switch");
    else if (is_prefix(switch_value,"autogen",5))
        naming = UF_CLONE_autogen;
    else if (is_prefix(switch_value, "autotranslate_using_altid", 14))
        naming = UF_CLONE_altid_autotranslate;
    else if (is_prefix(switch_value,"autotranslate",5))
        naming = UF_CLONE_autotranslate;
    else if (is_prefix(switch_value,"name_rule",0))
        naming = UF_CLONE_naming_rule;
    else if (is_prefix(switch_value,"user_name",0))
        naming = UF_CLONE_user_name;
    else
        error("Unexpected value %s for default_naming switch",switch_value);

    uf_check(UF_CLONE_set_def_naming(naming),"While setting default naming to %s",switch_value);
}

static void default_type(const char * switch_value)
{
    if (switch_value == NULL || switch_value[0] == '\0')
        error("Value required for default_type switch");

    uf_check(UF_CLONE_set_def_item_type(switch_value),
             "While setting default item type to %s",
             switch_value);
}

static void associated_file_root_dir(const char * switch_value)
{
    if (switch_value == NULL || switch_value[0] == '\0')
        error("Value required for associated_file_root_dir switch");

    uf_check(UF_CLONE_set_assoc_file_root_dir(switch_value),
             "While setting associated file root directory to %s",
             switch_value);

}

static void copy_associated_files(const char * switch_value)
{
    logical flag = false;
    if (switch_value == NULL || switch_value[0] == '\0')
        error("Value required for copy_associated_files switch");

    if (is_prefix(switch_value,"yes",0))
        flag = true;
    else if (is_prefix(switch_value,"no",0))
        flag = false;

    uf_check(UF_CLONE_set_def_assoc_file_copy(flag),
             "While setting copy_associated_files to %s",
             switch_value);
}

static void copy_nonmaster(const char *switch_value)
{
    char *switch_copy = NULL;
    char *switch_part = NULL;
    UF_CLONE_copy_nm_opt_p_t options = NULL;

    if (switch_value == NULL || switch_value[0] == '\0')
        error("Value required for copy_nonmaster switch");

    switch_copy = copy_string(switch_value);

    switch_part = strtok(switch_copy,":");

    while (switch_part != NULL)
    {
        int ier = 0;
        UF_CLONE_copy_nm_opt_p_t new_option =
            (UF_CLONE_copy_nm_opt_p_t)UF_allocate_memory(sizeof(UF_CLONE_copy_nm_opt_t),&ier);
        if (ier != 0)
            error("Failed to allocate memory while setting copy nonmaster options");

        new_option->next = options;
        new_option->nonmaster_type = switch_part;
        switch_part = strtok(NULL,":");
        if (switch_part == NULL || switch_part[0] == '\0')
            error("value for copy_nonmaster_switch must be of the form <nonmaster_type>:yes|no");
        if (is_prefix(switch_part,"yes",0))
            new_option->copy = true;
        else if (is_prefix(switch_part,"no",0))
            new_option->copy = false;
        else
            error("value for copy_nonmaster_switch must be of the form <nonmaster_type>:yes|no");
        options = new_option;

        switch_part = strtok(NULL,":");

    }

    uf_check(UF_CLONE_set_def_nm_copy(options),"while setting copy_nonmaster_options to %s",switch_value);

    UF_free(switch_copy);

    while (options != NULL)
    {
        UF_CLONE_copy_nm_opt_p_t this_option = options;
        options = options->next;
        UF_free(this_option);
    }
}

static  void default_owner(const char * switch_value)
{
    char * switch_copy = NULL;
    char * owner = NULL;
    char * group = NULL;

    if (switch_value == NULL || switch_value[0] == '\0')
        error("Value required for default_owner switch");

    switch_copy = copy_string(switch_value);

    owner = strtok(switch_copy,":");

    /* <x_rama> 23-Jun-2003 Fix PR#2026322. Get the next token for the group */
    group = strtok(NULL,":");

    if (owner == NULL || owner[0] == '\0' || group == NULL || group[0] == '\0')
        error("value for default_owner switch must be of the form <owner>:<group>");

    uf_check(UF_CLONE_set_def_owner(owner),"While setting default user to %s",owner);
    uf_check(UF_CLONE_set_def_group(group),"While setting default group to %s",group);

    UF_free(switch_copy);
}

static void assign_default_project(const char * switch_value)
{
    logical flag = false;
    if (switch_value == NULL || switch_value[0] == '\0')
        error("Value required for default_project switch");

    if (is_prefix(switch_value, "yes", 0))
        flag = true;
    else if (is_prefix(switch_value, "no", 0))
        flag = false;
    else
        error("Invalid value \"%s\" for default_project switch", switch_value);

    uf_check(UF_CLONE_set_assign_default_project(flag), "While setting default_project to %s", switch_value);
}

static void retain_ownership(const char * switch_value)
{
    logical flag = false;
    if (switch_value == NULL || switch_value[0] == '\0')
        error("Value required for retain_ownership switch");

    if (is_prefix(switch_value, "yes", 0))
        flag = true;
    else if (is_prefix(switch_value, "no", 0))
        flag = false;
    else
        error("Invalid value \"%s\" for retain_ownership switch", switch_value);

    uf_check(UF_CLONE_set_retain_original_ownership(flag), "While setting retain_ownership to %s", switch_value);
}


static void name_rule(const char *switch_value)
{
    char * switch_copy = NULL;
    char * type_string = NULL;
    UF_CLONE_name_rule_def_t rule_def = {UF_CLONE_prepend_string,NULL,NULL};

    if (switch_value == NULL || switch_value[0] == '\0')
        error("Value required for name_rule switch");

    switch_copy = copy_string(switch_value);
    type_string = strtok(switch_copy,":");

    // <deshpanm> 28-Sep-2010 PR#1717136 After splitting the switch_value, we have the possibility of encountering ":",
    // again, only in case of 'replace', for other cases prepend/append/rename, it must be the part of expression
    // e.g -n=rename:${NR}_${REV:-}
    if (is_prefix(type_string,"prepend",0))
    {
        rule_def.type = UF_CLONE_prepend_string;
        rule_def.base_string = NULL;
        if(switch_value != NULL) // To make QAZ happy
            rule_def.new_string  = copy_string(strchr(switch_value, ':') + 1);
    }
    else if (is_prefix(type_string,"append",0))
    {
        rule_def.type = UF_CLONE_append_string;
        rule_def.base_string = NULL;
        if(switch_value != NULL) // To make QAZ happy
            rule_def.new_string  = copy_string(strchr(switch_value, ':') + 1);
    }
    else if (is_prefix(type_string,"replace",3))
    {
        rule_def.type = UF_CLONE_replace_string;
        rule_def.base_string = strtok(NULL,":");
        rule_def.new_string = strtok(NULL,":");
    }
    else if (is_prefix(type_string,"rename",3))
    {
        rule_def.type = UF_CLONE_rename;
        rule_def.base_string = NULL;
        if(switch_value != NULL) // To make QAZ happy
            rule_def.new_string  = copy_string(strchr(switch_value, ':') + 1);
    }
    else
        error("invalid name rule type %s while processing name_rule switch");

    if (rule_def.new_string == NULL ||
        (rule_def.type == UF_CLONE_replace_string && rule_def.base_string == NULL))
        error("invalid name rule definition %s",switch_value);

    {
        UF_CLONE_naming_failures_t failures;
        int rc = 0;
        UF_CLONE_init_naming_failures(&failures);

        rc = UF_CLONE_set_name_rule(&rule_def,&failures);


        /*
          naming failures are not necessarily fatal here, as they could be
          sorted out by loading a log file.
        */
        if (rc == UF_CLONE_err_naming_failures)
            report_naming_failures(&failures);
        else
            uf_check(rc,"While setting name rule to %s",switch_value);
    }
    UF_free(switch_copy);
}

static void default_folder(const char * switch_value)
{

    /* <x_sardea> 30-jun-2004  : PR#1334242 */

    UF_CLONE_operation_class_t operation_class;
    uf_check(UF_CLONE_ask_operation_class(&operation_class),"While asking operation class");

    if(operation_class == UF_CLONE_export_operation)
    {
      error("While exporting invalid folder option is specified,use -folder option to export the folder contents\n");
      return;
    }

    if (switch_value == NULL || switch_value[0] == '\0')
        error("Value required for default_folder switch");

    uf_check(UF_CLONE_set_def_folder(switch_value),
             "While setting default folder to %s",
             switch_value);
}

static void default_directory(const char * switch_value)
{
    if (switch_value == NULL || switch_value[0] == '\0')
        error("Value required for default_directory switch");

    // <deshpanm> 03-Jun-2010 PR#6353652 if directory does not exist, so attempt to create it...
    uf_check(UF_CLONE_ensure_def_directory(switch_value),
             "While setting default directory to %s",
             switch_value);
}

static void load_log_file(const char * switch_value)
{
    UF_CLONE_naming_failures_t naming_failures;
    UF_CLONE_log_file_failure_t logfile_failure;
    UF_PART_load_status_t load_status;
    int rc = 0;

    if (switch_value == NULL || switch_value[0] == '\0')
        error("Value required for load_log_file switch");

    UF_CLONE_init_naming_failures(&naming_failures);
    UF_CLONE_init_log_file_failure(&logfile_failure);

    rc = UF_CLONE_load_logfile(switch_value,&naming_failures,&logfile_failure,&load_status);
    switch(rc)
    {
    case UF_CLONE_err_naming_failures:
    case UF_CLONE_err_bvr_out_of_sync:
    case UF_CLONE_err_comp_not_found:
        /*
          if any of these is returned then we might have both load failures and
          naming failures
        */
        if (load_status.failed)
            rc = report_load_status(&load_status);
        if (naming_failures.n_failures != 0)
            report_naming_failures(&naming_failures);
        break;
    case UF_CLONE_err_invalid_logfile:
        report_log_file_failure(&logfile_failure,switch_value);
        break;
    default:
        break;
    }
    uf_check(rc,"While loading logfile %s",switch_value);
}

static void save_log_file(const char * switch_value)
{
    if (switch_value == NULL || switch_value[0] == '\0')
        error("Value required for save_log_file switch");

    uf_check(UF_CLONE_set_logfile(switch_value),"While setting save_log_file to %s",switch_value);
}

/*
   sets the operation to do a dryrun only

*/
static void dryrun(const char *ignored)
{
    UF_CLONE_validation_opts_p_t validation_options= NULL;
    uf_check(UF_CLONE_set_dryrun(true),"While setting dryrun to true");

    UF_CLONE_ask_def_validation_options(&validation_options);
    if( validation_options!= NULL)
    {
        if ( validation_options->mode == UF_CLONE_import_from_part)
        {
            const char*  warning =  "Even though dry-run mode has been selected, the utility will still read validation results from each part "
                                                "and compare against validation rule. This could take some time if the target "
                                                "assembly or parts are large or there is a large number of them.";

            message("\nNote: %s\n", warning);
        }
        else if ( validation_options->mode == UF_CLONE_run_validation)
        {
             const char*  warning =  "Even though dry-run mode has been selected, the utility will still open each part, "
                                                "run validation against it and compare with validation rule. "
                                                "This could take some time if the target assembly or parts are large or there is a large number of them.";
             message("\nPerformance Warning: %s\n", warning);
        }
        else if ( validation_options->mode == UF_CLONE_run_validation_hybrid)
        {
             const char*  warning =  "Even though dry-run mode has been selected, the utility will still read validation results "
                                                    "from each part and compare against validation rule, if there is no result in a part, "
                                                    "the utlity will open the part, run validation against it and compare with validation rule. "
                                                    "This could take some time if the target assembly or parts are large or there is a large number of them.";
             message("\nPerformance Warning: %s\n", warning);
        }
    }
}

/*
    Determines how an import/export operation will treat part family
    members.
*/

static void family_treatment(const char* switch_value)
{
    UF_CLONE_family_treatment_t treatment = UF_CLONE_treat_as_lost;

    if (switch_value == NULL || switch_value[0] == '\0')
        error("Value required for family_treatment switch");

    if (is_prefix(switch_value,"lose",0))
        treatment = UF_CLONE_treat_as_lost;
    else if (is_prefix(switch_value,"strip_status",0))
        treatment = UF_CLONE_strip_family_status;
    else if (is_prefix(switch_value,"error",0))
        treatment = UF_CLONE_give_error;
    else
        error("invalid family treatment type %s while processing family_treatment switch", switch_value);

    uf_check (UF_CLONE_set_family_treatment(treatment),
              "While setting part family treatment to %s",
              switch_value);

}

static UF_UGMGR_tag_t find_folder(const char * folder_path)
{
    int error_code = 0;
    char * folder_path_copy = (char *)UF_allocate_memory(sizeof(char) * (strlen(folder_path) +1), &error_code);
    char * folder_name = NULL;
    UF_UGMGR_tag_t folder_tag = UF_UGMGR_null_tag;

    uf_check(error_code,"Allocating memory");
    strcpy(folder_path_copy,folder_path);
    folder_name = strtok(folder_path_copy,":");
    /* first component of the folder_path must be a user name, so get that
       user's root folder */
    /* <junankar> 12-Jul-2010
       PR#6142176: Display invalid folder error message if home folder for user is not found,
       instead of "Internal Hookup error - object does not exist.error".
    */
    error_code = UF_UGMGR_ask_user_folder(folder_name, &folder_tag);
    if(folder_tag == UF_UGMGR_null_tag)
        uf_check(UF_CLONE_err_invalid_folder, "Getting home folder for user %s", folder_name);
    else
        uf_check(error_code, "Getting home folder for user %s", folder_name);

    /* <x_sardea> 30-jun-2004 : PR#1334242 */
    while ((folder_name = strtok(NULL,":")) != NULL)
    {
        int count = 0;
        UF_UGMGR_tag_t * folder_contents = NULL;
        int i;

        uf_check(UF_UGMGR_list_folder_contents(folder_tag,&count,&folder_contents),"Listing contents of folder");
        for (i = 0; i < count; i++)
        {
            UF_UGMGR_object_type_t object_type;
            uf_check(UF_UGMGR_ask_object_type(folder_contents[i],&object_type),"Getting type of object");
            if (object_type == UF_UGMGR_type_folder)
            {
                char this_folder_name[UF_UGMGR_NAME_BUFSIZE];
                uf_check(UF_UGMGR_ask_folder_name(folder_contents[i],this_folder_name),"Asking name of folder");
                if (strcmp(this_folder_name,folder_name) == 0)
                {
                    folder_tag = folder_contents[i];
                    break;
                }
            }
        }
        UF_free(folder_contents);
        if (i == count)
            uf_check(UF_CLONE_err_invalid_folder,"Finding folder %s",folder_path);
    }
    UF_free((void *)folder_path_copy);

    return folder_tag;
}
/* implements the addition of all parts in a specified folder to the
   current operation
*/

static void folder(const char * switch_value)
{
    UF_UGMGR_tag_t folder_tag = find_folder(switch_value);
    int count = 0;
    UF_UGMGR_tag_t * folder_contents = NULL;
    int i;

    /* <x_sardea> 30-jun-2004 :PR#1334242 */

    UF_CLONE_operation_class_t operation_class;

    /* Get the clone operation and depending on import or export get the folder contents */
    uf_check(UF_CLONE_ask_operation_class(&operation_class),"While asking operation class");

    if(operation_class == UF_CLONE_import_operation)
    {
       error("While importing invalid folder option is specified,-default_f is the required option\n");
       return;
    }
    uf_check(UF_UGMGR_list_folder_contents(folder_tag,&count,&folder_contents),"Listing contents of %s",switch_value);
    for (i = 0; i < count; i++)
    {
        UF_UGMGR_object_type_t object_type;
        uf_check(UF_UGMGR_ask_object_type(folder_contents[i],&object_type),"Asking object type");
        if (object_type == UF_UGMGR_type_part)
        {
            char this_part_number[UF_UGMGR_NAME_BUFSIZE];
            char this_part_revid[UF_UGMGR_NAME_BUFSIZE];
            char this_part_specification[ MAX_FSPEC_BUFSIZE ];

            UF_UGMGR_tag_t part_rev_tag = UF_UGMGR_null_tag;

            uf_check(UF_UGMGR_ask_configured_rev(folder_contents[i],&part_rev_tag),"Configuring partrev");
            /* <x_sardea> 30-jun-2004 :PR#1334242 */
            uf_check(UF_UGMGR_ask_part_number(folder_contents[i],this_part_number),"Getting part number");
            uf_check(UF_UGMGR_ask_part_revision_id(part_rev_tag,this_part_revid),"Getting part revision");
            uf_check(UF_UGMGR_encode_part_filename(this_part_number,this_part_revid,NULL,NULL,this_part_specification),"Encoding part specification: part_number %s, revision_id %s",this_part_number,this_part_revid);
            assembly(this_part_specification);
        }
    }
    UF_free(folder_contents);
}

/* implements the addition of all parts in the specified directory to
   the operation
*/
static void directory(const char *switch_value)
{
    int options = (1 <<11) | (1 << 13); /* wildcard given (bit 11) and filenames only wanted (bit 13) */
    int ignored = 0;
    int error_code = 0;

    /* <larson - 13-Dec-2006 - PR#5666609>
        The following uc4508 is designed to have a return value of a non-negative number
        that corresponds to an assigned channel number.  Prior to nx5 ip22, that channel
        appears to have always been equal to 0.  With ip22, that value can be greater
        than 0 as well. Therefore, an error should be generated only when the return value
        is negative.
    */
    error_code = uc4508((char *)switch_value,options,ignored,"*.prt");
    if ( error_code < 0 )
    {
        uf_check (error_code, "Opening directory %s", switch_value);
    }

    while((error_code = uc4518()) == 0)
    {
        char file_name[ MAX_FSPEC_BUFSIZE ];
        uf_check(uc4519(file_name),"Asking next file name");
        assembly(file_name);
    }
    if (error_code < 0)
        uf_check(error_code,"While reading directory %s",switch_value);

    /* This time, look for fem files */
    error_code = uc4508((char *)switch_value,options,ignored,"*.fem");
    if ( error_code < 0 )
    {
        uf_check (error_code, "Opening directory %s", switch_value);
    }

    while((error_code = uc4518()) == 0)
    {
        char file_name[ MAX_FSPEC_BUFSIZE ];
        uf_check(uc4519(file_name),"Asking next file name");
        assembly(file_name);
    }
    if (error_code < 0)
        uf_check(error_code,"While reading directory %s",switch_value);

    /* This time, look for sim files */
    error_code = uc4508((char *)switch_value,options,ignored,"*.sim");
    if ( error_code < 0 )
    {
        uf_check (error_code, "Opening directory %s", switch_value);
    }

    while((error_code = uc4518()) == 0)
    {
        char file_name[ MAX_FSPEC_BUFSIZE ];
        uf_check(uc4519(file_name),"Asking next file name");
        assembly(file_name);
    }
    if (error_code < 0)
        uf_check(error_code,"While reading directory %s",switch_value);

}

/* implements setting the current revision rule to the specified value
*/
static void revision_rule(const char * switch_value)
{
    // <deshpanm> 02-Jun-2010 PR#6353652 process the as saved load option from revision rule switch
    if(switch_value != NULL && str_compare_i(switch_value, "AS SAVED") == 0)
    {
        UF_ASSEM_options_t assy_options;
        UF_ASSEM_ask_assem_options(&assy_options);
        assy_options.load_options = UF_ASSEM_load_as_saved;

        // <odoyy6> 26-Jul-2018 PR#9216453
        // From NX8.5 we have separated managed mode load option, refer PR#5687522, so also set managed_mode_load_options
        assy_options.managed_mode_load_options = UF_ASSEM_managed_load_as_saved;

        UF_ASSEM_set_assem_options(&assy_options);
    }
    else
    {
        uf_check(UF_UGMGR_set_config_rule((char *)switch_value),"While setting revision rule %s",switch_value);
    }
}

static void propagate_actions(const char * switch_value)
{
    logical flag = false;
    if (switch_value == NULL || switch_value[0] == '\0')
        error("Value required for propagate_actions switch");

    if (is_prefix(switch_value,"yes",0))
        flag = true;
    else if (is_prefix(switch_value,"no",0))
        flag = false;
    else
        error("Invalid value \"%s\" for propagate_actions switch",switch_value);

    uf_check(UF_CLONE_set_propagate_actions(flag),
             "While setting propagate_actions to %s",
             switch_value);
}

static void autotranslate_mode(const char * switch_value)
{
    UF_UGMGR_clone_auto_trans_f_t fn = NULL;

    if (switch_value == NULL || switch_value[0] == '\0')
        error("Value required for autotranslate_mode switch");

    if (is_prefix(switch_value,"default",0))
        fn = NULL;
    else if (is_prefix(switch_value,"legacy",0))
    {
        UF_CLONE_operation_class_t operation_class;
        uf_check(UF_CLONE_ask_operation_class(&operation_class),"While asking operation class");
        if (operation_class == UF_CLONE_import_operation)
            fn = ug_legacy_trans;
        else
            error("legacy autotranslate_mode is only compatible with an import operation");
    }
    else
        error("Invalid value \"%s\" for autotranslate_mode switch",switch_value);

    uf_check(UF_UGMGR_set_clone_auto_trans(fn),
             "While setting autotranslate_mode to %s", switch_value);
}

static void validation_mode(const char * switch_value)
{
    UF_CLONE_operation_class_t operation_class;
    logical is_active = false;
    UF_CLONE_validation_mode_t mode = UF_CLONE_no_validation;
    UF_CLONE_validation_opts_p_t validation_options= NULL;

    uf_check(UF_CLONE_ask_operation_class(&operation_class),"While asking operation class");

    if((operation_class != UF_CLONE_import_operation) )
    {
      error("validation_mode option is only valid for import operation\n");
      return;
    }

    uf_check(UF_is_ugmanager_active(&is_active),"While asking ugmanager active");
    if (!is_active)
    {
      error("validation_mode option is only valid when NX is connected to Teamcenter\n");
      return;
    }

    if (switch_value == NULL || switch_value[0] == '\0')
        error("Value required for validation_mode switch");


    if (is_prefix(switch_value,"off",0))
        mode = UF_CLONE_no_validation;
    else if (is_prefix(switch_value,"import_from_part",0))
        mode = UF_CLONE_import_from_part;
    else if (is_prefix(switch_value,"run_validation",0))
    {
        /*print out performance warning message*/
        const char*  performance_warning =
            "Set validation_mode to run_validation will open each part and run validation against it. "
            "This could take some time if the target assembly or parts are large or in large amount.";
        message("\nPerformance Warning: %s\n",performance_warning);

        mode = UF_CLONE_run_validation;
    }
    else if (is_prefix(switch_value,"run_validation_hybrid",0))
    {
        const char*  performance_warning =
            "Set validation_mode to run_validation_hybrid will open the part without results and run validation against it. "
             "This could take some time if the target assembly or parts are large or in large amount.";
        message("\nPerformance Warning: %s\n",performance_warning);

        mode = UF_CLONE_run_validation_hybrid;
    }
    else
        error("Invalid value \"%s\" for validation_mode switch",switch_value);

    UF_CLONE_ask_def_validation_options(&validation_options);
    if( validation_options!= NULL)
    {
        validation_options->mode = mode;
        uf_check(UF_CLONE_set_def_validation_options(validation_options),
                 "While setting validation_mode to %s",
                 switch_value);
        UF_CLONE_free_validation_options(validation_options);
    }
}

static void validation_rule(const char * switch_value)
{
    UF_CLONE_operation_class_t operation_class;
    logical is_active = false;
    uf_check(UF_CLONE_ask_operation_class(&operation_class),"While asking operation class");

    if((operation_class != UF_CLONE_import_operation))
    {
      error("validation_rule option is only valid for import operation\n");
      return;
    }

    uf_check(UF_is_ugmanager_active(&is_active),"While asking ugmanager active");
    if (!is_active)
    {
      error("validation_mode option is only valid when NX is connected to Teamcenter\n");
      return;
    }

    if (switch_value == NULL || switch_value[0] == '\0')
        error("Value required for validation_rule switch");
    else
    {
            UF_CLONE_validation_opts_p_t validation_options= NULL;
            UF_CLONE_ask_def_validation_options(&validation_options);
            if( validation_options!= NULL)
            {
                int err = 0;
                validation_options->validation_rule = (char*)UF_allocate_memory( (strlen(switch_value)+1)*sizeof(char), &err);
                uf_check(err,"While allocating memeory");
                strcpy( validation_options->validation_rule , switch_value);
                uf_check(UF_CLONE_set_def_validation_options(validation_options),
                         "While setting validation_rule to %s",
                         switch_value);
                UF_CLONE_free_validation_options(validation_options);
            }
    }
}

static void abort_import_on_fail(const char * switch_value)
{
    logical option = false;
    logical is_active = false;
    UF_CLONE_operation_class_t operation_class;
    uf_check(UF_CLONE_ask_operation_class(&operation_class),"While asking operation class");

    if((operation_class != UF_CLONE_import_operation))
    {
      error("abort_import_on_fail option is only valid for import operation\n");
      return;
    }

    uf_check(UF_is_ugmanager_active(&is_active),"While asking ugmanager active");
    if (!is_active)
    {
      error("validation_mode option is only valid when NX is connected to Teamcenter\n");
      return;
    }

    if (switch_value == NULL || switch_value[0] == '\0')
        error("Value required for treat_validation_warning switch");

    if (is_prefix(switch_value,"yes",0))
        option = true;
    else if (is_prefix(switch_value,"no",0))
        option = false;
    else
        error("Invalid value \"%s\" for abort_import_on_fail switch",switch_value);

    uf_check(UF_CLONE_set_validation_abort_option(option),
             "While setting abort_import_on_fail to %s",
             switch_value);

}

static void treat_validation_warning(const char * switch_value)
{
    logical flag = false;
    logical is_active = false;
    UF_CLONE_validation_opts_p_t validation_options= NULL;
    UF_CLONE_operation_class_t operation_class;
    uf_check(UF_CLONE_ask_operation_class(&operation_class),"While asking operation class");

    if((operation_class != UF_CLONE_import_operation))
    {
      error("treat_validation_warning_as_pass option is only valid for import operation\n");
      return;
    }

    uf_check(UF_is_ugmanager_active(&is_active),"While asking ugmanager active");
    if (!is_active)
    {
      error("validation_mode option is only valid when NX is connected to Teamcenter\n");
      return;
    }

    if (switch_value == NULL || switch_value[0] == '\0')
        error("Value required for treat_validation_warning_as_pass switch");

    if (is_prefix(switch_value,"yes",0))
        flag = true;
    else if (is_prefix(switch_value,"no",0))
        flag = false;
    else
        error("Invalid value \"%s\" for treat_validation_warning_as_pass switch",switch_value);

    UF_CLONE_ask_def_validation_options(&validation_options);
    if( validation_options!= NULL)
    {
        validation_options->treat_warning_as_pass = flag;
        uf_check(UF_CLONE_set_def_validation_options(validation_options),
                 "While setting treat_validation_warning_as_pass to %s",
                 switch_value);
        UF_CLONE_free_validation_options(validation_options);
    }
}

static void treat_validation_outdated(const char * switch_value)
{
    logical flag = false;
    logical is_active = false;
    UF_CLONE_validation_opts_p_t validation_options= NULL;
    UF_CLONE_operation_class_t operation_class;
    uf_check(UF_CLONE_ask_operation_class(&operation_class),"While asking operation class");

    if((operation_class != UF_CLONE_import_operation))
    {
      error("treat_validation_outdated_as_pass option is only valid for import operation\n");
      return;
    }

    uf_check(UF_is_ugmanager_active(&is_active),"While asking ugmanager active");
    if (!is_active)
    {
      error("validation_mode option is only valid when NX is connected to Teamcenter\n");
      return;
    }

    if (switch_value == NULL || switch_value[0] == '\0')
        error("Value required for treat_validation_warning_as_pass switch");

    if (is_prefix(switch_value,"yes",0))
        flag = true;
    else if (is_prefix(switch_value,"no",0))
        flag = false;
    else
        error("Invalid value \"%s\" for treat_validation_outdated_as_pass switch",switch_value);

    UF_CLONE_ask_def_validation_options(&validation_options);
    if( validation_options!= NULL)
    {
        validation_options->treat_outdated_as_pass = flag;
        uf_check(UF_CLONE_set_def_validation_options(validation_options),
                 "While setting treat_validation_outdated_as_pass to %s",
                 switch_value);
        UF_CLONE_free_validation_options(validation_options);
    }
}

static void id_display_rule(const char * switch_value)
{
    if (switch_value == NULL || switch_value[0] == '\0')
        error("Value required for identifier_display_rule switch");

    uf_check(UF_CLONE_set_identifier_display_rule(switch_value), "While setting identifier_display_rule to %s", switch_value);
}

/* This function registers a callback function to keep track of
   which parts are being operated on during clone performance, for error
   reporting purposes
*/
static void register_callbacks(void)
{
    UF_CLONE_register_ntfy_callback(UF_CLONE_beg_part_clone_cb,callback_fn,"UFD clone","Track parts",NULL,false);
    UF_CLONE_register_ntfy_callback(UF_CLONE_end_part_clone_cb,callback_fn,"UFD clone","Track parts",NULL,false);
}

/* this function is the callback function used to keep track of which
   parts are being operated on during lcone performance.

*/
static UF_CLONE_notify_response_t callback_fn
(
    UF_CLONE_notify_cb_t  callback_point,
    const char           *input_part,
    const void           *data
)
{
    switch (callback_point)
    {
    case UF_CLONE_beg_part_clone_cb:
        part_being_operated_on = copy_string(input_part);
        break;
    case UF_CLONE_end_part_clone_cb:
        UF_free(part_being_operated_on);
        part_being_operated_on = NULL;
        break;
    default:
        error("callback function called at an unexpected callback point %d",callback_point);
        break;
    }
    return UF_CLONE_continue;
}

static int ug_legacy_trans(const char input[ MAX_FSPEC_BUFSIZE ], char output[ MAX_FSPEC_BUFSIZE ])
{
    char *itemid = NULL;
    char *mfkid = NULL;
    char *revid = NULL;
    char *file_type = NULL;
    char *file_name = NULL;
    char internal_form[ MAX_FSPEC_BUFSIZE ] = "";
    int n_attributes;
    UF_ATTR_part_attr_p_t attributes = NULL;
    int ifail = 0;

    /*
      Because we want to carry on in the event of a naming failure, we don't
      use uf_check here, we just keep track of the ifail value. copy_string
      may still stop the process, but only if we have run out of memory,
      which is fatal anyway.
    */
    ifail = UF_CLONE_ask_part_attrs(input,&n_attributes,&attributes);
    if (ifail == 0)
    {
        int i = 0;
        /*
          First, we look through the attribute values to see if this part has
          been in iman before, and if so what the components of the part name
          should be.
        */
        for (i = 0; i < n_attributes; i++)
        {
            if (strcmp(attributes[i].title,"DB_PART_MFKID") == 0)
                mfkid =  copy_string(attributes[i].value.value.string);
            else if (strcmp(attributes[i].title,"DB_PART_NO") == 0)
                itemid =  copy_string(attributes[i].value.value.string);
            else if (strcmp(attributes[i].title,"DB_PART_REV") == 0)
                revid =  copy_string(attributes[i].value.value.string);
            else if (strcmp(attributes[i].title,"DB_MODEL_TYPE") == 0)
                file_type =  copy_string(attributes[i].value.value.string);
            else if (strcmp(attributes[i].title,"DB_MODEL_NAME") == 0)
                file_name =  copy_string(attributes[i].value.value.string);
            if (ifail != 0)
                break;
        }
        // <gezou> 12-Jul-2013
        // If we can not find the DB_PART_MFKID attribute value, then use DB_PART_NO attribute value
        // <deshpama> 13-Nov-2013
        // Added NULL check for item id
        if (mfkid == NULL && itemid != NULL)
        {
            mfkid = copy_string(itemid);
        }
    }
    UF_free(attributes);

    // <Manoj Patwal>, 25-Jul-2017, PR#8931847
    // Check for mfkid sting length as well
    if (ifail == 0 && (mfkid == NULL || mfkid[0] == '\0'))
    {
        char simple_name[ MAX_FSPEC_BUFSIZE ];
        ifail = uc4574((char *)input,2,simple_name);
        if (ifail == 0)
        {
            /* if exists, remove a fem or sim extension */
            uc4578(simple_name, 190, simple_name);
            uc4578(simple_name, 199, simple_name);
            mfkid = copy_string(simple_name);
        }
    }

    /* <APB> 11-Feb-2002
      Now we've got an mfkid. We may already have a RevID, but for
      legacy compatibility the configured revision if there is one is supposed to override the
      attribute value, so we go looking for that, obviously if the part is
      new to this database, there won't be one.
    */
    if (ifail == 0)
    {
        UF_UGMGR_tag_t part_tag;
        ifail = UF_UGMGR_ask_part_tag(mfkid,&part_tag);
        if (ifail == 0 && part_tag != null_tag)
        {
            UF_UGMGR_tag_t rev_tag;
            ifail = UF_UGMGR_ask_configured_rev(part_tag, &rev_tag);
            if (ifail != 0 && rev_tag != null_tag)
            {
                char rev[UF_UGMGR_NAME_BUFSIZE];
                ifail = UF_UGMGR_ask_part_revision_id(rev_tag,rev);
                if (ifail == 0)
                {
                    UF_free(revid);
                    revid = copy_string(rev);
                }
            }
        }
    }
    /*
      if we haven't got a rev any other way, default to A
    */
    // <Manoj Patwal>, 25-Jul-2017, PR#8931847
    // Check for revid sting length as well
    if (ifail == 0 && (revid == NULL || revid[0] == '\0'))
        revid = copy_string("A");

    if (ifail == 0)
        ifail = UF_UGMGR_encode_part_filename(mfkid,revid,file_type,file_name,internal_form);

    UF_free(itemid);
    UF_free(mfkid);
    UF_free(revid);
    UF_free(file_type);
    UF_free(file_name);

    /*
      finally we need to convert the part name we have in internal form to
      CLI form.
    */
    if (ifail == 0)
        ifail = UF_UGMGR_convert_name_to_cli(internal_form,output);

    return ifail;
}

/*
  This is the main function, it assumes UF_initialise has been called but nothing else.
*/
extern void UFD_clone_main(int argc, char **argv)
{
    int i;
    int ignored = 0;

    /*  <deshpama> 31-May-2011 Fix PR6541928
        If there is '-help or '-h' argument present in argument list, It won't ask for any login.
        It will show the help description.
    */
    for( i = 1; i < argc; i++ )
    {
        switch_descriptor_p_t help_descriptor = match_switch(argv[i]);
        if( help_descriptor != NULL && strcmp(help_descriptor->switch_name, "help") == 0 )
        {
            help_descriptor->handler(find_value(argv[i]));
        }
    }
    /*
      We call uc4624 to "remember" the argument list, despite the fact we do
      our own argument processing, because this is the call which notices
      the UG/Manager -pim, -user, -group and -password switches and
      initialises UG/Manager if they are present.
    */

    /* <novak> 05-Dec-08 If this is managed mode and encrypt paramater is set check
                      for encrypted password and process.
    */
    if (parameter_set(argc, argv, "pim", "yes") && parameter_set(argc, argv, "encrypt", "true"))
    {
        if (UF_CLONE_load_crypt() == 0)
        {
            /* Encryption library and functions are loaded, try to get decrypted password. */
            char decoded_passwd[MAX_CRYPTO_SIZE];
            handle_encryption( argc, argv, decoded_passwd );
        }
    }

    uc4624(ignored,argc,argv);

    // <deshpanm> 25-Jul-2020
    // Avoid aborting the program in case of assertions, continue gracefully after adding note in syslog
    ERROR_assertion_handler_t old_assertion_handler = ERROR_set_assertion_handler(ug_clone_assertion_handler);

    // <wrkab7> 02-Nov-2020
    // TCIN195312: Use PDI cache for performance improvement
    // Error finally block is needed to make sure we end the operation if an exception is raised.
    ERROR_FINALLY_PROTECT
    {
        // use PDI cache only if the operation is export/clone.
        bool usePdiCaching = false;
        if (parameter_set(argc, argv, "pim", "yes") && 
           (parameter_set(argc, argv, "operation", "export") || parameter_set(argc, argv, "operation", "clone")))
        {
            usePdiCaching = true;
        }

        UGS::PDM::PDIClientCloneOpCacher pdiClientCacher(usePdiCaching);

        register_callbacks();
        process_switches(argc,argv);

        if ((is_dfa))
        {
            if (dfa_import)
            {
                uf_check(UF_KF_UGMGR_initialize_import(is_dfa_list), "while performing DFA import.");

                return;
            }
            else if (dfa_export)
            {
                uf_check(UF_KF_UGMGR_initialize_export(dfa_export_option),
                         "while performing export dfa");

                return;
            }
        }
        else
        {
            /*
              perform_clone will do an apply_defaults for us.
            */
            int rc = 0;
            UF_CLONE_naming_failures_t naming_failures;
            UF_CLONE_operation_class_t operation_class;
            char* logfilename = NULL;

            uf_check(UF_CLONE_ask_operation_class(&operation_class),"While asking operation class");
            uf_check(UF_CLONE_ask_logfile(&logfilename),"While asking log file name");

            fprintf(stdout,"Logging %s to %s\n",operation_names[(int)operation_class],logfilename);
            UF_free(logfilename);

            UF_CLONE_init_naming_failures(&naming_failures);
            rc = UF_CLONE_perform_clone(&naming_failures);
            if (rc == UF_CLONE_err_naming_failures)
                report_naming_failures(&naming_failures);

            /*
                if we've still got naming failures, then we should report an error and
                stop anyway, as we should if we've got any other error.
            */
            uf_check(rc,"While performing %s",operation_names[(int)operation_class]);
            /*
                if we get here, we completed OK.
            */
            message("%s completed successfully",operation_names[(int)operation_class]);

            if (is_dfa_in_part)
                uf_check(UF_UGMGR_KF_export_dfa_in_part(NULL),
                    "While exporting DFA Classes referenced in part");

            uf_check(UF_CLONE_terminate(),"While terminating clone");
        }
    }
    ERROR_FINALLY
    {
    }
    ERROR_FINALLY_END

    //reset back the old assertion handler 
    ERROR_set_assertion_handler(old_assertion_handler);

}

/*
  shut down the program cleanly, then exit with the given exit code.
*/
static void quit(int exit_code)
{
    UF_CLONE_terminate();
    UF_terminate();
    exit(exit_code);
}

/*
  report an error and exit the program
*/
static void error(char *format,...)
{
    va_list args;
    va_start(args,format);
    log_and_stderr_printf ( "\nERROR: " );
    vlog_and_stderr_printf( format, args );
    log_and_stderr_printf ("\n");
    va_end(args);
    quit(EXIT_FAILURE);
}

/*
  print out a message
*/
static void message(char *format,...)
{
    va_list args;
    va_start(args,format);
    vfprintf(stdout,format,args);
    fprintf(stdout,"\n");
    va_end(args);
}

/*
  print out a messages like warning and do not exit
*/
static void log_and_stderr_printf (char *format,...)
{
    va_list args;
    va_start(args,format);
    vlog_and_stderr_printf(format,args);
    va_end(args);
}

/*
  Checks the return code and if it indicates an error, prints out the
  error message and quits
*/

static void uf_check(int return_code, char *error_format,...)
{
    if (return_code != 0)
    {
        va_list args;
        char message[ MAX_LINE_BUFSIZE ];
        int message_code = UF_get_fail_message(return_code,message);

        va_start(args,error_format);

        if (message_code != 0)
            strcpy(message,"Unknown error!");

        log_and_stderr_printf ("\nERROR: (%d) - %s\n\t", return_code,message);
        vlog_and_stderr_printf (error_format,args);
        va_end(args);
        if (part_being_operated_on != NULL)
        {
            log_and_stderr_printf ("\n\tThis error occurred while operating on the part %s",part_being_operated_on);
            log_and_stderr_printf ("\n\tYou should check the state of the output part for problems");
            log_and_stderr_printf ("\n\tbefore trying this operation again");
        }
        log_and_stderr_printf("\n");

        quit(EXIT_FAILURE);
    }
}

/* Prints the formated error to syslog and stderr */
static int  vlog_and_stderr_printf ( const char * format, va_list args )
{
    va_list args_copy;
    int  char_count    = 0;

    // <junankar> 02-Aug-2012
    // PR# 6676911: Value of args is undefined after the vfprintf call
    // So make a copy and use it before calling vsprintf again
    va_copy(args_copy, args);
    char_count = vfprintf ( stderr, format, args_copy );
    va_end(args_copy);

    if ( char_count > 0 )
    {
        int  errorCode     = 0;
        char *message      = NULL;
        message = ( char * ) UF_allocate_memory ( sizeof(char) * (char_count+1),
                                                  &errorCode );
        if ( errorCode == 0 )
        {
            va_copy(args_copy, args);
            vsprintf ( message, format, args_copy );
            va_end(args_copy);

            UF_print_syslog ( message, false );
            UF_free ( message );
        }
    }


    return ((char_count < 0) ? 0: char_count);

}

static void export_dfa_kf( const char *switch_value )
{
    if (switch_value == NULL || switch_value[0] == '\0')
        error("Value required for export_dfa_kf switch");

    if (is_prefix(switch_value,"dfa_only",6))
        is_dfa = true;
    else
        is_dfa_in_part = true;
}

static void export_dfa_list( const char *ignored )
{
    is_dfa_list = true;
}

static void import_dfa_kf(const char *switch_value)
{
    is_dfa     = true;
    dfa_import = true;
}

static void import_dfa_list( const char *ignored )
{
    is_dfa_list = true;
}

static logical is_the_value_dfa( const char *value, int option )
{
    logical       exists = FALSE;
    int           error  = 0;
    char         *internal_encoded_name = NULL;
    char          part_number[UF_UGMGR_PARTNO_BUFSIZE];
    char          part_revision[UF_UGMGR_PARTREV_BUFSIZE];
    char          part_file_type[UF_UGMGR_FTYPE_BUFSIZE];
    char          part_file_name[UF_UGMGR_FNAME_BUFSIZE];

    if ( !is_dfa ) return FALSE;

    if ( is_dfa_list ) return TRUE;

    is_dfa = FALSE;

    error = UF_UGMGR_convert_name_from_cli ( value, &internal_encoded_name );

    if ( !error )
    {
        error = UF_UGMGR_decode_part_filename ( internal_encoded_name, part_number,
                                            part_revision, part_file_type,
                                            part_file_name );
    }

    UF_KF_UGMGR_is_item_dfa_type( part_number, &exists );

    if ( exists )
    {
       is_dfa = TRUE;

       /* set option whether to perform export on part or assembly */
       if ( option == UF_KF_UGMGR_EXPORT_DFA_IN_ASSEMBLY )
           dfa_export_option = UF_KF_UGMGR_EXPORT_DFA_IN_ASSEMBLY;
       else
           dfa_export_option = UF_KF_UGMGR_EXPORT_DFA_IN_PART;
    }

    return exists;
}

static void rev_up_read_only(const char *ignored)
{
    uf_check(UF_CLONE_set_rev_up(true),"While setting rev_up to true");
}

/* NXDM MultiCad Clone (NXDM50101) project
   <DPL> 04-Apr-2007
*/
static void attach_log_file(const char *ignored)
{
    uf_check(UF_CLONE_set_attach_log_file(true),"While setting attach_log_file to true");
}

/* prasad Haldule < 27 Nov 2008>
 This method finds out whether the passed in coomand line arguments
 have any encryption and decodes the encryption
 Arguments
  argc  , i - Number of commandline arguments
  argv  , i - array which holds values of command line arguments
  output_str ,o - ptr to a char array which will return the decrypted string
 Return
  void
*/
static void handle_encryption(int argc, char **argv, char *output_str)
{
    int i, j, switch_length, cipherLength;
    const char *switchstring;
    char decoded_str[MAX_CRYPTO_SIZE];
    unsigned char aesKey[ 16 ];

    /* First check whether we have encrytion flag */
    if ( parameter_set(argc, argv, "encrypt", "true") )
    {
        for (i = 1; i < argc; i++)
        {
            switch_descriptor_p_t descriptor = match_switch(argv[i]);

            if ( descriptor != NULL )
            {
               if (strcmp( descriptor->switch_name, "password" ) == 0 )
               {
                    unsigned char cipherText[MAX_CRYPTO_SIZE] = {(unsigned char) 0};
                    char strVal[MAX_CRYPTO_SIZE];
                    strncpy(strVal, find_value(argv[i]), MAX_CRYPTO_SIZE-1);

                    /* Report an error during decode of base64 string. */
                    if (UF_CLONE_base_64_to_bytes( cipherText, &cipherLength, strVal, 0, strlen(strVal) ) != 0)
                    {
                        log_and_stderr_printf("Error decoding base64 string \n");
                        break;
                    }

                    if (UF_CLONE_get_key( aesKey ) != 0)
                    {
                        log_and_stderr_printf("Error getting key string \n");
                        break;
                    }

                    /* get the encrypted value of the passwd ( after the "=" sign)
                       and pass it to the decode method
                    */
                    if (UF_CLONE_decode(aesKey,(char *)cipherText, cipherLength, decoded_str) != 0)
                    {
                        log_and_stderr_printf("Error decoding string \n");
                        break;
                    }

                    switchstring = argv[i];
                    switch_length = strcspn(argv[i],switch_terminators);

                    for ( j = 0; j < (switch_length+1); ++j )
                    {
                        output_str[j] = switchstring[j];
                    }
                    strcpy ( &output_str[switch_length+1], decoded_str);
                    argv[i] = output_str;

                    break;
                }
            }
        }
    }
}

/* Michael Novak < 03 Dec 2008>
 This method checks whether the passed switch name has the passed value
 Arguments
  argc  , i - Number of commandline arguments
  argv  , i - array which holds values of command line arguments
  switch_name, i - description of switch to check
  value , i - Value to look for
 Return
  logical - if passed switch is set to the passed value then returns true, otherwise false.
*/
static logical parameter_set(int argc, char **argv, char *switch_name, char *value)
{

    logical ret_val = false;
    int i;
    for (i = 1; i < argc; i++)
    {
        switch_descriptor_p_t descriptor = match_switch(argv[i]);

        if ( descriptor != NULL )
        {
            if (strcmp( descriptor->switch_name, switch_name ) == 0 )
            {

                /* check whether the value of encryption flag is set to true
                   the value is after the "=" delimiter
                */
                if ( strcmp( find_value(argv[i]), value ) == 0 )
                {
                    ret_val = true;
                    break;
                }
            }
        }
    }
    return ret_val;
}

//--------------------------------------------------------------------------------------------------------------
// <ingle> 02-May-2013 CAE1469
// Provide support for adding related drawings to the clone/export operations
static void copy_related_drawings(const char* switch_value)
{
    logical flag = false;
    if(switch_value == NULL || switch_value[0] == '\0')
        error("Value required for copy_related_drawings switch");

    if(is_prefix(switch_value,"yes",0))
        flag = true;

    uf_check(UF_CLONE_set_clone_related_dwgs(flag),
        "While setting copy_related_drawings to %s",
        switch_value);
}

//--------------------------------------------------------------------------------------------------------------
// <ingle> 02-May-2013 CAE1469
// Provide support for adding related cae parts to the clone/export operations
static void copy_related_cae_parts(const char* switch_value)
{
    UF_CLONE_clone_rel_cae_t flag = UF_CLONE_clone_none;
    if (switch_value == NULL || switch_value[0] == '\0')
        error("Value required for copy_related_cae_parts switch");

    if(is_prefix(switch_value,"all",0))
    {
        flag = UF_CLONE_clone_sim_fem_ideal;
    }
    else if(is_prefix(switch_value,"fem",0))
    {
        flag = UF_CLONE_clone_fem_ideal;
    }
    else if(is_prefix(switch_value,"ideal",0))
    {
        flag = UF_CLONE_clone_ideal;
    }

    uf_check(UF_CLONE_set_clone_related_cae(flag),
        "While setting copy_related_cae_parts to %s",
        switch_value);
}

//--------------------------------------------------------------------------------------------------------------
// <Nikhil Vijay> 16-Mar-2018 TCIN130001
// Provide support for adding related drawings to the clone/export operations
static void export_extern_files(const char* switch_value)
{
    logical flag = true;
    if (switch_value == NULL || switch_value[0] == '\0')
        error("Value required for export_extern_files switch");

    if (is_prefix(switch_value, "no", 0))
        flag = false;

    uf_check(UF_CLONE_set_export_external_files(flag),
        "While setting export_ext_files to %s",
        switch_value);
}

//--------------------------------------------------------------------------------------------------------------
// <wrkab7> 23-May-2021 ER#10056454
// Provide support to exclude reference only components from the export operation
static void exclude_reference_only(const char* switch_value)
{
    if (switch_value == NULL || switch_value[0] == '\0')
        error("Value required for exclude_reference_only switch");

    logical flag = false;
    if (is_prefix(switch_value, "yes", 0))
        flag = true;
    else if (is_prefix(switch_value, "no", 0))
        flag = false;
    else
        error("Invalid value \"%s\" for exclude_reference_only switch", switch_value);

    uf_check(UF_CLONE_set_exclude_reference_only(flag), "While setting exclude_reference_only to %s", switch_value);
}

//--------------------------------------------------------------------------------------------------------------
// <wrkab7> 23-May-2021 ER#10056454
// Provide support to exclude non geometric components from the export operation
static void exclude_ngc(const char* switch_value)
{
    if (switch_value == NULL || switch_value[0] == '\0')
        error("Value required for exclude_ngc switch");

    logical flag = false;
    if (is_prefix(switch_value, "yes", 0))
        flag = true;
    else if (is_prefix(switch_value, "no", 0))
        flag = false;
    else
        error("Invalid value \"%s\" for exclude_ngc switch", switch_value);

    uf_check(UF_CLONE_set_exclude_ngc(flag), "While setting exclude_ngc to %s", switch_value);
}
