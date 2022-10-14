/****************************************************************************

                  Copyright (c) 1999-2003 Unigraphics Solutions Inc.
                             Unpublished - All rights reserved

 

File Description:
   This include file declares routines used for performing clone
   operations and clone based PDM Assembly Import and Export
   functions. Using these routines you can:

   Clone an assembly

   Edit an Existing assembly in place

   Import an assembly to the PDM system

   Export an assembly from the PDM system

   Note that all these operations act on part files on disk, parts which
   are currently loaded in the session will not be affected - if you wish
   to operate on parts which have been modified in the current session
   you should save them first.

   It is also possible to register user supplied callback functions,
   which clone operations will call at appropriate times. These functions
   can be registered in for use in Interactive NX as well as in
   Open API programs.

   The callback functions are of two types:

   Notify callbacks; these are called before and after actions are taken
   during a clone operation. A callback called before the action is taken
   has the option to forbid that operation from occurring. This could
   allow enforcement of company practices or conventions. Notify
   callbacks can also be useful to allow you to take actions which are a
   part of your company processes when a clone operation is performed,
   setting specific part attributes when a part is exported from the
   NX Manager database for instance. Finally they can be used to provide
   feedback to the user about the progress of the operation.

   Convert Callbacks; these are called when NX requires a value
   for a piece of information that has not been specifically supplied by
   the user or program. They are called before NX goes on to
   apply its own default algorithms for generating these values.

   In both cases, multiple callbacks can be registered at the same
   callback point - the callback lists are ordered, and callbacks earlier
   in the list can allow callbacks later in the list to be called, or
   prevent them from being so, by returning appropriate return codes.

   Note on Nomenclature: because the functions and types declared here
   can be used both within NX Manager or outside it (when performing a
   clone), or both at the same time (when performing an import or an
   export), there is a nomenclature problem. What NX Manager calls a part
   'number', native NX calls a part 'name'. NX Manager has a database
   attribute of 'name' which is *not* the same as the part number.

   In this file, name is used throughout in the native NX sense,
   corresponding to the NX Manager part number. The term 'pdm_name' is
   used for the database attribute 'name'.

   'def' is uniformly used in function names as an abbreviation for
   'default', likewise 'co' for 'checkout'.

******************************************************************************/

#ifndef UF_CLONE_INCLUDED
#define UF_CLONE_INCLUDED


/***************************************************************************

  ***************************************************************************/

#include <uf_part_types.h>
#include <uf_retiring.h>
#include <uf_attr.h>
#include <uf_clone_internal.h>
#include <libufun_exports.h>

#ifdef __cplusplus
extern "C" {
#endif

#define ERROR_UF_CLONE_base    3025000
/***************************************************************************
  
  ***************************************************************************/


/* The error codes supplied here are those which the programmer may
   wish to detect and handle programmatically. They are *not* a full list
   of those errors which UF_CLONE functions can return.
*/
#define UF_CLONE_err_not_active             (ERROR_UF_CLONE_base + 1)
#define UF_CLONE_err_iterator_active        (ERROR_UF_CLONE_base + 2)
#define UF_CLONE_err_part_not_present       (ERROR_UF_CLONE_base + 3)
#define UF_CLONE_err_active                 (ERROR_UF_CLONE_base + 4)
#define UF_CLONE_err_no_iterator            (ERROR_UF_CLONE_base + 5)
#define UF_CLONE_err_dryrun_with_no_logfile (ERROR_UF_CLONE_base + 6)
#define UF_CLONE_err_validation_failures    (ERROR_UF_CLONE_base + 7)

/*  <JJLD> 05-Aug-2003
    These are from assy.h*/
#define UF_CLONE_err_comp_not_found         (720090)
#define UF_CLONE_err_bvr_out_of_sync        (720091)
#define UF_CLONE_err_invalid_logfile        (720094)
#define UF_CLONE_err_naming_failures        (720117)
#define UF_CLONE_err_no_relative_cb         (720127)
#define UF_CLONE_err_invalid_folder         (720144)
#define UF_CLONE_err_no_copy_access         (720158)
#define UF_CLONE_err_xml_nested_alt_reps    (720181)

/*  <JJLD> 05-Aug-2003
    This is from part.h */
#define UF_CLONE_err_corrupt_part_file      (641001)

/*  <JJLD> 05-Aug-2003
        From opl.h*/
#define UF_CLONE_err_family_member          (870014)
#define UF_CLONE_err_appdata_not_found      (870012)


/* the following typedefs and functions (up to the comment "duplicates
   end here" have duplicate functionality with the UF_ASSEM_CLONE prefix, for
   historical reasons. The declarationss here are the preferred ones, the
   UF_ASSEM_clone_ functions will be retired in a later version of
   NX. The implementation of the provided functionality here
   differs in detail from that in the UF_ASSEM_clone implementation, code
   will have to be re-written to use the new functions, rather than
   simply replacing the old function call with the new one.

   Where the UF_ASSEM_clone interface refers to number (or num) for a
   part number, name is used here (see the note on nomenclature above).
*/

/* the types of clone operation available.  */
enum UF_CLONE_operation_class_e
{
        UF_CLONE_clone_operation,
        UF_CLONE_edit_operation,
        UF_CLONE_import_operation,
        UF_CLONE_export_operation
} ;
typedef enum UF_CLONE_operation_class_e UF_CLONE_operation_class_t,
             *UF_CLONE_operation_class_p_t;

struct UF_CLONE_ex_log_opts_s
{
    logical allow_missing_components; /*
                                         A flag indicating whether the clone
                                         should proceed even if components in
                                         the assembly being cloned cannot be
                                         found
                                      */
    logical allow_out_of_sync_bvrs; /*
                                       A flag for use in a NX Manager
                                       environment to control the clone
                                       operation's behaviour with respect
                                       to BOM View Revisions (BVR's) - see the
                                       NX Manager Users Manual for an
                                       explanation of these. The flag indicates
                                       whether the clone should proceed even if
                                       components in the assembly have BVR's in
                                       the database that are not synchronised
                                       with the NX component structure.
                                       The flag will be ignored in a
                                       Native NX environment.
                                    */
} ;
typedef struct UF_CLONE_ex_log_opts_s UF_CLONE_ex_log_opts_t,
               *UF_CLONE_ex_log_opts_p_t;

/***********************************************************************
This routine receives the name of a log file and an operation class performs
a clone operation using the log-file to specify the assemblies to clone and
to supply the action and naming operations for the clone operation.

Environment : Internal  and  External
See Also: UF_CLONE_ex_log_opts_p_t
History : Originally released in V16.0
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_execute_log_file
(
    UF_CLONE_operation_class_t   operation_class,  /* <I>
                                                      class of operation to
                                                      perform
                                                   */
    const char                  *logfile_name,     /* <I>
                                                      name of log file to use to
                                                      specify assemblies to
                                                      clone
                                                   */
    UF_CLONE_ex_log_opts_p_t     options           /* <I>
                                                      options to apply to
                                                      operation
                                                   */
);

/* UF_CLONE_action_e: enum specifying a default action to be
   applied to components in a clone, import or export operation.
*/
enum UF_CLONE_action_e
{
    UF_CLONE_clone, /* used for clone operations */
    UF_CLONE_retain, /* used for clone operations */
    UF_CLONE_replace, /* used for clone operations */
    UF_CLONE_overwrite, /* used for import or export operations */
    UF_CLONE_use_existing, /* used for import or export operations */
    UF_CLONE_default_action, /* used for clone, import, export etc
                                to simply use the default action specified
                                at start of the operation */
    UF_CLONE_exclude, /* used for export operations */
    UF_CLONE_new_revision /* used for import operations */
} ;
typedef enum UF_CLONE_action_e UF_CLONE_action_t, *UF_CLONE_action_p_t;

/* UF_CLONE_naming_technique_t: enum specifying a numbering
   technique for a clone operation.
*/
enum UF_CLONE_naming_technique_e
{
    UF_CLONE_autogen,
    UF_CLONE_autotranslate,
    UF_CLONE_naming_rule,
    UF_CLONE_user_name,
    UF_CLONE_default_naming
} ;
typedef enum UF_CLONE_naming_technique_e UF_CLONE_naming_technique_t,
             *UF_CLONE_naming_technique_p_t;

/*  UF_CLONE_family_treatment_e: Enum specifying ways of coping with
    part family members that have been added to clone operations.

    treat_as_lost means that they will be treated as lost parts.

    strip_family_status means that they will be imported/exported
    but will lose their part family status. This is only permitted
    for Clone Import/Export; not for a pure clone operation.

    give_error is the default value, and means that adding an assembly
    to User Function will fail if that assembly contains family members.
    
 */
enum UF_CLONE_family_treatment_e
{
    UF_CLONE_treat_as_lost,
    UF_CLONE_strip_family_status,
    UF_CLONE_give_error
};

typedef enum UF_CLONE_family_treatment_e UF_CLONE_family_treatment_t,
             *UF_CLONE_family_treatment_p_t;


/* UF_CLONE_copy_nm_opt_t: Element of a linked list setting the
   flag for a specific non-master type to indicate whether or not it
   should be copied during a clone, import or export operation, the
   list is terminated by setting the next field of this structure to
   NULL. This structure can be either an input argument to a _set_
   function or an output argument of an _ask_ function.
*/
struct UF_CLONE_copy_nm_opt_s
{
    char *nonmaster_type; /* <OF> when structure is being
                             returned a string containing the name of a
                             nonmaster type defined in the database, such as
                             "specification"
                          */
    logical copy;         /* <O> when structure is being returned
                            a logical indicating whether this nonmaster type
                            should be copied during a clone operation, imported,
                            or exported. TRUE means that nonmasters of that
                            type will be copied
                         */
    struct UF_CLONE_copy_nm_opt_s *next; /* <OF> when structure
                                            is being returned a pointer to the
                                            next element in the linked list of
                                            options
                                        */
} ;
typedef struct UF_CLONE_copy_nm_opt_s UF_CLONE_copy_nm_opt_t,
               *UF_CLONE_copy_nm_opt_p_t;

/* UF_CLONE_validation_mode_e: Validation mode to be applied to components
   during a import operation in an NX Manager environment
*/
enum UF_CLONE_validation_mode_e
{
    UF_CLONE_no_validation,
    UF_CLONE_import_from_part,
    UF_CLONE_run_validation,
    UF_CLONE_run_validation_hybrid
};
typedef enum UF_CLONE_validation_mode_e UF_CLONE_validation_mode_t,
               *UF_CLONE_validation_mode_p_t;


/* Validation options indicating how validation objects should be created during
   the import operation.  Only relevant for the import operation in an NX Manager
   environment.  This structure may be null ? no validation objects will be created.
*/
struct UF_CLONE_validation_opts_s
{
    UF_CLONE_validation_mode_t         mode; /*
                                               Default  validation mode to be applied to
                                               components
                                            */
    char * validation_rule; /* <OF> The validation rule file name to be used to compare
                                    with valdation results. It could be an O/S file name
                                    or a name in CLI format. Must specify one when mode
                                    is not UF_CLONE_no_validation
                                    This must be freed using UF_free
                                    */
    logical  treat_warning_as_pass; /*
                                    A flag indicating whether to treat a validation result
                                    with the status "Pass but with warning" as PASS or not
                                    while comparing this validation result with validation rule
                                    */
    logical treat_outdated_as_pass; /*
                                    A flag indicating whether to treat a validation result
                                    with the status "Pass but outdated" as PASS or not
                                    while comparing this validation result with validation rule
                                    */
} ;

typedef struct UF_CLONE_validation_opts_s UF_CLONE_validation_opts_t,
               *UF_CLONE_validation_opts_p_t;


