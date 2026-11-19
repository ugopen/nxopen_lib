/*******************************************************************************
             Copyright (c) 1998-2000 Unigraphics Solutions, Inc.
                       Unpublished - All Rights Reserved



File description:
    Open C API interface for interfacing with Design Rules.
    These include Design Rules, Design Rule Functions,
    Design Rule Violations, and Design Rule Violation Overrides.

Overview:
---------
The Rule module within NX provides functions to manage
the association of design rule and design rule violation data with
NX objects.

Concepts and Terminology:
-------------------------
There are four basic objects managed by the Rule module. Design
Rule, Design Rule Function, Design Rule Violation, Design Rule
Violation Override.  The Rule module provides functions for creating
and modifying objects of all these types.

A Design Rule is a simple object which describes a rule and has an
associated function for checking the rule.  The Design Rule is also
used to group Design Rule Violations associated with that Design
Rule.

A Design Rule Function is simply a reference to a subroutine in an
internal Open API image.  A Design Rule Function must be
created before a Design Rule which requires the function.

A Design Rule Violation object tracks objects in violation of a
particular Design Rule.

A Design Rule Violation Override marks a Design Rule Violation as
being acknowledged and ignored by a particular user for a given
reason.  Overrides are generally left to be managed interactively by
the user.
******************************************************************************/

#ifndef UF_RULE_H_INCLUDED
#define UF_RULE_H_INCLUDED

#include <uf_defs.h>
#include <libufun_exports.h>

/***************************************************************************

  ***************************************************************************/

#ifdef __cplusplus
extern "C" {
#endif

#define UF_RULE_CURRENT_TIME_STAMP -1

typedef void *(*UF_RULE_check_function_f_t)( tag_t   rule,/* <I> Rule to check */
                                          void   *data /* <I> Client data */);

/**********************************************************************
Create a Design Rule.

Environment: Internal  and  External

See Also:

History: Original release was in V14.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_RULE_create_rule(
tag_t object_in_part ,/* <I>
                      Tag of the object in the same part to
                      create the new rule object. (May be a
                      part tag).
                      */
char * name ,/* <I>
             Name of the rule.
             */
char * description ,/* <I>
                    Description of the rule.
                    */
char * application ,/* <I>
                    Application of the rule.
                    */
tag_t check_function ,/* <I>
                      Tag of a design Rule Function.
                      */
tag_t * rule  /* <O>
              Tag of new rule.
              */
);

/**********************************************************************
Returns the name of a Design Rule.

Environment: Internal  and  External

See Also:

History: Original release was in V14.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_RULE_ask_rule_name(
tag_t rule ,/* <I>
            Tag of the rule to query.
            */
char ** name  /* <OF>
              Name of the rule.
              */
);

/**********************************************************************
Sets the name of a Design Rule.

Environment: Internal  and  External

See Also:

History: Original release was in V14.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_RULE_set_rule_name(
tag_t rule ,/* <I>
            Tag of the rule to modify.
            */
char * name  /* <I>
             New name of the rule.
             */
);

/**********************************************************************
Returns the description of a Design Rule.

Environment: Internal  and  External

See Also:

History: Original release was in V14.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_RULE_ask_rule_description(
tag_t rule ,/* <I>
            Tag of the rule to query.
            */
char ** description  /* <OF>
                     Description of the rule.
                     */
);

/**********************************************************************
Sets the description of a Design Rule.

Environment: Internal  and  External

See Also:

History: Original release was in V14.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_RULE_set_rule_description(
tag_t rule ,/* <I>
            Tag of the rule to modify.
            */
char * description  /* <I>
                    New description of the rule.
                    */
);

/**********************************************************************
Returns the application of a Design Rule.

Environment: Internal  and  External

See Also:

History: Original release was in V14.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_RULE_ask_rule_application(
tag_t rule ,/* <I>
            Tag of the rule to query.
            */
char ** application  /* <OF>
                     Application of the rule.
                     */
);

/**********************************************************************
Sets the application of a Design Rule.

Environment: Internal  and  External

See Also:

History: Original release was in V14.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_RULE_set_rule_application(
tag_t rule ,/* <I>
            Tag of the rule to query.
            */
char * application  /* <I>
                    New application for the rule.
                    */
);

