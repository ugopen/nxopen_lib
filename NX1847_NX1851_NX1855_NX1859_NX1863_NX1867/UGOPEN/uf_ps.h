/*******************************************************************************

          Copyright (c) 1998-2000 Unigraphics Solutions Inc.
                   Unpublished - All rights reserved



File description: 

These functions provide the Open API programmer direct access to 
Parasolid information.

The Parasolid functions in this file enable you to:
  . Get the solid body object that corresponds to a given Parasolid tag.
  . Retrieve information pertaining to Parasolid journaling.
  . Get the Parasolid tag that corresponds to the given object in a file.
  . Create an NX tag from a Parasolid tag.
  . Create a Parasolid trimmed curve from a NX curve or edge object.
  . Export parasolid data.
  . Import parasolid data.
  . Enable and disable Parasolid journaling.
  . Write a specified character string to the Parasolid journal file.

*****************************************************************************/

#ifndef UF_PS_H_INCLUDED
#define UF_PS_H_INCLUDED


/***************************************************************************

  ***************************************************************************/

#include <uf_defs.h>
#include <libufun_exports.h>

#ifdef __cplusplus
extern "C" {
#endif

/* Used to return information about objects that could not be exported
   to a parasolid export file.
*/ 
struct UF_PS_unexported_s
{
   tag_t ug_body_tag;          /* NX tag of the unexported object. */
   int   fail_code;            /* Reason the tag was not exported.  */
};

typedef struct UF_PS_unexported_s UF_PS_unexported_t;

typedef int (*UF_PS_link_f_p_t)(
   tag_t       ug_tag, /* <I> */
   int         ps_tag /* <I> */);

struct UF_PS_kernel_version_s
{
   int major_revision;
   int minor_revision;
   int build_number;
   int year;
   int month;
   int day;
   int hour;
   int minute;
   int second;
};

typedef struct UF_PS_kernel_version_s   UF_PS_kernel_version_t;
typedef struct UF_PS_kernel_version_s  *UF_PS_kernel_version_p_t;

#define    UF_PS_DISABLED    0
#define    UF_PS_ENABLED     1
/*****************************************************************************
Import a Parasolid transmit file.  This file could have been
created from any application that uses Parasolid.

Environment: Internal  and  External
See Also:
History:
****************************************************************************/
extern UFUNEXPORT int UF_PS_import_data(
char * file_name ,/* <I>
                  File name to get data from
                  */
uf_list_p_t * body_list  /* <OF,free:UF_MODL_delete_list>
                         List of bodies that were imported.
                         This list must be freed with UF_MODL_delete_list.
                         */
);
/****************************************************************************
Creates a Parasolid transmit file. The bodies that are input into this routine
must be NX type 70 subtype 0.

Environment: Internal  and  External
See Also:
History:
***************************************************************************/
extern UFUNEXPORT int UF_PS_export_data(
uf_list_p_t body_list ,/* <I>
                       List of bodies to be exported
                       */
char * file_name  /* <I>
                  New File name to put output into. An error is
                  generated if the file you specify already exists.
                  If you specify a full pathname, then the Parasolid
                  transmit file will be created there. If you specify
                  a simple file name, the file will be created in the 
                  directory specified by the UGII_UGSOLIDS_TMP 
                  environment variable. If this environment variable is 
                  not defined, then the transmit file will placed in
                  the /tmp, /var/tmp or TMP directory.
                  */
);
/**************************************************************************
Retrieves information pertaining to Parasolid journaling. The
information that is currently returned through this command includes:
The current status of Parasolid journaling.

     When Parasolid journaling is enabled, each call to a
     Parasolid routine and the values returned from the routine
     are recorded in a  journal file. When Parasolid journaling is
     disabled, the calls to Parasolid routines are not recorded in
     the journal file.

The length of the Parasolid journal file name.
The name of the Parasolid journal file.

    If the -jou parameter is not specified when the command to
    initiate the NX session is entered, the Parasolid
    journal file is created with a default name. Utilizing the
    -jou parameter to specify a journal file name enables
    Parasolid journaling.

Return:
         Return code
          0 =  Requested information accessed
      not 0 = Unable to retrieve the requested information

Environment: Internal
See Also:  
History:
******************************************************************************/
extern UFUNEXPORT int UF_PS_ask_journal_data(
int * journal_state ,/* <O>
                     Current state of Parasolid journaling
                        UF_PS_DISABLED  =  Disabled
                        UF_PS_ENABLED  =   Enabled
                     */
char  journal_name[ MAX_FSPEC_BUFSIZE ]  /* <O,len:MAX_FSPEC_SIZE+1>
                                      Name of the Parasolid journal file.
                                      */
);
/*****************************************************************************
Enables and disables Parasolid journaling. When Parasolid
journaling is enabled, each call to a Parasolid routine and the values
returned from that call are recorded in a journal file. The Parasolid
journal file updates to record each Parasolid routine call until
journaling is disabled.  If Parasolid journaling is not enabled when the
NX session is terminated, the journal file is deleted.

Return:
         Return code
        0 = The  journaling state was updated
    not 0 = The journaling state was unable to be
                     updated

Environment: Internal
See Also: 
History:
******************************************************************************/
extern UFUNEXPORT int UF_PS_set_journal_state(
int journal_state  /* <I>
                   journaling state:
                   UF_PS_DISABLED = Disable journaling
                   UF_PS_ENABLED  = Enable journaling
                   */
);
/***************************************************************************
Writes a specified character string to the Parasolid journal file. The
character string is written out to the journal file in groups of 80
characters or until the null character is encountered. The character
string can be written out to the Parasolid journal file only if journaling
is enabled.  If Parasolid journaling is not enabled when the NX
session is terminated, the journal file is deleted and all of the data in the
file is lost.

Return:
         Return code
          0 = The character string was written to the
                   Parasolid journal file
      not 0 = Unable to write the character string to
                   the Parasolid journal file

Environment: Internal
See Also: 
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_PS_write_to_journal(
char * journal_commt  /* <I>
                      Character string to be written to the Parasolid
                      journal file
                      */
);