/************************************************************************
This routine sets the default validation related options

Environment : Internal  and  External
See Also: UF_CLONE_ask_def_validation_options
History : Originally released in NX5.0
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_set_def_validation_options
(
    UF_CLONE_validation_opts_p_t validation_options /* <I>
                                                    default validation options
                                                 */
);

/************************************************************************
This routine returns the default validation related options

Environment : Internal  and  External
See Also: UF_CLONE_set_def_validation_options
          UF_CLONE_validation_opts_t
History : Originally released in V5.0
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_ask_def_validation_options
(
    UF_CLONE_validation_opts_p_t *validation_options /* <OF,free:UF_CLONE_free_validation_options>
                                                     Default validation options
                                                     Must be freed using UF_CLONE_free_validation_options
                                                  */
);

/************************************************************************
This routine returns the default validation related options

Environment : Internal  and  External
See Also: UF_CLONE_ask_def_validation_options
          UF_CLONE_ask_validation_options
          UF_CLONE_validation_opts_t
History : Originally released in V5.0
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_free_validation_options
(
    UF_CLONE_validation_opts_p_t validation_options /* <I>
                                                     validation options to  be freed
                                                  */
);

/************************************************************************
This routine sets the validation option for for the specified part.

Environment : Internal  and  External
See Also: UF_CLONE_set_def_validation_options
          UF_CLONE_ask_validation_options
          UF_CLONE_ask_def_validation_options
History : Originally released in V5.0
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_set_validation_options
(
    const char *input_part_name,/*<I>
                                  Part name of part in the current cloning
                                  operation. It is a native O/S file name.
                                  Only relevant for import operation
                                  in an NX Manager environment.
                               */
    UF_CLONE_validation_opts_p_t validation_options /* <I>
                                                     validation options
                                                 */
);

/************************************************************************
This routine returns validation options for the specified part.

Environment : Internal  and  External
See Also:  UF_CLONE_set_def_validation_options
           UF_CLONE_set_validation_options
           UF_CLONE_ask_def_validation_options
History : Originally released in V5.0
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_ask_validation_options
(
    const char *input_part_name,/*<I>
                                  Part name of part in the current cloning
                                  operation. It is a native O/S file name.
                                  Only relevant for import operation
                                  in an NX Manager environment.
                               */
    UF_CLONE_validation_opts_p_t *validation_options /* <OF>
                                                      Default validation options
                                                      Must be freed using UF_CLONE_free_validation_options
                                                  */
);


/************************************************************************
This routine sets the global validation abort options

Environment : Internal  and  External
See Also: UF_CLONE_ask_validation_abort_option
History : Originally released in NX5.0
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_set_validation_abort_option
(
    logical abort_import /* <I>
                            whether to abort part import when validation failed
                         */
);

/************************************************************************
This routine returns the global validation abort options

Environment : Internal  and  External
See Also: UF_CLONE_set_def_validation_options
History : Originally released in V5.0
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_ask_validation_abort_option
(
    logical *abort_import /* <O>
                                      whether to abort part import when validation failed
                                         */
);

struct UF_CLONE_gen_log_opts_s
{
    UF_CLONE_action_t        default_action; /* <I>
                                               enum value indicating the default
                                               action to be applied to
                                               components
                                            */

    UF_CLONE_naming_technique_t  default_naming; /* <I>
                                                    enum value indicating the
                                                    default naming technique to
                                                    be applied to components
                                                 */
    UF_CLONE_copy_nm_opt_p_t copy_nonmaster_opts; /* <I>
                                                     a linked list of
                                                     nonmaster_type/logical
                                                     pairs indicating whether
                                                     those nonmaster types
                                                     should be copied during
                                                     the clone, import or
                                                     export operation. Only
                                                     relevant in a NX Manager
                                                     environment, may be null.
                                                  */
    UF_CLONE_validation_opts_p_t default_validation_opts; /* <I>
                                                     a data structure
                                                     indicating the options
                                                     to control whether and
                                                     how the validation objects
                                                     should be created during
                                                     the import operation. Only
                                                     relevant for import operation
                                                     in a NX Manager
                                                     environment, may be null.
                                                     When null is used, validation
                                                     objects will not be created.
                                                  */

} ;
typedef struct UF_CLONE_gen_log_opts_s UF_CLONE_gen_log_opts_t,
               *UF_CLONE_gen_log_opts_p_t;

/************************************************************************
This routine receives the name of an input assembly and the name of
a log file and performs a dryrun clone operation with the logging
output written to the given log file. This is suitable for
generating a basic log file for subsequent editing external to
NX before being used as input to UF_CLONE_execute_log_file

Environment : Internal  and  External
See Also: UF_CLONE_execute_log_file
History : Originally released in V16.0
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_create_log_file
(
    UF_CLONE_operation_class_t   operation_class,    /* <I>
                                                        class of operation to
                                                        execute dryrun for
                                                     */
    const char                  *input_name,         /* <I>
                                                        input assembly
                                                     */
    const char                  *logfile_name,       /* <I>
                                                        name of log file to be
                                                        generated
                                                     */
    UF_CLONE_gen_log_opts_p_t    options             /* <I>
                                                        options to apply to
                                                        dryrun operation
                                                     */
);

/***************************************************************
*                                                              *
*               duplicate functionality ends here              *
*                                                              *
***************************************************************/

/************************************************************************
This routine initialises a clone operation. If a clone
operation has already been started this routine will return
UF_CLONE_err_active.


Environment : Internal  and  External
See Also:
History : Originally released in V16.0
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_initialise
(
        UF_CLONE_operation_class_t operation_class /* <I>
                                                      class of operation to
                                                      initialise
                                                   */
);

/************************************************************************
This routine terminates the current clone operation if there is
one, returns no error if there is not


Environment : Internal  and  External
See Also: UF_CLONE_initialise
History : Originally released in V16.0
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_terminate(void);

/************************************************************************
This routine Resets the state of the current clone operation so that no parts
have exceptions or defaults applied to them, but leaving all the parts already
in the clone operation present.

Environment : Internal  and  External
See Also: UF_CLONE_unapply_defaults
History : Originally released in V16.0
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_reset_to_default(void);

/************************************************************************
This routine specified the name of the log-file to be used to record this
operation. If the value specified is NULL, no logfile will be written.

The log file will be attached as a named reference to any root
parts (whether input ot output) that are stored in the PDM.

Environment : Internal  and  External
See Also:
History : Originally released in V16.0
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_set_logfile
(
    const char  *log_file_name /* <I>
                                  name of logfile to be written (an O/S file
                                  name, even in NX Manager)
                               */
);

/************************************************************************
This routine returns a string containing the name of the log file that will
be written when UF_CLONE_perform_clone is called. If the value returned is
NULL, no log file has been specified, and so no log file will be written.

Environment : Internal  and  External
See Also: UF_CLONE_set_logfile
            UF_CLONE_perform_clone
History : Originally released in V16.0
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_ask_logfile
(
    char **log_file_name /* <OF>
                            the name of the logfile that will be written by this
                            clone operation or NULL if one has not been
                            specified
                         */
);

/* structure used to report naming failures during operations such as
   reading a log file, applying defaults or setting a name rule.
*/
struct UF_CLONE_naming_failures_s
{
    int    n_failures;       /* <O>
                                Number of failures reported
                             */
    int   *statuses;         /* <OF,len:n_failures> with UF_free;
                                Error codes, use UF_get_fail_message() to get
                                a description
                             */
    char  **input_names;     /* <OF,len:n_failures,free:UF_FREE_string_array> - with UF_FREE_string_array;
                                part names of parts the failures apply to
                             */
    char  **output_names;    /* <OF,len:n_failures,free:UF_FREE_string_array> - with UF_FREE_string_array;
                                output names for parts the failures apply to
                                (may be null, since the part name may not have
                                been generated correctly)
                             */
} ;
typedef struct UF_CLONE_naming_failures_s UF_CLONE_naming_failures_t,
               *UF_CLONE_naming_failures_p_t;

/************************************************************************
This routine initialises a naming failures structure. It should be called
before passing the structure to UF_CLONE_apply_defaults or
UF_CLONE_perform_clone

Environment : Internal  and  External
See Also: UF_CLONE_apply_defaults
            UF_CLONE_perform_clone
            UF_CLONE_naming_failures_t
History : Originally released in V16.0
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_init_naming_failures
(
    UF_CLONE_naming_failures_p_t failures /* <O>
                                             pointer to structure to be
                                             initialised
                                          */
);

/* structure used to report extra details of an error detected when
   reading a log file, supplementary to the information given by applying
   UF_get_fail_message to the return code of the UF_CLONE_load_logfile
   call
*/
struct UF_CLONE_log_file_failure_s
{
    int     line_number;     /* <O>
                                line number in the log file on which the error
                                was detected
                             */
    char   *input_part_name; /*
                                <OF> with UF_free
                                part name being processed when error occurred,
                                may be NULL
                             */
    char   *invalid_token;   /* <OF> with UF_free
                                token which was invalid, may be NULL
                             */
} ;
typedef struct UF_CLONE_log_file_failure_s UF_CLONE_log_file_failure_t,
               *UF_CLONE_log_file_failure_p_t;

/************************************************************************
This routine initialises a logfile_failures structure. It should be called
before passing the structure to UF_CLONE_load_logfile

Environment : Internal  and  External
See Also: UF_CLONE_log_file_failure_t
            UF_CLONE_load_logfile
History : Originally released in V16.0
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_init_log_file_failure
(
    UF_CLONE_log_file_failure_p_t logfile_failures /* <OF>
                                                      pointer to structure to be
                                                      initialised
                                                   */
);

/************************************************************************
This routine reads the specified log file and applies the data in it to the
current  operation.

A log file contains <keyword> <value> pairs, in a defaults section, followed
by a sequence of Part: sections. See the Assembly Modelling User Manual or the
NX Manager User Manual for a description of how to generate log-files
automatically during a clone operation, and of their structure.

Part sections with an action will be added to the clone operation if not
already present. Part sections without an action will be added as NameOnly
references if not already present.

If any naming failures occur during loading the log file, these will be
reported via the naming_failures output argument (which should have been
initialised via a call to UF_CLONE_init_naming_failures) and
UF_CLONE_err_naming_failures returned. If the logfile is invalid,
UF_CLONE_err_invalid_logfile will be returned, and details of the problem
will be placed in the logfile_failure output argument (which should be
initialised by a call to UF_CLONE_init_log_file_failure).

If processing the log file causes new assemblies to be loaded, then any errors
while loading the assembly (parts not found, or warnings about out of sync
BVRs) will be reported through the load_status output argument.

If both naming failures and load failures occur, it is not defined which error
code the return value of the function will be - if you wish to report both
you should check the n_failures member of the naming_failures structure and
the failed member of the load_status structure to see if errors have occurred

Environment : Internal  and  External
See Also: UF_CLONE_log_file_failure_t
            UF_CLONE_naming_failures_t
          UF_PART_load_status_t
          UF_CLONE_init_naming_failures
          UF_CLONE_init_log_file_failure
          UF_CLONE_set_logfile
History : Originally released in V16.0
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_load_logfile
(
    const char * log_file_name,         /* <I>
                                           log file to load
                                        */
    UF_CLONE_naming_failures_p_t naming_failures, /* <I/O>
                                                     naming failures if any
                                                  */
    UF_CLONE_log_file_failure_p_t logfile_failure, /* <OF>
                                                     details of the log file
                                                     invalidity
                                                  */
    UF_PART_load_status_p_t          load_status /* <OF>
                                                 reports any failures to load
                                                 parts
                                              */
);

