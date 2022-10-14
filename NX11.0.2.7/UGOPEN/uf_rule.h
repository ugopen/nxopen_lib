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

/*
*/
#ifndef UF_RULE_check_function_f_t_defined
#define UF_RULE_check_function_f_t_defined
typedef void *(*UF_RULE_check_function_f_t)( tag_t   rule,/* <I> Rule to check */
                                          void   *data /* <I> Client data */);
#endif


#ifdef __cplusplus
}
#endif

#include <uf_retiring.h>

#undef EXPORTLIBRARY

#endif /* UF_RULE_H_INCLUDED */