/***************************************************************************
Gets the NX object identifier that corresponds to a given
Parasolid tag.  The object identifier that is returned is always to the
prototype object.  If an object identifier is not found for the Parasolid
tag, a NULL_TAG is  returned.  This function is intended to be used by 
sites with direct access to the Parasolid solid modeler.
Return:
         Return code
        0 = Object identifier returned.
    not 0 = Unable to find the object identifier for the
            given Parasolid tag.

Environment: Internal
See Also: 
History:
****************************************************************************/
extern UFUNEXPORT int UF_PS_ask_object_of_ps_tag (
tag_t ps_tag ,/* <I>
              The Parasolid tag to lookup 
              */
tag_t * obj_id  /* <O>
                The NX object identifier that corresponds
                to the input Parasolid tag.
                NULL_TAG =  Could not find an object
                identifier to correspond to the given Parasolid tag.
                */
);
/******************************************************************************
Gets the Parasolid tag that corresponds to the given object identifier.
This command accepts solid body, solid edge or solid face
object identifiers. When the object identifier refers to an object
occurrence, the Parasolid tag that corresponds to the prototype object
is returned. If a Parasolid tag is not found for the object identifier, a
NULL_TAG is returned.
NOTE:  This command is intended to be used by sites with direct
access to the Parasolid solid modeler.
Return:
         Return code
        0 = Parasolid tag returned.
    not 0 = Unable to return the Parasolid tag for the
                 given object identifier.

Environment: Internal  and  External
See Also: 
History:
****************************************************************************/
extern UFUNEXPORT int UF_PS_ask_ps_tag_of_object(
tag_t obj_id ,/* <I>
              The object identifier to lookup
              */
tag_t * ps_tag  /* <O>
                The Parasolid tag that corresponds to the input
                object identifier.
                NULL_TAG = Could not find a Parasolid tag
                to correspond to the given object identifier.
                */
);
/****************************************************************************
Creates an NX object from a Parasolid tag. The Parasolid tag must be
the tag of a Parasolid body. If a call is made directly to Parasolid to create 
a solid body and a Parasolid tag is received by the application, that tag is 
unknown to NX.  This routine can be used to embed the Parasolid body 
into the NX's data model.  The Parasolid object becomes part of 
NX's data model and the NX's tag identifying the new object 
is returned.

Return:
         Return code
        0 = Object identifier returned.
    not 0 = Unable to create a NX object from the
            given Parasolid tag.

Environment: Internal
See Also:
History:
****************************************************************************/
extern UFUNEXPORT int  UF_PS_create_obj_from_ps_tag (
tag_t ps_tag ,/* <I>
              The Parasolid tag of a Parasolid body
              */
tag_t * ug_tag  /* <O>
                NX tag for Parasolid body
                */
);
/***************************************************************************
Creates a Parasolid trimmed curve from an NX curve or edge object.
The input entity is not affected by this routine.

Environment: Internal  and  External
See Also: 
History: Original release was in V14.0.
****************************************************************************/
extern UFUNEXPORT int UF_PS_create_ps_trimmed_curve(
tag_t curve_or_edge ,/* <I>
                     Tag of an NX curve or edge entity
                     */
tag_t *ps_curve  /* <O>
                 Tag of the Parasolid trimmed curve
                 */
);