/************************************************************************
This routine sets a logical in the current clone operation indicating whether
associated files should by default be copied (for a clone), exported or
imported in the current operation.


Environment : Internal  and  External
See Also:
History : Originally released in V16.0
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_set_def_assoc_file_copy
(
    logical copy_associated /* <I>
                               whether to copy associated files by default
                            */
);

/************************************************************************
This routine returns a logical indication whether by default associated files
will be copied, imported or exported (as appropriate) in this clone operation.

Environment : Internal  and  External
See Also: UF_CLONE_set_def_assoc_file_copy
History : Originally released in V16.0
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_ask_def_assoc_file_copy
(
    logical *copy_associated /* <O>
                                whether to copy associated files by default */
);

/************************************************************************
This routine sets a logical for the specified part in the current clone
operation indicating whether associated files should by default be copied
(for a clone), exported or imported in the current operation.

Environment : Internal  and  External
See Also:
History : Originally released in V16.0
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_set_assoc_file_copy
(
    const char *input_part_name,   /* <I>
                                      part name of part in the current cloning
                                      operation, in NX Manager clone, or for an
                                      export operation, this should be a CLI
                                      name, otherwise a native O/S file name
                                   */
    logical copy_associated /* <I>
                               whether to copy associated files for this part
                            */
);


/************************************************************************
This routine returns the value of the associated file copy flag for the given
part.

Environment : Internal  and  External
See Also:
History : Originally released in V16.0
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_ask_assoc_file_copy
(
    const char *input_part_name, /* <I>
                                    part name of part in the current cloning
                                    operation, in NX Manager clone, or for an
                                    export operation, this should be a CLI name,
                                    otherwise a native O/S file name
                                 */
    logical *copy_associated    /* <O>
                                 whether to copy associated files for this part
                                */
);

/************************************************************************
This routine sets the nonmaster copy option for the nonmaster types specified
in the input list. Each list entry contains:
nonmaster_type: the name of the nonmaster type to which the entry applies
copy:           logical indicating whether it will be copied
next:           pointer to next element in list, NULL to end list

Environment : Internal  and  External
See Also: UF_CLONE_set_def_nm_copy
History : Originally released in V16.0
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_set_def_nm_copy
(
    UF_CLONE_copy_nm_opt_p_t copy_nonmaster_opts /* <I>
                                                    list of default nonmaster
                                                    copy options
                                                 */
);

/************************************************************************
This routine returns a list of nonmaster copy options. Each entry contains:
nonmaster_type: the name of the nonmaster type to which this
                flag applies, must be freed with UF_free
copy:           logical indicating whether it will be copied
next:           pointer to next element in list, NULL to end list

each entry must also be freed after use using UF_free

Environment : Internal  and  External
See Also: UF_CLONE_set_def_nm_copy
          UF_CLONE_copy_nm_opt_t
History : Originally released in V16.0
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_ask_def_nm_copy
(
    UF_CLONE_copy_nm_opt_p_t *copy_nonmaster_opts /* <OF>
                                                     list of default nonmaster
                                                     copy options,
                                                     which must each be freed
                                                  */
);

/************************************************************************
This routine sets the nonmaster copy option for the nonmaster types specified
in the input list for the specified part.
Each list entry contains:
nonmaster_type: the name of the nonmaster type to which the entry applies
copy:           logical indicating whether it will be copied
next:           pointer to next element in list, NULL to end list

Environment : Internal  and  External
See Also: UF_CLONE_set_def_nm_copy
          UF_CLONE_ask_nm_copy
          UF_CLONE_ask_def_nm_copy
History : Originally released in V16.0
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_set_nm_copy
(
    const char *input_part_name,/*<I>
                                  part name of part in the current cloning
                                  operation, in NX Manager clone, or for an
                                  export operation, this should be a CLI name,
                                  otherwise a native O/S file name
                               */
    UF_CLONE_copy_nm_opt_p_t copy_nonmaster_opts /* <I>
                                                    list of nonmaster copy
                                                    options
                                                 */
);

/************************************************************************
This routine returns a list of nonmaster copy options for the specified part.
Each entry contains:
nonmaster_type: the name of the nonmaster type to which this
                flag applies, must be freed with UF_free
copy:           logical indicating whether it will be copied
next:           pointer to next element in list, NULL to end list

each entry must also be freed after use using UF_free

Environment : Internal  and  External
See Also:  UF_CLONE_set_def_nm_copy
           UF_CLONE_set_nm_copy
           UF_CLONE_ask_def_nm_copy
History : Originally released in V16.0
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_ask_nm_copy
(
    const char *input_part_name,/*<I>
                                  part name of part in the current cloning
                                  operation, in NX Manager clone, or for an
                                  export operation, this should be a CLI name,
                                  otherwise a native O/S file name
                               */
    UF_CLONE_copy_nm_opt_p_t *copy_nonmaster_opts /* <OF>
                                                     list of nonmaster copy
                                                     options
                                                  */
);

/************************************************************************
This routine sets the dryrun flag for the current operation. See
UF_CLONE_ask_dryrun for details of how this behaves

Environment : Internal  and  External
See Also:
History : Originally released in V16.0
***********************************************************************/
extern UFUNEXPORT int  UF_CLONE_set_dryrun
(
    logical dryrun /* <I>
                      true for a dryrun, false for the clone to actually take
                      place
                   */
);

/************************************************************************
This routine returns the value of the dryrun flag for the current operation.
If this flag is true, then when UF_CLONE_perform_clone is called,  a log file
will be written but the operation will not actually be performed.  A log
file must be specified for the dryrun to work.

Environment : Internal  and  External
See Also: UF_CLONE_set_dryrun
          UF_CLONE_perform_clone
          UF_CLONE_set_logfile
History : Originally released in V16.0
***********************************************************************/
extern UFUNEXPORT int  UF_CLONE_ask_dryrun
(
    logical *dryrun /* <O>
                       true for a dryrun, false if the operation will actually
                       take place
                    */
);

/************************************************************************
This routine sets the treatment of Part Family Members by Clone.

UF_CLONE_treat_as_lost:       family members are regarded as lost parts.
                              The operation will proceed.
UF_CLONE_strip_family_status: family members are imported/exported as
                              normal parts: i.e. if you import a part
                              family member, the original NX part remains
                              a part family member, but NX Manager part
                              is not.
UF_CLONE_give_error:          the operation will return an error if it
                              encounters a part family member and will
                              not proceed.

Environment : Internal  and  External

History : Originally released in V18.0
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_set_family_treatment
(
    UF_CLONE_family_treatment_t treatment /* <I>
                                           treatment to be applied to
                                           part family members when
                                           added toclone operations.
                                          */
);

/************************************************************************
This routine asks what the treatment of Part Family Members by Clone is.
Environment : Internal  and  External

See also: UF_CLONE_set_family_treatment
History : Originally released in V18.0
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_ask_family_treatment
(
    UF_CLONE_family_treatment_t * treatment /* <O> */
);

enum UF_CLONE_name_rule_type_e
{
    UF_CLONE_prepend_string, /* prepend a string to the input name */
    UF_CLONE_append_string,  /* append a string to the input name */
    UF_CLONE_replace_string, /* replace a string in the input with another
                                string */
    UF_CLONE_rename   /* substitute the given string for the full name, the
                         replacement string should contain
                         references to attribute values to ensure uniqueness */
} ;
typedef enum UF_CLONE_name_rule_type_e UF_CLONE_name_rule_type_t,
             *UF_CLONE_name_rule_type_p_t;

/************************************************************************
    Structure describing a name rule. See the Assembly Modelling User
    Manual for a description of clone name rules.
***********************************************************************/
struct UF_CLONE_name_rule_def_s
{
    UF_CLONE_name_rule_type_t type; /* the type of this name rule */
    char * base_string;             /* string to be replaced (only valid for
                                       UF_CLONE_replace) */
    char * new_string;              /* string to prepend or append, replace
                                       the base string with or renumber
                                       template*/
};
typedef struct UF_CLONE_name_rule_def_s UF_CLONE_name_rule_def_t,
               *UF_CLONE_name_rule_def_p_t;

/************************************************************************
This routine sets the name rule for the clone operation. If a previously
existing name rule has already been applied to any parts (via apply_defaults
or setting exceptions) then the new name rule will be applied to those parts;
any name rule applications which fail wil be reported via the name rule
failures argument and UF_CLONE_err_naming_failures will be returned

Environment : Internal  and  External
See Also: UF_CLONE_name_rule_def_t
          UF_CLONE_naming_failures_t
          UF_CLONE_name_rule_type_t
          UF_CLONE_init_naming_failures
History : Originally released in V16.0
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_set_name_rule
(
    UF_CLONE_name_rule_def_p_t    name_rule,      /* <I>
                                                     structure describing a
                                                     name rule
                                                  */
    UF_CLONE_naming_failures_p_t  naming_failures /* <I/O>
                                                     naming failures if any
                                                  */
);

/************************************************************************
This routine adds an assembly to the current clone operation. Any load errors
will be placed in the load_status output argument. Possible errors that will
be recorded here are
UF_CLONE_err_bvr_out_of_sync - meaning that the BVR has been
modified in NX Manager since the part was last saved, and
UF_CLONE_err_comp_not_found, meaning a component could not be
found using the current load options.

Environment : Internal  and  External
See Also:
History : Originally released in V16.0
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_add_assembly
(
   const char * part_name, /* <I>
                              The name of the top-level assembly file to add;
                              for native, or import, an O/S filename; in
                              NX Manager or for export, a CLI name
                           */
   UF_PART_load_status_p_t load_status /* <OF>
                                          The load status for the initialisation
                                          operation
                                       */

); /* <NEC> */

/************************************************************************
This routine adds a part to an initialised clone operation. If the part is an
assembly part, any components of the assembly not already a part of the clone
operation will be added as name only references

Environment : Internal  and  External
See Also:
History : Originally released in V16.0
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_add_part
(
   const char * part_name /* <I>
                             The name of the part file to add; for native, or
                             import, an O/S filename, in NX Manager or for
                             export, a CLI name
                          */
);


/************************************************************************
This routine initialises an iteration over the parts currently in the clone
operation. While an iteration is in progress, parts or assemblies should not
be added to the clone operation, or the iterator's behaviour is undefined,
functions which may add parts to the operation will therefore return
UF_CLONE_err_iterator_active.

Environment : Internal  and  External
See Also: UF_CLONE_stop_iteration
            UF_CLONE_iterate
History : Originally released in V16.0
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_start_iteration(void);

/************************************************************************
This routine returns the name of the next part in an iteration, or NULL if
there are no more. If the end of the iteration is reached, the iteration will
have been terminated. To terminate an iteration before reaching the end, call
UF_CLONE_stop_iteration()

Environment : Internal  and  External
See Also: UF_CLONE_start_iteration
           UF_CLONE_stop_iteration
History : Originally released in V16.0
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_iterate
(
    char ** part_name /* <OF>
                         The name of a part in the current clone operation;
                         for native, or import, an O/S filename; in NX Manager
                         or for export, a CLI name
                      */
);

/************************************************************************
This routine stops an iteration. It is only necessary to call this routine if
an iteration is to be stopped before all parts have been iterated over

Environment : Internal  and  External
See Also: UF_CLONE_start_iteration
           UF_CLONE_iterate
History : Originally released in V16.0
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_stop_iteration(void);


/************************************************************************
This routine returns the class of the current clone operation

Environment : Internal  and  External
See Also: UF_CLONE_operation_class_t
History : Originally released in V16.0
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_ask_operation_class
(
    UF_CLONE_operation_class_p_t operation_class /* <O>
                                                  the class of the current clone
                                                  operation
                                                 */
);