/**********************************************************************
Returns the check function of a Design Rule.

Environment: Internal  and  External

See Also:

History: Original release was in V14.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_RULE_ask_rule_check_function(
tag_t rule ,/* <I>
            Tag of the rule to query.
            */
tag_t * check_function  /* <O>
                        Tag of function object.
                        */
);

/**********************************************************************
Sets the check function of a Design Rule.

Environment: Internal  and  External

See Also:

History: Original release was in V14.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_RULE_set_rule_check_function(
tag_t rule ,/* <I>
            Tag of the rule to modify.
            */
tag_t check_function  /* <I>
                      Tag of UF_RULE_function object.
                      */
);

/**********************************************************************
Returns the violations of a Design Rule.

Environment: Internal  and  External

See Also:

History: Original release was in V14.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_RULE_ask_rule_vios(
tag_t rule ,/* <I>
            Tag of the rule to query.
            */
int      * num_violations ,/* <O>
                       Number of violations returned.
                       */
tag_t ** violations  /* <OF,len:num_violations>
                     Violations array.  This array must be freed by
                     calling UF_free.
                     */
);

/**********************************************************************
Sets the violations of a Design Rule.

Environment: Internal  and  External

See Also:

History: Original release was in V14.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_RULE_add_rule_violations(
tag_t rule ,/* <I>
            Tag of the rule to modify.
            */
int num_violations ,/* <I>
                    Number of violations.
                    */
tag_t * violations  /* <I,len:num_violations>
                    Violations array.
                    */
);

/**********************************************************************
Set the violations of a rule

Environment: Internal  and  External

See Also:

History: Original release was in V14.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_RULE_set_rule_violations(
tag_t  rule,          /* <I>
                      Tag of rule to modify
                      */
int    num_violations,/* <I>
                      Number of violations
                      */
tag_t violations[] /* <I,len:num_violations>
                  Array of violations
                  */
);

/**********************************************************************
Returns the violations of a design rule since a particular date.

Environment: Internal  and  External

See Also:

History: Original release was in V14.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_RULE_ask_rule_vios_since(
tag_t rule ,/* <I>
            Tag of the rule to inquire.
            */
int since ,/* <I>
           Date (Number of seconds since Jan 1,
           1970 00:00:00 GMT).
           */
int      * num_violations ,/* <O>
                           Number of violations returned.
                           */
tag_t ** violations  /* <OF,len:num_violations>
                     Violations array.  This array must be freed by calling
                     UF_free.
                     */
);

/**********************************************************************
Checks a design rule. The violations are returned using the
time_stamps of the violations that have been created since the check
started. This is done so that the check function does not have to
allocate and return an array of the violations created.
However, the check function is responsible for creating the violation
and attaching the violation to the rule. Otherwise, the new violations
are not found.

Environment: Internal  and  External

See Also:

History: Original release was in V14.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_RULE_check_rule(
tag_t rule ,/* <I>
            Tag of the rule to check.
            */
void * data ,/* <I>
             Client data to be passed to
             check_function.
             */
int * num_violations ,/* <O>
                      Number of violations created.
                      */
tag_t ** violations  /* <OF,len:num_violations>
                     Violations created.  This array must be freed by
                     calling UF_free.
                     */
);

/**********************************************************************
Checks many design rules.

Environment: Internal  and  External

See Also:

History: Original release was in V14.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_RULE_check_rules(
int num_rules ,/* <I>
               Number of rules to check.
               */
tag_t * rules ,/* <I,len:num_rules>
               Array of rules to check.
               */
void * data ,/* <I>
             Client data to be passed to
             check_function.
             */
int * num_violations ,/* <O>
                      Number of violations created.
                      */
tag_t ** violations  /* <OF,len:num_violations>
                     Array of violations created.  This array must be freed
                     by calling UF_free.
                     */
);

/**********************************************************************
Creates a violation.

Environment: Internal  and  External

See Also:

History: Original release was in V14.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_RULE_create_violation(
tag_t object_in_part ,/* <I>
                      Tag of object in same part to create
                      violation object.  May be a part tag.  May
                      not be NULL_TAG.
                      */
char * short_description ,/* <I>
                          Terse description of violation.
                          */
char * long_description ,/* <I>
                         Verbose description of violation.
                         */
int num_objects ,/* <I>
                 Number of objects in the violation.
                 */
tag_t  objects[] ,/* <I,len:num_objects>
                 Objects in the violation.
                 */