/***************************************************************************
Creates a Parasolid partition and sets it as the current partition.
A partition is an area within Parasolid where geometry can be created 
and deleted.  This function is only useful for a site with access to 
the Parasolid Solid Modeler.  NX usually creates a new partition 
for each solid body that is created.  Boolean operations are not allowed on 
bodies in different partitions.

Environment: Internal  and  External
See Also:
History: Original release was in V15.0.
****************************************************************************/
extern UFUNEXPORT int UF_PS_create_partition
(
    tag_t *partition /* <O>
                     Tag of the new Parasolid partition
                     */
);

/***************************************************************************
Return the current Parasolid partition.  A partition is an area within 
Parasolid where geometry can be created and deleted.  This function
is only useful for a site with access to the Parasolid Solid Modeler.
NX usually creates a new partition for each solid body that
is created.  Boolean operations are not allowed on bodies in different
partitions.

Environment: Internal  and  External
See Also:
History: Original release was in V15.0.
****************************************************************************/
extern UFUNEXPORT int UF_PS_ask_current_partition
(
    tag_t *partition /* <O>
                     Tag of the current Parasolid partition
                     */
);

/***************************************************************************
Sets the current Parasolid partition.  A partition is an area within 
Parasolid where geometry can be created and deleted.  This function
is only useful for a site with access to the Parasolid Solid Modeler.
NX usually creates a new partition for each solid body that
is created.  Boolean operations are not allowed on bodies in different
partitions.

Environment: Internal  and  External
See Also:
History: Original release was in V15.0.
****************************************************************************/
extern UFUNEXPORT int UF_PS_set_current_partition
(
    tag_t partition /* <I>
                     This Tag will be made the current Parasolid partition
                     */
);

/***************************************************************************
Returns the Parasolid partition that a Parasolid object resides in.  
This function is only useful for a site with access to the Parasolid Solid 
Modeler.  

Environment: Internal  and  External
See Also:
History: Original release was in V15.0.
****************************************************************************/
extern UFUNEXPORT int UF_PS_ask_entity_partition
(
    tag_t entity,    /* <I>
                        Tag of the parasolid entity
                     */
    tag_t *partition /* <O>
                     Tag of the Parasolid partition
                     */
);

/******************************************************************************
User Function routine to export parasolid data and include attributes
on the tags to link those tags to specific NX objects.

Environment: Internal  and  External
See Also:
History: Original release was in V16.0.
 ******************************************************************************/