/************************************************************************
This routine sets the default naming technique for the current clone operation.
See UF_CLONE_ask_def_naming for details of how this will be applied.

Environment : Internal  and  External
See Also: UF_CLONE_ask_def_naming
           UF_CLONE_set_naming
           UF_CLONE_ask_naming
History : Originally released in V16.0
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_set_def_naming
(
    UF_CLONE_naming_technique_t naming_technique /* <I>
                                                    any naming_technique except
                                                    UF_CLONE_default_naming
                                                 */
);

/************************************************************************
This routine returns the default naming technique of the current clone
operation. This is the naming technique that will be applied during an
apply_defaults operation to all parts which have the naming type
UF_CLONE_default_naming.

Environment : Internal  and  External
See Also: UF_CLONE_naming_technique_t
           UF_CLONE_set_def_naming
           UF_CLONE_apply_defaults
History :  Originally released in V16.0
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_ask_def_naming
(
    UF_CLONE_naming_technique_t *naming /* <O>
                                           the default naming technique of the
                                           current clone operation
                                        */
);

/************************************************************************
This routine sets the naming technique to be applied to the specified part
in the current clone operation. If the naming technique is UF_CLONE_user_name,
then an output part name (the user name) must also be supplied, otherwise
this argument should be NULL;

Environment : Internal  and  External
See Also:
History : Originally released in V16.0
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_set_naming
(
        const char                  *input_part_name,/* <I>
                                                         part name of part in
                                                         the current cloning
                                                         operation, in
                                                         NX Manager clone, or
                                                         for an export operation
                                                         , this should be an encoded
                                                         name, otherwise a
                                                         native O/S file name
                                                      */
        UF_CLONE_naming_technique_t naming_technique,/* <I>
                                                         naming technique to be
                                                         assigned to the
                                                         specified part
                                                      */
        const char                 *output_part_name /* <I>
                                                         output part name to be
                                                         set if naming_technique
                                                         is UF_CLONE_user_name,
                                                         otherwise NULL.
                                                         In NX Manager clone,
                                                         or for an import
                                                         operation, this
                                                         should be an encoded name,
                                                         otherwise a native O/S
                                                         file name
                                                      */
);

/************************************************************************
This routine returns the naming technique currently specified for the
specified part in the current clone operation. If the naming technique has
already been applied (by calling UF_CLONE_set_naming, or
UF_CLONE_apply_defaults) then the output name currently applied wil be
returned in the output_part_spec argument. If the naming technique has not
been applied, then an empty string will be returned in the output_part_spec

Environment : Internal  and  External
See Also: UF_CLONE_set_naming
           UF_CLONE_apply_defaults
           UF_CLONE_naming_technique_t
History : Originally released in V16.0
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_ask_naming
(
        const char                   *input_part_name, /* <I>
                                                         part name of part in
                                                         the current cloning
                                                         operation,
                                                         in NX Manager clone, or
                                                         for an export operation
                                                         , this should be a CLI
                                                         name, otherwise a
                                                         native O/S file name
                                                      */
        UF_CLONE_naming_technique_t *naming_technique,/* <O>
                                                         naming technique
                                                         currently assigned to
                                                         the specified part
                                                      */
        char                       **output_part_spec /* <OF>
                                                         output part name if set
                                                         otherwise NULL returned
                                                         in NX Manager clone, or
                                                         for an import operation
                                                         , this will be a CLI
                                                         name, otherwise a
                                                         native O/S file name
                                                      */
);

/************************************************************************
This routine sets the default action for the current clone operation, an
action inappropriate to the current operation will return an error.
UF_CLONE_replace may not be used as a default action.

Environment : Internal  and  External
See Also: UF_CLONE_set_action
 UF_CLONE_action_t
History : Originally released in V16.0
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_set_def_action
(
    UF_CLONE_action_t action /* <I>
                                any action except UF_CLONE_default_action and
                                UF_CLONE_replace
                             */
);

/************************************************************************
This routine returns the default action for the current clone operation

Environment : Internal  and  External
See Also: UF_CLONE_action_t
History : Originally released in V16.0
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_ask_def_action
(
    UF_CLONE_action_t *action /* <O>
                                 default action for the current clone
                              */
);

/************************************************************************
This routine sets the action for the specified part to be the given action.
In a clone operation this may result in this action being cascaded to parent
parts (if it is a clone action) or child parts (if it is a retain action)
whose action is currently UF_CLONE_default_action. (See the section
"resolving conflicts" in the "Cloning Assemblies" chapter of the Assemblies
User Manual for details of this behaviour.)

If the action being applied is UF_CLONE_replace, you must specify the name of
the replacement part, otherwise this argument should be null.

Environment : Internal  and  External
See Also: UF_CLONE_set_def_action
History : Originally released in V16.0
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_set_action
(
        const char * input_part_name,        /* <I>
                                                name of the part for which the
                                                action is to be set,
                                                in NX Manager or for export a
                                                CLI form name, otherwise a
                                                native file name
                                             */

        UF_CLONE_action_t action_type, /* <I>
                                         action to be applied
                                      */
        const char *replacement_part        /* <I>
                                               name of the replacement part if
                                               action is UF_CLONE_replace,
                                               otherwise null in NX Manager or
                                               for export a CLI form name,
                                               otherwise a native file name
                                            */
);

/************************************************************************
This routine returns the action which has been applied to the specified
component in the current clone operation.

Environment : Internal  and  External
See Also: UF_CLONE_action_t
History : Originally released in V16.0
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_ask_action
(
        const char        *input_part_name, /* <I>
                                              name of the part for which the
                                              action is to be returned,
                                              in NX Manager or for export a CLI
                                              form name, otherwise a native file
                                              name
                                           */
        UF_CLONE_action_t *action_type     /* <O>
                                              the action currently applied to
                                              this part
                                           */
);


/************************************************************************
This routine sets the default name which will be applied during the import
operation. See UF_CLONE_ask_def_pdm_name for details of how this will be
applied.

Environment : Internal  and  External
See Also: UF_CLONE_ask_def_pdm_name
           UF_CLONE_ask_pdm_name
           UF_CLONE_set_pdm_name
History : Originally released in V16.0
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_set_def_pdm_name
(
    const char *pdm_name /* <I>
                            the name to be applied
                         */
);

/*************************************************************************
This routine returns a string containing the default PDM name which will be
applied during the import operation. This name will be applied to newly
created Items, ItemRevisions or Datasets for which the part being imported
has not had its description set by some other method (such as by having a
user name applied, or via a convert callback

This setting is ignored for export operations (where it is irrelevant), and
for clone operations (where the name of the source part will be used if none
has been otherwise set). However it will be recorded in the clone log-file.

Environment : Internal  and  External
See Also: UF_CLONE_convert_cb_t
           UF_CLONE_set_def_pdm_name
History : Originally released in V16.0
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_ask_def_pdm_name
(
    char  **pdm_name /*  <OF>
                        string containing the default PDM name for this
                        import operation
                     */
);

/************************************************************************
This routine sets the PDM name to be applied to the specified part in the
current operation.

Environment : Internal  and  External
See Also: UF_CLONE_ask_pdm_name
           UF_CLONE_set_def_pdm_name
           UF_CLONE_ask_def_pdm_name
History : Originally released in V16.0
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_set_pdm_name
(
        const char *input_part_name,  /* <I>
                                         The name of a part in the current clone
                                         operation; for  import, an O/S
                                         filename; in NX Manager or for export,
                                         a CLI name
                                      */
        const char *pdm_name          /* <I>
                                         the name to be applied or the empty
                                         string
                                      */
);

/************************************************************************
This routine returns the PDM name that has been set for this part, or the
empty string if none has been supplied in which case the default description
will be used

Environment : Internal  and  External
See Also: UF_CLONE_set_def_pdm_name
           UF_CLONE_convert_cb_t
History : Originally released in V16.0
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_ask_pdm_name
(
        const char  *input_part_name,/* <I>
                                        The name of a part in the current clone
                                        operation; for  import,
                                        an O/S filename; in NX Manager or for
                                        export, a CLI name
                                     */
        char **pdm_name        /* <OF>
                                   the name which will be applied or the empty
                                   string
                                */
);
/************************************************************************
This routine sets the default description which will be applied during the
import operation. This description will be applied to newly created Items
and ItemRevisions for which the part being imported has not had its
description set by some other method (such as by having a user name applied,
or via a convert callback).

Environment : Internal  and  External
See Also: UF_CLONE_ask_def_pdm_desc
           UF_CLONE_ask_pdm_desc
           UF_CLONE_set_pdm_desc
History : Originally released in V16.0
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_set_def_pdm_desc
(
    const char *pdm_desc /* <I>
                            description to be applied by default
                         */
);

/*************************************************************************
This routine returns a string containing the default description which will be
applied during the import operation. This description will be applied to newly
created Items and ItemRevisions for which the part being imported has not had
its description set by some other method (such as by having a user name applied,
or via a convert callback).

This setting is ignored for export operations (where it is irrelevant), and for
clone operations (where the description of the source part will be used if
none has been otherwise set).
However it will be recorded in the clone log-file.

Environment : Internal  and  External
See Also: UF_CLONE_convert_cb_t
           UF_CLONE_set_def_pdm_desc
History : Originally released in V16.0
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_ask_def_pdm_desc
(
    char  **pdm_desc /* <OF>
                        string containing the default PDM description for this
                        import operation
                     */
);

/************************************************************************
This routine sets the PDM description to be applied to the specified part in
the current operation.

Environment : Internal  and  External
See Also: UF_CLONE_ask_pdm_desc
           UF_CLONE_set_def_pdm_desc
           UF_CLONE_ask_def_pdm_desc
History : Originally released in V16.0
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_set_pdm_desc
(
        const char *input_part_name,  /* <I>
                                         The name of a part in the current clone
                                         operation; for  import,
                                         an O/S filename; in NX Manager or for
                                         export, a CLI name
                                      */
        const char *pdm_desc          /* <I>
                                         the description to be applied
                                      */
);

/************************************************************************
This routine returns the PDM description that has been set for this part, or
the empty string if none has been supplied in which case the default
description will be used

Environment : Internal  and  External
See Also: UF_CLONE_set_def_pdm_desc
           UF_CLONE_convert_cb_t
History : Originally released in V16.0
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_ask_pdm_desc
(
        const char  *input_part_name,  /* <I>
                                          The name of a part in the current
                                          clone operation; for  import,
                                          an O/S filename; in NX Manager or for
                                          export, a CLI name
                                       */
        char **pdm_desc         /* <OF>
                                   the description which will be applied or the
                                   empty string
                                */
);

/************************************************************************
This routine sets the default PDM item type that will be used in this import
operation. See UF_CLONE_ask_item_type for details of how this will be applied

Environment : Internal  and  External
See Also: UF_CLONE_ask_def_item_type
           UF_CLONE_set_item_type
           UF_CLONE_ask_item_type
History : Originally released in V16.0
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_set_def_item_type
(
    const char *item_type /* <I>
                             item type to be used by default
                          */
);

/************************************************************************
This routine returns the default item type that will be used in this import
operation. This item type will be applied to newly created Items, ItemRevisions
 or Datasets for which the part being imported has not had its item type set
by some other method (such as by having a user name applied, or via a convert
callback)

This setting is ignored for export operations (where it is irrelevant), and
for clone operations (where the type of the source part will be used if none
has been otherwise set). However it will be recorded in the clone log-file.


Environment : Internal  and  External
See Also: UF_CLONE_set_item_type
           UF_CLONE_set_def_item_type
History : Originally released in V16.0
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_ask_def_item_type
(
    char  **item_type /* <OF>
                         string containing the default item type for this
                         import operation
                     */
);