int time_stamp ,/* <I>
                Date created : number of seconds since 1
                Jan 1970 00:00:00. Use
                UF_RULE_CURRENT_TIME_STAMP
                for current time.
                */
tag_t * violation  /* <O>
                   Tag of new violation object.
                   */
);

/**********************************************************************
Returns the short description of a violation.

Environment: Internal  and  External

See Also:

History: Original release was in V14.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_RULE_ask_vio_short_desc(
tag_t violation ,/* <I>
                 Tag of violation to inquire.
                 */
char ** short_desc  /* <OF>
                    Terse description of violation.
                    */
);

/**********************************************************************
Sets the short description of a violation.

Environment: Internal  and  External

See Also:

History: Original release was in V14.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_RULE_set_vio_short_desc(
tag_t violation ,/* <I>
                 Tag of violation to modify.
                 */
char * short_desc  /* <I>
                   Terse description of violation.
                   */
);

/**********************************************************************
Returns the long description of a violation.

Environment: Internal  and  External

See Also:

History: Original release was in V14.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_RULE_ask_vio_long_desc(
tag_t violation ,/* <I>
                 Tag of violation to query.
                 */
char ** long_desc  /* <OF>
                   Verbose description of violation.
                   */
);

/**********************************************************************
Sets the long description of a violation.

Environment: Internal  and  External

See Also:

History: Original release was in V14.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_RULE_set_vio_long_desc(
tag_t violation ,/* <I>
                 Tag of violation to modify.
                 */
char * long_desc  /* <I>
                  Verbose description of violation.
                  */
);

/**********************************************************************
Adds objects to a violation.

Environment: Internal  and  External

See Also:

History: Original release was in V14.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_RULE_add_violation_objects(
tag_t violation ,/* <I>
                 Tag of violation to modify.
                 */
int num_objects ,/* <I>
                 Number of objects to add.
                 */
tag_t * objects  /* <I,len:num_objects>
                 Array of added objects.
                 */
);

/**********************************************************************
Returns the objects of a violation.

Environment: Internal  and  External

See Also:

History: Original release was in V14.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_RULE_ask_vio_objects(
tag_t violation ,/* <I>
                 Tag of violation to inquire.
                 */
int      * num_objects ,/* <O>
                    Number of objects to returned.
                    */
tag_t ** objects  /* <OF,len:num_objects>
                  Array of objects.  This array must be freed by calling
                  UF_free.
                  */
);

/**********************************************************************
Sets the objects of a violation.

Environment: Internal  and  External

See Also:

History: Original release was in V14.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_RULE_set_vio_objects(
tag_t violation ,/* <I>
                 Tag of violation to modify.
                 */
int num_objects ,/* <I>
                 Number of objects.
                 */
tag_t  objects[]  /* <I,len:num_objects>
                 Array of objects.
                 */
);

/**********************************************************************
Inquire the violations which include this object

Environment: Internal  and  External

See Also:

History: Original release was in V14.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_RULE_ask_object_violations(
tag_t   object,        /* <I>
                       The object to inquire
                       */
int    *num_violations,/* <O>
                       The number of violations returned
                       */
tag_t **violations /* <OF,len:num_violations>
                   The array of violations.  This must be freed by calling
                   UF_free.
                   */
);


/**********************************************************************
Returns the override of a violation.

Environment: Internal  and  External

See Also:

History: Original release was in V14.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_RULE_ask_vio_override(
tag_t violation ,/* <I>
                 Tag of violation to inquire.
                 */
tag_t * override  /* <O>
                  Tag of override object.
                  */
);

/**********************************************************************
Sets the override of a violation.

Environment: Internal  and  External

See Also:

History: Original release was in V14.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_RULE_set_vio_override(
tag_t violation ,/* <I>
                 Tag of violation to modify.
                 */
tag_t override  /* <I>
                Tag of override object.
                */
);

/**********************************************************************
Asks if the violation is overridden.

Return:
         TRUE or FALSE.

Environment: Internal  and  External

See Also:

History:
 ***********************************************************************/
extern UFUNEXPORT logical UF_RULE_is_violation_overridden(
tag_t violation  /* <I>
                 Tag of violation to inquire.
                 */
);/* <NEC> */

/**********************************************************************
Returns the time_stamp of a violation.

Environment: Internal  and  External

See Also:

History: Original release was in V14.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_RULE_ask_vio_time_stamp(
tag_t violation ,/* <I>
                 Tag of violation to inquire.
                 */
