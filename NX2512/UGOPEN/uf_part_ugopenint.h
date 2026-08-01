/*******************************************************************************
           Copyright (c) 2000 Unigraphics Solutions Inc.
                       Unpublished - All Rights Reserved

 * 

File Description:

Open C API access to functions dealing with parts.
The subroutines in this section provide routines for parts. The parts
routines enable you to perform any of the interactive functions you
can perform within NX plus query routines.

Filename Lengths: Unless otherwise stated, filename lengths are limited
                  to UF_CFI_MAX_FILE_NAME_NCHARS characters which includes any
                  periods or extensions. This includes directory names and
                  part file names. Pathnames are limited to
                  MAX_FSPEC_NCHARS characters.  Valid characters
                  for a filename depend on the operating system.

Part Families:

The routines in this section enable you to:
  . Return the current part family instance save directory.
  . Return the part families in a part.
  . Return the object identifier of the part family instance within a part.
  . Create a new part containing an instance of a part family member.
  . Return the name of the part which contains the part family instance if the
    part can be found.
  . Query if a part contains a part family instance.
  . Query if a part family instance is up to date with respect to its template
    part.
  . Query if a part contains a part family.
  . Sets the current part family instance save directory.

Part History

The routines in this section enable you to:
  . create the history data structure object
  . fill in a history list object with the save history of the given part
  . return the number of save histories in the given history list object.
  . return the information about a particular save history from the given
    history list object.
  . delete (free) the given history list object
  . clear the history list

This section describes a set of routines that may be used to obtain
information about the save history of a loaded part.  The routines in
this set are:

UF_PART_create_history_list
UF_PART_ask_part_history
UF_PART_ask_num_histories
UF_PART_ask_nth_history
UF_PART_clear_history_list
UF_PART_delete_history_list

Save audit information is maintained for all V10 and later part files
and the "history" routines allow Open API access to this data.
The information maintained within the NX part file for each
"save" of a part includes: version number, time and date, machine
type on which the save was performed, user name of the "saver" of
the part, and program name of the program which performed the
save.

The history routines all make use of a pointer to a data structure
which is used to hold the save audit information.  In the routine
descriptions that follow, this structure is referred to as a "History List"
object.

This structure is created by the UF_PART_create_history_list routine,
filled in with data from the part file by the UF_PART_ask_part_history
routine, and interrogated for information on a particular "save" of the
part with the UF_PART_ask_num_histories and
UF_PART_ask_nth_history routines.

The UF_PART_delete_history_list routine is used to free the data
structures allocated by UF_PART_create_history_list and
UF_PART_ask_part_history.

The UF_PART_clear_history_list routine is used to clear the part
specific history information from a history list structure so that the
structure may be reused to obtain the history of a different part,
without having to delete the existing history list object and to create a
new one.  UF_PART_clear_history_list frees the storage associated
with the information obtained by UF_PART_ask_part_history.

NOTE:
The history list data object used by these routines is not a
normal NX object and can not be used by other Open
API routines.  Also note that it is a pointer to this object that is
returned by or supplied to the various Part History routines.

****************************************************************************/

#ifndef UF_PART_UGOPENINT_INCLUDED
#define UF_PART_UGOPENINT_INCLUDED

/***************************************************************************

  ***************************************************************************/

#include <uf_defs.h>
#include <libugopenint_exports.h>

#ifdef __cplusplus
extern "C" {
#endif

/*****************************************************************************
Adds a part to the top of the "recently opened parts" list used by the
NX user interface.  If the part already exists on the "recently opened
parts" list, it will be moved to the top of the list.

Environment: Internal

See Also:

History: Originally released in V17
 ******************************************************************************/
extern UGOPENINTEXPORT int UF_PART_add_to_recent_file_list (
tag_t part_tag  /* <I>
                tag of part to add to list
                */
);

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif /* UF_PART_UGOPENINT_INCLUDED */