/************************************************************************
This routine sets the item type to be used for this part in the current
operation. See UF_CLONE_ask_item_type for details of how this will be applied

Environment : Internal  and  External
See Also: UF_CLONE_ask_item_type
           UF_CLONE_set_def_item_type
           UF_CLONE_ask_def_item_type
    UF_CLONE_convert_cb_t
History : Originally released in V16.0
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_set_item_type
(
        const char *input_part_name, /* <I>
                                        The name of a part in the current clone
                                        operation; for  import, an O/S filename;
                                        in NX Manager or for export, a CLI name
                                     */
        const char *item_type        /* <I>
                                        The item type that should be applied to
                                        the part
                                     */

);

/************************************************************************
This routine returns the item type that has been set for this part in the
current operation. It may be the empty string, in which case the default
behaviour will be applied. No attempt is made to verify that the item type
exists in the database, if it does not, then again the default behaviour will
be applied.

See UF_CLONE_ask_def_item_type for a description of the default behaviour.

Environment : Internal  and  External
See Also: UF_CLONE_set_item_type
           UF_CLONE_set_def_item_type
           UF_CLONE_ask_def_item_type
    UF_CLONE_convert_cb_t
History : Originally released in V16.0
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_ask_item_type
(
        const char  *input_part_name, /* <I>
                                         The name of a part in the current clone
                                         operation; for import, an O/S filename;
                                         in NX Manager or for export, a CLI name
                                      */
        char **item_type       /* <OF>
                                  The item type that has been applied to the
                                  part
                               */
);

/************************************************************************
This routine sets the default owner that will be applied to Items,
ItemRevisions and Datasets created during this operation. If this is the empty
string, then the user under which the executing user is logged in will be used.

Environment : Internal  and  External
See Also: UF_CLONE_ask_def_owner
History : Originally released in V16.0
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_set_def_owner
(
    const char *owner /* <I>
                         default owner that will be assigned to Items,
                         ItemRevisions and Datasets created during this
                         operation
                      */
);

/************************************************************************
This routine returns the default owner that will be applied to Items,
ItemRevisions and Datasets created during this operation. If this is the empty
string, then the user under which the executing user is logged in will be used.

Environment : Internal  and  External
See Also: UF_CLONE_set_def_owner
History : Originally released in V16.0
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_ask_def_owner
(
    char  **owner /* <OF>
                     default owner that will be assigned to Items, ItemRevisions
                     and Datasets created during this operation
                  */
);

/************************************************************************
This routine sets the owner that will be applied to the Item, ItemRevision and
Dataset created if needed for this part in this operation. If this is the
empty string, then the owner under which the executing user is logged in will
be used. If the Item, Itemrevision or dataset already exist then they will not
be affected.


Environment : Internal  and  External
See Also: UF_CLONE_ask_def_group
History : Originally released in V16.0
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_set_owner
(
        const char *input_part_name,/*<I>
                                      The name of a part in the current clone
                                      operation; for  import, an O/S filename;
                                      in NX Manager or for export, a CLI name
                                   */
        const char *owner          /* <I>
                                      the owner to be used when creating PDM
                                      data for this part
                                   */
);

/************************************************************************
This routine returns the owner that will be applied to the Item, ItemRevision
and Dataset created if needed for this part in this operation. If this is the
empty string, then the owner under which the executing user is logged in will
be used. If the Item, Itemrevision or dataset already exist then they will
not be affected.

Environment : Internal  and  External
See Also: UF_CLONE_ask_def_group
History : Originally released in V16.0
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_ask_owner
(
        const char  *input_part_name,/*<I>
                                The name of a part in the current clone
                                operation; for  import, an O/S filename; in
                                NX Manager or for export, a CLI name
                             */
        char **owner           /*<OF>
                                the owner that will be used when creating PDM
                                data for this part, or the empty string
                               */
);

/************************************************************************
This routine sets the default group that will be applied to Items,
ItemRevisions and Datasets created during this operation. If this is the empty
string, then the group under which the executing user is logged in will be used.

Environment : Internal  and  External
See Also: UF_CLONE_ask_def_group
History : Originally released in V16.0
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_set_def_group
(
    const char *group /* <I>
                         the group ownership which will be assigned by default
                         to Items, ItemRevisions and datasets created by this
                         clone operation
                      */
);

/************************************************************************
This routine returns the default group that will be applied to Items,
ItemRevisions and Datasets created during this operation. If this is the empty
string, then the group under which the executing user is logged in will be used.

Environment : Internal  and  External
See Also: UF_CLONE_set_def_group
History : Originally released in V16.0
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_ask_def_group
(
    char  **group /* <OF>
                     the group ownership which will be assigned by default to
                     Items, ItemRevisions and datasets created by this clone
                     operation
                  */
);

/************************************************************************
This routine sets the group that will be applied to the Item, ItemRevision and
Dataset created if needed for this part in this operation. If this is the empty
string, then the group under which the executing user is logged in will be used.
If the Item, Itemrevision or dataset already exist then they will not be
affected.

Environment : Internal  and  External
See Also: UF_CLONE_ask_def_group
History : Originally released in V16.0
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_set_group
(
        const char *input_part_name,   /* <I>
                                          The name of a part in the current
                                          clone operation; for import,
                                          an O/S filename; in NX Manager or for
                                          export, a CLI name
                                       */
        const char *group              /* <I>
                                          the group ownership which will be
                                          assigned to Items, ItemRevisions and
                                          datasets created for this part
                                       */
);

/************************************************************************
This routine returns the group that will be applied to the Item, ItemRevision
and Dataset created if needed for this part in this operation. If this is the
empty string, then the group under which the executing user is logged in will
be used. If the Item, Itemrevision or dataset already exist then they will not
be affected.


Environment : Internal  and  External
See Also: UF_CLONE_ask_def_group
History : Originally released in V16.0
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_ask_group
(
        const char  *input_part_name, /*<I>
                                        The name of a part in the current clone
                                        operation; for import,
                                        an O/S filename; in NX Manager or for
                                        export, a CLI name
                                     */
        char **group           /*<OF>
                                 the group ownership which will be assigned to
                                 Items, ItemRevisions and datasets created for
                                 this part, or the empty string
                              */
);

/************************************************************************
This routine sets the root directory below which part specific associated file
directories will be placed (for export) or lookd for (for import)

Environment : Internal  and  External
See Also: UF_CLONE_ask_assoc_file_root_dir
History : Originally released in V16.0
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_set_assoc_file_root_dir
(
    const char  *root_directory /* <I>
                             root directory to be used, a native file
                             specification
                          */
);

/************************************************************************
This routine returns the root directory below which part specific associated
file directories will be placed (for export) or looked for (for import)

If this option has not been set, the empty string will be returned

Environment : Internal  and  External
See Also: UF_CLONE_set_assoc_file_root_dir
History : Originally released in V16.0
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_ask_assoc_file_root_dir
(
    char **root_directory /* <OF>
                             the root directory which will be used, or the
                             empty string
                          */
);

/************************************************************************
This routine sets the directory in which associated files for the specified
part will be placed, if relative, then relative to the associated file root
directory

Environment : Internal  and  External
See Also: UF_CLONE_set_assoc_file_root_dir
           UF_CLONE_ask_assoc_file_root_dir
           UF_CLONE_ask_asso_file_dir
History : Originally released in V16.0
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_set_assoc_file_dir
(
    const char *input_part_name, /*<I>
                                   The name of a part in the current clone
                                   operation; for import,
                                   an O/S filename; for export, a CLI name
                               */
    const char *assoc_file_dir   /*<I>
                                   directory to be used, a native file
                                   specification, relative or absolute
                                */
);
/************************************************************************
This routine returns the directory in which associated files for
the specified part will be placed, if relative, then relative to
the associated file root directory

Environment : Internal  and  External
See Also: UF_CLONE_set_assoc_file_root_dir
           UF_CLONE_ask_assoc_file_root_dir
           UF_CLONE_set_assoc_file_dir
History : Originally released in V16.0
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_ask_assoc_file_dir
(
    const char  *input_part_name, /*<I>
                                    The name of a part in the current clone
                                    operation; for import,
                                    an O/S filename; for export, a CLI name
                                 */
    char **assoc_file_dir   /*<OF>
                             directory to be used, a native file specification,
                             relative or absolute, or the empty string
                          */
);

/* structure defining a checkout operation. This structure can be
   either an input argument (to a _set_ function) or an output argument
   (to an _ask_ function
 */
struct UF_CLONE_checkout_data_s
{
    logical checkout; /* <O> if structure being returned
                         true if the part is to be checked out */
    char *comment; /* <OF> if structure being returned
                      comment string, ignored if flag is false */


} ;
typedef struct UF_CLONE_checkout_data_s UF_CLONE_checkout_data_t,
               *UF_CLONE_checkout_data_p_t;

/************************************************************************
This routine sets the default checkout options to be used for the current
export operation.

Environment : Internal  and  External
See Also: UF_CLONE_ask_def_co
           UF_CLONE_ask_co
           UF_CLONE_set_co
           UF_CLONE_checkout_data_t
History : Originally released in V16.0
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_set_def_co
(
    UF_CLONE_checkout_data_p_t checkout_data /* <I>
                                                checkout options to be applied
                                             */
);

/************************************************************************
This routine returns the default checkout options to be used for the current
export operation.

Environment : Internal  and  External
See Also: UF_CLONE_set_def_co
           UF_CLONE_ask_co
           UF_CLONE_set_co
           UF_CLONE_checkout_data_t
History : Originally released in V16.0
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_ask_def_co
(
    UF_CLONE_checkout_data_p_t *checkout_data /* <OF>
                                                checkout options which will be
                                                applied or NULL if none have
                                                been set
                                             */
);

/************************************************************************
This routine sets the checkout options to be used for the
specified part in the current export operation.

Environment : Internal  and  External
See Also: UF_CLONE_set_def_co
           UF_CLONE_ask_def_co
           UF_CLONE_ask_co
           UF_CLONE_checkout_data_t
History : Originally released in V16.0
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_set_co
(
    const char                 *input_part_name,/*<I>
                                                  The name of the part in the
                                                  current export operation, a
                                                  CLI name
                                               */
    UF_CLONE_checkout_data_p_t checkout_data   /*<I>
                                                 checkout options to be applied
                                              */
);

/************************************************************************
This routine sets the comment checking behaviour on checkin for the
specified part.

Return:
     Return Code:
             =0: success
             >0: failure code

Environment: Internal or External
History: Originally released in v19.0
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_set_ci_comment_checking



(
    const char *input_part_name,              /*<I>
                                                The name of the part in the
                                                current export operation, a
                                                CLI name
                                             */
    logical     error_unless_comments_match, /* <I>
                                                Whether to report an error if the checkout comment
                                                does not match the given comment*/
    const char *comment                      /* <I> string containing the comment to be checked */
);

/************************************************************************
This routine sets the default comment checking behaviour on checkin for the
import operation

Return:
     Return Code:
             =0: success
             >0: failure code

Environment: Internal or External
History: Originally released in v19.0
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_set_def_ci_comment_checking



(
    logical     error_unless_comments_match, /* <I>
                                                Whether to report an error if the checkout comment
                                                does not match the given comment*/
    const char *comment                      /* <I> string containing the comment to be checked */
);

/************************************************************************
This routine returns the comment checking behaviour on checkin for the
specified part.

Return:
     Return Code:
             =0: success
             >0: failure code

Environment: Internal or External
History: Originally released in v19.0
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_ask_ci_comment_checking



(
    const char  *input_part_name,             /*<I>
                                                 The name of the part in the
                                                 current export operation, a
                                                 CLI name
                                              */
    logical     *error_unless_comments_match, /* <O>
                                                 Whether to report an error if the checkout comment
                                                 does not match the given comment*/
    char **comment                            /* <OF> string containing the comment to be checked */
);