int      * time_stamp  /* <O>
                   Time in seconds since Jan 1, 1970
                   00:00:00 GMT.
                   */
);

/**********************************************************************
Sets the time_stamp of a violation.

Environment: Internal  and  External

See Also:

History: Original release was in V14.0.

 ***********************************************************************/
extern UFUNEXPORT int UF_RULE_set_vio_time_stamp(
tag_t violation ,/* <I>
                 Tag of violation to inquire.
                 */
int time_stamp  /* <I>
                Time in seconds since Jan 1, 1970
                00:00:00 GMT. Use
                UF_RULE_CURRENT_TIME_STAMP
                for current time.
                */
);

/**********************************************************************
Returns the rule of a violation.

Environment: Internal  and  External

See Also:

History: Original release was in V14.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_RULE_ask_vio_rule(
tag_t violation ,/* <I>
                 Tag of violation to inquire.
                 */
tag_t * rule  /* <O>
              Tag of rule.
              */
);

/**********************************************************************
Asks if the violation was created since the given date/time.

Return:
         TRUE  - Created After
         FALSE - Create on or before.

Environment: Internal  and  External

See Also:

History: Original release was in V14.0.
 ***********************************************************************/
extern UFUNEXPORT logical UF_RULE_is_violation_since(
tag_t violation ,/* <I>
                 Tag of violation to inquire.
                 */
int since  /* <I>
           Time in seconds since Jan 1, 1970
           00:00:00 GMT.
           */
);/* <NEC> */

/**********************************************************************
Creates an override object.

Environment: Internal  and  External

See Also:

History: Original release was in V14.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_RULE_create_override(
tag_t object_in_part ,/* <I>
                      Tag of object in same part to create
                      override.
                      */
char * user ,/* <I>
             Name of user.
             */
char * reason ,/* <I>
               Reason for the override taking place
               */
int time_stamp ,/* <I>
                Time in seconds since Jan 1, 1970
                00:00:00 GMT.
                */
tag_t * override  /* <O>
                  Tag of new override object
                  */
);

/**********************************************************************
Sets the user of an override

Environment: Internal  and  External

See Also:

History: Original release was in V14.0
 ***********************************************************************/
extern UFUNEXPORT int UF_RULE_ask_override_user(
tag_t  override, /* <I>
                 Tag of override to modify.
                 */
char **user   /* <OF>
              New user.
              */
);

/**********************************************************************
Sets the user of an override

Environment: Internal  and  External

See Also:

History: Original release was in V14.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_RULE_set_override_user(
tag_t override ,/* <I>
                Tag of override to modify.
                */
char * user  /* <I>
             New user.
             */
);

/**********************************************************************
Returns the reason of an override.

Environment: Internal  and  External

See Also:

History: Original release was in V14.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_RULE_ask_override_reason(
tag_t override ,/* <I>
                Tag of override to inquire.
                */
char ** reason  /* <OF>
                Reason for override (May have carriage returns).
                */
);

/**********************************************************************
Sets the reason of an override.

Environment: Internal  and  External

See Also:

History: Original release was in V14.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_RULE_set_override_reason(
tag_t override ,/* <I>
                Tag of override to modify.
                */
char * reason  /* <I>
               Reason for override.
               */
);

/**********************************************************************
Returns the time stamp of an override.

Environment: Internal  and  External

See Also:

History: Original release was in V14.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_RULE_ask_override_time_stamp(
tag_t override ,/* <I>
                Tag of override to inquire.
                */
int      * time_stamp  /* <O>
                       Date/Time.
                       */
);

/**********************************************************************
Sets the time stamp of an override.

Environment: Internal  and  External

See Also:

History:
 ***********************************************************************/
extern UFUNEXPORT int UF_RULE_set_override_time_stamp(
tag_t override ,/* <I>
                Tag of override to modify.
                */
int time_stamp  /* <I>
                Date/Time.
                */
);

/**********************************************************************
Returns the violations overridden by an override.

Environment: Internal  and  External

See Also:

History: Original release was in V14.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_RULE_ask_override_violations(
tag_t override ,/* <I>
                Tag of override to inquire.
                */
int      * num_violations ,/* <O>
                       Number of violations.
                       */
