/* 
===============================================================================

 Copyright (c) 1992 - 1998,1999,2001 Unigraphics Solutions Inc.
                       Unpublished - All rights reserved

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

#include <stdlib.h>
#include <stdarg.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

#include <uf.h>
#include <uf_cfi.h> /* for uc4621 */
#include <uf_part.h>
#include <uf_clone.h>
#include <ufd_clone.h>
#include <uf_ugmgr.h>
#include <uf_kf_ugmgr.h>

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
static void name_rule(const char * switch_value);
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
static void rev_up_read_only(const char *ignored);


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
static int ug_legacy_trans(const char input[MAX_FSPEC_SIZE+1], char output[MAX_FSPEC_SIZE]);
static logical is_the_value_dfa( const char *value, int option );

/*================================================================================
  
  Global Variables

  ================================================================================*/

static switch_descriptor_t switch_descriptors[] = {
/*   switch name                min   handler function          multi seen
                               length                                      */
    {"pim",                       3,  ignore_arg,               true, false,
     "=yes to initialise NX Manager rather than native NX"}, /* multi is harmless, though not useful */
    {"user",                      1,  ignore_arg,               false, false,
     "=<user> to specify NX Manager user name"},
    {"group",                     1,  ignore_arg,               false, false,
     "=<group> to specify NX Manager group name"},
    {"password",                  1,  ignore_arg,               false, false,
     " to specify NX Manager password"},
    {"corba_ior_file",            14,  ignore_arg,               false, false,
     " to specify imanserver IOR file"},
    {"operation",                 1,  operation,                false, false,
     "=clone|edit|import|export required, must precede arguments below"},
    {"family_treatment",          3,  family_treatment,         false, false,
     "=lose|strip_status|error specifies how to treat Part Family Members\n\tIf adding an assembly containing Family Members, this switch must\n\tbe positioned before the -assembly switch.\n\t Default is error"
    }, 
    {"assembly",                  4,  assembly,                 true,  false,
     "=<root assembly> to add an assembly to the operation"},
    {"part",                      3,  part,                     true,  false,
     "=<single part> to add a part to the operation"},
    {"directory",                 3,  directory,                true,  false,
     "=<directory name> to add all assemblies in that directory to the operation"},
    {"folder",                 3,  folder,                true,  false,
     "=<folder name> as <user>:<folder>:<folder...> to add all assemblies in that folder to the operation"},
    {"default_checkin",           14, default_checkin,          false, false,
     "=yes:yes|yes:no|no, default is no"},
    {"default_checkout",          14, default_checkout,         false, false,
     "=yes:<comment>|no, default is no"},
    {"default_action",            9,  default_action,           false, false,
     "=clone|retain|overwrite|use_existing|exclude|new_revision"},
    {"default_naming",            9,  default_naming,           false, false,
     "=autogen|autotranslate|name_rule|user_name"},
    {"autotranslate_mode",         3,  autotranslate_mode,       false, false,
     "=<default|legacy> \n\tspecifies whether autotranslate mode for import should be:\n\t\tthe default or \n\t\tlegacy compatible (use DB_ attributes if present otherwise leaf name)\n\tDefault is default"},
    {"default_type",              9,  default_type,             false, false,
     "=<item_type> specifies default NX Manager item type"},
    {"associated_file_root_dir",  4,  associated_file_root_dir, false, false,
     "=<directory> specifies default NX Manager Associated file directory"},
    {"copy_associated_files",     6,  copy_associated_files,    false, false,
     "=yes|no specifies whether to copy NX Manager Associated files\n\tdefault is yes"},
    {"copy_non_master",           6,  copy_nonmaster,           true,  false,
     "=<nonmaster-type>:yes|no\n\tspecifies whether to copy NX Manager Non-Master files"},
    {"default_owner",             9,  default_owner,            false, false,
     "=<user>:<group> specifies default NX Manager user and group to own parts"},
    {"name_rule",                 1,  name_rule,                false, false,
     "=prepend:<string>|append:<string>|replace:<base_string>:<replace_string>|rename:<string>"},
    {"default_folder",            9,  default_folder,           false,  false,
     "=<default-folder>"},
    {"default_directory",         9,  default_directory,        false,  false,
     "=<default-directory>"},
    {"load_log_file",             1,  load_log_file,            true,  false,
     "=<log-file-name>"},
    {"save_log_file",             1,  save_log_file,            false, false,
     "=<log-file-name>"},
    {"revision_rule",             1,  revision_rule,            true, false,
     "=<revision rule name>"},
    {"dryrun",                    2,  dryrun,                   false, false,
     ""},
    {"propagate_actions",         9,  propagate_actions,        false, false,
     "=<yes|no> specifies whether to propagate \n\taction settings to referenced and referencing parts\n\tDefault is no. \n\tThis option is intended for use by other applications driving ug_clone, not for direct use."},
    {"export_dfa_kf",             13,  export_dfa_kf,            false, false,
     " specify this option in the beginning of the argument list to export the dfa files\n\tExamples to use export_dfa_kf\n\t\t1.ug_clone -pim=yes -export_dfa_kf=dfa_only -o=export -part=<dfaclassname> (for dfa files)\n\t\t2.ug_clone -pim=yes -export_dfa_kf=dfa_in_part -o=export -part=<@DB/testprt/A> (for dfa files referenced by part)"},
    {"export_dfa_list",           15,  export_dfa_list,            false, false,
     " specify this option to export the dfa filenames listed in an input file\n\tExamples to use export_dfa_list\n\t ug_clone -pim=yes -export_dfa_kf=dfa_only -export_dfa_list -o=export -part=<input file list name>"},
    {"rev_up_read_only",          6,  rev_up_read_only,         false, false,
     " specifies that new revision will be created if operation=IMPORT,\n\t action=OVERWRITE, and dataset is read only"},
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

static const char * program_name = NULL;

static char * part_being_operated_on = NULL;

/* DFA global variables */
static logical is_dfa = false ;
static logical is_dfa_in_part = false ;
static logical is_dfa_list = false ;
static logical dfa_export = FALSE;
static int dfa_export_option;

/*================================================================================
  
  Function Definitions

  ================================================================================*/

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
  differ, compared case-independantly
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
  abbreviations by recognising a match if the whole of the input
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
    int i = 0;

    program_name = argv[0];
    
    for (i = 1; i < argc; i++)
    {
        switch_descriptor_p_t descriptor = match_switch(argv[i]);

        if (descriptor == NULL)
            error("Unknown switch %s, use -help for usage information",argv[i]);

        if (descriptor->seen && !descriptor->multi)
            error("Repeated switch %s",argv[i]);

        descriptor->seen = true;
        
        descriptor->handler(find_value(argv[i]));
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
        char input_display_name[MAX_FSPEC_SIZE+1];
        char output_display_name[MAX_FSPEC_SIZE+1];
        char error_message[MAX_LINE_SIZE+1];
        
        int rc = UF_PART_name_for_display(failures->input_names[i],input_display_name);

        if (rc != 0)
            strcpy(input_display_name,failures->input_names[i]);

        if (failures->output_names[i] == NULL)
            strcpy(output_display_name,"");
        else
        {
            rc = UF_PART_name_for_display(failures->output_names[i], output_display_name);
            if (rc != 0)
                strcpy(output_display_name,failures->output_names[i]);
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
            char display_name[MAX_FSPEC_SIZE+1];
            int display_rc = UF_PART_name_for_display(load_status->file_names[i],display_name);
            if (display_rc != 0)
                strcpy(display_name,load_status->file_names[i]);

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
            char display_name[MAX_FSPEC_SIZE+1];
            int display_rc = UF_PART_name_for_display(load_status->file_names[i],display_name);
            if (display_rc != 0)
                strcpy(display_name,load_status->file_names[i]);

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
            strcat(buffer,"[");
            strcat(buffer,switch_descriptors[i].switch_name + switch_descriptors[i].min_chars);
            strcat(buffer,"]");
        }
        else
            strcpy(buffer,switch_descriptors[i].switch_name);
        message("\t%c%s%s",switch_starts[0],buffer,switch_descriptors[i].help_text);
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
        op = UF_CLONE_import_operation;
    else
        error("Unexpected value %s given to operation switch",switch_value);
    
    uf_check(UF_CLONE_initialise(op),"while initialising %s operation",operation_names[op]);

    /*
      Make sure that a log file gets generated with a default name
      if the user never sets one explicitly.
    */
    {
        char default_log_file[MAX_FSPEC_SIZE+1];
        sprintf(default_log_file,"%s.clone",operation_names[op]);
        uf_check(UF_CLONE_set_logfile(default_log_file),"While setting default log file to %s",default_log_file);
    }
    
    if ( op == UF_CLONE_export_operation )
        dfa_export = TRUE;
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
                load_stat_rc = report_load_status(&load_status);
        
            switch(rc)
            {
            case UF_CLONE_err_bvr_out_of_sync:
                /*
                  will have been reported above, fall through
                */
            case UF_CLONE_err_comp_not_found:
                /*
                  will have been reported above, check for other errors
                */
                uf_check(load_stat_rc,"While adding assembly %s to the operation",switch_value);
                break;
            default:
                uf_check(rc,"While adding assembly %s to the operation",switch_value);
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

static void name_rule(const char *switch_value)
{
    char * switch_copy = NULL;
    char * type_string = NULL;
    UF_CLONE_name_rule_def_t rule_def = {UF_CLONE_prepend_string,NULL,NULL};

    if (switch_value == NULL || switch_value[0] == '\0')
        error("Value required for name_rule switch");
    
    switch_copy = copy_string(switch_value);
    type_string = strtok(switch_copy,":");
    
    if (is_prefix(type_string,"prepend",0))
    {
        rule_def.type = UF_CLONE_prepend_string;
        rule_def.base_string = NULL;
        rule_def.new_string = strtok(NULL,":");
    } 
    else if (is_prefix(type_string,"append",0))
    {
        rule_def.type = UF_CLONE_append_string;
        rule_def.base_string = NULL;
        rule_def.new_string = strtok(NULL,":");
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
        rule_def.new_string = strtok(NULL,":");
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
    
    if((operation_class == UF_CLONE_export_operation))
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
    
    uf_check(UF_CLONE_set_def_directory(switch_value),
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
    uf_check(UF_CLONE_set_dryrun(true),"While setting dryrun to true");
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
    uf_check(UF_UGMGR_ask_user_folder(folder_name,&folder_tag),"Getting home folder for user %s",folder_name);
    
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
                char this_folder_name[UF_UGMGR_NAME_SIZE+1];
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

    if((operation_class == UF_CLONE_import_operation))
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
            char this_part_number[UF_UGMGR_NAME_SIZE+1];
            char this_part_revid[UF_UGMGR_NAME_SIZE+1];
            char this_part_specification[MAX_FSPEC_SIZE+1];
            
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
    uf_check(uc4508((char *)switch_value,options,ignored,"*.prt"),"Opening directory %s",switch_value);
    while((error_code = uc4518()) == 0)
    {
        char file_name[UF_CFI_MAX_PATH_NAME_LEN+1];
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
    uf_check(UF_UGMGR_set_config_rule((char *)switch_value),"While setting revision rule %s",switch_value);
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

static int ug_legacy_trans(const char input[MAX_FSPEC_SIZE+1], char output[MAX_FSPEC_SIZE])
{
    char *itemid = NULL;
    char *revid = NULL;
    char *file_type = NULL;
    char *file_name = NULL;
    char internal_form[MAX_FSPEC_SIZE+1];    
    int n_attributes;
    char ** attribute_titles;
    char **attribute_values;
    int ifail = 0;

    /* 
      Because we want to carry on in the event of a naming failure, we don't
      use uf_check here, we just keep track of the ifail value. copy_string
      may still stop the process, but only if we have run out of memory,
      which is fatal anyway.
    */
    ifail = UF_CLONE_ask_attribute_values(input,&n_attributes,&attribute_titles,&attribute_values);
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
            if (strcmp(attribute_titles[i],"DB_PART_NO") == 0)
                itemid =  copy_string(attribute_values[i]);
            else if (strcmp(attribute_titles[i],"DB_PART_REV") == 0)
                revid =  copy_string(attribute_values[i]);
            else if (strcmp(attribute_titles[i],"DB_MODEL_TYPE") == 0)
                file_type =  copy_string(attribute_values[i]);
            else if (strcmp(attribute_titles[i],"DB_MODEL_NAME") == 0)
                file_name =  copy_string(attribute_values[i]);
            if (ifail != 0)
                break;
        }
    }
    UF_free_string_array(n_attributes, attribute_titles);
    UF_free_string_array(n_attributes, attribute_values);
    if (ifail == 0 && itemid == NULL)
    {
        char simple_name[MAX_FSPEC_SIZE+1];
        ifail = uc4574((char *)input,2,simple_name);
        if (ifail == 0)
            itemid = copy_string(simple_name);
    }
    
    /* <APB> 11-Feb-2002 
      Now we've got an ItemID. We may already have a RevID, but for
      legacy compatibility the configured revision if there is one is supposed to override the
      attribute value, so we go looking for that, obviously if the part is
      new to this database, there won't be one.
    */
    if (ifail == 0)
    {
        UF_UGMGR_tag_t part_tag;
        ifail = UF_UGMGR_ask_part_tag(itemid,&part_tag);
        if (ifail == 0 && part_tag != null_tag)
        {
            UF_UGMGR_tag_t rev_tag;
            ifail = UF_UGMGR_ask_configured_rev(part_tag, &rev_tag);
            if (ifail != 0 && rev_tag != null_tag)
            {
                char rev[UF_UGMGR_NAME_SIZE+1];
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
    if (ifail == 0 && revid == NULL)
        revid = copy_string("A");
    
    if (ifail == 0)
        ifail = UF_UGMGR_encode_part_filename(itemid,revid,file_type,file_name,internal_form);
    
    UF_free(itemid);
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
    int ignored = 0;
    
    /*
      We call uc4624 to "remember" the argument list, despite the fact we do
      our own argument processing, because this is the call which notices
      the UG/Manager -pim, -user, -group and -password switches and
      initialises UG/Manager if they are present.
    */
    uc4624(ignored,argc,argv);
    
    register_callbacks();
    process_switches(argc,argv);

    if ( ( is_dfa ) && ( dfa_export) )
    {
        uf_check(UF_KF_UGMGR_initialize_export( dfa_export_option ),
                 "while performing export dfa");
    
        return ;
    }
    else
    {
    /*
      perform_clone will do an apply_defaults for us.
    */
        int rc = 0;
        UF_CLONE_naming_failures_t naming_failures;
        UF_CLONE_operation_class_t operation_class;
        char * logfilename = NULL;

        uf_check(UF_CLONE_ask_operation_class(&operation_class),"While asking operation class");
        uf_check(UF_CLONE_ask_logfile(&logfilename),"While asking log file name");

        fprintf(stderr,"Logging %s to %s\n",operation_names[(int)operation_class],logfilename);
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
   
        if ( is_dfa_in_part )
            uf_check(UF_UGMGR_KF_export_dfa_in_part( NULL ), 
                "While exporting DFA Classes referenced in part" );
 
        uf_check(UF_CLONE_terminate(),"While terminating clone");
    }
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
    vfprintf(stderr,format,args);
    fprintf(stderr,"\n");
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
        char message[MAX_LINE_SIZE+1];
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
    int  char_count    = 0;
    

    char_count = vfprintf ( stderr, format, args );
    if ( char_count > 0 )
    {
        int  errorCode     = 0;
        char *message      = NULL;
        message = ( char * ) UF_allocate_memory ( sizeof(char) * (char_count+1),
                                                  &errorCode );
        if ( errorCode == 0 )
        {
            vsprintf ( message, format, args );
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
        is_dfa = TRUE;
    else
        is_dfa_in_part = TRUE;
}

static void export_dfa_list( const char *ignored )
{
    is_dfa_list = TRUE;

    return;
}

static logical is_the_value_dfa( const char *value, int option )
{
    logical       exists = FALSE;
    int           error  = 0;
    char         *internal_encoded_name = NULL;
    char          part_number[UF_UGMGR_PARTNO_SIZE + 1];
    char          part_revision[UF_UGMGR_PARTREV_SIZE + 1];
    char          part_file_type[UF_UGMGR_FTYPE_SIZE + 1];
    char          part_file_name[UF_UGMGR_FNAME_SIZE + 1];

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