/************************************************************************
This routine sets the default comment checking behaviour on checkin for the
import operation

Return:
     Return Code:
             =0: success
             >0: failure code

Environment: Internal or External
History: Originally released in v19.0
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_ask_def_ci_comment_checking



(
    logical     *error_unless_comments_match, /* <O>
                                                Whether to report an error if the checkout comment
                                                does not match the given comment*/
    char **comment                            /* <OF> string containing the comment to be checked */
);

/************************************************************************
This routine returns the checkout options to be used for the specified part in
the current export operation.

Return :
     Return code :
     = 0 : successful
     = not 0: Error code, use UF_get_fail_message to obtain message string

Environment : Internal  and  External
See Also: UF_CLONE_set_def_co
           UF_CLONE_ask_def_co
           UF_CLONE_set_co
           UF_CLONE_checkout_data_t
History : Originally released in V16.0
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_ask_co
(
    const char                 *input_part_name,/*<I>
                                                  The name of the part in the
                                                  current export operation, a
                                                  CLI name
                                               */
    UF_CLONE_checkout_data_p_t *checkout_data /* <OF>
                                                 checkout options which will be
                                                 applied or NULL if none have
                                                 been set
                                             */
);

/* structure defining checkin data */
struct UF_CLONE_checkin_data_s
{
    logical checkin; /* true if the part is to be checked out */
    logical error_if_no_co; /* true if it is an error for the part not be be
                               checked out */

};
typedef struct UF_CLONE_checkin_data_s
               UF_CLONE_checkin_data_t, *UF_CLONE_checkin_data_p_t;

/************************************************************************
This routine sets the default checkin options to be used in the
current export operation.

Environment : Internal  and  External
See Also: UF_CLONE_ask_def_ci
           UF_CLONE_set_ci
           UF_CLONE_ask_ci
History : Originally released in V16.0
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_set_def_ci
(
    UF_CLONE_checkin_data_p_t checkin_data /* <I>
                                              checkin options to be applied
                                           */
);

/************************************************************************
This routine asks the default checkin options to be used in the
current import operation.

Environment : Internal  and  External
See Also: UF_CLONE_set_def_ci
           UF_CLONE_set_ci
           UF_CLONE_ask_ci
History : Originally released in V16.0
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_ask_def_ci
(
    UF_CLONE_checkin_data_p_t *checkin_data /* <OF>
                                              checkin options which will be
                                              applied, or null if non have been
                                              set
                                           */
);

/************************************************************************
This routine sets the checkin options to be used for the
specified part in the current import operation.


Environment : Internal  and  External
See Also: UF_CLONE_ask_def_ci
           UF_CLONE_set_def_ci
           UF_CLONE_ask_ci
History : Originally released in V16.0
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_set_ci
(
    const char                 *input_part_name,   /*<I>
                                                     the name of a part in the
                                                     current import operation, a
                                                     native O/S filename
                                                  */
    UF_CLONE_checkin_data_p_t checkin_data /* <I>
                                              the checkin options to be applied
                                           */
);

/************************************************************************
This routine asks the checkin options to be used for the
specified part in the current import operation.

Environment : Internal  and  External
See Also: UF_CLONE_ask_def_ci
           UF_CLONE_set_def_ci
           UF_CLONE_set_ci
History : Originally released in V16.0
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_ask_ci
(
    const char                 *input_part_name,  /*<I>
                                                     the name of a part in the
                                                     current import operation, a
                                                     native O/S filename
                                                 */
    UF_CLONE_checkin_data_p_t *checkin_data        /* <OF>
                                                     the checkin options which
                                                     will be applied or null if
                                                     none have been set
                                                  */
);

/* enumeration describing the state of a part in the current clone
   operation */
enum UF_CLONE_part_state_s
{
    UF_CLONE_present_state,          /* a normal part occurrence in a clone */
    UF_CLONE_lost_state,             /* should be a part occurence, but the part
                                        cannot be found */
    UF_CLONE_nonmaster_state,        /* A non-master of a part in the clone
                                        operation */
    UF_CLONE_refnonmaster_state,     /* a non-master which is also an occurrence
                                        in an assembly int the clone
                                        operation */
    UF_CLONE_name_only_state         /* a part name referenced by a part in the
                                        operation, but not present itself */
} ;
typedef enum UF_CLONE_part_state_s UF_CLONE_part_state_t,
             *UF_CLONE_part_state_p_t;

/************************************************************************
This routine returns the state of the specified part in the
current clone operation.

Environment : Internal  and  External
See Also: UF_CLONE_part_state_t
History : Originally released in V16.0
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_ask_part_state
(
    const char *input_part_name, /* <I>
                                    The name of a part in the current clone
                                    operation; for native, or import,
                                    an O/S filename; in NX Manager or for
                                    export, a CLI name
                                 */
    UF_CLONE_part_state_p_t state /* <O>
                                     the part's state
                                  */
);

/************************************************************************
This routine returns an array of attributes for specified part from
the current clone operation

Environment : Internal  and  External
See Also :
History : Originally released in NX6.0
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_ask_part_attrs
(
    const char *part_name, /* <I>
                              The name of a part in the current clone operation;
                              for native, or import, an O/S filename; in
                              NX Manager or for export, a CLI name
                           */
    int        *n_attributes,    /* <O>
                                    the number of attributes returned
                                 */
    UF_ATTR_part_attr_p_t *attributes /* <OF, len:n_attributes> 
                                      Allocated array of structures holding
                                      attribute titles and values.  This must
                                      be freed by the caller using UF_free.
                                      */
);

/************************************************************************
This routine returns a logical indicating whether the part in question is
lacking necessary information. After a successful call to
UF_CLONE_apply_defaults this should be true for no parts in the operation.

It should not be necessary to call this function during an
operation, but it might be useful in order to give feedback to the
user, for example a notify callback registered against
UF_CLONE_beg_apply_defs_cb might iterate the parts in the clone
calling this function in order to count those parts which need
defaults applying, (since defaults application can take some time
for a NX Manager clone or import, where accesses to the database are
required to fill in values)

Environment : Internal  and  External
See Also:
History : Originally released in V16.0
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_part_under_specified
(
    const char *part_name, /* <I>
                              name of component */
    logical *is_under_specified /* <O>
                                   true if node is underspecified, false
                                   otherwise */
);


/************************************************************************
This routine calls the report callbacks for each part in the
clone operation, possibly multiple times, as follows:

call the begin occurrences report callback.

For each root part, call the report callback pre-order depth
first on the components

call the begin non-occurrences report callback

Then call the report callback for name-only references, and
non-masters that have assigned output names, in an undefined
order

call the end report callback.

For Interactive NX a default callback is registered for
these to generate a report to the listing window. For
non-interactive NX no default callback is registered.

Environment : Internal  and  External
See Also:
History : Originally released in V16.0
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_generate_report(void);

/************************************************************************
This routine performs the clone, if necessary completing defaults application
first. Defaults application may generate naming rule failures, in which case
the clone will not be performed, the failures reported through the
naming_failures argument, and UF_CLONE_err_naming_failures will be returned

Environment : Internal  and  External
See Also: UF_CLONE_naming_failures_t
           UF_CLONE_init_naming_failures
History : Originally released in V16.0
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_perform_clone
(
    UF_CLONE_naming_failures_p_t naming_failures /* <I/O>
                                                    naming failures if any
                                                 */
);


/************************************************************************
This routine applies default values to all parts in the clone
operation without performing the clone. Defaults application
may generate naming rule failures. In this case the clone will
not be performed, the return code will be
UF_CLONE_err_naming_failures and the
naming_failures argument will be filled in with:
   a count of the number of errors (n_failures)
   an array of error codes (statuses) which must be freed
   an array of input names (input_names) which must be freed
             with UF_FREE_string_array
   an array of output_names (output_names), entries may be
             null, must be freed with UF_FREE_string_array

     The  function UF_CLONE_init_naming_failures should be used to
     initialise the naming_failures structure before it is passed to
     this function.

Return :
     Return code :
     = 0 : successful
     UF_CLONE_err_naming_failures: naming failures occurred,
             details reported in the naming_failures output
             argument
     = not 0: Error code, use UF_get_fail_message to obtain message string

Environment : Internal  and  External
See Also: UF_CLONE_naming_failures_t
           UF_CLONE_init_naming_failures
History : Originally released in V16.0
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_apply_defaults
(
    UF_CLONE_naming_failures_p_t naming_failures /* <I/O>
                                                    Pointer to a naming failures
                                                    structure.If a naming
                                                    failure occurs the return
                                                    code will be
                                                    UF_CLONE_err_naming_failures
                                                    and this structure will be
                                                    filled in
                                                 */
);

/************************************************************************
This routine removes previously applied defaults, but leaves
exceptions which have been specified intact. Naming failures
may occur if a registered notify callback forbids the
operation.


Environment : Internal  and  External
See Also: UF_CLONE_reset_to_default
           UF_CLONE_naming_failures_t
    UF_CLONE_init_naming_failures
History: Originally released in V16.0
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_unapply_defaults
(
    UF_CLONE_naming_failures_p_t naming_failures /* <I/O>
                                                    Pointer to a naming failures
                                                    structure.  If a naming
                                                    failure occurs the return
                                                    code will be
                                                    UF_CLONE_err_naming_failures
                                                    and this structure will be
                                                    filled in
                                                 */
);

/* Possible return values for a registered notfiy callback.
   Note that the forbid return will always prevent the operation in
   question, but if that operation was incidental to some other operation
   (e.g. assigning a name to a component that has the default action
   causes the assigned action to be fixed at the current value of the
   default action) then the forbid return may not cause an error to be
   returned to the caller, although later operations may fail.
*/
enum UF_CLONE_notify_response_e
{
    UF_CLONE_continue, /* carry on, including calling any further notify
                          callbacks registered at this point */
    UF_CLONE_cut,      /* don't call any further notify callbacks registered at
                          this point, but carry on with the clone operation */
    UF_CLONE_forbid,  /* (only relevant for begin callbacks) forbid the
                         operation in question. Note that a forbid return, will
                         always prevent the operation in question, but if that
                         operation was incidental to some other
                         operation (e.g. assigning a name to a component that
                         has the default action causes the assigned action to
                         be fixed at the current value of the default action)
                         then the forbid return may not cause an error to
                         be returned to the caller
                      */
    UF_CLONE_notify_error       /* the callback has reported an error to the
                                   user, abort the clone operation */
} ;
typedef enum UF_CLONE_notify_response_e UF_CLONE_notify_response_t;