tag_t ** violations  /* <OF,len:num_violations>
                     Array of violations.  This array must be freed by
                     calling UF_free.
                     */
);

/**********************************************************************
Creates a function.

Environment: Internal  and  External

See Also:

History: Original release was in V14.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_RULE_create_function(
tag_t object_in_part ,/* <I>
                      Tag of object in same part to create function.
                      */
char * name ,/* <I>
             Name of function.
             */
char * library ,/* <I>
                Name of shared library / image.
                */
tag_t * function  /* <O>
                  Tag of new function.
                  */
);

/**********************************************************************
Returns the name of a function.

Environment: Internal  and  External

See Also:

History: Original release was in V14.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_RULE_ask_function_name(
tag_t function ,/* <I>
                Tag of function to inquire.
                */
char ** name  /* <OF>
              Name of function.
              */
);

/**********************************************************************
Sets the name of a function.

Environment: Internal  and  External

See Also:

History: Original release was in V14.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_RULE_set_function_name(
tag_t function ,/* <I>
                Tag of function to modify.
                */
char * name  /* <I>
             New name of function.
             */
);

/**********************************************************************
Returns the library of a function.

Environment: Internal  and  External

See Also:

History: Original release was in V14.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_RULE_ask_function_library(
tag_t function ,/* <I>
                Tag of function to inquire.
                */
char ** library  /* <OF>
                 Shared Library / Image.
                 */
);

/**********************************************************************
Sets the library of a function.

Environment: Internal  and  External

See Also:

History: Original release was in V14.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_RULE_set_function_library(
tag_t function ,/* <I>
                Tag of function to modify.
                */
char * library  /* <I>
                Shared Library / Image.
                */
);

/**********************************************************************
Returns the pointer to the actual function associated with a rule. This
is the address of the C function which should be invoked, e.g.,

(*func) ( rule, data );

NULL is returned for "func" if there is no function for this rule

Returns:
         ERROR_OK or error code

Environment: Internal  and  External

See Also:

History: Original release was in V14.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_RULE_resolve_function(
tag_t function,  /* <I>
                Tag of function.
                */
UF_RULE_check_function_f_t *func  /* <O>
                                  Address of the actual function to be invoked
                                  */
);

/**********************************************************************
Returns the rules of a function.

Environment: Internal  and  External

See Also:

History:
 ***********************************************************************/
extern UFUNEXPORT int UF_RULE_ask_function_rules(
tag_t function ,/* <I>
                Tag of function to inquire.
                */
int      * num_rules ,/* <O>
                  Number of rules returned.
                  */
tag_t ** rules  /* <OF,len:num_rules>
                Array of rules.  This array must be freed by calling UF_free.
                */
);

/**********************************************************************
Finds the violation of the given rule by the given object. If there is none,
a new violation is created. If the violation is updated, only the short and
long descriptions are updated.

Environment: Internal  and  External

See Also:

History: Original release was in V14.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_RULE_create_or_update_vio(
tag_t object ,/* <I>
              Tag of the object in violation
              */
tag_t rule ,/* <I>
            Tag of the rule which the object violates
            */
char * short_description ,/* <I>
                          Short description of the violation
                          */
char * long_description ,/* <I>
                         Long description of the violation
                         */
int num_objects ,/* <I>
                 Number of objects in violation
                 */
tag_t  objects[] ,/* <I,len:num_objects>
                 Tags of objects in violation
                 */
tag_t * violation  /* <O>
                 Tag of the violation
                 */
);

/**********************************************************************
FInds the violation of the given rule by the given object and deletes it.

Environment: Internal  and  External

See Also:

History: Original release was in V14.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_RULE_delete_vio_by_obj_rule(
tag_t object, /* <I>
              Tag of the object in violation
              */
tag_t rule /* <I>
           Tag of the rule which the object violates
           */
);

/**********************************************************************
FInds the violation of the given rule by the given object. If the given
object does not violate the rule, NULL_TAG is returned.

Environment: Internal  and  External

See Also:

History: Original release was in V14.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_RULE_find_vio_by_obj_rule(
tag_t object ,/* <I>
              Tag of the object in violation
              */
tag_t rule ,/* <I>
            Tag of the rule which the object violates
            */
tag_t * violation  /* <O>
                   Tag of the violation by the given object of the given rule
                   */
);

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif /* UF_RULE_H_INCLUDED */
