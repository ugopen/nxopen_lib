/*******************************************************************************
            Copyright (c) 1999-2000 Unigraphics Solutions, Inc.
                     Unpublished - All rights reserved
******************************************************************************



File description:

   The UF_NCGROUP module allows access to CAM UF_NCGROUPs. A CAM UF_NCGROUP is a
   collection of objects. Each object is either a UF_OPER object or a
   UF_NCGROUP object. This definition is intentionally recursive.

   The functions for dealing with UF_NCGROUPs allow for operations like asking
   for the members of a UF_NCGROUP, adding a new object to a UF_NCGROUP and
   asking of an object may be added to a UF_NCGROUP.

   A UF_SETUP contains 4 built-in UF_NCGROUPs: UF_NCGEOM, UF_NCMCT, UF_NCPROG,
   and UF_NCMTHD. The functions of UF_NCGROUP can be applied to all of these
   groups.

*******************************************************************************/
#ifndef UF_NCGROUP_H_INCLUDED
#define UF_NCGROUP_H_INCLUDED

/***************************** Include Files **********************************/
#include <uf_defs.h>
#include <uf_cam_errors.h>
#include <libufun_cam_exports.h>


#ifdef __cplusplus
extern "C" {
#endif


/******************************** Defines *************************************/
#define UF_NCGROUP_MAX_REASON_NCHARS 1024
#define UF_NCGROUP_MAX_REASON_BUFSIZE NX_BUFSIZE(UF_NCGROUP_MAX_REASON_NCHARS)

/*  */
#define UF_NCGROUP_MAX_REASON_LEN (UF_NCGROUP_MAX_REASON_BUFSIZE-1)
/*  */

/***************************** Public Typedefs ********************************/

/* The type for the callback function for cycling members of a group.
 * Input:
 *    tag - the tag of the member object currently being processed during the
 *          cycling
 *    data - the data passed to UF_NCGROUP_cycle_members
 * Return Value:
 *    TRUE - continue cycling
 *    FALSE - stop cycling
 */
typedef logical (*UF_NCGROUP_cycle_cb_f_t)(tag_t tag , /* <I> */ void *data /* <I> */);

enum UF_NCGROUP_position_e
{
   UF_NCGROUP_POSITION_BEFORE,   /* Insert before sibling */
   UF_NCGROUP_POSITION_AFTER     /* Insert after sibling */
};

typedef enum UF_NCGROUP_position_e UF_NCGROUP_position_t;

/************************* Public Function Definitions ************************/


/*******************************************************************************
 Given an object tag, this function reports if it is a UF_NCGROUP object.

Environment: Internal  and  External

See Also:

History: Originally released in V16.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_NCGROUP_is_group
(
   tag_t      obj_tag, /* <I> - the object being asked about */
   logical   *answer   /* <O> - TRUE if object is a UF_NCGROUP object, FALSE
                                otherwise */
);


/*******************************************************************************
 This function returns TRUE if the group 'obj1' can accept 'obj2' as a
 member. If the answer is FALSE the reason may be found in 'reason'.

Environment: Internal  and  External

See Also:

History: Originally released in V16.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_NCGROUP_can_accept_member
(
   tag_t      obj1,  /* <I> - the group */
   tag_t      obj2,  /* <I> - can this object be placed into the group */
   logical   *answer, /* <O> - see above */
   char       reason[UF_NCGROUP_MAX_REASON_BUFSIZE]  /* <O> - see above */
);


/*******************************************************************************
 This function returns the list of objects which are contained in the specified
 group.

Environment: Internal  and  External

See Also:

History: Originally released in V16.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_NCGROUP_ask_member_list
(
   tag_t    obj_tag, /* <I> - the group */
   int     *count,   /* <O> - the number of objects in the group */
   tag_t  **list     /* <OF,len:count> - the list of objects in the group.  This should
                        be freed by calling UF_free. */
);


/*******************************************************************************
 This function returns TRUE if object 'member' is part of the group 'group'.
 If the answer is TRUE then 'index' is the index of 'member' in group. The
 index is the position of 'member' in the group's member list. Indices go
 from 0 to n-1 where n is the number of objects in the member list.

Environment: Internal  and  External

See Also:

History: Originally released in V16.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_NCGROUP_is_a_member
(
   tag_t      group, /* <I> - see above */
   tag_t      member, /* <I> - see above */
   logical   *answer, /* <O> - see above */
   int       *index   /* <O> - see above */
);