enum UF_CLONE_notify_cb_e
{
    UF_CLONE_initialise_cb,           /* called when a clone operation is
                                         started, extra data is a pointer to a
                                         UF_CLONE_class_t */
    UF_CLONE_terminate_cb,            /* called when a clone  operation is
                                         terminated, extra data is a pointer to
                                         a UF_CLONE_class_t */
    UF_CLONE_beg_assy_load_cb,      /* called when an assembly is to be added to
                                       the clone operation,*/
    UF_CLONE_end_assy_load_cb,        /* data is top level assembly name */
    UF_CLONE_beg_assy_nc_load_cb,    /* called when an assembly just added to
                                        the clone operation,*/
    UF_CLONE_end_assy_nc_load_cb,    /* is about to start having non-component
                                        refs of its components added */
    UF_CLONE_beg_part_load_cb,        /* called when a part is added to the
                                         clone operation, either directly, */
    UF_CLONE_end_part_load_cb,        /* or because the part is a component of
                                         an assembly being added */
    UF_CLONE_beg_part_load_nc_cb,     /* called when non-component references
                                      for a part (if any) are being added to */
    UF_CLONE_end_part_load_nc_cb,     /* the clone operation, data is part name
                                      */
    UF_CLONE_beg_perform_cb,          /* called when the clone operation is
                                         performed, extra data is null */
    UF_CLONE_end_perform_cb,
    UF_CLONE_beg_apply_defs_cb,       /* called when apply defaults is performed
                                      */
    UF_CLONE_end_apply_defs_cb,
    UF_CLONE_beg_set_def_action_cb,   /* called when the default action is set,
                                         data is a pointer to a */
    UF_CLONE_end_set_def_action_cb,   /* UF_CLONE_action_type_t */
    UF_CLONE_beg_set_action_cb,       /* called when the action is set for a
                                         part, data is a pointer to a */
    UF_CLONE_end_set_action_cb,       /* UF_CLONE_action_type_t */
    UF_CLONE_beg_set_name_rule_cb,    /* called when the naming rule is set,
                                         extra data is a pointer to a */
    UF_CLONE_end_set_name_rule_cb,    /* UF_CLONE_name_rule_t */
    UF_CLONE_beg_set_def_naming_cb,   /* called when the default naming
                                         technique is set , data is a pointer
                                         to a*/
    UF_CLONE_end_set_def_naming_cb,   /* UF_CLONE_naming_technique_t */
    UF_CLONE_beg_set_naming_cb,       /* called when the naming technique is set
                                         for a part, data is a pointer to a*/
    UF_CLONE_end_set_naming_cb,       /* UF_CLONE_naming_technique_t */
    UF_CLONE_beg_set_name_cb,         /* called when the name of a part is being
                                         set, extra data is the name */
    UF_CLONE_end_set_name_cb,         /* being applied (a char *) */
    UF_CLONE_beg_set_def_pdm_name_cb, /* called when setting the default pdm
                                         name , extra data is the  */
    UF_CLONE_end_set_def_pdm_name_cb, /* pdm_name being applied (a char *) */
    UF_CLONE_beg_set_pdm_name_cb,     /* called when setting the pdm name of the
                                         part, extra data is the  */
    UF_CLONE_end_set_pdm_name_cb,     /* pdm_name being applied (a char *) */
    UF_CLONE_beg_set_def_item_type_cb, /* called when setting the default
                                          item_type , extra data is the  */
    UF_CLONE_end_set_def_item_type_cb, /* item_type being applied (a char *) */
    UF_CLONE_beg_set_item_type_cb,     /* called when setting the item_type of
                                          the part, extra data is the  */
    UF_CLONE_end_set_item_type_cb,     /* item_type being applied (a char *) */
    UF_CLONE_beg_set_def_pdm_desc_cb, /* called when setting the default pdm
                                         description, extra data is the  */
    UF_CLONE_end_set_def_pdm_desc_cb, /* pdm description being applied
                                         (a char *) */
    UF_CLONE_beg_set_pdm_desc_cb,     /* called when setting the default pdm
                                         description, extra data is the  */
    UF_CLONE_end_set_pdm_desc_cb,     /* pdm description being applied
                                         (a char *) */
    UF_CLONE_beg_set_def_co_cb,       /* called when setting the checkout flag,
                                         extra data is a  */
    UF_CLONE_end_set_def_co_cb,       /* UF_CLONE_checkout_data_p_t  */
    UF_CLONE_beg_set_co_cb,           /* called when the checkout flag is set,
                                         extra data is a  */
    UF_CLONE_end_set_co_cb,           /* UF_CLONE_checkout_data_p_t  */
    UF_CLONE_beg_part_co,             /* called when a part is being checked
                                         out, extra data is null */
    UF_CLONE_end_part_co,
    UF_CLONE_beg_set_def_ci_cb,       /* called when setting the checkin flag,
                                         extra data is a  */
    UF_CLONE_end_set_def_ci_cb,       /* UF_CLONE_checkin_data_p_t  */
    UF_CLONE_beg_set_ci_cb,           /* called when the checkin flag is set,
                                         extra data is a  */
    UF_CLONE_end_set_ci_cb,           /* UF_CLONE_checkin_data_p_t  */
    UF_CLONE_beg_part_ci,             /* called when a part is being checked in,
                                         extra data is null */
    UF_CLONE_end_part_ci,
    UF_CLONE_beg_part_clone_cb,       /* about to actually do the clone
                                         operation on this part */
    UF_CLONE_end_part_clone_cb,       /* completed the clone operation on this
                                         part */
    UF_CLONE_beg_occ_report_cb,       /* called when about to start a report
                                         operation */
    UF_CLONE_beg_nonocc_report_cb,    /* called when a report operation is about
                                         to start non-occ parts */
    UF_CLONE_report_cb,               /* called once for each occurrence and
                                         once for each non component part
                                         in a report. Extra data is: for an
                                         occurrence, a pointer to an int
                                         giving the depth in the assembly
                                         (0 for the root node);
                                         for a non-component part, NULL */
    UF_CLONE_end_report_cb            /* called  when a report finishes */

} ;
typedef enum UF_CLONE_notify_cb_e UF_CLONE_notify_cb_t,
             *UF_CLONE_notify_cb_p_t;

typedef UF_CLONE_notify_response_t (*UF_CLONE_notify_callback_t)
(
    UF_CLONE_notify_cb_t cb, /* <I>
                                callback reason
                             */
    const char * input_part_specifier, /* <I>
                                          The name of a part in the current
                                          clone operation; for import,
                                          an O/S filename; for export, a CLI
                                          name may be null if the cb applies to
                                          a whole clone operation */
    const void* data                  /* <I>
                                         data, e.g. the name of the name about
                                         to be applied, or a pointer to an
                                         action type or a naming type, or a
                                         checkout action/cb pair
                                      */
);


enum UF_CLONE_convert_response_e
{
    UF_CLONE_use_supplied,  /* Use what the called function returned, called
                               function allocates, caller must free */
    UF_CLONE_not_converted, /* keep calling callbacks until one of them
                               responds */
    UF_CLONE_no_conversion, /* not converted, but don't carry on and call
                               further callbacks */
    UF_CLONE_convert_error       /* the callback has reported an error to the
                                    user, abort the clone operation */
} ;
typedef enum UF_CLONE_convert_response_e UF_CLONE_convert_response_t;

enum UF_CLONE_convert_cb_e
{
    UF_CLONE_user_name_convert,              /* called when a part has
                                                USER_NAME naming */
    UF_CLONE_part_type_convert,              /* called when a part needs a type
                                                for the PDM system */
    UF_CLONE_part_name_convert,              /* called when a part needs a pdm
                                                name */
    UF_CLONE_part_desc_convert,              /* called when a part needs a pdm
                                                description */
    UF_CLONE_part_own_user_convert,          /* called when a part needs a pdm
                                                owner user */
    UF_CLONE_part_own_group_convert,         /* called when a part needs a pdm
                                                owner group */
    UF_CLONE_part_checkout_convert,          /* called when a part needs a
                                                checkout comment */
    UF_CLONE_assoc_file_dir_convert            /* called when a part needs an
                                                associated file directory */
} ;
typedef enum UF_CLONE_convert_cb_e UF_CLONE_convert_cb_t,
             *UF_CLONE_convert_cb_p_t;

/* <APB> 11-Jan-1999
  a convert callback, receives the callback being executed and the name
  of the input part, should return the answer as UF_allocate_memory
  allocated space which NX is at liberty to free, if
  UF_CLONE_use_supplied is returned.

*/
typedef UF_CLONE_convert_response_t (*UF_CLONE_convert_callback_t)
(
        UF_CLONE_convert_cb_t cb, /* <I>
                                     the callback reason indicating the answer
                                     needed
                                  */
        const char * input_part_specifier, /* <I>
                                              The name of a part in the current
                                              clone operation for which
                                              the specified answer is required;
                                              for import, an O/S filename;
                                              for export, a CLI name
                                           */
        char ** answer /* <O>
                          space should be allocated with UF_allocate_memory,
                          user must free
                       */
);

/* <nargund> CAE1469  07-Mar-2013
 *  Introduce new option to clone related CAE parts
*/
enum UF_CLONE_clone_rel_cae_e
{
    UF_CLONE_clone_sim_fem_ideal,              /* Clone/Export all related CAE parts to the CAD parts */
    UF_CLONE_clone_fem_ideal,              /* Clone/Export only the Idealized parts and Fems associated  to the CAD parts */
    UF_CLONE_clone_ideal,              /* Clone/Export only the Idealized parts associated  to the CAD parts */
    UF_CLONE_clone_none              /* Clone/Export no CAE parts associated to the CAD parts */
} ;
typedef enum UF_CLONE_clone_rel_cae_e UF_CLONE_clone_rel_cae_t, *UF_CLONE_clone_rel_cae_p_t;
/************************************************************************
This routine registers a callback function to be called at the
notify callback points specified by the cb argument. The name
argument is used to identify the callback for later removal, or
insertion of other callback functions before or after this
function in the callback list. The name should therefore be
unique (for this particular callback point). It is recommended
that the name should be prefixed with a site specific
code. Some callbacks are registered by NX itself, and
the names of these all begin with "UGS". Names are considered
to be case independent- i.e. "UGS NOTIFY" is the same as "UGS
Notify"

If a callback of the same name is already registered at this
call back point, then it will be removed before the function
supplied is registered.

The Clone operation will call these callbacks in the order in
which they are present in the list at the appropriate point in
the clone operation. The callback function should generally
return UF_CLONE_continue. Calling further callbacks in the list
may be prevented by returning UF_CLONE_cut.

Most of the notify callback points have begin and end
callbacks: begin (..._beg_...) callbacks will be called before
an operation is about to be performed, allowing a callback to
check and forbid it, or perform necessary pre-actions; end
callbacks will be called after an operation has completed
succesfully, allowing a callback to perform necessary
post-actions. Note the end callback corresponding to a begin
callback may not be called if the operation in question fails
for some reason.

It is possible to specify that the supplied callback should be
placed before or after another named callback using the
relative_callback and before_relative arguments. If the
specified relative callback is not present, the function will
return the error UF_CLONE_err_no_relative_cb and place the
callback being registered at the beginning or end of the
callback list depending on the value of the before_relative
flag.


Environment : Internal  and  External
See Also: UF_CLONE_notify_response_t
           UF_CLONE_notify_cb_t
           UF_CLONE_ask_ntfy_callbacks
           UF_CLONE_remove_ntfy_callback
History : Originally released in V16.0
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_register_ntfy_callback
(
    UF_CLONE_notify_cb_t cb,              /* <I>
                                             callback point at which to call
                                             function being registered */
    UF_CLONE_notify_callback_t callback,  /* <I>
                                             function pointer of the callback
                                             function */
    const char * name,                          /* <I>
                                                   the name of this callback -
                                                   should be unique to this
                                                   callback point */
    const char * description,                   /* <I>
                                                   A description of the
                                                   callback's function, for
                                                   information only
                                                */
    const char * relative_callback,             /* <I>
                                                   The name of a callback to
                                                   position this one relative
                                                   to, can be NULL, meaning the
                                                   entire list of callbacks at
                                                   this point.
                                                */
    logical before_relative               /* <I>
                                             Whether this callback should be
                                             placed before the relative
                                             callback (if true) or after it
                                             (if false). If the relative
                                             callback is NULL or not present,
                                             true places the new callback at
                                             the beginning of the list, after
                                             at the end
                                          */
);