extern UFUNEXPORT int UF_PS_export_linked_data(
   tag_p_t            tags,                  /* <I,len:n_tags>  
                                             Array of tags to export. Valid objects
                                             are NX solid bodies and NX curves.
                                             NX curves are exported as Parasolid 
                                             wire bodies.
                                             
                                             */
   int                n_tags,                /* <I>
                                             Count of tags in array.    
                                             */
   char               *file_name,            /* <I> 
                                             File name to put output into.
                                             This file must not exist.  The
                                             routine will return an error code
                                             if the file does exist.
                                             */
   int                version,               /* <I>
                                             Version number of Parasolid
                                             If non-zero, specifies the 
                                             desired version of Parasolid 
                                             for the transmit file. "250" 
                                             is version 25.0, "261" is version
                                             26.1 etc. It may not be possible
                                             to go back to every previous 
                                             version of Parasolid. If zero, 
                                             then the current version is 
                                             used.
                                                */
   UF_PS_link_f_p_t   link_fnc,              /* <I>
                                             Reserved for Licensed Parasolid
                                             Developers. Please use NULL 
                                             otherwise.

                                             Link attribute filter. 

                                             This is an integer function of
                                             the form: 

                                               int linkfn(tag_t  ug_tag,
                                                          int    ps_tag );

                                             The provided function will be
                                             called for all the curves,
                                             bodies, edges and faces being 
                                             exported. Objects of other types 
                                             will be ignored. "ug_tag" is
                                             the NX tag of the object, and 
                                             "ps_tag" is its corresponding
                                             Parasolid tag. 
                                             
                                             Currently, the integer status 
                                             returned is not used by NX. 

                                             This allows the user to define 
                                             a function to add user defined
                                             Parasolid attributes to the 
                                             ps_tag. These attributes are 
                                             stored in the transmit file and 
                                             can be interpreted later when the 
                                             file is imported. This is a way
                                             for users to add their own
                                             personalized information to 
                                             Parasolid objects.  

                                             */
   int                *n_unexported,         /* <O>
                                             Count of tags not exported. 
                                             */
   UF_PS_unexported_t **unexported_tags      /* <OF,len:n_unexported>
                                             If a NULL is passed in, then no
                                             information will be returned.  If
                                             the caller passes in a
                                             UF_PS_unexported_t *, then an array
                                             of UF_PS_unexported_t structures
                                             will be allocated containing the 
                                             tags of the bodies that were not
                                             exported, and the reasons (fail 
                                             code).  The caller must free this 
                                             array by calling UF_free.
                                             */
);


/******************************************************************************
User Function routine to determine the highest parasolid tag being used in the 
current session

Environment: Internal  and  External
See Also:
History: Original release was in V18.0.4
 ******************************************************************************/
extern UFUNEXPORT int UF_PS_ask_current_highest_tag( 
                      tag_t    *highest_tag       /* <O>
                                                     The highest parasolid 
                                                     being used in the current
                                                     session
                                                     */
);
 



/******************************************************************************
This function will return the number of parasolid tags that are available in the
current session

Environment: Internal  and  External
See Also:
History: Original release was in V18.0.4
 ******************************************************************************/
extern UFUNEXPORT int UF_PS_ask_tags_remaining( 
                     int      *tags_remaining   /* <O>
                                                   The number of parasolid tags 
                                                   that are available in the 
                                                   current session
                                                */
);

/******************************************************************************
 Returns information about the version of the parasolid kernel currently
 running.

 Environment: Internal and External
 See Also:
 History: Original release NX2.0
******************************************************************************/
extern UFUNEXPORT int UF_PS_ask_kernel_version
(
   UF_PS_kernel_version_t *version_data /* <I> - Pointer to a validly allocated
                                         *       UF_PS_kernel_version_t
                                         *       The results reside in that
                                         *       structure after the call.
                                         */
);


/**********************************************************************/

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif     /* UF_PS_H_INCLUDED */