/*******************************************************************************
 This function adds 'member' to the member list of 'parent'. It will become
 the last object in the member list. If 'parent' can not accept 'member' as
 a member and error will be returned.

Environment: Internal  and  External

See Also:

History: Originally released in V16.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_NCGROUP_accept_member
(
   tag_t   parent, /* <I> - see above */
   tag_t   member  /* <I> - see above */
);


/*******************************************************************************
 This function adds 'member' to the member list of 'parent'. If 'sibling' is
 NULL then add 'member' as the last member of 'parent's member list. If
 'sibling' is not NULL then if 'where' is UF_NCGROUP_POSITION_BEFORE it adds
 'member' to 'parent's member list immediately before 'sibling'.
 If 'sibling' is not NULL then if 'where' is UF_NCGROUP_POSITION_AFTER it adds
 'member' to 'parent's member list immediately after 'sibling'.

Environment: Internal  and  External

See Also:

History: Originally released in V16.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_NCGROUP_insert_member
(
   tag_t   parent, /* <I> - see above */
   tag_t   member, /* <I> - see above */
   tag_t   sibling, /* <I> - see above */
   UF_NCGROUP_position_t   where /* <I> - see above */
);


/*******************************************************************************
 This function returns the object which is the 'index'th member of 'parent's
 member list. The object is returned in 'member'.

Environment: Internal  and  External

See Also:

History: Originally released in V16.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_NCGROUP_ask_member_in_list
(
   tag_t    parent, /* <I> - see above */
   int      index,  /* <I> - see above */
   tag_t   *member  /* <O> - see above */
);


/*******************************************************************************
 This function iterates the members of group 'group'. For every object which
 is a member of 'group's member list it makes the call:

                  continue = cb( tag of member object, data );

 See the documentation for UF_NCGROUP_cycle_cb_f_t in this file for more
 information on the callback 'cb'.

Environment: Internal  and  External

See Also:

History: Originally released in V16.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_NCGROUP_cycle_members
(
   tag_t                     group, /* <I> - see above */
   UF_NCGROUP_cycle_cb_f_t   cb,    /* <I> - see above */
   void                     *data   /* <I> - see above */
);


/*******************************************************************************
 This function searches the member list of 'obj_tag' for an object with name
 'name'. If one is found, it's tag is returned in 'obj_with_name'. If no such
 object is found then NULL is returned in 'obj_with_name'.

Environment: Internal  and  External

See Also:

History: Originally released in V16.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_NCGROUP_ask_object_of_name
(
   tag_t    obj_tag, /* <I> - see above */
   char    *name,    /* <I> - see above */
   tag_t   *obj_with_name /* <O> - see above */
);


/*******************************************************************************
 For the group 'obj_tag' this function returns the tag of the object which
 is the root object of it's view. This will be either a UF_NCGEOM, UF_NCPROG,
 UF_NCMCT or UF_MCMTHD object.

Environment: Internal  and  External

See Also:

History: Originally released in V16.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_NCGROUP_ask_root_of_object
(
   tag_t    obj_tag, /* <I> - see above */
   tag_t   *root_tag /* <O> - see above */
);


/*******************************************************************************
 Create a new UF_NCGROUP object which is a UF_NCPROG Group object.

Environment: Internal  and  External

See Also:

History: Originally released in V16.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_NCPROG_create
(
   char    *type_name,    /* <I> - the type name of the object to create */
   char    *subtype_name, /* <I> - the subtype name of the object to create */
   tag_t   *new_object    /* <O> - the newly created object */
);


/*******************************************************************************
 Create a new UF_NCGROUP object which is a UF_NCGEOM Group object.

Environment: Internal  and  External

See Also:

History: Originally released in V16.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_NCGEOM_create
(
   char    *type_name,    /* <I> - the type name of the object to create */
   char    *subtype_name, /* <I> - the subtype name of the object to create */
   tag_t   *new_object    /* <O> - the newly created object */
);


/*******************************************************************************
 Create a new UF_NCGROUP object which is a UF_NCMTHD Group object.

Environment: Internal  and  External

See Also:

History: Originally released in V16.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_NCMTHD_create
(
   char    *type_name,    /* <I> - the type name of the object to create */
   char    *subtype_name, /* <I> - the subtype name of the object to create */
   tag_t   *new_object    /* <O> - the newly created object */
);


#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif /* UF_NCGROUP_H_INCLUDED */