/************************************************************************
This routine removes the callback of the specified name from
the given callback list and returns a pointer to the function
that was registered under that name.

Environment : Internal  and  External
See Also: UF_CLONE_notify_response_t
           UF_CLONE_notify_cb_t
           UF_CLONE_ask_ntfy_callbacks
           UF_CLONE_register_ntfy_callback
History : Originally released in V16.0
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_remove_ntfy_callback
(
        UF_CLONE_notify_cb_t cb,                      /* <I>
                                                         callback point from
                                                         which to remove
                                                         function
                                                      */
        char * name,                                 /* <I>
                                                        name of callback to
                                                        remove
                                                     */
        UF_CLONE_notify_callback_t *callback_removed /* <O>
                                                        the function that was
                                                        removed, so you can
                                                        reinstall it if desired,
                                                        may be NULL if no
                                                        callback of that name
                                                        was registered at the
                                                        specified callback point
                                                      */
);

/************************************************************************
This routine registers a callback which will be called when the clone operation
needs a string value for a piece of information, for example a user name, an
associated file directory or an item type. The convert callback list will be
called in order before other default behaviours are applied.

If a callback of the same name is already registered at this callback point,
then it will be removed before the function supplied is registered. Names are
case independent.

The relative_callback and before_relative arguments can be used to control
where the supplied callback function is placed in the list.

If the function returns UF_CLONE_use_supplied, then the callback function
should have filled in its answer argument with the needed information. Callback
functions later in the list will not be called.

If the function returns UF_CLONE_not_converted then the next function in the
callback list will be called, until the list runs out, at which point the
default behaviour will be applied

If the function returns UF_CLONE_no_conversion, then no further callback
functions in the list will be called, and the default behaviour will be applied.

Environment : Internal  and  External
See Also: UF_CLONE_remove_cvt_callback
           UF_CLONE_ask_cvt_callbacks
           UF_CLONE_convert_cb_t
History : Originally released in V16.0
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_register_cvt_callback
(
    UF_CLONE_convert_cb_t cb,               /* <I>
                                               callback point at which to call
                                               function being registered
                                            */
    UF_CLONE_convert_callback_t callback,   /* <I>
                                               function pointer of the callback
                                               function
                                            */
    char * name,                            /* <I>
                                               the name of this callback -
                                               should be unique to this callback
                                               point
                                            */
    char * description,                     /* <I>
                                               A description of the callback's
                                               function
                                            */
    char * relative_callback,               /* <I>
                                               The name of a callback to
                                               position this one relative to,
                                               can be NULL, meaning the entire
                                               list of callbacks it this point
                                          */
    logical before_or_after_relative        /* <I>
                                               Whether this callback should be
                                               placed before the relative
                                               callback (if true) or after it
                                               (if false). If the relative
                                               callback is null, true places the
                                               new callback at the beginning
                                               of the list, false at the end
                                            */
);

/************************************************************************
This routine removes the callback of the specified name from the given callback
list and returns a pointer to the function that was registered under that name.

Environment : Internal  and  External
See Also: UF_CLONE_notify_response_t
           UF_CLONE_notify_cb_t
           UF_CLONE_ask_cvt_callbacks
           UF_CLONE_register_cvt_callback
History : Originally released in V16.0
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_remove_cvt_callback
(
        UF_CLONE_convert_cb_t cb, /* <I>
                                     callback point from which to remove
                                     function
                                  */
        const char * name,               /* <I>
                                            name of callback to remove
                                         */
        UF_CLONE_convert_callback_t *callback_removed /* <O>
                                                         the function that was
                                                         removed, so you can
                                                         reinstall it if desired
                                                         may be NULL if no
                                                         callback of that
                                                         name was registered
                                                      */
);

/************************************************************************
This routine returns the currently registered notify callbacks in three
parallel arrays containing the callback points, the names of the callbacks
and the descriptions of the callbacks.

Environment : Internal  and  External
See Also: UF_CLONE_register_ntfy_callback
          UF_CLONE_remove_ntfy_callback
History : Originally released in V16.0
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_ask_ntfy_callbacks
(
    int *n_callbacks,                    /* <O>
                                            number of callbacks registered */
    UF_CLONE_notify_cb_p_t *points,       /* <OF,len:n_callbacks>
                                             callback points */
    char                ***names,        /* <OF,len:n_callbacks> n_callbacks (with UF_free_string_array)
                                            names of callbacks */
    char                ***descriptions  /* <OF,len:n_callbacks> n_callbacks (with UF_free_string_array)
                                            descriptions of callbacks */
);

/************************************************************************
This routine  returns the currently registered convert callbacks in three
parallel arrays containing the callbcack points, the names of the callbacks
and the descriptions of the callbacks

Environment : Internal  and  External
See Also: UF_CLONE_register_cvt_callback
          UF_CLONE_remove_cvt_callback
History : Originally released in V16.0
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_ask_cvt_callbacks
(
    int *n_callbacks,                    /* <O>
                                            number of callbacks registered */
    UF_CLONE_convert_cb_p_t *points,       /* <OF,len:n_callbacks>
                                              callback points */
    char                ***names,        /* <OF,len:n_callbacks> n_callbacks (with UF_free_string_array)
                                            names of callbacks */
    char                ***descriptions  /* <OF,len:n_callbacks> n_callbacks (with UF_free_string_array)
                                            descriptions of callbacks */
);

/************************************************************************
This routine returns the value of the default folder that parts
generated during a NX Manager clone or clone based import will be placed
in.

The folder name will be specified as
<user-name>:[<containing-folder>:...]<folder-name>
e.g. "smith:Imported Parts:machinehead" or "smith:My Parts"

If this option is not set, then the empty string will be returned

Environment : Internal  and  External
See Also: UF_CLONE_set_def_folder
History : Originally released in V16.0
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_ask_def_folder
(
    char **folder_name /* <OF>
                          the default folder parts will be placed in
                       */
);
/************************************************************************
This routine sets the value of the default folder that parts generated during
a NX Manager clone or clone based import will be placed in.

The folder name should be specified as
<user-name>:[<containing-folder>:...]<folder-name>
e.g. "smith:Imported Parts:machinehead" or "smith:My Parts"

If this option is never set, the executing users home
folder will be used.

Environment : Internal  and  External
See Also: UF_CLONE_ask_def_folder
History : Originally released in V16.0
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_set_def_folder
(
    const char *folder_name /* <I>
                               The default folder to place parts in
                            */
);

/************************************************************************
This routine sets the default directory that parts created during a native
clone or a clone based export will be placed in.

If this option is never set then the current directory will be used.
Note that this option is ignored for user name numbering technique.

Environment : Internal  and  External
See Also: UF_CLONE_ask_def_directory
History : Originally released in V16.0
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_set_def_directory
(
    const char * directory_name /* <I>
                                   directory to place created parts in
                                */
);

/************************************************************************
This routine sets the default directory that parts created during a native
clone or a clone based export will be placed in. This routine additionally 
tries to create the specified default directory on the fly if it does not
exist.

If this option is never set then the current directory will be used

Environment : Internal  and  External
See Also: UF_CLONE_ask_def_directory
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_ensure_def_directory
(
    const char * directory_name /* <I>
                                   directory to place created parts in
                                */
);

/************************************************************************
This routine returns the default directory that parts created during a native
clone or a clone based export will be placed in.

If this option is not set then the empty string will be returned
used

Environment : Internal  and  External
See Also: UF_CLONE_set_def_directory
History : Originally released in V16.0
***********************************************************************/
extern UFUNEXPORT int UF_CLONE_ask_def_directory
(
    char ** directory_name /* <OF>
                              directory to place created parts in
                           */
);

/***************************************************************************************************
* This routine sets the propagation behaviour for actions in an export operation (for Clone propagation is always on, and it
* is not relevant to an import operation.
* When propagation is on:
*          specifying an Exclude action for a part will cause all parts
*              it references that are not referenced by other non-excluded
*              parts to also have the Exclude action applied, and so on for their referenced parts
*          specifying an Overwrite or Use Existing action for a part will cause all parts
*              which reference it which currently have an Exclude action applied (directly or by default)
*              to have the same Overwrite or Use Existing action applied to them, and so on for their
*               referencing parts
* Return:
*         Return Code:
*              = 0 : success
*               UF_CLONE_err_invalid_operation : the current operation is not an export operation
*             > 0 : other failure code
*Environment: Internal or external
* See Also: UF_CLONE_set_def_action
*              : UF_CLONE_set_action
*History:
*       Originally released in v19.0
***************************************************************************************************/
extern UFUNEXPORT int UF_CLONE_set_propagate_actions
(
    logical propagate_actions /* <I> whether to propagate actions in this export operation */
);

/***************************************************************************************************
* This routine uses the PLMXML structure specified in "filename" to define
* a selective Clone Export operation. It is mainly intended for use by the
* ug_selective_export utility. It has no meaning for a Clone or Clone
* Import operation.
*
* Environment: Internal and External
* History : Originally released in NX2.0
***************************************************************************************************/

extern UFUNEXPORT int UF_CLONE_apply_selective_export_xml
(
    const char* xml_file, /* <I> */
    UF_PART_load_status_p_t load_status /* <OF>*/
);

/************************************************************************
This routine returns the rev_up flag for the current operation. It has no
meaning outside of the clone import operation.

Environment : Internal  and  External
See Also:
History : Originally released in NX4.0
***********************************************************************/
extern UFUNEXPORT int  UF_CLONE_ask_rev_up
(
    logical *rev_up /* <I> */
);

/************************************************************************
This routine returns the rev_up flag for the current operation. It has no
meaning outside of the clone import operation.

Environment : Internal  and  External
See Also:
History : Originally released in NX4.0
***********************************************************************/
extern UFUNEXPORT int  UF_CLONE_set_rev_up
(
    logical rev_up /* <I> */
);

/************************************************************************
               
This routine returns the attach_log_file flag for the current operation. It has no
meaning outside of the clone import operation.

Environment : Internal  and  External
See Also:
History : Originally released in NX5.1
***********************************************************************/
extern UFUNEXPORT int  UF_CLONE_ask_attach_log_file
(
    logical *attach_log_file /* <I> */
);

/************************************************************************

This routine sets the attach_log_file flag for the current operation.
It has no meaning outside of the clone import operation.

Environment : Internal  and  External
See Also:
History : Originally released in NX5.1
***********************************************************************/
extern UFUNEXPORT int  UF_CLONE_set_attach_log_file
(
    logical attach_log_file /* <I> */
);

/************************************************************************
This routine asks the current boolean option to clone/export the related drawings when cloning any CAD parts
It has no meaning in the Clone Import Operation
Environment : Internal  and  External
See Also:
History : Originally released in NX9.0
***********************************************************************/
extern UFUNEXPORT int  UF_CLONE_ask_clone_related_dwgs
(
    logical* rel_dwgs /* <O> */
);
/************************************************************************
This routine sets the boolean option to clone/export the related drawings when cloning any CAD parts
It has no meaning in the Clone Import Operation
Environment : Internal  and  External
See Also:
History : Originally released in NX9.0
***********************************************************************/
extern UFUNEXPORT int  UF_CLONE_set_clone_related_dwgs
(
    logical rel_dwgs /* <I> */
);

/************************************************************************
This routine asks the option to clone/export the related CAE parts when cloning any CAD parts
It has no meaning in the Clone Import Operation
Environment : Internal  and  External
See Also:
History : Originally released in NX9.0
***********************************************************************/
extern UFUNEXPORT int  UF_CLONE_ask_clone_related_cae
(
    UF_CLONE_clone_rel_cae_p_t rel_cae /* <O> */
);

/************************************************************************
This routine sets the option to clone/export the related CAE parts when cloning any CAD parts
It has no meaning in the Clone Import Operation
Environment : Internal  and  External
See Also:
History : Originally released in NX9.0
***********************************************************************/
extern UFUNEXPORT int  UF_CLONE_set_clone_related_cae
(
    UF_CLONE_clone_rel_cae_t rel_cae /* <I> */
);


#ifdef __cplusplus



}
#endif

#undef EXPORTLIBRARY

#endif /* UF_CLONE_INCLUDED */

